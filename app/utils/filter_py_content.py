import sys
import re

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        inside_docstring = False
        for line in lines:
            # stripped_line = line.strip()
            # # Ignora linhas vazias e comentários
            # if not stripped_line or stripped_line.startswith("#"):
            #     continue

            # # Checa por início ou fim de docstrings
            # if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            #     inside_docstring = not inside_docstring
            #     continue

            # if not inside_docstring:
                new_lines.append(line)

        # Exibe as linhas filtradas
        print(''.join(new_lines).strip())

    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")

if __name__ == "__main__":
    main(sys.argv[1])
