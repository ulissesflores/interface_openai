
# Interface OpenAI: Comunicação facilitada com a API OpenAI

![Python](https://img.shields.io/badge/python-3.9+-blue.svg) ![Docker](https://img.shields.io/badge/docker-supported-blue.svg) ![License MIT](https://img.shields.io/badge/license-MIT-green.svg) ![Cobertura de Testes](https://img.shields.io/badge/coverage-90%25-brightgreen.svg)  ![Versão](https://img.shields.io/badge/version-1.0-blue.svg)

## Introdução

A Interface OpenAI é uma ferramenta essencial para desenvolvedores e entusiastas de IA, facilitando a interação com a poderosa API da OpenAI. Ao encapsular a complexidade técnica, nossa biblioteca torna acessível a criação de soluções inovadoras em IA, fornecendo uma interface simples e intuitiva para enviar e receber mensagens, gerenciar threads e contexto. É possível criar chatbots inteligentes até análises de texto avançadas, apoiando-se nas capacidades sem precedentes dos modelos GPT.

## Características

- **Facilidade de uso**: Permite enviar e receber mensagens da API OpenAI com apenas algumas linhas de código, simplificando a interação com tecnologias de IA avançadas.

```python

          from interface_openai import generate_response

          response = generate_response(question_prompt=message)
```

- **Flexibilidade nos Modelos de IA**: Suporta a escolha entre diferentes modelos GPT, permitindo otimizar a aplicação conforme a necessidade específica de processamento de linguagem natural.

- **Integração com Assistente da OpenAI**: Facilita a criação de assistentes personalizados, oferecendo uma nova camada de interatividade e automação.

- **Gerenciamento Avançado de Contexto**: Mantém e gerencia threads de conversação e contexto, possibilitando diálogos mais coerentes e contínuos.

- **Documentação Completa**: Fornece documentação detalhada e exemplos de código, garantindo uma curva de aprendizado suave e um desenvolvimento eficiente.

- **Implementação Simplificada da API**: Abstrai a complexidade inerente da API OpenAI, tornando o desenvolvimento de aplicações baseadas em IA mais acessível.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para o desenvolvimento da biblioteca.
- **Flask**: Para criação de aplicações web e APIs.
- **Docker**: Para empacotamento e distribuição da aplicação em ambientes isolados.
- **OpenAI API**: Para acesso às capacidades de inteligência artificial do GPT-3 e outros modelos.

### Pré-requisitos

- Python 3.9+
- Docker (Opcional, mas recomendado)

## Instalação

## Uso do Docker

Para utilizar o projeto com [Docker]([https://linktodocumentation), siga estas instruções:

1. Construa a imagem Docker:

    ```bash
     docker build -t interface_openai:latest .
    ```

2. Execute o container:

    ```bash
    docker run -it interface_openai:latest
    ```

## Manual

1- Clone o repositório:

```bash
  git clone https://github.com/ulissesflores/interface_openai.git
```

2- Acesse o diretório do projeto:

```bash
  cd interface_openai
```

3- Instale as dependências:

```bash
  pip install -r requirements.txt
```

## Exemplos de Uso

### Enviando uma Pergunta e Recebendo Resposta

```python
  from interface_openai import generate_response

  # Exemplo de pergunta
  question_prompt = "Qual é a capital da França?"
  response = generate_response(question_prompt)
  print(response)
```

```plaintext
"Resposta: A capital da França é Paris."
```

## Gerenciamento de Contexto em Conversação

Este exemplo ilustra como gerenciar conversas intercaladas de múltiplos usuários, cada um com seu contexto individual, utilizando a biblioteca `interface_openai`.

### Cenário

Cícero, Severino e Amaro fazem perguntas intercaladas. Após três rodadas de interação, cada um solicita um resumo de sua conversa com o assistente.

### Implementação

```python
from interface_openai import generate_response

# Identificador único da conversa
thread_id = "th_123456"

# Primeira rodada de perguntas
response_cicero1 = generate_response("Qual é o sentido da vida?", thread_id, "Cícero")
response_severino1 = generate_response("Como está o tempo hoje?", thread_id, "Severino")
response_amaro1 = generate_response("O que é inteligência artificial?", thread_id, "Amaro")

# Continuação das perguntas, intercalando os usuários
response_cicero2 = generate_response("E sobre a felicidade?", thread_id, "Cícero")
response_severino2 = generate_response("Qual a previsão para amanhã?", thread_id, "Severino")
response_amaro2 = generate_response("Quem criou o GPT-3?", thread_id, "Amaro")

# Terceira rodada de perguntas
response_cicero3 = generate_response("Pode me contar uma piada?", thread_id, "Cícero")
response_severino3 = generate_response("Quais são os tipos de nuvens?", thread_id, "Severino")
response_amaro3 = generate_response("Como funciona o aprendizado de máquina?", thread_id, "Amaro")
```

```python
# Solicitação de resumo por Cícero
resumo_cicero = generate_response("Faça um resumo da nossa conversa.", thread_id, "Cícero")
print("Resumo da conversa de Cícero: ", resumo_cicero)
```

```plaintext
"Resposta: Resumo da conversa de Cícero: Conversamos sobre a vida, felicidade e lhe contei uma piada muito boa."
```

```python
# Solicitação de resumo por Severino
resumo_severino = generate_response("Faça um resumo da nossa conversa.", thread_id, "Severino")
print("Resumo da conversa de Severino: ", resumo_severino)
```

```plaintext
"Resposta: Resumo da conversa de Severino: Conversamos sobre a previsão do tempo e condição climática."
```

```python
# Solicitação de resumo por Amaro
resumo_amaro = generate_response("Faça um resumo da nossa conversa.", thread_id, "Amaro")
print("Resumo da conversa de Amaro: ", resumo_Amaro)
```

```plaintext
"Resposta: Resumo da conversa de Amaro: Conversamos sobre Inteligência Artificial."
```

A API da OpenAI oferece uma abordagem robusta para gerenciar conversas contínuas, empregando `thread_id` para identificar e manter o contexto de uma conversa. Além disso, permite a incorporação de metadados adicionais, como o nome do usuário, para enriquecer a interação e garantir que as conversas sejam não apenas contínuas, mas também personalizadas. Ao utilizar `thread_id` juntamente com identificadores únicos do usuário, nosso sistema pode gerenciar múltiplas conversas paralelas de forma eficiente, assegurando que cada interação seja relevante e isolada dentro do contexto apropriado.

Nossa interface `interface_openai` implementa uma solução que permite múltiplas conversas individuais sob a mesma thread_id, diferenciando-as por meio de metadados adicionais, como o nome do usuário. Isso significa que, mesmo dentro de uma única thread, podemos manter o contexto separado para cada usuário, permitindo conversas paralelas e personalizadas. Essa abordagem oferece uma gestão de diálogo mais rica e envolvente, maximizando a capacidade da API da OpenAI para aplicações interativas complexas.

Para mais informações, consulte a [documentação oficial da API da OpenAI](https://beta.openai.com/docs/).

## Simulando o Funcionamento

Para simular o funcionamento da interface `interface_openai`  executamos o arquivo `chat_simulator.py` localizado em `tests/simulator/`, siga os passos abaixo:

1. Navegue até o diretório do simulador:

```bash
  cd tests/simulator/
```

2. Execute o simulador

```bash
 python3 chat_simulator.py
```

3. O simulador pedirá seu nome. Insira seu nome e pressione Enter.

4. Após inserir seu nome, você começará a interagir com a interface. Responda às perguntas ou faça suas próprias perguntas.

5. Para sair do simulador, digite `/sair` a qualquer momento.

Este passo a passo oferece uma forma simples e direta de experimentar a interface de conversação, permitindo uma interação prática com o sistema.

## Screenshots do Simulador

### Tela Inicial

A primeira tela do simulador, pronta para receber o nome do usuário.
![Tela Inicial](https://i.imgur.com/oy1fB8i.png)

### Conversando com a Interface

Uma demonstração da interação fluida com o assistente AI.
![Conversando com a Interface](https://i.imgur.com/U0wocSC.png)

### Saindo

Como encerrar uma sessão no simulador.
![Saindo](https://i.imgur.com/dGCtIRK.png)




## Custos Associados ao Uso da API da OpenAI

O uso da API da OpenAI está sujeito a custos, que variam de acordo com o tipo de modelo utilizado e o volume de solicitações. É importante revisar a documentação oficial da OpenAI para entender as diferentes faixas de preços e otimizar o uso da API conforme suas necessidades. Para detalhes específicos sobre precificação e modelos disponíveis, visite a [página de preços da OpenAI](https://openai.com/pricing).

Recomendamos uma análise cuidadosa das opções para selecionar o modelo que melhor atende ao seu projeto, equilibrando custo e performance.

## Como Contribuir

Agradecemos o interesse em contribuir para a Interface OpenAI! Se você deseja propor melhorias, corrigir bugs ou adicionar novas funcionalidades, siga estes passos:

1. Fork o projeto.
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4. Push para a Branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.

Toda contribuição será bem-vinda, e juntos fortaleceremos a comunidade open source.

## Recursos Adicionais

Para aprofundar seus conhecimentos e explorar mais sobre a API da OpenAI e suas capacidades, visite:

- [Documentação Oficial da OpenAI](https://openai.com/api/)
- [Guia de Início Rápido da OpenAI](https://beta.openai.com/docs/guides/quickstart)

## Tecnologia utilizada

A interface `interface_openai` utiliza Python para a lógica de programação, Flask como framework web para criar APIs, e Docker para garantir a portabilidade e facilidade na configuração de ambientes. Cada tecnologia foi escolhida criteriosamente para oferecer a melhor experiência no desenvolvimento e uso da interface.

## Sobre os Desenvolvedores

Este projeto foi idealizado e desenvolvido por [Ulisses Flores](https://twitter.com/ulissesflores) e [Juliano Nizer Ribas](https://twitter.com/juliano_ribas), ambos desenvolvedores na CodexHash. Compartilhamos uma paixão por tecnologia e inovação, buscando sempre criar soluções que impactam positivamente a comunidade de desenvolvedores.

## Agradecimentos

Um agradecimento especial ao meu parceiro de desenvolvimento [Juliano Nizer Ribas](https://twitter.com/juliano_ribas) e à CodexHash, onde ambos somos desenvolvedores, por seu apoio e contribuições essenciais para este projeto.

## License

[MIT](https://choosealicense.com/licenses/mit/)