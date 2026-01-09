---
nav_title: Konnektor der Kampagne
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "In diesem Artikel erfahren Sie, was Campaign Connector ist und wie Sie ihn verwenden, um gezielte, relevante Inhalte zum richtigen Zeitpunkt zu liefern."

---
# Campaign Connector

> Mit dem Konnektor für Kampagnen können Sie Kampagnen erstellen, die ausgelöst werden, wenn Nutzer:innen mit aktiven Kampagnen interagieren. Sie können zielgerichtete, relevante Inhalte zum richtigen Zeitpunkt zustellen.

## Funktionsweise

Mit dieser Funktion können Sie Nutzer ansprechen, die die folgenden Interaktionen mit aktiven Kampagnen durchführen:

- In-App-Nachricht anzeigen
- In-App-Nachricht anklicken
- Klicken Sie auf die Schaltflächen für In-App-Nachrichten
- E-Mail anklicken
- Alias in E-Mail anklicken
- E-Mail öffnen
- Push-Benachrichtigung direkt öffnen
- Klicken Sie auf die Schaltfläche Push-Benachrichtigung
- Klicken Sie auf Push-Story Seite
- Konversions-Event durchführen
- E-Mail erhalten
- SMS empfangen
- Klicken Sie auf den verkürzten SMS-Link
- Push-Benachrichtigung erhalten
- Webhook empfangen
- in einer Kontrollgruppe eingeschrieben sind
- Inhaltskarte ansehen
- Inhaltskarte anklicken
- Inhaltskarte verwerfen

{% alert important %}
Campaign Connector-Trigger können nicht verwendet werden, um In-App-Nachrichtenkampagnen auszulösen. In-App-Nachrichten können nur durch SDK-Ereignisse ausgelöst werden, z. B. benutzerdefinierte Ereignisse oder den Start einer Sitzung. Weitere Informationen finden Sie unter [Eine In-App-Nachricht erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).
{% endalert %}

### Regeln für die Zustellung

Beachten Sie, dass Sie den Campaign Connector nicht verwenden können, um eine Nachricht an einen Nutzer:innen zu senden, nachdem dieser eine Interaktion mit einer Kampagne abgeschlossen hat. Wenn Sie beispielsweise eine Marketing-Kampagne neun Wochen lang laufen lassen und zu Beginn der vierten Woche eine Folgekampagne einrichten, die den Campaign Connector verwendet, werden in der Folgekampagne nur Nachrichten an Nutzer:innen zugestellt, die mit der Marketing-Kampagne interagiert haben, nachdem die Folgekampagne veröffentlicht wurde (Wochen 4-9). Um sicherzustellen, dass Ihre Folgekampagnen alle Nutzer:innen erreichen, auf die Sie das Targeting ausrichten, sollten Sie daher:

- Richten Sie Ihre ursprüngliche Kampagne als Entwurf ein
- Einrichten und Veröffentlichen Ihrer Folgekampagne
- Veröffentlichen Sie die ursprüngliche Kampagne

Diese Zustellungsregeln sind besonders wichtig beim Targeting von Nutzer:innen, die in einer Kontrollgruppe eingeschrieben sind, eine E-Mail oder eine Push-Benachrichtigung erhalten. Da die Benutzer in die Kontrollgruppe aufgenommen werden, sobald Sie die ursprüngliche Kampagne veröffentlichen, müssen Sie die Folgekampagne veröffentlichen, bevor Sie die ursprüngliche Kampagne veröffentlichen. Ähnlich verhält es sich, wenn Sie die ursprüngliche Kampagne vor der Folgekampagne veröffentlichen. Dann erhalten viele Nutzer:innen Ihre E-Mail und/oder Push-Benachrichtigung, bevor die Folgekampagne veröffentlicht wird.

## Verwendung von Campaign Connector mit Ihren Kampagnen

### Schritt 1: Erstellen Sie eine neue Kampagne

Verfassen Sie die Nachrichten, die Sie an Ihre Benutzer senden möchten. Je nach Anwendungsfall können Sie eine Kampagne mit einem Kanal oder einer Multichannel-Kampagne auswählen.

### Schritt 2: Interaktion und Zielkampagne auswählen

1. Wählen Sie [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) und fügen Sie den Auslöser "Mit Kampagne interagieren" hinzu, um Nutzer:innen anzusprechen, die mit einer aktiven Kampagne interagieren. 
2. Wählen Sie die auslösende Interaktion. 
3. Als Nächstes wählen Sie die aktive Kampagne aus, die Sie als Targeting verwenden möchten.

![]({% image_buster /assets/img_archive/Campaign_Connector1.png %})

### Schritt 3: Zeitplanverzögerung einstellen und Ausnahmen hinzufügen (optional)

Wenn Sie sich für eine Zeitplanverzögerung entscheiden, können Sie der Aktion triggern eine Ausnahme hinzufügen. Sie könnten zum Beispiel eine E-Mail-Kampagne erneut an Benutzer senden, die die ursprüngliche E-Mail nicht geöffnet haben.  In diesem Szenario können Sie "Empfangene E-Mail" als Trigger wählen und eine Zeitplanverzögerung von einer Woche festlegen. Dann können Sie "E-Mail öffnen" als Ausnahme hinzufügen. Jetzt senden Sie die E-Mail erneut an Benutzer, die die ursprüngliche E-Mail nicht innerhalb einer Woche nach Erhalt geöffnet haben.

![]({% image_buster /assets/img_archive/Campaign_Connector3.png %})

Ausnahme-Events werden nur ausgelöst, wenn ein:e Nutzer:in auf den Empfang der Nachricht wartet, mit der sie verbunden sind. Wenn ein:e Nutzer:in die Aktion ausführt, bevor er auf die Nachricht wartet, wird das Ausnahme-Event nicht ausgelöst.

### Schritt 4: Mit der Erstellung der Kampagne fortfahren

Fahren Sie mit der Erstellung Ihrer Kampagne fort, wie Sie es normalerweise tun würden. Beachten Sie: Wenn Sie sicherstellen möchten, dass Sie jedem Nutzer, der mit einer bestimmten Kampagne interagiert, eine Nachricht schicken, dann ist es am besten, wenn Sie ein Segment auswählen, das alle Nutzer Ihrer App enthält.

## Anwendungsfälle

Sie können Campaign Connector verwenden, um Nutzer anzusprechen, die sich an aktiven Kampagnen beteiligen oder nicht beteiligen.

So können Sie z.B. gezielt Nutzer ansprechen, die auf eine Push-Nachricht geklickt haben, in der ein kostenloser Versand beworben wurde, um ihnen eine Push-Nachricht zu schicken, in der ein Rabatt von 15% auf einen Einkauf beworben wird.

Der Kampagnen Konnektor kann auch Nutzer:innen zusammenstellen, die eine Push-Benachrichtigung erhalten, die sie daran erinnert, dass sie ihren Warenkorb-Abbruch vorgenommen haben. So können Sie beispielsweise die Benachrichtigung erneut an Benutzer senden, die sie nicht direkt geöffnet haben. Sie werden jedoch wahrscheinlich Nutzer ausschließen wollen, die seit dem Versand der ursprünglichen Benachrichtigung einen Kauf getätigt haben, auch wenn sie diese nicht direkt geöffnet haben. Sie können diesen Anwendungsfall erreichen, indem Sie einen Trigger "Empfangene Push-Benachrichtigung" für die Kampagne "Warenkorb-Abbruch" hinzufügen, eine Zeitplan-Verzögerung festlegen und "Kauf tätigen" und "Direkt geöffnete Push-Benachrichtigungen" als Ausnahmen hinzufügen.

