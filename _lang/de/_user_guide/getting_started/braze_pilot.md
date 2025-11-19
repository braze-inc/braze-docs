---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot ist eine mobile App, die für eine nahtlose Verbindung mit Ihrem Braze-Dashboard konzipiert ist. Damit können Sie Kampagnen und Canvase in die App einführen und so die Nachrichten von Braze auf Ihrem eigenen Telefon zum Leben erwecken. Braze Pilot enthält eine Bibliothek mit App-Simulationen für fiktive Marken, die verschiedene Branchen repräsentieren. So ist es zulässig, dass Sie erleben, wie Ihr Messaging aus der Sicht Ihrer Kunden aussehen könnte."
description: "Sehen Sie sich die verschiedenen Möglichkeiten an, wie Sie mit Braze Nachrichten vom Braze-Dashboard auf Ihr Telefon senden können."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Erste Schritte mit Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Daten Wörterbuch
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Deeplinks
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulationen von Pilot-Apps

Das Herzstück von Braze Pilot ist seine Bibliothek mit App-Simulationen. Jede App ist eine realistische Simulation einer fiktiven, branchenspezifischen Marke, die mit einer Vielzahl von Ereignissen und Attributen ausgestattet ist, die endlose Opportunitäten für die Umsetzung gängiger Braze-Anwendungsfälle schaffen.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington ist eine Fitness App mit Workouts, Trainingszielen und einem Steppington+ Premium Dienst. Es bietet mehrere Stellen zur Demonstration von [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), einen Bereich, der mit [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags) aufgedeckt werden kann, und eine robuste Bibliothek mit angepassten Event-Protokollen, die es ermöglichen, viele Customer Journeys für diese Branche zu illustrieren.

