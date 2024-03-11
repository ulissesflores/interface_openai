"""
Este módulo `config.py` utiliza classes para organizar e gerenciar as configurações 
e variáveis de ambiente do projeto de maneira estruturada e segura.

Usar classes oferece várias vantagens:

- **Organização**: Agrupa configurações relacionadas, tornando o código mais claro e fácil de entender.
- **Reuso e Modularidade**: Facilita o reuso de configurações e promove a modularidade ao permitir ajustes em um único lugar.
- **Manutenção Simplificada**: Centraliza a gestão de configurações, simplificando a manutenção e reduzindo o risco de inconsistências.
- **Segurança**: Ajuda a manter informações sensíveis fora do código-fonte, utilizando variáveis de ambiente para chaves de API e outros dados sensíveis.
- **Flexibilidade**: Permite expansões e ajustes fáceis nas configurações, incluindo a adição de novos atributos e lógica condicional baseada no ambiente de execução.
- **Integração**: Facilita a integração com ferramentas e bibliotecas externas que esperam configurações definidas de forma estruturada.

Cada classe dentro deste módulo representa um grupo específico de configurações, como configurações da API OpenAI, 
configurações do assistente conversacional, entre outros. Isso permite uma gestão eficaz e segura das 
configurações necessárias para a operação do projeto.

Variáveis sensíveis e específicas do ambiente está no arquivo `.env`
usaremos este módulo para carregá-las de forma segura, garantindo que não sejam expostas ou hardcoded no código-fonte.
"""

# Importa as bibliotecas necessárias para carregar variáveis de ambiente
from dotenv import load_dotenv
import os
import json

# Carrega variáveis de ambiente
load_dotenv()   # Isto irá carregar as variáveis do arquivo .env, que contém secrets.


# **SEÇÃO: Configurações do Modelo Padrão**
# *****Variável:** AI_MODEL

AI_MODEL="chat-gpt-3.5-turbo"


# **SEÇÃO: Configurações do Assistente**
    # **Variável:** ASSISTANT_NAME
    # **Variável:** INSTRUCTIONS
    # **Variável:** TOOLS
    # **Variável:** AI_ASSISTANT_MODEL
    # **Variável:** ASSISTANT_ID -  reutiliza um assistente já criado, ou seja, não é necessário recriar um assistente.

ASSISTANT_NAME="Carcará Risonho"
INSTRUCTIONS="Carcará Risonho, o comediante virtual direto do sertão nordestino, está sempre pronto para espalhar alegria e sabedoria com um toque de humor. Armado com piadas, causos e uma enxurrada de emojis, ele transforma qualquer conversa num momento de descontração e riso. Seja pedindo uma piada, buscando conselhos com o tempero do Nordeste, ou simplesmente batendo um papo, Carcará Risonho garante uma companhia arretada, cheia de carisma e coração. Vamos nessa aventura digital com sabor de cajuína e alma de baião?"
TOOLS='[{"type": "retrieval"}]'
AI_ASSISTANT_MODEL="gpt-3.5-turbo"
ASSISTANT_ID= "asst_pv6MdN6wAme6SX4HqOoL8iX3"
THREAD_ID= "thread_XnrBMJU0HJllaG6hjs3sFMKf"

