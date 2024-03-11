import time
from openai import OpenAI
import sys

# Define explicitamente o diretório raiz do projeto
sys.path.append('/workplace/')

from app.decorators.log_decorator import log_function_call
from app.utils.openia_config import OpenAIConfig, OpenAIAssistantConfig

class OpenAIClientSingleton:
    """
    Classe Singleton para gerenciar a instância única do cliente da OpenAI.

    Esta classe implementa o padrão de design Singleton para garantir que apenas uma
    instância do cliente OpenAI seja criada e utilizada em toda a aplicação. Isso é útil
    para cenários onde múltiplas partes do código precisam acessar o cliente OpenAI para
    realizar chamadas à API, mas desejam evitar a sobrecarga associada à recriação do cliente
    em cada uso.

    O padrão Singleton é implementado sobrescrevendo o método especial `__new__`. Isso garante
    que, se uma instância da classe já existir, ela será retornada em vez de criar uma nova.
    Além disso, a inicialização do cliente OpenAI é feita apenas uma vez, na primeira criação
    da instância, garantindo eficiência e consistência.

    Atributos:
        Não há atributos públicos.

    Métodos:
        Não há métodos públicos além do construtor.

    Uso:
        Para obter a instância do cliente OpenAI, simplesmente instancie `OpenAIClientSingleton`:
        
        ```python
        client = OpenAIClientSingleton()
        ```
        
        Isso retornará a instância única do cliente OpenAI, que pode ser usada para realizar
        chamadas à API. Chamadas subsequentes a `OpenAIClientSingleton()` retornarão a mesma
        instância.

    Notas:
        - Lembre-se de que o uso do padrão Singleton pode impactar a testabilidade do código
          e o isolamento de estados entre diferentes partes da aplicação. Use com cuidado e
          apenas quando necessário.
        - Esta implementação é thread-safe em ambientes onde `__new__` é atômico. Em ambientes
          multithread onde isso não é garantido, podem ser necessárias medidas adicionais para
          garantir a segurança na criação da instância.

    Referências:
        - Documentação da API da OpenAI: https://platform.openai.com/docs/api-reference
        - Padrão de Design Singleton: https://pt.wikipedia.org/wiki/Singleton
    """
    _instance = None
    
    @log_function_call
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIClientSingleton, cls).__new__(cls)
            # Inicializa o cliente OpenAI aqui
            cls._instance.client = OpenAI(api_key=OpenAIConfig.OPENAI_API_KEY)
        return cls._instance.client

# Instancia uma unica vez o client da OpenAI usando as configurações definidas em config.py
# Uso do Singleton
client = OpenAIClientSingleton()

@log_function_call
def upload_file_to_openai(path):
    """
    Faz o upload de um arquivo para a OpenAI para uso específico com "assistants".
    
    Esta função abre o arquivo localizado no caminho especificado e faz o upload
    para a OpenAI, marcando-o com o propósito de "assistants". Isso é útil para
    carregar dados que serão utilizados para treinar ou informar as respostas
    do modelo de IA.
    
    Parâmetros:
        path (str): O caminho do arquivo a ser carregado.
        
    Retorna:
        object: O objeto de arquivo retornado pela OpenAI após o upload.
                Contém informações sobre o arquivo carregado, como ID e status.
                
    Exceções:
        Pode lançar exceções relacionadas à falha na abertura do arquivo ou
        problemas no upload para a OpenAI. Recomenda-se chamar essa função dentro
        de um bloco try-except para lidar com possíveis exceções.
    """
    with open(path, "rb") as file_to_upload:
        file = client.files.create(file=file_to_upload, purpose="assistants")
    return file

