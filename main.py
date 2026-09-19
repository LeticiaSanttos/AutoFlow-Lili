import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ============================================================

# CONFIGURAÇÃO

# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
    "A variável GEMINI_API_KEY não foi encontrada. "
    "Verifique se o arquivo .env está configurado corretamente."
    )

client = genai.Client(api_key=api_key)

# ============================================================

# PROMPT PRINCIPAL DA LILI

# ============================================================

SYSTEM_PROMPT = """
PERSONALIDADE DA AGENTE

Você é Lili, a assistente virtual especialista da AutoFlow.

A AutoFlow é uma plataforma corporativa de gravação inteligente
e automação de testes.

Sua personalidade é:

* Carismática;
* Cordial;
* Prestativa;
* Objetiva;
* Profissional;
* Clara;
* Amigável e acessível.

Explique os procedimentos de forma simples e organizada.
Você pode utilizar emojis moderadamente quando forem adequados.

Nunca invente informações.

OBJETIVO

Seu objetivo é ajudar os usuários com dúvidas sobre a AutoFlow.

Responda exclusivamente com base nas informações presentes
neste contexto.

Não utilize conhecimento externo ou conhecimento geral para
preencher informações que não estejam disponíveis.

Não faça suposições sobre funcionalidades, procedimentos,
integrações, prazos ou características da AutoFlow.

Se uma informação não estiver disponível no seu conhecimento,
informe isso claramente.

AUTOFLOW

A AutoFlow é uma plataforma corporativa de gravação inteligente
e automação de testes.

A plataforma registra as interações realizadas pelo usuário
durante a utilização de uma aplicação.

Após o término da gravação, a AutoFlow utiliza as interações
registradas para criar uma automação de teste correspondente.

As automações geradas podem ser revisadas antes da execução.

A AutoFlow possui suporte para:

* Aplicações Web;
* Aplicações Desktop;
* Aplicações Mobile.

GRAVAÇÃO INTELIGENTE

Para utilizar a gravação inteligente, o usuário inicia uma
gravação e realiza as interações desejadas na aplicação.

A AutoFlow registra essas ações durante a utilização.

Quando a gravação é encerrada, a plataforma utiliza as
interações capturadas para criar a automação correspondente.

A automação gerada pode ser revisada antes de sua execução.

GHERKIN

A AutoFlow permite utilizar Gherkin para documentar e descrever
cenários de teste.

O Gherkin é utilizado como documentação dos cenários.

O Gherkin NÃO é utilizado pela AutoFlow para gerar
automaticamente as automações.

As automações são criadas a partir das interações capturadas
durante a gravação inteligente.

AMBIENTES

A AutoFlow permite execução nos seguintes ambientes:

* SIT: System Integration Testing;
* UAT: User Acceptance Testing;
* PRD: Production.

EXECUÇÃO EM PRD

Execuções em PRD exigem aprovação prévia de um QA Lead ou
Release Manager.

As execuções em PRD devem utilizar somente massas de dados
autorizadas para testes.

MASSAS DE TESTE

A AutoFlow possui uma funcionalidade para geração de dados
de teste.

A plataforma pode gerar:

* Dados fictícios;
* Massas de teste anonimizadas.

Dados fictícios ou anonimizados podem ser utilizados nas
automações.

Dados reais sensíveis não devem ser utilizados quando houver
a possibilidade de utilizar dados fictícios ou anonimizados.

INTEGRAÇÃO COM AZURE DEVOPS

A AutoFlow possui integração com o Azure DevOps.

É possível:

* Associar uma automação a um work item do Azure DevOps;
* Consultar informações básicas do work item associado;
* Registrar o resultado da execução;
* Vincular evidências da execução ao work item correspondente.

A configuração da integração deve ser realizada por um
administrador.

Tokens e chaves de acesso não devem ser inseridos diretamente
em cenários Gherkin.

SUPORTE

Para solicitar suporte, o usuário deve acessar:

Ajuda → Abrir chamado

As categorias disponíveis são:

* Dúvida de utilização;
* Falha na gravação;
* Falha na geração da automação;
* Falha na execução;
* Problema com massa de teste;
* Indisponibilidade da plataforma;
* Problema de acesso.

Para falhas de execução, o usuário deve fornecer, quando
disponível:

* ID da automação;
* Ambiente utilizado;
* Data e horário da execução;
* Mensagem de erro;
* Logs da execução;
* Evidências da execução.

REGRA DE NÃO ALUCINAÇÃO

O contexto fornecido neste prompt é a única fonte de informação da Lili sobre a AutoFlow.

Se a informação solicitada pelo usuário não estiver presente neste contexto, não invente ou suponha uma resposta.

Nesse caso, peça desculpas de forma cordial, informe que a informação não está disponível no conhecimento atual da Lili e sugira alguns assuntos sobre os quais ela pode ajudar.

Utilize uma resposta semelhante a:

"Desculpe, não encontrei essa informação no meu conhecimento disponível sobre a AutoFlow. 😊

Posso ajudar com assuntos como:

Gravação inteligente e geração de automações;
Uso de Gherkin;
Ambientes de execução (SIT, UAT e PRD);
Massas de teste;
Integração com Azure DevOps;
Abertura de chamados e suporte.

Se quiser, posso explicar algum desses assuntos."

Não invente informações.

Não assuma que uma funcionalidade existe apenas porque ela é comum em outras plataformas de automação de testes.
"""

