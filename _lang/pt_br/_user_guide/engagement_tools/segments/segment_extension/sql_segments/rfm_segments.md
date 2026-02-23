---
nav_title: "Segmentos de RFM"
article_title: Segmentos do RFM SQL
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Este artigo descreve como criar extensões de segmento de RFM, que identificam seus melhores usuários medindo seus hábitos de compra."
tool: Segments
---

# Segmentos do RFM SQL

> É possível criar uma extensão de segmento RFM (recência, frequência, monetário) para direcionar seus melhores usuários, medindo seus hábitos de compra.

A análise RFM é uma técnica de marketing que identifica seus melhores usuários pontuando-os em uma escala de 0 a 3 para cada categoria (recência, frequência, monetária), em que 3 é a melhor pontuação e 0 é a pior. Os valores de recência, frequência e monetários são todos baseados em dados de um intervalo de tempo específico de sua escolha.

## Categorias de RFM

| Categoria | Definição |
| --- | --- |
| Tempo decorrido | Há quanto tempo um cliente fez uma compra. Uma pontuação mais alta significa compras mais recentes. |
| Frequência | Com que frequência um cliente fez uma compra. Uma pontuação mais alta significa maior frequência. |
| Valor monetário | Valor total gasto pelo cliente. Uma pontuação mais alta significa gastos mais altos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Os eventos de compra devem ser ativados para usar os segmentos RFM SQL porque o valor monetário para seus usuários é determinado pela receita que eles geraram por meio dos eventos de compra do Braze.
{% endalert %}

## Criação de um segmento de RFM

1. Acesse **Público** > **Extensões de segmento**.
2. Selecione **New Extension (Nova extensão**) e, em seguida, selecione **Recency, frequency, and monetary value (RFM) segment (segmento de frequência, frequência e valor monetário**).

![Modal com a opção de criar um segmento de catálogo para eventos, compras ou segmentos de RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3\. No painel **Variables (Variáveis** ), selecione seu **Time Range (Intervalo de tempo** ) para especificar o período de tempo dos dados de compra a serem analisados. Você pode especificar até os últimos 60 dias. O intervalo de tempo selecionado é o intervalo de tempo do qual os dados de comportamento dos usuários são extraídos e depende das metas da sua campanha.

| Campo de intervalo de tempo | Descrição | Caso de uso |
| --- | --- | --- |
| Relativo | Especifique a atividade nos últimos X dias | Analise o comportamento mais recente do usuário com uma janela contínua. | 
| Data inicial | Especifique um ponto de partida fixo para sua análise | Analise a atividade do usuário a partir de uma data específica, por exemplo, após o lançamento de uma campanha. |
| Data final | Especifique um ponto final fixo para sua análise | Analise a atividade do usuário até uma data específica, por exemplo, antes de uma atualização de produto. |
| Período | Especifique uma data inicial e uma data final para um período personalizado | Analise o comportamento do usuário durante um período definido, como um evento promocional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{: start="4"}
4\. Selecione os [grupos de RFM](#rfm-groups) gerados para incluir em seu segmento. Se você selecionar vários grupos, seu segmento incluirá usuários que fazem parte de qualquer um dos grupos selecionados.

![Painel de variáveis com os grupos de RFM "Champions" e "Loyal Users" selecionados.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5\. Execute uma prévia e salve seu segmento

{% alert note %}
Não é necessário editar o código SQL no modelo para criar um segmento de RFM. Você pode usar exclusivamente o painel **Variables (Variáveis** ) para personalizar seu segmento.
{% endalert %}

### Grupos de RFM

Os segmentos do RFM são avaliados em uma ordem específica. Os usuários são atribuídos ao primeiro segmento cujos critérios eles atendem, do topo da lista de priorização para baixo. Por exemplo, um usuário que se qualifica tanto para "Campeões" quanto para "Usuários leais" é atribuído ao segmento "Campeões" porque tem uma prioridade mais alta.

| Grupo RFM          | Descrição do segmento                                                                 | Classificação de recência (R) | Classificação de frequência (F) | Classificação monetária (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Campeões          | O segmento de usuários mais valioso com as melhores pontuações em todas as categorias.                   | 3                | 2-3                | 2-3               |
| Usuários fiéis        | Usuários que têm alta recência e alta frequência. Pode ter um valor monetário menor do que os Campeões. | 2-3              | 2-3                | 1-3               |
| Leais em potencial| Usuários que compraram recentemente com frequência moderada e valor monetário moderado.   | 3                | 1-3                | 1-3               |
| Promissor          | Usuários que fizeram uma compra inicial recente e de alto valor, mas ainda não estabeleceram uma alta frequência de compras. | 3                | 0-3                | 1-3               |
| Novo cliente       | Usuários que fizeram sua primeira compra muito recentemente.                             | 3                | 0-3                | 0-3               |
| Necessitando de atenção  | Usuários com recência acima da média, mas com frequência de compra ou valor monetário abaixo da média. | 2-3              | 0-3                | 0-3               |
| Não posso perdê-los   | Usuários que anteriormente eram de alto valor com boa frequência e pontuações monetárias, mas que não compram há muito tempo. | 0-1              | 2-3                | 2-3               |
| Em risco            | Usuários que historicamente tiveram pontuações monetárias e de frequência moderadas, mas que não compram há muito tempo. | 0-1              | 1-3                | 1-3               |
| Prestes a dormir     | Usuários que têm pontuações baixas em todas as métricas.                                       | 1                | 0-3                | 0-3               |
| Hibernação        | Usuários com frequência moderada, mas que ficaram inativos por um longo período.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
