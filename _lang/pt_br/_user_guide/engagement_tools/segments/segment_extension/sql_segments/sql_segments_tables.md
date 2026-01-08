---
nav_title: "Referência de tabela SQL"
article_title: Referência de tabela SQL
page_order: 3
page_type: reference
toc_headers: h2
description: "Este artigo contém tabelas e colunas disponíveis para serem consultadas no Query Builder ou ao gerar Extensões de Segmento SQL."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Referência de tabela SQL

Esta página é uma referência de tabelas e colunas disponíveis para serem consultadas no [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) ou ao gerar [Extensões de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Tabela de conteúdo

Tabela | Descrição
------|------------
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Quando um usuário realiza um evento personalizado
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Quando um usuário instala um aplicativo e o atribuímos a um parceiro
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Quando um usuário registra um local
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Quando um usuário faz uma compra
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Quando um usuário desinstala um aplicativo
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Quando um usuário atualiza o aplicativo
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Quando um usuário tem sua primeira sessão
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Quando um usuário visualiza o Feed de notícias
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Quando um usuário encerra uma sessão em um aplicativo
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Quando um usuário inicia uma sessão em um aplicativo
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Quando um usuário aciona uma área delimitada geograficamente (por exemplo, quando ele entra ou sai de uma delimitação geográfica). Esse evento foi agrupado com outros eventos e recebido por meio do endpoint de eventos padrão e, portanto, pode não ter sido recebido pelo endpoint em tempo real.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Quando um usuário aciona uma área delimitada geograficamente (por exemplo, quando ele entra ou sai de uma delimitação geográfica). Esse evento foi recebido por meio do endpoint de geofence dedicado e, portanto, é recebido em tempo real assim que o dispositivo de um usuário detecta que acionou uma geofence. <br><br>Além disso, devido à limitação de taxa no endpoint de geofence, é possível que alguns eventos de geofence não sejam refletidos como um RecordEvent. Todos os eventos de geofence, no entanto, são representados por DataEvent (mas possivelmente com algum atraso devido ao agrupamento).
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Quando um usuário se inscreve ou cancela a inscrição globalmente em um canal como o e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Quando um usuário se inscreve ou cancela a inscrição em ou de um grupo de assinatura
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Quando um usuário converte para uma campanha
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Quando um usuário é inscrito no grupo de controle de uma campanha
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Quando um usuário recebe um limite de frequência para uma campanha
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período de conversão primária
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Quando um usuário avança para uma etapa do Canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Quando um usuário se converte para um evento de conversão do Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Quando um usuário entra em um Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Quando um usuário sai de um Canvas porque corresponde aos critérios de saída do público
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Quando um usuário sai de um Canvas porque executou um evento de exceção
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Quando um usuário converte para uma etapa do Canvas Experiment
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Quando um usuário entra em um caminho de etapa de Experiência
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Quando um usuário recebe o limite de frequência para uma etapa do Canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período do evento de conversão primária
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Uma mensagem do Content Card originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Quando um usuário clica em um Content Card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Quando um usuário dispensa um Content Card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um Content Card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Quando enviamos um Content Card a um usuário
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Uma mensagem de e-mail originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Um provedor de serviços de e-mail retornou um hard bounce. Um hard bounce significa uma falha permanente na capacidade de entrega.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Quando um usuário clica em um link em um e-mail
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Quando um e-mail é entregue
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Quando um e-mail é marcado como spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Quando um usuário abre um e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Quando enviamos um e-mail para um usuário
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Quando um e-mail é devolvido
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Quando um usuário cancela a assinatura do e-mail
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Uma mensagem in-app originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Quando um usuário clica em uma mensagem in-app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Quando um usuário visualiza uma mensagem in-app
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Uma mensagem de cartão do Feed de notícias originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Quando um usuário clica em um cartão do Feed de notícias
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um cartão do Feed de notícias
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Uma mensagem de notificação por push originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Quando uma notificação push é rejeitada
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Quando um usuário abre o aplicativo após receber uma notificação sem clicar na notificação
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Quando um usuário recebe uma notificação por push enquanto o aplicativo está aberto
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Quando um usuário abre uma notificação por push ou clica em um botão de notificação por push (incluindo um botão FECHAR que NÃO abre o aplicativo). <br><br> As ações de botão de pressão têm vários resultados. As ações Não, Recusar e Cancelar são "cliques", e as ações Aceitar são "aberturas". Ambos são representados nesta tabela, mas podem ser distinguidos na coluna **BUTTON_ACTION_TYPE** coluna. Por exemplo, uma consulta pode ser usada para agrupar por um `BUTTON_ACTION_TYPE` que não seja No (Não), Decline (Recusar) ou Cancel (Cancelar).
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Quando enviamos uma notificação por push a um usuário
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Uma mensagem SMS originalmente programada foi abortada por algum motivo.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Quando uma mensagem SMS é enviada para a operadora
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Quando uma mensagem SMS é entregue
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Quando o Braze não conseguir enviar a mensagem SMS para o provedor de serviços de SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Quando uma mensagem SMS é recebida de um usuário
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Quando uma mensagem SMS não é entregue a um usuário
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Quando uma mensagem SMS é enviada
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Quando um usuário clica em um URL encurtado do Braze incluído em uma mensagem SMS
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Uma mensagem de webhook originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Quando enviamos um webhook para um usuário
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Uma mensagem do WhatsApp originalmente programada foi abortada por algum motivo
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Quando uma mensagem do WhatsApp é entregue
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Quando uma mensagem do WhatsApp não é entregue a um usuário
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Quando uma mensagem do WhatsApp é recebida de um usuário
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Quando um usuário abre uma mensagem do WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Quando enviamos uma mensagem do WhatsApp para um usuário
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Quando o número do intervalo aleatório de um usuário é alterado
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Quando um usuário é excluído por uma solicitação do cliente
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Quando um usuário é mesclado com o perfil de outro usuário e o perfil original fica órfão


## Comportamentos

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou o evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`name` | `string` | Nome do evento personalizado
`properties` | `string` | Propriedades personalizadas do evento armazenadas como uma cadeia de caracteres codificada em JSON
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que instalou
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix no qual o usuário instalou
`source` | `string` | a fonte da atribuição
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que registra a localização
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse local foi registrado
`time` | `int` | Carimbo de data e hora Unix no qual o local foi registrado
`latitude` | `float` | [Latitude do local registrado
`longitude` | `float` | [Longitude do local registrado
`altitude` | `null, float` | [Altitude do local registrado
`ll_accuracy` | `null, float` | precisão da latitude e longitude do local registrado
`alt_accuracy` | `null, float` | precisão da altitude do local registrado
`device_id` | `null,` `string` | ID do dispositivo no qual a localização foi registrada
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso quando o local foi registrado
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que fez uma compra
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual a compra ocorreu
`time` | `int` | Carimbo de data e hora Unix no qual o usuário fez a compra
`device_id` | `null,` `string` | ID do dispositivo no qual a compra ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a compra
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`product_id` | `string` | ID do produto adquirido
`price` | `float` | Preço da compra
`currency` | `string` | Moeda da compra
`properties` | `string` | Propriedades personalizadas da compra armazenadas como uma cadeia de caracteres codificada em JSON
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que desinstalou
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo que foi desinstalado
`time` | `int` | Registro de data e hora Unix no qual o usuário desinstalou
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que atualizou o aplicativo
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo que o usuário atualizou
`time` | `int` | Registro de data e hora Unix no qual o usuário atualizou o aplicativo
`device_id` | `null,` `string` | ID do dispositivo no qual o usuário atualizou o aplicativo
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`old_app_version` | `null,` `string` | Versão antiga do aplicativo
`new_app_version` | `null,` `string` | Nova versão do aplicativo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa sessão ocorreu
`time` | `int` | Registro de data e hora Unix no qual a sessão foi iniciada
`session_id` | `string` | UUID da sessão
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que visualizou o Feed de notícias
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual o usuário visualizou o Feed de notícias
`time` | `int` | Registro de data e hora Unix em que o usuário visualizou o Feed de notícias
`device_id` | `null,` `string` | ID do dispositivo no qual a impressão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a impressão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa sessão ocorreu
`time` | `int` | Registro de data e hora Unix no qual a sessão foi encerrada
`duration` | `null, float` | Duração da sessão
`session_id` | `string` | UUID da sessão
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | Braze ID do usuário que executa essa ação
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa sessão ocorreu
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix no qual a sessão foi iniciada
`session_id` | `string` | UUID da sessão
`device_id` | `null,` `string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante a sessão
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou o evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi acionado. (por exemplo, "entrar" ou "sair")
`location_set_id` | `string` | A ID do conjunto de localizações da geocerca que foi acionada
`geofence_id` | `string` | A ID da geocerca que foi acionada
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou o evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual essa ação ocorreu
`time` | `int` | Registro de data e hora Unix em que o usuário realizou o evento
`device_id` | `null,` `string` | ID do dispositivo no qual ocorreu o evento personalizado
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi acionado. (por exemplo, "entrar" ou "sair")
`location_set_id` | `string` | A ID do conjunto de localizações da geocerca que foi acionada
`geofence_id` | `string` | A ID da geocerca que foi acionada
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário afetado
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`email_address` | `null,` `string` | Endereço de e-mail do usuário [PII]
`state_change_source` | `null,` `string` | fonte da alteração de estado (REST, SDK, Dashboard etc.)
`subscription_status` | `string` | Status da assinatura: "Subscribed" (Inscrito) ou "Unsubscribed" (Cancelado)
`channel` | `null,` `string` | Canal do estado da assinatura global, como e-mail
`time` | `int` | Registro de data e hora Unix no qual o estado da assinatura foi alterado
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`app_api_id` | `null,` `string` | ID da API do aplicativo ao qual o evento pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`send_id` | `null,` `string` | ID de envio de mensagem de onde se originou essa ação de alteração do estado da assinatura
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário afetado
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`email_address` | `null,` `string` | Endereço de e-mail do usuário [PII]
`phone_number` | `null,` `string` | Número de telefone [PII] do usuário no formato e164
`app_api_id` | `null,` `string` | ID da API do aplicativo ao qual o evento pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`channel` | `null,` `string` | Canal: "e-mail" ou "sms", dependendo do tipo de canal do grupo de assinaturas
`subscription_status` | `string` | Status da assinatura: "Subscribed" (Inscrito) ou "Unsubscribed" (Cancelado)
`time` | `int` | Registro de data e hora Unix no qual o estado da assinatura foi alterado
`timezone` | `null,` `string` | Fuso horário do usuário
`send_id` | `null,` `string` | ID de envio de mensagem de onde se originou essa ação de alteração do estado da assinatura
`state_change_source` | `null,` `string` | Origem da alteração de estado (REST, SDK, Dashboard etc.)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campanhas

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`conversion_behavior_index` | `null, int` | Índice do comportamento de conversão
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`channel` | `null,` `string` | Canal ao qual esse evento pertence
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`revenue` | `long` | O valor da receita em dólares americanos, em centavos, gerada
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Tela

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [ID de usuário externo do usuário                                                                              |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                                                                    |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence                                                     |
| `canvas_api_id`                        | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence        |         
| `canvas_variation_api_id`              | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                                                                 |
| `progression_type`                     | `string`, `null`    | Tipo de evento de progressão de etapas |
| `is_canvas_entry`                      | `boolean`, `null`   | Se essa é a entrada em uma primeira etapa de um Canvas        |
| `exit_reason`                          | `string`, `null`    | Se for uma saída, o motivo pelo qual o usuário saiu da tela durante a etapa                  |
| `canvas_entry_id`                      | `string`, `null`    | Identificador exclusivo para essa instância de um usuário em um Canvas  |
| `next_step_id`                         | `string`, `null`    | ID BSON da próxima etapa na tela |
| `next_step_api_id`                     | `string`, `null`    | ID da API da próxima etapa no Canvas |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`                     | `string`, `null`    | [ID de usuário externo do usuário                                                                              |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `app_group_api_id`                     | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                                                                    |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `app_api_id`                           | `string`, `null`    | ID da API do aplicativo no qual esse evento ocorreu                                                                  |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence                                                     |
| `canvas_api_id`                        | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Tipo de evento de conversão realizado pelo usuário, em que "0" é uma conversão primária e "1" é uma conversão secundária |
| `gender`                               | `string`, `null`    | [Sexo do usuário                                                                                        |
| `country`                              | `string`, `null`    | [País do usuário                                                                                       |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                                                            |
| `language`                             | `string`, `null`    | [Idioma do usuário                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`               | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | [Depreciado] ID da API da etapa do Canvas à qual esse evento pertence         |
| `gender`                  | `string`, `null`    | [Sexo do usuário                                             |
| `country`                 | `string`, `null`    | [País do usuário                                            |
| `timezone`                | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                | `string`, `null`    | [Idioma do usuário                                           |
| `in_control_group`        | `boolean`, `null`   | True se o usuário estiver inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`               | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                      |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`               | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`        | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                      |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Campo                       | Tipo                     | Descrição                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                   | `string`, `null`    | ID do Braze do usuário que realizou esse evento                                                                   |
| `external_user_id`          | `string`, `null`    | [ID de usuário externo do usuário                                                                              |
| `device_id`                 | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo                                            |
| `app_group_id`              | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                                                   |
| `time`                      | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                                                                      |
| `app_api_id`                | `string`, `null`    | ID da API do aplicativo no qual esse evento ocorreu                                                                  |
| `canvas_id`                 | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence                                                     |
| `canvas_api_id`             | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                                                            |
| `canvas_step_api_id`        | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | ID da API da etapa da experiência à qual esse evento pertence                                                             |
| `conversion_behavior_index` | `int`, `null`       | Tipo de evento de conversão realizado pelo usuário, em que "0" é uma conversão primária e "1" é uma conversão secundária |
| `sf_created_at`             | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`        | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`               | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`            | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `time`                    | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`           | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id` | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`      | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                      |
| `experiment_step_api_id`  | `string`, `null`    | ID da API da etapa da experiência à qual esse evento pertence                  |
| `in_control_group`        | `boolean`, `null`   | True se o usuário estiver inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`                     | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`                     | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`                        | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu       |
| `channel`                              | `string`, `null`    | Canal de mensagens ao qual esse evento pertence (e-mail, push, etc.)          |
| `gender`                               | `string`, `null`    | [Sexo do usuário                                             |
| `country`                              | `string`, `null`    | [País do usuário                                            |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`, `null`    | [Idioma do usuário                                           |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`, `null`    | ID do Braze do usuário que realizou esse evento                        |
| `external_user_id`                     | `string`, `null`    | [ID de usuário externo do usuário                                   |
| `device_id`                            | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                        |
| `app_group_api_id`                     | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                         |
| `time`                                 | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`, `null`    | (Apenas para uso no Braze) ID do Canvas ao qual esse evento pertence          |
| `canvas_api_id`                        | `string`, `null`    | ID da API do Canvas ao qual esse evento pertence                           |
| `canvas_variation_api_id`              | `string`, `null`    | ID da API da variação do Canvas à qual esse evento pertence                 |
| `canvas_step_api_id`                   | `string`, `null`    | ID da API da etapa do Canvas à qual esse evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu       |
| `gender`                               | `string`, `null`    | [Sexo do usuário                                             |
| `country`                              | `string`, `null`    | [País do usuário                                            |
| `timezone`                             | `string`, `null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`, `null`    | [Idioma do usuário                                           |
| `revenue`                              | `int`, `null`       | Valor da receita gerada em dólares americanos, exibido como centavos               |
| `sf_created_at`                        | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Mensagens

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`content_card_id` | `string` | ID do cartão que gerou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`content_card_id` | `string` | ID do cartão que gerou esse evento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`sending_ip` | `null,` `string` | Endereço IP do qual foi feito o envio do e-mail
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,` `string` | [PII] O código de motivo SMTP e a mensagem amigável recebida para esse evento de rejeição
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_drop` | `null, boolean` | Indica que esse evento conta como um evento de queda
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`url` | `null,` `string` | URL em que o usuário clicou
`user_agent` | `null,` `string` | Agente do usuário no qual o clique ocorreu
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`link_id` | `null,` `string` | ID exclusivo para o link que foi clicado, conforme criado pelo Braze
`link_alias` | `null,` `string` | Alias associado a essa ID de link
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`sending_ip` | `null,` `string` | Endereço IP do qual o e-mail foi enviado
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`user_agent` | `null,` `string` | Agente do usuário no qual ocorreu o relatório de spam
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`user_agent` | `null,` `string` | Agente do usuário no qual a abertura ocorreu
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`machine_open` | `null,` `string` | Preenchido como 'true' se o evento de abertura for acionado sem a participação do usuário, por exemplo, por um dispositivo Apple com a Proteção de privacidade de e-mail ativada. O valor pode mudar ao longo do tempo para fornecer mais granularidade.
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`message_extras` | `null,` `string` | [PII] Uma cadeia de caracteres JSON dos pares de valores-chave marcados durante a renderização do Liquid
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`sending_ip` | `null,` `string` | Endereço IP do qual foi feito o envio do e-mail
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,` `string` | [PII] O código de motivo SMTP e a mensagem amigável recebida para esse evento de rejeição
`esp` | `null,` `string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,` `string` | Domínio de envio do e-mail
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`email_address` | `string` | Endereço de e-mail do usuário [PII]
`ip_pool` | `null,` `string` | Pool de IPs a partir do qual o envio de e-mail foi feito
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`version` | `string` | Qual versão da mensagem in-app, antiga ou acionada
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | transportadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
`version` | `string` | qual versão da mensagem in-app, antiga ou acionada
`button_id` | `null,` `string` | ID do botão clicado, se esse clique representar um clique em um botão
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | transportadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
`version` | `string` | qual versão da mensagem in-app, antiga ou acionada
`ad_id` | `null,` `string` | Identificador de publicidade [PII]
`ad_id_type` | `null,` `string` | Um de `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | transportadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | transportadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`card_api_id` | `null,` `string` | ID da API do cartão
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | resolução do dispositivo
`carrier` | `null,` `string` | transportadora do dispositivo
`browser` | `null,` `string` | navegador do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que fizemos uma tentativa de entrega para
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`push_token` | `null,` `string` | Token de envio que foi devolvido
`device_id` | `null,` `string` | `device_id` para o qual fizemos uma tentativa de entrega que foi devolvida
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`platform` | `null,` `string` | Plataforma do dispositivo
`ad_id` | `null,` `string` | ID de publicidade [PII] do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`ad_id` | `null,` `string` | ID de publicidade [PII] do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`device_id` | `null,` `string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,` `string` | Versão do Braze SDK em uso durante o evento
`platform` | `null,` `string` | Plataforma do dispositivo
`os_version` | `null,` `string` | Versão do sistema operacional do dispositivo
`device_model` | `null,` `string` | Modelo do dispositivo
`resolution` | `null,` `string` | Resolução do dispositivo
`carrier` | `null,` `string` | Transportadora do dispositivo
`browser` | `null,` `string` | Navegador do dispositivo
`button_string` | `null,` `string` | Identificador (button_string) do botão de notificação push clicado. Nulo se não for um clique de botão
`button_action_type` | `null,` `string` | Tipo de ação do botão de notificação por push. Um de [URI, DEEP_LINK, NONE, CLOSE]. nulo se não for um clique de botão
`slide_id` | `null,` `string` | Identificador de slide do slide do carrossel de push em que o usuário clica
`slide_action_type` | `null,` `string` | Tipo de ação do slide do carrossel de empurrar
`ad_id` | `null,` `string` | ID de publicidade [PII] do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`push_token` | `null,` `string` | Push token de que fizemos uma tentativa de entrega para
`device_id` | `null,` `string` | `device_id` que fizemos uma tentativa de entrega para
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`app_api_id` | `null,` `string` | ID da API do aplicativo no qual esse evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`ad_id` | `null,` `string` | ID de publicidade [PII] do dispositivo para o qual fizemos uma tentativa de entrega
`ad_id_type` | `null,` `string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento está ou não ativado para publicidade
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
`error` | `null,` `string` | nome do erro
`provider_error_code` | `null,` `string` | código de erro do provedor de serviços de SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `null,` `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho associado ao número de telefone de entrada
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`user_phone_number` | `string` | [PII] o número de telefone do usuário do qual a mensagem foi recebida
`subscription_group_id` | `null,` `string` | ID do grupo de assinaturas visado por essa mensagem SMS
`subscription_group_api_id` | `null,` `string` | ID da API do grupo de assinaturas direcionado para essa mensagem SMS
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`action` | `string` | Ação tomada em resposta a essa mensagem. Por exemplo, `Subscribed`, `Unsubscribed`, ou `None`.
`message_body` | `string` | Resposta do usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem à qual esse evento pertence
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas à qual esse evento pertence
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
`error` | `null,` `string` | nome do erro
`provider_error_code` | `null,` `string` | código de erro do provedor de serviços de SMS
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`subscription_group_api_id` | `null,` `string` | ID externa do grupo de assinaturas
`category` | `null,` `string` | Nome da categoria da palavra-chave, preenchido apenas para mensagens de resposta automática: 'Opt-in', 'Opt-out', 'Help' ou valor personalizado
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `null,` `string` | Braze ID do usuário visado por short_url, null se short_url não usou o rastreamento de cliques do usuário
`external_user_id` | `null,` `string` | [PII] ID externa do usuário visado por short_url, se houver, nula se short_url não tiver usado o rastreamento de cliques do usuário
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho usado para gerar short_url
`time` | `int` | Registro de data e hora Unix no qual short_url foi clicado
`timezone` | `null,` `string` | Fuso horário do usuário
`campaign_id` | `null,` `string` | Braze ID da campanha para a qual short_url foi gerado, nulo se não for de uma campanha
`campaign_api_id` | `null,` `string` | ID da API da campanha para a qual short_url foi gerado, nulo se não for de uma campanha
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem para a qual short_url foi gerada, nula se não for de uma campanha
`canvas_id` | `null,` `string` | Braze ID do Canvas short_url foi gerado para, nulo se não for de um Canvas
`canvas_api_id` | `null,` `string` | ID da API do Canvas para o qual short_url foi gerado, nulo se não for de um Canvas
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas para a qual short_url foi gerado, nulo se não for de um Canvas
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas para a qual short_url foi gerado, nulo se não for de um Canvas
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas short_url foi gerada para, nula se não for de um Canvas
`url` | `string` | URL original contido na mensagem para a qual é redirecionado por short_url
`short_url` | `string` | URL encurtado que foi clicado
`user_agent` | `null,` `string` | agente do usuário solicitando short_url
`user_phone_number` | `string` | [PII] o número de telefone do usuário
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`send_id` | `null,` `string` | ID de envio de mensagem à qual essa mensagem pertence
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`gender` | `null,` `string` | [Sexo do usuário
`country` | `null,` `string` | [País do usuário
`timezone` | `null,` `string` | Fuso horário do usuário
`language` | `null,` `string` | [Idioma do usuário
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | 	`null,` `string` | Número de telefone [PII] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`abort_type` | `null,` `string` | Tipo de aborto, uma das opções: `liquid_abort_message` ou `rate_limit`
`abort_log` | `null,` `string` | [Mensagem de registro descrevendo os detalhes da interrupção (máximo de 2.000 caracteres)
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`provider_error_code` | `null,` `string` | Código de erro do WhatsApp
`provider_error_title` | `null, ` `string` | Título de erro do WhatsApp
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`user_phone_number` | `string` | [PII] o número de telefone do usuário do qual a mensagem foi recebida
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`message_body` | `string` | Resposta do usuário
`quick_reply_text` | `string` | Texto do botão pressionado pelo usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`action` | `string` | Ação tomada em resposta a essa mensagem. Por exemplo, `Subscribed`, `Unsubscribed`, ou `None`.
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string` | Número de telefone [PII] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | Número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Registro de data e hora Unix em que o evento ocorreu
`to_phone_number` | `null,` `string`	| Número de telefone [PII] do destinatário
`user_id` | `string` | ID do Braze do usuário que realizou esse evento
`external_user_id` | `null,` `string` | [ID de usuário externo do usuário
`device_id` | `null,` `string` | `device_id` que está vinculado a esse usuário se o usuário for anônimo
`timezone` | `null,` `string` | Fuso horário do usuário
`from_phone_number` | `null,` `string` | número de telefone do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,` `string` | ID do espaço de trabalho ao qual esse usuário pertence
`app_group_api_id` | `null,` `string` | ID da API do espaço de trabalho ao qual esse usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de assinatura
`campaign_id` | `null,` `string` | ID do Braze de uso interno da campanha à qual esse evento pertence
`campaign_api_id` | `null,` `string` | ID da API da campanha à qual esse evento pertence
`message_variation_api_id` | `null,` `string` | ID da API da variação de mensagem que esse usuário recebeu
`canvas_id` | `null,` `string` | ID do brasão de uso interno do Canvas ao qual esse evento pertence
`canvas_api_id` | `null,` `string` | ID da API do Canvas ao qual esse evento pertence
`canvas_variation_api_id` | `null,` `string` | ID da API da variação do Canvas à qual esse evento pertence
`canvas_step_api_id` | `null,` `string` | ID da API da etapa do Canvas à qual esse evento pertence
`canvas_step_message_variation_api_id` | `null,` `string` | ID da API da variação da mensagem da etapa do Canvas que esse usuário recebeu
`dispatch_id` | `null,` `string` | ID do despacho ao qual essa mensagem pertence
`message_extras` | `null,` `string` | [PII] Uma cadeia de caracteres JSON dos pares de valores-chave marcados durante a renderização do Liquid
`sf_created_at` | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuários

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Campo                       | Tipo                     | Descrição                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | ID globalmente exclusivo para esse evento                  |
| `app_group_id`              | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence      |
| `app_group_api_id`          | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence       |
| `user_id`                   | `string`, `null`    | ID do Braze do usuário que realizou esse evento      |
| `external_user_id`          | `string`, `null`    | [ID de usuário externo do usuário                 |
| `time`                      | `int`, `null`       | Registro de data e hora Unix em que o evento ocorreu         |
| `random_bucket_number`      | `int`, `null`       | Número atual do intervalo aleatório atribuído ao usuário  |
| `prev_random_bucket_number` | `int`, `null`       | Número de balde aleatório anterior atribuído ao usuário |
| `sf_created_at`             | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Campo              | Tipo                     | Descrição                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID globalmente exclusivo para esse evento                             |
| `user_id`          | `string`, `null`    | ID do Braze do usuário que foi excluído                          |
| `app_group_id`     | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                 |
| `app_group_api_id` | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                  |
| `time`             | `int`, `null`       | Registro de data e hora Unix no qual a solicitação de exclusão de usuário foi processada |
| `sf_created_at`    | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Campo              | Tipo                     | Descrição                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | ID globalmente exclusivo para esse evento                                             |
| `user_id`          | `string`, `null`    | ID do Braze do usuário que ficou órfão                                         |
| `external_user_id` | `string`, `null`    | [ID de usuário externo do usuário                                            |
| `device_id`        | `string`, `null`    | ID do dispositivo que está vinculado a esse usuário, se o usuário for anônimo          |
| `app_group_id`     | `string`, `null`    | ID do Braze do espaço de trabalho ao qual esse usuário pertence                                 |
| `app_group_api_id` | `string`, `null`    | ID da API do espaço de trabalho ao qual esse usuário pertence                                  |
| `app_api_id`       | `string`, `null`    | ID da API do aplicativo ao qual o usuário órfão pertencia                               |
| `time`             | `int`, `null`       | Registro de data e hora Unix em que o usuário ficou órfão                                 |
| `orphaned_by_id`   | `string`, `null`    | ID do Braze do usuário cujo perfil foi mesclado com o perfil do usuário órfão |
| `sf_created_at`    | `timestamp`, `null` | Quando esse evento foi registrado pela Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
