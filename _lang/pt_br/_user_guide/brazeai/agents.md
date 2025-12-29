---
nav_title: Agentes
article_title: Agentes de brasagem
page_order: 0.5
description: "Os Braze Agents podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes."
---

# Agentes de brasagem

> Os Braze Agents são ajudantes com tecnologia de IA que você pode criar dentro do Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes.

{% alert important %}
Os Agentes Braze estão atualmente na versão beta. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Por que usar agentes de brasagem?

Os Braze Agents ajudam sua equipe a oferecer experiências mais inteligentes e personalizadas - sem adicionar trabalho extra. Eles atuam como assistentes inteligentes que não apenas respondem a solicitações, mas entendem o contexto, tomam decisões e agem em direção a uma meta.

Na prática, os agentes podem criar automaticamente uma cópia da mensagem, como linhas de assunto ou texto no produto, para que cada cliente receba uma comunicação que pareça personalizada para ele. Eles também podem se adaptar em tempo real, encaminhando as pessoas por diferentes caminhos do Canvas com base em preferências, comportamentos ou outros dados.

Além das mensagens, os agentes podem enriquecer seus catálogos calculando ou gerando valores de campos de produtos e perfis, mantendo seus dados atualizados e dinâmicos. Ao assumir tarefas repetitivas ou complexas, eles liberam sua equipe para se concentrar na estratégia e na criatividade, em vez de na configuração manual. Os Braze Agents agem mais como colaboradores do que como processos em segundo plano - ajudando você a resolver problemas e a causar impacto em escala.

## Recursos

Os recursos dos agentes de brasagem incluem:

- **Configuração flexível:** Use um LLM fornecido pelo Braze ou conecte seu próprio provedor de modelos (como OpenAI, Anthropic, Google Gemini ou AWS Bedrock).
- **Integração perfeita:** Implante agentes diretamente nas etapas do Canvas ou nos campos do catálogo.
- **Ferramentas de teste e registro:** Visualize o resultado do seu agente testando com entradas de amostra antes de iniciar. Visualize os registros de cada vez que o agente for executado, incluindo a entrada e a saída para essa execução.
- **Controles de uso:** Os limites integrados de invocação e tamanho ajudam a gerenciar o desempenho e os custos.

## Sobre a Braze Agents

Os agentes são configurados com instruções (prompts do sistema) que definem como eles se comportam. Quando um agente é executado, ele usa suas instruções e todos os dados que você fornece para gerar uma resposta. 

### Conceitos-chave

| Prazo | Definição |
| --- | --- |
| [Modelo]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | O "cérebro" do agente, neste caso um modelo de linguagem grande (LLM). Ele interpreta entradas, gera respostas e realiza raciocínios. Um modelo mais robusto (treinado com dados mais relevantes) torna o agente mais capaz e versátil. |
| [Instruções]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | As regras ou diretrizes que você fornece ao agente (prompt do sistema). Eles definem como o agente deve se comportar sempre que for executado. Instruções claras tornam o agente mais confiável e previsível. |
| Contexto | Dados passados para o agente em tempo de execução onde quer que ele seja implantado, como campos de perfil de usuário ou linhas de catálogo. Essa entrada fornece as informações que o agente usa para gerar saídas. |
| [Variável de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | A saída que o agente produz quando usado nas etapas do Canvas. As variáveis de saída armazenam o resultado do agente para personalizar o conteúdo ou orientar os caminhos do fluxo de trabalho. As variáveis de saída podem ser do tipo de dados string, número ou booleano.  |
| Invocação | Uma única execução do agente. Isso é contabilizado em seus limites diários e totais. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

Os agentes processam solicitações a cerca de 1.000 invocações por minuto. Cada espaço de trabalho pode suportar até 1.000 agentes. Se esse limite for atingido, você precisará remover um agente existente antes de criar um novo. 

Além disso, durante o período beta:

- A invocação é limitada a 50.000 execuções por dia e 500.000 execuções no total.
- Cada corrida deve ser concluída em 30 segundos. Após 30 segundos, o agente retornará uma resposta nula quando for usado.
- Os dados de entrada são limitados a 10 KB por solicitação. Entradas mais longas são truncadas.
- Para catálogos, os campos agênticos atualizam apenas as primeiras 10.000 linhas.

## Próximas etapas

Agora que você já conhece os Braze Agents, está pronto para as próximas etapas:

- [Criação de agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Implementação de agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