class OpenAIConfig:
    """
    Esta classe armazena as configurações da API OpenAI, como a chave da API e o modelo de IA a ser usado.

    Atributos:

    * **OPENAI_API_KEY (str):**

        * **Descrição:** A chave da API OpenAI necessária para autenticar as solicitações à API.
        * **Origem:** Carregada do arquivo .env.
        * **Observação:** Certifique-se de definir a variável de ambiente OPENAI_API_KEY com o valor correto.

    * **AI_MODEL (str):**

        * **Descrição:** O modelo de inteligência artificial a ser usado.
        * **Padrão:** "gpt-3.5-turbo".
        * **Opções:**

            * **Modelos de Linguagem Geral:**
                * **GPT-3.5-turbo:** Versão aprimorada do GPT-3 com maior velocidade e melhor desempenho em tarefas complexas.
                * **GPT-4:** Modelo de última geração com habilidades avançadas de geração de texto, tradução e resposta a perguntas.
                * **ChatGPT:** Modelo conversacional que simula diálogos humanos e é ideal para chatbots e assistentes virtuais.
                * **Bloom:** Modelo multilíngue com foco em precisão factual e geração de texto informativo.
                * **InstructGPT:** Modelo instrucional que segue comandos e completa tarefas de maneira eficiente.
            * **Modelos Especializados:**
                * **DALL-E 2:** Modelo de geração de imagens a partir de texto, permitindo criar imagens realistas e criativas.
                * **Whisper:** Modelo de transcrição de áudio que converte fala em texto com alta precisão.
                * **Codex:** Modelo que traduz linguagem natural para código, automatizando tarefas de programação.
            * **Modelos para OpenAI Assistant:**
                * **Assistant-GPT-3.5:** Versão do GPT-3.5 otimizada para assistentes, com foco em fluidez conversacional e personalização.
                * **Assistant-GPT-4:** Modelo de última geração para assistentes, com capacidades avançadas de compreensão de contexto e resposta a perguntas.
                * **Assistant-ChatGPT:** Modelo conversacional robusto para chatbots e assistentes, com habilidades avançadas de diálogo e personalização.

        * **Recomendações:**

            * A escolha do modelo depende das suas necessidades e objetivos.
            * Considere o tamanho do modelo, o custo de uso e suas capacidades específicas.
            * Consulte a documentação oficial da OpenAI para obter mais informações sobre cada modelo.

        * **Recursos Adicionais:**

            * Documentação da API OpenAI: https://platform.openai.com/docs/api-reference
            * Lista de Modelos OpenAI: https://platform.openai.com/docs/models
            * Tutoriais OpenAI Assistant: https://www.youtube.com/watch?v=0h1ry-SqINc

    """

    # Carrega a chave da API do OpenAI do arquivo .env
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Define o modelo de inteligência artificial a ser usado
    AI_MODEL = AI_MODEL

    # Define uma thread padrão
    AI_THREAD_ID = THREAD_ID


