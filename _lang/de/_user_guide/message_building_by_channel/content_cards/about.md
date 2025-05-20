---
nav_title: Über Content-Cards
article_title: Über Content-Cards
page_order: 0
description: "Dieser Referenzartikel bietet einen Überblick über den Braze Content Card-Kanal und gängige Anwendungsfälle."
channel:
  - content cards
search_rank: 4
---

# [![Braze-Lernkurs]](https://learning.braze.com/content-cards)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Über Content-Cards

> Content-Cards werden direkt in Ihre App oder Website eingebettet, so dass Sie Nutzer:innen ein natürliches und nahtloses Engagement bieten können. Sie geben Ihnen mehr Kontrolle über Ihre App oder Website und ermöglichen es Ihnen, Nachrichteneingänge, Karussells und Banner zu erstellen und die Reichweite anderer Kanäle (wie E-Mail oder Push-Benachrichtigungen) zu erweitern.

Content Cards sind eine Zusatzfunktion und müssen gekauft werden. Wenn Sie Content Cards nutzen möchten, wenden Sie sich an Ihren Braze Customer Success Manager oder unser Support-Team.

{% alert note %}
Wenn Sie unser News Feed-Tool verwenden, empfehlen wir Ihnen, zu unserem Content Cards-Nachrichtenkanal zu wechseln - er ist flexibler, anpassbar und zuverlässig. Auch der Newsfeed wird bald eingestellt. Weitere Informationen erhalten Sie in unserem [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) oder von Ihrem Braze-Kundenbetreuer.
{% endalert %}

## Vorteile der Verwendung von Content Cards

Hier sind nur einige Vorteile der Verwendung von Content Cards gegenüber der Einbindung von Inhalten in Ihre App durch Ihre Entwickler:

- **Leichtere Segmentierung und Personalisierung:** Ihre Nutzerdaten befinden sich in Braze, so dass Sie Ihre Zielgruppe leicht definieren und Ihre Nachrichten mit Content-Cards personalisieren können.
- **Zentralisierte Berichterstattung:** Content-Card-Analysen werden in Braze getrackt, sodass Sie Insights zu all Ihren Kampagnen an einem Standort erhalten.
- **Kohärente Customer Journeys:** Sie können Content-Cards mit anderen Kanälen in Braze kombinieren, um konsistente Kundenerlebnisse zu schaffen. Ein beliebter Anwendungsfall ist das Versenden einer Push-Benachrichtigung und das anschließende Speichern dieser Benachrichtigung als Inhaltskarte in Ihrer App für alle, die nicht auf die Push-Benachrichtigung reagiert haben. Wenn der Inhalt von Ihren Entwicklern direkt in Ihre App eingebaut wird, ist er vom Rest Ihrer Nachrichten isoliert.
- **Kein Opt-in erforderlich:** Ähnlich wie bei In-App-Nachrichten benötigen Content-Cards kein Opt-in und keine Genehmigungen von Ihren Nutzer:innen. Während In-App-Nachrichten jedoch zustimmungsfrei und kurzlebig sind, sind Content-Cards zustimmungsfrei und dauerhaft. Das bedeutet, dass Messaging-Strategien, die In-App-Nachrichten und Content-Cards miteinander kombinieren, ein gutes Gleichgewicht darstellen.
- **Mehr Kontrolle über das Messaging-Erlebnis:** Auch wenn Sie bei der anfänglichen Einrichtung von Content Cards noch die Hilfe Ihrer Entwickler benötigen, können Sie danach die Nachricht, die Empfänger, den Zeitpunkt und vieles mehr direkt von Ihrem Braze-Dashboard aus steuern.

### Content Cards nach Zahlen

Da Sie als Marketer die Content-Cards in Braze selbst erstellen, können Sie Messaging-Updates vornehmen und eine Kapitalrendite erzielen, ohne Ihre App oder Website komplett überarbeiten zu müssen. Hier finden Sie einige hilfreiche Statistiken über den ROI von Content-Cards:

- Content-Cards sind **38-mal** effektiver als E-Mails, wenn es darum geht, die Verkäufe in einem 72-Stunden-Fenster zu steigern.[^1]
- Der Einsatz von Content-Cards in Kampagnen zur Kundenbindung steigert die Konversion um **das Fünffache**[^1].]
- Das Engagement von Nutzer:innen durch Push-Benachrichtigungen, In-App-Nachrichten und Content-Cards führt zu einer **6,9-fachen** Steigerung der Sitzungen im Vergleich zu Nutzern:innen, die nur durch Push-Benachrichtigungen engagiert werden.[^2]
- Das Engagement von Nutzern:innen per E-Mail, In-App-Nachrichten und Content-Cards führt zu einer **3,6-fach** längeren durchschnittlichen Lifetime im Vergleich zu Nutzern:innen, die nur per E-Mail engagiert sind.[^2]

