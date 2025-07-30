---
nav_title: Métricas por segmentos
article_title: Métricas por segmentos
page_order: 2.5
page_type: reference
description: "Esta página descreve como você pode usar os modelos de relatório do Query Builder para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos."
tool: 
  - Segments
  - Reports
  
---

# Métricas por segmentos

> Use os modelos de relatório [do Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos.

[O rastreamento da análise de dados]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) deve estar ativado para os segmentos aos quais você deseja acessar as métricas.

Para executar esses relatórios, faça o seguinte:
1. No **Criador de consultas**, escolha criar um novo relatório SQL com um modelo. 
2. Selecione **Detalhamentos de segmento** para a métrica, que filtra modelos para aqueles em que as métricas incluem detalhamentos de segmento, que são:
- Métricas de performance de e-mail por segmento
- Métricas de engajamento de e-mail para variantes ou etapas, por segmento
- Compras e receita por segmento
- Compras e receita de variantes ou etapas por segmento
- Performance de push por segmento

![A página de detalhamento do segmento contém um editor de SQL, um painel lateral com guias para Variáveis, Tabelas de dados disponíveis, Histórico de consultas e o Criador de consultas de segmentos e uma seção de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Modelos de relatórios

{% tabs %}
{% tab Métricas de engajamento de e-mail por segmento %}

### Visualização de métricas para campanhas ou telas {#campaign-canvas-email}

Para visualizar as métricas de performance de e-mail divididas por segmento no nível da campanha ou do Canvas, use a guia [Variables (Variáveis](#variables) ) para especificar as campanhas ou Canvas e um período de tempo para extrair dados. Se nenhuma campanha ou Canvas for especificado, o relatório incluirá os e-mails de todas as campanhas e Canvases do período especificado. Você também pode aceitar a visualização de todas as campanhas e Canvas com determinadas tags.

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Envios
- Entregas
- Reclamações
- Aberturas exclusivas
- Aberturas exclusivas por máquina
- Aberturas exclusivas sem ser por máquinas
- Cliques exclusivos
- Cancelamentos de inscrição
- Bounces
- Soft bounces
- Deferidos

#### Resultados

Seus resultados mostrarão métricas de engajamento de e-mail por segmento para as campanhas ou Canvas selecionadas. Se você não selecionou campanhas ou Canvases específicos, seu relatório mostrará as métricas de e-mail para cada segmento em todas as campanhas de e-mail e Canvases dentro do período de tempo do relatório. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de engajamento de e-mail

### Visualização de métricas para variantes ou etapas

Para visualizar a performance do envio de e-mail dividida por segmento no nível da variante de campanha, no nível da variante do Canvas ou no nível da etapa do Canva, primeiro escolha um relatório no nível da variante ou da etapa (esses são relatórios que têm "para variantes ou etapas" no título) e, em seguida, use a guia **Variáveis** para especificar o seguinte:

- Campanha ou Canva específico (necessário se estiver usando um relatório de variante ou de etapa do canva) 
- Variantes (necessário se estiver usando um relatório de variantes ou de etapas)
- Etapa do canva (opcional)

As métricas são as mesmas que as oferecidas para o modelo [de nível de campanha ou de tela](#campaign-canvas-email). Se você escolher várias variantes, seus resultados serão agrupados por variante.

#### Resultados

Seus resultados mostrarão as métricas de engajamento de e-mail por segmento para as variantes ou etapas selecionadas. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de engajamento de e-mail

{% endtab %}

{% tab Compras e receita por segmento %}
### Visualização de métricas para campanhas ou telas

Para visualizar as métricas de compra e receita divididas por segmento para uma campanha ou Canva específico, use a guia [Variables (Variáveis)](#variables) para especificar o seguinte:

- Janela de conversão (o número de dias após o recebimento do e-mail ou clique ao qual a Braze deve atribuir compras ou receita)
- Produto específico (opcional) 

Além disso, use a guia **Variables (Variáveis** ) para especificar se o relatório deve ser executado para uma ou mais campanhas ou Canvas, ou para uma ou mais tags. Se nenhuma campanha, Canvas ou tag for escolhida, o relatório será executado para todos os e-mails de campanhas ou Canvas durante o período de tempo escolhido.

Atualmente, esse relatório extrai métricas apenas do canal de e-mail. Qualquer receita ou dados de compra de outros canais além de e-mails não serão refletidos no relatório. 

As seguintes métricas estão disponíveis para e-mails:

- Compras exclusivas após o recebimento
- Receita após o recebimento
- Compras exclusivas após o clique
- Receita por clique
- Destinatários únicos
- Cliques exclusivos de e-mail

Todas as métricas de taxa usam destinatários de e-mail exclusivos como denominador.

#### Definições

- "Após o recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, depois que os usuários receberam as campanhas ou as Canvas especificadas. 
- "Após o clique" refere-se aos eventos de compra ou à receita que ocorreu após os eventos de compra, dentro da janela de conversão especificada, depois que os usuários clicaram nas campanhas ou Canvas especificadas.

Por exemplo, digamos que um segmento contenha 10 usuários e cinco deles tenham feito uma compra depois de receber seu e-mail. Se um desses cinco fizesse uma compra depois de clicar em seu e-mail, sua "Taxa de compras únicas após o recebimento" seria de 50% e sua "Taxa de compras únicas após o clique" seria de 10%.

![O relatório mostra métricas de e-mail, incluindo compras únicas no recebimento, receita no recebimento, compras únicas no clique, receita no clique, destinatários únicos e cliques únicos no e-mail.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Seus resultados mostrarão métricas de compra por segmento para suas campanhas ou telas selecionadas. Se você não selecionou campanhas ou Canvas específicos, seu relatório mostrará as métricas de compra para cada segmento em todas as campanhas de e-mail ou Canvas dentro do período de tempo do seu relatório. 

- **Fileiras:** Segmentos
- **Colunas:** Métricas de compra


### Visualização de métricas para variantes ou etapas

Para visualizar as métricas de compra e receita divididas por segmento para uma variante de campanha específica, variante do Canvas ou etapa do Canva, use a guia [Variables (Variáveis](#variables) ) para especificar o seguinte:

- Campanha específica ou Canva
- Variantes 
- Etapa do canva (opcional) 
- Período
- Produto específico (opcional) 

#### Resultados

Seus resultados mostrarão as métricas de compra por segmento para as variantes ou etapas selecionadas.

- **Fileiras:** Segmentos
- **Colunas:** Métricas de compra

{% endtab %}
{% tab Envio de mensagens de topo ou fundo para engajamento de e-mail %}

### Visualização de métricas para as melhores ou piores performances

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe as campanhas, Canvas ou etapas do Canvas que tiveram a melhor ou a pior performance para uma métrica de engajamento de e-mail especificada. 

Os casos de uso incluem: 
- 10 campanhas com as maiores taxas de abertura de e-mails exclusivos
- 25 telas com o maior número de cancelamentos de inscrição por e-mail
- 50 etapas do Canva com os maiores cliques exclusivos

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Envios
- Entregas
- Reclamações
- Aberturas exclusivas
- Aberturas exclusivas por máquina
- Aberturas exclusivas sem ser por máquinas
- Cliques exclusivos
- Cancelamentos de inscrição
- Bounces
- Soft bounces
- Reclamações

Para visualizar esse relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** Selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** Selecione os resultados superiores ou inferiores e o número de resultados, como 10 superiores ou 15 inferiores
- **Tipo de mensagem:** Especifique se seus resultados são campanhas, Canvas ou etapas do Canva

#### Resultados

Seus resultados mostrarão as campanhas, Canvases ou etapas do Canva principais (ou inferiores) que você selecionou. Por exemplo, se você selecionou as 10 principais campanhas para taxa de cliques, seus resultados mostrarão as 10 principais campanhas ordenadas da maior para a menor taxa de cliques. Suas colunas exibirão todas as métricas de engajamento com e-mail para cada linha (campanhas, Canvas ou etapas de mensagens).

{% endtab %}
{% tab Envio de mensagens para compras em cima ou embaixo %}

### Visualização de métricas para as melhores ou piores performances

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe as campanhas, Canvas ou etapas do Canvas que tiveram a melhor ou a pior performance para uma métrica de compra ou receita especificada.

Os casos de uso incluem:
- 20 campanhas com as taxas de compra mais altas para um produto específico
- 25 Canvas com a maior receita gerada
- 10 etapas do canva com a menor taxa de compra de produtos

As seguintes métricas de e-mail estão disponíveis nesse relatório:
- Compras exclusivas após o recebimento
- Receita após o recebimento
- Compras exclusivas após o clique
- Receita por clique
- Destinatários únicos
- Cliques exclusivos de e-mail

Para visualizar esse relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** Selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** Selecione os resultados superiores ou inferiores e o número de resultados, como 10 superiores ou 15 inferiores
- **Tipo de mensagem:** Especifique se seus resultados são campanhas, Canvas ou etapas do Canva
- **Janela de conversão:** O número de dias após o recebimento do e-mail ou do clique ao qual o Braze atribuirá compras ou receita 

#### Definições

- "Após o recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, depois que os usuários receberam as campanhas ou as Canvas especificadas. 
- "Após o clique" refere-se aos eventos de compra ou à receita que ocorreu após os eventos de compra, dentro da janela de conversão especificada, depois que os usuários clicaram nas campanhas ou Canvas especificadas.

Por exemplo, digamos que um segmento contenha 10 usuários e cinco deles tenham feito uma compra depois de receber seu e-mail. Se um desses cinco fizer uma compra depois de clicar em seu e-mail, sua taxa de "compras únicas após o recebimento" será de 50% e sua taxa de "compras únicas após o clique" será de 10%.

#### Resultados

Seus resultados mostrarão as campanhas, Canvases ou etapas do Canva principais (ou inferiores) que você selecionou. Por exemplo, se você selecionou as 10 principais campanhas para "receita após o clique", seus resultados mostrarão as 10 principais campanhas ordenadas da maior para a menor "receita após o clique". Suas colunas exibirão todas as métricas de compra de cada linha (campanhas, Canvas ou etapas de mensagens).

{% endtab %}
{% tab Performance do push por segmento %}

### Exibição de métricas push para segmentos

Esse relatório na guia [Variables (Variáveis](#variables) ) exibe métricas push divididas por segmentos. 

Na guia **Variables (Variáveis** ), especifique as campanhas ou Canvas para visualizar as métricas e um período de tempo para extrair dados. Se você não selecionar nenhuma campanha ou Canvas, o relatório mostrará os pushs de todas as campanhas e Canvases no período especificado. Você também pode visualizar todas as campanhas e Canvas com determinadas tags.

As seguintes métricas push estão disponíveis neste relatório:

- Envios
- Bounces
- Entregas
- Aberturas diretas

#### Resultados

Seu relatório exibirá os seguintes resultados:

- **Fileiras:** Segmentos
- **Colunas:** Métricas push
{% endtab %}
{% endtabs %}