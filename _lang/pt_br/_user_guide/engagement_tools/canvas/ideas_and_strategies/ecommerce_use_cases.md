---
nav_title: casos de uso de eCommerce
article_title: Casos de Uso de eCommerce
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artigo de referência cobre vários modelos Braze pré-construídos, adaptados especificamente para profissionais de marketing de eCommerce, facilitando a implementação de estratégias essenciais."
toc_headers: h2
---

# Como usar eventos recomendados de eCommerce

> Esta página cobre como e onde você pode usar eventos recomendados de eCommerce na plataforma, incluindo como usar modelos Canvas de eCommerce do Braze.

{% alert important %}
[eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente do Braze se você estiver interessado em participar deste acesso antecipado. <br><br>Se você estiver usando o novo conector Shopify, os eventos recomendados de eCommerce estarão automaticamente disponíveis através da integração.
{% endalert %}

## Usando um modelo Canvas

Para usar um modelo Canvas:
1. Acesse **Envio de mensagens** > **Canva**.
2. Selecione **Criar Canvas** > **Usar um Modelo Canvas**.
3. Navegue na aba **modelos Braze** para o modelo que você deseja usar. Você pode visualizar um modelo selecionando seu nome.
4. Selecione **Aplicar Modelo** para o modelo que você deseja usar.<br><br>![Página "modelos Canvas" aberta na aba "modelos Braze" e mostrando uma lista de modelos usados recentemente e modelos Braze selecionáveis.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## modelos Canvas de eCommerce

O Braze oferece quatro modelos Canvas de eCommerce.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalização de mensagens

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) é uma poderosa linguagem de modelagem usada pelo Braze que permite criar conteúdo dinâmico e personalizado para seus clientes. Ao usar tags Liquid, você pode personalizar mensagens com base em dados de clientes, informações de produtos e outras variáveis, melhorando a experiência de compra e aumentando o engajamento.

### Principais recursos do Liquid

- **Conteúdo dinâmico:** Insira informações específicas do cliente, como nomes, detalhes do pedido e preferências em suas mensagens.
- **Lógica condicional:** Use declarações if/else para exibir conteúdo diferente com base em condições específicas (como localização do cliente e histórico de compras).
- **Laços:** Itere sobre coleções de produtos ou dados de clientes para exibir listas ou grades de itens.

### Introdução ao Liquid

Para começar a personalizar suas mensagens usando tags Liquid, você pode consultar os seguintes recursos:

- Referência de [dados do Shopify]({{site.baseurl}}/shopify_features/#shopify-data) com tags liquid pré-definidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentação

Use segmentos do Braze para criar segmentos de clientes direcionados com base em atributos e comportamentos específicos, e entregar mensagens e campanhas personalizadas. Com este recurso poderoso, você pode engajar efetivamente seus clientes alcançando o público certo com a mensagem certa no momento certo.

Para mais informações sobre como começar com segmentos, confira [Sobre os segmentos do Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Eventos de eCommerce são baseados em [eventos recomendados]({{site.baseurl}}/recommended_events/).
Como os eventos recomendados são eventos personalizados mais opinativos, você pode procurar os nomes dos eventos de eCommerce recomendados selecionando qualquer [filtro de evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de eCommerce

Segmentar seus usuários com filtros de eCommerce, como **Fonte de Ecommerce** e **Receita Total**, acessando a seção **Ecommerce** dentro do segmentador. 

Para uma lista de filtros de eCommerce e suas definições, consulte [Filtros de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) e selecione a categoria de pesquisa "eCommerce".

![Dropdown de filtros de segmento com filtros "Ecommerce".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriedades de evento aninhadas

Para segmentar por propriedades de eventos aninhados, você pode aproveitar as [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por exemplo, você pode usar as extensões de segmento para encontrar quem comprou o produto “SKU-123” nos últimos 90 dias.

## Análise de dados

### relatório de eventos personalizados

Você pode acompanhar o volume de eventos recomendados de eCommerce no [relatório de Eventos Personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filtre por **Executar Evento Personalizado**, em seguida, especifique o [nome do evento recomendado de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) para visualizar seu desempenho ao longo do tempo.

![Gráfico de Eventos Personalizados exibindo resultados para seis eventos selecionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Dashboards

#### Painel de controle de conversões

Após lançar uma campanha ou canva usando o evento de conversão "Fazer Pedido", você pode criar um [relatório de conversão]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#setting-up-your-report) correspondente para acompanhar o desempenho.

![Tabela de Detalhes de Conversões com campanhas e canvases, e as estatísticas de conversão associadas.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### dashboard de receita de eCommerce

Para obter insights sobre a receita atribuída à última campanha ou canva com a qual um usuário interagiu antes de fazer um pedido, use o [dashboard de receita de eCommerce]({{site.baseurl}}/ecommerce_revenue_dashboard/) e selecione uma janela de conversão.

### relatório de receita 

Para analisar dados desses novos eventos, Acessar o [Construtor de Dashboard]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) e visualizar o [**Receita de eCommerce - Atribuição do Último Toque** dashboard]({{site.baseurl}}/ecommerce_revenue_dashboard/).
