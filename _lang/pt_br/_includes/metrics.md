{% if include.metric == "AMP Clicks" %}
<i>Cliques AMP</i> é o número total de cliques em seu e-mail HTML AMP, cumulativo das versões HTML, texto simples e HTML AMP do e-mail.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>Aberturas AMP</i> é a contagem total de aberturas em seu e-mail AMP HTML e nas versões AMP HTML do e-mail.
{% endif %}

{% if include.metric == "Audience" %}
O <i>público</i> é a porcentagem de usuários que receberam uma determinada mensagem. Esse número é recebido do Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Bounces</i> é o número total de mensagens que foram entregues sem sucesso aos destinatários pretendidos.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
A <i>estimativa de aberturas reais</i> é uma estimativa de quantas aberturas únicas haveria se as aberturas de máquina não existissem, e é o resultado de um modelo estatístico proprietário da Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Ajuda</i> é quando um usuário responde à sua mensagem com a <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palavra-chave HELP</a> e recebe uma resposta automática de HELP.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Um <i>Hard Bounce</i> é quando um e-mail não é entregue ao destinatário devido a um erro de entrega permanente. Um hard bounce pode ocorrer porque o nome de domínio não existe ou porque o destinatário é desconhecido.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Um <i>Soft Bounce</i> é quando um e-mail não é entregue ao destinatário devido a um erro de entrega temporário, mesmo que o endereço de e-mail do destinatário seja válido. Um soft bounce pode ocorrer porque a caixa de entrada do destinatário está cheia, o servidor estava fora do ar ou a mensagem era muito grande para a caixa de entrada do destinatário.
{% endif %}

{% if include.metric == "Deferral" %}
Um <i>adiamentos</i> é quando um e-mail não foi entregue imediatamente, mas o Braze tenta novamente o e-mail por até 72 horas após essa falha temporária de entrega para maximizar as chances de uma entrega bem-sucedida antes que as tentativas para essa campanha específica sejam interrompidas.
{% endif %}

{% if include.metric == "Body Click" %}
As notificações por push de histórias registram um <i>clique no corpo da mensagem</i> quando a notificação é clicada. Ele não será gravado quando uma mensagem for expandida ou para cliques em botões de ação.
{% endif %}

{% if include.metric == "Body Clicks" %}
Os <i>cliques no corpo da mensagem</i> ocorrem quando um usuário clica em uma mensagem que não tem botões (Botão 1, Botão 2) e foi criada com o editor tradicional, e quando uma mensagem criada com o editor de HTML ou o editor de arrastar e soltar usa <code>brazeBridge.logClick()</code> sem argumentos.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Cliques no Botão 1</i> é o número total de cliques no Botão 1 da mensagem.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Cliques no Botão 2</i> é o número total de cliques no Botão 2 da mensagem.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Opções enviadas</i> é o número total de opções selecionadas quando o usuário clica no botão enviar na página de perguntas de um <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>questionário simples</a>.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
A <i>taxa de cliques para abertura</i> é a porcentagem de e-mails entregues que foram abertos por um único usuário ou máquina pelo menos uma vez, e está disponível apenas no <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a>.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Fechar mensagem</i> é o número total de cliques no botão Fechar da mensagem. Isso só existe para mensagens no app criadas no editor de arrastar e soltar, não no editor tradicional.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
<i>Entregas confirmadas</i> são quando a operadora confirma que a mensagem foi entregue ao número de telefone de destino.
{% endif %}

{% if include.metric == "Confidence" %}
<i>Confiança</i> é a porcentagem de confiança de que uma determinada variante de uma mensagem supera o desempenho do grupo de controle.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Botão da página de confirmação</i> é o total de cliques no botão de chamada para ação na página de confirmação de um <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>questionário simples</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Desistências da página de confirmação</i> é o total de cliques no botão fechar (x) na página de confirmação de um <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>questionário simples</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>Taxa de conversão</i> é a porcentagem de vezes que um evento definido ocorreu em comparação com todos os destinatários de uma mensagem. Esse evento definido é determinado quando você cria a campanha.
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>Janela de conversão</i> é o número de dias após o recebimento da mensagem durante os quais as ações do usuário são rastreadas e atribuídas a um evento de conversão. As conversões que acontecem após este período não são atribuídas ao evento de conversão.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
As <i>conversões (B, C, D)</i> são eventos de conversão adicionais adicionados após o evento de conversão primária. Esse é o número de vezes que um evento definido ocorreu após a interação ou a visualização de uma mensagem recebida de uma campanha do Braze.
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>Total de conversões</i> é o número total de vezes que um usuário conclui um evento de conversão específico depois de visualizar uma campanha de mensagens no app.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Entregas</i> é o número total de solicitações de mensagens que são aceitas pelo servidor receptor. Isso não significa que a mensagem foi entregue a um dispositivo, apenas que ela foi aceita pelo servidor.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>Entregas %</i> é a porcentagem do número total de mensagens (Envios) enviadas e recebidas com êxito pelas partes que podem enviar e-mails.
{% endif %}

