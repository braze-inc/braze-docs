---
page_order: 2
nav_title: Filtros de segmentação
article_title: Filtros de segmentação
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "Este glossário lista os filtros disponíveis para segmentar e direcionar seus usuários."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Segmento ou associação CSV
  - name: Atributos personalizados
  - name: Eventos personalizados
  - name: Sessões
  - name: Retargeting
  - name: Comportamento de assinatura de canal
  - name: Comportamento de compra
  - name: Atributos demográficos
  - name: Aplicativo
  - name: Desinstalação
  - name: Dispositivos
  - name: Localização
  - name: Membros da coorte
  - name: Atribuição de instalação
  - name: Inteligência e previsão
  - name: Atividade social
  - name: Outros filtros

glossaries:
  - name: Associação ao segmento
    description: "Permite filtrar com base na associação ao segmento em qualquer lugar em que os filtros sejam usados (como segmentos, campanhas e outros) e direcionar vários segmentos diferentes em uma campanha. <br><br>Observe que os segmentos que já estão usando esse filtro não podem ser incluídos ou aninhados em outros segmentos, pois isso pode criar um ciclo em que o Segmento A inclui o Segmento B, que, por sua vez, tenta incluir o Segmento A novamente. Se isso acontecesse, o segmento continuaria fazendo referência a si mesmo, tornando impossível calcular quem realmente pertence a ele. Além disso, o aninhamento de segmentos como esse aumenta a complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que está tentando incluir usando os mesmos filtros."
    tags:
      - Segment or CSV membership
  - name: Extensões de segmento de brasagem
    description: "Depois de criar uma extensão de segmento no painel do Braze, você pode optar por incluir/excluir essas extensões em seu segmento."
    tags:
      - Segment or CSV membership
  - name: Atualizado/Importado de CSV
    description: Segmenta seus usuários com base no fato de eles terem feito parte de um upload de CSV ou não.
    tags:
      - Segment or CSV membership
  - name: Atributos personalizados
    description: "Determina se um usuário corresponde ou não a um valor de atributo personalizado registrado. <br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Custom attributes
  - name: Criado em
    description: "Segmenta os usuários de acordo com a data de criação do perfil de usuário. Se um usuário tiver sido adicionado por CSV ou API, esse filtro refletirá a data em que ele foi adicionado. Se o usuário não for adicionado por CSV ou API e tiver sua primeira sessão rastreada pelo SDK, esse filtro refletirá a data dessa primeira sessão."
    tags:
      - Other Filters
  - name: Atributos personalizados aninhados
    description: "Atributos que são as propriedades de atributos personalizados.<br><br>Ao filtrar um atributo personalizado de hora aninhado, você pode optar por filtrar com base no \"Dia do ano\" ou na \"Hora\". \"Day of Year\" verificará apenas o mês e o dia para comparação. \"Time\" comparará o registro de data e hora completo, incluindo o ano."
    tags:
      - Custom attributes
  - name: Dia do evento recorrente
    description: "Esse filtro examina o mês e o dia do atributo personalizado com o tipo de dados \"date\", mas não examina o ano. Esse filtro é útil para eventos anuais.<br><br>Fuso horário:<br>Esse filtro se ajusta a qualquer fuso horário em que o usuário esteja, desde que a mensagem seja enviada usando a opção de agendamento de horário local; caso contrário, esse filtro usa o fuso horário da sua empresa."
    tags:
      - Custom attributes
  - name: Evento personalizado
    description: "Determina se um usuário realizou ou não um evento especialmente registrado.<br><br> Exemplo:<br>Atividade concluída com a propriedade activty_name.<br><br>Fuso horário:<br>UTC - Dia do calendário = 1 dia do calendário analisará 24-48 horas do histórico do usuário"
    tags:
      - Custom events
  - name: Primeiro evento personalizado realizado
    description: "Determina a hora mais antiga em que um usuário realizou um evento especialmente registrado. (período de 24 horas) <br><br>Exemplo:<br> Primeiro carrinho abandonado Há menos de 1 dia<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Custom events
  - name: Evento personalizado Last Did 
    description: "Determina a última hora em que um usuário realizou um evento especialmente registrado. Esse filtro aceita decimais, como 0,25 horas. (período de 24 horas) <br><br>Exemplo:<br> Último carrinho abandonado Há menos de 1 dia<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Custom events
  - name: X evento personalizado em Y dias
    description: "Determina se um usuário realizou ou não um evento especialmente registrado entre 0 e 50 vezes no último número especificado de dias do calendário entre 1 e 30. (Dia do calendário = 1 dia do calendário analisará de 24 a 48 horas do histórico do usuário)<br> <a href=\"/docs/x-in-y-behavior/\"> Saiba mais sobre o comportamento X-in-Y aqui.</a> <br><br>Exemplo:<br>Carrinho abandonado exatamente 0 vezes no último 1 dia do calendário<br><br>Fuso horário:<br>UTC - Para levar em conta todos os fusos horários, 1 dia do calendário analisará de 24 a 48 horas do histórico do usuário, dependendo da hora em que o segmento for avaliado; para 2 dias do calendário, analisará de 48 a 72 horas do histórico do usuário e assim por diante."
    tags:
      - Custom events
  - name: Propriedade do evento personalizado X em Y dias
    description: "Determina se um usuário realizou ou não um evento especialmente registrado em relação a uma propriedade específica entre 0 e 50 vezes no último número especificado de dias de calendário entre 1 e 30. (Dia do calendário = 1 dia do calendário analisará de 24 a 48 horas do histórico do usuário)<br><a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-in-Y aqui.</a> <br><br>Exemplo:<br> Adicionado aos Favoritos com a propriedade \"event_name\" exatamente 0 vezes no último dia do calendário<br><br>Fuso horário:<br>UTC - Para levar em conta todos os fusos horários, 1 dia do calendário analisará de 24 a 48 horas do histórico do usuário, dependendo da hora em que o segmento for avaliado; para 2 dias do calendário, analisará de 48 a 72 horas do histórico do usuário e assim por diante."
    tags:
      - Custom events
  - name: Endereço de e-mail 
    description: "Permite que você designe os destinatários de sua campanha por endereços de e-mail individuais para testes. Isso também pode ser usado para enviar e-mails transacionais a todos os seus usuários (inclusive os que cancelaram a assinatura) usando o especificador \"Email Address is not Blank\" (Endereço de e-mail não está em branco) dentro do filtro, para que você possa maximizar a entrega de e-mails independentemente do status de opt-in. <br><br>Esse filtro verifica apenas se os perfis de usuário têm um endereço de e-mail, enquanto o filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">E-mail disponível</a> verifica critérios adicionais."
    tags:
      - Other Filters
  - name: ID de usuário externo
    description: Permite designar os destinatários da campanha por IDs de usuários individuais para testes.
    tags:
      - Other Filters
  - name: "Balde aleatório #"
    description: Segmenta seus usuários por um número atribuído aleatoriamente (0 a 9999 inclusive). Ele pode permitir a criação de segmentos uniformemente distribuídos de usuários verdadeiramente aleatórios para testes A/B e multivariados.
    tags:
      - Other Filters
  - name: Contagem de sessões
    description: Segmenta seus usuários pelo número de sessões que eles tiveram em qualquer um dos seus aplicativos dentro do seu espaço de trabalho.
    tags:
      - Sessions
  - name: Contagem de sessões para o aplicativo
    description: Segmenta seus usuários pelo número de sessões que eles tiveram em um aplicativo específico e designado.
    tags:
      - Sessions
  - name: X sessões nos últimos Y dias
    description: "Segmenta seus usuários pelo número de sessões (entre 0 e 50) que eles tiveram em seu aplicativo no último número especificado de dias de calendário entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-in-Y aqui.</a>"
    tags:
      - Sessions
  - name: Primeiro aplicativo usado
    description: "Segmenta seus usuários pelo primeiro horário registrado em que eles abriram seu aplicativo. <em>Observe que isso capturará a primeira sessão que eles tiverem usando uma versão do seu aplicativo com o SDK do Braze integrado.</em> (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Sessions
  - name: Aplicativo específico usado pela primeira vez
    description: "Segmenta seus usuários pelo primeiro horário registrado em que eles abriram qualquer um dos seus aplicativos dentro do seu espaço de trabalho. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Sessions
  - name: Último aplicativo usado
    description: "Segmenta seus usuários de acordo com o momento mais recente em que eles abriram seu aplicativo. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Sessions
  - name: Último aplicativo específico usado
    description: "Segmenta seus usuários pelo tempo mais recente em que eles abriram um aplicativo específico e designado. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Sessions
  - name: Duração média da sessão
    description: Segmenta seus usuários pela duração média de suas sessões em seu aplicativo.
    tags:
      - Sessions
  - name: Mensagem recebida da campanha
    description: "Segmenta seus usuários de acordo com o fato de terem recebido ou não uma campanha específica.<br><br> Para Content Cards, Banners e mensagens in-app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem in-app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, é quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. <br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Variante de campanha recebida
    description: "Segmenta seus usuários de acordo com a variante de uma campanha multivariada que eles receberam.<br><br> Para Content Cards, Banners e mensagens in-app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem in-app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, é quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. <br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Mensagem recebida da etapa do Canvas
    description: "Segmenta seus usuários de acordo com o fato de terem ou não recebido um componente específico do Canvas.<br><br> Para Content Cards e mensagens in-app, é quando um usuário registra uma impressão, não quando o cartão ou a mensagem in-app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, é quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. <br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Última mensagem recebida de uma etapa específica do Canvas
    description: Segmenta seus usuários de acordo com o momento em que eles receberam um componente específico do Canvas. Esse filtro não considera quando os usuários receberam outros componentes do Canvas.
    tags:
      - Retargeting
  - name: Última mensagem recebida de uma campanha específica
    description: Segmenta seus usuários de acordo com o fato de terem recebido ou não uma campanha específica. Esse filtro não considera quando os usuários receberam outras campanhas.
    tags:
      - Retargeting
  - name: Mensagem recebida da campanha ou do Canvas com tag
    description: "Segmenta seus usuários de acordo com o fato de eles terem recebido ou não uma campanha específica ou um Canvas com uma tag específica.<br><br> Para Content Cards, Banners (somente campanhas) e mensagens in-app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem in-app é enviada.<br><br>Para push e webhooks, é quando a mensagem é enviada ao usuário.<br><br> Para o WhatsApp, é quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. <br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário."
    tags:
      - Retargeting
  - name: Última mensagem recebida da campanha ou do Canvas com tag
    description: Segmenta seus usuários por quando eles receberam uma campanha específica ou Canvas com uma tag específica. Esse filtro não considera quando os usuários receberam outras campanhas ou Canvases. (período de 24 horas)
    tags:
      - Retargeting
  - name: Nunca recebeu uma mensagem da Campaign ou do Canvas Step
    description: Segmenta seus usuários de acordo com o fato de terem ou não recebido qualquer campanha ou componente do Canvas.
    tags:
      - Retargeting
  - name: Último e-mail recebido
    description: "Segmenta seus usuários de acordo com a última vez que eles receberam uma de suas mensagens de e-mail. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Último envio recebido
    description: "Segmenta seus usuários de acordo com a última vez em que receberam uma de suas notificações por push. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Impressão da última mensagem no aplicativo
    description: Segmenta seus usuários de acordo com a última vez que eles visualizaram uma mensagem in-app.
    tags:
      - Retargeting
  - name: Último SMS recebido
    description: "Segmenta seus usuários pelo horário em que a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Último webhook recebido
    description: "Segmenta seus usuários de acordo com a última vez em que o Braze enviou um webhook para esse usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Último WhatsApp recebido
    description: "Segmenta seus usuários de acordo com a última vez que eles receberam uma mensagem do WhatsApp. É quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Campanha clicada/aberta
    description: "Filtrar por interação com uma campanha específica. Para mensagens de e-mail, o evento de abertura inclui aberturas de máquina e aberturas que não são de máquina.<br><br> Para e-mail, isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail depois que a mensagem for enviada e antes da abertura ou do clique, a abertura ou o clique será aplicado a todos os usuários restantes com esse endereço de e-mail, em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou pela última vez um SMS de resposta que corresponde a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com esse número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>- O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha."
    tags:
      - Retargeting
  - name: Campanha clicada/aberta ou Canvas com tag
    description: "Filtrar por interação com uma campanha específica que tenha uma tag específica. Para mensagens de e-mail, o evento de abertura inclui aberturas de máquina e aberturas que não são de máquina.<br><br> Para e-mail, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail depois que a mensagem for enviada e antes da abertura ou do clique, a abertura ou o clique será aplicado a todos os usuários restantes com esse endereço de e-mail, em vez do usuário original.<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou pela última vez um SMS de resposta que corresponde a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com esse número de telefone. A campanha deve ter sido recebida nas últimas quatro horas.<br>- Quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, de uma determinada campanha ou etapa do Canvas com tag."
    tags:
      - Retargeting
  - name: Etapa clicada/aberta
    description: "Filtrar por interação com um componente específico do Canvas. Para mensagens de e-mail, o evento de abertura inclui aberturas de máquina e aberturas que não são de máquina.<br><br>Para e-mail, isso inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\".<br><br>Para SMS, uma interação é definida como:<br>- O usuário enviou pela última vez um SMS de resposta que corresponde a uma determinada categoria de palavra-chave. Isso é atribuído à campanha mais recente recebida por todos os usuários com esse número de telefone. A campanha deve ter sido recebida nas últimas quatro horas. <br>- O usuário selecionou pela última vez qualquer link encurtado em uma mensagem SMS que tenha o rastreamento de cliques do usuário ativado, em uma determinada etapa do Canvas."
    tags:
      - Retargeting
  - name: Alias clicado na campanha
    description: "Filtre seus usuários por terem clicado em um alias específico em uma campanha específica. Isso se aplica somente a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail depois que a mensagem for enviada e antes da abertura ou do clique, a abertura ou o clique será aplicado a todos os usuários restantes com esse endereço de e-mail, em vez do usuário original."
    tags:
      - Retargeting
  - name: Alias clicado na etapa do Canvas
    description: "Filtre seus usuários por terem clicado em um alias específico em um Canvas específico. Isso se aplica somente a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail depois que a mensagem for enviada e antes da abertura ou do clique, a abertura ou o clique será aplicado a todos os usuários restantes com esse endereço de e-mail, em vez do usuário original."
    tags:
      - Retargeting
  - name: Alias clicado em qualquer etapa do Campaign ou do Canvas
    description: "Filtre seus usuários por terem clicado em um alias específico em qualquer campanha ou Canvas. Isso se aplica somente a mensagens de e-mail. <br><br> Se vários usuários compartilharem o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail depois que a mensagem for enviada e antes da abertura ou do clique, a abertura ou o clique será aplicado a todos os usuários restantes com esse endereço de e-mail, em vez do usuário original."
    tags:
      - Retargeting
  - name: Hard Bounced
    description: "Segmente seus usuários de acordo com o fato de o endereço de e-mail deles ter ou não sofrido hard bounce (por exemplo, o endereço de e-mail é inválido)."
    tags:
      - Retargeting
  - name: Soft Bounced
    description: "Segmente seus usuários de acordo com o número de vezes que eles sofreram soft bounce em Y dias. Os filtros do Segment só podem olhar para trás 30 dias, mas você pode olhar mais para trás com o Segment Extensions.<br><br>Esse filtro funciona de forma diferente de um evento de soft bounce no Currents. O filtro de segmento Soft Bounced conta um soft bounce se não houver uma entrega bem-sucedida durante o período de tentativa de 72 horas. No Currents, cada nova tentativa malsucedida é enviada como um evento de soft bounce." 
    tags:
      - Retargeting
  - name: Marcou você como spam
    description: Segmenta seus usuários de acordo com o fato de eles terem ou não marcado suas mensagens como spam.
    tags:
      - Retargeting
  - name: Número de telefone inválido 
    description: Segmenta seus usuários de acordo com o fato de o número de telefone ser inválido ou não.
    tags:
      - Retargeting
  - name: Categoria de palavra-chave de entrada do último SMS enviado específico
    description: Segmenta seus usuários de acordo com a última vez que eles enviaram um SMS para um grupo de assinatura específico dentro de uma categoria de palavra-chave específica. 
    tags:
      - Retargeting
  - name: Convertido da campanha
    description: Segmenta seus usuários de acordo com o fato de eles terem convertido ou não em uma campanha específica. Esse filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: Convertido de tela
    description: Segmenta seus usuários de acordo com o fato de eles terem convertido ou não em um Canvas específico. Esse filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: No grupo de controle da campanha
    description: Segmenta seus usuários de acordo com o fato de eles estarem ou não no grupo de controle de uma campanha multivariada específica.
    tags:
      - Retargeting
  - name: No grupo de controle do Canvas
    description: "Segmenta seus usuários de acordo com o fato de estarem ou não no grupo de controle de um Canvas específico. Esse filtro avalia apenas os usuários que entraram no Canvas.<br><br>Por exemplo, se você filtrar os usuários que não estão no grupo de controle de um Canvas, receberá todos os usuários que entraram no Canvas, mas não estão no grupo de controle."
    tags:
      - Retargeting
  - name: Último inscrito em qualquer grupo de controle
    description: "Segmenta seus usuários de acordo com a última vez em que eles se enquadraram no grupo de controle em uma campanha. <br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Variação de tela inserida
    description: "Segmenta seus usuários de acordo com o fato de eles terem ou não entrado em um caminho de variação de um Canvas específico. Esse filtro avalia todos os usuários.<br><br>Por exemplo, se você filtrar os usuários que não entraram em um grupo de controle de variação do Canvas, receberá todos os usuários que não estão no grupo de controle, independentemente de terem entrado no Canvas."
    tags:
      - Retargeting
  - name: Última mensagem recebida
    description: "Segmenta seus usuários determinando a última mensagem recebida. (período de 24 horas)<br><br> Para Content Cards, Banners e mensagens in-app, é quando um usuário registrou uma impressão pela última vez, não quando o cartão ou a mensagem in-app foi enviada pela última vez.<br><br>Para push e webhooks, é quando qualquer mensagem foi enviada ao usuário.<br><br> Para o WhatsApp, é quando a última solicitação de API de mensagem foi enviada ao WhatsApp, não quando a mensagem foi entregue ao dispositivo do usuário. <br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando a última mensagem foi entregue ao provedor de SMS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário.<br><br>Exemplo:<br>Last Received Message Less than 1 Day ago = menos de 24 horas atrás<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Último engajamento com mensagem
    description: "Segmenta seus usuários pela última vez em que clicaram ou abriram um de seus canais de mensagens (banners, cartão de conteúdo, e-mail, no aplicativo, SMS, push, WhatsApp). Para mensagens de e-mail, o evento de abertura inclui aberturas de máquina e aberturas que não são de máquina. (período de 24 horas)<br><br>No caso de e-mails, é quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Isso também inclui a opção de filtrar por \"abriu qualquer e-mail (aberturas de máquina)\" e \"abriu qualquer e-mail (outras aberturas)\". Quando vários usuários compartilham o mesmo endereço de e-mail:<br>- No envio inicial, apenas o perfil específico do usuário-alvo é atualizado. <br>- Quando o e-mail for entregue, ou se o usuário abrir o e-mail ou um link no e-mail, todos os usuários que compartilham esse endereço de e-mail parecerão ter recebido a mensagem.<br><br>Para SMS, é quando o usuário selecionou pela última vez qualquer link encurtado em uma mensagem que tenha o rastreamento de cliques do usuário ativado.<br><br>Fuso horário:<br>Fuso horário da empresa"
    tags:
      - Retargeting
  - name: Cartão clicado 
    description: "Segmenta seus usuários de acordo com o fato de terem ou não clicado em um Content Card específico. Esse filtro está disponível como um subfiltro de \"Campanha clicada/aberta\", \"Campanha clicada/aberta ou Canvas com tag\" e \"Etapa clicada/aberta\"."
    tags:
      - Retargeting
  - name: Sinalizadores de recursos
    description: "O segmento de seus usuários que têm um <a href=\"/docs/developer_guide/feature_flags/\">sinalizador de recurso</a> específico ativado no momento."
    tags:
      - Retargeting
  - name: Grupo de Assinatura
    description: "Segmenta seus usuários por grupo de assinatura de e-mail, SMS/MMS ou WhatsApp. Os grupos arquivados não serão exibidos e não poderão ser usados."
    tags:
      - Channel subscription behavior
  - name: E-mail disponível
    description: "Segmenta seus usuários de acordo com a existência de um endereço de e-mail válido e se eles estão inscritos ou optaram por receber e-mails. Esse filtro verifica três critérios: se o usuário cancelou a assinatura de e-mails, se o Braze recebeu um hard bounce e se o e-mail foi marcado como spam. Se algum desses critérios for atendido ou se não houver um e-mail para um usuário, ele não será incluído.<br><br>Observe que, se você enviar uma mensagem transacional, os usuários cujo \"E-mail disponível\" for <code>falso</code> não serão incluídos no cálculo do público, mas ainda assim poderão receber uma mensagem. No entanto, o cálculo do público incluirá apenas usuários inscritos ou opt-in. <br><br>Para e-mails em que o status de opt-in é importante, sugerimos o uso do filtro \"Email Available\" (E-mail disponível) em vez do filtro \" <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">Email Address\" (Endereço de e-mail)</a>; os critérios adicionais podem ajudá-lo a direcionar os usuários que realmente desejam ver suas mensagens."
    tags:
      - Channel subscription behavior
  - name: Data de aceitação do e-mail
    description: Segmenta seus usuários de acordo com a data em que eles optaram por receber e-mails.
    tags:
      - Channel subscription behavior
  - name: Status da assinatura de e-mail
    description: Segmenta seus usuários pelo status de assinatura de e-mail.
    tags:
      - Channel subscription behavior
  - name: Data de cancelamento da assinatura do e-mail 
    description: Segmenta seus usuários pela data em que eles cancelaram a assinatura de futuros e-mails.
    tags:
      - Channel subscription behavior
  - name: Push de primeiro plano ativado
    description: "Segmenta os usuários que têm autorização provisória de push ou que estão habilitados para push em primeiro plano. Especificamente, essa contagem inclui:<br>1. usuários do iOS que estão provisoriamente autorizados a receber push. <br>2. Usuários que estão habilitados para push em primeiro plano e cujo status de assinatura de push não foi cancelado, para qualquer um dos seus aplicativos. Para esses usuários, essa contagem inclui apenas o push em primeiro plano.<br><br>O Foreground Push Enabled não inclui usuários que cancelaram a assinatura. <br><br>Depois de segmentar com esse filtro, você poderá ver um detalhamento de quem está nesse segmento para Android, iOS e Web no painel inferior, chamado <em>Reachable Users (Usuários alcançáveis</em>)."
    tags:
      - Channel subscription behavior
  - name: Push em primeiro plano ativado para o aplicativo
    description: Segmenta se os usuários têm o push ativado para seu aplicativo no dispositivo deles. Usuários que têm o push em primeiro plano ativado para um aplicativo. Isso não leva em conta o status da assinatura push. Essa contagem inclui usuários que autorizaram provisoriamente tokens de push em primeiro e segundo plano.
    tags:
      - Channel subscription behavior
  - name: Push de fundo ou de primeiro plano ativado
    description: Segmenta de acordo com o fato de os usuários terem um token de envio e não terem cancelado a assinatura. Usuários que têm o push em segundo plano ou em primeiro plano ativado para qualquer um dos seus aplicativos.
    tags:
      - Channel subscription behavior
  - name: Data de ativação do push
    description: Segmenta seus usuários pela data em que eles optaram pelo push.
    tags:
      - Channel subscription behavior
  - name: Status da assinatura push
    description: "Segmenta seus usuários por <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">status de assinatura</a> para envio."
    tags:
      - Channel subscription behavior
  - name: Data de cancelamento da assinatura do push
    description: Segmenta seus usuários pela data em que eles cancelaram a assinatura de futuras notificações por push.
    tags:
      - Channel subscription behavior
  - name: Produto adquirido
    description: Segmenta seus usuários por produtos comprados em seu aplicativo.
    tags:
      - Purchase behavior
  - name: Número total de compras
    description: Segmenta seus usuários de acordo com o número de compras que eles fizeram em seu aplicativo.
    tags:
      - Purchase behavior
  - name: X produto comprado em Y dias
    description: Filtre os usuários por horários em que um produto específico foi comprado.
    tags:
      - Purchase behavior
  - name: X compras nos últimos Y dias
    description: "Segmenta seus usuários pelo número de vezes (entre 0 e 50) que eles fizeram uma compra no último número especificado de dias corridos entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-in-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: X Compra de propriedade em Y dias
    description: "Segmenta seus usuários pelo número de vezes que uma compra foi feita em relação a uma determinada propriedade de compra no último número especificado de dias corridos entre 1 e 30. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-in-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: Primeira compra realizada
    description: Segmenta seus usuários pelo primeiro momento em que um usuário fez uma compra em seu aplicativo.
    tags:
      - Purchase behavior
  - name: Primeira compra do aplicativo
    description: Segmenta seus usuários pelo primeiro momento em que um usuário fez uma compra em seu aplicativo.
    tags:
      - Purchase behavior
  - name: Última compra realizada
    description: Filtre os usuários pela última vez que fizeram uma compra.
    tags: 
      - Purchase behavior
  - name: Último produto comprado
    description: Filtre os usuários por quando eles compraram um produto específico pela última vez.
    tags:
      - Purchase behavior
  - name: Dinheiro gasto
    description: Segmenta seus usuários de acordo com a quantia de dinheiro que eles gastaram em seu aplicativo.
    tags:
      - Purchase behavior
  - name: X dinheiro gasto em Y dias
    description: "Segmenta seus usuários pela quantidade de dinheiro que eles gastaram em seu aplicativo no último número especificado de dias corridos, entre 1 e 30. Esse valor incluirá apenas a soma das últimas 50 compras. <br> <a href=\"/docs/x-in-y-behavior/\">Saiba mais sobre o comportamento X-in-Y aqui.</a>"
    tags:
      - Purchase behavior
  - name: País
    description: Segmenta seus usuários pela última localização de país indicada.
    tags:
      - Demographic attributes
  - name: Cidade
    description: Segmenta seus usuários pela última localização de cidade indicada.
    tags:
      - Demographic attributes
  - name: Idioma
    description: Segmenta seus usuários de acordo com o idioma preferido deles.
    tags:
      - Demographic attributes
  - name: Idade
    description: "Segmenta seus usuários por idade, conforme indicado no seu aplicativo."
    tags:
      - Demographic attributes
  - name: Aniversário
    description: "Segmenta seus usuários por data de aniversário, conforme indicado no aplicativo. <br> Os usuários com aniversário no dia 29 de fevereiro serão incluídos em segmentos que incluem o dia 1º de março.<br><br>Para segmentar aniversários de dezembro ou janeiro, insira a lógica de filtro somente dentro do período de 12 meses do ano que você está segmentando. Em outras palavras, não insira uma lógica que remeta ao mês de dezembro do ano civil anterior ou ao mês de janeiro do ano seguinte. Por exemplo, para segmentar aniversários de dezembro, você pode filtrar por \"em 31 de dezembro\", \"antes de 31 de dezembro\" ou \"após 30 de novembro\"."
    tags:
      - Demographic attributes
  - name: Gênero
    description: "Segmenta seus usuários por gênero, conforme indicado no seu aplicativo."
    tags:
      - Demographic attributes
  - name: Número de telefone não formatado
    description: "Segmenta seus usuários pelo número de telefone não formatado. Não inclui parênteses, traços ou outros símbolos."
    tags:
      - Demographic attributes
  - name: Primeiro nome
    description: "Segmenta seus usuários pelo primeiro nome, conforme indicado no seu aplicativo."
    tags:
      - Demographic attributes
  - name: Sobrenome
    description: "Segmenta seus usuários pelo sobrenome, conforme indicado no seu aplicativo."
    tags:
      - Demographic attributes
  - name: Tem aplicativo
    description: "Segmenta de acordo com o fato de um usuário ter ou não instalado seu aplicativo. Isso incluirá os usuários que atualmente têm seu aplicativo instalado e aqueles que o desinstalaram no passado. Isso geralmente exige que os usuários abram o aplicativo (iniciem uma sessão) para serem incluídos nesse filtro. No entanto, há algumas exceções, como se um usuário tiver sido importado para o Braze e associado manualmente ao seu aplicativo."
    tags:
      - App
  - name: Nome da versão mais recente do aplicativo
    description: "Segmentos pelo nome recente do aplicativo do usuário.<br><br>Ao usar \"menor que\" ou \"menor que ou igual a\", se a versão principal do aplicativo não existir, esse filtro retornará `verdadeiro` porque o usuário é mais antigo que a versão do aplicativo. Isso significa que, se a última versão do aplicativo principal do usuário não existir, ele corresponderá automaticamente ao filtro."
    tags:
      - App 
  - name: Número da versão mais recente do aplicativo
    description: "Segmenta pelo número da versão recente do aplicativo do usuário.<br><br>Ao usar \"menor que\" ou \"menor que ou igual a\", se a versão principal do aplicativo não existir, esse filtro retornará `verdadeiro` porque o usuário é mais antigo que a versão do aplicativo. Isso significa que, se a última versão do aplicativo principal do usuário não existir, ele corresponderá automaticamente ao filtro.<br><br>Pode levar algum tempo para que as versões atuais do aplicativo sejam preenchidas. A versão do aplicativo no perfil do usuário é atualizada quando as informações são capturadas pelo SDK, que se baseia em quando os usuários abrem seus aplicativos. Se o usuário não abrir o aplicativo, a versão atual não será atualizada. Esses filtros também não serão aplicados retroativamente. É bom usar \"maior que\" ou \"igual\" para versões atuais e futuras, mas usar filtros de versões anteriores pode causar comportamentos inesperados."
    tags:
      - App 
  - name: Desinstalado
    description: Segmenta seus usuários de acordo com o fato de eles terem desinstalado seu aplicativo e não o terem reinstalado.
    tags:
      - Uninstall 
  - name: Transportadora de dispositivos
    description: Segmenta seus usuários de acordo com a operadora do dispositivo.
    tags:
      - Devices
  - name: Contagem de dispositivos
    description: Segmenta seus usuários de acordo com o número de dispositivos em que eles usaram seu aplicativo.
    tags:
      - Devices
  - name: Modelo do dispositivo
    description: Segmenta seus usuários pela versão do modelo do telefone celular.
    tags:
      - Devices
  - name: Sistema operacional do dispositivo
    description: Segmenta seus usuários que têm um ou mais dispositivos com o sistema operacional especificado.
    tags:
      - Devices
  - name: Localidade do dispositivo mais recente
    description: "Segmenta seus usuários pelas <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">informações de localidade</a> do dispositivo usado mais recentemente."
    tags:
      - Devices      
  - name: Modelo de relógio mais recente
    description: Segmenta seus usuários pelo modelo mais recente de smartwatch.
    tags:
      - Devices    
  - name: Autorizado provisoriamente no iOS
    description: Permite encontrar usuários que estão autorizados provisoriamente no iOS 12 para um determinado aplicativo.
    tags:
      - Devices   
  - name: Navegador da Web
    description: Segmenta seus usuários pelo navegador da Web que eles usam para acessar seu site.
    tags:
      - Devices
  - name: Dispositivo IDFA
    description: Permite que você designe os destinatários de sua campanha por IDFA para testes.
    tags:
      - Advertising use cases
  - name: Dispositivo IDFV
    description: Permite que você designe os destinatários de sua campanha por IDFV para testes.
    tags:
      - Advertising use cases 
  - name: Dispositivo ID de anúncio do Google
    description: Segmenta seus usuários pelo ID do anúncio do Google.
    tags:
      - Advertising use cases
  - name: Dispositivo ID do anúncio Roku
    description: Segmenta seus usuários pelo ID do anúncio da Roku.
    tags:
      - Advertising use cases
  - name: ID de anúncio do Windows do dispositivo
    description: Segmenta seus usuários pelo ID de anúncio do Windows.
    tags:
      - Advertising use cases  
  - name: Rastreamento de anúncios ativado
    description: "Permite filtrar com base no fato de seus usuários terem optado pelo rastreamento de anúncios. O rastreamento de anúncios está relacionado ao IDFA ou \"identificador para anunciantes\" atribuído a todos os dispositivos iOS pela Apple, que pode ser definido pelos SDKs. Esse identificador permite que os anunciantes rastreiem os usuários e exibam anúncios direcionados a eles."
    tags:
      - Advertising use cases
  - name: Local mais recente
    description: Segmenta seus usuários pelo último local registrado em que eles usaram seu aplicativo.
    tags:
      - Location
  - name: Localização disponível
    description: "Segmenta seus usuários de acordo com o fato de eles terem ou não informado suas localizações. Para usar esse filtro, seu aplicativo precisa ter <a href=\"/docs/search/?query=location%20tracking\">o rastreamento de localização integrado.</a>"
    tags:
      - Location
  - name: Coortes de amplitude
    description: Os clientes que usam o Amplitude podem complementar seus segmentos escolhendo e importando seus cohorts no Amplitude.
    tags:
      - Cohort membership
  - name: Coortes do Censo
    description: Os clientes que usam o Censo podem complementar seus segmentos escolhendo e importando suas coortes no Censo.
    tags:
      - Cohort membership
  - name: Coortes de pilha
    description: Os clientes que usam o Heap podem complementar seus segmentos escolhendo e importando seus cohorts no Heap.
    tags:
      - Cohort membership
  - name: Coortes Hightouch
    description: Os clientes que usam o Hightouch podem complementar seus segmentos escolhendo e importando suas coortes no Hightouch.
    tags:
      - Cohort membership
  - name: Coortes de Kubit
    description: Os clientes que usam o Kubit podem complementar seus segmentos escolhendo e importando seus cohorts no Kubit.
    tags:
      - Cohort membership
  - name: Coortes do Mixpanel
    description: Os clientes que usam o Mixpanel podem complementar seus segmentos escolhendo e importando suas coortes no Mixpanel.
    tags:
      - Cohort membership
  - name: Coortes de segmentos
    description: Os clientes que usam o Segment podem complementar seus segmentos escolhendo e importando seus cohorts no Segment.
    tags:
      - Cohort membership
  - name: Coortes Tinyclues
    description: Os clientes que usam o Tinyclues podem complementar seus segmentos escolhendo e importando suas coortes no Tinyclues.
    tags:
      - Cohort membership
  - name: Instalar anúncio de atribuição
    description: Segmenta seus usuários pelo anúncio ao qual a instalação foi atribuída.
    tags:
      - User Attributes
  - name: Instalar o Attribution Adgroup
    description: Segmenta seus usuários pelo grupo de anúncios ao qual a instalação foi atribuída.
    tags:
      - Install Attribution
  - name: Instalar campanha de atribuição
    description: Segmenta seus usuários pela campanha de anúncios à qual a instalação foi atribuída.
    tags:
      - Install Attribution
  - name: Instalar a fonte de atribuição
    description: Segmenta seus usuários pela fonte à qual a instalação foi atribuída.
    tags:
      - Install Attribution
  - name: Categoria de risco de rotatividade
    description:  Segmenta seus usuários por categoria de risco de rotatividade de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Pontuação de risco de rotatividade
    description: Segmenta seus usuários por pontuação de risco de rotatividade de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Categoria de probabilidade de evento
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Pontuação de probabilidade de evento
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Canal inteligente
    description: Segmente seus usuários pelo canal mais ativo nos últimos três meses.
    tags:
      - Intelligence and predictive
  - name: Mensagem Aberta Probabilidade
    description: "Filtra seus usuários com base na probabilidade de eles abrirem uma mensagem em um canal específico em uma escala de 0 a 100%. Os usuários sem dados suficientes para medir a probabilidade de um canal podem ser selecionados usando \"está em branco\"."
    tags:
      - Intelligence and predictive
  - name: Número de amigos do Facebook que usam o aplicativo
    description: Segmenta seus usuários de acordo com o número de amigos do Facebook que usam o mesmo aplicativo.
    tags:
      - Social activity
  - name: Facebook conectado
    description: Segmenta seus usuários de acordo com o fato de eles terem conectado seu aplicativo ao Facebook.
    tags:
      - Social activity
  - name: Twitter conectado
    description: Segmenta seus usuários de acordo com o fato de eles terem conectado seu aplicativo ao X (antigo Twitter).
    tags:
      - Social activity
  - name: Número de seguidores no Twitter
    description: Segmenta seus usuários de acordo com o número de seguidores do X (antigo Twitter) que eles têm.
    tags:
      - Social activity
  - name: Número de telefone
    description: "Segmenta seus usuários pelo campo de número de telefone formatado em E.164.<br><br> Quando um número de telefone é enviado ao Braze, o Braze tenta coagir o número para o <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">formato e.164</a>, que é usado para enviar pelos canais SMS e WhatsApp. O processo de coerção pode falhar se o número não estiver formatado corretamente, o que faz com que o perfil do usuário tenha um número de telefone não formatado, mas não um número de telefone de envio. Esse filtro de segmento retorna os usuários pelo número de telefone formatado em e.164 (quando disponível).<br><br>Casos de uso:<br> - Use esse filtro para entender o tamanho do público-alvo mais preciso ao enviar mensagens SMS ou WhatsApp.  <br>- Use expressões regulares (regex) com esse filtro para segmentar por números telefônicos com um código de país específico. <br>- Use esse filtro para segmentar usuários por números de telefone que não passaram no processo de coerção e.164."
    tags:
      - Other filters
---
