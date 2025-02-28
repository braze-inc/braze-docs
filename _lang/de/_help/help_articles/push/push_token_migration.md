---
nav_title: Push-Token migrieren
article_title: Push-Token migrieren
page_order: 0

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie Push-Token migrieren, damit Sie auch nach dem Wechsel zu Braze weiterhin Push-Nachrichten an Ihre Benutzer senden können."
channel: push
---

# Push-Token migrieren

Ein [Push-Token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) ist ein eindeutiger anonymer Bezeichner, der angibt, wohin die Benachrichtigungen einer App gesendet werden sollen. Braze stellt eine Verbindung zu Anbietern von Push-Diensten wie Firebase Cloud Messaging Service (FCMs) für Android und Apple Push Notification Service (APNs) für iOS her. Diese Anbieter senden eindeutige Geräte-Token, die Ihre App identifizieren. Wenn Sie vor der Integration von Braze selbst oder über einen anderen Anbieter Push-Benachrichtigungen versendet haben, können Sie mit der Push-Token-Migration weiterhin Push-Benachrichtigungen an Ihre Benutzer mit registrierten Push-Tokens versenden.

## Automatische Migration über SDK

Das Braze SDK migriert automatisch das Push-Token eines Benutzers, der sich zuvor für Ihre Push-Benachrichtigungen entschieden hat, wenn er sich zum ersten Mal bei Ihrer Braze-integrierten App oder Website anmeldet. Wenn Sie die Braze SDKs integrieren, müssen Sie die Push-Tokens nicht über die API migrieren.

Da Push-Tokens jedoch migriert werden, wenn sich ein Benutzer zum ersten Mal bei Ihrer App anmeldet, beachten Sie, dass Braze keine Push-Benachrichtigungen an Benutzer senden kann, die sich nach Ihrer SDK-Integration nicht angemeldet haben. Möglicherweise möchten Sie dennoch Android- und iOS-Push-Tokens manuell migrieren, um diese Nutzer wieder zu erreichen.

{% alert note %}
Aufgrund der Natur von Web-Push-Tokens läuft der Token alle 60 Tage ab und wird zurückgesetzt. Jeder, der innerhalb dieses Zeitraums keine Sitzung hat, hat auch kein aktives Web-Push-Token. Braze wird abgelaufene Web-Push-Tokens nicht migrieren. Diese Benutzer müssen durch [Push-Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) wieder angesprochen werden.
{% endalert %}

## Manuelle Migration über API

Bei der manuellen Push-Token-Migration werden diese zuvor erstellten Schlüssel über die API in Ihre Braze-Plattform importiert.

Migrieren Sie iOS- (APNs) und Android- (FCM) Token programmatisch auf Ihre Plattform, indem Sie den [Endpunkt`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) verwenden. Sie können sowohl identifizierte Benutzer (Benutzer mit einer zugehörigen externen ID) als auch anonyme Benutzer (Benutzer ohne externe ID) migrieren.

Geben Sie während der Push-Token-Migration die `app_id` Ihrer App an, um das entsprechende Push-Token mit der entsprechenden App zu verknüpfen. Jede App (iOS, Android, etc.) hat ihre eigene `app_id`, die Sie im Abschnitt **Identifikation** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) finden können. Achten Sie darauf, dass Sie die richtige Plattform `app_id` verwenden.

{% alert important %}
Es ist nicht möglich, Web-Push-Tokens über die API zu migrieren. Das liegt daran, dass Web-Push-Tokens nicht demselben Schema entsprechen wie andere Plattformen. 

<br>Wenn Sie versuchen, Web-Push-Tokens programmatisch zu migrieren, wird möglicherweise ein Fehler wie der folgende angezeigt: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Als Alternative zur API-Migration empfehlen wir Ihnen, das SDK zu integrieren und zuzulassen, dass sich Ihre Token-Basis auf natürliche Weise neu füllt.
{% endalert %}

### Migration bei Vorhandensein einer externen ID
Für identifizierte Benutzer setzen Sie das Kennzeichen `push_token_import` auf `false` (oder lassen den Parameter weg) und geben die Werte `external_id`, `app_id` und `token` im Objekt `attributes` des Benutzers an. 

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

### Migration, wenn keine externe ID vorhanden ist
Beim Importieren von Push-Tokens aus anderen Systemen ist nicht immer eine `external_id` verfügbar. In diesem Fall setzen Sie das Kennzeichen `push_token_import` auf `true` und geben die Werte `app_id` und `token` an. Braze wird für jedes Token ein temporäres, anonymes Benutzerprofil erstellen, damit Sie diesen Personen weiterhin Nachrichten senden können. Wenn das Token bereits in Braze existiert, wird die Anfrage ignoriert.

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

Wenn der anonyme Benutzer nach dem Import die Braze-aktivierte Version Ihrer App startet, verschiebt Braze das importierte Push-Token automatisch in sein Braze-Benutzerprofil und bereinigt das temporäre Profil.

Braze prüft einmal im Monat, ob ein anonymes Profil mit dem Kennzeichen `push_token_import` kein Push-Token hat. Wenn das anonyme Profil nicht mehr über ein Push-Token verfügt, löschen wir das Profil. Wenn das anonyme Profil jedoch immer noch ein Push-Token hat, was darauf hindeutet, dass der tatsächliche Benutzer sich noch nicht mit diesem Push-Token bei dem Gerät angemeldet hat, unternehmen wir nichts.

## Importieren von Android-Push-Tokens

{% alert important %}
Die folgenden Überlegungen gelten nur für Android-Apps. iOS-Apps benötigen diese Schritte nicht, da diese Plattform nur ein Framework für die Anzeige von Push hat und Push-Benachrichtigungen sofort gerendert werden, solange Braze über die erforderlichen Push-Token und Zertifikate verfügt.
{% endalert %}

Wenn Sie Android-Push-Benachrichtigungen an Ihre Benutzer senden müssen, bevor die Integration des Braze SDK abgeschlossen ist, verwenden Sie Schlüssel-Wert-Paare, um Push-Benachrichtigungen zu validieren. 

Sie müssen über einen Empfänger verfügen, der Push-Nutzdaten verarbeiten und anzeigen kann. Um den Empfänger der Push-Nutzdaten zu benachrichtigen, fügen Sie der Push-Kampagne die erforderlichen Schlüssel-Wert-Paare hinzu. Die Werte dieser Paare hängen von dem spezifischen Push-Partner ab, den Sie vor Braze verwendet haben.

{% alert note %}
Für einige Anbieter von Push-Benachrichtigungen muss Braze die Schlüssel-Wert-Paare reduzieren, damit sie richtig interpretiert werden können. Um Schlüssel-Wert-Paare für eine bestimmte Android-App zu reduzieren, wenden Sie sich an Ihren Customer Onboarding oder Success Manager.
{% endalert %}

_Zuletzt aktualisiert am 5\. Dezember 2022_
