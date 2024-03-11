#!/bin/bash
# Esse arquivo apenas faz uma listagem da estrutura do projeto e com a ajuda do arquivo filter_py_content.py tira os comentarios dos arquivos, 
# gerando um arquivo de texto com todas essas informações.

PROJECT_ROOT="~/codexhash/Docker/interface_openai"
cd "$(eval echo ${PROJECT_ROOT})" || exit

{
    find . -mindepth 1 \
    -not -path '*/__pycache__*' \
    -not -name '__init__.py' \
    -not -name '*.cpython-*.pyc' \
    -not -path '*/  PROJETO ANTIGO/*' \
    -not -name '  PROJETO ANTIGO' \
    -not -path '*/.git/*' \
    -not -name '.git' \
    -print | grep -vE '__pycache__|__init__.py|.cpython-[0-9]+.pyc'

    echo "========================================"
    echo "Conteúdo dos arquivos Python (.py):"
    echo "========================================"

    find . -type f -name "*.py" -not -name '__init__.py' -print0 | while IFS= read -r -d $'\0' file; do
        echo "---------- Início de $file ----------"
        python3 app/utils/filter_py_content.py "$file"
        echo "----------- Fim de $file -----------"
        echo
    done
} > estrutura_e_conteudo.txt
