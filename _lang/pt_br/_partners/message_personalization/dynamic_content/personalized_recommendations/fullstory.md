---
nav_title: História completa
article_title: História completa
description: "Este artigo de referência descreve a parceria entre a Braze e a Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# História completa

A plataforma de dados comportamentais da Fullstory ajuda os líderes de tecnologia a tomar decisões melhores e mais bem informadas. Ao injetar dados comportamentais digitais em seu stack de análises, a tecnologia patenteada da Fullstory libera o poder dos dados comportamentais de qualidade em escala, transformando cada visita digital em insights práticos. 

*Essa integração é mantida pela Fullstory*

## Sobre essa integração
Você pode aproveitar os insights da Fullstory no Braze para criar imagens momento a momento da experiência de um usuário no site ou no app para fornecer mensagens hipercontextuais. A API de resumo de sessão da Fullstory possibilita a captura de metadados detalhados sobre o comportamento de navegação de um usuário para uso no envio de mensagens do Braze, o que é particularmente poderoso quando aproveitado em uma jornada de mensagens de várias etapas, como um Canva. 

O valor em tempo real dos dados do Resumo da Sessão da Fullstory é melhor aproveitado por meio do Conteúdo Conectado. Ao usar o conteúdo conectado em uma etapa do Canvas Context, é possível armazenar os dados da Fullstory durante toda a jornada do usuário no Canvas para uso em qualquer etapa subsequente do Canvas. Isso também evita a necessidade de gravar esses dados em um perfil de usuário do Braze por meio de eventos ou atributos personalizados. 

No exemplo a seguir, os dados do Canvas Context são aproveitados em uma etapa do Canva da IA do agente para gerar a mensagem ideal para incentivar um usuário a pegar de volta um carrinho abandonado. No entanto, é possível aproveitar os dados para personalizar a mensagem diretamente, para determinar a jornada do usuário por meio de jornadas do público ou para determinar a cópia ou os ativos usados nas etapas subsequentes do envio de mensagens.

## Casos de uso

![Diagrama mostrando casos de uso de integração da Fullstory com o Braze]({% image_buster /assets/img/fullstory/1.png %})

## Pré-requisitos

Antes de começar, você precisa dos seguintes itens:

|Requisito     | Descrição |                        
|-----------------------|-----------------|
| Um token de autorização da API da sessão Fullstory   | Consulte a etapa 1 abaixo.  | 
| Um token de autorização de conteúdo conectado Braze ativado | Veja a nota abaixo sobre o Acesso Antecipado |
| Etapa do contexto do Braze Canvas |Veja a nota abaixo sobre o Acesso Antecipado |
| Etapa de capacitação do Braze IA Agent | Veja a nota abaixo sobre o Acesso Antecipado|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integrando o Fullstory

### Etapa 1: Configure o Fullstory para ativar a API de resumo de sessão

#### A: Recuperação do [token](https://developer.fullstory.com/server/authentication/) de autenticação para o ponto de extremidade da API Session Summary

Para criar uma chave de API da Fullstory, navegue até a plataforma da Fullstory e, em seguida, **Configurações** > **Chaves de API**. Selecione o nível de permissão **Standard** e copie imediatamente o valor da chave, pois ele aparece apenas uma vez.

#### B: Criação de um resumo da sessão ID do perfil

Seguindo [as orientações da Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), crie um perfil de resumo da sessão usando o endpoint dedicado. É aqui que você define o tipo de dados que deseja que a resposta do Resumo da sessão forneça ao Braze.
Na resposta a essa solicitação, a Fullstory fornece um "ID de perfil" de sessão. Esse ID de perfil é um componente-chave do corpo da solicitação de conteúdo conectado usado no seguinte caso de uso.


### Etapa 2: Criar a autenticação do token de conteúdo conectado
1. No Braze, navegue até **Configurações > Configurações do espaço de trabalho > Conteúdo conectado > Adicionar credencial > Autenticação por token**. 

2. Nomeie a autenticação como "fullstory".

3. Adicione a chave de cabeçalho "Authorization". Forneça o valor do cabeçalho Fullstory fornecido na etapa anterior. 

4. Em Allowed Domain (Domínio permitido), envie "api.fullstory.com".

