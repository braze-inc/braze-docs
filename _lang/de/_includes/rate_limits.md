<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Wir wenden auf diesen Endpunkt das standardmäßige Braze-Rate-Limit von 250.000 Anfragen pro Stunde an, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Dieser Endpunkt hat ein Rate-Limit von 5.000 Anfragen pro Tag und Unternehmen. Dieses Rate-Limit wird mit den `/scim/v2/Users/`-Endpunkten GET, DELETE und POST geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Dieser Endpunkt hat ein Rate-Limit von 5.000 Anfragen pro Tag und Unternehmen. Dieses Rate-Limit wird mit den `/scim/v2/Users/`-Endpunkten PUT, GET, DELETE und POST geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Dieser Endpunkt hat ein Rate-Limit von 5.000 Anfragen pro Tag und Unternehmen. Dieses Rate-Limit wird mit den `/scim/v2/Users/`-Endpunkten PUT, GET und POST geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Dieser Endpunkt hat ein Rate-Limit von 5.000 Anfragen pro Tag und Unternehmen. Dieses Rate-Limit wird mit den `/scim/v2/Users/`-Endpunkten PUT, GET und DELETE geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Dieser Endpunkt hat ein Rate-Limit von 5.000 Anfragen pro Tag und Unternehmen. Dieses Rate-Limit wird mit den `/scim/v2/Users/`-Endpunkten PUT, GET, DELETE und POST geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Für diesen Endpunkt gilt ein Rate-Limit von 1.000 Anfragen pro Minute, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Ab dem 28\. Oktober 2024 gilt für diesen Endpunkt für alle Kund:innen ein Basisgeschwindigkeitslimit von 3.000 Anfragen pro drei Sekunden. Jede `/users/track`-Anfrage kann bis zu 75 Event-Objekte, 75 Attribut-Objekte und 75 Kauf-Objekte enthalten. Jedes Objekt (Ereignis-, Attribut- und Kauf-Arrays) kann jeweils eine:n Nutzer:in aktualisieren. Insgesamt können Sie also bis zu 225 Nutzer:innen mit einem einzigen Aufruf aktualisieren. Darüber hinaus können Sie ein einzelnes Nutzerprofil mit mehreren Objekten aktualisieren.

Für Kund:innen, die **Monthly Active Users - CY 24-25** erworben haben, gelten andere Limits. Einzelheiten zu diesen Limits finden Sie unter [Monthly Active Users - CY 24-25 Limits]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau).

Weitere Informationen finden Sie auf unserer Seite über [API-Rate-Limits]({{site.baseurl}}/api/api_limits/). Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie Ihr Limit erhöhen möchten.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Wenn Sie Braze am oder nach dem 22\. August 2024 eingerichtet haben, gilt für diesen Endpunkt ein Rate-Limit von 250 Anfragen pro Minute, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

Sie können das Rate-Limit dieses Endpunkts auch auf 40 Anfragen pro Sekunde erhöhen, wenn Sie die folgenden Voraussetzungen erfüllen:

- In Ihrem Workspace ist das Standard-Rate-Limit (250 Anfragen pro Minute) aktiviert. Wenden Sie sich an Ihren Braze Account Manager, um weitere Unterstützung bei der Aufhebung eines bereits bestehenden Rate-Limits zu erhalten.
- Ihre Anfrage enthält den Parameter `fields_to_export`, um alle Felder aufzulisten, die Sie erhalten möchten.

{% alert important %}
Wenn Sie `canvases_received` oder `campaigns_received` im Parameter `fields_to_export` angeben, kommt Ihre Anfrage nicht für das schnellere Rate-Limit in Frage. Wir empfehlen, diese nur dann in Ihre Anfrage aufzunehmen, wenn Sie einen speziellen Anwendungsfall dafür haben.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Wir wenden ein gemeinsames Rate-Limit von 20.000 Anfragen pro Minute auf diesen Endpunkt an. Dieses Rate-Limit wird mit den Endpunkten `/users/alias/new`, `/users/identify`, `/users/merge` und `/users/alias/update` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Wir wenden ein gemeinsames Rate-Limit von 20.000 Anfragen pro Minute auf diesen Endpunkt an. Dieses Rate-Limit wird mit den Endpunkten `/users/delete`, `/users/identify`, `/users/merge` und `/users/alias/update` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Wir wenden ein gemeinsames Rate-Limit von 20.000 Anfragen pro Minute auf diesen Endpunkt an. Dieses Rate-Limit wird mit den Endpunkten `/users/delete`, `/users/alias/new`, `/users/identify` und `/users/merge` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Wir wenden ein gemeinsames Rate-Limit von 20.000 Anfragen pro Minute auf diesen Endpunkt an. Dieses Rate-Limit wird mit den Endpunkten `/users/delete`, `/users/alias/new`, `/users/merge` und `/users/alias/update` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Wir wenden ein gemeinsames Rate-Limit von 20.000 Anfragen pro Minute auf diesen Endpunkt an. Dieses Rate-Limit wird mit den Endpunkten `/users/delete`, `/users/alias/new`, `/users/identify` und `/users/alias/update` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Wir wenden auf diesen Endpunkt ein gemeinsames Rate-Limit von 1.000 Anfragen pro Stunde an. Dieses Rate-Limit wird mit den Endpunkten `/events`, `/events/list` und `/purchases/product_list` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/events-->

