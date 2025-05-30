---
nav_title: Migration von Push-Token
article_title: Migration von Push-Token
page_order: 0

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie Push-Token migrieren, damit Sie auch nach dem Wechsel zu Braze weiterhin Push-Nachrichten an Ihre Nutzer:innen senden können."
channel: push
---

# Migration von Push-Tokens

> Ein [Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) ist ein eindeutiger anonymer Bezeichner, der angibt, wohin die Push-Benachrichtigungen einer App gesendet werden sollen. Braze stellt eine Verbindung zu Anbietern von Push-Diensten wie Firebase Cloud Messaging Service (FCMs) für Android und Apple Push Notification Service (APNs) für iOS her. Diese Anbieter senden eindeutige Geräte-Token, die Ihre App identifizieren. Wenn Sie vor der Integration von Braze bereits Push-Benachrichtigungen versendet haben, entweder selbst oder über einen anderen Anbieter, ist es mit der Push-Token Migration zulässig, weiterhin Push-Benachrichtigungen an Ihre Nutzer:innen mit registrierten Push-Token zu senden.

## Automatische Migration über SDK

Nachdem Sie [das Braze SDK integriert haben]({{site.baseurl}}/developer_guide/sdk_integration/), werden die Push-Token für Ihre Opt-in Nutzer:innen automatisch migriert, wenn sie Ihre App das nächste Mal öffnen. Bis dahin können Sie diesen Nutzer:innen keine Push-Benachrichtigungen über Braze senden.

Alternativ können Sie [Ihre Push-Token auch manuell migrieren](#manual-migration-via-api), was eine schnellere erneute Interaktion mit Ihren Nutzer:innen zulässt.

### Überlegungen zum Internet Token

Aufgrund der Natur von Web-Push-Tokens sollten Sie bei der Implementierung von Push für das Internet Folgendes beachten:

|Betrachtung|Details|
|----------------------|------------|
| **Service-Teammitglieder**  | Standardmäßig sucht das Internet SDK unter `./service-worker` nach einem Service-Teammitglied, es sei denn, es ist eine andere Option angegeben, wie `manageServiceWorkerExternally` oder `serviceWorkerLocation`. Wenn Ihr Service-Teammitglied nicht richtig eingerichtet ist, kann dies dazu führen, dass Push-Token für Ihre Nutzer:innen ablaufen. |
| **Abgelaufene Token**   | Wenn ein Nutzer:innen innerhalb von 60 Tagen keine Internetsitzung gestartet hat, verfällt sein Push-Token. Da Braze abgelaufene Push-Token nicht migrieren kann, müssen Sie einen [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) senden, um sie erneut zu engagieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Manuelle Migration über API

Bei der manuellen Push-Token Migration werden diese zuvor erstellten Schlüssel über die API in Ihre Braze Plattform importiert.

Programmatische Migration von iOS- (APNs) und Android- (FCM) Token auf Ihre Plattform mit Hilfe des [Endpunkts`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Sie können sowohl identifizierte Nutzer:in (Nutzer mit einer zugehörigen externen ID) als auch anonyme Nutzer:innen (Nutzer ohne externe ID) migrieren.

Geben Sie während der Push-Token Migration die `app_id` Ihrer App an, um das entsprechende Push-Token mit der entsprechenden App zu verknüpfen. Jede App (iOS, Android, etc.) hat ihre eigene `app_id`, die Sie im Abschnitt **Identifikation** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) finden. Achten Sie darauf, dass Sie die richtige Plattform `app_id` verwenden.

{% alert important %}
Es ist nicht möglich, Web-Push-Tokens über die API zu migrieren. Das liegt daran, dass Web-Push-Tokens nicht demselben Schema entsprechen wie andere Plattformen. 

<br>Wenn Sie versuchen, Web-Push-Tokens programmatisch zu migrieren, wird möglicherweise eine Fehlermeldung wie die folgende angezeigt: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Als Alternative zur API-Migration empfehlen wir Ihnen, das SDK zu integrieren und zuzulassen, dass sich Ihre Token-Basis auf natürliche Weise neu füllt.
{% endalert %}

{% tabs local %}
{% tab Externe ID vorhanden %}
Für identifizierte Nutzer:innen setzen Sie das Kennzeichen `push_token_import` auf `false` (oder lassen den Parameter weg) und geben die Werte `external_id`, `app_id` und `token` im Objekt `attributes` des Nutzers an. 

Zum Beispiel:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab Externe ID fehlt %}
Beim Importieren von Push-Tokens aus anderen Systemen ist nicht immer eine `external_id` verfügbar. In diesem Fall setzen Sie das Kennzeichen `push_token_import` auf `true` und geben die Werte `app_id` und `token` an. Braze erstellt für jeden Token ein temporäres, anonymes Nutzerprofil, damit Sie diesen Personen weiterhin Nachrichten schicken können. Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert.

Zum Beispiel:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

Wenn der anonyme Nutzer:in nach dem Import die Braze-fähige Version Ihrer App startet, verschiebt Braze das importierte Push-Token automatisch in sein Nutzerprofil und bereinigt das temporäre Profil.

Braze sucht einmal im Monat nach anonymen Profilen mit dem Kennzeichen `push_token_import`, die kein Push-Token haben. Wenn das anonyme Profil nicht mehr über einen Push-Token verfügt, löschen wir das Profil. Wenn das anonyme Profil jedoch immer noch ein Push-Token hat, was darauf hindeutet, dass der tatsächliche Nutzer sich noch nicht mit dem besagten Push-Token bei dem Gerät angemeldet hat, unternehmen wir nichts.
{% endtab %}
{% endtabs %}

## Importieren von Android Push-Tokens

{% alert important %}
Die folgenden Überlegungen gelten nur für Android Apps. iOS Apps benötigen diese Schritte nicht, da diese Plattform nur ein Framework für die Anzeige von Push hat und Push-Benachrichtigungen sofort gerendert werden, solange Braze über die notwendigen Push-Token und Zertifikate verfügt.
{% endalert %}

Wenn Sie Android Push-Benachrichtigungen an Ihre Nutzer:innen senden müssen, bevor die Braze SDK-Integration abgeschlossen ist, verwenden Sie Schlüssel-Wert-Paare, um Push-Benachrichtigungen zu validieren. 

Sie müssen über einen Empfänger verfügen, der Push-Nutzdaten verarbeiten und anzeigen kann. Um den Empfänger der Push-Nutzdaten zu benachrichtigen, fügen Sie der Kampagne die erforderlichen Schlüssel-Wert-Paare hinzu. Die Werte dieser Paare hängen von dem Push-Partner ab, den Sie vor Braze verwendet haben.

{% alert note %}
Bei einigen Anbietern von Push-Benachrichtigungen muss Braze die Schlüssel-Wert-Paare glätten, damit sie richtig interpretiert werden können. Um Schlüssel-Wert-Paare für eine bestimmte Android App zu reduzieren, wenden Sie sich an Ihren Customer Onboarding- oder Success-Manager:in.
{% endalert %}

_Zuletzt aktualisiert am 5\. Dezember 2022_
