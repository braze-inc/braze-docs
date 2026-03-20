---
nav_title: E-Mail-Nachrichten senden
article_title: E-Mail-Nachrichten über die REST API senden
page_order: 3
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Sie E-Mail-Nachrichten über die Braze REST API und eine API-Kampagne senden."
channel:
  - email
---

# E-Mail-Nachrichten über die REST API senden

> Verwenden Sie die Braze REST API, um Transaktions-E-Mails in Echtzeit aus Ihrem Backend zu senden. Mit diesem Ansatz können Sie einen Dienst aufbauen, der E-Mails programmatisch versendet und gleichzeitig die Zustellungs-Analytics neben Ihren anderen Kampagnen und Canvasen im Braze-Dashboard verfolgt.

Dies kann besonders nützlich für Transaktions-Messaging sein, bei dem der Inhalt in Ihren Backend-Systemen definiert wird. Zum Beispiel können Sie Verbraucher:innen benachrichtigen, wenn sie eine Nachricht von einer anderen Person erhalten, und sie einladen, Ihre Website zu besuchen und ihren Posteingang zu überprüfen.

Mit diesem Ansatz können Sie:

- E-Mails in Echtzeit aus Ihrem Backend triggern.
- Analytics neben all Ihren Marketing-eigenen Kampagnen und Canvasen verfolgen, einschließlich Öffnungen, Klicks und Absprüngen.
- Nachrichteninteraktionsdaten verwenden, um Folgenachrichten auszulösen, z. B. Follow-up-Retargeting.
- Den Anwendungsfall mit zusätzlichen Braze-Features erweitern, wie z. B. Nachrichtenverzögerungen und A/B-Tests.
- Optional zur [API-getriggerten Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) wechseln, um Ihre E-Mail-Templates im Braze-Dashboard zu definieren und trotzdem den Versand aus Ihrem Backend zu triggern.

Um eine E-Mail über die REST API zu senden, müssen Sie eine API-Kampagne im Braze-Dashboard einrichten und dann den [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)-Endpunkt verwenden, um die Nachricht zu senden.

## Voraussetzungen

Um diese Anleitung abzuschließen, benötigen Sie:

| Anforderung | Beschreibung |
| --- | --- |
| Braze REST-API-Schlüssel | Einen Schlüssel mit der Berechtigung `messages.send`. Um einen zu erstellen, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. |
| Braze App-ID | Der Bezeichner für Ihre App innerhalb Ihres Workspace. Um ihn zu finden, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** und prüfen Sie den Abschnitt **App-Bezeichner**. Dieser Wert ist im Feld `app_id` des E-Mail-Messaging-Objekts erforderlich. Weitere Informationen finden Sie unter [App-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| HTML-E-Mail-Inhalt | Der HTML-Body Ihrer E-Mail-Nachricht, im Voraus vorbereitet. |
| Backend-Dienst | Ein Backend-Dienst oder eine Skriptumgebung, die HTTP-POST-Anfragen an die Braze REST API senden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1. Schritt: Eine API-Kampagne erstellen

1. Gehen Sie im Braze-Dashboard zu **Messaging** > **Kampagnen**.
2. Wählen Sie **Kampagne erstellen** und dann **API-Kampagne**.
3. Geben Sie einen Namen und eine Beschreibung für Ihre Kampagne ein, z. B. „E-Mail-Nachrichtenbenachrichtigung".
4. Fügen Sie relevante Tags zur Identifikation und zum Tracking hinzu.
5. Wählen Sie **Messaging-Kanal hinzufügen** und dann **E-Mail**.
6. Notieren Sie sich die **Kampagnen-ID**, die auf der Kampagnenseite angezeigt wird. Sie benötigen diesen Wert beim Erstellen Ihrer API-Anfrage. Optional können Sie sich auch die **Nachrichtenvarianten-ID** notieren – fügen Sie sie in Ihre Anfrage ein, wenn Sie Versandstatistiken einer bestimmten Nachrichtenvariante zuordnen möchten.

## 2. Schritt: Eine E-Mail über die API senden

Erstellen Sie eine POST-Anfrage an den [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)-Endpunkt. Fügen Sie die Kampagnen-ID, die externe Nutzer-ID der Empfängerin bzw. des Empfängers und den E-Mail-Inhalt in den Anfrage-Payload ein.

{% alert important %}
Jede in `external_user_ids` referenzierte Empfängerin bzw. jeder Empfänger muss bereits in Braze existieren. Reine API-Sendungen erstellen keine neuen Nutzerprofile. Wenn Sie Nutzer:innen im Rahmen eines Versands erstellen müssen, verwenden Sie zuerst [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) oder nutzen Sie stattdessen eine [API-getriggerte Kampagne]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Beispielanfrage

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Ersetzen Sie `YOUR_REST_ENDPOINT` durch die [REST-Endpunkt-URL]({{site.baseurl}}/api/basics/#endpoints) für Ihren Workspace.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

Ersetzen Sie die Platzhalter-Werte durch Ihre tatsächlichen IDs. Das Feld `from` muss das Format `"Anzeigename <email@adresse.com>"` verwenden. Das Feld `body` akzeptiert gültiges HTML und unterstützt [Liquid-Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), sodass Sie den E-Mail-Inhalt für jede Empfängerin und jeden Empfänger individuell anpassen können. Die vollständige Liste der vom E-Mail-Messaging-Objekt unterstützten Parameter finden Sie unter [E-Mail-Objekt]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

Nachdem Sie die Anfrage erstellt haben, senden Sie die POST-Anfrage von Ihrem Backend-Dienst an die Braze REST API.

## 3. Schritt: Ihre Integration überprüfen

Nachdem Sie die Einrichtung abgeschlossen haben, überprüfen Sie Ihre Integration:

1. Senden Sie eine API-Anfrage wie in [2. Schritt](#step-2-send-an-email-using-the-api) beschrieben und verwenden Sie Ihre eigene Nutzer-ID als Empfänger:in.
2. Bestätigen Sie, dass die E-Mail in Ihrem Posteingang zugestellt wird.
3. Gehen Sie im Braze-Dashboard zur Kampagnenergebnisseite und bestätigen Sie, dass der Versand aufgezeichnet wurde.
4. Überwachen Sie die Ergebnisse genau, während Sie Ihre Kampagne skalieren.

## Hinweise

- Stellen Sie sicher, dass Ihre E-Mail-Kampagnen den relevanten Vorschriften entsprechen, wie z. B. der DSGVO und CAN-SPAM, indem Sie die erforderlichen Abmeldeoptionen und Datenschutzhinweise einbinden. Weitere Informationen finden Sie unter [Nutzer-Abos verwalten]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) und [Best Practices für E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/).
- Verwenden Sie die [Personalisierungs-Features]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) von Braze, um E-Mail-Inhalte auf individuelle Verbraucher:innen zuzuschneiden, einschließlich dynamischem Content und nutzerspezifischen Daten.
- Die Braze REST API bietet zusätzliche [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/) zum Planen von Nachrichten, Triggern von Kampagnen und mehr.