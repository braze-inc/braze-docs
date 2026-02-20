---
nav_title: Projetando agentes de decisão
article_title: Projetando agentes de decisão
page_order: 4
page_type: reference
description: "Este artigo de referência cobre conceitos-chave e melhores práticas para projetar e configurar seu agente de decisão."
---

# Projetando agentes de decisão

> Este artigo de referência cobre conceitos-chave e melhores práticas para projetar e configurar seu agente de decisão.

## Sobre agentes de decisão

Projetar seu agente de decisão é o primeiro passo para configurar o Decisioning Studio. Para que o agente de decisão possa tomar decisões, você precisa definir qual resultado deseja maximizar e quais ações o agente pode tomar para isso.

### Conceitos-chave

Os seguintes termos são referenciados ao longo do guia do Decisioning Studio.

| Prazo | Definição |
| --- | --- |
| **Agente de decisão** | Um agente de decisão é uma configuração personalizada para o BrazeAI Decisioning Studio™ que é feita sob medida para atender a uma meta comercial específica. Isso é definido pela métrica de sucesso, dimensões e opções que você escolher. |
| **Métrica de sucesso** | A métrica comercial específica que você deseja otimizar, como receita, conversões ou receita média por usuário (ARPU). Esta é a métrica que o agente de decisão buscará maximizar por meio de suas ações. |
| **Dimensões** | As dimensões podem ser pensadas como os *tipos de alavancas* que o agente de decisão pode acionar para maximizar a métrica de sucesso. As dimensões típicas incluem oferta, linha de assunto, criativo, canal ou horário de envio. |
| **Banco de Ações** | O banco de ações define as *opções específicas* às quais o agente de decisão tem acesso para cada "alavanca" de dimensão. Por exemplo, para uma dimensão de canal, você definiria os canais específicos aos quais o agente de decisão tem acesso. Para uma dimensão de oferta, você definiria as ofertas específicas que o agente de decisão pode testar. 
| **Restrições** | Em geral, o agente de decisão poderia tomar qualquer combinação de ações que você colocar no banco de ações. No entanto, você também pode definir restrições para limitar as ações do agente de decisão a respeitar regras de negócios críticas. Por exemplo, isso poderia ser impedir que uma oferta específica seja selecionada para clientes em uma geografia não elegível, ou definir um orçamento máximo para o agente de decisão gastar. 
{: .reset-td-br-1 .reset-td-br-2}

