---
nav_title: Métricas por segmentos
article_title: Métricas por segmentos
page_order: 2.5
page_type: reference
description: "Esta página descreve como você pode usar os modelos de relatório do Query Builder para detalhar as métricas de desempenho de campanhas, Canvas, variantes e etapas por segmentos."
tool: 
  - Segments
  - Reports
  
---

# Métricas por segmentos

> Use os modelos de relatório [do Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) para detalhar as métricas de desempenho de campanhas, Canvas, variantes e etapas por segmentos.

[O rastreamento do Analytics]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) deve estar ativado para os segmentos para os quais você deseja acessar as métricas.

Para executar esses relatórios, faça o seguinte:
1. No **Query Builder**, escolha criar um novo relatório SQL com um modelo. 
2. Selecione **Detalhamentos de segmento** para a métrica, que filtra os modelos para aqueles em que as métricas incluem detalhamentos de segmento, que são:
- Métricas de desempenho de e-mail por segmento
- Métricas de engajamento de e-mail para variantes ou etapas, por segmento
- Compras e receita por segmento
- Compras e receita de variantes ou etapas, por segmento
- Desempenho do impulso por segmento

A página de detalhamento do segmento contém um editor SQL, um painel lateral com guias para variáveis, tabelas de dados disponíveis, histórico de consultas e o AI Query Builder, além de uma seção de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Modelos de relatório

{% tabs %}
{% tab Email engagement metrics by segment %}

### Visualização de métricas para campanhas ou Canvases {#campaign-canvas-email}

