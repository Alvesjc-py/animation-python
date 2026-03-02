import sys
import time


def typing_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


if __name__ == '__main__':
    # Example usage:
    typing_effect("Bem-vindo ao efeito de digitação estilo PC antigo!", delay=0.05)