@log_function_call
def create_assistant(**kwargs):
     """
    Cria um assistente na OpenAI com configurações personalizadas.

    Esta função oferece flexibilidade para criar assistentes personalizados na OpenAI,
    permitindo especificar diversos parâmetros que moldam suas capacidades e comportamento.

    **Parâmetros:**

    * **kwargs (dict):** Dicionário de parâmetros nomeados. Os parâmetros válidos
        e seus efeitos são descritos a seguir:

        * **`file_id` (str, optional):** O ID de um arquivo previamente carregado na OpenAI.
            Se especificado, o assistente terá acesso ao conteúdo do arquivo para
            processamento e geração de respostas.

        * **`name` (str, optional):** O nome do assistente. Por padrão, o valor
            `"OpenAI Assistant"` é utilizado.

        * **`instructions` (str, optional):** Instruções que moldam a personalidade e o tom de voz do
            assistente. Estas instruções servem como guia para o comportamento do
            assistente durante as interações.

        * **`tools` (list, optional):** Uma lista de ferramentas e recursos que o assistente
            pode acessar e utilizar para gerar respostas. As ferramentas disponíveis
            podem ser consultadas na documentação da OpenAI.

        * **`model` (str, optional):** O modelo de IA específico da OpenAI que será usado
            para gerar as respostas do assistente. Modelos diferentes possuem
            diferentes capacidades e características.

    **Retorno:**

    * **object:** O objeto de assistente criado pela API da OpenAI após a
        solicitação de criação. Este objeto contém informações sobre o assistente,
        como ID, nome e status.

    **Exceções:**

    * **`OpenAIError`:** Se a requisição à API da OpenAI falhar.
        A exceção conterá informações detalhadas sobre o erro.

    **Referências:**

    * **Documentação OpenAI: Criando um Assistente:** https://platform.openai.com/docs/api-reference/assistants/create
    * **Documentação OpenAI: Modelos de Assistente:** https://platform.openai.com/docs/api-reference/models#list-models
    * **Padrões de Boas Práticas para Documentação Python:** https://www.python.org/dev/peps/pep-0257/

    **Detalhes da Implementação:**

    1. A função utiliza `kwargs` para extrair os parâmetros passados para a função.
    2. Se um parâmetro não for especificado em `kwargs`, o valor padrão da variável
        correspondente na classe `OpenAIAssistantConfig` será usado.
    3. A função utiliza o cliente OpenAI para criar um novo assistente, definindo as
        configurações de acordo com os valores em `kwargs`.
    4. A função retorna o objeto de assistente criado pela API da OpenAI.

    **Observações:**

    * É importante verificar a documentação da OpenAI para obter mais informações sobre
        os parâmetros e o objeto de resposta da API `create_assistant`.
    * A função trata exceções do tipo `OpenAIError` que podem ser levantadas durante a
        requisição à API da OpenAI.
    * A função utiliza variáveis da classe `OpenAIAssistantConfig` para definir as
        configurações do assistente.

    **Exemplos de Uso:**

    # Criando um assistente com configurações padrão
    assistant = create_assistant()

    # Especificando o ID do arquivo e personalizando o nome
    assistant = create_assistant(file_id="file-id-123", name="Meu Assistente")

    # Definindo instruções personalizadas e ferramentas específicas
    instructions = "Seja informativo e criativo. Utilize linguagem simples e evite jargões."
    tools = ["summarization", "translation"]
    assistant = create_assistant(instructions=instructions, tools=tools)

    # Personalizando o modelo de IA
    model = "davinci-codex"
    assistant = create_assistant(model=model)

    """
     try:
        # Extrai os parâmetros de kwargs
        file_id = kwargs.get("file_id")
        name = kwargs.get("name", OpenAIAssistantConfig.ASSISTANT_NAME)
        instructions = kwargs.get("instructions", OpenAIAssistantConfig.INSTRUCTIONS)
        tools = kwargs.get("tools", OpenAIAssistantConfig.TOOLS)
        model = kwargs.get("model", OpenAIAssistantConfig.AI_ASSISTANT_MODEL)

        file_ids = [file_id] if file_id else []
        assistant = client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=tools,
            model=model,
            file_ids=file_ids,
        )
        return assistant

     except Exception as e:
        # Trate ou registre a exceção conforme necessário
        print(f"Erro ao criar assistente: {e}")
        return None