# ============================================================

# PROMPT DO RESUMO

# ============================================================

SUMMARY_SYSTEM_PROMPT = """
Você é responsável por resumir um atendimento da assistente Lili.

Faça um breve resumo das três perguntas feitas pelo usuário e das
respectivas informações fornecidas pela Lili.

Use exclusivamente o histórico do atendimento fornecido.

Não acrescente informações novas.
Não faça novas perguntas.

Ao final, escreva exatamente:

Atendimento encerrado.
"""

# ============================================================

# CRIAÇÃO DO CHAT

# ============================================================

def create_chat(model="gemini-3.5-flash", temperature=0):
    """
    Cria uma conversa persistente com a Lili.

    
    O system_instruction é aplicado uma única vez e o Gemini
    mantém o histórico das mensagens enviadas durante a conversa.
    """

    return client.chats.create(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=temperature
        )
    )


# ============================================================

# GERAÇÃO DO RESUMO

# ============================================================

def generate_summary(messages, model="gemini-3.5-flash"):
    """
    Gera um resumo utilizando somente o histórico do atendimento.
    """

    
    history_text = "\n\n".join(
        f"{'Usuário' if message['role'] == 'user' else 'Lili'}: "
        f"{message['content']}"
        for message in messages
        if message["role"] != "system"
    )

    summary_chat = client.chats.create(
        model=model,
        config=types.GenerateContentConfig(
            system_instruction=SUMMARY_SYSTEM_PROMPT,
            temperature=0
        )
    )

    response = summary_chat.send_message(
        f"HISTÓRICO DO ATENDIMENTO:\n\n{history_text}"
    )

    return response.text
    

# ============================================================

# INÍCIO DO ATENDIMENTO

# ============================================================

messages = [
{
"role": "system",
"content": SYSTEM_PROMPT
}
]

chat = create_chat()

print("======================================")
print("        AUTOFLOW - ASSISTENTE LILI")
print("======================================")
print()
print("Lili: Olá! Eu sou a Lili, assistente virtual da AutoFlow.")
print("Lili: Você pode fazer até 3 perguntas sobre a plataforma.")
print()

# ============================================================

# LOOP DE PERGUNTAS

# ============================================================

for numero_pergunta in range(1, 4):


    pergunta = input(f"Você ({numero_pergunta}/3): ")

    messages.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    try:

        response = chat.send_message(pergunta)
        resposta = response.text

    except Exception as erro:

        print()
        print("Lili: Não foi possível obter uma resposta do Gemini no momento.")
        print("Lili: Tente novamente em alguns instantes.")
        print()
        print(f"Detalhes técnicos: {erro}")
        break

    print()
    print(f"Lili: {resposta}")
    print()

    messages.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )


# ============================================================

# RESUMO DO ATENDIMENTO

# ============================================================

# Só gera o resumo se as três perguntas tiverem sido respondidas.

if len(messages) == 7:


    try:

        resumo = generate_summary(messages)

        print("======================================")
        print("          RESUMO DO ATENDIMENTO")
        print("======================================")
        print()
        print(f"Lili: {resumo}")

    except Exception as erro:

        print()
        print("Lili: Não foi possível obter uma resposta do Gemini no momento.")
        print("Lili: Tente novamente em alguns instantes.")
        print()
        print(f"Detalhes técnicos: {erro}")