## Funktionsweise

Content-Cards sind im Grunde genommen eine Nutzlast von Daten, nicht das Aussehen der Daten. Braze bietet Template-Ansichten (Banner, Modal, Bildunterschrift), um die Daten der Content-Card anzuzeigen, die letztlich das Aussehen Ihrer Nachricht bestimmen.

Lassen Sie uns nun ein wenig technisch werden. Hinter den Kulissen besteht eine Content-Card im Wesentlichen aus drei Teilen:

- **Modell:** Welche Art von Daten auf der Karte gespeichert sind
- **Ansicht:** So sieht die Karte aus
- **Controller:** Wie der Benutzer mit der Karte interagiert

Bei einer Standardimplementierung fügen Sie den Karteninhalt - das Modell - entweder über das Dashboard oder über APIs hinzu, und die Ansicht und der Controller werden von einem so genannten View Controller verwaltet. Ein View Controller ist der "Klebstoff" zwischen der Gesamtanwendung und dem Bildschirm.

## Anwendungsfälle

In diesem Abschnitt finden Sie einige häufige Anwendungsfälle für Content Cards.

{% alert tip %}
Für weitere Inspirationen empfehlen wir Ihnen unseren [Content Cards Inspiration Guide](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), der über 20 anpassbare Kampagnen enthält, darunter Empfehlungsprogramme, die Einführung neuer Produkte und die Verlängerung von Abonnements.
{% endalert %}

{% tabs %}
{% tab Onboarding und nächste Schritte %}

Wenn neue Benutzer Ihre App und Website erkunden, können Sie ihnen mit strategisch platzierten Inhaltskarten die Werte und Vorteile Ihres Angebots näher bringen. Ermutigen Sie Nutzer:innen mit einer Content-Card auf Ihrer Homepage, sich für andere Kommunikationskanäle zu entscheiden, und speichern Sie ausstehende Onboarding-Aufgaben in einem speziellen Tab, der von Content-Cards unterstützt wird. Vergessen Sie nicht, eine Karte zu entfernen, nachdem ein Nutzer:innen die gewünschte Aufgabe erledigt hat!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event-Teilnahme %}

Präsentieren Sie Content Cards oben auf der Startseite eines Nutzers, um zur Teilnahme an einer Veranstaltung zu ermutigen, und nutzen Sie die Standortausrichtung, um potenzielle Nutzer dort zu erreichen, wo sie sind. Wenn Sie Nutzer zu relevanten physischen Ereignissen einladen, fühlen sie sich als etwas Besonderes, insbesondere mit personalisierten Nachrichten, die ihre früheren Aktivitäten mit Ihrer Marke nutzen.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Empfehlungen %}

Nutzen Sie die Daten, die Sie über das Verhalten und die Vorlieben der Benutzer haben, um relevante Inhalte in Echtzeit auf der Homepage oder in den Inhaltskarten des Posteingangs anzuzeigen und die Benutzer auf Ihr Produktangebot aufmerksam zu machen.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Verkäufe und Aktionen %}

Nutzen Sie Content-Cards, um Nachrichten und nicht beanspruchte Angebote direkt auf Ihrer Homepage oder in einem speziellen Posteingang für Aktionen hervorzuheben. Ziehen Sie relevanten Content heran, der auf den früheren Käufen jedes Kunden oder jeder Kundin basieren, um aufmerksamkeitsstarke, personalisierte Aktionen zu liefern.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Andere Anwendungsfälle

Abgesehen von diesen Hauptanwendungsfällen nutzen unsere Kunden Content Cards auf so viele verschiedene Arten. Die Stärke von Content Cards ist ihre Flexibilität. Wenn der von Ihnen gewünschte Anwendungsfall hier nicht gezeigt wird, können Sie [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) einrichten und die Nutzdaten an Ihre Anwendung oder Website senden.

## Platzierung von Inhaltskarten

In diesem Abschnitt finden Sie die drei gängigsten Möglichkeiten, Content-Cards in Ihrer App oder Website zu platzieren:

