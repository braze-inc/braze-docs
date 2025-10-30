---
nav_title: Canvas Grundlagen
article_title: Canvas-Grundlagen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen von Canvas und geht auf verschiedene Fragen ein, die Sie sich bei der Einrichtung Ihres ersten Canvas stellen sollten."
tool: Canvas

---

# Canvas Grundlagen

> Dieser Referenzartikel behandelt die Grundlagen von Canvas und geht auf verschiedene Fragen ein, die Sie sich bei der Einrichtung Ihres ersten Canvas stellen sollten. Wir erklären Ihnen auch die fünf W's (was, wann, wer, warum und wo) der Visualisierung und wie Sie damit Ihr Canvas gestalten und definieren können.

## Verstehen der Canvas-Struktur

Bevor wir uns mit den Feinheiten der [Canvas-Einrichtung]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) befassen, sollten wir die wichtigsten Bestandteile eines Canvas identifizieren.

{% tabs %}
  {% tab Canvas %}
  Canvas ist eine einheitliche Schnittstelle, über die Marketer Kampagnen mit mehreren Nachrichten erstellen können. Es ist ein bisschen wie ein visuelles Programmierwerkzeug, mit dem Sie aus einer Reihe von Schritten eine zusammenhängende Nutzer:in erstellen können.

  \![Ein Beispiel für ein Canvas mit einem Decision-Split-Schritt, der in zwei verschiedene Nutzer:innen unterteilt ist, je nachdem, ob ein Nutzer:in Push aktiviert ist.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Journey %}

  Eine Reise, häufig als User Journey bezeichnet, ist die Erfahrung eines einzelnen Nutzers oder einer einzelnen Nutzerin innerhalb des Canvas.<br><br> \![Ein Chart mit der Customer Journey für eine neue Nutzer:in. Ein anonymer Nutzer:in installiert eine App, Kat erstellt ein Konto, Kat öffnet die App eine Woche lang nicht, eine Push-Benachrichtigung bringt Kat zurück zur App, dann nutzt Kat die App regelmäßig.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas Builder %}
  Der Canvas-Builder zeigt Ihnen die Schritte, die Sie bei der Erstellung Ihres Canvas ausführen müssen. Dazu gehören Grundlagen wie das Benennen Ihres Canvas und das Hinzufügen von Teams. Im Grunde genommen ist der Canvas-Builder die entscheidende Einrichtung, die Sie benötigen, bevor Sie mit der Erstellung Ihres Canvas beginnen können. Hier können Sie die Art und Weise steuern, wie Ihre Nutzer ihre Kundenreise beginnen und abschließen, indem Sie den [Zeitplan für die Eingabe]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), die [Zielgruppe]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) und die [Sendeeinstellungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings) bearbeiten.<br><br> \![Der Canvas-Builder im Abschnitt Grundlagen für einen Canvas namens "Neuer Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  Eine Variante ist der Weg, dem jede Kund:in auf ihrer Reise folgt. Canvas unterstützt bis zu acht Varianten mit einer Kontrollgruppe. Sie bestimmen, welches Segment Ihrer Zielgruppe jeder Variante folgen wird.<br><br> \![Auswählen des Buttons "Variante hinzufügen".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Steps %}
  Ein Canvas-Schritt ist ein Marketing-Entscheidungspunkt: "wenn dies, dann das." Nutzen Sie [Canvas-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components), um die Schritte einer Nutzer:in zu erstellen.<br><br> \![Beispiel für das Hinzufügen eines Verzögerungsschritts zu einem Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Wenn ein Nutzer:innen einen Canvas betritt, beginnt er mit dem ersten Schritt. Jeder Schritt hat Bedingungen, die bestimmen, ob ein Nutzer:innen zum nächsten Schritt übergehen kann. Innerhalb eines Schrittes können Sie Trigger setzen oder die Zustellung planen, das Targeting durch Hinzufügen von Filtern oder Markieren von Ausnahme-Events verfeinern und verschiedene Kanäle wie Push-Benachrichtigungen oder Webhook-Events festlegen. In Canvas erfolgen die Schritte in einer Reihenfolge, d.h. der erste Schritt erfolgt, bevor der zweite Schritt erfolgen kann. Nehmen wir an, wir haben einen Canvas mit den folgenden Schritten: Verzögerungsschritt A mit einer 24-stündigen Verzögerung, Nachrichtenschritt A mit einer Push-Nachricht und Nachrichtenschritt B mit einer In-App-Nachricht. Nutzer:in wird in einer 24-stündigen Verzögerung gehalten. Nach 24 Stunden erhält er eine Push-Nachricht, dann eine In-App-Nachricht.

  {% endtab %}
{% endtabs %}

## Aufbau der Customer Journey

Mithilfe der fünf W's (was, wann, wer, warum und wo) der Visualisierung können Sie Ihre Customer-Engagement-Strategien ermitteln, um eine personalisierte Nachricht für jeden Ihrer Nutzer:innen zu erstellen.

### Das "Was": Benennen Sie Ihr Canvas

> Was wollen Sie dem Benutzer helfen zu tun oder zu verstehen?

Unterschätzen Sie niemals die Macht des Namens. Braze wurde für die Zusammenarbeit entwickelt. Dies ist also ein guter Zeitpunkt, um sich darüber klar zu werden, wie Sie Ihre Ziele mit Ihrem Team kommunizieren werden.

Sie können Tags hinzufügen und die Schritte und Varianten in einem Canvas benennen. Wenn Sie mehr über Customer Journeys erfahren möchten, lesen Sie unseren Braze-Lernkurs zur [Abbildung von Nutzerlebenszyklen](https://learning.braze.com/mapping-customer-lifecycles).

### Das "Warum": Bezeichner für Konversions-Events

> Ausgehend von dem "Was", warum bauen Sie dieses Canvas? 

Es ist immer wichtig, ein definiertes Ziel vor Augen zu haben, und Canvas hilft Ihnen dabei, zu verstehen, wie Ihre Performance im Hinblick auf KPIs wie Engagement, Käufe und angepasste Events aussieht.

Wenn Sie mindestens ein [Konversions-Event]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) auswählen, können Sie nachvollziehen, wie Sie die Performance innerhalb des Canvas optimieren können. Und wenn Ihr Canvas mehrere Varianten oder eine Kontrollgruppe hat, verwendet Braze das Konversionsereignis, um die beste Variante zum Erreichen dieses Ziels zu ermitteln.

* **Sitzung beginnen**: Ich möchte, dass meine Nutzer:innen wiederkommen und sich mit der App beschäftigen.
* **Kaufen**: Ich möchte, dass meine Nutzer kaufen.
* **Angepasstes Event durchführen**: Ich möchte, dass meine Benutzer eine bestimmte Aktion ausführen, die ich als benutzerdefiniertes Ereignis verfolge.
* **Upgraden Sie die App:** Ich möchte, dass meine Benutzer ihre App-Version aktualisieren.

### Das "wenn": Startbedingungen schaffen

> Wann wird ein Benutzer diese Erfahrung machen?

Ihre Antwort bestimmt die Details, wann und wie Ihr Canvas Ihren Kund:innen zugestellt wird. Benutzer können Ihr Canvas auf eine von zwei Arten betreten: durch geplante oder aktionsbasierte Auslöser.

{% alert tip %}
Unter [Zeitbasierte Funktionen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) für Canvas finden Sie weitere Strategien und Antworten auf häufige Fragen.
{% endalert %}

Mit der zeitgesteuerten Zustellung können Sie ein Canvas sofort an Ihre Zielgruppe senden. Sie können sie auch regelmäßig versenden lassen oder für einen bestimmten Zeitpunkt in der Zukunft planen. Aktionsbasierte Werbemittel reagieren auf bestimmte Verhaltensweisen von Kunden, sobald diese auftreten. Ein aktionsbasierter Trigger kann zum Beispiel das Öffnen einer App, einen Kauf, die Interaktion mit einer anderen Kampagne oder das Auslösen eines angepassten Events sein. An dem Punkt, an dem die Aktion stattfindet, können Sie das Canvas an Ihre Nutzer:innen senden lassen.

### Das "Wer": Zielgruppe auswählen

> Wen versuchen Sie zu erreichen? 

Um Ihr "Wer" zu definieren, können Sie vordefinierte Segmente verwenden, die in Canvas verfügbar sind. Sie können auch weitere Filter hinzufügen, um Ihre Targeting-Zielgruppe noch gezielter anzusprechen. Nachdem Sie diese Segmente zusammengestellt haben, können nur die Nutzer:innen, die den Kriterien der Zielgruppe entsprechen, an der Canvas-Reise teilnehmen, was zu einem stärker personalisierten Erlebnis führt. In dieser Tabelle finden Sie eine Übersicht über die verfügbaren Filter und wie sie Ihre Benutzer für Ihren Anwendungsfall segmentieren.

| Filter              | Beschreibung                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Benutzerdefinierte Daten         | Segmentieren Sie Nutzer:innen auf der Grundlage von Events und Attributen, die Sie definieren. Sie können spezielle Funktionen für Ihr Produkt verwenden. |
| Benutzer Aktivität       | Segmentieren Sie Kund:innen auf der Grundlage ihrer Aktionen und Käufe.                                             |
| Retargeting         | Segmentieren Sie Kund:innen, die frühere Canvase gesendet, erhalten oder mit ihnen interagiert haben.               |
| Marketing Aktivität  | Segmentieren Sie Kunden auf der Grundlage universeller Verhaltensweisen wie dem letzten Engagement.                         |
| Nutzerattribute     | Segmentieren Sie Kunden nach ihren konstanten Eigenschaften und Merkmalen.                                 |
| Install-Attribution | Segmentieren Sie Kunden nach ihrer ersten Quelle, Anzeigengruppe, Kampagne oder Anzeige.                                 |

### Das "Wo": Meine Zielgruppe finden

> Wo kann ich mein Publikum am besten erreichen? 

Hier bestimmen wir, welche Messaging-Kanäle für Ihre Nutzer:innen am sinnvollsten sind. Idealerweise möchten Sie Ihre Nutzer dort erreichen, wo sie am besten erreichbar sind. In diesem Sinne können Sie jeden der folgenden Kanäle mit Canvas verwenden:
* [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS oder MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### Das "Wie": Erstellen Sie das komplette Erlebnis

> Wie baue ich meine Canvas-Reise auf, nachdem ich die fünf W's identifiziert habe?

Das "Wie" fasst zusammen, wie Sie Ihr Canvas erstellen und wie Sie Ihre Nutzer:innen mit Ihrer Nachricht erreichen werden. Damit eine Nachricht wirksam ist, sollten Sie beispielsweise das Timing Ihrer Nachrichten im Hinblick auf die Zeitzonen Ihrer verschiedenen Nutzer optimieren.

Die Antwort auf die Frage "Wie" bestimmt auch die Kadenz, in der Sie ein Canvas an Ihre Zielgruppe senden (z. B. einmal pro Woche oder alle zwei Wochen), und welche Messaging-Kanäle Sie für jedes Canvas nutzen, das Sie wie bei der Frage "Wo" beschrieben erstellen.

## Anwendungsfall: Ablauf des Onboarding von Kund:in

Nehmen wir zum Beispiel an, Sie sind Marketer bei MovieCanon, einem Anbieter von Online-Streaming-Diensten, und Sie sind für die Erstellung eines Onboarding-Flusses für neue Nutzer Ihrer App zuständig. Indem wir uns auf die fünf W's beziehen, können wir das Canvas folgendermaßen aufbauen.

* **Was**: Unser Canvas wird den Namen "Neue Onboarding Journey" tragen.
* **Warum**? Das Ziel unseres Canvas ist es, unsere Nutzer willkommen zu heißen und sie dazu zu bringen, sich weiterhin mit der App zu beschäftigen.
* **Wann**: Nachdem ein Benutzer die App zum ersten Mal geöffnet hat, möchten wir ihm eine E-Mail zur Begrüßung schicken. 
* **Wer**: Wir richten uns an neue Nutzer, die unsere App zum ersten Mal verwenden.
* **Wo**: Wir sind zuversichtlich, dass wir neue Nutzer über ihre E-Mail erreichen können, so wie wir es in der Vergangenheit immer gemacht haben.
* **Wie**: Wir möchten eine Verzögerung von einem Tag festlegen, um unsere neuen Nutzer:innen nicht mit Benachrichtigungen zu überhäufen. Nach dieser Verzögerung senden wir eine E-Mail mit einer Liste der beliebtesten Filme und Fernsehsendungen, um sie zur weiteren Nutzung der App zu bewegen.

## Allgemeine Tipps

### Bestimmen Sie, wann und wie Sie Schritte und Varianten verwenden

Jeder Canvas muss mindestens eine Variante und mindestens einen Schritt haben. Von da an sind Ihnen keine Grenzen mehr gesetzt. Wie entscheiden Sie sich also für die Form Ihrer Canvas? Hier kommen Ihre Ziele, Daten und Hypothesen ins Spiel. Das Brainstorming zum "Wie" und "Wo" wird Ihnen helfen, die richtige Form und Struktur Ihres Canvas zu entwerfen.

### Rückwärts arbeiten

Einige Ziele haben kleinere Unterziele. Wenn Sie zum Beispiel einen kostenlosen Nutzer in ein Abonnement umwandeln möchten, benötigen Sie eine Seite, auf der Sie Ihre Abonnementdienste vorstellen. Ein Besucher muss die Optionen sehen, bevor er sie kauft. Sie können Ihre Messaging-Bemühungen darauf konzentrieren, ihnen diese Seite vor einer Kassenseite zu zeigen. Wenn Sie rückwärts arbeiten, um die Reise zu verstehen, die ein:e Kundin durchlaufen muss, um Ihr Ziel zu erreichen, ist das der Schlüssel, um ihn zur Konversion zu führen.

### Mischen Sie Ihr Messaging

Haben Sie in der Vergangenheit eine ähnliche Kampagne durchgeführt? Oder läuft gerade eine? Versuchen Sie, diese eine Nachricht zu verwenden und sie noch persönlicher zu gestalten. Versuchen Sie einen neuen Filter oder fügen Sie eine weitere Nachricht hinzu. Überwachen Sie Ihre Leistung und optimieren Sie sie durch schrittweise Änderungen, während Sie Ihre Kommunikationstechniken ändern.
