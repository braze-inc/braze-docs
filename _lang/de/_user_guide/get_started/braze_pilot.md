---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot ist eine mobile App, die für die nahtlose Verbindung mit Ihrem Braze-Dashboard entwickelt wurde. Dies ermöglicht es Ihnen, Kampagnen und Canvases in der App einzuführen und Braze-Nachrichten auf Ihrem eigenen Smartphone zum Leben zu erwecken. Braze Pilot umfasst eine Bibliothek mit App-Simulationen für fiktive Marken aus verschiedenen Branchen, mit denen Sie erleben können, wie Ihre Nachrichten aus Kundensicht wirken könnten."
description: "Informieren Sie sich über die verschiedenen Möglichkeiten, wie Sie Braze nutzen können, um Nachrichten vom Braze-Dashboard auf Ihr Telefon zu senden."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Erste Schritte mit Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Datenwörterbuch
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Deeplinks
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Pilot-App-Simulationen

Der Kern von Braze Pilot ist die Bibliothek mit App-Simulationen. Jede App stellt eine realistische Simulation einer branchenspezifischen fiktiven Marke dar und ist so konzipiert, dass sie eine Vielzahl von Ereignissen und Attributen protokolliert, die unzählige Möglichkeiten für gängige Braze-Anwendungsfälle bieten.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington ist eine Fitness-App mit Trainingsprogrammen, Trainingszielen und einem Steppington+ Premium-Dienst. Es bietet mehrere Möglichkeiten zur Demonstration von[ Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), einen Bereich, der mit [Feature-Flag]({{site.baseurl}}/developer_guide/feature_flags) freigeschaltet werden kann, sowie eine umfangreiche Bibliothek mit angepassten Events, mit denen sich viele Customer Journeys für diese Branche veranschaulichen lassen.

