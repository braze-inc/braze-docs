---
nav_title: Newsfeed-Artikel erstellen
article_title: Newsfeed-Artikel erstellen
page_order: 3
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie Newsfeed-Artikel erstellen. Mit News Feed-Elementen können Sie permanente Inhalte direkt von unserem Web-Dashboard aus in Ihre App einfügen."
channel: news feed
hidden: true


---

# Newsfeed-Artikel erstellen

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Mit News Feed-Elementen können Sie permanente Inhalte direkt von unserem Web-Dashboard aus in Ihre App einfügen. Und noch besser: Der News Feed lässt sich wie alle unsere anderen Nachrichtentypen auch auf einzelne Segmente ausrichten. Das bedeutet, dass das, was Sie im Feed sehen, völlig anders aussehen kann als bei einer anderen Person. Die Möglichkeiten für den News-Feed sind nahezu grenzenlos.

Beispiele und hilfreiche Tipps zu Newsfeeds finden Sie in den [Kundenberichten][13], [Anwendungsbeispielen][15] und [Best Practices][16].

## Schritt 1: Klicken Sie auf Karte erstellen

Zunächst müssen Sie die Art der Newsfeed-Elemente auswählen, die Sie an weiterleiten möchten. Aus dem Dropdown-Menü können Sie einen unserer vier News-Feed-Kartentypen auswählen.

![Die Schaltfläche Karte erstellen im Braze-Dashboard. Die erweiterten Dropdown-Optionen zum Erstellen einer Karte: Klassisch, Bildunterschrift und Banner.][1]

### Spezifikationen der News Feed Karte

#### News Feed Karten

<br>![Eine klassische Kartenvorschau mit dem Facebook-Symbol, einer Kopfzeile mit der Aufschrift "Gefällt mir auf Facebook!" und zwei Textzeilen: "Klicken Sie hier!" und "www.facebook.com".][2]{: style="max-width:40%;"}

Die Standard-Newsfeed-Karten bestehen aus:

- 110x110 Bild
- Titel
- Haupttext
- Link (In-App/Web)

#### Bildkarten mit Untertiteln

<br>![Eine Bildkartenvorschau mit Untertiteln und einem Bild von einem Apfelkuchen und Äpfeln. Unter dem Bild befindet sich eine Überschrift mit der Aufschrift "Holiday Sale! Sparen Sie bis zu 50 Dollar!" mit dem folgenden Text: "Nur für kurze Zeit erhalten Sie vier Premium-Apfelkuchen zum Preis von drei. Beeilen Sie sich! Dieser Deal wird nicht lange halten. Klicken Sie hier zum Einlösen. www.example.com".][3]{: style="max-width:40%;"}

Bildunterschrift-Cards bestehen aus:

- 600x450 Bild
- Titel
- Haupttext
- Link (In-App/Web)

#### Banner-Cards

<br>![Eine Vorschau der Banner-Card mit einem Bild, auf dem "Dies ist ein Banner" steht.][4]{: style="max-width:40%;"}

Bannerkarten bestehen aus:

- 600x100 Bild
- Link (In-App/Web)

#### Leitfaden Bilder

|          Kartentyp         |          Bildseitenverhältnis         | Empfohlene Bildgröße | Maximale Bildgröße |   Dateitypen  |
|:-----------------------------:|:----------------------:|:------------------:|:-------------:|
|          Klassisch         | 1:1 (mindestens 110 Pixel breit) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Bildunterschrift         | 4:3 (mindestens 600 Pixel breit) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Banner         | 6:1 (mindestens 600 Pixel breit) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

- PNG-Dateien werden empfohlen.
- Für die Anzeige von GIFs unter Android ist eine benutzerdefinierte Bildladebibliothek erforderlich. Wir empfehlen Glide.
- Kleine, aber hochwertige Bilder werden schneller geladen. Daher empfiehlt es sich, das kleinstmögliche Bild zu verwenden, um das gewünschte Ergebnis zu erzielen.

## Schritt 2: Fügen Sie einen Titel, eine Zusammenfassung, ein Bild und Links hinzu

