Die folgende Tabelle listet die möglichen `abort_type`-Werte auf. Ein Abbruchtyp beschreibt den konkreten Grund, warum eine Nachricht nicht gesendet wurde.

{% if include.channel %}
{% assign ch = include.channel %}
{% else %}
{% assign ch = "all" %}
{% endif %}

### Allgemein

Diese Abbruchtypen können auf jedem Messaging-Kanal auftreten.

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `liquid_abort_message` | Der Liquid-Tag [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) wurde aufgerufen, daher wurde der Versand abgebrochen. |
| `template_parse_error` | Das Nachrichten-Template konnte aufgrund eines Syntax- oder Rendering-Fehlers nicht geparst werden, daher wurde der Versand abgebrochen. |
| `rate_limit` | Die Nachricht wurde abgebrochen, weil das konfigurierte [Rate-Limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) überschritten wurde. |
| `campaign_disabled` | Die Kampagne wurde deaktiviert, bevor die Nachricht gesendet werden konnte. |
| `campaign_does_not_exist` | Die mit dieser Nachricht verknüpfte Kampagne existiert nicht mehr. |
| `campaign_action_does_not_exist` | Die mit dieser Nachricht verknüpfte Kampagnenaktion existiert nicht mehr. |
| `message_variation_does_not_exist` | Die diesem/dieser Nutzer:in zugewiesene Nachrichtenvariante existiert nicht mehr. |
| `user_not_in_segment` | Der/die Nutzer:in befindet sich nicht im Zielsegment, daher wurde die Nachricht nicht gesendet. |
| `trigger_event_blacklisted` | Das Trigger-Event ist auf der Sperrliste, daher wurde die Nachricht nicht gesendet. |
| `exhausted_retries` | Die Nachricht konnte nach der maximalen Anzahl von Wiederholungsversuchen nicht gesendet werden. |
| `frequency_capped` | Der/die Nutzer:in hat bereits die maximale Anzahl an Nachrichten erhalten, die durch die [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping)-Regeln Ihres Workspace erlaubt sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% unless ch == "newsfeedcard" or ch == "rcs" %}

### Inhalt und Rendering

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `exhausted_cc_retries` | Connected-Content ist nach der maximalen Anzahl von Wiederholungsversuchen fehlgeschlagen, daher wurde die Nachricht abgebrochen. |
| `connected_content_not_supported` | [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) wird in diesem Kontext nicht unterstützt, daher wurde die Nachricht abgebrochen. |
| `promo_codes_not_supported` | Aktionscodes werden in diesem Kontext nicht unterstützt, daher wurde die Nachricht abgebrochen. |
| `catalog_items_rerender_not_supported` | Das erneute Rendern von Katalogartikeln wird in diesem Kontext nicht unterstützt, daher wurde die Nachricht abgebrochen. |
{% if ch == "all" or ch == "email" or ch == "push" or ch == "inappmessage" or ch == "contentcard" or ch == "webhook" or ch == "banner" %}| `blacklisted_media_url` | Die Medien-URL ist auf der Sperrliste und kann nicht in Nachrichten verwendet werden. |
| `blocked_media_url` | Die Medien-URL wurde durch Sicherheitsrichtlinien blockiert. |
| `invalid_media_url` | Die Medien-URL ist ungültig oder konnte nicht aufgelöst werden. |{% endif %}
{% if ch == "all" or ch == "email" or ch == "webhook" %}| `ssl_error` | Bei einer Anfrage ist ein SSL-Fehler aufgetreten. |
| `invalid_http_status` | Eine HTTP-Anfrage hat einen nicht erfolgreichen Statuscode zurückgegeben. |
| `http_timeout` | Bei einer HTTP-Anfrage wurde das Zeitlimit überschritten, bevor eine Antwort empfangen wurde. |
| `missing_hostname` | In der Anfrage-URL fehlt ein Hostname. |{% endif %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endunless %}

{% if ch == "all" or ch == "email" %}