{% if include.metric == "Delivery Failures" %}
As <i>falhas de entrega</i> ocorrem quando o SMS não pode ser enviado devido ao transbordamento das filas (envio de SMS em uma taxa maior do que os códigos longos ou curtos podem suportar).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>As falhas de entrega</i> ocorrem quando o RCS não pode ser enviado devido ao transbordamento das filas (envio de RCS em uma taxa maior do que o remetente verificado pelo RCS pode suportar).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
A <i>taxa de falha na entrega</i> é a porcentagem de envios que falharam porque a mensagem não pôde ser enviada. Isso pode acontecer por vários motivos, incluindo estouro de fila, suspensões de conta e erros de mídia no caso de MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Aberturas diretas</i> é o número total de usuários que abriram seu app ou site pressionando diretamente a notificação.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Envio de e-mail</i> é o número total de usuários que têm um endereço de e-mail registrado e que explicitamente aceitaram ou se inscreveram.
{% endif %}

{% if include.metric == "Errors" %}
<i>Erros</i> é o número de erros retornados por eventos de webhook (incrementado durante o processo de envio).
{% endif %}

{% if include.metric == "Failures" %}
As <i>falhas</i> ocorrem quando a mensagem do WhatsApp não pode ser enviada porque o prestador de serviço de Internet retornou um hard bounce. Um hard bounce significa uma falha permanente de entregabilidade.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Aberturas por influência</i> é o número total (e a porcentagem) de usuários que abriram o app depois que a notificação por push foi enviada, sem abrir diretamente o push.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
<i>A receita vitalícia</i> é o total de  <code>PurchaseEvents</code> valor do preço (em USD) recebido desde o início.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
O <i>Valor do tempo de vida por usuário</i> é a <i>receita do tempo de vida</i> dividida pelo total de <i>usuários</i> (localizado na página inicial).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
A <i>receita média diária</i> é a média da soma da receita da campanha e da receita do Canva em um determinado dia.
{% endif %}

{% if include.metric == "Daily Purchases" %}
As <i>compras diárias</i> são a média do total de compras únicas <code>PurchaseEvents</code> durante o período de tempo.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
<i>Receita diária por usuário</i> é a receita média diária por usuário ativo diário.
{% endif %}

{% if include.metric == "Machine Opens" %}
As <i>aberturas por máquina</i> incluem a proporção de "aberturas" que são afetadas pela proteção de privacidade de e-mail (MPP) da Apple para iOS 15. Por exemplo, se um usuário abrir um e-mail usando o app Mail em um dispositivo Apple, isso será registrado como uma <i>abertura de máquina</i>.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Outras aberturas</i> inclui e-mails que não foram identificados como <i>aberturas de máquina</i>. Por exemplo, quando um usuário abre um e-mail em outra plataforma (como o app do Gmail em um telefone ou o Gmail em um navegador de desktop), isso será registrado como <i>Outras aberturas</i>.
{% endif %}

{% if include.metric == "Opens" %}
As <i>aberturas</i> são instâncias que incluem <i>aberturas diretas</i> e <i>aberturas por influência</i> nas quais o SDK da Braze determinou, usando um algoritmo proprietário, que uma notificação por push fez com que um usuário abrisse o aplicativo.
{% endif %}

{% if include.metric == "Opt-Out" %}
<i>Opt-Out</i> é quando um usuário respondeu à sua mensagem com uma <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palavra-chave de aceitação</a> e cancelou a inscrição no seu programa de SMS ou RCS.
{% endif %}

{% if include.metric == "Pending Retry" %}
<i>Pending Retry (Tentativa pendente)</i> é o número de solicitações que foram temporariamente rejeitadas pelo servidor de recebimento, mas que ainda tentaram ser reentregues pelo provedor de serviço de e-mail (ESP). O ESP tentará novamente a entrega até que um período de tempo limite seja atingido (normalmente após 72 horas).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Conversões primárias (A)</i> ou <i>evento de conversão primária</i> é o número de vezes que um evento definido ocorreu após a interação ou a visualização de uma mensagem recebida de uma campanha do Braze. Esse evento definido é determinado por você ao criar a campanha.
{% endif %}

{% if include.metric == "Reads" %}
<i>Reads</i> é quando o usuário lê a mensagem. Os recibos de leitura do usuário devem estar "Ativados" para que a Braze rastreie as leituras.
{% endif %}

{% if include.metric == "Read Rate" %}
<i>Taxa de leitura</i> é a porcentagem de envios que resultaram em uma leitura. Isso é fornecido apenas para usuários que têm recibos de leitura ativados.
{% endif %}

{% if include.metric == "Received" %}
O <i>recebimento</i> é definido de forma diferente por canal e pode ser quando os usuários visualizam a mensagem, quando os usuários executam uma ação-gatilho definida ou quando a mensagem é enviada ao provedor de mensagens.
{% endif %}

