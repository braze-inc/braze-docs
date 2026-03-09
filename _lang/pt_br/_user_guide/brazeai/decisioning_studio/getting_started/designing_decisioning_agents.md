---
nav_title: Projetando agentes de tomada de decisão
article_title: Projetando agentes de tomada de decisão
page_order: 4
page_type: reference
description: "Este artigo de referência aborda os principais conceitos e as melhores práticas para projetar e configurar seu agente de tomada de decisão."
---

# Projetando agentes de tomada de decisão

> Este artigo de referência aborda os principais conceitos e as melhores práticas para projetar e configurar seu agente de tomada de decisão.

## Sobre os agentes de decisão

Projetar seu agente de decisão é a primeira etapa para configurar o Decisioning Studio. Para que o agente decisório possa tomar decisões, você precisa definir qual resultado deseja maximizar e quais ações o agente pode realizar para isso.

### Conceitos-chave

Os seguintes termos são referenciados ao longo do guia do Decisioning Studio.

| Prazo | Definição |
| --- | --- |
| **Agente decisório** | Um agente de decisão é uma configuração personalizada para o BrazeAI Decisioning Studio™, feita sob medida para atender a uma meta comercial específica. Isso é definido pela métrica de sucesso, dimensões e opções que você escolher. |
| **Métrica de sucesso** | A métrica de negócios específica que você deseja otimizar, como receita, conversões ou receita média por usuário (ARPU). Esta é a métrica que o agente decisório procurará maximizar através de suas ações. |
| **Dimensões** | As dimensões podem ser consideradas como os *tipos de alavancas* que o agente decisório pode acionar para maximizar a métrica de sucesso. As dimensões típicas incluem oferta, linha de assunto, criativo, canal ou hora de envio. |
| **Banco de Ação** | O banco de ações define as *opções específicas* às quais o agente decisório tem acesso para cada dimensão “alavanca”. Por exemplo, para uma dimensão de canal, você definiria os canais específicos aos quais o agente de decisão tem acesso. Para uma dimensão de oferta, você definiria as ofertas específicas que o agente de decisão pode testar. 
| **Restrições** | Em geral, o agente de decisão pode tomar qualquer combinação de ações que você colocar no banco de ações. No entanto, você também pode definir restrições para limitar as ações do agente de decisão, a fim de respeitar regras comerciais críticas. Por exemplo, isso poderia impedir que uma oferta específica fosse selecionada para clientes em uma região geográfica inelegível ou definir um orçamento máximo para o agente de decisão gastar. 
{: .reset-td-br-1 .reset-td-br-2}