### E-Mail

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `exhausted_link_shortening_retries` | Die Linkverkürzung ist nach der maximalen Anzahl von Wiederholungsversuchen fehlgeschlagen. |
| `missing_email` | Der/die Nutzer:in hat keine E-Mail-Adresse in seinem/ihrem Profil. |
| `invalid_domain` | Die E-Mail-Adresse hat eine ungültige Domain. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "push" %}

### Push

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `invalid_push_payload` | Die Payload der Push-Benachrichtigung ist ungültig oder fehlerhaft formatiert. |
| `sdk_not_supported` | Die SDK-Version auf dem Gerät des/der Nutzer:in unterstützt diesen Typ von Push-Benachrichtigung nicht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "sms" %}

### SMS/MMS

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `exhausted_link_shortening_retries` | Die Linkverkürzung ist nach der maximalen Anzahl von Wiederholungsversuchen fehlgeschlagen. |
| `sms_empty_payload` | Der SMS-Nachrichtentext ist leer. |
| `sms_no_sending_numbers` | Für diese Abo-Gruppe sind keine Absender-Telefonnummern verfügbar. |
| `sms_fatal_provider_error` | Beim SMS-Anbieter ist ein schwerwiegender Fehler aufgetreten, der die Nachrichtenzustellung verhindert hat. |
| `sms_gateway_domain_not_allowed` | Die SMS-Gateway-Domain befindet sich nicht auf der Zulassungsliste. |
| `blocked_recipient_country` | Die Telefonnummer der Empfänger:in befindet sich in einem Land, das durch Ihre [geografischen Berechtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/) blockiert ist. |
| `mms_not_supported` | MMS wird für diese Empfänger:in oder Absendernummer nicht unterstützt. |
| `no_current_messaging_service` | Für diese Abo-Gruppe ist kein aktiver Messaging-Dienst konfiguriert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "whatsapp" %}

### WhatsApp

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `whats_app_no_sending_numbers` | Für diese WhatsApp-Abo-Gruppe sind keine Absender-Telefonnummern verfügbar. |
| `whats_app_invalid_template_message` | Die WhatsApp-Template-Nachricht ist ungültig oder nicht genehmigt. |
| `whats_app_invalid_response_message` | Die WhatsApp-Antwortnachricht ist ungültig. |
| `whats_app_fatal_provider_error` | Beim WhatsApp-Anbieter ist ein schwerwiegender Fehler aufgetreten, der die Nachrichtenzustellung verhindert hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "line" %}

### LINE

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `line_fatal_provider_error` | Beim LINE-Anbieter ist ein schwerwiegender Fehler aufgetreten, der die Nachrichtenzustellung verhindert hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "kakao" %}

### Kakao

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `kakao_fatal_provider_error` | Beim Kakao-Anbieter ist ein schwerwiegender Fehler aufgetreten, der die Nachrichtenzustellung verhindert hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "contentcard" %}

### Content Cards

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `content_card_size_exceeded` | Die Payload der Content-Card überschreitet die maximale Größenbeschränkung (2 KB). |
| `content_card_content_invalid` | Der Inhalt der Content-Card ist ungültig oder enthält nicht unterstützte Zeichen. |
| `content_card_expiration_invalid` | Das Ablaufdatum der Content-Card ist ungültig. |
| `content_card_general` | Die Content-Card konnte aufgrund eines allgemeinen Fehlers nicht erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "inappmessage" %}

### In-App-Nachrichten

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `no_longer_in_availability_window` | Die Nachricht konnte nicht innerhalb des konfigurierten Verfügbarkeitsfensters gesendet werden und wurde daher abgebrochen. |
| `maximum_impressions_reached` | Die In-App-Nachricht hat bereits die maximale Anzahl an Impressionen erreicht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}

{% if ch == "all" or ch == "webhook" %}

### Webhooks

| `abort_type`-Wert | Beschreibung |
| --- | --- |
| `blocked_webhook_url` | Die Webhook-URL wurde durch Sicherheitsrichtlinien blockiert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}