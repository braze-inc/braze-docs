---
page_order: 2
nav_title: Filtros de segmentação
article_title: Filtros de Segmentação
layout: glossary_page
glossary_top_header: "Filtros de Segmentação"
glossary_top_text: "O Braze SDK oferece um poderoso arsenal de filtros para segmentar e direcionar seus usuários com base em características e atribuições específicas. Você pode pesquisar ou restringir esses filtros por categoria de filtro.<br><br>Para saber mais sobre os diferentes tipos de dados de atributos personalizados que podem ser usados para segmentar usuários, consulte <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">Tipos de dados de atributos personalizados</a>."

page_type: glossary
tool: Segments
description: "Este glossário lista os filtros disponíveis para segmentar e direcionar seus usuários."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Inscrição por segmento ou CSV
  - name: Atributo personalizado
  - name: Eventos personalizados
  - name: Sessões
  - name: Redirecionamento
  - name: Comportamento de inscrição em canal
  - name: Comportamento de compra
  - name: e-commerce
  - name: Atributos demográficos
  - name: App
  - name: Desinstalar
  - name: Dispositivos
  - name: Local
  - name: Inscrição em coorte
  - name: Atribuição da instalação
  - name: Inteligência e previsões
  - name: Atividades de redes sociais
  - name: Outros filtros

