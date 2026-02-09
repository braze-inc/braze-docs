---
nav_title: Agentes
article_title: Agentes da Braze
page_order: 0.5
description: "Os Agentes Braze podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes."
---

# Agentes da Braze

> Os Agentes Braze são assistentes impulsionados por IA que você pode criar dentro do Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes.

{% alert important %}
Os Agentes Braze estão atualmente em beta. Para obter ajuda para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Por que usar Agentes Braze?

Os Agentes Braze ajudam sua equipe a oferecer experiências mais inteligentes e personalizadas—sem adicionar trabalho extra. Eles atuam como assistentes inteligentes que não apenas respondem a solicitações, mas entendem o contexto, tomam decisões e agem em direção a um objetivo.

Na prática, os agentes podem criar automaticamente cópias de mensagens—como linhas de assunto ou texto dentro do produto—para que cada cliente receba uma comunicação que pareça feita sob medida para ele. Eles também podem se adaptar em tempo real, direcionando as pessoas por diferentes caminhos no Canvas com base em preferências, comportamentos ou outros dados.

Além do envio de mensagens, os agentes podem enriquecer seus catálogos calculando ou gerando valores de campos de produtos e perfis, mantendo seus dados atualizados e dinâmicos. Ao assumir tarefas repetitivas ou complexas, eles liberam sua equipe para se concentrar em estratégia e criatividade em vez de configuração manual. Os Agentes Braze agem mais como colaboradores do que processos em segundo plano—ajudando você a resolver problemas e gerar impacto em escala.

### Quando usar Agentes Braze em vez de outros recursos do BrazeAI

Use agentes para personalizar conteúdo instantaneamente usando o contexto específico de um usuário. Por exemplo, se um agente sabe que o sabor de sorvete favorito de um usuário específico é chocolate e a cobertura favorita são ursinhos de goma, ele pode criar uma cópia de push específica para essa combinação para esse usuário enquanto ele passa pelo Canvas.

No entanto, o agente não aprende por tentativa e erro, e não tem ideia de um objetivo de marketing final que está tentando medir e maximizar. Mesmo que você diga a ele para escrever geralmente cópias que gerem conversões, ele não tem um mecanismo para "monitorar" o impacto de conversão de sua escrita e integrar esses dados de volta em futuras chamadas de agente. Você pode pensar nisso como uma decisão de "vibe", não uma decisão de IA baseada em recompensas.

Em contraste, outras ferramentas BrazeAI são projetadas para maximizar as métricas que estão medindo. Por exemplo, os agentes são muito bons em avaliar qualitativamente como as características de um usuário influenciam sua probabilidade ou propensão a realizar um certo evento ou gostar de um certo produto. No entanto, como o agente não aprende por tentativa e erro, ele não tem ideia de como medir sua precisão em prever probabilidades e melhorar o sinal ao longo do tempo. Assim, usar o Predictive Suite supera a etapa do Agente quando julgado pela precisão de suas previsões e melhorias ao longo do tempo.

## Recursos

Recursos para Agentes Braze incluem:

- **Configuração flexível:** Use um LLM fornecido pela Braze ou conecte seu próprio provedor de modelo (como OpenAI, Anthropic, Google Gemini ou AWS Bedrock).
- **Integração perfeita:** Implante agentes diretamente em etapas do Canvas ou campos de catálogo.
- **Ferramentas de teste e registro:** Prévia da saída do seu agente testando com entradas de amostra antes de lançar. Veja os registros para cada vez que o agente é executado, incluindo a entrada e a saída daquela execução.
- **Controles de uso:** Limites diários ajudam a gerenciar desempenho e custos.

## Sobre os Agentes Braze

Os agentes são configurados com instruções (prompts do sistema) que definem como eles se comportam. Quando um agente é executado, ele usa suas instruções junto com quaisquer dados que você passar para gerar uma resposta. 

### Conceitos-chave

| Prazo | Definição |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | O "cérebro" do agente, neste caso, um grande modelo de linguagem (LLM). Ele interpreta entradas, gera respostas e realiza raciocínios. Um modelo mais forte (treinado com dados mais relevantes) torna o agente mais capaz e versátil. |
| [Instruções]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | As regras ou diretrizes que você dá ao agente (prompt do sistema). Elas definem como o agente deve se comportar cada vez que é executado. Instruções claras tornam o agente mais confiável e previsível. |
| Contexto | Dados passados para o agente em tempo de execução, onde quer que ele seja implantado, como campos de perfil de usuário ou linhas de catálogo. Essa entrada fornece as informações que o agente usa para gerar saídas. |
| [Variável de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | A saída que o agente produz quando usado em etapas do Canvas. Variáveis de saída armazenam o resultado do agente para personalizar conteúdo ou guiar caminhos de fluxo de trabalho. Variáveis de saída podem ser um tipo de dado string, número ou booleano.  |
| [Execução](#limitations) | Uma única execução do agente. Isso conta contra seus limites diários. |
| [Formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) | A estrutura de dados predefinida da resposta do agente. |
| [Temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) | O nível de desvio para a saída do agente. Isso define quão preciso ou criativo seu agente pode ser. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

Durante o período beta, as seguintes limitações se aplicam:

- Cada agente tem um limite diário padrão de execução de 50.000 execuções, que pode ser aumentado até um máximo de 100.000 execuções por dia.
- Por padrão, cada execução deve ser concluída em 15 segundos. Após 15 segundos, o agente retorna uma resposta `null` onde é utilizado. 
    - Se seus agentes constantemente atingirem o limite de tempo, entre em contato com seu gerente de conta Braze para aumentar esse limite.
- Os dados de entrada são limitados a 25 KB por solicitação. Entradas mais longas são truncadas.

## Próximos passos

Agora que você sabe sobre os Agentes Braze, está pronto para os próximos passos:

- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Implantar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

## Modelos como Subprocessadores ou Fornecedores de Terceiros

Onde o Cliente usa uma integração com modelos fornecidos pela Braze através dos Serviços Braze (“LLM fornecido pela Braze”), os fornecedores de tais LLMs fornecidos pela Braze atuarão como Subprocessadores da Braze, sujeitos aos termos do Aditivo de Processamento de Dados (DPA) entre o Cliente e a Braze. 

Se o Cliente optar por trazer sua própria chave de API para integrar com a funcionalidade de IA da Braze, o fornecedor da assinatura LLM do Cliente será considerado um Fornecedor de Terceiros, conforme definido no contrato entre o Cliente e a Braze. 

### Como meus dados são usados e enviados para LLMs fornecidos pela Braze?

Para gerar saída de IA através dos recursos de IA da Braze que a Braze identifica como aproveitando LLMs fornecidos pela Braze (“Saída”), a Braze enviará seu prompt de sistema ou qualquer outra entrada, conforme aplicável (“Entrada”) para o LLM fornecido pela Braze. Os dados enviados para o LLM fornecido pela Braze aplicável não são usados para treinar ou melhorar o LLM fornecido pela Braze. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará qualquer direito de propriedade autoral sobre tal Saída. A Braze não oferece garantia de qualquer tipo em relação a qualquer conteúdo gerado por IA em geral, incluindo a Saída.

O LLM fornecido pela Braze para Agentes Braze, identificado como “Auto”, usa modelos Google Gemini. O Google retém Entradas e Saídas enviadas através da Braze por 55 dias, após os quais os dados são excluídos.
