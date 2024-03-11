import sys
sys.path.append('/workplace/')
from cli.cli_layout import draw_chat_frame, prompt_user_name, prompt_message, display_response
from app.services.message_routing_manager import get_or_create_thread
from app.interfaces.interface_openai import generate_response

# Variáveis globais
THREAD_ID = None
USER_NAME = None

def chat():
    draw_chat_frame()  #Monta a tela do sistema.
    
    global THREAD_ID, USER_NAME

    USER_NAME = prompt_user_name()
    THREAD_ID = get_or_create_thread(USER_NAME)
    
    while True:
        
        message = prompt_message(USER_NAME)
            
        # Integração API Openia
        response = generate_response(question_prompt=message, thread_id=THREAD_ID, user_name=USER_NAME)                

        display_response(response)

if __name__ == '__main__':
    chat()
