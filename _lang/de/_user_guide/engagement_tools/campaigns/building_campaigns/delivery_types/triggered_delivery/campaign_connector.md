---
nav_title: Campaign Connector
article_title: Campaign Connector
page_order: 2
tool: Campaigns
page_type: tutorial
description: "In diesem Artikel erfahren Sie, was Campaign Connector ist und wie Sie ihn verwenden, um gezielte, relevante Inhalte zum richtigen Zeitpunkt zu liefern."

---
# Campaign Connector

> Mit Campaign Connector können Sie Kampagnen erstellen, die ausgelöst werden, wenn Nutzer mit aktiven Kampagnen oder News Feed-Karten interagieren. Dieses Feature ist nützlich, weil es Ihnen ermöglicht, gezielte, relevante Inhalte zum richtigen Zeitpunkt zuzustellen. 

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

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

Sowie Nutzer:innen, die die folgenden Interaktionen mit aktiven Newsfeed-Cards durchführen:

- Anzeigen
- Klick

## Regeln für die Zustellung

Die Funktion Campaign Connector funktioniert nur mit aktiven Kampagnen. Außerdem können Sie den Campaign Connector nicht verwenden, um einem Benutzer eine Nachricht zu senden, nachdem er eine Interaktion mit einer Kampagne abgeschlossen hat. Wenn Sie z.B. eine Marketingkampagne neun Wochen lang laufen lassen und zu Beginn der vierten Woche eine Folgekampagne einrichten, die Campaign Connector nutzt, wird die Folgekampagne nur Nachrichten an Nutzer liefern, die mit der Marketingkampagne interagiert haben, nachdem die Folgekampagne veröffentlicht wurde (Wochen 4-9). Um sicherzustellen, dass Ihre Folgekampagnen alle Nutzer:innen erreichen, auf die Sie das Targeting ausrichten, sollten Sie daher:

- Richten Sie Ihre ursprüngliche Kampagne als Entwurf ein
- Einrichten und Veröffentlichen Ihrer Folgekampagne
- Veröffentlichen Sie die ursprüngliche Kampagne

Diese Zustellungsregeln sind besonders wichtig beim Targeting von Nutzer:innen, die in einer Kontrollgruppe eingeschrieben sind, eine E-Mail oder eine Push-Benachrichtigung erhalten. Da die Benutzer in die Kontrollgruppe aufgenommen werden, sobald Sie die ursprüngliche Kampagne veröffentlichen, müssen Sie die Folgekampagne veröffentlichen, bevor Sie die ursprüngliche Kampagne veröffentlichen. Ähnlich verhält es sich, wenn Sie die ursprüngliche Kampagne vor der Folgekampagne veröffentlichen. Dann erhalten viele Nutzer:innen Ihre E-Mail und/oder Push-Benachrichtigung, bevor die Folgekampagne veröffentlicht wird.

## Wie Sie die Funktion Campaign Connector verwenden

### Schritt 1: Erstellen Sie eine neue Kampagne

Verfassen Sie die Nachrichten, die Sie an Ihre Benutzer senden möchten. Sie können eine klassische Kampagne oder eine Kampagne mit nur einem Kanal auswählen, je nach Anwendungsfall.

### Schritt 2: Interaktion und Zielkampagne auswählen

Sie können Nutzer ansprechen, die mit einer aktiven Kampagne interagieren, oder Nutzer, die mit einer aktiven News Feed-Karte interagieren.

#### Targeting von Nutzer:innen, die mit einer Kampagne interagieren

Wählen Sie [Aktionsbasierte Zustellung][7] und fügen Sie den Trigger "Mit Kampagne interagieren" hinzu. Wählen Sie dann die auslösende Interaktion. Als Nächstes wählen Sie die aktive Kampagne aus, die Sie als Targeting verwenden möchten.

![][4]

#### Nutzer anvisieren, die mit einer News Feed-Karte interagieren (veraltet)