![Uma visão geral de alto nível de um agente de tomada de decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
O agente de decisão só pode realizar ações que *você* configurar e adicionar ao banco de ações. Isso significa que todas as ações possíveis são definidas pelas combinações do que você coloca no banco de ações.
{% endalert %}

## Como projetar seu agente de tomada de decisão

Ao configurar um agente de decisão, você precisará considerar quatro elementos principais de design:

### O "objetivo": Defina sua métrica de sucesso

> Que resultado você deseja que o agente maximize?

Sua métrica de sucesso é o resultado comercial que o agente otimizará. Isso deve estar diretamente alinhado com seus objetivos de negócios — não com métricas indiretas, como cliques ou aberturas, mas com resultados comerciais reais, como receita, conversões, ARPU ou valor do tempo de vida do cliente.

### O "quem": Selecione seu público

> Quem será o objeto do engajamento do agente decisório?

Defina o público que seu agente irá atender. Isso pode incluir todos os clientes, um segmento específico (como membros do programa de fidelidade) ou clientes em um determinado estágio do ciclo de vida (como compradores recentes ou assinantes em risco).

### O "quê": Configure seu banco de ações

> Quais opções o agente pode escolher para impulsionar o resultado?

O banco de ações define todas as alavancas que o agente pode acionar — as dimensões (como canal, oferta, tempo e frequência) e as opções específicas dentro de cada dimensão. O agente experimenta diferentes combinações dessas opções para descobrir o que funciona melhor para cada cliente.

### O "como": Configure suas restrições

> Que regras o agente deve seguir?

Restrições são as regras que o agente deve seguir. Isso pode impedir que uma oferta específica seja selecionada para clientes em uma região geográfica inelegível ou definir um orçamento máximo para o agente de decisão gastar.

## Melhores práticas e exemplos

Para maximizar o impacto do seu agente de decisão, você deve:

- Escolha uma métrica de sucesso que esteja alinhada com suas metas comerciais e objetivos, como receita, conversões ou ARPU.
- Concentre-se nas dimensões ou “alavancas” a testar, tais como oferta, assunto, criatividade, canal ou hora de envio, que são mais suscetíveis de ter um impacto significativo na métrica de sucesso.
- Selecione as opções para cada dimensão, como e-mail versus SMS ou frequência diária versus semanal, que provavelmente terão um impacto significativo na métrica de sucesso.

Alguns exemplos de agentes de decisão que você poderia criar são:

{% tabs %}
{% tab Repeat purchase agent %}
Você poderia criar um agente de compras repetidas para aumentar as conversões de acompanhamento após uma venda inicial:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de ofertas de produtos, tempo de envio de mensagens e frequência para cada cliente.
- Com o tempo, o BrazeAI™ aprende o que funciona melhor para cada cliente.
- Orquestra envios personalizados através do Braze para maximizar as taxas de recompra
{% endtab %}
{% tab Cross-sell or upsell agent %}
Você poderia criar um agente de vendas cruzadas ou vendas adicionais para maximizar a receita média por usuário (ARPU) das inscrições de internet:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de mensagens, horários de envio, descontos e ofertas de planos para cada cliente.
- O BrazeAI™ aprende quais clientes são suscetíveis a ofertas de salto e quais exigem descontos ou outros incentivos para fazer upgrade.
- Orquestra envios personalizados através do Braze para maximizar a ARPU
{% endtab %}
{% tab Renewal and retention agent %}
Você poderia criar um agente de renovação e retenção para garantir renovações de contrato, maximizando tanto a duração do contrato quanto o valor presente líquido (VPL):

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas de renovação para cada cliente.
- O BrazeAI™ identifica clientes que são menos sensíveis ao preço e precisam de descontos menos significativos para renovar.
- Orquestra envios personalizados através do Braze para maximizar renovações de contratos e NPV
{% endtab %}
{% tab Winback agent %}
Você poderia criar um agente de reconquista para aumentar a reativação, incentivando os assinantes antigos a se inscreverem novamente:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando milhares de variáveis ao mesmo tempo, incluindo criatividade, mensagem, canal e cadência.
- O BrazeAI™ descobre a melhor combinação para cada cliente individualmente.
- Orquestra envios personalizados através do Braze para maximizar as taxas de reativação
{% endtab %}
{% tab Referral agent %}
Você poderia criar um agente de referência para maximizar a abertura de novas contas por meio de referências de cartões de crédito empresariais de clientes existentes:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes e-mails, criativos, horários de envio e ofertas de cartão de crédito para cada cliente.
- O BrazeAI™ determina a combinação ideal para clientes específicos.
- Orquestra envios personalizados através do Braze para maximizar as conversões de referências.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Você poderia criar um agente de nutrição e conversão de leads para impulsionar o aumento da receita e pagar o valor certo por cada cliente:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes segmentos de clientes, metodologias de licitação, níveis de licitação e criatividade.
- A BrazeAI™ utiliza dados primários robustos para otimizar a performance dos anúncios pagos à medida que as políticas de privacidade mudam.
- Orquestra envios personalizados através do Braze para maximizar a receita e otimizar o custo por cliente.
{% endtab %}
{% tab Loyalty and engagement agent %}
Você poderia criar um agente de fidelidade e engajamento para maximizar as compras de novos inscritos em um programa de fidelidade do cliente:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas de e-mail, horários de envio e frequências para cada cliente.
- O BrazeAI™ aprende o que funciona melhor para cada novo inscrito no programa de fidelidade.
- Orquestra envios personalizados através do Braze para maximizar as taxas de compra e recompra.
{% endtab %}
{% endtabs %}

## Próximos passos

Pronto para criar seu próprio agente de tomada de decisão? Siga as etapas a seguir para o seu nível do Decisioning Studio:

- **Decisão do Studio Go**: [Configurar o Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Configurar o Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Esses guias orientam você na conexão de fontes de dados, na configuração da orquestração, no projeto do seu agente e no lançamento para produção.