- [Posteingang für Nachrichten](#message-inbox)
- [Karussell](#carousel)
- [Banner](#banner)

Die Logik und die Implementierung dieser Platzierungen sind in Braze nicht voreingestellt, so dass Ihr Entwicklungsteam die Arbeit zur Erreichung dieser Anwendungsfälle liefern und unterstützen muss. Einen Überblick über die Implementierung dieser Platzierungen finden Sie unter [Erstellen einer benutzerdefinierten Inhaltskarte]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

![3 Beispiel-Content-Cards, die die verschiedenen Platzierungsoptionen zeigen: Posteingang, Karussell und Banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Posteingang für Nachrichten

![Ein Beispiel für eine Inhaltskarte mit der Platzierung "Nachrichteneingang".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Ein Nachrichteneingang (auch Benachrichtigungszentrale oder Feed genannt) ist ein dauerhafter Ort in Ihrer App oder Website, an dem Sie Content Cards in dem von Ihnen bevorzugten Format anzeigen können. Jede Nachricht im Posteingang ist eine eigene Inhaltskarte. 

Der Posteingang ist eine Standard-Implementierung mit minimalem Entwicklungsaufwand. Braze bietet einen [View Controller](#how-it-works) für einen Posteingang auf iOS, Android und im Internet, um den Erstellungsprozess zu vereinfachen.

#### Vorteile

- Benutzer können viele Karten an einem Ort empfangen
- Effiziente Möglichkeit, Informationen, die Sie auf anderen Kanälen (insbesondere Push-Benachrichtigungen) verpasst oder verworfen haben, wieder aufzugreifen
- Kein Opt-in erforderlich

#### Verhalten

Wenn ein Benutzer für eine Karte in Frage kommt, wird sie automatisch in seinem Posteingang erscheinen. Content Cards sind so konzipiert, dass sie in großen Mengen angezeigt werden können, so dass Benutzer alle Karten, für die sie in Frage kommen, auf einmal sehen können.

Bei der Standardimplementierung können Inhaltskarten im Posteingang als klassische Karten (mit einem Titel, Text und einem optionalen Bild), als reine Bildkarten oder als Karten mit Bildunterschriften erscheinen. Sie wählen aus, wo sich der Nachrichteneingang in Ihrer App befinden soll.

Content Cards werden mit einem Standardstil geliefert, aber Sie können eine benutzerdefinierte Implementierung wählen, um die Karten und den Feed entsprechend dem Look and Feel Ihrer App anzuzeigen.

### Karussell

![Ein Beispiel für eine Content-Card, die die „Karussell“-Platzierung verwendet.]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Karussells zeigen mehrere Inhalte in einem einzigen Bereich an, den Ihre Kunden durch Wischen aufrufen können. Sie können eine Diashow mit Bildern, Text, Videos oder einer Kombination davon sein. Dies ist eine angepasste Implementierung und erfordert ein wenig Arbeit von Ihren Entwickler:innen.

#### Vorteile

- Benutzer können viele Karten an einem Ort empfangen
- Engagierte Art, Empfehlungen zu veröffentlichen

#### Verhalten

Wenn ein Benutzer für eine Karte in Frage kommt, wird sie in einem Karussell auf der Seite Ihrer App angezeigt, zu der das Karussell hinzugefügt wird. Sie können horizontal wischen, um weitere vorgestellte Karten anzuzeigen.

Da es sich um eine benutzerdefinierte Implementierung handelt, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um Ihre eigenen Ansichten zur Anzeige der Inhaltskarten zu erstellen. Die Standardkarten „Klassisch“, „Nur Bild“ und „Bild mit Bildunterschrift“ werden bei dieser Implementierung nicht unterstützt.

### Banner

![Ein Beispiel für eine Inhaltskarte mit der Platzierung "Banner".]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Content-Cards können als dynamisches Banner angezeigt werden, das dauerhaft auf Ihrer Startseite oder oben auf anderen festgelegten Seiten angezeigt wird.

#### Vorteile

- Bleibt im Gegensatz zu einer In-App-Nachricht auf der Seite, sodass Sie mehr Zeit haben, Ihre Zielgruppe zu erreichen.
- Eine gute Möglichkeit, neuen Content an einem prominenten Standort auf Ihrer Startseite zu präsentieren

#### Verhalten

Die Nutzer können die für sie relevanten Inhalte anzeigen und nutzen. Da es sich um eine benutzerdefinierte Implementierung handelt, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um die Ansichten für die Anzeige der Content Cards anzupassen.

## Integration von Content-Cards

Ihre Entwickler:innen werden Content-Cards integrieren, wenn sie das Braze-SDK integrieren. Weitere Einzelheiten zur Integration von Content-Cards finden Sie in den Entwicklerartikeln für Ihre Plattform:

- [iOS]({{site.baseurl}}/developer_guide/platforms/swift/content_cards/ "Content-Card-Integrationsleitfaden für iOS")
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Content-Card-Integrationsleitfaden für Android")
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "Content-Card-Integrationsleitfaden für Web")

## Quellen

<span></span>

[^1]: [8 Tipps, wie Sie das Beste aus Ihren Kampagnen zur Kundenbindung herausholen](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Bericht: Der Unterschied im kanalübergreifenden Marketing](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)