![Die Homepage von Steppington mit Symbolen für Marathontraining, Yoga, Radfahren und Gewichte.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### HosenLabyrinth

PantsLabyrinth ist eine E-Commerce App, die (Sie haben es erraten) Hosen verkauft! Die PantsLabyrinth App enthält eine vollständige Warenkorb-Kassenfunktion, eine optionale Wunschliste, die mit einem Feature-Flag aktiviert werden kann, und viele Opportunitäten für schlaue Witze mit Freunden aus Großbritannien.

![Eine Produktseite für PantsLabyrinth mit Optionen, um Jeans in den Warenkorb zu legen.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon ist ein Dienst zum Streamen, der perfekt zur Veranschaulichung gängiger Braze Anwendungsfälle rund um das Engagement für Inhalte geeignet ist. 

![Die MovieCanon App mit verschiedenen Thrillern zum Anschauen.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Wie sich Pilot mit Ihrem Braze-Dashboard verbindet

Das Braze SDK ist ein Code-Paket, das Daten von Ihren Nutzern:innen sammelt, sobald es in Ihre App oder Website integriert ist. Wenn Sie Pilot mit Ihrem Dashboard verbinden, initialisieren Sie diese Verbindung zwischen der Pilot-App auf Ihrem Telefon und dem Braze SDK und stellen eine eindeutige Verbindung mit Ihrer Braze-Instanz her, indem Sie Pilot Ihren API-Schlüssel als Bezeichner für Ihr Dashboard übergeben.

![Der erste Schritt zur Einrichtung von Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Nachdem Pilot eine Verbindung zu Ihrem Braze-Dashboard hergestellt hat, funktioniert das Braze SDK in der App genauso wie bei der Integration des SDK in Ihre eigene App oder Website. Das heißt, Braze wird:

- Speichern Sie Daten über Ihre Nutzer:in in Pilot, einschließlich angepasster Daten für die fiktiven Marken in der App.
- Erfassen Sie automatisch Sitzungsdaten, Gerätedaten und Push-Token.
- Leistungsstarke Push-Benachrichtigungen, In-App-Nachrichten und Messaging-Kanäle für Content-Cards, die eine SDK-Integration erfordern, um zu funktionieren.

Mehr über das Braze SDK finden Sie unter [Integration]({{site.baseurl}}/user_guide/getting_started/integration).

![Der Customer-Engagement-Stack von Braze, der Integrationen, APIs, SDKs für Datenaufnahme, Klassifizierung, Orchestrierung, Personalisierung und Aktionen mit Messaging-Kanälen für eine interaktive Feedback-Schleife mit Ihren Kunden umfasst.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Nutzerprofile in Braze

Alle Daten, die an Braze gesendet werden, werden in einem Nutzerprofil gespeichert, das einem bestimmten Nutzer:innen Ihrer App oder Website zugeordnet ist. Sobald Sie Pilot mit Ihrem Braze-Dashboard verbinden, beginnt Braze mit der Aufzeichnung von Daten über Sie als Nutzer:in von Pilot. Es gibt zwei Arten von Nutzern:in, die über diese Verbindung für Sie erstellt werden können: anonyme und identifizierte.

### Anonym 

Dieser Verbindungsstatus repräsentiert die Erfahrung eines Gastes Ihrer App oder Website, der sich noch nicht angemeldet hat. Wenn Sie Pilot als anonymer Nutzer initialisieren, erstellt Braze ein [anonymes Nutzerprofil]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) für Sie und protokolliert dort Daten über Ihre Aktivitäten. Anonyme Nutzer:innen können weiterhin mit Kampagnen angesprochen werden, aber Sie können ihr Nutzerprofil nicht direkt in Ihrem Braze-Dashboard einsehen.

### Bezeichner

Dieser Verbindungsstatus bedeutet, dass Braze Ihr Nutzerprofil anhand eines eindeutigen Bezeichners erkennt, der Ihnen zugewiesen wurde und als externer Bezeichner bezeichnet wird. Sie können auf der Seite **Benutzersuche** Ihres Dashboards nach diesem externen Bezeichner suchen, um Ihr Nutzerprofil zu finden, in dem alle Attribute und Ereignisse gespeichert sind, die von Pilot auf der Grundlage Ihrer Aktivitäten in der App protokolliert wurden.

![Ein Beispiel für ein Braze Nutzerprofil für Nutzer:in "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Verbindungstyp

Um zu prüfen, welche Art von Verbindung Sie haben, können Sie den Verbindungsstatus oben rechts auf Ihrem Bildschirm überprüfen.

{% tabs local %}
{% tab Anonymous user  %}

**Anonym** bedeutet, dass Sie Daten als anonymer Nutzer:in protokollieren.

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

Wenn Sie Daten als identifizierter Nutzer protokollieren, wird neben Ihrer externen ID ein Benutzersymbol angezeigt.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**Nicht verbunden** bedeutet, dass Sie die Verbindung zwischen Braze SDK und Pilot noch nicht initialisiert haben.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Kampagnen und Canvase

Mit Kampagnen und Canvases senden Sie Nachrichten an Ihre Nutzer. 

- Kampagnen eignen sich am besten für einzelne Nachrichten, die über verschiedene Kanäle an ein bestimmtes Zielgruppensegment gesendet werden. 
- Canvases sind fortschrittliche Kampagnen-Workflows, mit denen Sie personalisierte Customer Journeys über mehrere Kanäle hinweg automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvase sorgen für eine konsistente und nahtlose Kommunikation über verschiedene Berührungspunkte hinweg und erhöhen so die Chancen auf Customer-Engagement und Konversion.

## Unterstützte Messaging-Kanäle

Braze Pilot unterstützt derzeit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), die in Ihrer App erscheinen und zeitnahe Nachrichten zustellen, während sich der Nutzer:in aktiv engagiert.

![Eine In-App-Nachricht in der MovieCanon App "Gefällt Ihnen MovieCanon? Empfehlen Sie Ihre Freunde!" mit der Möglichkeit, Ihre E-Mail Adresse einzugeben, um eine Empfehlung zu senden.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}