Wählen Sie **Aktionsbasierte Zustellung** und fügen Sie den Trigger "Mit Karte interagieren" hinzu. Wählen Sie dann, ob Sie Nutzer:innen, die eine Newsfeed-Card ansehen, oder Nutzer:innen, die auf eine Newsfeed-Card klicken, als Zielgruppe zusammenstellen möchten. Wählen Sie die aktive Newsfeed-Card aus, für die Sie ein Targeting durchführen möchten.

![][5]

### Schritt 3: Legen Sie eine Zeitverzögerung fest und fügen Sie bei Bedarf Ausnahmen hinzu

Wenn Sie sich für eine Zeitplanverzögerung entscheiden, können Sie der Aktion triggern eine Ausnahme hinzufügen. Sie könnten zum Beispiel eine E-Mail-Kampagne erneut an Benutzer senden, die die ursprüngliche E-Mail nicht geöffnet haben.  In diesem Szenario können Sie "Empfangene E-Mail" als Trigger wählen und eine Zeitplanverzögerung von einer Woche festlegen. Dann können Sie "E-Mail öffnen" als Ausnahme hinzufügen. Jetzt senden Sie die E-Mail erneut an Benutzer, die die ursprüngliche E-Mail nicht innerhalb einer Woche nach Erhalt geöffnet haben.

![][6]

Ausnahme-Events werden nur ausgelöst, wenn ein:e Nutzer:in auf den Empfang der Nachricht wartet, mit der sie verbunden sind. Wenn ein:e Nutzer:in die Aktion ausführt, bevor er auf die Nachricht wartet, wird das Ausnahme-Event nicht ausgelöst.

### Schritt 4: Mit der Erstellung der Kampagne fortfahren

Fahren Sie mit der Erstellung Ihrer Kampagne fort, wie Sie es normalerweise tun würden. Beachten Sie: Wenn Sie sicherstellen möchten, dass Sie jedem Nutzer, der mit einer bestimmten Kampagne interagiert, eine Nachricht schicken, dann ist es am besten, wenn Sie ein Segment auswählen, das alle Nutzer Ihrer App enthält.

## Anwendungsfälle

Sie können Campaign Connector verwenden, um Nutzer anzusprechen, die sich an aktiven Kampagnen beteiligen oder nicht beteiligen.

So können Sie z.B. gezielt Nutzer ansprechen, die auf eine Push-Nachricht geklickt haben, in der ein kostenloser Versand beworben wurde, um ihnen eine Push-Nachricht zu schicken, in der ein Rabatt von 15% auf einen Einkauf beworben wird.

Oder Sie können Nutzer:innen, die in einer In-App-Nachricht zum Onboarding auf einen Deeplink geklickt haben, eine weitere In-App-Nachricht schicken, in der zusätzliche Features hervorgehoben werden.  Auf diese Weise können Sie gezielt Nutzer ansprechen, die gezeigt haben, dass sie daran interessiert sind, mehr über die Funktionen Ihrer Anwendung zu erfahren, und vermeiden es, Nutzer zu verärgern, die diese Funktionen lieber selbst entdecken möchten.

Der Kampagnen Konnektor kann auch Nutzer:innen zusammenstellen, die eine Push-Benachrichtigung erhalten, die sie daran erinnert, dass sie ihren Warenkorb-Abbruch vorgenommen haben. So können Sie beispielsweise die Benachrichtigung erneut an Benutzer senden, die sie nicht direkt geöffnet haben. Sie werden jedoch wahrscheinlich Nutzer ausschließen wollen, die seit dem Versand der ursprünglichen Benachrichtigung einen Kauf getätigt haben, auch wenn sie diese nicht direkt geöffnet haben. Sie können diesen Anwendungsfall erreichen, indem Sie einen Trigger "Empfangene Push-Benachrichtigung" für die Kampagne "Warenkorb-Abbruch" hinzufügen, eine Zeitplan-Verzögerung festlegen und "Kauf tätigen" und "Direkt geöffnete Push-Benachrichtigungen" als Ausnahmen hinzufügen.

[4]: {% image_buster /assets/img_archive/Campaign_Connector1.png %}
[5]: {% image_buster /assets/img_archive/Campaign_Connector2.png %}
[6]: {% image_buster /assets/img_archive/Campaign_Connector3.png %}
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/