{% elsif include.endpoint == "events" %}
Wir wenden auf diesen Endpunkt ein gemeinsames Rate-Limit von 1.000 Anfragen pro Stunde an. Dieses Rate-Limit wird mit den Endpunkten `/custom_attributes`, `/events/list` und `/purchases/product_list` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Wir wenden auf diesen Endpunkt ein gemeinsames Rate-Limit von 1.000 Anfragen pro Stunde an. Dieses Rate-Limit wird mit den Endpunkten `/custom_attributes`, `/events` und `/purchases/product_list` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Wir wenden auf diesen Endpunkt ein gemeinsames Rate-Limit von 1.000 Anfragen pro Stunde an. Dieses Rate-Limit wird mit den Endpunkten `/custom_attributes`, `/events` und `/events/list` geteilt, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Wenn Sie Connected-Audience-Filter in Ihrer Anfrage verwenden, gilt für diesen Endpunkt ein Rate-Limit von 250 Anfragen pro Minute. Andernfalls, wenn Sie eine `external_id` angeben, gilt für diesen Endpunkt ein Standard-Rate-Limit von 250.000 Anfragen pro Stunde, das zwischen `/messages/send`, `/campaigns/trigger/send` und `/canvas/trigger/send` geteilt wird, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

Braze-Endpunkte unterstützen das Stapeln von API-Anfragen. Eine einzelne Anfrage an die Messaging-Endpunkte kann Folgendes erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein Zielgruppensegment beliebiger Größe, das in der Anfrage als Connected-Audience-Objekt definiert ist

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
Der Endpunkt `/transactional/v1/campaigns/{campaign_id}/send` ist ein kostenpflichtiger Endpunkt in Einheiten pro Stunde (z. B. 50.000 pro Stunde, abhängig von Ihrem Paket). Es gibt kein separates Rate-Limit pro Endpunkt: Sie können über Ihr zugewiesenes Volumen hinaus senden, aber nur das zugewiesene Volumen ist durch das SLA abgedeckt. Anfragen an diesen Endpunkt werden auf Ihr [gesamtes Rate-Limit für externe APIs]({{site.baseurl}}/api/api_limits/) angerechnet. Wenn Sie dieses Limit überschreiten (z. B. 250.000 Anfragen pro Stunde über alle Endpunkte), gibt Braze den Statuscode 429 zurück und die Anfragen werden gedrosselt. Die Zählung des Transaktionsvolumens wird jede Stunde zurückgesetzt, sodass nach einer Stunde ein neues Kontingent zur Verfügung steht. Innerhalb des durch das SLA abgedeckten Volumens werden 99,9 % der E-Mails in weniger als einer Minute versendet.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Sie können mit diesem Endpunkt bis zu 100 angepasste Sende-Bezeichner pro Tag für einen bestimmten Workspace erstellen. Jede `send_id`- und `campaign_id`-Kombination, die Sie erstellen, wird auf Ihr Tageslimit angerechnet. Die Antwort-Header für jede gültige Anfrage enthalten den aktuellen Rate-Limit-Status. Einzelheiten finden Sie unter [API-Rate-Limits]({{site.baseurl}}/api/api_limits/).

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Für diesen Endpunkt gilt ein Rate-Limit von 5.000 Anfragen pro Minute, das zwischen den Endpunkten `/subscription/status/set` und `/v2/subscription/status/set` geteilt wird, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Dieser Endpunkt hat ein Rate-Limit von 50 Anfragen pro Minute.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Dieser Endpunkt hat ein Rate-Limit von 20 Anfragen pro Minute.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Dieser Endpunkt hat ein Rate-Limit von 100 Anfragen pro Minute.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Braze-Endpunkte unterstützen das [Stapeln von API-Anfragen]({{site.baseurl}}/api/api_limits/#batching-api-requests). Eine einzelne Anfrage an die Messaging-Endpunkte kann Folgendes erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein im Braze-Dashboard erstelltes Segment beliebiger Größe, angegeben durch seine `segment_id`
- Ein Zielgruppensegment beliebiger Größe, das in der Anfrage als [Connected-Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)-Objekt definiert ist

{% endif %}

{% if include.category == "send messages endpoints" %}

Braze-Endpunkte unterstützen das [Stapeln von API-Anfragen]({{site.baseurl}}/api/api_limits/#batching-api-requests). Eine einzelne Anfrage an die Messaging-Endpunkte kann Folgendes erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein Zielgruppensegment beliebiger Größe, das in der Anfrage als [Connected-Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)-Objekt definiert ist

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Dieser Endpunkt hat ein Rate-Limit von 250.000 Anfragen pro Minute.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Braze-Endpunkte unterstützen das [Stapeln von API-Anfragen]({{site.baseurl}}/api/api_limits/#batching-api-requests). Eine einzelne Anfrage an die Messaging-Endpunkte kann Folgendes erreichen:

- Bis zu 50 spezifische `external_ids`
- Ein im Braze-Dashboard erstelltes Segment beliebiger Größe, angegeben durch seine `segment_id`
- Ein Zielgruppensegment beliebiger Größe, das in der Anfrage als [Connected-Audience]({{site.baseurl}}/api/objects_filters/connected_audience/)-Objekt definiert ist

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Für diesen Endpunkt gilt ein gemeinsames Rate-Limit von 16.000 Anfragen pro Minute für alle asynchronen Katalog-Artikel-Endpunkte, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Für diesen Endpunkt gilt ein gemeinsames Rate-Limit von 50 Anfragen pro Minute für alle synchronen Katalog-Artikel-Endpunkte, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Für diesen Endpunkt gilt ein gemeinsames Rate-Limit von 50 Anfragen pro Minute für alle synchronen Katalog-Endpunkte, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Für diesen Endpunkt gilt ein gemeinsames Rate-Limit von 50 Anfragen pro Minute für alle asynchronen Katalog-Felder- und Auswahl-Endpunkte, wie in [API-Rate-Limits]({{site.baseurl}}/api/api_limits/) dokumentiert.

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Dieser Endpunkt hat ein Rate-Limit von 50.000 Anfragen pro Minute.

{% endif %}