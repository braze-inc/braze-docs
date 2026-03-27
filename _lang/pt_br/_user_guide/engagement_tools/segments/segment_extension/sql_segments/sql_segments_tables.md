---
nav_title: "Referência de tabela SQL"
article_title: Referência de tabela SQL
page_order: 3
page_type: reference
toc_headers: h2
description: "Esta página é uma referência das tabelas e colunas SQL do Snowflake usadas no Query Builder, nas extensões de segmento SQL e no Snowflake Data Sharing."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# Referência de tabela SQL

Esta página é uma referência das tabelas e colunas SQL do Snowflake disponíveis nas seguintes ferramentas da Braze:

- [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/)
- [Extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)
- [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

A maioria das tabelas está disponível nas três ferramentas. As tabelas marcadas como **Somente Snowflake Data Sharing** são exclusivas do Snowflake Data Sharing e não estão acessíveis no Query Builder ou nas extensões de segmento SQL.

{% alert tip %}
Essas tabelas SQL correspondem aos eventos documentados no [glossário de eventos do Currents]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Por exemplo, a tabela SQL `USERS_MESSAGES_EMAIL_SEND_SHARED` corresponde ao evento do Currents `users.messages.email.Send`. Se você precisar de esquemas de eventos JSON ou formatos específicos de parceiros (Amplitude, Mixpanel, Segment), consulte o glossário do Currents.
{% endalert %}

## Sumário

Tabela | Descrição
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Quando um agente do Agent Console é executado (**somente Snowflake Data Sharing**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Quando uma ferramenta é executada (**somente Snowflake Data Sharing**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Itens de catálogo não excluídos
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Quando uma campanha é alterada (**somente Snowflake Data Sharing**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Quando um Canvas é alterado (**somente Snowflake Data Sharing**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Quando o grupo de controle global é alterado
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Quando um usuário realiza um evento personalizado
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Quando um usuário instala um app e a instalação é atribuída a um parceiro
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Quando um usuário registra um local
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Quando um usuário faz uma compra
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Quando um usuário desinstala um app
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Quando um usuário faz upgrade do app
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Quando um usuário tem sua primeira sessão
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Quando um usuário visualiza o News Feed
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Quando um usuário encerra uma sessão em um app
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Quando um usuário inicia uma sessão em um app
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Quando um usuário aciona uma área de geofence (por exemplo, quando entra ou sai de uma geofence). Esse evento foi agrupado com outros eventos e recebido pelo endpoint padrão de eventos, portanto pode não ter sido recebido pelo endpoint em tempo real.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Quando um usuário aciona uma área de geofence (por exemplo, quando entra ou sai de uma geofence). Esse evento foi recebido pelo endpoint dedicado de geofence e, portanto, é recebido em tempo real assim que o dispositivo do usuário detecta que acionou uma geofence. <br><br>Além disso, devido ao limite de taxa no endpoint de geofence, é possível que alguns eventos de geofence não sejam refletidos como RecordEvent. No entanto, todos os eventos de geofence são representados por DataEvent (mas potencialmente com algum atraso devido ao agrupamento).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Quando um token push-to-start de Live Activity é alterado
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Quando um token de atualização de Live Activity é alterado
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Quando o estado de um token de notificação por push é alterado
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Quando um usuário é inscrito ou tem a inscrição cancelada globalmente em um canal, como e-mail
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Quando um usuário é inscrito ou tem a inscrição cancelada em um grupo de inscrições
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Quando um usuário converte em uma campanha
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Quando um usuário é inscrito no grupo de controle de uma campanha
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Quando um usuário atinge o limite de frequência de uma campanha
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período de conversão primária
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Quando um usuário avança para uma etapa do Canvas
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Quando um usuário converte em um evento de conversão do Canvas
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Quando um usuário entra em um Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Quando um usuário sai de um Canvas porque corresponde aos critérios de saída de público
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Quando um usuário sai de um Canvas porque realizou um evento de exceção
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Quando um usuário converte em uma etapa de Experimento do Canvas
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Quando um usuário entra em uma jornada de etapa de Experimento
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Quando um usuário atinge o limite de frequência de uma etapa do Canvas
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Quando um usuário gera receita dentro do período do evento de conversão primária
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Uma mensagem de banner originalmente programada foi cancelada por algum motivo
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Quando um usuário clica em um banner
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Quando um usuário visualiza um banner
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Uma mensagem de Content Card originalmente programada foi cancelada por algum motivo.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Quando um usuário clica em um Content Card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Quando um usuário descarta um Content Card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um Content Card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Quando enviamos um Content Card para um usuário
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Uma mensagem de e-mail originalmente programada foi cancelada por algum motivo.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Um prestador de serviço de e-mail retornou um hard bounce. Um hard bounce indica uma falha permanente de entregabilidade.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Quando um usuário clica em um link em um e-mail
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Quando um e-mail é adiado
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Quando um e-mail é entregue
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Quando um e-mail é marcado como spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Quando um usuário abre um e-mail
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Quando enviamos um e-mail para um usuário
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Quando um e-mail sofre soft bounce
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Quando um usuário cancela a inscrição de e-mail
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Quando uma mensagem de e-mail é reenviada após ser despriorizada ou ter atingido o limite de frequência (**somente Snowflake Data Sharing**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Quando um usuário visualiza uma Feature Flag
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Uma mensagem no app originalmente programada foi cancelada por algum motivo.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Quando um usuário clica em uma mensagem no app
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Quando um usuário visualiza uma mensagem no app
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Quando uma mensagem LINE programada não pode ser entregue, antes do envio ao LINE
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Quando um usuário clica em um link em uma mensagem LINE
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Quando uma mensagem LINE é recebida de um usuário
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Quando uma mensagem LINE é enviada ao LINE
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Quando uma mensagem LINE é reenviada após ser despriorizada ou ter atingido o limite de frequência (**somente Snowflake Data Sharing**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Quando uma Live Activity tem um evento de resultado
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Quando uma mensagem de Live Activity é enviada
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Um cartão do News Feed originalmente programado foi cancelado por algum motivo
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Quando um usuário clica em um cartão do News Feed
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Quando um usuário visualiza um cartão do News Feed
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Uma notificação por push originalmente programada foi cancelada por algum motivo.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Quando uma notificação por push sofre bounce
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Quando um usuário abre o app após receber uma notificação sem clicar nela
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Quando um usuário recebe uma notificação por push enquanto o app está aberto. <br><br>Esse evento não é compatível com o [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) e está descontinuado no [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Quando um usuário abre uma notificação por push ou clica em um botão da notificação por push (incluindo um botão FECHAR que NÃO abre o app). <br><br> As ações de botão de push têm múltiplos resultados. As ações Não, Recusar e Cancelar são "cliques", e as ações Aceitar são "aberturas". Ambas são representadas nesta tabela, mas podem ser diferenciadas na coluna **BUTTON_ACTION_TYPE**. Por exemplo, uma consulta pode ser usada para agrupar por um `BUTTON_ACTION_TYPE` que não seja Não, Recusar ou Cancelar.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Quando enviamos uma notificação por push para um usuário
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Quando um envio de RCS é interrompido devido a um erro detectado na Braze e a mensagem é descartada
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Quando o usuário final interage com uma mensagem RCS tocando ou clicando em um elemento da interface
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Quando uma mensagem RCS é entregue com sucesso ao dispositivo móvel do usuário final
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Quando a Braze recebe uma mensagem RCS originada do usuário final
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Quando o usuário final abre uma mensagem RCS em seu dispositivo
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Quando uma mensagem RCS não é entregue devido a intervenção da operadora
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Quando uma mensagem RCS é enviada dos sistemas da Braze para os parceiros de entrega final
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Uma mensagem SMS originalmente programada foi cancelada por algum motivo.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Quando uma mensagem SMS é enviada para a operadora
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Quando uma mensagem SMS é entregue
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Quando a Braze não consegue entregar a mensagem SMS ao prestador de serviço de SMS
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Quando uma mensagem SMS é recebida de um usuário
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Quando uma mensagem SMS não é entregue a um usuário
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Quando uma mensagem SMS é enviada
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Quando um usuário clica em uma URL encurtada da Braze incluída em uma mensagem SMS
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Quando uma mensagem SMS é reenviada após ser despriorizada ou ter atingido o limite de frequência (**somente Snowflake Data Sharing**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Uma mensagem de webhook originalmente programada foi cancelada por algum motivo
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Quando uma mensagem de webhook é entregue, mas falha com uma resposta de erro do endpoint
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Quando enviamos um webhook para um usuário
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Quando uma mensagem de webhook é reenviada após ser despriorizada ou ter atingido o limite de frequência (**somente Snowflake Data Sharing**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Uma mensagem de WhatsApp originalmente programada foi cancelada por algum motivo
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Quando um usuário clica em um link ou botão em uma mensagem de WhatsApp
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Quando uma mensagem de WhatsApp é entregue
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Quando uma mensagem de WhatsApp não é entregue a um usuário
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Quando uma mensagem de WhatsApp é recebida de um usuário
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Quando um usuário abre uma mensagem de WhatsApp
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Quando enviamos uma mensagem de WhatsApp para um usuário
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Quando uma mensagem de WhatsApp é reenviada após ser despriorizada ou ter atingido o limite de frequência (**somente Snowflake Data Sharing**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Quando o número de bucket aleatório de um usuário é alterado
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Quando um usuário é excluído por solicitação do cliente
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Quando um usuário é mesclado com o perfil de outro usuário e o perfil original se torna órfão
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | Snapshots de app (**somente Snowflake Data Sharing**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Snapshots de variação de mensagem de campanha (**somente Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Snapshots de etapa do Canvas Flow (**somente Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Snapshots de etapa do Canvas (**somente Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Snapshots de variação do Canvas (**somente Snowflake Data Sharing**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Snapshots de etapa de Experimento (**somente Snowflake Data Sharing**)


## Agent Console {#agent-console}

{% alert note %}
As tabelas do Agent Console estão disponíveis somente no Snowflake Data Sharing.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`invocation_id` | `string` | ID globalmente exclusivo para essa mensagem
`request_id` | `string` | ID exclusivo para essa solicitação LLM geral e execução completa
`duration` | `int` | Duração da sessão em segundos
`prompt_tokens` | `int` | Quantos tokens de prompt essa solicitação usou
`completion_tokens` | `int` | Quantos tokens de conclusão essa solicitação usou
`total_tokens` | `int` | Quantos tokens no total essa solicitação usou
`cache_tokens` | `int` | Quantos tokens em cache essa solicitação usou
`reasoning_tokens` | `int` | Quantos tokens de raciocínio essa solicitação usou
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`agent_id` | `string` | ID BSON do CustomerDefinedAgent
`agent_name` | `string` | Nome do CustomerDefinedAgent
`model_provider` | `string` | Nome do provedor do modelo LLM
`model_name` | `string` | Nome do modelo LLM usado nessa solicitação
`provider_request_id` | `string` | Qualquer ID de solicitação fornecido pelo provedor do modelo para a chamada de API
`cache_hit` | `boolean` | Se essa solicitação usou o cache para retornar a resposta
`llm_owned_by_customer` | `boolean` | Se verdadeiro, a chave de API do cliente foi usada; se falso, a chave da Braze foi usada
`is_error` | `boolean` | Se essa solicitação resultou em erro
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas ao qual este evento pertence
`user_id` | `string` | [IPI] ID de usuário da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`input` | `null,`&nbsp;`string` | [IPI] Entrada para o LLM
`output` | `null,`&nbsp;`string` | [IPI] Resposta do LLM
`invocation_source` | `null,`&nbsp;`string` | Qual objeto ruby invocou a solicitação LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`tool_call_id` | `string` | ID globalmente exclusivo para essa chamada de ferramenta
`duration` | `int` | Duração da sessão em segundos
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`agent_id` | `string` | ID BSON do CustomerDefinedAgent
`agent_name` | `string` | Nome do CustomerDefinedAgent
`is_error` | `boolean` | Se essa solicitação resultou em erro
`tool_name` | `string` | Nome da ferramenta
`tool_arguments` | `null,`&nbsp;`string` | [IPI] JSON dos argumentos da ferramenta
`invocation_source` | `null,`&nbsp;`string` | Qual objeto ruby invocou a solicitação LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Catálogos

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Campo | Tipo | Descrição
------|------|------------
`catalog_id` | `string` | ID BSON do catálogo
`item_id` | `string` | ID BSON do item do catálogo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app
`field_name` | `null,`&nbsp;`string` | Nome do campo
`field_value` | `null,`&nbsp;`string` | Valor do campo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Changelogs

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`random_bucket_number` | `null, int` | Novo número de bucket aleatório
`global_control_group` | `null, boolean` | Com essa mudança, o número do bucket é incluído como grupo de controle global
`previous_global_control_group` | `null, boolean` | Antes dessa mudança, o número do bucket era incluído como grupo de controle global, mas não é mais
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% alert note %}
Esta tabela está disponível somente no Snowflake Data Sharing.
{% endalert %}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API da campanha
`name` | `null,`&nbsp;`string` | Nome da campanha
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamentos de conversão da campanha
`actions` | `null,`&nbsp;`string` | Ações da campanha
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% alert note %}
Esta tabela está disponível somente no Snowflake Data Sharing.
{% endalert %}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API do Canvas
`name` | `null,`&nbsp;`string` | Nome do Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamentos de conversão do Canvas
`variations` | `null,`&nbsp;`string` | Variações do Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Comportamentos

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou o evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta ação ocorreu
`time` | `int` | Timestamp Unix em que o usuário realizou o evento
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento personalizado ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`name` | `string` | Nome do evento personalizado
`properties` | `string` | Propriedades personalizadas do evento armazenadas como uma string codificada em JSON
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que instalou
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o usuário instalou
`source` | `string` | A origem da atribuição
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que registra o local
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este local foi registrado
`time` | `int` | Timestamp Unix em que o local foi registrado
`latitude` | `float` | [IPI] Latitude do local registrado
`longitude` | `float` | [IPI] Longitude do local registrado
`altitude` | `null, float` | [IPI] Altitude do local registrado
`ll_accuracy` | `null, float` | Precisão de latitude e longitude do local registrado
`alt_accuracy` | `null, float` | Precisão de altitude do local registrado
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o local foi registrado
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso quando o local foi registrado
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que fez a compra
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual a compra ocorreu
`time` | `int` | Timestamp Unix em que o usuário fez a compra
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual a compra ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante a compra
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`product_id` | `string` | ID do produto comprado
`price` | `float` | Preço da compra
`currency` | `string` | Moeda da compra
`properties` | `string` | Propriedades personalizadas da compra armazenadas como uma string codificada em JSON
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que desinstalou
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app que foi desinstalado
`time` | `int` | Timestamp Unix em que o usuário desinstalou
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que fez upgrade do app
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app que o usuário atualizou
`time` | `int` | Timestamp Unix em que o usuário fez upgrade do app
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o usuário fez upgrade do app
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`old_app_version` | `null,`&nbsp;`string` | Versão anterior do app
`new_app_version` | `null,`&nbsp;`string` | Nova versão do app
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realiza esta ação
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta sessão ocorreu
`time` | `int` | Timestamp Unix em que a sessão começou
`session_id` | `string` | UUID da sessão
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante a sessão
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realiza esta ação
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta sessão ocorreu
`time` | `int` | Timestamp Unix em que a sessão terminou
`duration` | `null, float` | Duração da sessão em segundos
`session_id` | `string` | UUID da sessão
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante a sessão
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realiza esta ação
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta sessão ocorreu
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que a sessão começou
`session_id` | `string` | UUID da sessão
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual a sessão ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante a sessão
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou o evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta ação ocorreu
`time` | `int` | Timestamp Unix em que o usuário realizou o evento
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento personalizado ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi acionado. (por exemplo, 'enter' ou 'exit')
`location_set_id` | `string` | O ID do conjunto de locais da geofence que foi acionada
`geofence_id` | `string` | O ID da geofence que foi acionada
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou o evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual esta ação ocorreu
`time` | `int` | Timestamp Unix em que o usuário realizou o evento
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento personalizado ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`event_type` | `string` | Que tipo de evento de geofence foi acionado. (por exemplo, 'enter' ou 'exit')
`location_set_id` | `string` | O ID do conjunto de locais da geofence que foi acionada
`geofence_id` | `string` | O ID da geofence que foi acionada
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo da Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push-to-start da Live Activity
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplica-se apenas a tokens por push iOS, 1 para desenvolvimento, 2 para produção
`push_token_state_change_type` | `null,`&nbsp;`string` | Uma descrição do tipo de mudança de estado do token por push
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID de usuário da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`activity_id` | `null,`&nbsp;`string` | Identificador da Live Activity
`update_token` | `null,`&nbsp;`string` | Token de atualização da Live Activity
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplica-se apenas a tokens por push iOS, 1 para desenvolvimento, 2 para produção
`push_token_state_change_type` | `null,`&nbsp;`string` | Uma descrição do tipo de mudança de estado do token por push
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`time_ms` | `int` | Horário em milissegundos em que o evento ocorreu
`user_id` | `string` | ID de usuário da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`push_token` | `null,`&nbsp;`string` | Token por push do evento
`push_token_created_at` | `null, int` | Timestamp UNIX em que o token por push foi criado
`push_token_updated_at` | `null, int` | Timestamp UNIX em que o token por push foi atualizado pela última vez
`push_token_foreground_push_disabled` | `null, boolean` | Flag de push em primeiro plano desativado do token por push
`push_token_device_id` | `null,`&nbsp;`string` | ID do dispositivo do token por push
`push_token_provisionally_opted_in` | `null, boolean` | Flag de aceitação provisória do token por push
`ios_push_token_apns_gateway` | `null, int` | Gateway APNS do token por push, aplica-se apenas a tokens por push iOS, 1 para desenvolvimento, 2 para produção
`web_push_token_public_key` | `null,`&nbsp;`string` | Chave pública do token por push, aplica-se apenas a tokens de push para a web
`web_push_token_user_auth` | `null,`&nbsp;`string` | Autenticação do usuário do token por push, aplica-se apenas a tokens de push para a web
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | Chave pública VAPID do token por push, aplica-se apenas a tokens de push para a web
`push_token_state_change_type` | `null,`&nbsp;`string` | Uma descrição do tipo de mudança de estado do token por push
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário afetado
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`email_address` | `null,`&nbsp;`string` | [IPI] Endereço de e-mail do usuário
`state_change_source` | `null,`&nbsp;`string` | Origem da mudança de estado (REST, SDK, Dashboard, etc.)
`subscription_status` | `string` | Status da inscrição: 'Subscribed', 'Unsubscribed' ou 'Opted In'
`channel` | `null,`&nbsp;`string` | Canal do estado de inscrição global, como e-mail
`time` | `int` | Timestamp Unix em que o estado da inscrição foi alterado
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app ao qual o evento pertence
`campaign_id` | `null,`&nbsp;`string` | ID interno da Braze da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem à qual este evento pertence
`canvas_id` | `null,`&nbsp;`string` | ID interno da Braze do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas ao qual este evento pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem que originou esta ação de mudança de estado de inscrição
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`channel_identifier` | `null,`&nbsp;`string` | [IPI] O identificador do usuário no canal ao qual o evento se refere.
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário afetado
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`email_address` | `null,`&nbsp;`string` | [IPI] Endereço de e-mail do usuário
`phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário no formato e164
`app_api_id` | `null,`&nbsp;`string` | ID da API do app ao qual o evento pertence
`campaign_id` | `null,`&nbsp;`string` | ID interno da Braze da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem à qual este evento pertence
`canvas_id` | `null,`&nbsp;`string` | ID interno da Braze do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas ao qual este evento pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`channel` | `null,`&nbsp;`string` | Canal: 'email' ou 'sms', dependendo do tipo de canal do grupo de inscrições
`subscription_status` | `string` | Status da inscrição: 'Subscribed', 'Unsubscribed' ou 'Opted In'
`time` | `int` | Timestamp Unix em que o estado da inscrição foi alterado
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem que originou esta ação de mudança de estado de inscrição
`state_change_source` | `null,`&nbsp;`string` | Origem da mudança de estado (REST, SDK, Dashboard, etc.)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`channel_identifier` | `null,`&nbsp;`string` | [IPI] O identificador do usuário no canal ao qual o evento se refere.
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campanhas

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`conversion_behavior_index` | `null, int` | Índice do comportamento de conversão
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`channel` | `null,`&nbsp;`string` | Canal ao qual este evento pertence
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para esse evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`revenue` | `long` | Valor da receita em USD gerada, em centavos
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence        |         
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | Tipo de evento de progressão de etapa |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Se esta é uma entrada em uma primeira etapa de um Canvas        |
| `exit_reason`                          | `string`,&nbsp;`null`    | Se for uma saída, o motivo pelo qual o usuário saiu do Canvas durante a etapa                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Identificador exclusivo para esta instância de um usuário em um Canvas  |
| `next_step_id`                         | `string`,&nbsp;`null`    | ID BSON da próxima etapa no Canvas |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | ID da API da próxima etapa no Canvas |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Campo                                  | Tipo                     | Descrição                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | ID da API do app no qual este evento ocorreu                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Tipo de evento de conversão que o usuário realizou, onde "0" é uma conversão primária e "1" é uma conversão secundária |
| `gender`                               | `string`,&nbsp;`null`    | [IPI] Gênero do usuário                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [IPI] País do usuário                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | Fuso horário do usuário                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [IPI] Idioma do usuário                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo |
| `app_group_id`            | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                         |
| `time`                    | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Descontinuado] ID da API da etapa do Canvas ao qual este evento pertence         |
| `gender`                  | `string`,&nbsp;`null`    | [IPI] Gênero do usuário                                             |
| `country`                 | `string`,&nbsp;`null`    | [IPI] País do usuário                                            |
| `timezone`                | `string`,&nbsp;`null`    | Fuso horário do usuário                                                 |
| `language`                | `string`,&nbsp;`null`    | [IPI] Idioma do usuário                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Verdadeiro se o usuário foi inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                         |
| `time`                    | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                         |
| `time`                    | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Campo                       | Tipo                     | Descrição                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                                                              |
| `app_group_id`              | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                                                                   |
| `time`                      | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | ID da API do app no qual este evento ocorreu                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | ID da API da etapa de Experimento ao qual este evento pertence                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Tipo de evento de conversão que o usuário realizou, onde "0" é uma conversão primária e "1" é uma conversão secundária |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ID da API da divisão do experimento na qual o usuário foi inscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Campo                     | Tipo                     | Descrição                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                 | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `time`                    | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | ID da API da etapa de Experimento ao qual este evento pertence                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Verdadeiro se o usuário foi inscrito no grupo de controle                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |

| `experiment_split_api_id` | `string`,&nbsp;`null` | ID da API da divisão do experimento na qual o usuário foi inscrito |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                         |
| `time`                                 | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu       |
| `channel`                              | `string`,&nbsp;`null`    | Canal de envio de mensagens ao qual este evento pertence (e-mail, push, etc.)          |
| `gender`                               | `string`,&nbsp;`null`    | [IPI] Gênero do usuário                                             |
| `country`                              | `string`,&nbsp;`null`    | [IPI] País do usuário                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`,&nbsp;`null`    | [IPI] Idioma do usuário                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Campo                                  | Tipo                     | Descrição                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | ID globalmente exclusivo para esse evento                                    |
| `user_id`                              | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo |
| `app_group_id`                         | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                         |
| `time`                                 | `int`,&nbsp;`null`       | Timestamp Unix em que o evento ocorreu                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Somente para uso interno da Braze) ID do Canvas ao qual este evento pertence          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | ID da API do Canvas ao qual este evento pertence                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | ID da API da variação do Canvas ao qual este evento pertence                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | ID da API da etapa do Canvas ao qual este evento pertence                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu       |
| `gender`                               | `string`,&nbsp;`null`    | [IPI] Gênero do usuário                                             |
| `country`                              | `string`,&nbsp;`null`    | [IPI] País do usuário                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Fuso horário do usuário                                                 |
| `language`                             | `string`,&nbsp;`null`    | [IPI] Idioma do usuário                                           |
| `revenue`                              | `int`,&nbsp;`null`       | Valor da receita gerada em USD, exibido em centavos               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                        |
| `app_api_id` | `string`,&nbsp;`null` | ID da API do app no qual este evento ocorreu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Mensagens


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (até 128 caracteres)
`banner_placement_id` | `null,`&nbsp;`string` | ID de posicionamento do banner especificado pelo cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`button_id` | `null,`&nbsp;`string` | ID do botão clicado, se este clique representa um clique em um botão
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`banner_placement_id` | `null,`&nbsp;`string` | ID de posicionamento do banner especificado pelo cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`banner_placement_id` | `null,`&nbsp;`string` | ID de posicionamento do banner especificado pelo cliente
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`content_card_id` | `string` | ID do cartão que gerou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`content_card_id` | `string` | ID do cartão que gerou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`content_card_id` | `string` | ID do cartão que gerou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`content_card_id` | `string` | ID do cartão que gerou este evento
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`sending_ip` | `null,`&nbsp;`string` | Endereço IP a partir do qual o envio de e-mail foi feito
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,`&nbsp;`string` | [IPI] O código de razão SMTP e a mensagem amigável recebida para este evento de bounce
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`is_drop` | `null, boolean` | Indica que este evento conta como um evento de descarte
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`url` | `null,`&nbsp;`string` | URL em que o usuário clicou
`user_agent` | `null,`&nbsp;`string` | User agent no qual o clique ocorreu
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`link_id` | `null,`&nbsp;`string` | ID exclusivo do link clicado, conforme criado pela Braze
`link_alias` | `null,`&nbsp;`string` | Alias associado a este ID de link
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`is_suspected_bot_click` | `null, boolean` | Se este evento foi processado como um evento de bot
`suspected_bot_click_reason` | `null, object` | Por que este evento foi classificado como bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`email_address` | `null,`&nbsp;`string` | [IPI] Endereço de e-mail do usuário
`recipient_domain` | `null,`&nbsp;`string` | Domínio de e-mail do destinatário
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (Sparkpost, Sendgrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`sending_ip` | `null,`&nbsp;`string` | Endereço IP a partir do qual o envio de e-mail foi feito
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`deferral_reason` | `null,`&nbsp;`string` | [IPI] O código de razão SMTP e a mensagem amigável recebida para este evento de adiamento
`attempt_count` | `null, int` | Número de tentativas feitas para enviar a mensagem
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`sending_ip` | `null,`&nbsp;`string` | Endereço IP a partir do qual o e-mail foi enviado
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`user_agent` | `null,`&nbsp;`string` | User agent no qual o relatório de spam ocorreu
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`user_agent` | `null,`&nbsp;`string` | User agent no qual a abertura ocorreu
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`machine_open` | `null,`&nbsp;`string` | Preenchido com 'true' se o evento de abertura for acionado sem interação do usuário, por exemplo, por um dispositivo Apple com a proteção de privacidade de e-mail ativada. O valor pode mudar ao longo do tempo para fornecer mais granularidade.
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`is_amp` | `null, boolean` | Indica que este é um evento AMP
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`sending_ip` | `null,`&nbsp;`string` | Endereço IP a partir do qual o envio de e-mail foi feito
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`bounce_reason` | `null,`&nbsp;`string` | [IPI] O código de razão SMTP e a mensagem amigável recebida para este evento de bounce
`esp` | `null,`&nbsp;`string` | ESP relacionado ao evento (SparkPost, SendGrid ou Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Domínio de envio do e-mail
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `string` | [IPI] Endereço de e-mail do usuário
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% alert note %}
Esta tabela está disponível apenas no Snowflake Data Sharing.
{% endalert %}

Este evento ocorre quando uma mensagem é despriorizada ou limitada por frequência e é reenviada posteriormente dentro da janela de reenvio configurada.

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | [IPI] ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`retry_type` | `null,`&nbsp;`string` | Tipo de reenvio
`retry_log` | `null,`&nbsp;`string` | Mensagem de registro descrevendo os detalhes do reenvio
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`email_address` | `null,`&nbsp;`string` | [IPI] Endereço de e-mail do usuário
`ip_pool` | `null,`&nbsp;`string` | Pool de IP a partir do qual o envio de e-mail foi feito
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`feature_flag_id_name` | `null,`&nbsp;`string` | O identificador de rollout da Feature Flag
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`version` | `string` | Qual versão da mensagem no app, legada ou disparada
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`version` | `string` | Qual versão da mensagem no app, legada ou disparada
`button_id` | `null,`&nbsp;`string` | ID do botão clicado, se este clique representa um clique em um botão
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`version` | `string` | Qual versão da mensagem no app, legada ou disparada
`ad_id` | `null,`&nbsp;`string` | [IPI] Identificador de publicidade
`ad_id_type` | `null,`&nbsp;`string` | Um entre `ios_idfa`, `google_ad_id`, `windows_ad_id` OU `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado para o dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`locale_key` | `null,`&nbsp;`string` | [IPI] A chave correspondente às traduções (por exemplo, 'en-us') usada para compor esta mensagem (null para padrão).
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (até 128 caracteres)
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`line_channel_id` | `null,`&nbsp;`string` | O ID do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`line_channel_name` | `null,`&nbsp;`string` | O nome do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`native_line_id` | `null,`&nbsp;`string` | [IPI] O ID do LINE do usuário a partir do qual a mensagem foi enviada ou recebida
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`native_line_id` | `null,`&nbsp;`string` | [IPI] O ID do LINE do usuário a partir do qual a mensagem foi enviada ou recebida
`line_channel_id` | `null,`&nbsp;`string` | O ID do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`line_channel_name` | `null,`&nbsp;`string` | O nome do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`is_suspected_bot_click` | `null, boolean` | Se este evento foi processado como um evento de bot
`short_url` | `null,`&nbsp;`string` | URL encurtada que foi clicada
`url` | `null,`&nbsp;`string` | URL em que o usuário clicou
`user_agent` | `null,`&nbsp;`string` | User agent no qual o relatório de spam ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`line_channel_id` | `null,`&nbsp;`string` | O ID do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`line_channel_name` | `null,`&nbsp;`string` | O nome do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`media_id` | `null,`&nbsp;`string` | O ID gerado pelo LINE que pode ser usado para recuperar mídia de entrada do LINE
`message_body` | `null,`&nbsp;`string` | Resposta digitada pelo usuário
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`native_line_id` | `null,`&nbsp;`string` | [IPI] O ID do LINE do usuário a partir do qual a mensagem foi enviada ou recebida
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`line_channel_id` | `null,`&nbsp;`string` | O ID do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`line_channel_name` | `null,`&nbsp;`string` | O nome do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`native_line_id` | `null,`&nbsp;`string` | [IPI] O ID do LINE do usuário a partir do qual a mensagem foi enviada ou recebida
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% alert note %}
Esta tabela está disponível apenas no Snowflake Data Sharing.
{% endalert %}

Este evento ocorre quando uma mensagem é despriorizada ou limitada por frequência e é reenviada posteriormente dentro da janela de reenvio configurada.

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | [IPI] ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`retry_type` | `null,`&nbsp;`string` | Tipo de reenvio
`retry_log` | `null,`&nbsp;`string` | Mensagem de registro descrevendo os detalhes do reenvio
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`line_channel_id` | `null,`&nbsp;`string` | O ID do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`line_channel_name` | `null,`&nbsp;`string` | O nome do canal LINE para o qual a mensagem foi enviada ou do qual foi recebida
`native_line_id` | `null,`&nbsp;`string` | [IPI] O ID do LINE do usuário a partir do qual a mensagem foi enviada ou recebida
`subscription_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de inscrições
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`activity_id` | `null,`&nbsp;`string` | Identificador da Live Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo da Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push to start da Live Activity
`update_token` | `null,`&nbsp;`string` | Token de atualização da Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Tipo de evento da Live Activity. Um entre ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Resultado do evento da Live Activity
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`activity_id` | `null,`&nbsp;`string` | Identificador da Live Activity
`activity_attributes_type` | `null,`&nbsp;`string` | Tipo de atributo da Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Token push to start da Live Activity
`update_token` | `null,`&nbsp;`string` | Token de atualização da Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Tipo de evento da Live Activity. Um entre ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (até 128 caracteres)
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`card_api_id` | `null,`&nbsp;`string` | ID da API do cartão
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo - extraído do user_agent - no qual a abertura ocorreu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` para o qual tentamos fazer a entrega
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`push_token` | `null,`&nbsp;`string` | Token por push que sofreu bounce
`device_id` | `null,`&nbsp;`string` | `device_id` para o qual tentamos fazer a entrega e que sofreu bounce
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] ID de publicidade do dispositivo para o qual tentamos fazer a entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado ou não
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Este evento não é compatível com o [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) e está descontinuado no [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).
{% endalert %}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] ID de publicidade do dispositivo para o qual tentamos fazer a entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado ou não
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`sdk_version` | `null,`&nbsp;`string` | Versão do SDK da Braze em uso durante o evento
`platform` | `null,`&nbsp;`string` | Plataforma do dispositivo
`os_version` | `null,`&nbsp;`string` | Versão do sistema operacional do dispositivo
`device_model` | `null,`&nbsp;`string` | Modelo do dispositivo
`resolution` | `null,`&nbsp;`string` | Resolução do dispositivo
`carrier` | `null,`&nbsp;`string` | Operadora do dispositivo
`browser` | `null,`&nbsp;`string` | Navegador do dispositivo
`button_string` | `null,`&nbsp;`string` | Identificador (button_string) do botão da notificação por push clicado. null se não for de um clique em botão
`button_action_type` | `null,`&nbsp;`string` | Tipo de ação do botão da notificação por push. Um entre [URI, DEEP_LINK, NONE, CLOSE]. null se não for de um clique em botão
`slide_id` | `null,`&nbsp;`string` | Identificador do slide do carrossel push em que o usuário clicou
`slide_action_type` | `null,`&nbsp;`string` | Tipo de ação do slide do carrossel push
`ad_id` | `null,`&nbsp;`string` | [IPI] ID de publicidade do dispositivo para o qual tentamos fazer a entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado ou não
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`push_token` | `null,`&nbsp;`string` | Token por push para o qual tentamos fazer a entrega
`device_id` | `null,`&nbsp;`string` | `device_id` para o qual tentamos fazer a entrega
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`app_api_id` | `null,`&nbsp;`string` | ID da API do app no qual este evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`platform` | `string` | Plataforma do dispositivo
`ad_id` | `null,`&nbsp;`string` | [IPI] ID de publicidade do dispositivo para o qual tentamos fazer a entrega
`ad_id_type` | `null,`&nbsp;`string` | Tipo do ID de publicidade
`ad_tracking_enabled` | `null, boolean` | Se o rastreamento de publicidade está ativado ou não
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`is_sampled` | `null,`&nbsp;`string` | Indica se o envio push foi amostrado e se era esperado um evento de entrega
`locale_key` | `null,`&nbsp;`string` | [IPI] A chave correspondente às traduções (por exemplo, 'en-us') usada para compor esta mensagem (null para padrão).
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (até 128 caracteres)
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`is_suspected_bot_click` | `null, boolean` | Se este evento foi processado como um evento de bot
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`short_url` | `null,`&nbsp;`string` | URL encurtada que foi clicada
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Por que este evento foi classificado como bot
`user_agent` | `null,`&nbsp;`string` | User agent no qual o relatório de spam ocorreu
`user_phone_number` | `null,`&nbsp;`string` | [IPI] O número de telefone do usuário a partir do qual a mensagem foi recebida
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`interaction_type` | `null,`&nbsp;`string` | O tipo de interação que gerou o clique. Exemplos de valores de string: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Detalhes opcionais sobre o elemento clicado, como o texto de uma resposta sugerida ou botão
`element_type` | `null,`&nbsp;`string` | Especifica se um interaction_type comum entre sugestões e botões veio de uma sugestão ou botão. Exemplos: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`url` | `null,`&nbsp;`string` | URL em que o usuário clicou
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário que recebe a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`from_rcs_sender` | `null,`&nbsp;`string` | O ID do remetente RCS ou nome do agente usado para enviar a mensagem
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`action` | `null,`&nbsp;`string` | Ação tomada em resposta a esta mensagem. (por exemplo, Subscribed, Unsubscribed ou None).
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`media_urls` | `null,`&nbsp;`string` | URLs de mídia do usuário
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`user_phone_number` | `null,`&nbsp;`string` | [IPI] O número de telefone do usuário a partir do qual a mensagem foi recebida
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_body` | `null,`&nbsp;`string` | Resposta digitada pelo usuário
`to_rcs_sender` | `null,`&nbsp;`string` | O remetente RCS de entrada para o qual a mensagem foi enviada
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário que recebe a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`error` | `null,`&nbsp;`string` | Nome do erro
`from_rcs_sender` | `null,`&nbsp;`string` | O ID do remetente RCS ou nome do agente usado para enviar a mensagem
`is_sms_fallback` | `null, boolean` | Indica se o fallback por SMS foi tentado para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de entrega de SMS
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`provider_error_code` | `null,`&nbsp;`string` | Código de erro do provedor
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário que recebe a mensagem no formato e.164 (por exemplo, +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`category` | `null,`&nbsp;`string` | Nome da categoria de palavra-chave, preenchido apenas para mensagens de resposta automática: 'opt-in', 'opt-out', 'help' ou valor personalizado
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`from_rcs_sender` | `null,`&nbsp;`string` | O ID do remetente RCS ou nome do agente usado para enviar a mensagem
`message_extras` | `null,`&nbsp;`string` | Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário que recebe a mensagem no formato e.164 (por exemplo, +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se o fallback por SMS foi tentado para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`error` | `null,`&nbsp;`string` | Nome do erro
`provider_error_code` | `null,`&nbsp;`string` | Código de erro do prestador de serviço de SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se o fallback por SMS foi tentado para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `null,`&nbsp;`string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho associado ao número de telefone de entrada
`time` | `int` | Timestamp Unix em que o evento ocorreu
`user_phone_number` | `string` | [IPI] O número de telefone do usuário a partir do qual a mensagem foi recebida
`subscription_group_id` | `null,`&nbsp;`string` | ID do grupo de inscrições direcionado para esta mensagem SMS
`subscription_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de inscrições direcionado para esta mensagem SMS
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`action` | `string` | Ação tomada em resposta a esta mensagem. Por exemplo, `Subscribed`, `Unsubscribed` ou `None`.
`message_body` | `string` | Resposta do usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem à qual este evento pertence
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas à qual este evento pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem SMS foi enviada
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`error` | `null,`&nbsp;`string` | Nome do erro
`provider_error_code` | `null,`&nbsp;`string` | Código de erro do prestador de serviço de SMS
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`is_sms_fallback` | `null, boolean` | Indica se o fallback por SMS foi tentado para esta mensagem RCS rejeitada. Está vinculado/pareado ao evento de entrega de SMS
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`subscription_group_api_id` | `null,`&nbsp;`string` | ID externo do grupo de inscrições
`category` | `null,`&nbsp;`string` | Nome da categoria de palavra-chave, preenchido apenas para mensagens de resposta automática: 'Opt-in', 'Opt-out', 'Help' ou valor personalizado
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `null,`&nbsp;`string` | ID da Braze do usuário direcionado pela short_url, null se a short_url não usou rastreamento de clique do usuário
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário direcionado pela short_url, se existir, null se a short_url não usou rastreamento de clique do usuário
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho usado para gerar a short_url
`time` | `int` | Timestamp Unix em que a short_url foi clicada
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`campaign_id` | `null,`&nbsp;`string` | ID da Braze da campanha para a qual a short_url foi gerada, null se não for de uma campanha
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha para a qual a short_url foi gerada, null se não for de uma campanha
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem para a qual a short_url foi gerada, null se não for de uma campanha
`canvas_id` | `null,`&nbsp;`string` | ID da Braze do Canvas para o qual a short_url foi gerada, null se não for de um Canvas
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas para o qual a short_url foi gerada, null se não for de um Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas para a qual a short_url foi gerada, null se não for de um Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas para a qual a short_url foi gerada, null se não for de um Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas para a qual a short_url foi gerada, null se não for de um Canvas
`url` | `string` | URL original contida na mensagem que é redirecionada pela short_url
`short_url` | `string` | URL encurtada que foi clicada
`user_agent` | `null,`&nbsp;`string` | User agent que solicitou a short_url
`user_phone_number` | `string` | [IPI] O número de telefone do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`is_suspected_bot_click` | `null, boolean` | Se este evento foi processado como um evento de bot
`suspected_bot_click_reason` | `null, object` | Por que este evento foi classificado como bot
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% alert note %}
Esta tabela está disponível apenas no Snowflake Data Sharing.
{% endalert %}

Este evento ocorre quando uma mensagem é despriorizada ou limitada por frequência e é reenviada posteriormente dentro da janela de reenvio configurada.

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | [IPI] ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`subscription_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de inscrições
`retry_type` | `null,`&nbsp;`string` | Tipo de reenvio
`retry_log` | `null,`&nbsp;`string` | Mensagem de registro descrevendo os detalhes do reenvio
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`http_status_code` | `null, int` | Código de status HTTP da resposta
`endpoint_url` | `null,`&nbsp;`string` | A URL do endpoint sendo solicitada
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`content_length` | `null, int` | Tamanho do conteúdo da resposta
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`host` | `null,`&nbsp;`string` | O host da requisição
`id` | `string` | ID globalmente exclusivo para este evento
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`raw_response` | `null,`&nbsp;`string` | Resposta bruta truncada do endpoint
`retry_count` | `null, int` | O número de tentativas de reenvio realizadas
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`url_path` | `null,`&nbsp;`string` | O caminho da URL sendo solicitada
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`webhook_duration` | `null, int` | Duração total desta requisição em milissegundos
`webhook_failure_source` | `null,`&nbsp;`string` | Para indicar se um erro foi criado pela Braze ou pelo próprio endpoint. O campo de origem pode ser External Endpoint, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Se este evento foi a tentativa final em um envio
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`time` | `int` | Timestamp Unix em que o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`campaign_name` | `null,`&nbsp;`string` | Nome da campanha
`message_variation_name` | `null,`&nbsp;`string` | Nome da variação de mensagem
`canvas_name` | `null,`&nbsp;`string` | Nome do Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Nome da variação do Canvas que este usuário recebeu
`canvas_step_name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% alert note %}
Esta tabela está disponível apenas no Snowflake Data Sharing.
{% endalert %}

Este evento ocorre quando uma mensagem é despriorizada ou limitada por frequência e é reenviada posteriormente dentro da janela de reenvio configurada.

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | [IPI] ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`gender` | `null,`&nbsp;`string` | [IPI] Gênero do usuário
`country` | `null,`&nbsp;`string` | [IPI] País do usuário
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`language` | `null,`&nbsp;`string` | [IPI] Idioma do usuário
`retry_type` | `null,`&nbsp;`string` | Tipo de reenvio
`retry_log` | `null,`&nbsp;`string` | Mensagem de registro descrevendo os detalhes do reenvio
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`to_phone_number` | 	`null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`abort_type` | `null,`&nbsp;`string` | Tipo de cancelamento. Para uma lista de valores, consulte [Tipos de cancelamento](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [IPI] Mensagem de registro descrevendo os detalhes do cancelamento (máximo de 2.000 caracteres)
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`url` | `null,`&nbsp;`string` | URL em que o usuário clicou
`short_url` | `null,`&nbsp;`string` | URL encurtada que foi clicada
`user_agent` | `null,`&nbsp;`string` | User agent no qual o relatório de spam ocorreu
`user_phone_number` | `null,`&nbsp;`string` | [IPI] O número de telefone do usuário a partir do qual a mensagem foi recebida
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`flow_id` | `null,`&nbsp;`string` | O ID exclusivo do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [IPI] Nome do modelo no WhatsApp Manager. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,`&nbsp;`string` | O ID exclusivo gerado pela Meta para esta mensagem
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`provider_error_code` | `null,`&nbsp;`string` | Código de erro do WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Título do erro do WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`message_id` | `null,`&nbsp;`string` | O ID exclusivo gerado pela Meta para esta mensagem
`template_name` | `null,`&nbsp;`string` | [IPI] Nome do modelo no WhatsApp Manager. Presente se estiver enviando uma mensagem de modelo
`flow_id` | `null,`&nbsp;`string` | O ID exclusivo do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`user_phone_number` | `string` | [IPI] O número de telefone do usuário a partir do qual a mensagem foi recebida
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`inbound_phone_number` | `string` | O número de entrada para o qual a mensagem foi enviada
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`message_body` | `string` | Resposta do usuário
`quick_reply_text` | `string` | Texto do botão pressionado pelo usuário
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | URLs de mídia do usuário
`action` | `string` | Ação tomada em resposta a esta mensagem. Por exemplo, `Subscribed`, `Unsubscribed` ou `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
`catalog_id` | `null,`&nbsp;`string` | ID do catálogo de um produto, se um produto for referenciado na mensagem de entrada. Caso contrário, vazio.
`product_id` | `null,`&nbsp;`string` | ID do produto comprado
`flow_id` | `null,`&nbsp;`string` | O ID exclusivo do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
`flow_response_json` | `null,`&nbsp;`string` | [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um WhatsApp Flow.
`message_id` | `null,`&nbsp;`string` | O ID exclusivo gerado pela Meta para esta mensagem
`in_reply_to` | `null,`&nbsp;`string` | O message_id da mensagem à qual esta mensagem estava respondendo
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do destinatário
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`template_name` | `null,`&nbsp;`string` | [IPI] Nome do modelo no WhatsApp Manager. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,`&nbsp;`string` | O ID exclusivo gerado pela Meta para esta mensagem
`flow_id` | `null,`&nbsp;`string` | O ID exclusivo do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Timestamp Unix em que o evento ocorreu
`to_phone_number` | `null,`&nbsp;`string`	| [IPI] Número de telefone do destinatário
`user_id` | `string` | ID da Braze do usuário que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`device_id` | `null,`&nbsp;`string` | `device_id` vinculado a este usuário, se o usuário for anônimo
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`from_phone_number` | `null,`&nbsp;`string` | Número de telefone a partir do qual a mensagem do WhatsApp foi enviada
`app_group_id` | `null,`&nbsp;`string` | ID do espaço de trabalho ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do espaço de trabalho ao qual este usuário pertence
`subscription_group_api_id` | `string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID da Braze para uso interno da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID da Braze para uso interno do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`message_extras` | `null,`&nbsp;`string` | [IPI] Uma string JSON dos pares chave-valor marcados durante a renderização Liquid
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe      
`send_id` | `null,`&nbsp;`string` | ID de envio da mensagem à qual esta mensagem pertence
`flow_id` | `null,`&nbsp;`string` | O ID exclusivo do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
`template_name` | `null,`&nbsp;`string` | [IPI] Nome do modelo no WhatsApp Manager. Presente se estiver enviando uma mensagem de modelo
`message_id` | `null,`&nbsp;`string` | O ID exclusivo gerado pela Meta para esta mensagem
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% alert note %}
Esta tabela está disponível apenas no Snowflake Data Sharing.
{% endalert %}

Este evento ocorre quando uma mensagem é despriorizada ou limitada por frequência e é reenviada posteriormente dentro da janela de reenvio configurada.

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`user_id` | `string` | [IPI] ID do usuário na Braze que realizou este evento
`external_user_id` | `null,`&nbsp;`string` | [IPI] ID externo do usuário
`app_group_id` | `null,`&nbsp;`string` | ID BSON do grupo de app ao qual este usuário pertence
`app_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de app ao qual este usuário pertence
`time` | `int` | Timestamp UNIX em que o evento ocorreu
`to_phone_number` | `null,`&nbsp;`string` | [IPI] Número de telefone do usuário que recebe a mensagem no formato e.164
`device_id` | `null,`&nbsp;`string` | ID do dispositivo no qual o evento ocorreu
`timezone` | `null,`&nbsp;`string` | Fuso horário do usuário
`subscription_group_api_id` | `null,`&nbsp;`string` | ID da API do grupo de inscrições
`campaign_id` | `null,`&nbsp;`string` | ID BSON da campanha à qual este evento pertence
`campaign_api_id` | `null,`&nbsp;`string` | ID da API da campanha à qual este evento pertence
`message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem que este usuário recebeu
`canvas_id` | `null,`&nbsp;`string` | ID BSON do Canvas ao qual este evento pertence
`canvas_api_id` | `null,`&nbsp;`string` | ID da API do Canvas ao qual este evento pertence
`canvas_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação do Canvas à qual este evento pertence
`canvas_step_api_id` | `null,`&nbsp;`string` | ID da API da etapa do Canvas à qual este evento pertence
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
`dispatch_id` | `null,`&nbsp;`string` | ID do despacho ao qual esta mensagem pertence
`retry_type` | `null,`&nbsp;`string` | Tipo de reenvio
`retry_log` | `null,`&nbsp;`string` | Mensagem de registro descrevendo os detalhes do reenvio
`sf_created_at` | `timestamp`,&nbsp;`null` | Quando este evento foi captado pelo Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuários

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Campo                       | Tipo                     | Descrição                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | ID globalmente exclusivo para este evento                  |
| `app_group_id`              | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence       |
| `user_id`                   | `string`,&nbsp;`null`    | ID da Braze do usuário que realizou este evento      |
| `external_user_id`          | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                 |
| `time`                      | `int`,&nbsp;`null`       | Registro de data/hora Unix em que o evento ocorreu         |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Número de bucket aleatório atual atribuído ao usuário  |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Número de bucket aleatório anterior atribuído ao usuário |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Campo              | Tipo                     | Descrição                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | ID globalmente exclusivo para este evento                             |
| `user_id`          | `string`,&nbsp;`null`    | ID da Braze do usuário que foi excluído                          |
| `app_group_id`     | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                  |
| `time`             | `int`,&nbsp;`null`       | Registro de data/hora Unix em que a solicitação de exclusão do usuário foi processada |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Campo              | Tipo                     | Descrição                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | ID globalmente exclusivo para este evento                                             |
| `user_id`          | `string`,&nbsp;`null`    | ID da Braze do usuário que se tornou órfão                                         |
| `external_user_id` | `string`,&nbsp;`null`    | [IPI] ID externo do usuário                                            |
| `device_id`        | `string`,&nbsp;`null`    | ID do dispositivo vinculado a este usuário, se o usuário for anônimo          |
| `app_group_id`     | `string`,&nbsp;`null`    | ID da Braze do espaço de trabalho ao qual este usuário pertence                                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | ID da API do espaço de trabalho ao qual este usuário pertence                                  |
| `app_api_id`       | `string`,&nbsp;`null`    | ID da API do app ao qual o usuário órfão pertencia                               |
| `time`             | `int`,&nbsp;`null`       | Registro de data/hora Unix em que o usuário se tornou órfão                                 |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | ID da Braze do usuário cujo perfil foi mesclado com o perfil do usuário órfão |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Quando este evento foi capturado pelo Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Snapshots {#snapshots}

{% alert note %}
As tabelas de snapshots estão disponíveis apenas no Snowflake Data Sharing.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API do app
`name` | `null,`&nbsp;`string` | Nome do app
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API da variação de mensagem da campanha
`name` | `null,`&nbsp;`string` | Nome da variação de mensagem da campanha
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`type` | `null,`&nbsp;`string` | Tipo da etapa do Canvas Flow
`api_step_id` | `string` | ID da API da etapa do Canvas
`experiment_splits` | `null,`&nbsp;`string` | Divisões do experimento para a etapa
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamentos de conversão para a etapa
`name` | `null,`&nbsp;`string` | Nome da etapa do Canvas Flow
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API da etapa do Canvas
`name` | `null,`&nbsp;`string` | Nome da etapa do Canvas
`actions` | `null,`&nbsp;`string` | Ações para a etapa do Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`api_id` | `string` | ID da API da variação do Canvas
`name` | `null,`&nbsp;`string` | Nome da variação do Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

Campo | Tipo | Descrição
------|------|------------
`id` | `string` | ID globalmente exclusivo para este evento
`time` | `int` | Registro de data/hora UNIX em que o evento ocorreu
`app_group_id` | `string` | ID BSON do grupo de app ao qual este usuário pertence
`type` | `null,`&nbsp;`string` | Tipo da etapa do Experimento
`api_step_id` | `string` | ID da API da etapa do Experimento
`experiment_splits` | `null,`&nbsp;`string` | Divisões do experimento para a etapa
`conversion_behaviors` | `null,`&nbsp;`string` | Comportamentos de conversão para a etapa
`name` | `null,`&nbsp;`string` | Nome da etapa do Experimento
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Tipos de cancelamento

{% include abort_types_reference.md %}