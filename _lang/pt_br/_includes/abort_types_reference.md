A tabela a seguir lista os possíveis valores de `abort_type`. Um tipo de cancelamento descreve o motivo específico pelo qual uma mensagem não foi enviada.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### Geral

Esses tipos de cancelamento podem ocorrer em qualquer canal de envio de mensagens.

| Valor de `abort_type` | Descrição |
| --- | --- |
| `liquid_abort_message` | A Liquid tag [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) foi chamada, então o envio foi cancelado. |
| `template_parse_error` | O modelo de mensagem não pôde ser analisado devido a um erro de sintaxe ou renderização, então o envio foi cancelado. |
| `rate_limit` | A mensagem foi cancelada porque excedeu o [limite de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) configurado. |
| `campaign_disabled` | A campanha foi desativada antes que a mensagem pudesse ser enviada. |
| `campaign_does_not_exist` | A campanha associada a esta mensagem não existe mais. |
| `campaign_action_does_not_exist` | A ação de campanha associada a esta mensagem não existe mais. |
| `message_variation_does_not_exist` | A variação de mensagem atribuída a este usuário não existe mais. |
| `user_not_in_segment` | O usuário não está no segmento alvo, então a mensagem não foi enviada. |
| `trigger_event_blacklisted` | O evento de gatilho está na lista de proibições, então a mensagem não foi enviada. |
| `exhausted_retries` | A mensagem não pôde ser enviada após o número máximo de tentativas. |
| `frequency_capped` | O usuário já recebeu o número máximo de mensagens permitido pelas regras de [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) do seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### Conteúdo e renderização

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_cc_retries` | O Conteúdo conectado falhou após o número máximo de tentativas, então a mensagem foi cancelada. |
| `connected_content_not_supported` | O [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) não é compatível neste contexto, então a mensagem foi cancelada. |
| `promo_codes_not_supported` | Códigos de promoção não são compatíveis neste contexto, então a mensagem foi cancelada. |
| `catalog_items_rerender_not_supported` | A re-renderização de itens do Catálogo não é compatível neste contexto, então a mensagem foi cancelada. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | A URL de mídia está na lista de proibições e não pode ser usada em mensagens. |
| `blocked_media_url` | A URL de mídia foi bloqueada por políticas de segurança. |
| `invalid_media_url` | A URL de mídia não é válida ou não pôde ser resolvida. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | Ocorreu um erro de SSL ao fazer uma solicitação. |
| `invalid_http_status` | Uma solicitação HTTP retornou um código de status sem sucesso. |
| `http_timeout` | Uma solicitação HTTP expirou antes de receber uma resposta. |
| `missing_hostname` | A URL da solicitação não contém um hostname. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### E-mail

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_link_shortening_retries` | O encurtamento de link falhou após o número máximo de tentativas. |
| `missing_email` | O usuário não tem um endereço de e-mail no perfil. |
| `invalid_domain` | O endereço de e-mail tem um domínio inválido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| Valor de `abort_type` | Descrição |
| --- | --- |
| `invalid_push_payload` | A carga útil da notificação por push é inválida ou está malformada. |
| `sdk_not_supported` | A versão do SDK no dispositivo do usuário não é compatível com esse tipo de notificação por push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| Valor de `abort_type` | Descrição |
| --- | --- |
| `exhausted_link_shortening_retries` | O encurtamento de link falhou após o número máximo de tentativas. |
| `sms_empty_payload` | O corpo da mensagem SMS está vazio. |
| `sms_no_sending_numbers` | Não há números de telefone de envio disponíveis para este grupo de inscrições. |
| `sms_fatal_provider_error` | Ocorreu um erro fatal com o provedor de SMS, impedindo a entrega da mensagem. |
| `sms_gateway_domain_not_allowed` | O domínio do gateway SMS não está na lista de permissões. |
| `blocked_recipient_country` | O número de telefone do destinatário está em um país bloqueado pelas suas [permissões geográficas]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/). |
| `mms_not_supported` | MMS não é compatível com este destinatário ou número de envio. |
| `no_current_messaging_service` | Nenhum serviço de envio de mensagens ativo está configurado para este grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| Valor de `abort_type` | Descrição |
| --- | --- |
| `whats_app_no_sending_numbers` | Não há números de telefone de envio disponíveis para este grupo de inscrições do WhatsApp. |
| `whats_app_invalid_template_message` | O modelo de mensagem do WhatsApp é inválido ou não foi aprovado. |
| `whats_app_invalid_response_message` | A mensagem de resposta do WhatsApp é inválida. |
| `whats_app_fatal_provider_error` | Ocorreu um erro fatal com o provedor do WhatsApp, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| Valor de `abort_type` | Descrição |
| --- | --- |
| `line_fatal_provider_error` | Ocorreu um erro fatal com o provedor do LINE, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| Valor de `abort_type` | Descrição |
| --- | --- |
| `kakao_fatal_provider_error` | Ocorreu um erro fatal com o provedor do Kakao, impedindo a entrega da mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Cartões de conteúdo

| Valor de `abort_type` | Descrição |
| --- | --- |
| `content_card_size_exceeded` | A carga útil do cartão de conteúdo excede o limite máximo de tamanho (2 KB). |
| `content_card_content_invalid` | O conteúdo do cartão de conteúdo é inválido ou contém caracteres não compatíveis. |
| `content_card_expiration_invalid` | A data de expiração do cartão de conteúdo é inválida. |
| `content_card_general` | O cartão de conteúdo não pôde ser criado devido a um erro geral. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### Mensagens no app

| Valor de `abort_type` | Descrição |
| --- | --- |
| `no_longer_in_availability_window` | A mensagem não pôde ser enviada dentro do período de disponibilidade configurado, então foi cancelada. |
| `maximum_impressions_reached` | A mensagem no app já atingiu o número máximo de impressões. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| Valor de `abort_type` | Descrição |
| --- | --- |
| `blocked_webhook_url` | A URL do webhook foi bloqueada por políticas de segurança. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}