@log_function_call
def retrieve_assistant(assistant_id: str) -> any:
    """
    Recupera detalhes de um assistente específico na API da OpenAI usando seu ID.

    Esta função é essencial para aplicações que trabalham com múltiplos assistentes personalizados, permitindo
    acessar informações específicas e utilizar recursos particulares de cada assistente. A recuperação de um
    assistente por ID é útil para gerenciar dinamicamente os assistentes em uso, adaptando a interação de acordo
    com as necessidades da conversa ou preferências do usuário.

    Parâmetros:
        assistant_id (str): O identificador único do assistente a ser recuperado.

    Retorna:
        object: Um objeto representando o assistente recuperado, incluindo seu ID, nome, configurações e
                status, entre outros detalhes relevantes.

    Exemplo de Uso:
        assistant = retrieve_assistant("assistant_id_exemplo")
        print(f"Assistente recuperado com ID: {assistant.id}")

    Importância:
        Gerenciar assistentes específicos é fundamental para proporcionar experiências de interação ricas e
        variadas, especialmente em ambientes onde diferentes assistentes são especializados em temas ou tarefas
        distintas.

    Notas:
        - A identificação correta do assistente é crucial para o sucesso da recuperação, exigindo o uso
          preciso do ID.
        - Similarmente à recuperação de threads, a tentativa de acessar um assistente não existente resultará
          em erro, recomendando-se práticas adequadas de tratamento de exceções.

    Referências:
        - Documentação da API OpenAI sobre assistentes: https://beta.openai.com/docs/api-reference/assistants
    """    
    
    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        return assistant
    except Exception as e:
        raise Exception(f"Erro ao recuperar assistente com ID {assistant_id}: {e}")

@log_function_call
def create_thread() -> any:
    """
    Cria um novo thread na API da OpenAI para facilitar o gerenciamento de conversas contínuas.

    Um thread na API da OpenAI é uma sequência de mensagens que mantém o contexto da conversa, permitindo
    que o modelo de IA forneça respostas mais coesas e contextuais. A criação de um novo thread é
    essencial para iniciar uma nova conversa ou separar contextos de diálogo diferentes dentro de uma aplicação.

    Retorna:
        object: Um objeto representando o thread criado, contendo informações importantes como o ID do thread,
                que será necessário para enviar mensagens subsequentes mantendo o contexto da conversa.

    Exemplo de Uso:
        thread = create_thread()
        print(f"Thread criado com ID: {thread.id}")

    Importância:
        O uso de threads é fundamental para manter uma experiência de conversa natural e contínua, pois
        permite que a IA acompanhe o desenvolvimento da conversa, mantendo um histórico de interações
        anteriores. Isso é especialmente útil em aplicativos de chat, assistentes virtuais ou qualquer
        interface que necessite de uma interação conversacional consistente com o usuário.

    Notas:
        - A criação de um novo thread não requer parâmetros adicionais, simplificando o processo de
          início de uma nova conversa.
        - Cada thread é identificado unicamente por um ID, que deve ser utilizado em todas as mensagens
          subsequentes para garantir a continuidade do contexto.

    Referências:
        - Documentação da API OpenAI sobre gerenciamento de threads: https://beta.openai.com/docs/api-reference/threads
    """
    try:
            thread = client.beta.threads.create()
            return thread
    except Exception as e:
        raise Exception(f"Erro ao criar thread: {e}")

@log_function_call
def retrieve_thread(thread_id: str) -> any:
    """
    Recupera um thread existente na API da OpenAI usando seu ID.

    Esta função é útil para retomar conversas anteriormente iniciadas, permitindo acessar o histórico
    de mensagens e continuar a interação no mesmo contexto. Isso é fundamental para aplicações que
    precisam de persistência de conversa ou que desejam analisar o conteúdo das interações passadas.

    Parâmetros:
        thread_id (str): O identificador único do thread a ser recuperado.

    Retorna:
        object: Um objeto representando o thread recuperado, contendo todas as informações relevantes,
                incluindo o histórico de mensagens.

    Exemplo de Uso:
        thread = retrieve_thread("thread_id_exemplo")
        print(f"Thread recuperado com ID: {thread.id}")

    Importância:
        A capacidade de recuperar threads específicos é crucial para aplicações que operam com múltiplas
        conversas simultâneas, necessitando de uma maneira eficiente de alternar entre contextos diferentes
        sem perder o histórico de interações.

    Notas:
        - É importante garantir que o ID do thread fornecido corresponda a um thread existente para evitar
          erros na recuperação.
        - A função lança uma exceção se o thread especificado não puder ser encontrado, portanto, é
          recomendável o uso de tratamento de exceções adequado ao invocar esta função.

    Referências:
        - Documentação da API OpenAI sobre gerenciamento de threads: https://beta.openai.com/docs/api-reference/threads
    """

    try:
        thread = client.beta.threads.retrieve(thread_id)
        return thread
    except Exception as e:
        raise Exception(f"Erro ao recuperar thread com ID {thread_id}: {e}")

