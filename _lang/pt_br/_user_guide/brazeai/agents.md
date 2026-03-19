---
nav_title: Agent Console
article_title: Agentes da Braze
page_order: 1
description: "Os agentes da Braze podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes."
---

# Agentes Braze no Console do Agente

> Os Braze Agents são assistentes alimentados por IA que você pode criar dentro do Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados de cliente para que você possa oferecer experiências mais personalizadas aos clientes.

{% alert important %}
São necessários créditos de envio de mensagens para acessar e usar o Braze Agents. Se você não tem créditos de mensagens no momento e deseja usar o Braze Agents, entre em contato com seu gerente de conta para saber as próximas etapas.
{% endalert %}

## Por que usar os agentes da Braze?

Os agentes da Braze ajudam sua equipe a oferecer experiências mais inteligentes e personalizadas, sem adicionar trabalho extra. Eles agem como agentes autônomos que não apenas respondem a comandos, mas compreendem o contexto, tomam decisões e agem em direção a um objetivo.

Na prática, os agentes podem criar automaticamente cópias de mensagens — como linhas de assunto ou texto no produto — para que cada cliente receba uma comunicação personalizada. Eles também podem se adaptar em tempo real, direcionando as pessoas por diferentes jornadas do Canvas com base em preferências, comportamentos ou outros dados.

Além do envio de mensagens, os agentes podem enriquecer seus catálogos calculando ou gerando valores de campos de produtos e perfis, mantendo seus dados atualizados e dinâmicos. Ao assumir tarefas repetitivas ou complexas, eles liberam sua equipe para se concentrar em estratégia e criatividade, em vez de configurações manuais. Os agentes da Braze atuam mais como colaboradores do que como processos em segundo plano, ajudando você a resolver problemas e causar impacto em grande escala.

### Quando usar os agentes Braze em comparação com outros recursos do BrazeAI

Use agentes para personalizar o conteúdo em tempo real, utilizando o contexto específico do usuário. Por exemplo, se um agente sabe que o sabor de sorvete favorito de um determinado usuário é chocolate e sua cobertura favorita são ursinhos de goma, ele pode criar uma mensagem específica para essa combinação para esse usuário quando ele passar pelo canva.

No entanto, o agente não aprende por tentativa e erro e não tem ideia de um objetivo final de marketing que deseja medir e maximizar. Mesmo que você peça para ele escrever textos que gerem conversões, ele não possui um mecanismo para “monitorar” o impacto de suas redações na conversão e integrar esses dados em futuras chamadas. Você pode pensar nisso como uma decisão baseada na “vibração”, e não como uma decisão de IA baseada em recompensas.

Em contrapartida, outras ferramentas da BrazeAI são projetadas para maximizar as métricas que estão medindo. Por exemplo, os agentes são muito bons em avaliar qualitativamente como as características de um usuário influenciam sua probabilidade ou propensão a realizar uma determinada ação ou gostar de um determinado produto. No entanto, como o agente não aprende por meio de tentativa e erro, ele não tem ideia de como medir sua precisão na previsão de probabilidades e melhorar o sinal ao longo do tempo. Assim, o uso do Predictive Suite supera a etapa do Agente quando avaliado pela precisão de suas previsões e melhorias ao longo do tempo.

## Recursos

Os recursos para os agentes da Braze incluem:

- **Configuração flexível:** Use um LLM fornecido pela Braze ou conecte seus próprios [provedores de modelos de IA]({{site.baseurl}}/partners/ai_model_providers) (como OpenAI, Anthropic ou Google Gemini).
- **Integração perfeita:** Implemente agentes diretamente nas etapas do canva ou nos campos do catálogo.
- **Ferramentas de teste e registro:** Prévia do resultado do seu agente testando com entradas de amostra antes de iniciar. Visualize os registros de cada vez que o agente é executado, incluindo a entrada e a saída dessa execução.
- **Controles de uso:** Os limites diários ajudam a gerenciar a performance e os custos.

## Sobre os agentes da Braze

Os agentes são configurados com instruções (solicitações do sistema) que definem como eles se comportam. Quando um agente é executado, ele usa suas instruções juntamente com quaisquer dados que você passar para gerar uma resposta.

### Conceitos-chave

| Prazo | Definição |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) | O “cérebro” do agente, neste caso, um grande modelo de linguagem (LLM). Ele interpreta entradas, gera respostas e realiza raciocínios. Um modelo mais robusto (treinado com dados mais relevantes) torna o agente mais capaz e versátil. |
| [Instruções]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) | As regras ou diretrizes que você fornece ao agente (solicitação do sistema). Eles definem como o agente deve se comportar cada vez que é executado. Instruções claras tornam o agente mais confiável e previsível. |
| Contexto | Dados passados para o agente em tempo de execução, onde quer que ele esteja implantado, como campos de perfil do usuário ou linhas de catálogo. Essa entrada fornece as informações que o agente usa para gerar saídas. |
| [Variável de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#define-the-output-variable) | A saída que o agente produz quando usado nas etapas do canva. As variáveis de saída armazenam o resultado do agente para personalizar o conteúdo ou orientar as jornadas do fluxo de trabalho. As variáveis de saída podem ser uma string, um número ou um tipo de dados booleano.  |
| [Execução](#limitations) | Uma única execução do agente. Isso conta para os seus limites diários. |
| [Formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#select-output) | A estrutura de dados predefinida da resposta do agente. |
| [Temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) | O nível de desvio para a produção do agente. Isso define o nível de precisão ou criatividade do seu agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

Aplicam-se as seguintes limitações:

- Cada agente tem um limite diário padrão de execução de 250.000 execuções, que pode ser aumentado até um máximo de 1.000.000 de execuções por dia. Entre em contato com seu gerente de sucesso do cliente se estiver interessado em aumentar esse limite.
- Por padrão, cada execução deve ser concluída em 15 segundos. Após 15 segundos, o agente retorna uma`null`resposta onde é usado.
    - Se seus agentes estiverem constantemente excedendo o tempo limite, entre em contato com o gerente da sua conta Braze para aumentar esse limite.
- Os dados de entrada estão limitados a 25 KB por solicitação. Entradas mais longas são truncadas.

## Como meus dados são usados e enviados para os LLMs fornecidos pela Braze?

Para gerar resultados de IA por meio dos recursos de IA da Braze que a Braze identifica como aproveitando os LLMs fornecidos pela Braze (“Resultados”), a Braze enviará o prompt do seu sistema ou qualquer outra entrada, conforme aplicável (“Entrada”), para o Braze LLM fornecido pela Braze. Os dados enviados para o Braze LLM não são utilizados para treinar ou melhorar o Braze LLM. Entre você e a Braze, a Produção é sua propriedade intelectual. Braze não reivindicará quaisquer direitos de propriedade intelectual sobre tais Resultados. Braze não oferece qualquer tipo de garantia em relação a qualquer conteúdo gerado por IA em geral, incluindo a Saída.

O LLM fornecido pela Braze para os agentes da Braze, identificado como “Auto”, utiliza modelos Google Gemini. O Google retém as entradas e saídas enviadas através do Braze por 55 dias, após os quais os dados são eliminados.

## Próximos passos

Agora que você já conhece os Braze Agents, está pronto para as próximas etapas:

- [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Implemente agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
