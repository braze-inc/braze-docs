---
nav_title: SMS-Nachrichten senden
article_title: Versenden von SMS-Nachrichten über die REST API
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie SMS-Nachrichten mithilfe der Braze REST API und einer API-Kampagne versenden können."
channel:
  - SMS
---

# Versenden von SMS-Nachrichten über die REST API

> Verwenden Sie die Braze REST API, um Transaktions-SMS-Nachrichten in Realtime von Ihrem Backend aus zu versenden. Mit diesem Ansatz können Sie einen Dienst erstellen, der SMS-Nachrichten programmgesteuert versendet und gleichzeitig die Zustellungsanalytics zusammen mit Ihren anderen Kampagnen und Canvases im Braze-Dashboard verfolgt.

Dies kann insbesondere für transaktionsbasiertes Messaging mit hohem Volumen nützlich sein, bei dem der Inhalt in Ihren Backend-Systemen definiert ist. Sie können beispielsweise Verbraucher:innen benachrichtigen, wenn sie eine Nachricht von einem anderen Nutzer:in erhalten, und sie einladen, Ihre Website zu besuchen und ihren Posteingang zu überprüfen.

Mit diesem Ansatz können Sie:

- Triggern Sie SMS-Nachrichten in Realtime von Ihrem Backend aus.
- Verfolgen Sie die Analytics-Daten aller Ihrer Marketing-Kampagnen und Canvases.
- Erweitern Sie den Anwendungsfall mit zusätzlichen Braze-Features wie Nachrichtenverzögerungen, Follow-up-Retargeting und A/B-Tests.
- Optional können Sie zur [API-gesteuerten Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) wechseln, um Ihre Nachrichten-Templates im Braze-Dashboard zu definieren, während Sie den Versand weiterhin über Ihr Backend triggern.

Um eine SMS-Nachricht über die REST API zu versenden, müssen Sie im Braze-Dashboard eine Messaging-Kampagne einrichten und anschließend den[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)Endpunkt verwenden, um die Nachricht zu versenden.

## Voraussetzungen

Um diese Anleitung zu bearbeiten, benötigen Sie:

| Anforderung | Beschreibung |
| --- | --- |
| Braze REST API-Schlüssel | Ein Schlüssel mit der entsprechenden`messages.send` Berechtigung. Um einen zu erstellen, navigieren Sie bitte zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. |
| SMS-Abo-Gruppe | Eine in Ihrem Braze-Workspace konfigurierte SMS-Abo-Gruppe. |
| Backend-Dienst | Ein Backend-Dienst oder eine Skriptumgebung, die HTTP-POST-Anfragen an die Braze-REST-API senden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 1: Erstellen Sie eine API-Kampagne

1. Bitte gehen Sie im Braze-Dashboard zu **„Messaging“** > **„Kampagnen**“.
2. Bitte wählen Sie **„Kampagne erstellen**“ und anschließend **„API-Kampagnen**“.
3. Bitte geben Sie einen Namen und eine Beschreibung für Ihre Kampagne ein, beispielsweise „SMS-Benachrichtigung“.
4. Fügen Sie bitte relevante Tags zur Identifizierung und zum Tracking hinzu.
5. Bitte wählen Sie **„Messaging-Kanal hinzufügen**“ und anschließend **„SMS**“.
6. Bitte notieren Sie sich die **Kampagnen-ID** und **die Nachrichtenvariations-ID**, die auf der Kampagnenseite angezeigt werden. Sie benötigen beide Werte, um Ihre API-Anfrage zu erstellen.

## Schritt 2: Bitte senden Sie eine SMS-Nachricht über die API.

Erstellen Sie eine POST-Anfrage an den[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)Endpunkt. Bitte geben Sie die ID der Kampagne, die externe ID des Empfängers und den SMS-Inhalt in der Anfrage-Nutzlast an.

{% alert important %}
Jeder in  referenzierte`external_user_ids` Empfänger:in muss bereits in Braze vorhanden sein. API-only-Sends erstellen keine neuen Nutzerprofile. Wenn Sie im Rahmen eines Versands Nutzer:innen anlegen müssen, verwenden Sie bitte[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) zunächst oder alternativ eine [API-gesteuerte Kampagne]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Beispiel Anfrage

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Ersetzen Sie dies`YOUR_REST_ENDPOINT`durch die [REST-Endpunkt-URL]({{site.baseurl}}/api/basics/#endpoints) für Ihre Workspace.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Ersetzen Sie die Platzhalterwerte durch Ihre tatsächlichen IDs. Das`body`Feld unterstützt [Liquid-Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), sodass Sie den Inhalt der Nachricht an jede Empfänger:in individuell anpassen können. Die vollständige Liste der vom SMS-Messaging-Objekt unterstützten Parameter finden Sie unter [SMS-Objekt]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

Nachdem Sie die Anfrage erstellt haben, senden Sie die POST-Anfrage von Ihrem Backend-Dienst an die Braze REST API.

## Schritt 3: Bitte überprüfen Sie Ihre Integration.

Bitte überprüfen Sie nach Abschluss der Einrichtung Ihre Integration:

1. Senden Sie eine API-Anfrage wie in [Schritt 2](#step-2-send-an-sms-message-using-the-api) beschrieben und verwenden Sie dabei Ihre eigene Benutzer-ID als Empfänger:in.
2. Bitte bestätigen Sie, dass die SMS-Nachricht auf Ihrem Telefon zugestellt wurde.
3. Bitte gehen Sie im Braze-Dashboard zur Seite mit den Ergebnissen der Kampagne und überprüfen Sie, ob der Versand aufgezeichnet wurde.
4. Bitte überwachen Sie die Ergebnisse sorgfältig, während Sie Ihre Kampagne skalieren.

## Überlegungen

- Bitte stellen Sie sicher, dass Ihre SMS-Kampagnen den geltenden Vorschriften und Anforderungen der Netzbetreiber entsprechen. Bitte fügen Sie in jede Nachricht eine Abmeldeanweisung ein (z. B. „Senden Sie STOP, um sich abzumelden“). Weitere Informationen finden Sie unter [SMS-Gesetze und -Vorschriften]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) sowie [Opt-in- und Opt-out-Schlüsselwörter]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/).
- Nutzen Sie [die Features der Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) von Braze, um SMS-Inhalte individuell auf individuelle Verbraucher:innen zuzuschneiden, einschließlich dynamischen Contents und benutzerspezifischer Daten.
- Die Braze REST API bietet zusätzliche [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/) für den Zeitplan von Nachrichten, das Triggern von Kampagnen und vieles mehr.
