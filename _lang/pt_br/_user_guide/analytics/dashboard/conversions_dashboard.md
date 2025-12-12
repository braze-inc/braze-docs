---
nav_title: Painel de controle de conversões
article_title: Painel de controle de conversões
alias: "/conversions_dashboard_v2/"
description: "O painel de conversões permite que você analise as conversões em campanhas, Canvases e canais, usando diferentes métodos de atribuição."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Painel de controle de conversões

> O painel de conversões analisa as conversões em campanhas, Canvases e canais, usando vários [métodos de atribuição](#attribution-methods). Ao medir suas conversões, você pode especificar o período de tempo, o evento de conversão e a janela de conversão.

## Configuração de seu relatório

Para configurar seu relatório do painel de conversões:

1. Vá para **Analytics** > **Conversions**( **Análises** > **Conversões**).
2. Selecione um **Intervalo de datas** para seu relatório, até um período de 90 dias.
3. Selecione as campanhas ou Canvases (ou ambas) a serem analisadas. 
   - (opcional) Filtre campanhas e Canvases selecionando uma tag.  
4. Selecione o **(s) canal(is)** a ser **(** em) analisado( **s)** para suas mensagens.
5. Selecione uma **divisão por** camada para visualizar diferentes dimensões de dados, como por variante, etapa do Canvas, país ou idioma.
6. (Opcional) Se você quiser calcular as conversões de um evento que não foi configurado como um evento de conversão na campanha ou no Canvas, ative [Usar eventos personalizados](#using-custom-events).
7. Selecione um [método de atribuição](#attribution-methods) para analisar as mensagens selecionadas.

{% alert note %}
Se você estiver analisando conversões para vários canais, seu **Attribution Method** será padronizado para **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8\. Selecione **Criar** para executar o relatório.

Após o carregamento da página, selecione um **evento de conversão** para filtrar os dados de conversão do relatório. As seleções disponíveis incluirão os eventos que foram pré-configurados nos Canvases e nas campanhas. Se você selecionou um evento personalizado ao configurar seu relatório (etapa 6), essa opção não estará disponível.

### Uso de eventos personalizados

Para que as métricas de eventos personalizados apareçam no painel de conversões, você deve ter um evento de conversão e um evento de entrada no Canvas no intervalo de datas especificado na página. 

Para calcular as conversões de um evento que não foi configurado como um evento de conversão na campanha ou no Canvas, selecione um evento personalizado específico para usar como um evento de conversão. 

1. Ao configurar seu relatório, ative a opção **Usar eventos personalizados**.
2. Selecione um evento personalizado para usar como o evento de conversão.
3. Selecione a janela de conversão na qual esse evento deveria ter ocorrido para ser contado como uma conversão.

{% alert note %}
Se você selecionar um evento personalizado, não verá o menu suspenso **Evento de conversão** na página e terá que executar novamente o relatório para visualizar as conversões de diferentes eventos personalizados.
{% endalert %}

## Compreensão de seu relatório

Seu relatório é dividido em três seções:

- [Detalhes da conversão](#conversion-details)
- [Funil de conversão](#conversion-funnel)
- [Conversões ao longo do tempo](#conversions-over-time)

### Detalhes da conversão

A tabela de detalhes da conversão sempre mostra uma coluna para *Destinatários* e outra para *Conversões* (taxa e total). As duas colunas restantes da tabela que aparecem dependem das opções que você selecionou ao configurar o relatório. 

Tabela de detalhes de conversão mostrando o Touches como o método de atribuição para as colunas três e quatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

A tabela a seguir descreve as métricas possíveis.

| Métrica mostrada | Descrição |
| --- | --- |
| Beneficiários | O número de usuários que receberam uma mensagem por meio do canal selecionado dentro do intervalo de datas do relatório |
| Taxa de conversão (destinatários) | Calculado como: (Número de conversões) / (Número de destinatários) |
| Método de atribuição | Definido pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Para atribuição de Último Toque ou se vários canais forem selecionados, isso aparecerá como [Toques](#terms-to-know). |
| Taxa de conversão (método de atribuição) | Definido pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Se vários canais forem selecionados, o padrão será a atribuição do último toque. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se você tiver selecionado detalhes em nível de detalhamento para campanhas ou Canvases ao [configurar o relatório](#setting-up-your-report) (etapa 5), poderá clicar em <i class="fas fa-angle-down"></i> para expandir a tabela.

### Funil de conversão

Esse gráfico de barras mostra as contagens absolutas de cada [evento de engajamento]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) com base no canal selecionado. A contagem de conversões será definida de acordo com o método de atribuição selecionado.

Por padrão, todas as campanhas e Canvases selecionados são exibidos. Para desmarcar uma campanha ou um Canvas, selecione o nome da campanha ou do Canvas que você deseja excluir. Para obter detalhes adicionais sobre o evento de compromisso, passe o mouse sobre cada barra.

Para fazer o download dos dados da série temporal, selecione uma opção de download: PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Esse gráfico mostra apenas os dados de um único canal de cada vez. Use o menu suspenso **Channel (Canal** ) no gráfico para selecionar um único canal.
{% endalert %}

Gráfico de barras do funil de conversões para duas campanhas de e-mail mostrando resultados semelhantes para E-mails entregues, E-mails abertos, E-mails clicados e Conversões.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversões ao longo do tempo

Esse gráfico de série temporal inclui uma representação das conversões por campanha ou Canvas ao longo do tempo. Por padrão, todas as campanhas e Canvases selecionados são exibidos. Para desmarcar uma campanha ou um Canvas, clique no nome da campanha ou do Canvas que você deseja excluir.

Para fazer o download dos dados de série temporal, selecione <i class="fas fa-bars"></i> e, em seguida, selecione a opção de download. As opções disponíveis são PNG, JPEG, PDF, SVG ou CSV.

Gráfico de série temporal de conversões ao longo do tempo para duas campanhas de e-mail, mostrando as conversões por dia.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribuição

| Método de atribuição | Definição | Cálculo da taxa | Opções específicas do canal |
| --- | --- | --- | --- |
| Após o recebimento | Número total de conversões que ocorreram após o recebimento da mensagem | Calculado como (Conversões Únicas Recebidas) / (Destinatários Únicos) | {::nomarkdown}<ul><li>Após a entrega do e-mail</li><li>Após a entrega do SMS</li></ul>{:/} |
| Após o envio | Número total de conversões que ocorreram após o envio da mensagem | Calculado como (conversões de envio único) / (destinatários únicos) | {::nomarkdown}<ul><li>Após o envio de push</li><li>Após o envio do Content Card</li><li>Após o envio do SMS</li></ul>{:/} |
| Após a abertura | Número total de conversões que ocorreram após a abertura da mensagem | Calculado como (conversões abertas únicas) / (destinatários únicos) | {::nomarkdown}<ul><li>Após a abertura do e-mail</li><li>Ao pressionar para abrir</li></ul>{:/} |
| Após o clique | Número total de conversões que ocorreram por clique na mensagem | Calculado como (conversões de cliques únicos) / (destinatários únicos) | {::nomarkdown}<ul><li>Ao clicar no e-mail</li><li>Ao clicar no Content Card</li><li>Ao clicar em IAM</li></ul>{:/} |
| Impressão | Número total de conversões que ocorreram após uma impressão | Calculado como (conversões de impressões únicas) / (destinatários únicos) | {::nomarkdown}<ul><li>Após a impressão do IAM</li><li>Após a impressão do Content Card</li></ul>{:/} |
| Após o último toque | Conversões que dão todo o crédito à última mensagem tocada ou clicada durante a janela de conversão. | Calculado como (número de toques) / (destinatários únicos) | A atribuição de último toque é selecionada automaticamente se vários canais forem adicionados ao relatório.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Termos a serem conhecidos

| Prazo | Definição |
| --- | --- |
| Toque | Uma interação física ou ponto de contato com uma mensagem.<br><br>Os toques podem incluir:<br>{::nomarkdown}<ul><li>Clique no e-mail</li><li>Empurrar para abrir</li><li>Clique no Content Card</li><li>Clique na mensagem no aplicativo</li><li>Clique em SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