{% if include.metric == "Rejections" %}
<i>As rejeições</i> ocorrem quando o SMS ou RCS foi rejeitado pela operadora. Isso pode ocorrer por vários motivos, inclusive filtragem de conteúdo da operadora, disponibilidade do dispositivo de destino, o número de telefone não está mais em serviço e outros semelhantes.
{% endif %}

{% if include.metric == "Revenue" %}
<i>Receita</i> é a receita total em dólares dos destinatários da campanha dentro da <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>janela de conversão primária</a> definida.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Mensagens enviadas</i> é o número total de mensagens enviadas em uma campanha. Após o lançamento de uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de frequência. Isso não significa que a mensagem foi recebida ou entregue em um dispositivo, apenas que a mensagem foi enviada.
{% endif %}

{% if include.metric == "Sent" %}
<i>Enviado</i> é toda vez que uma campanha ou etapa do Canva foi lançada ou disparada e um SMS ou RCS foi enviado pelo Braze. É possível que o SMS ou RCS não tenha chegado ao dispositivo do usuário devido a erros.
{% endif %}

{% if include.metric == "Sends" %}
<i>Envios</i> é o número total de mensagens enviadas em uma campanha. Após o lançamento de uma campanha programada, essa métrica incluirá todas as mensagens enviadas, independentemente de já terem sido enviadas devido ao limite de frequência. Isso não significa que a mensagem foi recebida ou entregue em um dispositivo, apenas que a mensagem foi enviada.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
O <i>envio para a operadora</i> está obsoleto, mas continuará a ter suporte para os usuários que já o possuem. É a soma de Entregas <i>Confirmadas</i>, <i>Rejeições</i> e <i>Envios</i> em que a entrega ou rejeição não foi confirmada pela operadora. Isso inclui os casos em que as operadoras não fornecem confirmação de entrega ou de rejeição, pois algumas operadoras não fornecem essa confirmação ou não podem fazê-lo no momento do envio.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
A <i>taxa de envios para a operadora</i> é a porcentagem do total de mensagens enviadas que foram classificadas como <i>Envios para a operadora</i>. Isso inclui os casos em que as operadoras não fornecem confirmação de entrega ou rejeição, pois algumas operadoras não fornecem essa confirmação ou não podem fazê-lo no momento do envio. Essa métrica está obsoleta, mas continuará a ter suporte para os usuários que já a possuem.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> é o número total de e-mails entregues que foram marcados como "spam" pelo destinatário. Embora o Braze não altere o estado da inscrição desses usuários, eles serão automaticamente excluídos em e-mails futuros, a menos que você esteja enviando um e-mail de transação, que está configurado para "enviar a todos os usuários, inclusive cancelar inscrição".
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Dispensas de página de questionário</i> é o total de cliques no botão fechar (x) na página de perguntas de um <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>questionário simples</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Envios de questionário</i> é o total de cliques no botão enviar de um <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>questionário simples</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Total de cliques</i> é o número de destinatários únicos que clicaram em um link na mensagem entregue.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>Total de descartes</i> é o número de vezes que os cartões de conteúdo de uma campanha foram descartados.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>Total de impressões</i> é o número de vezes que a mensagem foi carregada e aparece na tela do usuário, independentemente da interação anterior (por exemplo, se uma mensagem for mostrada a um usuário duas vezes, ele será contado duas vezes).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Total de aberturas</i> é o número total de mensagens que foram abertas.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Receita total</i> é a receita total em dólares dos destinatários da campanha dentro da janela de conversão primária definida.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Cliques únicos</i> é o número distinto de destinatários que clicaram em um link em uma mensagem pelo menos uma vez e é medido por <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Dispensas únicas</i> é o número de destinatários únicos que dispensaram um cartão de conteúdo de uma campanha. Um usuário que descarta um cartão de conteúdo de uma campanha várias vezes representa uma única rejeição.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
<i>Impressões únicas</i> é o número total de usuários que receberam e visualizaram uma mensagem de uma determinada campanha.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Unique Recipients (Destinatários únicos</i> ) é o número de destinatários diários únicos, ou usuários que receberam uma nova mensagem em um dia. Para que essa contagem seja incrementada para um usuário mais de uma vez, o usuário deve receber uma nova mensagem em um dia diferente.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Aberturas exclusivas</i> é o número total de mensagens enviadas que foram abertas por um único usuário pelo menos uma vez e são rastreadas durante um período de sete dias.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Cancelamentos de inscrição</i> ou <i>Unsub</i> é o número de mensagens que resultaram em um cancelamento de inscrição. Os cancelamentos de inscrição ocorrem quando um usuário clica no ink de cancelamento de inscrição da Braze.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Cancelamentos de inscrição</i> é o número de destinatários cujo estado de inscrição foi alterado para cancelado como resultado de um clique no URL de cancelamento de inscrição fornecido pela Braze.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variação</i> é o número de variações de uma campanha, diferindo conforme definido pelo criador.
{% endif %}
