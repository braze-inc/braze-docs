---
nav_title: Painel de controle de conversões
article_title: Dashboard de conversões
alias: "/conversions_dashboard_v2/"
description: "O dashboard de conversões permite que você analise as conversões em campanhas, Canvas e canais, usando diferentes métodos de atribuição."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# Painel de controle de conversões

> O dashboard de conversões analisa as conversões em campanhas, Canvas e canais, usando vários [métodos de atribuição](#attribution-methods). Ao medir suas conversões, você pode especificar o período de tempo, o evento de conversão e a janela de conversão.

## Configuração de seu relatório

Para configurar seu relatório do dashboard de conversões:

1. Acesse **Análise de dados** > **Conversões**.
2. Selecione um **Intervalo de datas** para seu relatório, até um período de 90 dias.
3. Selecione as campanhas ou as Canvas (ou ambas) a serem analisadas. 
   - (opcional) Filtre campanhas e telas selecionando uma tag.  
4. Selecione o(s) **canal(is)** a ser(em) analisado(s) para suas mensagens.
5. Selecione uma **Quebra por** camada para visualizar diferentes dimensões de dados, como por variante, etapa do canva, país ou idioma.
6. (Opcional) Se você quiser calcular conversões de um evento que não foi configurado como um evento de conversão na campanha ou no Canvas, ative [Usar eventos personalizados](#using-custom-events).
7. Selecione um [método de atribuição](#attribution-methods) para analisar as mensagens selecionadas.

{% alert note %}
Se estiver analisando conversões para vários canais, seu **método de atribuição** terá como padrão a **atribuição de último ponto de contato**.
{% endalert %}

{:start="8"}
8\. Selecione **Criar** para executar o relatório.

Após o carregamento da página, selecione um **evento de conversão** para filtrar os dados de conversão do relatório. As seleções disponíveis incluirão os eventos que foram pré-configurados nas telas e campanhas. Se você selecionou um evento personalizado ao configurar seu relatório (etapa 6), essa opção não estará disponível.

### Uso de eventos personalizados

Para que as métricas de eventos personalizados apareçam no dashboard de conversões, você deve ter um evento de conversão e um evento de entrada do Canva no intervalo de datas especificado na página. 

Para calcular as conversões de um evento que não foi configurado como um evento de conversão na campanha ou na tela, selecione um evento personalizado específico para usar como um evento de conversão. 

1. Ao configurar seu relatório, ative a opção **Usar eventos personalizados**.
2. Selecione um evento personalizado para usar como o evento de conversão.
3. Selecione a janela de conversão na qual esse evento deveria ter ocorrido para ser contado como uma conversão.

{% alert note %}
Se você selecionar um evento personalizado, não verá o menu suspenso **Evento de conversão** na página e terá que executar novamente o relatório para visualizar as conversões de diferentes eventos personalizados.
{% endalert %}

### Considerações

Para que um usuário seja contado no relatório, ele deve atender aos seguintes critérios dentro do intervalo de datas selecionado:
1. Insira o Canvas ou a campanha.
2. Registre um [método de atribuição]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#attribution-methods).
3. Realize o evento de conversão.

Por exemplo, digamos que um usuário faça o seguinte:
1. Entre no Canvas em 30 de setembro.
2. Registra um método de atribuição em 1 de outubro.
3. Realiza o evento de conversão em 2 de outubro.

Esse usuário **não** aparecerá em um relatório com um intervalo de datas de 1 a 7 de outubro. Isso ocorre porque o usuário entrou no Canvas antes do período de relatório, mesmo que o evento de conversão tenha ocorrido dentro do intervalo de datas definido. Para que o usuário apareça em um relatório, o intervalo de datas deve incluir 30 de setembro.

## Compreensão de seu relatório

Seu relatório é dividido em três seções:

- [Detalhes da conversão](#conversion-details)
- [Funil de conversão](#conversion-funnel)
- [Conversões ao longo do tempo](#conversions-over-time)

### Detalhes da conversão

A tabela de detalhes da conversão sempre mostra uma coluna para *Destinatários* e outra para *Conversões* (taxa e total). As duas colunas restantes da tabela que aparecem dependem das opções que você selecionou ao configurar o relatório. 

![Tabela de detalhes de conversão mostrando Toques como o método de atribuição para as colunas três e quatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

A tabela a seguir descreve as métricas possíveis.

| Métrica mostrada | Descrição |
| --- | --- |
| Destinatários | O número de usuários que receberam uma mensagem por meio do canal selecionado dentro do intervalo de datas do relatório |
| Taxa de conversão (destinatários) | Calculado como: (Número de conversões) / (Número de destinatários) |
| Método de atribuição | Definido pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Para atribuição do Último ponto de contato ou se vários canais forem selecionados, isso aparecerá como [Toques](#terms-to-know). |
| Taxa de conversão (método de atribuição) | Definido pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Se vários canais forem selecionados, o padrão será a atribuição do último ponto de contato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se você selecionou detalhes em nível de detalhamento para campanhas ou Canvas ao [configurar seu relatório](#setting-up-your-report) (etapa 5), poderá clicar em <i class="fas fa-angle-down"></i> para expandir a tabela.

### Funil de conversão

Esse gráfico de barras mostra as contagens absolutas de cada [evento de engajamento]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) com base no canal selecionado. A contagem de conversões será definida de acordo com o método de atribuição selecionado.

Por padrão, todas as campanhas e canvas selecionados são mostrados. Para desmarcar uma campanha ou Canvas, selecione o nome da campanha ou Canvas que você deseja excluir. Para obter detalhes adicionais sobre o evento de engajamento, passe o mouse sobre cada barra.

Para baixar os dados da série temporal, selecione uma opção de download: PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Esse gráfico mostra apenas os dados de um único canal de cada vez. Use o menu suspenso **Canal** no gráfico para selecionar um único canal.
{% endalert %}

![Gráfico de barras do funil de conversões para duas campanhas de e-mail mostrando resultados semelhantes para E-mail Entregue, E-mail Aberto, E-mail Clicado e Conversões.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversões ao longo do tempo

Esse gráfico de série temporal inclui uma representação das conversões por campanha ou Canva ao longo do tempo. Por padrão, todas as campanhas e canvas selecionados são mostrados. Para desmarcar uma campanha ou canvas, clique no nome da campanha ou canvas que você deseja excluir.

Para baixar os dados da série temporal, selecione <i class="fas fa-bars"></i> e, em seguida, selecione a opção de download. As opções disponíveis são PNG, JPEG, PDF, SVG ou CSV.

![Gráfico de séries temporais de conversões ao longo do tempo para duas campanhas de e-mail, mostrando conversões por dia.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribuição

| Método de atribuição | Definição | Cálculo da taxa | Opções específicas do canal |
| --- | --- | --- | --- |
| No momento do recebimento | Número total de conversões que ocorreram após o recebimento de mensagens | Calculado como (Conversões Únicas Recebidas) / (Destinatários Únicos) | {::nomarkdown}<ul><li>Após o envio do e-mail</li><li>Após a entrega do SMS</li></ul>{:/} |
| No momento do envio | Número total de conversões que ocorreram após o envio de mensagens | Calculado como (conversões de envio único) / (destinatários únicos) | {::nomarkdown}<ul><li>Após o envio do push</li><li>No momento do envio do cartão de conteúdo</li><li>Após o envio do SMS</li></ul>{:/} |
| Na momento da abertura | Número total de conversões que ocorreram após a abertura da mensagem | Calculado como (Conversões Abertas Únicas) / (Destinatários Únicos) | {::nomarkdown}<ul><li>Ao abrir o e-mail</li><li>No momento da abertura do push</li></ul>{:/} |
| No momento do clique | Número total de conversões que ocorreram por clique de mensagem | Calculado como (conversões de cliques únicos) / (destinatários únicos) | {::nomarkdown}<ul><li>Ao clicar no e-mail</li><li>Ao clicar no cartão de conteúdo</li><li>Ao clicar em IAM</li></ul>{:/} |
| No momento da impressão | Número total de conversões que ocorreram após uma impressão | Calculado como (conversões de impressões únicas) / (destinatários únicos) | {::nomarkdown}<ul><li>Após a impressão do IAM</li><li>Após a impressão do cartão de conteúdo</li></ul>{:/} |
| No momento do último toque | Conversões que dão todo o crédito à última mensagem tocada ou clicada durante a janela de conversão. | Calculado como (número de toques) / (destinatários únicos) | A atribuição do último ponto de contato é selecionada automaticamente se vários canais forem adicionados ao relatório.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Termos importantes

| Prazo | Definição |
| --- | --- |
| Toque | Uma interação física ou ponto de contato com uma mensagem.<br><br>Os toques podem incluir:<br>{::nomarkdown}<ul><li>Clique no e-mail</li><li>Abertura de push</li><li>Clique no cartão de conteúdo</li><li>Clique em mensagem no app</li><li>Clique em SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas

### Por que tenho baixas conversões na campanha ou no Canvas?

Suas conversões podem não ser tão altas quanto você espera quando comparadas a campanhas anteriores ou às suas expectativas. As conversões são um negócio complicado, mas dependem de algumas funções simples em nossa plataforma: rastreamento de eventos e prazos de conversão.

Para solucionar por que isso acontece, recomendamos verificar seu rastreamento de eventos e prazos de conversão.

#### Rastreamento de eventos

Quando uma campanha aciona um início de sessão ou um evento personalizado, é preciso garantir que esse evento ou sessão esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique o [painel inicial]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para dados de sessão, ou seu relatório de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reporting/configuring_reporting/).

#### Prazos de conversão

Para cada evento de conversão que você selecionar por campanha, você define o [prazo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#creating-a-campaign-with-conversion-tracking). Isso significa que você está definindo um limite de tempo dentro do qual uma conversão deve ocorrer para que seja contabilizada em cada campanha respectiva.

Verifique se você revisou as informações sobre [regras de rastreamento de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#conversion-tracking-rules) para entender as métricas da sua campanha. Para obter informações sobre conversões de usuários no Canvas, consulte [as Perguntas frequentes sobre o Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#how-are-user-conversions-tracked-in-a-canvas). 