---
nav_title: "Referência de tabela SQL"
article_title: Referência de tabela SQL
page_order: 3
page_type: reference
toc_headers: h2
description: "Este artigo contém tabelas e colunas disponíveis para serem consultadas no Criador de consultas ou ao gerar extensões de segmento SQL."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Referência de tabela SQL

Esta página é uma referência de tabelas e colunas disponíveis para consulta no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) ou ao gerar [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Tabela de conteúdo

Tabela | Descrição
------|------------
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Itens de catálogo não excluídos
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Quando o Grupo de Controle Global é alterado
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Quando um usuário realiza um evento personalizado
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Quando um usuário instala um app e nós o atribuímos a um parceiro
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Quando um usuário registra um local
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Quando um usuário faz uma compra
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Quando um usuário desinstala um app
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Quando um usuário faz upgrade do aplicativo
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Quando um usuário tem sua primeira sessão
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Quando um usuário visualiza o Feed de notícias
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Quando um usuário termina uma sessão em um aplicativo
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Quando um usuário inicia uma sessão em um app
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Quando um usuário dispara uma área com geofences (por exemplo, quando ele entra ou sai de uma geofence). Esse evento foi agrupado com outros eventos e recebido por meio do endpoint de eventos padrão e, portanto, pode não ter sido recebido pelo endpoint em tempo real.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Quando um usuário dispara uma área com geofences (por exemplo, quando ele entra ou sai de uma geofence). Esse evento foi recebido por meio do endpoint dedicado de geofence e, portanto, é recebido em tempo real assim que o dispositivo de um usuário detecta que disparou uma geofence. <br><br>Além disso, devido ao limite de frequência no endpoint do geofence, é possível que alguns eventos de geofence não sejam refletidos como um RecordEvent. Todos os eventos de geofence, no entanto, são representados por DataEvent (mas potencialmente com alguma postergação devido ao agrupamento).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Quando um token por push de atividade ao vivo é alterado
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Quando um token de atualização do Live Activity é alterado
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Quando o estado de um token de notificação por push muda
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Quando um usuário se inscreve ou cancela a inscrição globalmente em um canal, como e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Quando um usuário é inscrito ou cancela a inscrição em um grupo de inscrições ou de um grupo de inscrições
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Quando um usuário converte para uma campanha
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Quando um usuário é inscrito no grupo de controle de uma campanha
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Quando um usuário recebe um limite de frequência para uma campanha
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período de conversão primária
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Quando um usuário avança para uma etapa do Canva
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Quando um usuário se converte em um evento de conversão do Canva
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Quando um usuário entra em um Canva
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Quando um usuário sai de um Canva porque corresponde aos critérios de saída do público
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Quando um usuário sai de um Canva porque executou um evento de exceção
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Quando um usuário converte para uma etapa do Canva Experiment
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Quando um usuário entra em uma etapa da jornada experimental
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Quando um usuário recebe um limite de frequência para uma etapa do Canva
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período do evento de conversão primária
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Uma mensagem de banner originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Quando um usuário clica em um banner
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Quando um usuário visualiza um banner
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Uma mensagem de cartão de conteúdo originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Quando um usuário clica em um cartão de conteúdo
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Quando um usuário descarta um cartão de conteúdo
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um cartão de conteúdo
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Quando enviamos um cartão de conteúdo a um usuário
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Uma mensagem de e-mail originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Um provedor de serviços de e-mail retornou um hard bounce. Um hard bounce significa uma falha permanente de entregabilidade.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Quando um usuário clica em um link em um e-mail
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Quando um e-mail é adiado
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Quando um e-mail é entregue
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Quando um e-mail é marcado como spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Quando um usuário abre um e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Quando enviamos um e-mail para um usuário
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Quando um e-mail é soft bounce
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Quando um usuário cancela a inscrição no e-mail
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Quando um usuário visualiza um Feature Flag
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Uma mensagem no app originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Quando um usuário clica em uma mensagem no app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Quando um usuário visualiza uma mensagem no app
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Quando uma mensagem programada do LINE não puder ser entregue, antes de enviá-la ao LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Quando um usuário clica em um link em uma mensagem do LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Quando uma mensagem LINE é recebida de um usuário
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Quando uma mensagem LINE é enviada para o LINE
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Quando uma atividade ao vivo tem um evento de resultado
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Quando uma mensagem de Atividade ao vivo é enviada
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Uma mensagem de cartão do feed de notícias originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Quando um usuário clica em um cartão do feed de notícias
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um cartão do Feed de notícias
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Uma mensagem de notificação por push originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Quando uma notificação por push é devolvida
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Quando um usuário abre o app após receber uma notificação sem clicar na notificação
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Quando um usuário recebe uma notificação por push enquanto o app está aberto. <br><br>Esse evento não é compatível com o [SDK do Swift](https://github.com/braze-inc/braze-swift-sdk) e está obsoleto no [SDK do Obj-C](https://github.com/Appboy/appboy-ios-sdk).
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Quando um usuário abre uma notificação por push ou clica em um botão de notificação por push (incluindo um botão FECHAR que NÃO abre o app). <br><br> Os botões de ação por push têm vários resultados. As ações Não, Recusar e Cancelar são "cliques", e as ações Aceitar são "aberturas". Ambos são representados nesta tabela, mas podem ser distinguidos na coluna **BUTTON_ACTION_TYPE** coluna. Por exemplo, uma consulta pode ser usada para agrupar por um `BUTTON_ACTION_TYPE` que não seja No (Não), Decline (Recusar) ou Cancel (Cancelar).
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Quando enviamos uma notificação por push a um usuário
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Quando um envio de mensagens RCS é interrompido devido a um erro detectado no Braze e a mensagem é descartada
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Quando o usuário final interage com uma mensagem RCS tocando ou clicando em um elemento da interface do usuário
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Quando uma mensagem RCS é entregue com sucesso ao dispositivo móvel de um usuário final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Quando o Braze recebe uma mensagem RCS originada do usuário final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Quando o usuário final abre uma mensagem RCS em seu dispositivo
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Quando uma mensagem RCS não é entregue devido à intervenção da operadora
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Quando uma mensagem RCS é enviada dos sistemas da Braze para parceiros de entrega de última milha
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Uma mensagem SMS originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Quando uma mensagem SMS é enviada para a operadora
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Quando uma mensagem SMS é enviada
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Quando o Braze não conseguir enviar a mensagem SMS para o prestador de serviço de SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Quando uma mensagem SMS é recebida de um usuário
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Quando uma mensagem SMS não é entregue a um usuário
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Quando uma mensagem SMS é enviada
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Quando um usuário clica em um URL encurtado do Braze incluído em uma mensagem SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Uma mensagem de webhook originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Quando uma mensagem de webhook é enviada, mas falha com uma resposta de erro do ponto de extremidade
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Quando enviamos um webhook para um usuário
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Uma mensagem do WhatsApp originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Quando um usuário clica em um link ou botão em uma mensagem do WhatsApp
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Quando uma mensagem do WhatsApp é enviada
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Quando uma mensagem do WhatsApp não é entregue a um usuário
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Quando uma mensagem do WhatsApp é recebida de um usuário
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Quando um usuário abre uma mensagem do WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Quando enviamos uma mensagem do WhatsApp para um usuário
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Quando o número do intervalo aleatório de um usuário é alterado
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Quando um usuário é excluído por uma solicitação do cliente
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Quando um usuário é mesclado com o perfil de outro usuário e o perfil original fica órfão


## Catálogos

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Campo | Tipo | Descrição
------|------|------------
`catalog_id` | `string` | ID BSON do catálogo
`item_id` | `string` | ID BSON do item de catálogo
`app_group_id` | `null,` `string` | ID BSON do grupo de app
`app_group_api_id` | `null,` `string` | API ID do grupo de app
`field_name` | `null,` `string` | Nome do campo
`field_value` | `null,` `string` | Valor do campo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Changelogs

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`random_bucket_number` | `null, int` | Novo número de balde aleatório
`global_control_group` | `null, boolean` | Com essa alteração, o número do balde é incluído como grupo de controle global
`previous_global_control_group` | `null, boolean` | Antes dessa alteração, o número do balde era incluído como grupo de controle global, mas não é mais
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Comportamentos

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que realizou o evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`name` | `string` | Nome do evento personalizado
`properties` | `string` | Propriedades personalizadas do evento armazenadas como uma string codificada em JSON
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que instalou
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix no qual o usuário instalou
`source` | `string` | a fonte da atribuição
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que registra o local
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse local foi registrado
`time` | `int` | Carimbo de data e hora Unix no qual o local foi registrado
`latitude` | `float` | [IPI] Latitude do local registrado
`longitude` | `float` | [IPI] Longitude do local registrado
`altitude` | `null, float` | [IPI] altitude do local registrado
`ll_accuracy` | `null, float` | precisão da latitude e longitude do local registrado
`alt_accuracy` | `null, float` | precisão da altitude do local registrado
`device_id` | `null,` `string` | ID do dispositivo no qual o local foi registrado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso quando o local foi registrado
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que fez uma compra
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual a compra ocorreu
`time` | `int` | Carimbo de data e hora Unix no qual o usuário fez a compra
`device_id` | `null,` `string` | ID do dispositivo no qual a compra ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a compra
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`product_id` | `string` | ID do produto adquirido
`price` | `float` | Preço da compra
`currency` | `string` | Moeda da compra
`properties` | `string` | Propriedades personalizadas da compra armazenadas como uma string codificada em JSON
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que desinstalou
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app que foi desinstalado
`time` | `int` | Registro de data e hora Unix no qual o usuário desinstalou
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que fez o upgrade do app
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app que o usuário fez upgrade
`time` | `int` | Registro de data e hora Unix no qual o usuário fez upgrade do app
`device_id` | `null,` `string` | ID do dispositivo no qual o usuário fez upgrade do app
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`old_app_version` | `null,` `string` | Versão antiga do aplicativo
`new_app_version` | `null,` `string` | Nova versão do app
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual essa sessão ocorreu
`time` | `int` | Registro de data e hora Unix no qual a sessão foi iniciada
`session_id` | `string` | UUID da sessão
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual essa sessão ocorreu
`time` | `int` | Registro de data e hora Unix no qual a sessão terminou
`duration` | `null, float` | Duração da sessão em segundos
`session_id` | `string` | UUID da sessão
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_api_id` | `null,` `string` | API ID do app no qual essa sessão ocorreu
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix no qual a sessão foi iniciada
`session_id` | `string` | UUID da sessão
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que realizou o evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi disparado. (por exemplo, 'enter' (entrar) ou 'exit' (sair))
`location_set_id` | `string` | A ID do conjunto de locais da geofence que foi disparada
`geofence_id` | `string` | A ID da geofence que foi disparada
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que realizou o evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi disparado. (por exemplo, 'enter' (entrar) ou 'exit' (sair))
`location_set_id` | `string` | A ID do conjunto de locais da geofence que foi disparada
`geofence_id` | `string` | A ID da geofence que foi disparada
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`activity_attributes_type` | `null,` `string` | Tipo de atribuição de atividade ao vivo
`push_to_start_token` | `null,` `string` | Atividade ao vivo token por push para iniciar
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplicável apenas a tokens por push do iOS, 1 para desenvolvimento, 2 para produção
`push_token_state_change_type` | `null,` `string` | Uma descrição do tipo de alteração de estado do token por push
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`activity_id` | `null,` `string` | Identificador de atividade ao vivo
`update_token` | `null,` `string` | Token de atualização de atividade ao vivo
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplicável apenas a tokens por push do iOS, 1 para desenvolvimento, 2 para produção
`push_token_state_change_type` | `null,` `string` | Uma descrição do tipo de alteração de estado do token por push
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`push_token` | `null,` `string` | Token por push do evento
`push_token_created_at` | `null, int` | Registro de data e hora UNIX no qual o token por push foi criado
`push_token_updated_at` | `null, int` | Registro de data e hora UNIX no qual o token por push foi atualizado pela última vez
`push_token_foreground_push_disabled` | `null, boolean` | Sinalizador de desativação de push em primeiro plano do token por push
`push_token_device_id` | `null,` `string` | ID do dispositivo do token por push
`push_token_provisionally_opted_in` | `null, boolean` | Bandeira de aceitação provisória do token por push
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplicável apenas a tokens por push do iOS, 1 para desenvolvimento, 2 para produção
`web_push_token_public_key` | `null,` `string` | Chave pública do token por push, aplicável somente a tokens por push da web
`web_push_token_user_auth` | `null,` `string` | Autenticação do usuário do token por push, aplicável apenas a tokens por push da Web
`web_push_token_vapid_public_key` | `null,` `string` | Chave pública VAPID do token por push, aplicável somente a tokens por push da web
`push_token_state_change_type` | `null,` `string` | Uma descrição do tipo de alteração de estado do token por push
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário afetado
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`email_address` | `null,` `string` | [IPI] endereço de e-mail do usuário
`state_change_source` | `null,` `string` | fonte da mudança de estado (REST, SDK, dashboard, etc.)
`subscription_status` | `string` | Status da inscrição: 'Inscrição', 'Cancelamento de inscrição' ou 'Aceitação'
`channel` | `null,` `string` | Canal do estado da inscrição global, como e-mail
`time` | `int` | Registro de data e hora Unix no qual o estado da inscrição foi alterado
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app ao qual o evento pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`send_id` | `null,` `string` | ID de envio de mensagens que originou essa ação de mudança de estado da inscrição
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`channel_identifier` | `null,` `string` | [IPI] O identificador do usuário no canal ao qual o evento se destina.
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário afetado
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`email_address` | `null,` `string` | [IPI] endereço de e-mail do usuário
`phone_number` | `null,` `string` | Número de telefone [IPI] do usuário no formato e164
`app_api_id` | `null,` `string` | API ID do app ao qual o evento pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`channel` | `null,` `string` | Canal: "e-mail" ou "sms", dependendo do tipo de canal do grupo de inscrições
`subscription_status` | `string` | Status da inscrição: 'Inscrição', 'Cancelamento de inscrição' ou 'Aceitação'
`time` | `int` | Registro de data e hora Unix no qual o estado da inscrição foi alterado
`timezone` | `null,` `string` | Fuso horário do usuário
`send_id` | `null,` `string` | ID de envio de mensagens que originou essa ação de mudança de estado da inscrição
`state_change_source` | `null,` `string` | Fonte da mudança de estado (REST, SDK, dashboard, etc.)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`channel_identifier` | `null,` `string` | [IPI] O identificador do usuário no canal ao qual o evento se destina.
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campanhas

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`conversion_behavior_index` | `null, int` | Índice do comportamento de conversão
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`channel` | `null,` `string` | Canal ao qual esse evento pertence
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`revenue` | `long` | O valor da receita em dólares americanos, em centavos, gerada
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canva

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [IPI] ID de usuário externo do usuário                                                                              |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                                                                    |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID do Canva ao qual esse evento pertence        |         
| `canvas_variation_api_id`              | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                                                                 |
| `progression_type`                     | `string`, `null`    | Tipo de evento de progressão de etapas |
| `is_canvas_entry`                      | `boolean`, `null`   | Se essa é a entrada em uma primeira etapa do Canva        |
| `exit_reason`                          | `string`, `null`    | Se for uma saída, o motivo pelo qual o usuário saiu da tela durante a etapa do canva                  |
| `canvas_entry_id`                      | `string`, `null`    | Identificador exclusivo para essa instância de um usuário em um Canva  |
| `next_step_id`                         | `string`, `null`    | BSON ID da próxima etapa do canva |
| `next_step_api_id`                     | `string`, `null`    | API ID da próxima etapa do canva |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [IPI] ID de usuário externo do usuário                                                                              |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                                                                    |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `app_api_id`                           | `string`, `null`    | API ID do app no qual esse evento ocorreu                                                                  |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence                                                     |
| `canvas_api_id`                        | `string`, `null`    | API ID do Canva ao qual esse evento pertence                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID da variação da mensagem da etapa do canva que este usuário recebeu                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Tipo de evento de conversão que o usuário realizou, em que "0" é uma conversão primária e "1" é uma conversão secundária |
| `gender`                               | `string`, `null`    | [IPI] Gênero do usuário                                                                                        |
| `country`                              | `string`, `null`    | [IPI] País do usuário                                                                                       |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                                                            |
| `language`                             | `string`, `null`    | [IPI] Idioma do usuário                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `device_id`               | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | [Depreciado] ID da API da etapa do Canva à qual esse evento pertence         |
| `gender`                  | `string`, `null`    | [IPI] Gênero do usuário                                             |
| `country`                 | `string`, `null`    | [IPI] País do usuário                                            |
| `timezone`                | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                | `string`, `null`    | [IPI] Idioma do usuário                                           |
| `in_control_group`        | `boolean`, `null`   | True se o usuário estiver inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                      |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                      |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Campo                       | Tipo                     | Descrição                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                   | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`          | `string`, `null`    | [IPI] ID de usuário externo do usuário                                                                              |
| `app_group_id`              | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `time`                      | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `app_api_id`                | `string`, `null`    | API ID do app no qual esse evento ocorreu                                                                  |
| `canvas_id`                 | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence                                                     |
| `canvas_api_id`             | `string`, `null`    | API ID do Canva ao qual esse evento pertence                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                                                            |
| `canvas_step_api_id`        | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | API ID da etapa do experimento à qual esse evento pertence                                                             |
| `conversion_behavior_index` | `int`, `null`       | Tipo de evento de conversão que o usuário realizou, em que "0" é uma conversão primária e "1" é uma conversão secundária |
| `sf_created_at`             | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
| `experiment_split_api_id` | `string`, `null` | API ID da divisão do experimento em que o usuário se inscreveu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                      |
| `experiment_step_api_id`  | `string`, `null`    | API ID da etapa do experimento à qual esse evento pertence                  |
| `in_control_group`        | `boolean`, `null`   | True se o usuário estiver inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |

| `experiment_split_api_id` | `string`, `null` | API ID da divisão do experimento em que o usuário se inscreveu
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`                     | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`                     | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`                        | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id`              | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`                   | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID da variação da mensagem da etapa do canva que este usuário recebeu       |
| `channel`                              | `string`, `null`    | Canal de envio de mensagens ao qual esse evento pertence (e-mail, push, etc.)          |
| `gender`                               | `string`, `null`    | [IPI] Gênero do usuário                                             |
| `country`                              | `string`, `null`    | [IPI] País do usuário                                            |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`, `null`    | [IPI] Idioma do usuário                                           |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`                     | `string`, `null`    | [IPI] ID de usuário externo do usuário                                   |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`                     | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID da tela à qual esse evento pertence          |
| `canvas_api_id`                        | `string`, `null`    | API ID do Canva ao qual esse evento pertence                           |
| `canvas_variation_api_id`              | `string`, `null`    | API ID da variação da tela à qual esse evento pertence                 |
| `canvas_step_api_id`                   | `string`, `null`    | API ID da etapa do Canva à qual esse evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API ID da variação da mensagem da etapa do canva que este usuário recebeu       |
| `gender`                               | `string`, `null`    | [IPI] Gênero do usuário                                             |
| `country`                              | `string`, `null`    | [IPI] País do usuário                                            |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`, `null`    | [IPI] Idioma do usuário                                           |
| `revenue`                              | `int`, `null`       | Valor da receita gerada em dólares americanos, exibido como centavos               |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
| `app_api_id` | `string`, `null` | API ID do app no qual esse evento ocorreu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Mensagens


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um dos ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes do aborto (até 128 caracteres)
`banner_placement_id` | `null,` `string` | ID de posicionamento de banner especificado pelo cliente
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`button_id` | `null,` `string` | ID do botão clicado, se esse clique representar um clique em um botão
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um dos ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`banner_placement_id` | `null,` `string` | ID de posicionamento de banner especificado pelo cliente
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um dos ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`banner_placement_id` | `null,` `string` | ID de posicionamento de banner especificado pelo cliente
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`content_card_id` | `string` | ID do cartão que gerou esse evento
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`sending_ip` | `null,` `string` | Endereço IP a partir do qual o envio de e-mail foi feito
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,` `string` | [IPI] O código de motivo SMTP e a mensagem amigável recebida para esse evento de bounce
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_drop` | `null, boolean` | Indica que esse evento conta como um evento de queda
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`url` | `null,` `string` | URL em que o usuário clicou
`user_agent` | `null,` `string` | Agente do usuário no qual o clique ocorreu
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`link_id` | `null,` `string` | ID exclusivo para o link que foi clicado, conforme criado pelo Braze
`link_alias` | `null,` `string` | Alias associado a essa ID de link
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`is_suspected_bot_click` | `null, boolean` | Se esse evento foi processado como um evento de bot
`suspected_bot_click_reason` | `null, object` | Por que esse evento foi classificado como um bot
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`email_address` | `null,` `string` | [IPI] Endereço de e-mail do usuário
`recipient_domain` | `null,` `string` | Domínio de e-mail do destinatário
`esp` | `null,` `string` | ESP relacionado ao evento (Sparkpost ou Sendgrid, ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`sending_ip` | `null,` `string` | Endereço IP a partir do qual o envio de e-mail foi feito
`timezone` | `null,` `string` | Fuso horário do usuário
`deferral_reason` | `null,` `string` | [IPI] O código de motivo SMTP e a mensagem amigável recebida para esse evento de adiamento
`attempt_count` | `null, int` | Número de tentativas feitas para enviar a mensagem
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`sending_ip` | `null,` `string` | Endereço IP do qual o e-mail foi enviado
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`user_agent` | `null,` `string` | Agente do usuário no qual ocorreu o relatório de spam
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`user_agent` | `null,` `string` | Agente do usuário no qual a abertura ocorreu
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`machine_open` | `null,` `string` | Preenchido como "true" se o evento de abertura for disparado sem engajamento do usuário, por exemplo, por um dispositivo Apple com a proteção de privacidade de e-mail ativada. O valor pode mudar ao longo do tempo para fornecer mais granularidade.
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares de valores-chave marcados durante a renderização do Liquid
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`sending_ip` | `null,` `string` | Endereço IP a partir do qual o envio de e-mail foi feito
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,` `string` | [IPI] O código de motivo SMTP e a mensagem amigável recebida para esse evento de bounce
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] endereço de e-mail do usuário
`ip_pool` | `null,` `string` | Pool de IP a partir do qual o envio de e-mail foi feito
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`feature_flag_id_name` | `null,` `string` | O identificador do lançamento do Feature Flag
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`carrier` | `null,` `string` | Operadora do dispositivo
`country` | `null,` `string` | [IPI] País do usuário
`device_model` | `null,` `string` | Modelo do dispositivo
`language` | `null,` `string` | [IPI] Idioma do usuário
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`platform` | `null,` `string` | Plataforma do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`timezone` | `null,` `string` | Fuso horário do usuário
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`version` | `string` | Qual versão da mensagem no app, antiga ou disparada
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | operadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
`version` | `string` | qual versão da mensagem no app, antiga ou disparada
`button_id` | `null,` `string` | ID do botão clicado, se esse clique representar um clique em um botão
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | operadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
`version` | `string` | qual versão da mensagem no app, antiga ou disparada
`ad_id` | `null,` `string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`locale_key` | `null,` `string` | [IPI] A chave correspondente às traduções (por exemplo, "en-us") usadas para criar essa mensagem (nulo para o padrão).
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes do aborto (até 128 caracteres)
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`line_channel_id` | `null,` `string` | A ID do canal LINE para o qual a mensagem foi enviada ou recebida
`line_channel_name` | `null,` `string` | O nome do canal LINE para o qual a mensagem foi enviada ou recebida
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`native_line_id` | `null,` `string` | [IPI] A ID do LINE do usuário para o qual a mensagem foi enviada ou recebida
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,` `string` | Fuso horário do usuário
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`timezone` | `null,` `string` | Fuso horário do usuário
`native_line_id` | `null,` `string` | [IPI] A ID do LINE do usuário para o qual a mensagem foi enviada ou recebida
`line_channel_id` | `null,` `string` | A ID do canal LINE para o qual a mensagem foi enviada ou recebida
`line_channel_name` | `null,` `string` | O nome do canal LINE para o qual a mensagem foi enviada ou recebida
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_name` | `null,` `string` | Nome da campanha
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`is_suspected_bot_click` | `null, boolean` | Se esse evento foi processado como um evento de bot
`short_url` | `null,` `string` | URL abreviado que foi clicado
`url` | `null,` `string` | URL em que o usuário clicou
`user_agent` | `null,` `string` | Agente do usuário no qual ocorreu o relatório de spam
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`line_channel_id` | `null,` `string` | A ID do canal LINE para o qual a mensagem foi enviada ou recebida
`line_channel_name` | `null,` `string` | O nome do canal LINE para o qual a mensagem foi enviada ou recebida
`media_id` | `null,` `string` | A ID gerada pelo LINE que pode ser usada para recuperar a mídia de entrada do LINE
`message_body` | `null,` `string` | Resposta digitada pelo usuário
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`native_line_id` | `null,` `string` | [IPI] A ID do LINE do usuário para o qual a mensagem foi enviada ou recebida
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,` `string` | Fuso horário do usuário
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`line_channel_id` | `null,` `string` | A ID do canal LINE para o qual a mensagem foi enviada ou recebida
`line_channel_name` | `null,` `string` | O nome do canal LINE para o qual a mensagem foi enviada ou recebida
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`native_line_id` | `null,` `string` | [IPI] A ID do LINE do usuário para o qual a mensagem foi enviada ou recebida
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,` `string` | Fuso horário do usuário
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`activity_id` | `null,` `string` | Identificador de atividade ao vivo
`activity_attributes_type` | `null,` `string` | Tipo de atribuição de atividade ao vivo
`push_to_start_token` | `null,` `string` | Atividade ao vivo token por push para iniciar
`update_token` | `null,` `string` | Token de atualização de atividade ao vivo
`live_activity_event_type` | `null,` `string` | Tipo de evento de atividade ao vivo. Um de ['start', 'update', 'end']
`live_activity_event_outcome` | `null,` `string` | Resultado do evento Live Activity
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`activity_id` | `null,` `string` | Identificador de atividade ao vivo
`activity_attributes_type` | `null,` `string` | Tipo de atribuição de atividade ao vivo
`push_to_start_token` | `null,` `string` | Atividade ao vivo token por push para iniciar
`update_token` | `null,` `string` | Token de atualização de atividade ao vivo
`live_activity_event_type` | `null,` `string` | Tipo de evento de atividade ao vivo. Um de ['start', 'update', 'end']
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes do aborto (até 128 caracteres)
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`card_api_id` | `null,` `string` | API ID do cartão
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo - extraído de user_agent \- no qual a abertura ocorreu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que fizemos uma tentativa de entrega para
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`push_token` | `null,` `string` | Token por push que apresentou bounce
`device_id` | `null,` `string` | `device_id` para o qual fizemos uma tentativa de entrega que foi devolvida
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`platform` | `null,` `string` | Plataforma do dispositivo
`ad_id` | `null,` `string` | [IPI] ID de publicidade do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Esse evento não é compatível com o [SDK do Swift](https://github.com/braze-inc/braze-swift-sdk) e está obsoleto no [SDK do Obj-C](https://github.com/Appboy/appboy-ios-sdk).
{% endalert %}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | [IPI] ID de publicidade do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Operadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`button_string` | `null,` `string` | Identificador (button_string) do botão de notificação por push clicado. Nulo se não for de um clique de botão
`button_action_type` | `null,` `string` | Tipo de ação do botão de notificação por push. Um de [URI, DEEP_LINK, NONE, CLOSE]. nulo se não for um clique de botão
`slide_id` | `null,` `string` | Identificador de slide do slide do carrossel push em que o usuário clica
`slide_action_type` | `null,` `string` | Tipo de ação do slide do carrossel push
`ad_id` | `null,` `string` | [IPI] ID de publicidade do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`push_token` | `null,` `string` | Push token que fizemos uma tentativa de entrega para
`device_id` | `null,` `string` | `device_id` que fizemos uma tentativa de entrega para
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | API ID do app no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`ad_id` | `null,` `string` | [IPI] ID de publicidade do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`is_sampled` | `null,` `string` | Indica se o push send foi amostrado e se esperava um evento de entrega
`locale_key` | `null,` `string` | [IPI] A chave correspondente às traduções (por exemplo, "en-us") usadas para criar essa mensagem (nulo para o padrão).
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes do aborto (até 128 caracteres)
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`is_suspected_bot_click` | `null, boolean` | Se esse evento foi processado como um evento de bot
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`short_url` | `null,` `string` | URL abreviado que foi clicado
`suspected_bot_click_reason` | `null,` `string` | Por que esse evento foi classificado como um bot
`user_agent` | `null,` `string` | Agente do usuário no qual ocorreu o relatório de spam
`user_phone_number` | `null,` `string` | [IPI] O número de telefone do usuário do qual a mensagem foi recebida
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`interaction_type` | `null,` `string` | O tipo de interação que gerou o clique. Exemplo de valores de string: URL de texto, resposta, OpenURL
`element_label` | `null,` `string` | Detalhes opcionais sobre o elemento clicado, como o texto de uma resposta ou botão sugerido
`element_type` | `null,` `string` | Especifica se um interaction_type que é comum entre sugestões e botões veio de uma sugestão ou botão. Exemplos: Sugestão, botão
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`url` | `null,` `string` | URL em que o usuário clicou
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`to_phone_number` | `null,` `string` | [IPI] Número de telefone do usuário que está recebendo a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`from_rcs_sender` | `null,` `string` | A ID do remetente RCS ou o nome do agente usado para enviar a mensagem
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`action` | `null,` `string` | Ação tomada em resposta a essa mensagem. (por exemplo, inscrição, cancelamento da inscrição ou nenhuma).
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`media_urls` | `null,` `string` | URLs de mídia do usuário
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`user_phone_number` | `null,` `string` | [IPI] O número de telefone do usuário do qual a mensagem foi recebida
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_body` | `null,` `string` | Resposta digitada pelo usuário
`to_rcs_sender` | `null,` `string` | O remetente RCS de entrada para o qual a mensagem foi enviada
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`to_phone_number` | `null,` `string` | [IPI] Número de telefone do usuário que está recebendo a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`error` | `null,` `string` | Nome do erro
`from_rcs_sender` | `null,` `string` | A ID do remetente RCS ou o nome do agente usado para enviar a mensagem
`is_sms_fallback` | `null, boolean` | Indica se houve tentativa de fallback de SMS para essa mensagem RCS rejeitada. Ele está vinculado/emparelhado ao evento de entrega de SMS
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`provider_error_code` | `null,` `string` | Código de erro do provedor
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`to_phone_number` | `null,` `string` | [IPI] Número de telefone do usuário que está recebendo a mensagem no formato e.164 (por exemplo, +14155552671)
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`campaign_name` | `null,` `string` | Nome da campanha
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_name` | `null,` `string` | Nome da tela
`canvas_step_name` | `null,` `string` | Nome da etapa do canva
`canvas_variation_name` | `null,` `string` | Nome da variante do canva recebida por este usuário
`category` | `null,` `string` | Nome da categoria da palavra-chave, preenchido apenas para mensagens de resposta automática: "aceitação", "desativação", "ajuda" ou valor personalizado
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`from_rcs_sender` | `null,` `string` | A ID do remetente RCS ou o nome do agente usado para enviar a mensagem
`message_extras` | `null,` `string` | Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`message_variation_name` | `null,` `string` | Nome da variação da mensagem
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`to_phone_number` | `null,` `string` | [IPI] Número de telefone do usuário que está recebendo a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se houve tentativa de fallback de SMS para essa mensagem RCS rejeitada. Ele está vinculado/emparelhado ao evento de entrega de SMS
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`error` | `null,` `string` | nome do erro
`provider_error_code` | `null,` `string` | código de erro do prestador de serviço de SMS
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se houve tentativa de fallback de SMS para essa mensagem RCS rejeitada. Ele está vinculado/emparelhado ao evento de entrega de SMS
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `null,` `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho associado ao número telefônico de entrada
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`user_phone_number` | `string` | [IPI] o número de telefone do usuário do qual a mensagem foi recebida
`subscription_group_id` | `null,` `string` | ID do grupo de inscrições direcionado para essa mensagem SMS
`subscription_group_api_id` | `null,` `string` | API ID do grupo de inscrições direcionado para essa mensagem SMS
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`action` | `string` | Ação tomada em resposta a essa mensagem. Por exemplo, `Subscribed`, `Unsubscribed`, ou `None`.
`message_body` | `string` | Resposta do usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação de mensagens da etapa do canva à qual esse evento pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`error` | `null,` `string` | nome do erro
`provider_error_code` | `null,` `string` | código de erro do prestador de serviço de SMS
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se houve tentativa de fallback de SMS para essa mensagem RCS rejeitada. Ele está vinculado/emparelhado ao evento de entrega de SMS
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de inscrições
`category` | `null,` `string` | Nome da categoria da palavra-chave, preenchido apenas para mensagens de resposta automática: 'Aceitação', 'Desaceitação', 'Ajuda' ou valor personalizado
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `null,` `string` | Braze ID do usuário direcionado por short_url, null se short_url não usou o rastreamento de cliques do usuário
`external_user_id` | `null,` `string` | [IPI] ID externo do usuário direcionado por short_url, se houver, nulo se short_url não tiver usado o rastreamento de cliques do usuário
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho usado para gerar short_url
`time` | `int` | Registro de data e hora Unix no qual short_url foi clicado
`timezone` | `null,` `string` | Fuso horário do usuário
`campaign_id` | `null,` `string` | Braze ID da campanha para a qual short_url foi gerado, nulo se não for de uma campanha
`campaign_api_id` | `null,` `string` | ID da API da campanha para a qual short_url foi gerado, nulo se não for de uma campanha
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem para a qual short_url foi gerado, nulo se não for de uma campanha
`canvas_id` | `null,` `string` | Braze ID do Canvas short_url foi gerado para, nulo se não for de um Canvas
`canvas_api_id` | `null,` `string` | API ID do Canvas short_url foi gerado para, nulo se não for de um Canvas
`canvas_variation_api_id` | `null,` `string` | API ID da variação do Canva short_url foi gerada para, nula se não for de um Canvas
`canvas_step_api_id` | `null,` `string` | API ID da etapa do canva para a qual short_url foi gerada, nula se não for de um canva
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação de mensagem da etapa do canva short_url foi gerada para, nula se não for de um canva
`url` | `string` | URL original contido na mensagem para a qual é redirecionado por short_url
`short_url` | `string` | URL encurtado que foi clicado
`user_agent` | `null,` `string` | agente do usuário solicitando short_url
`user_phone_number` | `string` | [IPI] o número de telefone do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`is_suspected_bot_click` | `null, boolean` | Se esse evento foi processado como um evento de bot
`suspected_bot_click_reason` | `null, object` | Por que esse evento foi classificado como um bot
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`http_status_code` | `null, int` | Código de status HTTP da resposta
`endpoint_url` | `null,` `string` | O URL do ponto de extremidade que está sendo solicitado
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`content_length` | `null, int` | Comprimento do conteúdo da resposta
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`host` | `null,` `string` | O host da solicitação
`id` | `string` | ID globalmente exclusivo para esse evento
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`raw_response` | `null,` `string` | Resposta bruta truncada do endpoint
`retry_count` | `null, int` | O número de tentativas de novas tentativas
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`url_path` | `null,` `string` | A jornada da url que está sendo solicitada
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`webhook_duration` | `null, int` | Duração total dessa solicitação em milissegundos
`webhook_failure_source` | `null,` `string` | Para saber se um erro foi criado pelo Braze ou pelo próprio endpoint. O campo de origem pode ser External Endpoint, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Se esse evento foi a tentativa terminal em um envio
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`gender` | `null,` `string` | [IPI] Gênero do usuário
`country` | `null,` `string` | [IPI] País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [IPI] Idioma do usuário
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares chave-valor tag durante a renderização Liquid
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | 	`null,` `string` | Número de telefone [IPI] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`abort_type` | `null,` `string` | Tipo de aborto, um de ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [IPI] Mensagem de registro que descreve os detalhes da interrupção (máximo de 2.000 caracteres)
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID externa do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`app_group_id` | `null,` `string` | ID BSON do grupo de app ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do grupo de app ao qual esse usuário pertence
`time` | `int` | Registro de data e hora UNIX em que o evento ocorreu
`timezone` | `null,` `string` | Fuso horário do usuário
`campaign_id` | `null,` `string` | ID BSON da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID BSON da tela à qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`url` | `null,` `string` | URL em que o usuário clicou
`short_url` | `null,` `string` | URL abreviado que foi clicado
`user_agent` | `null,` `string` | Agente do usuário no qual ocorreu o relatório de spam
`user_phone_number` | `null,` `string` | [IPI] O número de telefone do usuário do qual a mensagem foi recebida
`sf_created_at` | `timestamp`, `null` | quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`flow_id` | `null,` `string` | A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
`template_name` | `null,` `string` | [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,` `string` | A ID exclusiva gerada pelo Meta para essa mensagem
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`provider_error_code` | `null,` `string` | Código de erro do WhatsApp
`provider_error_title` | `null, ` `string` | Título de erro do WhatsApp
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`message_id` | `null,` `string` | A ID exclusiva gerada pelo Meta para essa mensagem
`template_name` | `null,` `string` | [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
`flow_id` | `null,` `string` | A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`user_phone_number` | `string` | [IPI] o número de telefone do usuário do qual a mensagem foi recebida
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`message_body` | `string` | Resposta do usuário
`quick_reply_text` | `string` | Texto do botão pressionado pelo usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`action` | `string` | Ação tomada em resposta a essa mensagem. Por exemplo, `Subscribed`, `Unsubscribed`, ou `None`.
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
`catalog_id` | `null,` `string` | ID do catálogo de produto, caso um produto seja mencionado na mensagem recebida (caso contrário, permanece vazio).
`product_id` | `null,` `string` | ID do produto adquirido
`flow_id` | `null,` `string` | A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
`flow_response_json` | `null,` `string` | [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
`message_id` | `null,` `string` | A ID exclusiva gerada pelo Meta para essa mensagem
`in_reply_to` | `null,` `string` | O endereço message_id da mensagem à qual esta mensagem estava respondendo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [IPI] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`template_name` | `null,` `string` | [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,` `string` | A ID exclusiva gerada pelo Meta para essa mensagem
`flow_id` | `null,` `string` | A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string`	| Número de telefone [IPI] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [IPI] ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | API ID do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | API ID da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | API ID da variação de mensagens que este usuário recebeu
`canvas_id` | `null,` `string` | ID do Braze de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | API ID do Canva ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | API ID da variação da tela à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | API ID da etapa do Canva à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | API ID da variação da mensagem da etapa do canva que este usuário recebeu
`dispatch_id` | `null,` `string` | ID do envio ao qual essa mensagem pertence
`message_extras` | `null,` `string` | [IPI] Uma string JSON dos pares de valores-chave marcados durante a renderização do Liquid
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
`send_id` | `null,` `string` | ID de envio de mensagens à qual esta mensagem pertence
`flow_id` | `null,` `string` | A ID exclusiva do fluxo no WhatsApp Manager. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
`template_name` | `null,` `string` | [IPI] Nome do modelo no gerenciador do WhatsApp. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,` `string` | A ID exclusiva gerada pelo Meta para essa mensagem
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuários

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Campo                       | Tipo                     | Descrição                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID globalmente exclusivo para esse evento                  |
| `app_group_id`              | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence      |
| `app_group_api_id`          | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence       |
| `user_id`                   | `string`, `null`    | ID do Braze do usuário que realizou esse evento      |
| `external_user_id`          | `string`, `null`    | [IPI] ID de usuário externo do usuário                 |
| `time`                      | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu         |
| `random_bucket_number`      | `int`, `null`       | Número atual do intervalo aleatório atribuído ao usuário  |
| `prev_random_bucket_number` | `int`, `null`       | Número do balde aleatório anterior atribuído ao usuário |
| `sf_created_at`             | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Campo              | Tipo                     | Descrição                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID globalmente exclusivo para esse evento                             |
| `user_id`          | `string`, `null`    | ID do Braze do usuário que foi excluído                          |
| `app_group_id`     | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                 |
| `app_group_api_id` | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                  |
| `time`             | `int`, `null`       | Registro de data e hora Unix no qual a solicitação de exclusão de usuário foi processada |
| `sf_created_at`    | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Campo              | Tipo                     | Descrição                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID globalmente exclusivo para esse evento                                             |
| `user_id`          | `string`, `null`    | Braze ID do usuário órfão                                         |
| `external_user_id` | `string`, `null`    | [IPI] ID de usuário externo do usuário                                            |
| `device_id`        | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo          |
| `app_group_id`     | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                 |
| `app_group_api_id` | `string`, `null`    | API ID do espaço de trabalho ao qual esse usuário pertence                                  |
| `app_api_id`       | `string`, `null`    | API ID do app ao qual o usuário órfão pertencia                               |
| `time`             | `int`, `null`       | Registro de data e hora Unix em que o usuário ficou órfão                                 |
| `orphaned_by_id`   | `string`, `null`    | ID do Braze do usuário cujo perfil foi mesclado com o perfil do usuário órfão |
| `sf_created_at`    | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
