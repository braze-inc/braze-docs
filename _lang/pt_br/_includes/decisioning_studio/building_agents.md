# Criação de agentes

> Saiba como criar um agente para o BrazeAI Decisioning Studio™, para que você possa automatizar a experimentação personalizada e otimizar resultados como conversões, retenção ou receita, sem testes A/B manuais.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Sobre os agentes

Um agente de tomada de decisão de IA é uma configuração personalizada para o mecanismo de tomada de decisão BrazeAI™ que é feito sob medida para atender a um objetivo comercial específico.

Por exemplo, você pode criar um agente de compras repetidas para aumentar as conversões de acompanhamento após uma venda inicial. Você define o público e a mensagem na Braze, enquanto seus agentes de decisão executam experimentos diários e testam automaticamente diferentes combinações de ofertas de produtos, tempo de mensagem e frequência para cada cliente. Com o tempo, a BrazeAI™ aprende o que funciona melhor e orquestra envios personalizados por meio da Braze para maximizar as taxas de recompra.

Para formar um bom agente, você deverá:

- Escolher uma métrica de sucesso para otimizar a BrazeAI™, como receita, conversões ou ARPU.
- Definir quais dimensões serão testadas, como oferta, linha de assunto, criativo, canal ou horário de envio.
- Selecionar as opções para cada dimensão, como e-mail versus SMS, ou frequência diária versus semanal.

![Exemplo de diagrama de um agente de estúdio de decisão para envios de e-mail de referência.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Agentes de amostra

Aqui estão alguns exemplos de agentes que você pode criar com o BrazeAI Decisioning Studio™. Seus agentes de decisão com IA aprenderão com cada interação com o cliente e aplicarão esses insights às ações do dia seguinte.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Criação de um agente

### Pré-requisitos

Antes de criar um agente, você precisará [integrar o BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration).

### Etapa 1: Entre em contato com a AI Expert Services

A equipe trabalhará em conjunto com você para definir o escopo, projetar e construir o seu agente de decisão. Se ainda não fez isso, entre em [contato](https://www.braze.com/get-started/) para começar.

Vocês concluirão juntos as etapas a seguir para criar um agente personalizado adequado para você.

### Etapa 2: Crie seu agente

Juntamente com a equipe de Serviços Especializados em IA, você definirá:

- um público-alvo, 
- a métrica de negócios a ser otimizada, 
- as ações para o agente de decisão BrazeAI™, e 
- todos os dados primários do cliente que o agente deverá aproveitar para impulsionar seus resultados comerciais. 

Com o projeto em mãos, a equipe trabalhará com você para identificar e concluir quaisquer requisitos adicionais de integração.

### Etapa 3: Configure sua plataforma de entrega

Em seguida, a equipe do AI Expert Service ajudará a configurar sua plataforma de automação de marketing. Embora o estúdio de tomada de decisões funcione melhor com a Braze, há suporte para várias outras plataformas. Fale com a equipe do AI Expert Service para obter recursos adicionais.

{% tabs local %}
{% tab Braze %}
Para configurar a Braze:

1. Crie uma [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) ou um [canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule). O BrazeAI Decisioning Studio™ usará esse método de entrega para enviar eventos de ativação personalizados 1:1 para os usuários do seu público definido.
2. Certifique-se de não incluir um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze, para que a BrazeAI™ possa ser o grupo de controle dedicado.
3. Dependendo de suas dimensões, você pode configurar Liquid tags em seu conteúdo criativo para preencher dinamicamente suas mensagens com as recomendações da BrazeAI™. A BrazeAI™ passará o conteúdo específico do cliente para as tags Liquid em seus modelos usando a API Braze.
{% endtab %}
{% endtabs %}

### Etapa 4: Lançamento e monitoramento

Depois de lançar o agente, a equipe de Serviços Especializados em IA continuará a monitorá-lo e ajustá-lo ao design acordado. Eles também ajudarão a fazer ajustes, expansões ou modificações no agente, se necessário.
