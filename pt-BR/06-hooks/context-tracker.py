#!/usr/bin/env python3
# i18n-source: 06-hooks/context-tracker.py
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
"""
Rastreador de Uso de Contexto - Rastreia o consumo de tokens por requisição.

Usa UserPromptSubmit como hook "pré-mensagem" e Stop como hook "pós-resposta"
para calcular o delta no uso de tokens de cada requisição.

Esta versão usa estimativa baseada em caracteres (sem dependências).
Para maior precisão, veja context-tracker-tiktoken.py.

Uso:
    Configure ambos os hooks para usar o mesmo script:
    - UserPromptSubmit: salva a contagem atual de tokens
    - Stop: calcula o delta e reporta o uso
"""
import json
import os
import sys
import tempfile

# Configuração
CONTEXT_LIMIT = 128000  # Janela de contexto do Claude (ajuste para o seu modelo)


def get_state_file(session_id: str) -> str:
    """Retorna o caminho do arquivo temporário para armazenar a contagem de tokens pré-mensagem, isolado por sessão."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens_estimate(text: str) -> int:
    """
    Estima a contagem de tokens usando aproximação por caracteres.

    Usa a proporção de ~4 caracteres por token, que fornece ~80-90% de precisão
    para texto em inglês. Menos preciso para código e texto em outros idiomas.
    """
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Lê e concatena todo o conteúdo do arquivo de transcrição."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Extrai conteúdo de texto de vários formatos de mensagem
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Hook pré-mensagem: salva a contagem atual de tokens antes da requisição."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens_estimate(transcript_content)

    # Salva em arquivo temporário para comparação posterior
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Hook pós-resposta: calcula e reporta o delta de tokens."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens_estimate(transcript_content)

    # Carrega contagem pré-mensagem
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Calcula delta
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Reporta uso (stderr para não interferir com a saída do hook)
    print(
        f"Contexto (estimado): ~{current_tokens:,} tokens "
        f"({percentage:.1f}% usado, ~{remaining:,} restantes)",
        file=sys.stderr,
    )
    if delta_tokens > 0:
        print(f"Esta requisição: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