class OpenAIAssistantConfig:
    """
    Esta classe armazena as configurações essenciais para personalizar um assistente conversacional 
    baseado na inteligência da OpenAI. Ela define atributos que controlam o comportamento, 
    o conhecimento e as capacidades de processamento do assistente.

    Atributos:

    **ASSISTANT_NAME (str):**

        * **Descrição:** O nome que o assistente usará para se identificar com os usuários.
        * **Tamanho máximo:** 255 caracteres, incluindo espaços.
        * **Exemplos:**
            * "Seu Manoel"
            * "Meu Assistente Português"
            * "Doutor Estranho"
        * **Recomendações:**
            * Use nomes curtos e descritivos que sejam fáceis de lembrar e pronunciar.
            * Evite nomes muito longos ou complexos, pois podem ser difíceis de lembrar e podem dificultar a interação com o assistente.
            * O nome deve ser consistente com a persona e o tom de voz que você deseja que o assistente tenha.
        * **Observações:**
            * O nome do assistente será usado em várias partes da interface do usuário, como na tela de boas-vindas e nas mensagens de resposta.
            * É importante escolher um nome que seja adequado para o público-alvo do seu assistente.

        * **Referências:**
            * [Documentação OpenAI: Personalizando seu Assistente](https://platform.openai.com/docs/guides/personalizing-your-assistant)

    **INSTRUCTIONS (str):**

        * **Descrição:** Instruções iniciais que moldam a personalidade e tom de voz do assistente.
        * **Tamanho máximo:** 1024 caracteres, incluindo espaços.
        * **Exemplos:**
            * "Sou um assistente engraçado, aja sempre de forma gentil e bem humorada."
            * "Sou um assistente informativo e preciso, sempre responda às perguntas de forma clara e concisa."
            * "Sou um assistente criativo e inovador, não tenha medo de pensar fora da caixa."
        * **Recomendações:**
            * As instruções devem ser claras e concisas.
            * Use linguagem natural e evite termos técnicos.
            * Seja específico sobre o tipo de personalidade e tom de voz que você deseja que o assistente tenha.
            * Você pode fornecer exemplos de como você gostaria que o assistente respondesse a diferentes tipos de perguntas.
        * **Observações:**
            * As instruções serão usadas pelo modelo de linguagem da OpenAI para gerar as respostas do assistente.
            * É importante fornecer instruções claras e precisas para garantir que o assistente se comporte de acordo com suas expectativas.

        * **Referências:**
            * [Documentação OpenAI: Ajustando a Personalidade do Assistente](https://platform.openai.com/docs/guides/tuning-your-assistant-personality)

    **TOOLS (list):**

        * **Descrição:** Uma lista de ferramentas e recursos que o assistente pode acessar para responder às perguntas.
        * **Tamanho máximo:** 100 elementos.
        * **Cada elemento da lista:** Um dicionário com as chaves "type" e "languages".
        * **Exemplos:**
            * [{'type': 'retrieval'}]
            * [{'type': 'retrieval'}, {'type': 'translation', 'languages': ['pt', 'en']}]
            * [{'type': 'code_interpreter'}, {'type': 'summarization'}]
        * **Recomendações:**
            * Preencha a lista com as ferramentas e recursos realmente necessários.
            * Evite adicionar ferramentas que não serão utilizadas pelo assistente.
            * Considere o tipo de perguntas que o assistente irá responder e as ferramentas que podem ser úteis para fornecer respostas precisas e relevantes.
        * **Observações:**
            * A lista de ferramentas é usada pelo modelo de linguagem da OpenAI para gerar as respostas do assistente.
            * As ferramentas disponíveis dependem do modelo de IA que você está usando.
            * Consulte a documentação da OpenAI para obter mais informações sobre as ferramentas disponíveis para cada modelo.

        * **Referências:**
            * [Documentação OpenAI: Ferramentas e Recursos para Assistentes](https://platform.openai.com/docs/guides/tools-and-resources-for-assistants)

    **AI_ASSISTANT_MODEL (str):**

        * **Descrição:** O modelo específico da OpenAI que será usado para gerar as respostas do assistente.
        * **Tamanho máximo:** 255 caracteres.
        * **Exemplos:**
            * "gpt-

    """
    ASSISTANT_NAME = ASSISTANT_NAME
    """
    O nome que o assistente usará para se identificar com os usuários.

    Tamanho máximo: 255 caracteres, incluindo espaços.
    Exemplo: "Seu Manoel" #Meu Assistente português 
    """

    INSTRUCTIONS = INSTRUCTIONS
    """
    Instruções iniciais que moldam a personalidade e tom de voz do assistente.

    Tamanho máximo: 1024 caracteres, incluindo espaços.
    Exemplo: "Sou um assistente amigável que te ajuda."
    """

    TOOLS = json.loads(TOOLS)
    """
    Uma lista de ferramentas e recursos que o assistente pode acessar para responder às perguntas.

    Tamanho máximo: 100 elementos.
    Cada elemento da lista: Um dicionário com as chaves "type" e "languages".
    Exemplo: [{'type': 'retrieval'}, {'type': 'translation', 'languages': ['pt', 'en']}]
    """

    AI_ASSISTANT_MODEL = AI_ASSISTANT_MODEL
    """
    O modelo específico da OpenAI que será usado para gerar as respostas do assistente. 
    Modelos diferentes impactam significativamente na geração de linguagem, compreensão de contexto e na qualidade das respostas.

    Tamanho máximo: 255 caracteres.
    Exemplo: "gpt-4-1106-preview"
    """

    # Recomendações:

    # * ASSISTANT_NAME: Use nomes curtos e descritivos.
    # * INSTRUCTIONS: As instruções devem ser claras e concisas.
    # * TOOLS: Preencha a lista com as ferramentas e recursos realmente necessários.
    # * AI_ASSISTANT_MODEL: Defina o modelo de IA que melhor atende às suas necessidades.

    AI_ASSISTANT_ID = ASSISTANT_ID

    """
    Identificador único do assistente na plataforma OpenAI.

    Este identificador é usado para referenciar um assistente específico na API da OpenAI. Cada assistente criado
    na plataforma possui um ID único que permite à API realizar operações como recuperar, atualizar e interagir
    com o assistente. O ID do assistente é fundamental para manter a consistência do contexto e personalização
    nas interações realizadas através do assistente.

    **Características:**
    - **Tipo:** String
    - **Tamanho:** Fixo, determinado pela OpenAI.
    - **Formato:** Uma combinação de letras, números e caracteres especiais.

    **Importância:**
    - **Contextualização:** Permite manter o contexto das interações ao longo do tempo, crucial para assistentes conversacionais.
    - **Personalização:** Associa as configurações, personalidades e instruções específicas ao assistente.
    - **Gerenciamento:** Facilita o gerenciamento de múltiplos assistentes dentro da mesma aplicação ou entre aplicações diferentes.

    **Utilização:**
    - O `ASSISTANT_ID` é utilizado em chamadas API para especificar qual assistente deve ser usado para gerar respostas ou ser atualizado.
    - Fundamental em operações de CRUD (Criação, Recuperação, Atualização e Deleção) na gestão de assistentes.

    **Referências:**
    - [Criando um Assistente na OpenAI](https://platform.openai.com/docs/guides/assistants): Documentação sobre a criação e gerenciamento de assistentes na OpenAI.
    - [API Reference for Assistants](https://platform.openai.com/docs/api-reference/assistants): Referência da API para operações com assistentes, incluindo detalhes sobre como utilizar o `ASSISTANT_ID` em solicitações.

    **Exemplo de Uso:**
    - Recuperar um assistente específico para obter informações sobre ele ou para interagir com o mesmo:
    ```python
    assistant_info = client.beta.assistants.retrieve(ASSISTANT_ID)
    print(assistant_info)
    """








