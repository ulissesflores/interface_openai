import shelve
import os
import sys
sys.path.append('/workplace/')
from app.decorators.log_decorator import log_function_call

# Define o caminho para o arquivo do banco de dados threads.db
DB_PATH = os.path.join(os.path.dirname(__file__), 'threads')

@log_function_call
def retrieve_thread_id(user_name: str):
    """
    Recupera o ID do thread associado a um nome de usuário específico.

    Esta função busca no banco de dados 'shelve' pelo thread ID correspondente ao nome de usuário fornecido.
    É útil para recuperar o estado da conversa de um usuário específico, permitindo que a aplicação continue
    interações passadas sem perder o contexto.

    Parâmetros:
        user_name (str): O nome do usuário cujo thread ID está sendo buscado.

    Retorna:
        str or None: O ID do thread associado ao nome do usuário, se encontrado; caso contrário, retorna None.

    Exemplo de Uso:
        thread_id = retrieve_thread_id("Cícero")
        if thread_id:
            print(f"O ID do thread para Cícero é: {thread_id}")
        else:
            print("Nenhum thread encontrado para Cícero.")
    """
    with shelve.open(DB_PATH, 'r') as db:
        return db.get(user_name)

@log_function_call
def retrieve_user_name(thread_id: str):
    """
    Recupera o nome do usuário associado a um ID de thread específico.

    Dado um ID de thread, esta função varre o banco de dados 'shelve' em busca do nome de usuário correspondente.
    Isso é particularmente útil para identificar o participante de uma conversa quando conhecemos apenas o ID
    do thread, facilitando a gestão de interações múltiplas e contextuais.

    Parâmetros:
        thread_id (str): O ID do thread cujo nome do usuário está sendo buscado.

    Retorna:
        str or None: O nome do usuário associado ao ID do thread fornecido, se encontrado; caso contrário, retorna None.

    Exemplo de Uso:
        user_name = retornar_user_name("XYZ123")
        if user_name:
            print(f"O nome do usuário associado ao ID do thread XYZ123 é: {user_name}")
        else:
            print("Nenhum usuário encontrado para o ID do thread XYZ123.")
    """
    with shelve.open(DB_PATH, 'r') as db:
        for key, value in db.items():
            if value == thread_id:
                return key
    return None

# Exemplos de uso das funções
# print("Buscando o ID do thread para o usuário 'Cícero':")
# thread_id = retrieve_thread_id("Cícero")
# if thread_id:
#     print(f"O ID do thread para Cícero é: {thread_id}")
# else:
#     print("Nenhum thread encontrado para Cícero.")

# print("\nBuscando o nome do usuário para o thread ID 'ABC123':")
# user_name = retrieve_user_name("ABC123")
# if user_name:
#     print(f"O nome do usuário associado ao ID do thread ABC123 é: {user_name}")
# else:
#     print("Nenhum usuário encontrado para o ID do thread ABC123.")


@log_function_call
def print_shelve_contents():
    """
    Imprime o conteúdo do banco de dados shelve 'threads'.

    Esta função lê e exibe todos os registros armazenados no banco de dados shelve 'threads',
    fornecendo uma visão geral dos usuários armazenados e seus respectivos thread IDs.

    O propósito desta função é facilitar a verificação e o gerenciamento dos dados armazenados,
    permitindo que desenvolvedores e administradores visualizem rapidamente o mapeamento entre
    nomes de usuários e seus threads de comunicação.

    Exemplo de Saída:
        user_name: Joaquim -> Thread ID: XYZ123
        user_name: Boris -> Thread ID: ABC789
    """
    with shelve.open(DB_PATH, flag='r') as db:
        if len(db) == 0:
            print("O banco de dados shelve está vazio.")
        else:
            for key, value in db.items():
                print(f"user_name: {key} -> Thread ID: {value}")

@log_function_call
def upsert_thread(user_name: str, thread_id: str):
    """
    Insere ou atualiza um registro de thread no banco de dados shelve.

    Parâmetros:
        user_name (str): O nome do usuário associado ao thread.
        thread_id (str): O ID do thread a ser armazenado ou atualizado.

    Esta função assegura que cada nome de usuário tenha um único thread ID associado,
    substituindo qualquer thread ID existente para o mesmo nome de usuário. Isso é especialmente
    útil para manter a integridade dos dados quando um usuário inicia uma nova sessão de comunicação
    ou quando precisamos atualizar a referência de thread para um usuário existente.

    A função também imprime uma mensagem de sucesso para confirmar a operação realizada.
    """
    with shelve.open(DB_PATH, writeback=True) as db:
        db[user_name] = thread_id
        return f"Thread_id {thread_id} : e user_name: {user_name} atualizado/inserido com sucesso."

@log_function_call
def delete_thread(user_name: str):
    """
    Remove um registro de thread do banco de dados shelve com base no nome do usuário.

    Parâmetros:
        user_name (str): O nome do usuário do thread a ser removido.

    Se um thread associado ao nome do usuário fornecido for encontrado no banco de dados,
    ele será removido. Caso contrário, uma mensagem indicando que o thread não foi encontrado
    será impressa.

    Esta função é útil para limpar threads antigos ou quando um usuário solicita a remoção
    de seus dados.
    """
    with shelve.open(DB_PATH, writeback=True) as db:
        if user_name in db:
            del db[user_name]
            print(f"Thread {user_name} removido com sucesso.")
        else:
            print(f"Thread com nome de usuário {user_name} não encontrado.")

@log_function_call
def clear_all_threads():
    """
    Remove todos os registros do banco de dados shelve 'threads', limpando o banco de dados.

    Esta função deleta todos os registros armazenados no banco de dados, efetivamente resetando
    o estado do armazenamento. É uma operação irreversível que deve ser usada com extrema cautela,
    especialmente em um ambiente de produção.

    Após a execução desta função, uma mensagem de confirmação é impressa para indicar que todos
    os dados foram removidos com sucesso.
    """
    with shelve.open(DB_PATH, writeback=True) as db:
        db.clear()
        print("Todos os threads foram removidos com sucesso.")


# Exemplo de uso: Imprimindo o conteúdo do threads.db para verificar os dados atuais.
#
