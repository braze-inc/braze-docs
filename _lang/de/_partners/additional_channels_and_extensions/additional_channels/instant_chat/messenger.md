---
nav_title: Messenger
article_title: Facebook Messenger
alias: /partners/messenger/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Facebook Messenger, einer der weltweit beliebtesten Plattformen für Instant Messaging."
page_type: partner
search_tag: Partner

---

# Facebook Messenger

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/) ist eine der beliebtesten Instant Messaging-Plattformen der Welt, die von fast einer Milliarde monatlich aktiver Nutzer:innen genutzt wird. Über diese Plattform können Marken ansprechende Chatbots erstellen, die intelligent und automatisch mit ihren Kund:in interagieren.

Die Braze- und Facebook-Integration nutzt Braze-Webhooks, Segmentierung, Personalisierung und Triggering Features, um Ihren Benutzern im Facebook Messenger über die Messenger Platform API Nachrichten zu senden. Eine angepasste Facebook Messenger Webhook-Vorlage ist in unserer Plattform unter **Templates** > **Webhook Templates** enthalten.

Die Facebook Messenger-Plattform ist für "nicht werbliche Nachrichten gedacht, die eine bereits bestehende Transaktion erleichtern, andere Aktionen zur Kundenbetreuung anbieten oder von einer Person angefragte Inhalte liefern." Weitere Informationen finden Sie in [den Richtlinien der Facebook-Plattform](https://developers.facebook.com/docs/messenger-platform) und in den [Beispielen für akzeptable Anwendungsfälle](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable).

## Voraussetzungen

Bestätigen Sie die folgenden Punkte, bevor Sie mit der Integration fortfahren:
- Facebook lässt die Nutzung der Messenger-Plattform zum Versenden von Marketing Nachrichten nicht zu. 
- Sie benötigen die ausdrückliche Zustimmung des Nutzers:innen für Nachrichten von Ihrer Seite. 
- Um Nachrichten an Nutzer:innen zu senden, die keine Testnutzer:innen Ihrer Facebook App sind, muss Ihre App die [App-Prüfung](https://developers.facebook.com/docs/messenger-platform/app-review) von Facebook bestehen.<br><br>

| Anforderung| Herkunft| Zugang| Beschreibung|
| ---| ---| ---|
| Facebook Messenger Seite| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Eine Facebook-Seite wird als Identität für Ihren Bot verwendet. Wenn Menschen mit Ihrer App chatten, sehen sie den Seitennamen und das Profilbild.|
| Facebook Messenger App| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Die Facebook App enthält die Einstellungen für Ihren Messenger Bot, einschließlich der Zugangstoken.
| App Bot Überprüfung und Genehmigung | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | Wenn Sie bereit sind, Ihren Bot für die Öffentlichkeit freizugeben, müssen Sie ihn bei Facebook zur Überprüfung und Genehmigung einreichen. Mit diesem Überprüfungsprozess können wir sicherstellen, dass Ihr Messenger-Bot unsere Richtlinien einhält und wie erwartet funktioniert, bevor wir ihn für alle Nutzer des Messengers verfügbar machen. |
| Seitenbereichs-IDs (PSIDs) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Sie benötigen die PSIDs der Nutzer:innen, um Nachrichten im Facebook Messenger zu versenden. Wenn ein Nutzer:innen über Messenger mit Ihrer App interagiert, erstellt Facebook eine PSID. Diese PSID kann als angepasstes Attribut in Form eines Strings an Braze gesendet werden.
| Token für den Zugriff auf die Seite | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | Diese Token ähneln den Nutzer:innen-Zugriffstoken, mit dem Unterschied, dass sie APIs die Erlaubnis erteilen, die Daten einer Facebook-Seite zu lesen, zu schreiben oder zu ändern. Um ein Token für den Seitenzugriff zu erhalten, müssen Sie ein Token für den Nutzer:innen erhalten und nach dem `manage_pagespermission` fragen. Nachdem Sie den Nutzer:innen-Zugangstoken haben, erhalten Sie den Seitenzugangstoken über die Graph API.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Im Folgenden wird gezeigt, wie Sie einen Braze Facebook Messenger Webhook einrichten.
Wenn Sie zusätzliche Hilfe bei der Einrichtung Ihres Bots benötigen, finden Sie im [GitHub-Repository von Braze](https://github.com/Appboy/appboy-fb-messenger-bot) ein vollständiges Tutorial zum Messenger-Bot und Beispielcode!

### Schritt 1: Sammeln Sie Ihre PSIDs

Um Nachrichten im Facebook Messenger zu versenden, müssen Sie die seitenbezogenen IDs (PSIDs) Ihrer Nutzer:innen erfassen, um Ihre Nutzer:innen zu identifizieren und einheitlich mit ihnen zu interagieren. PSIDs sind nicht dasselbe wie die Facebook ID der Nutzer:innen. Facebook erstellt diesen Bezeichner jedes Mal, wenn Sie einem Kunden eine Nachricht senden oder wenn ein Kunde Ihnen eine Nachricht sendet.

PSIDs können über einen der verschiedenen [Eingänge](https://developers.facebook.com/docs/messenger-platform/discovery), die Facebook bietet, gefunden werden. Nachdem der Nutzer eine Nachricht an Ihre App geschickt oder eine Aktion in einer Konversation durchgeführt hat, wie z.B. das Antippen eines Buttons oder das Senden einer Nachricht, wird seine PSID in die Eigenschaft `sender.id` des Webhook-Ereignisses aufgenommen, so dass Ihr Bot erkennen kann, wer die Aktion durchgeführt hat.

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

Wann immer Sie eine Nachricht senden, wird ihre PSID in die Eigenschaft `recipient.id` der Anfrage aufgenommen, um zu identifizieren, wer die Nachricht erhalten soll.

### Schritt 2: An Braze als angepasstes Attribut senden

Sobald Sie sicher sind, dass Sie PSIDs erhalten, koordinieren Sie dies mit Ihren Entwickler:in, um die PSIDs als [angepasstes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#custom-attributes) an Braze zu senden. PSIDs sind Strings, auf die durch einen [API-Aufruf](https://developers.facebook.com/docs/messenger-platform/reference/send-api) zugegriffen werden kann.

### Schritt 3: Richten Sie Ihr Webhook Template ein

Gehen Sie unter **Templates und Medien** zu **Webhook Templates** und wählen Sie das **Facebook Messenger Webhook Template**.

1. Geben Sie einen Template-Namen an und fügen Sie Teams und Tags hinzu, falls erforderlich.
2. Geben Sie Ihre Nachricht ein oder wählen Sie ein Template aus den [von Facebook zur Verfügung gestellten](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) Nachrichten. Sie können auch die [Art](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) Ihrer Nachricht oder Ihren [Tag](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) auswählen.
3. Fügen Sie die PSID als angepasstes Attribut ein. Verwenden Sie dazu den blau-weißen Button **"+"** in der Ecke des Feldes **"Anfrage"**.
3. Fügen Sie Ihr Token für den Seitenzugriff in die Webhook-URL ein, indem Sie `FACEBOOK_PAGE_ACCESS_TOKEN` durch Ihr Token ersetzen.

#### Vorschau und Test Ihres Webhooks

Bevor Sie Ihre Nachricht versenden, testen Sie Ihren Webhook. Vergewissern Sie sich, dass Ihre Messenger ID in Braze gespeichert ist (oder suchen Sie sie und testen Sie als angepasster Nutzer:in), und verwenden Sie die Vorschau, um die Testnachricht zu versenden:

![Tab "Test" in der Facebook Messenger Webhook-Vorlage, der Ihnen eine Vorschau der Nachricht zeigt, indem Sie sie an einen bestehenden Nutzer:innen senden.]({% image_buster /assets/img_archive/fbm-test.png %})

Wenn Sie die Nachricht erfolgreich empfangen haben, können Sie die Einstellungen für die Zustellung konfigurieren.

## Verwendung dieser Integration

Sobald Sie diese Integration eingerichtet haben, können Sie Nutzer:innen des Facebook Messenger als Targeting nutzen. Wenn Sie Nachrichten nicht über die Telefonnummern der Nutzer versenden und planen, Messenger-Nachrichten wiederholt zu versenden, sollten Sie für alle Nutzer:innen [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment), für die die Messenger ID als angepasstes Attribut existiert, und das [Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) aktivieren, um Ihre Messenger-Abonnementraten im Laufe der Zeit zu verfolgen. 

![Segment Filter "messenger_id" auf "ist nicht leer" gesetzt.]({% image_buster /assets/img_archive/fbm-segmentation.png %})

Wenn Sie sich dafür entscheiden, kein spezielles Segment für Messenger Abonnenten zu erstellen, stellen Sie sicher, dass Sie einen Filter für die vorhandene Messenger ID einfügen, um Fehler zu vermeiden.

Sie können auch andere Segmentierungen für das Targeting Ihrer Messenger Kampagnen verwenden und den Rest des Prozesses der Kampagnenerstellung wie bei jeder anderen Kampagne.