#***EXPLICAÇÃO DETALHADA DAS VARIÁVEIS OPENIA***

# **SEÇÃO: Configurações do Modelo Padrão**

# **Variável:** AI_MODEL
# **Descrição:** Define o modelo de IA padrão que será utilizado pela aplicação.
# **Tipo:** String
# **Padrão:** "chat-gpt-3.5-turbo"
# **Opções:**

#     * **Modelos de Linguagem Geral:**
#         * "chat-gpt-3.5-turbo": Versão aprimorada do GPT-3 com maior velocidade e melhor desempenho em tarefas complexas.
#         * "gpt-4": Modelo de última geração com habilidades avançadas de geração de texto, tradução e resposta a perguntas.
#         * "bloom": Modelo multilíngue com foco em precisão factual e geração de texto informativo.
#         * "instructgpt": Modelo instrucional que segue comandos e completa tarefas de maneira eficiente.
#     * **Modelos Especializados:**
#         * "dall-e 2": Modelo de geração de imagens a partir de texto, permitindo criar imagens realistas e criativas.
#         * "whisper": Modelo de transcrição de áudio que converte fala em texto com alta precisão.
#         * "codex": Modelo que traduz linguagem natural para código, automatizando tarefas de programação.
#     * **Modelos para OpenAI Assistant:**
#         * "assistant-chat-gpt-3.5-turbo": Versão do GPT-3.5 otimizada para assistentes, com foco em fluidez conversacional e personalização.
#         * "assistant-gpt-4": Modelo de última geração para assistentes, com capacidades avançadas de compreensão de contexto e resposta a perguntas.
#         * "assistant-bloom": Modelo multilíngue para assistentes, com foco em precisão factual e geração de respostas informativas.

# # **Observações:**

#     * A escolha do modelo depende das suas necessidades e objetivos.
#     * Considere o tamanho do modelo, o custo de uso e suas capacidades específicas.
#     * Consulte a documentação oficial da OpenAI para obter mais informações sobre cada modelo: https://beta.openai.com/docs/models.

# **Exemplos:**
# AI_MODEL="gpt-4"
# AI_MODEL="assistant-bloom"

# **SEÇÃO: Configurações do Assistente**

# **Variável:** ASSISTANT_NAME
# **Descrição:** Define o nome do assistente virtual que será utilizado pela aplicação.
# **Tipo:** String
# **Padrão:** "Chaves"
# **Tamanho máximo:** 255 caracteres, incluindo espaços.
# **Exemplos:**
# ASSISTANT_NAME="Seu Assistente"
# ASSISTANT_NAME="Doutor Bard"