@log_function_call
def generate_response(question_prompt: str, **kwargs):
    """
    Gera uma resposta usando a API OpenAI, opcionalmente dentro de uma thread específica
    para manter o contexto da conversa. Utilizar threads facilita o gerenciamento de
    conversas contínuas, permitindo um diálogo mais coeso e contextualizado.

    A inclusão do nome do usuário na pergunta personaliza a experiência, tornando
    a interação mais direta e pessoal.

    Args:
        question_prompt (str): Texto do prompt de pergunta para o qual a resposta é gerada.
        **kwargs: Argumentos opcionais, incluindo:
            thread_id (str, optional): ID de uma thread existente para manter o contexto das conversas.
                Se não fornecido, utiliza-se um valor padrão.
            assistant_id (str, optional): ID do assistente a ser utilizado.
                Se não fornecido, utiliza-se um valor padrão.
            user_name (str, optional): Nome do usuário que faz a pergunta.
                Se não fornecido, considera-se None.

    Returns:
        str: A resposta gerada pela API da OpenAI.

    Raises:
        ValueError: Se `question_prompt` for None ou uma string vazia.

    Exemplos de Uso:
        generate_response("Qual é o sentido da vida?", user_name="Alice")
        # Output: "Criando nova thread.\nAlice pergunta: Qual é o sentido da vida?\n42"

        generate_response("Conte-me uma piada.", thread_id="existing_thread_id", assistant_id="custom_assistant_id")
        # Output: "Utilizando thread existente.\nResposta simulada da OpenAI."

    Nota:
        Esta função depende de um cliente OpenAI configurado (`client`) e funções auxiliares
        `format_user_question` e `run_assistant` para preparar perguntas e obter respostas.
        Essas dependências são fundamentais para a funcionalidade da função.

    Referências:
        Documentação da API OpenAI: https://beta.openai.com/docs/
        PEP 257 -- Docstring Conventions: https://www.python.org/dev/peps/pep-0257/

    Motivação:
        A decisão de incluir o nome do usuário e a opção de utilizar threads visa melhorar
        a interatividade e o contexto das conversas geradas pela API OpenAI. A estrutura e
        o conteúdo desta docstring seguem as diretrizes sugeridas pelo PEP 257 para garantir
        clareza e compreensão.
    """
        
    # !!! ATENÇÃO: Esse trecho define funções auxiliares para o funcionamento da generate_response.
    @log_function_call
    def _format_user_question(user_name=None, question_prompt=None):
        """
        ## Motivação

        Esta função foi criada para diferenciar várias conversas dentro de uma mesma thread em um sistema de chat. Ao prefixar cada pergunta com o nome do usuário, o modelo de IA pode:

        * Manter o contexto de quem está fazendo a pergunta, especialmente útil em chats com múltiplos usuários.
        * Fornecer respostas mais direcionadas e personalizadas para cada usuário.

        Essa abordagem também é útil em grupos do WhatsApp, onde a quantidade de mensagens pode ser alta e o contexto pode ser facilmente perdido.


        ## Funcão

        Prepara uma pergunta para ser enviada ao ChatGPT, prefixando-a com o nome do usuário e formatando-a de acordo com as melhores práticas.

        Essa abordagem oferece diversos benefícios:

        * **Contextualização:** Permite ao modelo de IA manter o contexto de quem está fazendo a pergunta, especialmente útil em chats com múltiplos usuários.
        * **Personalização:** Melhora a experiência de interação, tornando as respostas do modelo mais direcionadas e relevantes para cada usuário.
        * **Usabilidade:** Facilita a leitura e compreensão das perguntas em interfaces conversacionais.

        A função formata a pergunta da seguinte maneira:

        * **Nome do usuário:** "Usuário {nome}"
        * **Pergunta:** "{pergunta}"

        Exemplo:

        --- format_user_question("Alice", "O que é inteligência artificial?")
        'Usuário Alice pergunta: O que é inteligência artificial?'

        **Observações:**

        * A formatação pode ser facilmente adaptada para atender às necessidades específicas do seu aplicativo.
        * Ao utilizar esta função em um sistema real, considere as implicações de segurança e privacidade relacionadas ao uso de nomes de usuários e perguntas que podem conter informações confidenciais.

        **Referências:**

        * Documentação da OpenAI sobre threads e gestão de contexto em conversas: https://openai.com/api/
        * Práticas recomendadas para interação com modelos de IA e gestão de estado de conversa em chatbots e assistentes virtuais.
        * Considerações sobre usabilidade e experiência do usuário em interfaces conversacionais.

        """
        if user_name is None:
            return question_prompt

        # Verifica se o prompt de pergunta foi fornecido
        if question_prompt is None:
            raise ValueError("Por favor, insira uma pergunta.")
        
        #formatted_question = f"Meu nome é: {user_name}, e te faço uma pergunta: {question_prompt}"
        
        formatted_question = f"Meu nome é: {user_name}, e use esse nome para distinguir entre as perguntas. Não precisa ficar dizendo meu nome, nem o que vai fazer, apenas faça. Te faço uma pergunta: {question_prompt}"
        
        return formatted_question

    @log_function_call
    def _run_assistant(thread_id: str, assistant_id: str):
        """
    Executa um assistente conversacional da OpenAI em uma thread específica, gerando uma resposta personalizada.

    Esta função interage com o endpoint Assistants da API OpenAI para:

    1. **Recuperar o assistente:** Obtém as configurações e o modelo relacionado ao assistente especificado pelo seu ID.
    2. **Executar o assistente:** Inicia a execução do assistente no contexto da thread fornecida, aproveitando as conversas anteriores para gerar respostas relevantes.
    3. **Monitorar o progresso:** Verifica periodicamente o status da execução do assistente, aguardando sua conclusão.
    4. **Extrair a resposta:** Extrai a última mensagem gerada pelo assistente a partir das mensagens da thread.

    Args:
            thread_id (str): O ID do thread que será utilizado na conversa.
            assistant_id (str): O ID do assistente que será utilizado para gerar respostas.

        Returns:
            str: A resposta gerada pelo assistente na thread fornecida.

    Referências:
        * Documentação da API OpenAI - Assistentes: https://beta.openai.com/docs/api-reference/assistants
        * Documentação da API OpenAI - Threads: https://beta.openai.com/docs/api-reference/threads
        * Documentação da API OpenAI - Execuções do Assistente: https://beta.openai.com/docs/api-reference/threads/runs 
        """
    
        # Run the assistant (https://beta.openai.com/docs/api-reference/threads/runs/create)
        run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

        # Wait for completion (https://beta.openai.com/docs/api-reference/threads/runs/retrieve)
        while run.status != "completed":
            # Be nice to the API
            time.sleep(0.5)
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

        # Retrieve the Messages (https://beta.openai.com/docs/api-reference/threads/messages/list)
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        new_message = messages.data[0].content[0].text.value
        return new_message
 

    if not question_prompt:
        raise ValueError("Por favor, insira uma pergunta.")

    # Retrieve the Assistant and thread_id (https://beta.openai.com/docs/api-reference/assistants/retrieve)
    assistant_id = kwargs.get('assistant_id', OpenAIAssistantConfig.AI_ASSISTANT_ID)  # Usa o assistant_id padrão se não for especificado.
    thread_id = kwargs.get('thread_id', OpenAIConfig.AI_THREAD_ID)  # Usa o thread_id padrão se não for especificado.
    user_name = kwargs.get('user_name', None)  # Assume None para user_name se não for especificado.

   # PREPARAR PERGUNTA COM NOME DE USUÁRIO
    formated_question = _format_user_question(user_name=user_name, question_prompt=question_prompt)

    try:
        #Cria a mensagem para ser enviada à API da OpenAI
        client.beta.threads.messages.create(thread_id=thread_id, role="user", content=formated_question)

        # Roda o assistant da OpenIA, aguarda e retorna a resposta utilizando a thread especificada. E, se for o caso, 
        # apropriada para cada usuário de uma thread       
        response = _run_assistant(thread_id, assistant_id) 

    except Exception as e:

        raise Exception(f"Erro durante execução: {e}")
     
    return response