glossaries:
  - name: Inscrição em segmento
    description: "Permite filtrar com base na associação de segmento em qualquer lugar onde os filtros são usados (como segmentos, campanhas e outros) e segmentar vários segmentos diferentes dentro de uma campanha. <br><br>Observe que os segmentos que já estão usando esse filtro não podem ser incluídos ou aninhados em outros segmentos, pois isso pode criar um ciclo em que o Segmento A inclui o Segmento B, que, por sua vez, tenta incluir o Segmento A novamente. Se isso acontecesse, o segmento continuaria fazendo referência a si mesmo, tornando impossível calcular quem realmente pertence a ele. Além disso, o aninhamento de segmentos como esse aumenta a complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que está tentando incluir usando os mesmos filtros."
    tags:
      - Segment or CSV membership
  - name: Extensões de segmento da Braze
    description: "Depois de criar uma extensão de segmento no dashboard do Braze, você pode escolher incluir/excluir essas extensões no seu segmento."
    tags:
      - Segment or CSV membership
  - name: Atualizados/importados via CSV
    description: Segmenta seus usuários com base em se eles faziam parte de um fazer upload de CSV ou não.
    tags:
      - Segment or CSV membership
  - name: Atributos personalizados
    description: "Determina se um usuário corresponde ou não a um valor de atributo registrado personalizado. <br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom attribute
  - name: Criação às
    description: "Segmenta os usuários de acordo com a data de criação do perfil de usuário. Se um usuário tiver sido adicionado por CSV ou API, esse filtro refletirá a data em que ele foi adicionado. Se o usuário não for adicionado por CSV ou API e tiver sua primeira sessão rastreada pelo SDK, esse filtro refletirá a data dessa primeira sessão."
    tags:
      - Other Filters
  - name: Atributos personalizados aninhados
    description: "Atributos que são as propriedades de atributos personalizados.<br><br>Ao filtrar um atributo personalizado de tempo aninhado, você pode escolher filtrar com base em \"Dia do Ano\" ou \"Hora\". \"Day of Year\" verifica apenas o mês e o dia para comparação. \"Time\" compara o registro de data e hora completo, incluindo o ano."
    tags:
      - Custom attribute
  - name: Dia do evento recorrente
    description: "Este filtro analisa o mês e o dia do atributo personalizado com o tipo de dado \"data\", mas não analisa o ano. Este filtro é útil para eventos anuais.<br><br>Fuso horário:<br>Esse filtro se ajusta a qualquer fuso horário em que o usuário esteja, desde que a mensagem seja enviada usando a opção de agendamento de fuso local; caso contrário, esse filtro usa o fuso horário da sua empresa."
    tags:
      - Custom attribute
  - name: Evento personalizado
    description: "Determina se um usuário realizou ou não um evento especialmente registrado.<br><br> Exemplo:<br>Atividade concluída com a propriedade activity_name.<br><br>Fuso horário:<br>UTC - Dia do calendário = 1 dia do calendário analisa 24-48 horas do histórico do usuário"
    tags:
      - Custom events
  - name: Realizou pela primeira vez um evento personalizado
    description: "Determina o primeiro horário em que um usuário realizou um evento especialmente registrado. (período de 24 horas) <br><br>Exemplo:<br> Primeiro Carrinho Abandonado Menos de 1 dia atrás<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom events
  - name: Realizou pela última vez um evento personalizado 
    description: "Determina a última vez que um usuário realizou um evento especialmente registrado. Esse filtro aceita decimais, como 0,25 horas. (período de 24 horas) <br><br>Exemplo:<br> Último Carrinho Abandonado Há menos de 1 dia<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Custom events
  - name: Evento personalizado X em Y dias
    description: "Determina se um usuário realizou ou não um evento especialmente registrado entre 0 e 50 vezes nos últimos dias de calendário especificados entre 1 e 30. (Dia do calendário = 1 dia do calendário considera 24-48 horas do histórico do usuário)<br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento de X-em-Y aqui.</a> <br><br>Exemplo:<br>Carrinho abandonado exatamente 0 vezes no último 1 dia de calendário<br><br>Fuso horário:<br>UTC - Para levar em conta todos os fusos horários, 1 dia do calendário analisa 24-48 horas do histórico do usuário, dependendo do horário em que o segmento é avaliado; para 2 dias do calendário, analisa 48-72 horas do histórico do usuário e assim por diante."
    tags:
      - Custom events
  - name: Propriedade do evento personalizado X em Y dias
    description: "Determina se um usuário realizou ou não um evento especialmente registrado em relação a uma propriedade específica entre 0 e 50 vezes nos últimos dias de calendário especificados entre 1 e 30. (Dia do calendário = 1 dia do calendário considera 24-48 horas do histórico do usuário)<br><a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a> <br><br>Exemplo:<br> Adicionado aos Favoritos com a propriedade \"event_name\" exatamente 0 vezes no último 1 dia de calendário<br><br>Fuso horário:<br>UTC - Para levar em conta todos os fusos horários, 1 dia do calendário analisa 24-48 horas do histórico do usuário, dependendo do horário em que o segmento é avaliado; para 2 dias do calendário, analisa 48-72 horas do histórico do usuário e assim por diante."
    tags:
      - Custom events
  - name: Endereço de e-mail 
    description: "Permite designar os destinatários da sua campanha por endereços de e-mail individuais para teste. Isso também pode ser usado para enviar e-mails de transação a todos os seus usuários (incluindo os que cancelaram a inscrição) usando a especificação \"Endereço de e-mail não está em branco\" no filtro, para que você possa maximizar a entrega de e-mails independentemente do status de aceitação. <br><br>Esse filtro verifica apenas se os perfis de usuário têm um endereço de e-mail, enquanto o filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">E-mail disponível</a> verifica critérios adicionais."
    tags:
      - Other Filters
  - name: ID de usuário externo
    description: Permite designar os destinatários da sua campanha por IDs de usuário individuais para teste.
    tags:
      - Other Filters
  - name: "Número de buckets aleatórios"
    description: Segmenta seus usuários por um número atribuído aleatoriamente (0 a 9999 inclusive). Ele pode ativar a criação de segmentos uniformemente distribuídos de usuários verdadeiramente aleatórios para testes A/B e multivariantes.
    tags:
      - Other Filters
  - name: Contagem de sessões
    description: Segmenta seus usuários pelo número de sessões que eles tiveram em qualquer um de seus aplicativos dentro do seu espaço de trabalho.
    tags:
      - Sessions
  - name: Contagem de sessões para o app
    description: Segmenta seus usuários pelo número de sessões que tiveram em um app específico e designado.
    tags:
      - Sessions
  - name: X Sessões Nos Últimos Y Dias
    description: "Segmenta seus usuários pelo número de sessões (entre 0 e 50) que eles tiveram em seu app nos últimos dias de calendário especificados entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Sessions
  - name: Usou o app pela primeira vez
    description: "Segmenta seus usuários pelo horário mais antigo registrado em que abriram seu app. <em>Isso captura a primeira sessão que eles têm usando uma versão do seu app com a integração do SDK do Braze.</em> (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Usou um app específico pela primeira vez
    description: "Segmenta seus usuários pelo horário mais antigo registrado em que abriram qualquer um de seus aplicativos dentro do seu espaço de trabalho. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Último uso do app
    description: "Segmenta seus usuários pelo horário mais recente que eles abriram seu app. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Último uso de um app específico
    description: "Segmenta seus usuários pelo horário mais recente que eles abriram um app específico e designado. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Sessions
  - name: Duração média das sessões
    description: Segmenta seus usuários pela duração mediana de suas sessões no seu app.
    tags:
      - Sessions
  - name: Recebeu mensagem de campanha
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica. Esse filtro captura apenas os usuários que receberam explicitamente a mensagem, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign (Mensagem recebida da campanha) ou Canva with Tag (Tela com tag</a>).<br><br> Para cartões de conteúdo, banners e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Recebeu variante de campanha
    description: "Segmenta seus usuários por qual variante de uma campanha multivariante eles receberam. Esse filtro captura apenas os usuários que receberam explicitamente a mensagem, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign (Mensagem recebida da campanha) ou Canva with Tag (Tela com tag</a>).<br><br> Para cartões de conteúdo, banners e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Recebeu mensagem de uma etapa de um canva
    description: "Segmenta seus usuários por terem ou não recebido um componente específico da canva. Esse filtro captura apenas os usuários que receberam explicitamente a mensagem, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas. Para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign (Mensagem recebida da campanha) ou Canva with Tag (Tela com tag</a>).<br><br> Para Cartões de Conteúdo e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue).<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Última mensagem recebida de uma etapa de canva específica
    description: "Segmenta seus usuários por quando eles receberam um componente específico da canva. Esse filtro captura apenas os usuários que receberam explicitamente a mensagem, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas; para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag</a>. Esse filtro não considera quando os usuários receberam outros componentes do Canva."
    tags:
      - Retargeting
  - name: Última mensagem recebida de uma campanha específica
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica. Esse filtro captura apenas os usuários que receberam explicitamente a mensagem, e não outros usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas; para capturar usuários duplicados, use <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag</a>. Esse filtro não considera quando os usuários receberam outras campanhas."
    tags:
      - Retargeting
  - name: Recebeu mensagem de campanha ou canva com tag
    description: "Segmenta seus usuários por terem ou não recebido uma campanha específica ou canva com uma tag específica. Ao contrário de \"Received Message from Campaign\" e \"Received Message from Canvas Step\", esse filtro captura todos os usuários com o mesmo e-mail ou número de telefone que receberam mensagens duplicadas.<br><br> Para cartões de conteúdo, banners (somente campanhas) e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue). Quando vários usuários compartilham o mesmo e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Recebeu mensagem de campanha ou canva com tag pela última vez
    description: Segmenta seus usuários por quando eles receberam uma campanha específica ou canva com uma tag específica. Esse filtro não considera quando os usuários receberam outras campanhas ou Canvas. (período de 24 horas)
    tags:
      - Retargeting
  - name: Nunca recebeu mensagem de campanha ou etapa do canva
    description: Segmenta seus usuários por terem ou não recebido qualquer campanha ou componente de canva.
    tags:
      - Retargeting
  - name: Último recebimento de e-mail
    description: "Segmenta seus usuários pela última vez que eles receberam uma de suas mensagens de e-mail. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Último push recebido
    description: "Segmenta seus usuários pela última vez que receberam uma de suas notificações por push. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Última impressão da mensagem no app
    description: Segmenta seus usuários pela última vez que visualizaram uma mensagem no app.
    tags:
      - Retargeting
  - name: Último SMS recebido
    description: "Segmenta seus usuários pelo tempo em que a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Último webhook recebido
    description: "Segmenta seus usuários pelo último envio de webhook da Braze para esse usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Último recebimento por WhatsApp
    description: "Segmenta seus usuários pela última vez que receberam uma mensagem do WhatsApp. Isso é quando a solicitação de API da última mensagem é enviada para o WhatsApp, não quando a mensagem é entregue no dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Atividades ao vivo Push to Start registradas para app
    description: Segmenta seus usuários por estarem registrados para iniciar uma Live Activity por meio de notificações por push do iOS para um app específico.
    tags:
      - Devices
  - name: Campanha clicada/aberta
    description: "Filtrar por interação com uma campanha específica. Para o envio de mensagens de e-mail, o evento de abertura inclui tanto as aberturas por máquina quanto as que não são por máquina.<br><br> Para e-mail, isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Os cliques em links de cancelamento de inscrição e centrais de preferências não contam para esse filtro. Se vários usuários compartilharem o mesmo e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha."
    tags:
      - Retargeting
  - name: Campanhas ou canvas clicados/abertos com tag
    description: "Filtrar por interação com uma campanha específica que possui uma tag específica. Para o envio de mensagens de e-mail, o evento de abertura inclui tanto as aberturas por máquina quanto as que não são por máquina.<br><br> Para e-mails, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Se vários usuários compartilharem o mesmo e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>- Quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha ou etapa do canva com tag."
    tags:
      - Retargeting
  - name: Clicou/abriu uma etapa
    description: "Filtrar por interação com um componente específico da canva. Para o envio de mensagens de e-mail, o evento de abertura inclui tanto as aberturas por máquina quanto as que não são por máquina.<br><br>Para e-mails, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\".<br><br>Para SMS, uma interação é definida como:<br>O usuário enviou por último uma resposta SMS correspondente a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com este número de telefone. A campanha deve ter sido recebida nas últimas quatro horas. <br>O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, a partir de uma determinada etapa do canva."
    tags:
      - Retargeting
  - name: Alias clicado na campanha
    description: "Filtre seus usuários por terem clicado em um alias específico em uma campanha específica. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Alias clicado na etapa do canva
    description: "Filtre seus usuários por terem clicado em um alias específico em uma canva específica. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Apelido clicado em qualquer campanha ou etapa do canva
    description: "Filtre seus usuários por terem clicado em um alias específico em qualquer campanha ou canva. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original mudar seu endereço de e-mail após a mensagem ser enviada e antes da abertura ou clique, a abertura ou clique será aplicado a todos os usuários restantes com esse endereço de e-mail em vez do usuário original."
    tags:
      - Retargeting
  - name: Hard bounce
    description: Segmente seus usuários por saber se o endereço de e-mail deles teve um hard bounce (como quando o endereço de e-mail é inválido).
    tags:
      - Retargeting
  - name: Soft bounce
    description: "Segmente seus usuários de acordo com o número de soft bounces X vezes em Y dias. Os filtros do Segment só podem olhar para trás 30 dias, mas você pode olhar mais para trás com as extensões do Segment.<br><br>Esse filtro funciona de forma diferente de um evento de soft bounce no Currents. O filtro de segmento Soft Bounce conta um soft bounce se não houver uma entrega bem-sucedida durante o período de tentativa de 72 horas. No Currents, cada tentativa malsucedida é enviada como um evento de soft bounce." 
    tags:
      - Retargeting
  - name: Marcou sua mensagem como spam
    description: Segmenta seus usuários por se eles marcaram ou não suas mensagens como spam.
    tags:
      - Retargeting
  - name: Número de telefone inválido 
    description: Segmenta seus usuários por se o número de telefone deles é inválido ou não.
    tags:
      - Retargeting
  - name: Última categoria de palavra-chave de SMS de inbound específica enviada
    description: Segmenta seus usuários pelo momento em que enviaram um SMS pela última vez para um grupo de inscrições específico dentro de uma categoria de palavra-chave específica. 
    tags:
      - Retargeting
  - name: Convertidos de uma campanha
    description: Segmenta seus usuários por terem ou não convertido em uma campanha específica. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: Convertidos de um canva
    description: Segmenta seus usuários por terem ou não convertido em uma canva específica. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: No grupo de controle da campanha
    description: Segmenta seus usuários por estarem ou não no grupo de controle para uma campanha multivariante específica.
    tags:
      - Retargeting
  - name: No grupo de controle do canva
    description: "Segmenta seus usuários por estarem ou não no grupo de controle para um canva específico. Este filtro avalia apenas os usuários que entraram na canva.<br><br>Por exemplo, se você filtrar os usuários que não estão no grupo de controle de um Canvas, receberá todos os usuários que entraram no Canvas, mas não estão no grupo de controle."
    tags:
      - Retargeting
  - name: Ultima inscrição em qualquer grupo de controle
    description: "Segmenta seus usuários pela última vez que eles caíram no grupo de controle em uma campanha. <br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Entrou na variação do canva
    description: "Segmenta seus usuários por terem ou não entrado em uma jornada de variação de um canva específico. Este filtro avalia todos os usuários.<br><br>Por exemplo, se você filtrar os usuários que não entraram em um grupo de controle de variação do Canvas, receberá todos os usuários que não estão no grupo de controle, independentemente de terem entrado no Canvas."
    tags:
      - Retargeting
  - name: Último recebimento de qualquer mensagem
    description: "Segmenta seus usuários determinando a última mensagem que foi recebida. (período de 24 horas)<br><br> Para cartões de conteúdo, banners e mensagens no app, é quando um usuário registrou uma impressão pela última vez, não quando o cartão ou a mensagem no app foi enviada pela última vez.<br><br>Para push e webhooks, isso é quando qualquer mensagem foi enviada ao usuário.<br><br> Para o WhatsApp, isso é quando a última solicitação de API de mensagem foi enviada para o WhatsApp, não quando a mensagem foi entregue ao dispositivo do usuário. <br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue). Quando vários usuários compartilham o mesmo e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário.<br><br>Exemplo:<br>Última mensagem recebida há menos de 1 dia = menos de 24 horas atrás<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Última interação com mensagem
    description: "Segmenta seus usuários pela última vez em que clicaram ou abriram um de seus canais de envio de mensagens (banners, cartão de conteúdo, e-mail, no app, SMS, push, WhatsApp). Para o envio de mensagens de e-mail, o evento de abertura inclui tanto as aberturas por máquina quanto as que não são por máquina. (período de 24 horas)<br><br>Para e-mails, isso é quando uma solicitação de e-mail é enviada ao prestador de serviço de e-mail (independentemente se ela realmente é entregue). Isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Quando vários usuários compartilham o mesmo e-mail:<br>- No envio inicial, apenas o perfil do usuário específico é atualizado. <br>- Quando o e-mail é entregue, ou se o usuário abre o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecem ter recebido a mensagem.<br><br>Para SMS, isso é quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem que tem o rastreamento de cliques do usuário ativado.<br><br>Fuso horário:<br>Fuso Horário da Empresa"
    tags:
      - Retargeting
  - name: Cartão clicado 
    description: "Segmenta seus usuários por terem ou não clicado em um cartão de conteúdo específico. Este filtro está disponível como um subfiltro de \"Campanha clicada/aberta\", \"Campanha clicada/aberta ou Canva com Tag\" e \"Etapa clicada/aberta\"."
    tags:
      - Retargeting
  - name: Feature Flags
    description: "O segmento de seus usuários que têm um <a href=\"/docs/developer_guide/feature_flags/\">Feature Flag</a> específico atualmente ativado."
    tags:
      - Retargeting
  - name: Grupo de inscrições
    description: "Segmenta seus usuários por seu grupo de inscrições para e-mail, SMS/MMS ou WhatsApp. Os grupos arquivados não são exibidos e não podem ser usados."
    tags:
      - Channel subscription behavior
  - name: E-mail disponível
    description: "Segmenta seus usuários de acordo com o fato de eles terem um endereço de e-mail válido e de estarem inscritos ou terem aceitado o envio de e-mail. Esse filtro verifica três critérios: se o usuário cancelou a inscrição de e-mails, se o Braze recebeu um hard bounce e se o e-mail foi marcado como spam. Se algum desses critérios for atendido ou se não houver um e-mail para um usuário, ele não será incluído.<br><br>Observe que, se você enviar uma mensagem de transação, os usuários cujo \"E-mail disponível\" seja <code>false</code> não será incluído no cálculo do público, mas ainda poderá receber uma mensagem. No entanto, o cálculo do público inclui apenas usuários inscritos ou com aceitação. <br><br>Para e-mails em que o status de aceitação é importante, sugerimos usar o filtro \"E-mail disponível\" em vez do filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">de endereço de e-mail</a>; os critérios adicionais podem ajudá-lo a direcionar os usuários que realmente desejam ver suas mensagens."
    tags:
      - Channel subscription behavior
  - name: Data de aceitação de recebimento de e-mails
    description: Segmenta seus usuários pela data em que optaram por e-mail.
    tags:
      - Channel subscription behavior
  - name: Status de inscrição no e-mail
    description: Segmenta seus usuários pelo status de inscrição para e-mail.
    tags:
      - Channel subscription behavior
  - name: Data de cancelamento de inscrição no e-mail 
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de futuros e-mails.
    tags:
      - Channel subscription behavior
  - name: Notificações por push em primeiro plano ativadas
    description: "Segmenta seus usuários que têm autorização provisória de push ou estão habilitados para push em primeiro plano. Especificamente, esta contagem inclui:<br>1. Usuários do iOS que estão provisoriamente autorizados para push. <br>2. Usuários que têm a capacitação push em primeiro plano ativada e cujo status de inscrição push não está cancelado, para qualquer um dos seus apps. Para esses usuários, essa contagem inclui apenas push em primeiro plano.<br><br>A capacitação de push em primeiro plano não inclui usuários que cancelaram a inscrição. <br><br>Depois de segmentar com esse filtro, você pode ver um detalhamento de quem está nesse segmento para Android, iOS e Web no painel inferior, chamado <em>Reachable Users (Usuários alcançáveis</em>)."
    tags:
      - Channel subscription behavior
  - name: Push em primeiro plano ativado para o aplicativo
    description: Segmentos por se os usuários têm push ativado para seu app em seu dispositivo. Usuários que têm a capacitação push em primeiro plano ativada para um aplicativo. Isso não leva em conta o status da inscrição push. Esta contagem inclui usuários que autorizaram provisoriamente tokens de push em primeiro e segundo plano.
    tags:
      - Channel subscription behavior
  - name: Ativação do push em primeiro plano ou segundo plano
    description: Segmenta de acordo com o fato de os usuários terem um token por push e não terem cancelado a inscrição. Usuários que têm o push em segundo ou primeiro plano ativado para qualquer um dos seus apps.
    tags:
      - Channel subscription behavior
  - name: Data de aceitação de recebimento de push
    description: Segmenta seus usuários pela data em que eles aceitaram o recebimento de push.
    tags:
      - Channel subscription behavior
  - name: Status de inscrição para push
    description: "Segmenta seus usuários pelo <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">status de inscrição</a> para push."
    tags:
      - Channel subscription behavior
  - name: Data de cancelamento de recebimento de push
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de futuras notificações por push.
    tags:
      - Channel subscription behavior
  - name: Produto comprado
    description: Segmenta seus usuários por produtos comprados no seu app.
    tags:
      - Purchase behavior
  - name: Total de compras
    description: Segmenta seus usuários pelo número de compras que fizeram no seu app.
    tags:
      - Purchase behavior
  - name: X produtos comprados em Y dias
    description: Filtrar usuários pelo número de vezes que um produto específico foi comprado.
    tags:
      - Purchase behavior
  - name: X compras nos últimos Y dias
    description: "Segmenta seus usuários pelo número de vezes (entre 0 e 50) que eles fizeram uma compra no último número especificado de dias corridos entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: Propriedade de compra X em Y dias
    description: "Segmenta seus usuários pelo número de vezes que uma compra foi feita em relação a uma certa propriedade de compra nos últimos dias de calendário especificados entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: Primeira compra feita
    description: Segmenta seus usuários pelo horário mais cedo em que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: Primeira Compra Para App
    description: Segmenta seus usuários pelo horário mais cedo em que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: Última compra feita
    description: Filtrar usuários pela última vez que fizeram uma compra.
    tags: 
      - Purchase behavior
  - name: Última compra de produto
    description: Filtre os usuários pela última vez que compraram um produto específico.
    tags:
      - Purchase behavior
  - name: Dinheiro gasto
    description: Segmenta seus usuários pela quantidade de dinheiro que gastaram em seu app.
    tags:
      - Purchase behavior
  - name: X Dinheiro Gasto em Y Dias
    description: "Segmenta seus usuários pela quantidade de dinheiro que eles gastaram no seu app nos últimos dias de calendário especificados entre 1 e 30. Esse valor inclui apenas a soma das últimas 50 compras. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-em-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: Último pedido realizado (últimos 730 dias)
    description: "Segmenta os usuários de acordo com a última vez que fizeram um pedido, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para o pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados por esse filtro uma vez por dia, e a janela máxima de retrospectiva é os últimos 2 anos.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Contagem total de pedidos (últimos 730 dias)
    description: "Segmenta seus usuários pela contagem total de pedidos de um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico recomendado</a> para o pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para pedido cancelado. Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Total de pedidos
    description: "Segmenta seus usuários pela contagem total de pedidos de um usuário ao longo de sua vida útil, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico recomendado</a> para o pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para pedido cancelado. Os usuários são avaliados por esse filtro em tempo real.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Contagem total de pedidos cancelados (últimos 730 dias)
    description: "Segmenta seus usuários pela contagem total de pedidos que um usuário cancelou nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para o pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Valor do tempo de vida do cliente (últimos 730 dias)
    description: "Segmenta seus usuários de acordo com a receita total que se espera que um usuário gere ao longo do histórico de compras com sua marca. O cálculo considera os últimos 730 dias e pega o valor médio do pedido (AOV), multiplica-o pelo número total de pedidos feitos e, em seguida, considera a duração da compra ativa do usuário (o intervalo de tempo entre o primeiro e o mais recente pedido). Esse filtro usa dados rastreados em <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">eventos recomendados</a>de comércio eletrônico (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Valor total de reembolsos (últimos 730 dias)
    description: "Segmenta seus usuários pelo valor dos reembolsos concedidos a um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para o pedido reembolsado (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Total de reembolsos
    description: "Segmenta seus usuários pelo valor total dos reembolsos concedidos a um usuário ao longo de seu tempo de vida, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado</a> pelo <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico</a> para o pedido reembolsado (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados por esse filtro em tempo real.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Receita total (últimos 730 dias)
    description: "Segmenta seus usuários pela receita total gerada pelos pedidos de um usuário nos últimos 2 anos, calculada com base na subtração da receita associada ao <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento de comércio eletrônico recomendado</a> para pedido reembolsado da receita associada ao evento de comércio eletrônico para pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Total de receitas
    description: "Segmenta seus usuários pela receita total gerada pelos pedidos de um usuário ao longo de sua vida útil, calculada com base na subtração da receita associada ao evento de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico recomendado</a> para pedido reembolsado da receita associada ao evento de comércio eletrônico para pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados por esse filtro em tempo real.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: Valor médio do pedido (últimos 730 dias)
    description: "Segmenta seus usuários pelo valor médio dos pedidos de um usuário nos últimos 2 anos, com base no <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento</a> de <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comércio eletrônico recomendado</a> para o pedido feito (os espaços de trabalho que não rastreiam eventos de comércio eletrônico não têm dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Esse filtro está na versão beta. Entre em contato com seu gerente de conta Braze se estiver interessado em usar esse filtro."
    tags:
      - eCommerce
  - name: País
    description: Segmenta seus usuários pelo último país local indicado.
    tags:
      - Demographic attributes
  - name: Cidade
    description: Segmenta seus usuários pela última cidade local indicada.
    tags:
      - Demographic attributes
  - name: Idioma
    description: Segmenta seus usuários pelo idioma preferido.
    tags:
      - Demographic attributes
  - name: Idade
    description: "Segmenta seus usuários pela idade, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Data de nascimento
    description: "Segmenta seus usuários pelo aniversário, conforme indicado no seu app. <br> Os usuários com aniversário no dia 29 de fevereiro são incluídos em segmentos que incluem o dia 1º de março.<br><br>Para direcionar aniversários de dezembro ou janeiro, insira a lógica do filtro apenas dentro do período de 12 meses do ano que você está direcionando. Em outras palavras, não insira lógica que olhe para trás para o dezembro do ano anterior ou para frente para o janeiro do próximo ano. Por exemplo, para direcionar aniversários em dezembro, você pode filtrar por \"em 31 de dezembro\", \"antes de 31 de dezembro\" ou \"depois de 30 de novembro\"."
    tags:
      - Demographic attributes
  - name: Gênero
    description: "Segmenta seus usuários por gênero, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Número de telefone não formatado
    description: "Segmenta seus usuários pelo número de telefone não formatado. Não inclui parênteses, traços ou outros símbolos."
    tags:
      - Demographic attributes
  - name: Nome
    description: "Segmenta seus usuários pelo nome, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Sobrenome
    description: "Segmenta seus usuários pelo sobrenome, conforme indicado no seu app."
    tags:
      - Demographic attributes
  - name: Tem o app
    description: "Segmentos por saber se um usuário já instalou seu app ou não. Isso inclui usuários que atualmente têm seu app instalado e aqueles que o desinstalaram no passado. Isso geralmente requer que os usuários abram o app (iniciem uma sessão) para serem incluídos neste filtro. No entanto, há algumas exceções, como se um usuário foi importado para o Braze e associado manualmente ao seu app."
    tags:
      - App
  - name: Nome da versão mais recente do app
    description: "Segmentos pelo nome recente do app do usuário.<br><br>Ao usar \"menor que\" ou \"menor que ou igual a\", se a versão principal do app não existir, esse filtro retornará `verdadeiro` porque o usuário é mais antigo que a versão do app. Isso significa que, se a última versão do app principal do usuário não existir, ela corresponderá automaticamente ao filtro."
    tags:
      - App 
  - name: Número da versão mais recente do app
    description: "Segmentos pelo número da versão recente do app do usuário.<br><br>Ao usar \"menor que\" ou \"menor que ou igual a\", se a versão principal do app não existir, esse filtro retornará `verdadeiro` porque o usuário é mais antigo que a versão do app. Isso significa que, se a última versão do app principal do usuário não existir, ela corresponderá automaticamente ao filtro.<br><br>Pode levar algum tempo para que as versões atuais do app sejam preenchidas. A versão do aplicativo no perfil do usuário é atualizada quando as informações são capturadas pelo SDK, que se baseia em quando os usuários abrem seus apps. Se o usuário não abrir o app, a versão atual não será atualizada. Esses filtros também não serão aplicados retroativamente. É bom usar \"maior que\" ou \"igual\" para versões atuais e futuras, mas o uso de filtros de versões anteriores pode causar comportamentos inesperados."
    tags:
      - App 
  - name: Desinstalou
    description: Segmenta seus usuários por terem desinstalado seu app e não o reinstalado.
    tags:
      - Uninstall 
  - name: Operadora do dispositivo
    description: Segmenta seus usuários pelo dispositivo operadora.
    tags:
      - Devices
  - name: Contagem de dispositivos
    description: Segmenta seus usuários pelo número de dispositivos em que usaram seu app.
    tags:
      - Devices
  - name: Modelo do dispositivo
    description: Segmenta seus usuários pela versão do modelo do celular.
    tags:
      - Devices
  - name: SO do dispositivo
    description: "Segmenta seus usuários que possuem um ou mais dispositivos com o sistema operacional especificado. Para segmentar os usuários por uma variedade de sistemas operacionais, use o filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">Device OS Version Number</a>."
    tags:
      - Devices
  - name: Versão do sistema operacional do dispositivo
    description: "Segmenta seus usuários que têm um ou mais dispositivos com uma versão de sistema operacional que está dentro de um intervalo especificado. Por exemplo, você pode direcionar os usuários que têm uma versão do sistema operacional iOS superior ou igual a 26.0."
    tags:
      - Devices
  - name: Localidade mais recente do dispositivo
    description: "Segmenta seus usuários pela <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">informação de localidade</a> do dispositivo mais recentemente usado."
    tags:
      - Devices      
  - name: Modelo de smartwatch mais recente
    description: Segmenta seus usuários pelo modelo de smartwatch mais recente.
    tags:
      - Devices    
  - name: Autorização provisória no iOS
    description: Permite encontrar usuários que estão provisoriamente autorizados no iOS 12 para um determinado app.
    tags:
      - Devices   
  - name: Navegador web
    description: Segmenta seus usuários pelo navegador da web que eles usam para acessar seu site.
    tags:
      - Devices
  - name: IDFA do dispositivo
    description: Permite designar os destinatários da sua campanha por IDFA para teste.
    tags:
      - Advertising use cases
  - name: IDFV do dispositivo
    description: Permite designar os destinatários da sua campanha por IDFV para teste.
    tags:
      - Advertising use cases 
  - name: ID de publicidade do Google do dispositivo
    description: Segmenta seus usuários pelo ID de anúncio do Google.
    tags:
      - Advertising use cases
  - name: ID de publicidade do Roku do dispositivo
    description: Segmenta seus usuários pelo ID de anúncio do Roku.
    tags:
      - Advertising use cases
  - name: ID de publicidade do Windows do dispositivo
    description: Segmenta seus usuários pelo ID de anúncio do Windows.
    tags:
      - Advertising use cases  
  - name: Rastreamento de anúncios ativado
    description: "Permite que você filtre com base em se seus usuários optaram pelo rastreamento de anúncios. O rastreamento de anúncios está relacionado ao IDFA ou \"identificador para anunciantes\" atribuído a todos os dispositivos iOS pela Apple, que pode ser configurado por SDKs. Este identificador permite que os anunciantes rastreiem os usuários e lhes sirvam anúncios direcionados."
    tags:
      - Advertising use cases
  - name: Local mais recente
    description: Segmenta seus usuários pela última localidade registrada em que usaram seu app.
    tags:
      - Location
  - name: Local disponível
    description: "Segmenta seus usuários por terem ou não relatado suas localizações. Para usar este filtro, seu app precisa ter <a href=\"/docs/search/?query=location%20tracking\">monitoramento de localização integrado.</a>"
    tags:
      - Location
  - name: Coortes de amplitude
    description: Clientes que usam Amplitude podem complementar seus segmentos escolhendo e importando suas coortes no Amplitude.
    tags:
      - Cohort membership
  - name: Coortes de Census
    description: Clientes que usam Census podem complementar seus segmentos escolhendo e importando suas coortes no Census.
    tags:
      - Cohort membership
  - name: Coortes do Heap
    description: Clientes que usam Heap podem complementar seus segmentos escolhendo e importando suas coortes no Heap.
    tags:
      - Cohort membership
  - name: Coortes do Hightouch
    description: Clientes que usam Hightouch podem complementar seus segmentos escolhendo e importando suas coortes no Hightouch.
    tags:
      - Cohort membership
  - name: Coortes do Kubit
    description: Clientes que usam Kubit podem complementar seus segmentos escolhendo e importando suas coortes no Kubit.
    tags:
      - Cohort membership
  - name: Coortes do Mixpanel
    description: Clientes que usam Mixpanel podem complementar seus segmentos escolhendo e importando suas coortes no Mixpanel.
    tags:
      - Cohort membership
  - name: Coortes de segmento
    description: Clientes que usam o Segment podem complementar seus segmentos escolhendo e importando suas coortes no Segment.
    tags:
      - Cohort membership
  - name: Coortes do Tinyclues
    description: Clientes que usam Tinyclues podem complementar seus segmentos escolhendo e importando suas coortes no Tinyclues.
    tags:
      - Cohort membership
  - name: Instalação por anúncio
    description: Segmenta seus usuários pelo anúncio ao qual a instalação deles foi atribuída.
    tags:
      - User Attributes
  - name: Instalação por grupo de anúncio
    description: Segmenta seus usuários pelo grupo de anúncios ao qual a instalação deles foi atribuída.
    tags:
      - Install Attribution
  - name: Instalação por campanha
    description: Segmenta seus usuários pela campanha publicitária à qual sua instalação foi atribuída.
    tags:
      - Install Attribution
  - name: Instalação por origem
    description: Segmenta seus usuários pela fonte à qual a instalação deles foi atribuída.
    tags:
      - Install Attribution
  - name: Categoria de risco de churn
    description:  Segmenta seus usuários por categoria de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Pontuação de risco de churn
    description: Segmenta seus usuários pelo score de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Categoria de probabilidade do evento
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Pontuação de probabilidade do evento
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Canal inteligente
    description: Segmente seus usuários pelo canal mais ativo nos últimos três meses.
    tags:
      - Intelligence and predictive
  - name: Probabilidade de abrir mensagens
    description: "Filtra seus usuários com base na probabilidade de abrir uma mensagem em um canal especificado em uma escala de 0-100%. Usuários sem dados suficientes para medir a probabilidade de um canal podem ser selecionados usando \"está em branco.\"<br><br>Para e-mails, as aberturas de máquina são excluídas do cálculo de probabilidade."
    tags:
      - Intelligence and predictive
  - name: Número de amigos do Facebook que usam o app
    description: Segmenta seus usuários pelo número de amigos no Facebook que eles têm que usam o mesmo app.
    tags:
      - Social activity
  - name: Conectou o Facebook
    description: Segmenta seus usuários por terem conectado seu app ao Facebook.
    tags:
      - Social activity
  - name: Conectou o Twitter
    description: Segmenta seus usuários por terem conectado seu app ao X (anteriormente Twitter).
    tags:
      - Social activity
  - name: Número de seguidores do Twitter
    description: Segmenta seus usuários por quantos seguidores no X (anteriormente Twitter) eles têm.
    tags:
      - Social activity
  - name: Número de telefone
    description: "Segmenta seus usuários pelo campo de número de telefone formatado em E.164.<br><br> Quando um número de telefone é enviado para Braze, Braze tenta forçá-lo para o <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">formato e.164</a> que é usado para enviar através dos canais SMS e WhatsApp. O processo de coerção pode falhar se o número não estiver formatado corretamente, o que faz com que o perfil do usuário tenha um número de telefone não formatado, mas não um número de telefone de envio. Esse filtro de segmento retorna os usuários pelo número de telefone formatado em e.164 (quando disponível).<br><br>Casos de uso:<br> - Use esse filtro para entender o tamanho do público-alvo mais preciso ao enviar mensagens SMS ou WhatsApp.  <br>Use expressões regulares (regex) com este filtro para segmentar por números de telefone com um código de país específico. <br>Use este filtro para segmentar usuários por números de telefone que falharam no processo de coerção e.164."
    tags:
      - Other filters
---