![Die Startseite von Steppington mit Symbolen für das Trainieren für den Marathon, Yoga, Radfahren und Krafttraining.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### Hosenlabyrinth

PantsLabyrinth ist eine E-Commerce-App, die (Sie haben es erraten) Hosen verkauft. Die PantsLabyrinth-App umfasst ein vollständiges Warenkorb-Kasse-Erlebnis, eine optionale Wunschliste, die mit einem Feature-Flag aktiviert werden kann, sowie zahlreiche Möglichkeiten für humorvolle Interaktionen mit Freunden aus Großbritannien.

![Eine Produktseite für PantsLabyrinth mit Optionen zum Hinzufügen von Jeans zum Warenkorb.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### Filmkanon 

MovieCanon ist ein Streaming-Dienst, der ideal geeignet ist, um gängige Anwendungsfälle von Braze im Bereich Content-Engagement zu veranschaulichen. 

![Die MovieCanon-App mit einer Auswahl an verschiedenen Thrillern zum Anschauen.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Wie Pilot mit Ihrem Braze-Dashboard verbunden wird

Das Braze SDK ist ein Code-Paket, das Daten von Ihren Nutzer:innen sammelt, sobald es in Ihre App oder Website integriert ist. Wenn Sie Pilot mit Ihrem Dashboard verbinden, initialisieren Sie diese Verbindung zwischen der Pilot-App auf Ihrem Smartphone und dem Braze SDK und stellen eine eindeutige Verbindung zu Ihrer Braze-Instanz her, indem Sie Pilot Ihren API-Schlüssel-Bezeichner für Ihr Dashboard mitteilen.

![Der erste Schritt zur Einrichtung von Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Nachdem Pilot eine Verbindung zu Ihrem Braze-Dashboard hergestellt hat, funktioniert das Braze SDK in der App genauso wie nach der Integration des SDK in Ihre eigene App oder Website. Dies bedeutet, dass Braze:

- Speichern Sie Daten zu Ihren Benutzeraktivitäten in Pilot, einschließlich angepasster Daten, die für die fiktiven Marken in der App spezifisch sind.
- Sammeln Sie automatisch Sitzungsdaten, Gerätedaten und Push-Token.
- Power-Push-Benachrichtigungen, In-App-Nachrichten und Content-Card-Messaging-Kanäle, die eine SDK-Integration erfordern, um zu funktionieren.

Weitere Informationen zum Braze SDK finden Sie unter [Integration]({{site.baseurl}}/user_guide/getting_started/integration).

![Der Braze-Engagement-Stack umfasst Integrationen, APIs, SDKs für die Datenaufnahme, Klassifizierung, Orchestrierung, Personalisierung und Maßnahmen mit Messaging-Kanälen für einen interaktiven Feedback-Loop mit Ihren Kunden.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Nutzerprofile in Braze

Jede an Braze übermittelte Daten wird in einem Nutzerprofil gespeichert, das einem bestimmten Nutzer Ihrer App oder Website zugeordnet ist. Sobald Sie Pilot mit Ihrem Braze-Dashboard verbunden haben, beginnt Braze mit der Protokollierung von Daten über Sie als Nutzer:in von Pilot. Es gibt zwei Arten von Nutzer:innen, die über diese Verbindung für Sie erstellt werden können: anonyme Nutzer:innen und identifizierte Nutzer:innen.

### Anonym 

Dieser Verbindungsstatus spiegelt die Erfahrung eines Gastes Ihrer App oder Website wider, der sich noch nicht angemeldet hat. Wenn Sie Pilot als anonyme:r Nutzer:in initialisieren, erstellt Braze ein [anonimes Nutzerprofil]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) für Sie und protokolliert dort Daten zu Ihren Aktivitäten. Anonyme Nutzer:innen können weiterhin mit Kampagnen angesprochen werden, jedoch ist es nicht möglich, ihr Nutzerprofil direkt in Ihrem Braze-Dashboard aufzurufen.

### Identifiziert

Dieser Verbindungsstatus bedeutet, dass Braze Ihr Nutzerprofil anhand eines Ihnen zugewiesenen eindeutigen Bezeichners, der sogenannten externen Kennung, erkennt. Sie können auf der Seite **„Nutzersuche“** Ihres Dashboards nach diesem externen Bezeichner suchen, um Ihr Nutzerprofil zu finden, in dem alle Benutzerattribute und Ereignisse gespeichert sind, die von Pilot basierend auf Ihren Aktivitäten in der App protokolliert wurden.

![Ein Beispiel für ein Braze-Nutzerprofil für die Nutzer:in „torchie-208117“.]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Verbindungstyp

Um zu überprüfen, welche Art von Verbindung Sie haben, können Sie den Verbindungsstatus oben rechts auf Ihrem Bildschirm überprüfen.

{% tabs local %}
{% tab Anonymous user  %}

**Anonym** bedeutet, dass Sie Daten als anonyme:r Nutzer:in protokollieren.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

Wenn Sie Daten als identifizierte Nutzer:in protokollieren, wird neben Ihrer externen ID ein Benutzersymbol angezeigt.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**„Nicht verbunden“** bedeutet, dass Sie die Verbindung des Braze SDK mit Pilot noch nicht initialisiert haben.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Kampagnen und Canvase

Mit Kampagnen und Canvases senden Sie Nachrichten an Ihre Nutzer. 

- Kampagnen eignen sich am besten für einzelne Nachrichten, die über verschiedene Kanäle an ein bestimmtes Zielgruppensegment gesendet werden. 
- Canvases sind fortschrittliche Kampagnen-Workflows, mit denen Sie personalisierte Customer Journeys über mehrere Kanäle hinweg automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvases tragen dazu bei, eine konsistente und nahtlose Kommunikation über verschiedene Kontaktpunkte hinweg sicherzustellen, wodurch die Chancen für Customer-Engagement und Konversion erhöht werden.

## Unterstützte Messaging-Kanäle

Braze Pilot unterstützt derzeit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), die in Ihrer App angezeigt werden und zeitnahe Nachrichten übermitteln, während der Nutzer:in aktiv mit der App interagiert.

![Eine In-App-Nachricht in der MovieCanon-App: „Gefällt Ihnen MovieCanon? Refernzieren Sie Ihre Bekannten! Mit der Option, Ihre E-Mail-Adresse einzugeben, um eine Empfehlung zu versenden.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}