from colorama import Fore, Style, init
import sys

# Inicializa o Colorama para converter automaticamente os códigos ANSI para chamadas de API Win32.
# Isso é necessário apenas no Windows. Nos sistemas Unix, os códigos ANSI são usados como estão.
# A opção autoreset=True faz com que o Style seja resetado após cada print, evitando a necessidade de chamá-lo manualmente.
init(autoreset=True)

def draw_chat_frame():
    """
    Desenha um quadro no terminal para a interface do chat.
    
    Utiliza a biblioteca colorama para colorir o quadro de ciano.
    O quadro é desenhado com caracteres especiais para criar uma borda, e o título é centralizado dentro dessa borda.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    title = "Simulador de Chat usando ChatGPT API da OpenAI"
    width = 100
    print(Fore.CYAN + '╒' + '═' * (width - 2) + '╕')
    print(Fore.CYAN + '│' + title.center(width - 2) + '│')
    print(Fore.CYAN + '╘' + '═' * (width - 2) + '╛')

def prompt_user_name():
    """
    Solicita ao usuário que digite seu nome.
    
    Retorna o nome digitado após remover espaços desnecessários.
    Se o usuário digitar '/sair', a função `mensagem_despedida` é chamada e o programa é encerrado.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    name = input(Fore.YELLOW + 'Por favor, digite seu nome: ' + Style.RESET_ALL).strip()
    if name.lower() == '/sair':
        mensagem_despedida()  # Chama a função de despedida
        sys.exit()
    return name

def prompt_message(user_name):
    """
    Solicita ao usuário que digite sua mensagem.
    
    O nome do usuário é exibido em verde antes do prompt para digitar a mensagem.
    A função retorna a mensagem digitada pelo usuário, também removendo espaços desnecessários.
    Se o usuário digitar '/sair', a função `mensagem_despedida` é chamada e o programa é encerrado.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    message = input(Fore.GREEN + f"{user_name}, digite sua mensagem (ou '/sair' para finalizar): " + Style.RESET_ALL).strip()
    if message.lower() == '/sair':
        mensagem_despedida()  # Chama a função de despedida
        sys.exit()
    return message

def display_message(user_name, message):
    """
    Exibe a mensagem do usuário no terminal.
    
    O nome do usuário é exibido em verde, seguido pela mensagem.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    print(Fore.GREEN + f"{user_name}: " + message + Style.RESET_ALL)

def display_response(response):
    """
    Exibe a resposta do ChatGPT no terminal.
    
    A resposta é exibida em azul para distinguir das mensagens do usuário.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    print(Fore.BLUE + "ChatGPT: " + response + Style.RESET_ALL)

def mensagem_despedida():
    """
    Exibe uma mensagem de despedida e encerra o programa.
    
    A mensagem de despedida é exibida em vermelho.
    
    Referências:
    - Colorama: https://pypi.org/project/colorama/
    """
    print(Fore.RED + 'Saindo do simulador de chat...')

