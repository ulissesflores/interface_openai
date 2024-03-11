from functools import wraps
import logging
import os

log_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'logs', 'function_calls.log')
log_file_path = os.path.abspath(log_file_path)  # Garante que o caminho é absoluto


# Configuração do logger
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_function_call(func):
    """
    Um decorator que registra detalhes sobre a chamada de funções.

    Este decorator registra o início e o término de cada chamada de função, incluindo
    o nome da função, os argumentos recebidos, o valor retornado, e quaisquer
    exceções que possam ocorrer durante a execução da função. Os logs são gravados
    em um arquivo especificado na configuração do logger.

    Uso:
        Pode ser aplicado a qualquer função para adicionar automaticamente registro
        de chamadas no log. Útil para depuração, monitoramento de performance e
        auditorias de segurança.

    Args:
        func (Callable): A função que será decorada.

    Returns:
        Callable: A função wrapper que adiciona logging à função original.

    Raises:
        Exception: Propaga qualquer exceção que ocorra dentro da função decorada,
                   garantindo que o comportamento da função não seja alterado.

    Exemplo:
        @log_function_call
        def minha_funcao(x, y):
            return x + y

    Notas:
        - O caminho do arquivo de log é definido no início deste script.
        - Este decorator é especialmente útil em ambientes de produção onde
          o monitoramento contínuo e a capacidade de resposta rápida a problemas são críticos.
        - A configuração do logger pode ser ajustada conforme necessário para incluir
          mais informações, alterar o formato do log, ou modificar o nível de severidade do log.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"'{func.__name__}' executed successfully. Return: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in '{func.__name__}': {e}")
            raise  # Re-raise the exception after logging
    return wrapper
