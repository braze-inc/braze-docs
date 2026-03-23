---
page_order: 2
nav_title: Filtros de segmentação
article_title: Filtros de Segmentação
layout: glossary_page
glossary_top_header: "Filtros de Segmentação"
glossary_top_text: "O SDK da Braze fornece um poderoso arsenal de filtros para segmentar e direcionar seus usuários com base em recursos e atributos específicos. Você pode pesquisar ou restringir esses filtros por categoria de filtro.<br><br>Para saber mais sobre os diferentes tipos de dados de atributo personalizado que você pode usar para segmentar usuários, veja <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">Tipos de dados de atributo personalizado</a>."

page_type: glossary
tool: Segments
description: "Este glossário lista os filtros disponíveis para segmentar e direcionar seus usuários."
search_rank: 2
glossary_tag_name: Categoria do filtro
glossary_filter_text: "Selecione uma categoria para restringir o glossário:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic). Do not translate.
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: "Permite filtrar com base na associação de segmento em qualquer lugar onde os filtros são usados (como segmentos, campanhas e outros) e direcionar vários segmentos diferentes dentro de uma campanha. <br><br>Observe que os segmentos que já estão usando esse filtro não podem ser incluídos ou aninhados em outros segmentos, pois isso pode criar um ciclo em que o Segmento A inclui o Segmento B, que, por sua vez, tenta incluir o Segmento A novamente. Se isso acontecesse, o segmento continuaria fazendo referência a si mesmo, tornando impossível calcular quem realmente pertence a ele. Além disso, o aninhamento de segmentos como esse aumenta a complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que está tentando incluir usando os mesmos filtros."
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: "Depois de criar uma extensão de segmento no dashboard da Braze, você pode escolher incluir/excluir essas extensões no seu segmento."
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: Segmenta seus usuários com base em se eles faziam parte de um upload de CSV ou não.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: "Determina se um usuário corresponde ou não a um valor de atributo personalizado registrado. <br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom attribute
  - name: Created At
    description: "Segmenta os usuários de acordo com a data de criação do perfil de usuário. Se um usuário tiver sido adicionado por CSV ou API, esse filtro refletirá a data em que ele foi adicionado. Se o usuário não for adicionado por CSV ou API e tiver sua primeira sessão rastreada pelo SDK, esse filtro refletirá a data dessa primeira sessão."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: "Atributos que são as propriedades de atributos personalizados.<br><br>Ao filtrar um atributo personalizado de tempo aninhado, você pode escolher filtrar com base em \"Dia do Ano\" ou \"Hora\". \"Dia do Ano\" verifica apenas o mês e o dia para comparação. \"Hora\" compara o timestamp completo, incluindo o ano."
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: "Este filtro analisa o mês e o dia do atributo personalizado com o tipo de dado \"data\", mas não analisa o ano. Este filtro é útil para eventos anuais.<br><br>Fuso horário&#58;<br>Este filtro se ajusta a qualquer fuso horário em que o usuário esteja, desde que a mensagem seja enviada usando a opção de agendamento de horário local; caso contrário, este filtro usa o fuso horário da sua empresa."
    tags:
      - Custom attribute
  - name: Custom Event
    description: "Determina se um usuário realizou ou não um evento especialmente registrado.<br><br> Exemplo:<br>Atividade concluída com a propriedade activity_name.<br><br>Fuso horário:<br>UTC - Dia do Calendário = 1 dia do calendário considera 24-48 horas de histórico do usuário"
    tags:
      - Custom events
  - name: First Did Custom Event
    description: "Determina o primeiro horário em que um usuário realizou um evento especialmente registrado. (período de 24 horas) <br><br>Exemplo:<br> Primeiro Carrinho Abandonado Há menos de 1 dia<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: "Determina a última vez que um usuário realizou um evento especialmente registrado. Este filtro suporta decimais, como 0,25 horas. (período de 24 horas) <br><br>Exemplo:<br> Último Carrinho Abandonado Há menos de 1 dia<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: "Determina se um usuário realizou ou não um evento especialmente registrado entre 0 e 50 vezes nos últimos dias de calendário especificados entre 1 e 30. (Dia do Calendário = 1 dia do calendário considera 24-48 horas de histórico do usuário)<br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento de X-em-Y aqui.</a> <br><br>Exemplo:<br>Carrinho abandonado exatamente 0 vezes no último 1 dia de calendário<br><br>Fuso horário:<br>UTC - Para contabilizar todos os fusos horários, 1 dia do calendário considera 24-48 horas de histórico do usuário, dependendo do horário em que o segmento é avaliado; para 2 dias do calendário, considera 48-72 horas de histórico do usuário, e assim por diante."
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: "Determina se um usuário realizou ou não um evento especialmente registrado em relação a uma propriedade específica entre 0 e 50 vezes nos últimos dias de calendário especificados entre 1 e 30. (Dia do Calendário = 1 dia do calendário considera 24-48 horas de histórico do usuário)<br><a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a> <br><br>Exemplo:<br> Adicionado aos Favoritos com a propriedade \"event_name\" exatamente 0 vezes no último 1 dia de calendário<br><br>Fuso horário:<br>UTC - Para contabilizar todos os fusos horários, 1 dia do calendário considera 24-48 horas de histórico do usuário, dependendo do horário em que o segmento é avaliado; para 2 dias do calendário, considera 48-72 horas de histórico do usuário, e assim por diante."
    tags:
      - Custom events
  - name: Email Address
    description: "Permite designar os destinatários da sua campanha por endereços de e-mail individuais para teste. Isso também pode ser usado para enviar e-mails de transação a todos os seus usuários (incluindo os que cancelaram a inscrição) usando o especificador \"Endereço de E-mail não está em Branco\" dentro do filtro, para que você possa maximizar a entrega de e-mails, independentemente do status de aceitação. <br><br>Este filtro apenas verifica se os perfis de usuário têm um endereço de e-mail, enquanto o filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">E-mail Disponível</a> verifica critérios adicionais."
    tags:
      - Other Filters
  - name: External User ID
    description: Permite designar os destinatários da sua campanha por IDs de usuário individuais para teste.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: Segmenta seus usuários por um número atribuído aleatoriamente (0 a 9999 inclusive). Ele pode ativar a criação de segmentos uniformemente distribuídos de usuários verdadeiramente aleatórios para testes A/B e multivariantes.
    tags:
      - Other Filters
  - name: Session Count
    description: Segmenta seus usuários pelo número de sessões que eles tiveram em qualquer um dos seus apps dentro do seu espaço de trabalho.
    tags:
      - Sessions
  - name: Session Count For App
    description: Segmenta seus usuários pelo número de sessões que tiveram em um app específico e designado.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: "Segmenta seus usuários pelo número de sessões (entre 0 e 50) que eles tiveram em seu app nos últimos dias de calendário especificados entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Sessions
  - name: First Used App
    description: "Segmenta seus usuários pelo horário mais antigo registrado em que abriram seu app. <em>Isso captura a primeira sessão que eles tiveram usando uma versão do seu app com o SDK da Braze integrado.</em> (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: First Used Specific App
    description: "Segmenta seus usuários pelo horário mais antigo registrado em que abriram qualquer um dos seus apps dentro do seu espaço de trabalho. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Last Used App
    description: "Segmenta seus usuários pelo horário mais recente em que abriram seu app. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Last Used Specific App
    description: "Segmenta seus usuários pelo horário mais recente em que abriram um app específico e designado. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Median Session Duration
    description: Segmenta seus usuários pela duração mediana de suas sessões no seu app.
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica. Este filtro captura apenas usuários que receberam a mensagem explicitamente, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensagem Recebida de Campanha ou Canvas com Tag</a>.<br><br> Para Cartões de conteúdo, Banners e mensagens no app, isso é quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: "Segmenta seus usuários por qual variante de uma campanha multivariante eles receberam. Este filtro captura apenas usuários que receberam a mensagem explicitamente, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensagem Recebida de Campanha ou Canvas com Tag</a>.<br><br> Para Cartões de conteúdo, Banners e mensagens no app, isso é quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: "Segmenta seus usuários por terem ou não recebido um componente específico do canva. Este filtro captura apenas usuários que receberam a mensagem explicitamente, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensagem Recebida de Campanha ou Canvas com Tag</a>.<br><br> Para Cartões de conteúdo e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: "Segmenta seus usuários por quando receberam um componente específico do canva. Este filtro captura apenas usuários que receberam a mensagem explicitamente, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas; para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensagem Recebida de Campanha ou Canvas com Tag</a>. Esse filtro não considera quando os usuários receberam outros componentes do canva."
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica. Este filtro captura apenas usuários que receberam a mensagem explicitamente, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas; para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensagem Recebida de Campanha ou Canvas com Tag</a>. Esse filtro não considera quando os usuários receberam outras campanhas."
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica ou canva com uma tag específica. Diferente de \"Mensagem Recebida de Campanha\" e \"Mensagem Recebida de Etapa do Canvas\", este filtro captura todos os usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas.<br><br> Para Cartões de conteúdo, Banners (apenas Campanhas) e mensagens no app, isso é quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário então abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: Segmenta seus usuários por quando receberam uma campanha específica ou canva com uma tag específica. Esse filtro não considera quando os usuários receberam outras campanhas ou canvas. (período de 24 horas)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: Segmenta seus usuários por terem ou não recebido qualquer campanha ou componente de canva.
    tags:
      - Retargeting
  - name: Last Received Email
    description: "Segmenta seus usuários pela última vez que receberam uma de suas mensagens de e-mail. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Last Received Push
    description: "Segmenta seus usuários pela última vez que receberam uma de suas notificações por push. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: Segmenta seus usuários pela última vez que visualizaram uma mensagem no app.
    tags:
      - Retargeting
  - name: Last Received SMS
    description: "Segmenta seus usuários pelo momento em que a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: "Segmenta seus usuários pela última vez que a Braze enviou um webhook para esse usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: "Segmenta seus usuários pela última vez que receberam uma mensagem do WhatsApp. Isso é quando a solicitação de API da última mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: Segmenta seus usuários com base em se estão registrados para iniciar uma Live Activity através de notificações por push do iOS para um app específico.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: "Filtrar por interação com uma campanha específica. Para envio de mensagens por e-mail, o evento de abertura inclui tanto aberturas de máquina quanto aberturas não-máquina.<br><br> Para e-mail, isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Cliques em links de cancelamento de inscrição e centrais de preferência não contam para esse filtro. Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>- O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha."
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: "Filtrar por interação com uma campanha específica que possui uma tag específica. Para envio de mensagens por e-mail, o evento de abertura inclui tanto aberturas de máquina quanto aberturas não-máquina.<br><br> Para e-mail, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>- Quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha ou etapa do canva com tag."
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: "Filtrar por interação com um componente específico do canva. Para envio de mensagens por e-mail, o evento de abertura inclui tanto aberturas de máquina quanto aberturas não-máquina.<br><br>Para e-mail, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\".<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas. <br>- O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, a partir de uma determinada etapa do canva."
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: "Filtre seus usuários por terem clicado em um alias específico em uma campanha específica. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: "Filtre seus usuários por terem clicado em um alias específico em um canva específico. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: "Filtre seus usuários por terem clicado em um alias específico em qualquer campanha ou canva. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Hard Bounced
    description: Segmente seus usuários por saber se o endereço de e-mail deles teve um hard bounce (como quando o endereço de e-mail é inválido).
    tags:
      - Retargeting
  - name: Soft Bounced
    description: "Segmente seus usuários de acordo com o número de soft bounces X vezes em Y dias. Os filtros de segmento só podem olhar para trás 30 dias, mas você pode olhar mais para trás com as extensões de segmento.<br><br>Esse filtro funciona de forma diferente de um evento de soft bounce no Currents. O filtro de segmento Soft Bounced conta um soft bounce se não houver uma entrega bem-sucedida durante o período de tentativa de 72 horas. No Currents, cada tentativa malsucedida é enviada como um evento de soft bounce."
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: Segmenta seus usuários por se eles marcaram ou não suas mensagens como spam.
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: Segmenta seus usuários por se o número de telefone deles é inválido ou não.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: Segmenta seus usuários pelo momento em que enviaram um SMS pela última vez para um grupo de inscrições específico dentro de uma categoria de palavra-chave específica.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: Segmenta seus usuários por terem ou não convertido em uma campanha específica. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: Segmenta seus usuários por terem ou não convertido em um canva específico. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: Segmenta seus usuários por estarem ou não no grupo de controle para uma campanha multivariante específica.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: "Segmenta seus usuários por estarem ou não no grupo de controle para um canva específico. Esse filtro avalia apenas usuários que entraram no canva, portanto, usuários que nunca entraram são excluídos dos resultados completamente.<br><br>Por exemplo, se você filtrar por usuários que não estão no grupo de controle de um canva, você recebe apenas usuários que entraram no canva e foram designados a uma variante não-controle — usuários que nunca entraram no canva não estão incluídos. Para incluir todos os usuários, independentemente da entrada no canva, use o filtro <code>Entered Canvas Variation</code> em vez disso."
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: "Segmenta seus usuários pela última vez que caíram no grupo de controle em uma campanha. <br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: "Segmenta seus usuários por terem ou não entrado em uma jornada de variação de um canva específico. Este filtro avalia todos os usuários.<br><br>Por exemplo, se você filtrar por usuários que não entraram em um grupo de controle de variação do canva, você recebe todos os usuários que não estão no grupo de controle, independentemente de terem entrado no canva."
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: "Segmenta seus usuários determinando a última mensagem que foi recebida. (período de 24 horas)<br><br> Para Cartões de conteúdo, Banners e mensagens no app, isso é quando um usuário registrou a última impressão, não quando o cartão ou mensagem no app foi enviado pela última vez.<br><br>Para push e webhooks, isso é quando qualquer mensagem foi enviada ao usuário.<br><br> Para o WhatsApp, isso é quando a última solicitação de API de mensagem foi enviada para o WhatsApp, não quando a mensagem foi entregue ao dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário então abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário.<br><br>Exemplo:<br>Última mensagem recebida há menos de 1 dia = menos de 24 horas atrás<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: "Segmenta seus usuários pela última vez que clicaram ou abriram um de seus canais de envio de mensagens (Banners, cartão de conteúdo, e-mail, no app, SMS, push, WhatsApp). Para envio de mensagens por e-mail, o evento de abertura inclui tanto aberturas de máquina quanto aberturas não-máquina. (período de 24 horas)<br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente de ela realmente ser entregue). Isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário então abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem que tem o rastreamento de cliques do usuário ativado.<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Clicked card
    description: "Segmenta seus usuários por terem ou não clicado em um cartão de conteúdo específico. Este filtro está disponível como um subfiltro de \"Campanha clicada/aberta\", \"Campanha clicada/aberta ou Canvas com Tag\" e \"Etapa clicada/aberta\"."
    tags:
      - Retargeting
  - name: Feature Flags
    description: "O segmento de seus usuários que têm uma <a href=\"/docs/developer_guide/feature_flags/\">Feature Flag</a> específica atualmente ativada."
    tags:
      - Retargeting
  - name: Subscription Group
    description: "Segmenta seus usuários por seu grupo de inscrições para e-mail, SMS/MMS ou WhatsApp. Grupos arquivados não aparecem e não podem ser usados."
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: "Segmenta seus usuários com base em se possuem um endereço de e-mail válido e se estão inscritos ou optaram por receber e-mails. Esse filtro verifica três critérios&#58; se o usuário cancelou a inscrição de e-mails, se a Braze recebeu um hard bounce e se o e-mail foi marcado como spam. Se algum desses critérios for atendido, ou se um e-mail não existir para um usuário, o usuário não é incluído.<br><br>Usuários cujo E-mail Disponível é <code>false</code> são excluídos do público da campanha e não recebem o e-mail — mesmo que suas configurações de envio estejam configuradas para enviar para todos os usuários (incluindo usuários que cancelaram a inscrição).<br><br>Para e-mails onde o status de aceitação é importante, use E-mail Disponível em vez de <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">Endereço de E-mail</a>. Os critérios adicionais ajudam você a direcionar usuários que são elegíveis para receber e-mail."
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: Segmenta seus usuários pela data em que optaram por receber e-mail.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: Segmenta seus usuários pelo status de inscrição para e-mail.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de futuros e-mails.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: "Segmenta seus usuários que têm autorização provisória de push ou estão habilitados para push em primeiro plano. Especificamente, esta contagem inclui:<br>1. Usuários do iOS que estão provisoriamente autorizados para push. <br>2. Usuários que têm push habilitado em primeiro plano e cujo status de inscrição em push não é cancelado, para qualquer um dos seus apps. Para esses usuários, essa contagem inclui apenas push em primeiro plano.<br><br>Push Habilitado em Primeiro Plano não inclui usuários que cancelaram a inscrição. <br><br>Após segmentar com este filtro, você pode ver uma divisão de quem está nesse segmento para Android, iOS e web no painel inferior, chamado <em>Reachable Users</em>."
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: Segmenta por se os usuários têm push ativado para seu app em seu dispositivo. Usuários que têm push habilitado em primeiro plano para um app. Isso não leva em conta o status de inscrição em push. Esta contagem inclui usuários que autorizaram provisoriamente tokens de push em primeiro e segundo plano.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: Segmenta por se os usuários têm um token por push e não cancelaram a inscrição. Usuários que têm push habilitado em segundo plano ou em primeiro plano para qualquer um dos seus apps.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: Segmenta seus usuários pela data em que aceitaram o recebimento de push.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: "Segmenta seus usuários pelo <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">status de inscrição</a> para push."
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de futuras notificações por push.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: Segmenta seus usuários por produtos comprados no seu app.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: Segmenta seus usuários pelo número de compras que fizeram no seu app.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: Filtra usuários pelo número de vezes que um produto específico foi comprado.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: "Segmenta seus usuários pelo número de vezes (entre 0 e 50) que fizeram uma compra nos últimos dias de calendário especificados entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: "Segmenta seus usuários pelo número de vezes que uma compra foi feita em relação a uma certa propriedade de compra nos últimos dias de calendário especificados entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: Segmenta seus usuários pelo momento mais antigo em que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: Segmenta seus usuários pelo momento mais antigo em que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: Filtra usuários pela última vez que fizeram uma compra.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: Filtra os usuários pela última vez que compraram um produto específico.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: Segmenta seus usuários pela quantidade de dinheiro que gastaram no seu app.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: "Segmenta seus usuários pela quantidade de dinheiro que gastaram no seu app nos últimos dias de calendário especificados entre 1 e 30. Esse valor inclui apenas a soma das últimas 50 compras. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: "Segmenta seus usuários por quando fizeram o último pedido, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia, e a janela máxima de retrocesso é os últimos 2 anos.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: "Segmenta seus usuários pela contagem total de pedidos de um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido cancelado. Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total orders count
    description: "Segmenta seus usuários pela contagem total de pedidos de um usuário ao longo de sua vida, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido cancelado. Os usuários são avaliados para este filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: "Segmenta seus usuários pelo total de pedidos que um usuário cancelou nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: "Segmenta seus usuários pela receita total que um usuário deve gerar ao longo de seu histórico de compras com sua marca. O cálculo considera os últimos 730 dias e leva em conta o Valor Médio do Pedido (AOV), multiplica pelo total de pedidos realizados e, em seguida, considera a duração ativa de compras do usuário (o intervalo de tempo entre seu primeiro e seu pedido mais recente). Este filtro usa dados rastreados em <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eventos recomendados de eCommerce</a> (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: "Segmenta seus usuários pelo valor de reembolsos concedidos a um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido reembolsado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total refund value
    description: "Segmenta seus usuários pelo valor total de reembolsos concedidos a um usuário ao longo de sua vida, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido reembolsado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: "Segmenta seus usuários pela receita total gerada a partir dos pedidos de um usuário nos últimos 2 anos, calculada com base na subtração da receita associada ao <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido reembolsado da receita associada ao evento de eCommerce para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Total revenue
    description: "Segmenta seus usuários pela receita total gerada a partir dos pedidos de um usuário ao longo de sua vida, calculada com base na subtração da receita associada ao <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido reembolsado da receita associada ao evento de eCommerce para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: "Segmenta seus usuários pelo valor médio (média) dos pedidos de um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não têm dados para este filtro). Os usuários são avaliados para este filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com seu gerente de conta da Braze se você tiver interesse em usar este filtro."
    tags:
      - eCommerce
  - name: Country
    description: Segmenta seus usuários pelo último país indicado.
    tags:
      - Demographic attributes
  - name: City
    description: Segmenta seus usuários pela última cidade indicada.
    tags:
      - Demographic attributes
  - name: Language
    description: Segmenta seus usuários pelo idioma preferido.
    tags:
      - Demographic attributes
  - name: Age
    description: "Segmenta seus usuários pela idade, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Birthday
    description: "Segmenta seus usuários pelo aniversário, conforme indicado no seu app. <br> Usuários com aniversário no dia 29 de fevereiro estão incluídos em segmentos que incluem 1º de março.<br><br>Para direcionar aniversários de dezembro ou janeiro, insira a lógica do filtro apenas dentro do período de 12 meses do ano que você está direcionando. Em outras palavras, não insira lógica que olhe para trás para o dezembro do ano anterior ou para frente para o janeiro do próximo ano. Por exemplo, para direcionar aniversários em dezembro, você pode filtrar por \"em 31 de dezembro\", \"antes de 31 de dezembro\" ou \"depois de 30 de novembro\"."
    tags:
      - Demographic attributes
  - name: Gender
    description: "Segmenta seus usuários por gênero, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: "Segmenta seus usuários pelo número de telefone não formatado. Não inclui parênteses, traços ou outros símbolos."
    tags:
      - Demographic attributes
  - name: First Name
    description: "Segmenta seus usuários pelo nome, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Last Name
    description: "Segmenta seus usuários pelo sobrenome, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Has App
    description: "Segmenta por saber se um usuário já instalou seu app ou não. Isso inclui usuários que atualmente têm seu app instalado e aqueles que desinstalaram no passado. Isso geralmente requer que os usuários abram o app (iniciem uma sessão) para serem incluídos neste filtro. No entanto, há algumas exceções, como se um usuário foi importado para a Braze e associado manualmente ao seu app."
    tags:
      - App
  - name: Most Recent App Version Name
    description: "Segmenta pelo nome recente do app do usuário.<br><br>Ao usar \"menor que\" ou \"menor ou igual a\", se a versão principal do app não existir, este filtro retorna `true` porque o usuário é mais antigo que a versão do app. Isso significa que se a última versão principal do app do usuário não existir, eles automaticamente correspondem ao filtro."
    tags:
      - App
  - name: Most Recent App Version Number
    description: "Segmenta pelo número da versão recente do app do usuário.<br><br>Ao usar \"menor que\" ou \"menor ou igual a\", se a versão principal do app não existir, este filtro retorna `true` porque o usuário é mais antigo que a versão do app. Isso significa que se a última versão principal do app do usuário não existir, eles automaticamente correspondem ao filtro.<br><br>Pode levar tempo para que as versões atuais do app sejam populadas. A versão do app no perfil do usuário é atualizada quando as informações são capturadas pelo SDK, o que depende de quando os usuários abrem seus apps. Se o usuário não abrir o app, a versão atual não será atualizada. Esses filtros também não se aplicam retroativamente. É recomendável usar \"maior que\" ou \"igual\" para versões atuais e futuras, mas usar filtros de versões passadas pode causar comportamentos inesperados."
    tags:
      - App
  - name: Uninstalled
    description: Segmenta seus usuários por terem desinstalado seu app e não o reinstalado.
    tags:
      - Uninstall
  - name: Device Carrier
    description: Segmenta seus usuários pela operadora do dispositivo.
    tags:
      - Devices
  - name: Device Count
    description: Segmenta seus usuários pelo número de dispositivos em que usaram seu app.
    tags:
      - Devices
  - name: Device Model
    description: Segmenta seus usuários pela versão do modelo do celular.
    tags:
      - Devices
  - name: Device OS
    description: "Segmenta seus usuários que possuem um ou mais dispositivos com o sistema operacional especificado. Para segmentar usuários por uma faixa de sistemas operacionais, use o filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">Número da Versão do SO do Dispositivo</a>."
    tags:
      - Devices
  - name: Device OS Version Number
    description: "Segmenta seus usuários que possuem um ou mais dispositivos com uma versão do sistema operacional dentro de uma faixa especificada. Por exemplo, você pode direcionar usuários que têm uma versão do sistema operacional iOS maior ou igual a 26.0."
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: "Segmenta seus usuários pela <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">informação de localidade</a> do dispositivo mais recentemente usado."
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: Segmenta seus usuários pelo modelo de smartwatch mais recente.
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: Permite encontrar usuários que estão provisoriamente autorizados no iOS 12 para um determinado app.
    tags:
      - Devices
  - name: Web Browser
    description: Segmenta seus usuários pelo navegador da web que usam para acessar seu site.
    tags:
      - Devices
  - name: Device IDFA
    description: Permite designar os destinatários da sua campanha por IDFA para teste.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: Permite designar os destinatários da sua campanha por IDFV para teste.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: Segmenta seus usuários pelo ID de anúncio do Google.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Segmenta seus usuários pelo ID de anúncio do Roku.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Segmenta seus usuários pelo ID de anúncio do Windows.
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: "Permite filtrar com base em se seus usuários optaram pelo rastreamento de anúncios. O rastreamento de anúncios está relacionado ao IDFA ou \"identificador para anunciantes\" atribuído a todos os dispositivos iOS pela Apple, que pode ser configurado por SDKs. Esse identificador permite que os anunciantes rastreiem os usuários e exibam anúncios direcionados."
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: Segmenta seus usuários pela última localização registrada em que usaram seu app.
    tags:
      - Location
  - name: Location Available
    description: "Segmenta seus usuários por terem ou não relatado suas localizações. Para usar este filtro, seu app precisa ter <a href=\"/docs/search/?query=location%20tracking\">monitoramento de localização integrado.</a>"
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Clientes que usam Amplitude podem complementar seus segmentos escolhendo e importando suas coortes no Amplitude.
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Clientes que usam Census podem complementar seus segmentos escolhendo e importando suas coortes no Census.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Clientes que usam Heap podem complementar seus segmentos escolhendo e importando suas coortes no Heap.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Clientes que usam Hightouch podem complementar seus segmentos escolhendo e importando suas coortes no Hightouch.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Clientes que usam Kubit podem complementar seus segmentos escolhendo e importando suas coortes no Kubit.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Clientes que usam Mixpanel podem complementar seus segmentos escolhendo e importando suas coortes no Mixpanel.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Clientes que usam o Segment podem complementar seus segmentos escolhendo e importando suas coortes no Segment.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Clientes que usam Tinyclues podem complementar seus segmentos escolhendo e importando suas coortes no Tinyclues.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: Segmenta seus usuários pelo anúncio ao qual a instalação deles foi atribuída.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: Segmenta seus usuários pelo grupo de anúncios ao qual a instalação deles foi atribuída.
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: Segmenta seus usuários pela campanha publicitária à qual a instalação deles foi atribuída.
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: Segmenta seus usuários pela fonte à qual a instalação deles foi atribuída.
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: Segmenta seus usuários por categoria de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: Segmenta seus usuários pelo score de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: Segmente seus usuários pelo canal mais ativo nos últimos três meses.
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: "Filtra seus usuários com base na <a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">probabilidade de abrir uma mensagem em um canal especificado</a> em uma escala de 0 a 100%. Usuários sem dados suficientes para medir a probabilidade de um canal podem ser selecionados usando \"está em branco\".<br><br>Para e-mail, aberturas de máquina são excluídas do cálculo de probabilidade."
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: Segmenta seus usuários pelo número de amigos no Facebook que usam o mesmo app.
    tags:
      - Social activity
  - name: Connected Facebook
    description: Segmenta seus usuários por terem conectado seu app ao Facebook.
    tags:
      - Social activity
  - name: Connected Twitter
    description: Segmenta seus usuários por terem conectado seu app ao X (anteriormente Twitter).
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: Segmenta seus usuários por quantos seguidores no X (anteriormente Twitter) eles têm.
    tags:
      - Social activity
  - name: Phone Number
    description: "Segmenta seus usuários pelo campo de número de telefone formatado em E.164.<br><br> Quando um número de telefone é enviado para a Braze, a Braze tenta convertê-lo para o <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">formato e.164</a> que é usado para enviar através dos canais SMS e WhatsApp. O processo de conversão pode falhar se o número não estiver formatado corretamente, resultando no perfil do usuário ter um número de telefone não formatado, mas não um número de telefone de envio. Este filtro de segmento retorna usuários pelo seu número de telefone formatado em e.164 (quando disponível).<br><br>Casos de uso:<br> - Use este filtro para entender o tamanho do público-alvo mais preciso ao enviar mensagens SMS ou WhatsApp.  <br>- Use expressões regulares (regex) com este filtro para segmentar por números de telefone com um código de país específico. <br>- Use este filtro para segmentar usuários por números de telefone que falharam no processo de conversão e.164."
    tags:
      - Other Filters
---