![Captura de tela do Braze mostrando os campos Editar credencial]({% image_buster /assets/img/fullstory/2.png %})

## Caso de uso: Aproveite os dados de resumo da sessão do Fullstory e as etapas do contexto do Braze Canvas e os agentes de IA para criar jornadas dinâmicas de mensagens

Usando os [fluxos de ativação](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) da Fullstory, é possível disparar Braze Canvases imediatamente após as principais interações do usuário. O poder dessa integração está no site exclusivo `client_session_id` (acessível via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que o sistema passa automaticamente do Fullstory para o Braze. Esse ID funciona como uma chave, permitindo que o Braze busque o resumo completo da sessão, exatamente o que o usuário experimentou. 

Ao aproveitar as etapas do Canva Context e o Connected Content, você pode usar essa ID para fazer uma solicitação de API à Fullstory, recuperar os dados da sessão e armazená-los como uma variável para uso posterior na jornada. 

![Captura de tela da etapa do contexto do Braze Canvas mostrando a variável de contexto `summary_result` sendo criada e preenchida com uma chamada de conteúdo conectado ao Fullstory, para recuperar um resumo da sessão]({% image_buster /assets/img/fullstory/3.png %})

Com o token de autorização criado anteriormente, use a seguinte estrutura de solicitação para extrair os dados do resumo da sessão. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 A resposta é armazenada como a tag Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Usamos essa tag Context nas etapas subsequentes do Canva.
{% endalert %}

Nesse estágio, a tela pode acessar a resposta à chamada Connected Content, que contém toda a carga útil da mensagem para a sessão de um usuário.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

É possível aproveitar qualquer um dos dados disponíveis no objeto acima usando a tag Liquid do contexto posteriormente na jornada do usuário no Canva. As etapas a seguir mostram como você pode usar esses dados em uma etapa do Canva [do IA Agent](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step).

{% alert Note %}
Para evitar comportamentos inesperados, inclua uma jornada do público após a etapa Context, que pode retirar os usuários do contexto se a tag Context estiver vazia, indicando que a chamada de conteúdo conectado falhou ou não retornou nenhuma informação.

![Captura de tela da etapa do público do Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Crie um IA Agent que possa analisar as cargas úteis da Fullstory e produzir uma cópia apropriada para seu caso de uso

[O guia de agentes do Braze]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) descreve como os usuários do Braze podem criar agentes de IA. Ao inserir uma etapa do IA Agent em um Canvas disparado pelo Fullstory e incluir a etapa do Canvas Context descrita acima, os usuários podem alimentar o IA Agent com dados de resumo da sessão do Fullstory, para uma ampla gama de finalidades. 

Neste exemplo, usamos esses dados para permitir que o IA Agent gere uma cópia de mensagem apropriada para uso em um cartão de conteúdo, o que pode incentivar o usuário a retornar à cesta abandonada.

![Captura de tela do criador de contexto do Braze Agent com o prompt]({% image_buster /assets/img/fullstory/4.png %})

Use o mesmo nome para a tag Context Liquid criada nesta etapa que a tag Context Liquid usada na etapa IA Agent criada anteriormente. 

O prompt necessário para o seu caso de uso varia, mas para conhecer nossas práticas recomendadas para a criação de prompts de agente eficazes, consulte [Instruções de redação]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) na *criação de agentes*. 


Em sua tela, selecione uma etapa do IA Agent e, em seguida, selecione o agente "Session Context" criado no menu suspenso. Salve a saída como uma variável, nesse caso "message", que pode ser colocada na cópia da mensagem usando a tag Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Captura de tela da etapa do canva de contexto do Braze Agent com o prompt]({% image_buster /assets/img/fullstory/5.png %})

Crie uma etapa de mensagem que aproveite a cópia criada pelo IA Agent. Use a tag Liquid nessa etapa. 

{% alert Note %}

A API Session Summary da Fullstory pode retornar dados de usuários identificáveis e confidenciais. Para garantir a conformidade ao lidar com IPI (informações de identificação pessoal), certifique-se de que as regras de captura de dados do Fullstory excluam IPI antes de usar esse caso de uso.

{% endalert %}