Para visualizar as métricas de desempenho de e-mail divididas por segmento no nível da campanha ou do Canvas, use a guia [Variables (Variáveis](#variables) ) para especificar as campanhas ou Canvases e um período de tempo para extrair dados. Se nenhuma campanha ou Canvase for especificado, o relatório incluirá e-mails de todas as campanhas e Canvases do período de tempo especificado. Você também pode optar por visualizar todas as campanhas e Canvases com determinadas tags.

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Envia
- Entregas
- Reclamações
- Abertura exclusiva
- A máquina exclusiva abre
- Abertura exclusiva sem máquina
- Cliques exclusivos
- Cancelamento de inscrição
- Saltos
- Saltos suaves
- Diferido

#### Resultados

Seus resultados mostrarão métricas de engajamento de e-mail por segmento para as campanhas ou Canvases que você selecionou. Se você não selecionou campanhas ou Canvases específicos, seu relatório mostrará as métricas de e-mail para cada segmento em todas as campanhas de e-mail e Canvases dentro do período de tempo do seu relatório. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de engajamento de e-mail

### Visualização de métricas para variantes ou etapas

Para visualizar o desempenho do e-mail dividido por segmento no nível da variante da campanha, no nível da variante do Canvas ou no nível da etapa do Canvas, primeiro escolha um relatório no nível da variante ou da etapa (esses são relatórios que têm "para variantes ou etapas" no título) e, em seguida, use a guia **Variáveis** para especificar o seguinte:

- Campanha ou Canvas específico (necessário se estiver usando um relatório de variante ou de nível de etapa) 
- Variantes (necessário se estiver usando um relatório de variante ou de nível de etapa)
- Etapa da tela (opcional)

As métricas são as mesmas oferecidas para o modelo [de nível de campanha ou Canvas](#campaign-canvas-email). Se você escolher várias variantes, seus resultados serão agrupados por variante.

#### Resultados

Seus resultados mostrarão métricas de envolvimento de e-mail por segmento para as variantes ou etapas selecionadas. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de engajamento de e-mail

{% endtab %}

{% tab Purchases and revenue by segment %}
### Visualização de métricas para campanhas ou Canvases

Para visualizar as métricas de compra e receita divididas por segmento para uma campanha ou Canvas específico, use a guia [Variables (Variáveis](#variables) ) para especificar o seguinte:

- Janela de conversão (o número de dias após o recebimento do e-mail ou clique ao qual o Braze deve atribuir compras ou receita)
- Produto específico (opcional) 

Além disso, use a guia **Variables (Variáveis** ) para especificar se o relatório deve ser executado para uma ou mais campanhas ou Canvases, ou para uma ou mais tags. Se não forem escolhidas campanhas, Canvases ou tags, o relatório será executado para todos os e-mails de campanhas ou Canvases durante o período de tempo escolhido.

Atualmente, esse relatório extrai métricas apenas do canal de e-mail. Qualquer receita ou dados de compra de outros canais além de e-mails não serão refletidos no relatório. 

As métricas a seguir estão disponíveis para e-mails:

- Compras exclusivas após o recebimento
- Receita após o recebimento
- Compras exclusivas após o clique
- Receita por clique
- Destinatários exclusivos
- Cliques exclusivos em e-mails

Todas as métricas de taxa usam destinatários de e-mail exclusivos como denominador.

#### Definições

- "Após o recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, depois que os usuários receberam as campanhas ou Canvases especificadas. 
- "Após o clique" refere-se aos eventos de compra ou à receita que ocorreu após os eventos de compra, dentro da janela de conversão especificada, depois que os usuários clicaram nas campanhas ou Canvases especificadas.

Por exemplo, digamos que um segmento contenha 10 usuários e cinco deles tenham feito uma compra depois de receber seu e-mail. Se um desses cinco fizesse uma compra depois de clicar em seu e-mail, sua "Taxa de compras únicas após o recebimento" seria de 50% e sua "Taxa de compras únicas após o clique" seria de 10%.

O relatório mostra métricas de e-mail, incluindo compras exclusivas após o recebimento, receita após o recebimento, compras exclusivas após o clique, receita após o clique, destinatários exclusivos e cliques exclusivos em e-mails.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Seus resultados mostrarão métricas de compra por segmento para suas campanhas ou Canvases selecionados. Se você não selecionou campanhas ou Canvases específicos, seu relatório mostrará as métricas de compra para cada segmento em todas as campanhas de e-mail ou Canvases dentro do período de tempo do seu relatório. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de compra


### Visualização de métricas para variantes ou etapas

Para visualizar as métricas de compra e receita divididas por segmento para uma variante de campanha específica, variante do Canvas ou etapa do Canvas, use a guia [Variáveis](#variables) para especificar o seguinte:

- Campanha específica ou Canvas
- Variantes 
- Etapa da tela (opcional) 
- Intervalo de tempo
- Produto específico (opcional) 

#### Resultados

Seus resultados mostrarão métricas de compra por segmento para as variantes ou etapas selecionadas.

- **Fileiras:** Segmentos
- **Colunas:** Métricas de compra

{% endtab %}
{% tab Top or bottom messaging for email engagement %}

### Visualização de métricas para os melhores ou piores desempenhos

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe as campanhas, Canvases ou etapas do Canvas que tiveram o melhor ou o pior desempenho para uma métrica de envolvimento de e-mail especificada. 

Os casos de uso incluem: 
- 10 campanhas com as maiores taxas de abertura de e-mails exclusivos
- 25 telas com o maior número de cancelamentos de inscrição de e-mail
- 50 etapas do Canvas com os maiores cliques exclusivos

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Envia
- Entregas
- Reclamações
- Abertura exclusiva
- A máquina exclusiva abre
- Abertura exclusiva sem máquina
- Cliques exclusivos
- Cancelamento de inscrição
- Saltos
- Saltos suaves
- Reclamações

Para visualizar esse relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** Selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** Selecione os resultados superiores ou inferiores e o número de resultados, como 10 superiores ou 15 inferiores
- **Tipo de mensagem:** Especifique se seus resultados são campanhas, Canvases ou etapas do Canvas

#### Resultados

Seus resultados mostrarão as campanhas, Canvases ou etapas de Canvas principais (ou inferiores) que você selecionou. Por exemplo, se você selecionou as 10 principais campanhas para taxa de cliques, seus resultados mostrarão as 10 principais campanhas ordenadas da maior para a menor taxa de cliques. Suas colunas exibirão todas as métricas de envolvimento de e-mail para cada linha (campanhas, Canvases ou etapas de mensagens).

{% endtab %}
{% tab Top or bottom messaging for purchases %}

### Visualização de métricas para os melhores ou piores desempenhos

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe as campanhas, Canvases ou etapas do Canvas que tiveram o melhor ou o pior desempenho para uma métrica de compra ou receita especificada.

Os casos de uso incluem:
- 20 campanhas com as taxas de compra mais altas para um produto específico
- 25 telas com a maior receita gerada
- 10 etapas do Canvas com a menor taxa de compra de produtos

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Compras exclusivas após o recebimento
- Receita após o recebimento
- Compras exclusivas após o clique
- Receita por clique
- Destinatários exclusivos
- Cliques exclusivos em e-mails

Para visualizar esse relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** Selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** Selecione os resultados superiores ou inferiores e o número de resultados, como 10 superiores ou 15 inferiores
- **Tipo de mensagem:** Especifique se seus resultados são campanhas, Canvases ou etapas do Canvas
- **Janela de conversão:** O número de dias após o recebimento do e-mail ou clique ao qual a Braze atribuirá compras ou receita 

#### Definições

- "Após o recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, depois que os usuários receberam as campanhas ou Canvases especificadas. 
- "Após o clique" refere-se aos eventos de compra ou à receita que ocorreu após os eventos de compra, dentro da janela de conversão especificada, depois que os usuários clicaram nas campanhas ou Canvases especificadas.

Por exemplo, digamos que um segmento contenha 10 usuários e cinco deles tenham feito uma compra depois de receber seu e-mail. Se um desses cinco fizesse uma compra depois de clicar em seu e-mail, sua taxa de "compras únicas após o recebimento" seria de 50% e sua taxa de "compras únicas após o clique" seria de 10%.

#### Resultados

Seus resultados mostrarão as campanhas, Canvases ou etapas de Canvas principais (ou inferiores) que você selecionou. Por exemplo, se você selecionou as 10 principais campanhas para "receita após o clique", seus resultados mostrarão as 10 principais campanhas ordenadas da maior para a menor "receita após o clique". Suas colunas exibirão todas as métricas de compra de cada linha (campanhas, Canvases ou etapas de mensagens).

{% endtab %}
{% tab Push performance by segment %}

### Exibição de métricas de push para segmentos

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe métricas de push divididas por segmentos. 

Na guia **Variables (Variáveis** ), especifique as campanhas ou Canvases para visualizar as métricas e um período de tempo para extrair dados. Se você não selecionar nenhuma campanha ou Canvase, o relatório mostrará os impulsos de todas as campanhas e Canvases no período de tempo especificado. Você também pode visualizar todas as campanhas e Canvases com determinadas tags.

As seguintes métricas de push estão disponíveis neste relatório:

- Envia
- Saltos
- Entregas
- Abertura direta

#### Resultados

Seu relatório exibirá os seguintes resultados:

- **Fileiras:** Segmentos
- **Colunas:** Métricas de push
{% endtab %}
{% endtabs %}