Zeit, Ihre News-Feed-Karte zu verfassen! Erstellen Sie einen Titel und eine Zusammenfassung für Ihre Karte und laden Sie ein Bild hoch, das dazu passt. Auf dieser Seite können Sie auch das Linkverhalten einstellen. Dieser Link kann ein Standardlink oder ein [Deeplink][7] zu In-App-Inhalten sein.

![Editor für Newsfeed-Elemente, der den Kartennamen, die Kartenvorschau und Anpassungsdetails für die jeweilige Sprache enthält.][6]

## Schritt 3: Wählen Sie einen Zeitplan aus

Unter dem Editor für die News-Feed-Karte finden Sie Optionen dafür, wann dieser Artikel veröffentlicht werden soll. Sie können es sofort nach der Erstellung veröffentlichen oder einen Zeitpunkt in der Zukunft für die Veröffentlichung festlegen. Sie können die News-Feed-Karte auch zu einer bestimmten Uhrzeit in der Ortszeit Ihrer Benutzer bereitstellen, indem Sie das Kontrollkästchen **Für Benutzer in ihrer Ortszeitzone veröffentlichen** aktivieren.

![][8]

## Schritt 4: Wählen Sie ein Segment

Sie können die Newsfeed-Card so konfigurieren, dass sie beliebige [Segmente][10]] aus dem Dashboard zum gewünschten Zeitpunkt anspricht. Wählen Sie Ihr Zielsegment aus, indem Sie auf das Dropdown-Menü klicken. Hier können Sie allgemeine Statistiken wie E-Mail-Verfügbarkeit und Lifetime-Value nach Benutzer einsehen.

![][11]

## Schritt 5: Details überprüfen und veröffentlichen

Als nächstes werden Sie auf eine Seite weitergeleitet, auf der alle Details zu Ihrer Karte (und ggf. eine In-App-Begleitnachricht) angezeigt werden. Sie können alle Details zu diesen Artikeln überprüfen und bei Bedarf bearbeiten, indem Sie auf das Stiftsymbol in einer der Überschriften klicken.

![][12]

Das war's! Sie sind fertig! Sie haben Ihre erste Newsfeed-Karte veröffentlicht!

## Optional: Verknüpfen Sie eine News Feed-Karte mit einer In-App-Nachricht

Kampagnen auf mehreren Kanälen erhöhen oft Konversionsrate und Engagement. Deshalb ist es bei Braze ganz einfach, In-App-Nachrichten mit bestimmten Newsfeed-Karten zu verknüpfen. 

Nach dem Start einer Newsfeed-Karte erscheint auf der Seite mit den neuen Feed-Statistiken eine Schaltfläche, über die Sie eine "passende In-App-Nachricht erstellen" können. Wenn Sie diese anklicken, gelangen Sie zum Kampagnen-Editor für neue In-App-Kampagnen. Wenn Sie Text, Erscheinungsbild und Handhabung der In-App-Nachricht einrichten, kopiert Braze automatisch die Zustellungs- und Targeting-Regeln der zugehörigen Newsfeed-Karte, damit die Kampagnen gleichzeitig starten.

## Newsfeed organisieren

Sie können Ihre Karten auf der Seite News Feed neu anordnen.
- Die Karten im Feed sind zunächst danach geordnet, ob sie vom Benutzer gesehen wurden oder nicht. Nicht gesehene Artikel stehen ganz oben im Feed.
  - Eine Karte gilt als gelesen, wenn sie einen Abdruck im Feed erhalten hat.
  - Impressionen werden nur gezählt, wenn die Karte im Feed sichtbar ist (d.h. wenn ein Benutzer nicht nach unten scrollt, um eine Karte zu lesen, wird eine Impression nicht gezählt).
- Die Karten sind dann nach Datum und Uhrzeit der Erstellung geordnet, wobei die neueren Artikel zuerst erscheinen.

[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %}
[2]: {% image_buster /assets/img_archive/classiccard.png %}
[3]: {% image_buster /assets/img_archive/captionedimage.png %}
[4]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/news-feed-title-summary_new.png %}
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[8]: {% image_buster /assets/img_archive/newsfeed2_new.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[11]: {% image_buster /assets/img_archive/targetsegment_new.png %}
[12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %}
[13]: https://www.braze.com/customers
[14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
