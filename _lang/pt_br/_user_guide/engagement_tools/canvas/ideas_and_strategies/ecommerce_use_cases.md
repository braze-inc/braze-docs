---
nav_title: Casos de uso de comércio eletrônico
article_title: Casos de uso de comércio eletrônico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artigo de referência aborda vários modelos pré-construídos do Braze adaptados especificamente para profissionais de marketing de comércio eletrônico, facilitando a implementação de estratégias essenciais."
toc_headers: h2
---

# Como usar os eventos recomendados para comércio eletrônico

> Esta página aborda como e onde você pode usar os eventos recomendados para comércio eletrônico em toda a plataforma, inclusive como usar os modelos do Braze eCommerce Canvas.

{% alert important %}
[Os eventos recomendados para comércio eletrônico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente Braze se estiver interessado em participar desse acesso antecipado. <br><br>Se estiver usando o novo conector do Shopify, os eventos recomendados para comércio eletrônico estarão automaticamente disponíveis por meio da integração.
{% endalert %}

## Usando um modelo do Canvas

Para usar um modelo do Canva:
1. Acesse **Envio de mensagens** > **Canva**.
2. Selecione **Criar tela** > **Usar um modelo de tela**.
3. Procure na guia **Braze templates** o modelo que deseja usar. Você pode fazer uma prévia de um modelo selecionando seu nome.
4. Selecione **Apply Template (Aplicar modelo** ) para o modelo que você deseja usar.<br><br>![A página "Modelos de tela" foi aberta na guia "Modelos do Braze" e mostra uma lista de modelos usados recentemente e modelos do Braze selecionáveis.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modelos de canvas para comércio eletrônico

O Braze oferece quatro modelos de Canvas para comércio eletrônico.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalização de mensagens

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) é uma poderosa linguagem de modelos usada pelo Braze que permite criar conteúdo dinâmico e personalizado para seus clientes. Ao usar Liquid tags, você pode personalizar as mensagens com base nos dados do cliente, nas informações do produto e em outras variáveis, aprimorando a experiência de compra e promovendo o engajamento.

### Principais recursos do Liquid

- **Conteúdo dinâmico:** Insira informações específicas do cliente, como nomes, detalhes do pedido e preferências em suas mensagens.
- **Lógica condicional:** Use instruções if/else para exibir conteúdo diferente com base em condições específicas (como o local do cliente e o histórico de compras).
- **Loops:** Iterate sobre coleções de produtos ou dados de clientes para exibir listas ou grades de itens.

### Introdução ao Liquid

Para começar a personalizar suas mensagens usando Liquid tags, consulte os recursos a seguir:

- Referência de [dados do Shopify]({{site.baseurl}}/shopify_features/#shopify-data) com Liquid tags predefinidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentação

Use os segmentos Braze para criar segmentos de clientes direcionados com base em atributos e comportamentos específicos e fornecer campanhas e mensagens personalizadas. Com esse poderoso recurso, você pode engajar seus clientes de forma eficaz, atingindo o público certo com a mensagem certa no momento certo.

Para saber mais sobre como começar a usar segmentos, consulte [Sobre os segmentos do Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Os eventos de comércio eletrônico são baseados em [eventos recomendados]({{site.baseurl}}/recommended_events/).
Como os eventos recomendados são eventos personalizados mais opinativos, você pode pesquisar os nomes dos eventos de comércio eletrônico recomendados selecionando qualquer [filtro de evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de comércio eletrônico

Segmente seus usuários com filtros de comércio eletrônico, como **Fonte de comércio eletrônico** e **Receita total**, acessando a seção **Comércio eletrônico** no segmentador. 

Para obter uma lista de filtros de comércio eletrônico e suas definições, consulte [Filtros de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) e selecione a categoria de pesquisa "comércio eletrônico".

![Filtros de segmento suspensos com filtros de "Comércio eletrônico".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriedades de eventos aninhados

Para segmentar por propriedades de eventos aninhados, você pode aproveitar [as extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por exemplo, você pode usar as extensões de segmento para descobrir quem comprou o produto "SKU-123" nos últimos 90 dias.

## Análise de dados

### Relatório de eventos personalizados

É possível rastrear o volume de eventos recomendados para comércio eletrônico no [relatório Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filtre por **Perform Custom Event** e, em seguida, especifique o [nome do evento recomendado de comércio eletrônico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) para visualizar sua performance ao longo do tempo.

![Gráfico de eventos personalizados exibindo resultados de seis eventos selecionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Relatório de conversões 

### Relatório de eventos personalizados

Para criar um [relatório de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) com base em quem realizou um evento suportado pela integração, você pode especificar o [nome do evento]({{site.baseurl}}/shopify_data_features/) específico.

### Dashboards

#### Painel de controle de conversões

Para obter insights sobre as tendências relacionadas aos pedidos feitos a partir de seus Canvases lançados, configure um [dashboard de Conversões]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) e especifique seus Canvases.

#### Painel de receitas de comércio eletrônico

Para obter insights sobre a receita atribuída à última campanha ou à última tela com a qual um usuário interagiu antes de fazer um pedido, use o [dashboard de receita de comércio eletrônico]({{site.baseurl}}/ecommerce_revenue_dashboard/) e selecione uma janela de conversão.

### Criador de consultas

### Relatório de receita 

Para analisar os dados desses novos eventos, acesse o [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) e visualize o [dashboard**eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/).