![Uma visão geral de alto nível de um agente de decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
O agente de decisão só pode tomar ações que *você* configurar e adicionar ao banco de ações. Isso significa que todas as ações possíveis são definidas pelas combinações do que você coloca no banco de ações.
{% endalert %}

## Como projetar seu agente de decisão

Ao configurar um agente de decisão, você precisará pensar em quatro elementos principais de design:

### O "objetivo": Defina sua métrica de sucesso

> Qual resultado você deseja que o agente maximize?

Sua métrica de sucesso é o resultado de negócios que o agente irá otimizar. Isso deve alinhar-se diretamente com seus objetivos de negócios—não métricas proxy como cliques ou aberturas, mas resultados reais de negócios como receita, conversões, ARPU ou valor do tempo de vida do cliente.

### O "quem": Selecione seu público

> Quem o agente de decisão irá engajar?

Defina o público que seu agente irá atender. Isso pode ser todos os clientes, um segmento específico (como membros do programa de fidelidade), ou clientes em uma fase particular de seu ciclo de vida (como compradores recentes ou assinantes em risco).

### O "quê": Configure seu banco de ações

> Quais opções o agente pode escolher para impulsionar o resultado?

O banco de ações define todas as alavancas que o agente pode puxar— as dimensões (como canal, oferta, timing e frequência) e as opções específicas dentro de cada dimensão. O agente experimenta diferentes combinações dessas opções para encontrar o que funciona melhor para cada cliente.

### O "como": Configure suas restrições

> Quais regras o agente deve seguir?

Restrições são as regras que o agente deve seguir. Isso pode ser impedir que uma oferta específica seja selecionada para clientes em uma geografia não elegível, ou definir um orçamento máximo para o agente de decisão gastar.

## Melhores práticas e exemplos

Para maximizar o impacto do seu agente de decisão, você deve:

- Escolher uma métrica de sucesso que esteja alinhada com seus objetivos e metas de negócios, como receita, conversões ou ARPU.
- Focar nas dimensões, ou "alavancas" a serem testadas, como oferta, linha de assunto, criativo, canal ou horário de envio, que são mais propensas a ter um impacto significativo na métrica de sucesso.
- Selecionar as opções para cada dimensão, como e-mail versus SMS, ou frequência diária versus semanal, que são mais propensas a ter um impacto significativo na métrica de sucesso.

Alguns exemplos de agentes de decisão que você poderia construir são:

{% tabs %}
{% tab Repeat purchase agent %}
Você poderia construir um agente de recompra para aumentar as conversões de acompanhamento após uma venda inicial:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de ofertas de produtos, horários de mensagens e frequência para cada cliente
- Com o tempo, o BrazeAI™ aprende o que funciona melhor para cada cliente
- Orquestra envios personalizados através do Braze para maximizar as taxas de recompra
{% endtab %}
{% tab Cross-sell or upsell agent %}
Você poderia construir um agente de cross-sell ou upsell para maximizar a receita média por usuário (ARPU) de assinaturas de internet:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes combinações de mensagens, horários de envio, descontos e ofertas de planos para cada cliente
- O BrazeAI™ aprende quais clientes são suscetíveis a ofertas de leapfrog e quais precisam de descontos ou outros incentivos para fazer upgrade
- Orquestra envios personalizados através do Braze para maximizar o ARPU
{% endtab %}
{% tab Renewal and retention agent %}
Você poderia construir um agente de renovação e retenção para garantir renovações de contrato, maximizando tanto a duração do contrato quanto o valor presente líquido (NPV):

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas de renovação para cada cliente
- O BrazeAI™ identifica clientes que são menos sensíveis a preços e precisam de descontos menos significativos para renovar
- Orquestra envios personalizados através do Braze para maximizar renovações de contrato e NPV
{% endtab %}
{% tab Winback agent %}
Você poderia construir um agente de recuperação para aumentar a reativação, incentivando assinantes anteriores a se reinscreverem:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando milhares de variáveis de uma vez, incluindo criativos, mensagens, canais e cadência
- O BrazeAI™ descobre a melhor combinação para cada cliente individual
- Orquestra envios personalizados através do Braze para maximizar taxas de reativação
{% endtab %}
{% tab Referral agent %}
Você poderia construir um agente de referência para maximizar novas contas abertas através de referências de cartões de crédito empresariais de clientes existentes:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes e-mails, criativos, horários de envio e ofertas de cartões de crédito para cada cliente
- O BrazeAI™ determina a combinação ideal para clientes específicos
- Orquestra envios personalizados através do Braze para maximizar conversões de referência
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Você poderia construir um agente de nutrição e conversão de leads para gerar receita incremental e pagar o valor certo por cada cliente:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes segmentos de clientes, metodologia de lances, níveis de lance e criativos
- O BrazeAI™ aproveita dados robustos de primeira parte para otimizar o desempenho de anúncios pagos à medida que as políticas de privacidade mudam
- Orquestra envios personalizados através do Braze para maximizar a receita enquanto otimiza o custo por cliente
{% endtab %}
{% tab Loyalty and engagement agent %}
Você poderia construir um agente de fidelidade e engajamento para maximizar compras por novos inscritos em um programa de fidelidade:

- Defina o público e a mensagem no Braze
- O Decisioning Studio executa automaticamente experimentos diários, testando diferentes ofertas de e-mail, horários de envio e frequências para cada cliente
- O BrazeAI™ aprende o que funciona melhor para cada novo inscrito no programa de fidelidade
- Orquestra envios personalizados através do Braze para maximizar taxas de compra e recompra
{% endtab %}
{% endtabs %}

## Próximos passos

Pronto para construir seu próprio agente de decisão? Siga os próximos passos para o seu nível do Decisioning Studio:

- **Decisioning Studio Go**: [Configurar o Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Configurar o Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Esses guias o orientam sobre como conectar fontes de dados, configurar a orquestração, projetar seu agente e lançar em produção.