# **Variável:** INSTRUCTIONS
# **Descrição:** Define as instruções iniciais que moldam a personalidade e o tom de voz do assistente virtual.
# **Tipo:** String multilíngue
# **Padrão:** "Aja como se fosse o chaves da turma do chaves, aja sempre de forma gentil e bem humorada"
# **Observações:**

#    * As instruções podem ser formatadas usando markdown para adicionar negrito, itálico, listas e outros elementos visuais.
#    * É possível definir instruções específicas para diferentes idiomas, utilizando a sintaxe `lang: código_idioma|instruções`.
#    * Consulte a documentação da OpenAI para obter mais informações sobre como formatar instruções: https://beta.openai.com/docs/api-reference/models/assistant/create.

# **Exemplos:**

# **Português:**
# INSTRUCTIONS="Aja como se fosse o chaves da turma do chaves, aja sempre de forma gentil e bem humorada."

# **Inglês:**
# INSTRUCTIONS="Act like the character Chaves from the TV show El Chavo del Ocho, always be kind and humorous."

# **Espanhol:**
# INSTRUCTIONS="Actúa como el personaje Chavo del programa El Chavo del Ocho, sé siempre amable y humorístico."

# **Variável:** TOOLS
# **Descrição:** Define uma lista de ferramentas que o assistente virtual terá acesso para realizar tarefas.
# **Tipo:** Lista de dicionários
# **Padrão:** `[{"type": "retrieval"}]`
# **Opções:**

    # * **Ferramentas de Recuperação:**
    #     * "retrieval": Permite ao assistente acessar e recuperar informações de diversas fontes, como bancos de dados, APIs e websites.
    #     * "search": Permite ao assistente realizar pesquisas na web utilizando diferentes mecanismos de busca.

    # * **Ferramentas de Tradução:**
    #     * "translation": Permite ao assistente traduzir textos de um idioma para outro, utilizando diversos modelos de tradução.

    # * **Ferramentas de Geração:**
    #     * "generation": Permite ao assistente gerar diferentes tipos de conteúdo textual, como poemas, scripts, emails, código e outros.

    # * **Ferramentas de Diálogo:**
    #     * "dialogflow": Permite ao assistente integrar com o Dialogflow, plataforma de desenvolvimento de chatbots.

# **Observações:**

    # * A lista de ferramentas pode ser expandida de acordo com suas necessidades.
    # * Consulte a documentação da OpenAI para obter mais informações sobre cada ferramenta: https://beta.openai.com/docs/api-reference/models/assistant/create.

# **Exemplos:**

# Ferramenta de recuperação e tradução:
# TOOLS=[{"type": "retrieval"}, {"type": "translation", "languages": ["pt", "en"]}]

# Ferramenta de geração de código:
# TOOLS=[{"type": "retrieval"}, {"type": "generation", "type_of_content": "code"}]

# **Variável:** AI_ASSISTANT_MODEL
# **Descrição:** Define o modelo de IA específico que será utilizado pelo assistente virtual.
# **Tipo:** String
# **Padrão:** "gpt-3.5-turbo"
# **Opções:**

    # * **Modelos de Linguagem Geral:**
    #     * "chat-gpt-3.5-turbo": Versão aprimorada do GPT-3 com maior velocidade e melhor desempenho em tarefas complexas.
    #     * "gpt-4": Modelo de última geração com habilidades avançadas de geração de texto, tradução e resposta a perguntas.
    #     * "bloom": Modelo multilíngue com foco em precisão factual e geração de texto informativo.
    #     * "instructgpt": Modelo instrucional que segue comandos e completa tarefas de maneira eficiente.

    # * **Modelos Especializados para Assistentes:**
    #     * "assistant-chat-gpt-3.5-turbo": Versão do GPT-3.5 otimizada para assistentes, com foco em fluidez conversacional e personalização.
    #     * "assistant-gpt-4": Modelo de última geração para assistentes, com capacidades avançadas de compreensão de contexto e resposta a perguntas.
    #     * "assistant-bloom": Modelo multilíngue para assistentes, com foco em precisão factual e geração de respostas informativas.

# **Observações:**

    # * A escolha do modelo depende das suas necessidades e objetivos.
    # * Considere o tamanho do modelo, o custo de uso e suas capacidades específicas.
    # * Consulte a documentação oficial da OpenAI para obter mais informações sobre cada modelo.








