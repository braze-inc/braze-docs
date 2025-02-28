---
nav_title: Bote
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Facebook Messenger, einer der beliebtesten Instant-Messaging-Plattformen der Welt."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) ist eine der beliebtesten Instant-Messaging-Plattformen der Welt und wird von fast einer Milliarde monatlich aktiver Nutzer verwendet. Über diese Plattform können Marken ansprechende Chatbots erstellen, die intelligent und automatisch mit ihren Kunden interagieren.

Die Braze- und Facebook-Integration nutzt die Webhooks, Segmentierungs-, Personalisierungs- und Triggering-Funktionen von Braze, um Ihren Benutzern über die Messenger Platform API Nachrichten im Facebook Messenger zu senden. Eine benutzerdefinierte Facebook Messenger-Webhook-Vorlage ist in unserer Plattform unter **Vorlagen** > **Webhook-Vorlagen** enthalten.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Die Facebook-Messenger-Plattform ist für "nicht-werbliche Nachrichten gedacht, die eine bereits bestehende Transaktion erleichtern, andere Kundensupport-Aktionen anbieten oder von einer Person angeforderte Inhalte liefern". Weitere Informationen finden Sie in [den Richtlinien der Facebook-Plattform](https://developers.facebook.com/docs/messenger-platform) und in den [Beispielen für akzeptable Anwendungsfälle](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Voraussetzungen

Bestätigen Sie die folgenden Punkte, bevor Sie mit der Integration fortfahren:
- Facebook erlaubt die Nutzung der Messenger-Plattform nicht, um Marketing-Nachrichten zu versenden. 
- Sie benötigen die ausdrückliche Erlaubnis des Benutzers für Nachrichten von Ihrer Seite. 
- Um Nachrichten an Nutzer zu senden, die keine Testnutzer Ihrer Facebook-App sind, muss Ihre App die [App-Prüfung](https://developers.facebook.com/docs/messenger-platform/app-review) von Facebook bestehen.<br><br>

| Anforderung| Herkunft| Zugang| Beschreibung|
| ---| ---| ---|
| Facebook Messenger Seite| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Eine Facebook-Seite wird als Identität Ihres Bots verwendet. Wenn Menschen mit Ihrer App chatten, sehen sie den Seitennamen und das Profilbild.|
| Facebook Messenger App| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Die Facebook-App enthält die Einstellungen für Ihren Messenger-Bot, einschließlich der Zugriffstoken.
| App Bot Überprüfung und Genehmigung | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Wenn Sie bereit sind, Ihren Bot für die Öffentlichkeit freizugeben, müssen Sie ihn bei Facebook zur Überprüfung und Genehmigung einreichen. Dieser Überprüfungsprozess ermöglicht es uns, sicherzustellen, dass Ihr Messenger-Bot unsere Richtlinien einhält und wie erwartet funktioniert, bevor er für alle Messenger-Nutzer verfügbar gemacht wird. |
| Seitenbereichs-IDs (PSIDs) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Sie benötigen die PSIDs der Benutzer, um Nachrichten im Facebook Messenger zu versenden. Wenn ein Benutzer über den Messenger mit Ihrer App interagiert, erstellt Facebook eine PSID. Diese PSID kann als benutzerdefiniertes String-Attribut an Braze gesendet werden.
| Zugriffstoken für die Seite | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Diese Zugriffstoken ähneln den Benutzerzugriffstoken, mit dem Unterschied, dass sie APIs die Berechtigung erteilen, die Daten einer Facebook-Seite zu lesen, zu schreiben oder zu ändern. Um ein Seitenzugriffstoken zu erhalten, müssen Sie ein Benutzerzugriffstoken erhalten und nach dem `manage_pagespermission` fragen. Nachdem Sie das Benutzerzugriffstoken haben, erhalten Sie das Seitenzugriffstoken über die Graph API.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Im Folgenden wird gezeigt, wie Sie einen Braze Facebook Messenger Webhook einrichten.
Für diejenigen, die zusätzliche Hilfe bei der Einrichtung Ihres Bots benötigen, finden Sie ein vollständiges Messenger-Bot-Tutorial und Beispielcode im [Braze GitHub Repository](https://github.com/Appboy/appboy-fb-messenger-bot)!

### Schritt 1: Sammeln Sie Ihre PSIDs

Um Nachrichten im Facebook Messenger zu versenden, müssen Sie die seitenbezogenen IDs (PSIDs) Ihrer Nutzer erfassen, um sie zu identifizieren und mit ihnen konsistent zu interagieren. PSIDs sind nicht dasselbe wie die Facebook-ID des Benutzers. Facebook erstellt diese Kennung jedes Mal, wenn Sie einem Kunden eine Nachricht senden oder wenn ein Kunde Ihnen eine Nachricht sendet.

PSIDs können über einen der verschiedenen [Einstiegspunkte](https://developers.facebook.com/docs/messenger-platform/discovery) gefunden werden, die Facebook bietet. Wenn der Benutzer eine Nachricht an Ihre App sendet oder eine Aktion in einer Konversation durchführt, z. B. auf eine Schaltfläche tippt oder eine Nachricht sendet, wird seine PSID in die `sender.id` Eigenschaft des Webhook-Ereignisses aufgenommen, so dass Ihr Bot erkennen kann, wer die Aktion durchgeführt hat.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

Wann immer Sie eine Nachricht senden, wird ihre PSID in die `recipient.id` Eigenschaft der Anfrage aufgenommen, um zu identifizieren, wer die Nachricht erhalten soll.

### Schritt 2: An Braze als benutzerdefiniertes Attribut senden

Sobald Sie sicher sind, dass Sie PSIDs erhalten, koordinieren Sie dies mit Ihren Entwicklern, damit diese die PSIDs als [benutzerdefiniertes Attribut]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes) an Braze senden. PSIDs sind Zeichenketten, auf die durch einen [API-Aufruf](https://developers.facebook.com/docs/messenger-platform/reference/send-api) zugegriffen werden kann.

### Schritt 3: Einrichten Ihrer Webhook-Vorlage

Gehen Sie unter **Vorlagen & Medien** zu **Webhook-Vorlagen** und wählen Sie die **Facebook Messenger Webhook-Vorlage**.

1. Geben Sie einen Vorlagennamen an und fügen Sie bei Bedarf Teams und Tags hinzu.
2. Geben Sie Ihre Nachricht ein oder wählen Sie eine der [von Facebook zur Verfügung gestellten](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) Nachrichtenvorlagen aus. Sie können auch die [Art](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) Ihrer Nachricht oder den [Tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) auswählen.
3. Fügen Sie die PSID als benutzerdefiniertes Attribut ein. Verwenden Sie dazu die blau-weiße Schaltfläche **+** in der Ecke des Feldes **Anfragetext**.
3. Fügen Sie Ihr Seitenzugriffstoken in die Webhook-URL ein, indem Sie `FACEBOOK_PAGE_ACCESS_TOKEN` durch Ihr Token ersetzen.

#### Vorschau und Test Ihres Webhooks

Bevor Sie Ihre Nachricht senden, testen Sie Ihren Webhook. Vergewissern Sie sich, dass Ihre Messenger-ID in Braze gespeichert ist (oder suchen Sie sie und testen Sie sie als benutzerdefinierter Benutzer), und verwenden Sie die Vorschau, um die Testnachricht zu senden:

![Die Registerkarte Test in der Facebook Messenger Webhook-Vorlage zeigt, dass Sie eine Vorschau der Nachricht anzeigen können, indem Sie sie an einen bestehenden Benutzer senden.][60]

Wenn Sie die Nachricht erfolgreich empfangen haben, können Sie die Zustellungseinstellungen konfigurieren.

## Mit dieser Integration

Einmal eingerichtet, können Sie diese Integration nutzen, um Facebook Messenger-Nutzer anzusprechen. Wenn Sie keine Nachrichten über die Telefonnummern der Benutzer versenden und planen, Messenger-Nachrichten wiederholt zu versenden, sollten Sie [ein Segment][62] für alle Benutzer erstellen, für die die Messenger-ID als benutzerdefiniertes Attribut existiert, und [analytics tracking][61] aktivieren, um Ihre Messenger-Abonnementraten im Laufe der Zeit zu verfolgen. 

![Segmentfilter "messenger_id" auf "ist nicht leer" gesetzt.][63]

Wenn Sie sich dafür entscheiden, kein spezielles Segment für Messenger-Abonnenten zu erstellen, stellen Sie sicher, dass Sie einen Filter für die vorhandene Messenger-ID einfügen, um Fehler zu vermeiden.

Sie können auch andere Segmentierungen verwenden, um Ihre Messenger-Kampagnen auf die Zielgruppe auszurichten, und den Rest der Kampagnenerstellung wie bei jeder anderen Kampagne.

[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}