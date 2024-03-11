import sys
import os

# Define explicitamente o diretório raiz do projeto
sys.path.append('/workplace/')

from app.interfaces.interface_openai import create_thread
from app.data.threads_manager import retrieve_user_name, retrieve_thread_id, upsert_thread
from app.decorators.log_decorator import log_function_call

"""
Message Routing Manager

Este arquivo é crucial para a gestão das conversas entre os usuários e a API da OpenAI, proporcionando uma experiência de conversação personalizada. Ele faz isso associando um nome de usuário a um Thread ID específico, o que permite a continuidade das conversas e a manutenção do contexto ao longo do tempo. Este gerenciamento facilita interações mais naturais e engajadas com o sistema, aprimorando significativamente a experiência do usuário.

Ao utilizar o módulo `threads_manager` para operações de dados, este arquivo abstrai a complexidade do gerenciamento direto do banco de dados `shelve`, promovendo um código mais limpo, modular e reutilizável. A integração com a API da OpenAI é otimizada ao manter um registro persistente dos threads de cada usuário, o que é fundamental para customizar respostas e manter um fluxo de diálogo coerente.

Referências:
- Documentação da OpenAI para gestão de threads e mensagens: https://platform.openai.com/docs/guides/conversation
- Documentação do Python `shelve` para persistência de dados simples: https://docs.python.org/3/library/shelve.html
"""


@log_function_call
def get_or_create_thread(user_name):
    # Verificar se o nome de usuário já possui um thread_id
    thread_id = check_if_thread_exists(user_name)
    if thread_id is None:
        # Se não possuir, criar um novo thread_id
        thread = create_thread()  # Recebendo o objeto diretamente
        thread_id = thread.id  # Acessando o id do objeto thread
        # Armazenar o novo thread_id com o nome de usuário no banco de dados
        store_thread(user_name, thread_id)
    return thread_id


@log_function_call
def check_if_thread_exists(user_name: str):
    """
    Verifica a existência de um thread associado a um nome de usuário específico.

    Ao buscar no banco de dados `shelve`, esta função determina se um determinado usuário já iniciou uma conversa e possui um Thread ID associado. Isso é essencial para assegurar que as conversas possam ser continuadas de onde pararam, sem a necessidade de reiniciar o contexto em cada interação.

    Parâmetros:
        user_name (str): O nome do usuário cuja existência do thread está sendo verificada.

    Retorna:
        str or None: Retorna o ID do thread se o usuário especificado possui um thread associado; caso contrário, retorna None.

    Exemplo de Uso:
        existent_thread_id = check_if_thread_exists("Cícero")
        if existent_thread_id:
            print(f"Encontrado thread existente para Cícero: {existent_thread_id}")
        else:
            print("Nenhum thread encontrado para Cícero.")
    """
    return retrieve_thread_id(user_name)

@log_function_call
def check_if_user_name_exists(thread_id: str):
    """
    Verifica se existe um nome de usuário associado a um ID de thread específico.

    Esta operação é inversa à função `check_if_thread_exists`, buscando no banco de dados `shelve` por um nome de usuário vinculado a um dado Thread ID. Isso permite identificar a quem pertence uma determinada conversa, facilitando a gestão e personalização das interações.

    Parâmetros:
        thread_id (str): O ID do thread cujo nome do usuário associado está sendo procurado.

    Retorna:
        str or None: Retorna o nome do usuário associado ao Thread ID especificado; se não houver associação, retorna None.

    Exemplo de Uso:
        user_name = check_if_user_name_exists("ABC123")
        if user_name:
            print(f"Nome de usuário associado ao ID do thread ABC123: {user_name}")
        else:
            print("Nenhum nome de usuário associado ao ID do thread ABC123 encontrado.")
    """
    return retrieve_user_name(thread_id)

@log_function_call
def store_thread(user_name: str, thread_id: str):
    """
    Armazena ou atualiza a associação entre um nome de usuário e um ID de thread.

    Utilizando o módulo `threads_manager`, essa função insere um novo mapeamento ou atualiza um existente entre um nome de usuário e seu Thread ID correspondente no banco de dados `shelve`. Isso é crucial para rastrear as conversas em andamento, permitindo retomá-las com precisão em futuras interações.

    Parâmetros:
        user_name (str): O nome do usuário envolvido na conversa.
        thread_id (str): O ID do thread associado à conversa do usuário.

    Retorna:
        str: Retorna o status da inserção..

    Exemplo de Uso:
        store_thread("Genivaldo", "thread_789")
        print("Thread armazenado com sucesso para Genivaldo.")
    """
    return upsert_thread(user_name, thread_id)
