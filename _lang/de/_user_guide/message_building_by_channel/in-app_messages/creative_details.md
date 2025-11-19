---
nav_title: Kreative Details
article_title: Kreative Details
page_order: 3.5
layout: dev_guide
guide_top_header: "Kreative Details"
guide_top_text: "Bevor Sie mit unseren In-App-Nachrichten kreativ werden, sollten Sie einige der Richtlinien kennen. Alle Templates für In-App-Nachrichten sind so konzipiert, dass sie auf modernen Geräten unterschiedliche Textlängen und Bildgrößen anzeigen. Um sicherzustellen, dass Ihre Nachricht auf allen Handys, Tablets und Computern gut angezeigt wird, empfehlen wir Ihnen, die folgenden Richtlinien zu befolgen und <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>Ihre Nachrichten</a> vor der Veröffentlichung immer <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>zu testen</a>."
description: "Dieser Landing-Hub deckt die Design- und Content-Anforderungen für die drei Arten von In-App-Nachrichten ab: Modal, Slideup und Vollbild."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Spezifikationen nach Nachrichtentyp"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Vollbild"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Content-Richtlinien

### Text

Für In-App-Nachrichtentexte oder Kopfzeilen empfehlen wir Ihnen, sich kurz und bündig zu fassen - ein bis zwei Zeilen für Kopfzeilen und bis zu drei Zeilen für Textkörper. Nach drei Zeilen muss die Nachricht wahrscheinlich vertikal gescrollt werden, und die Nutzer:innen beschäftigen sich möglicherweise nicht mit dem gesamten Inhalt. Der Schwellenwert, der das Scrollen auslöst, kann je nach Größe des Endgeräts des Benutzers, dem benutzerdefinierten Styling oder dem Vorhandensein von Bildern in den Nachrichten variieren, aber drei Zeilen sind normalerweise sicher.

Wenn Sie die neueste Generation von In-App-Nachrichten (Generation 3) verwenden, werden Sie feststellen, dass die Schriftarten standardmäßig auf die Standardschriftart des Betriebssystems Sans Serif für iOS und Android eingestellt sind. Web-In-App-Nachrichten werden standardmäßig in Helvetica angezeigt.

### Bilder

Unsere Richtlinien für Bilder sind stärker strukturiert als die für Text, da wir sicherstellen möchten, dass Ihre Botschaften wie beabsichtigt und auf Handys, Tablets und Computern aller Modelle und Größen gut dargestellt werden.

Im Allgemeinen empfiehlt Braze, Bilder zu verwenden, die auf einen 16:10-Bildschirm passen.

- **Alle Bilder müssen kleiner als 5 MB sein.**
- Wir akzeptieren nur die Dateitypen PNG, JPEG und GIF.
- Wir empfehlen, Bilder in der [Bibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) zu hosten, damit das Braze-SDK-Assets von unserem CDN herunterladen kann, um Nachrichten offline anzuzeigen.
- Für Vollbildnachrichten befolgen Sie unsere Richtlinien für die [sichere Bildzone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} Erstellen Sie Assets mit Vertrauen! Unsere Templates für In-App-Nachricht-Bilder und Overlays für die sichere Zone sind so konzipiert, dass sie auf Geräten aller Größen gut funktionieren. [Download Design-Vorlagen ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

![In-App-Nachricht im Vollbildmodus, die den Bildschirm einer App einnimmt. Die Nachricht im Vollbildmodus enthält ein großes Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Layout | Asset-Größe | Anmerkungen |
|--- | --- | --- |
| Bild + Text | Seitenverhältnis 6:5<br>Hochauflösend 1200 x 1000 px<br> Minimum 600 x 500 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus |
| Nur Bild | Seitenverhältnis 3:5<br>Hochauflösend 1200 x 2000 px<br> Minimum 600 x 1000 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Weitere Details für Vollbildschirme]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialog erscheint. Das Modal enthält ein Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Layout | Asset-Größe | Anmerkungen |
|--- | --- | ------ |
| Bild + Text | 29:10 Seitenverhältnis<br>Hohe Auflösung 1450 x 500 px<br> Minimum 600 x 205 px | Große Bilder werden verkleinert und horizontal zentriert. Breite Bilder werden am linken und rechten Rand abgeschnitten. |
| Nur Bild | Nahezu jedes Seitenverhältnis<br>Hohe Auflösung bis zu 1200 x 2000 px<br> Minimum 600 x 600 px | Die Nachricht passt sich an die meisten Bildformate an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Weitere Details für Modale]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

![Slideup In-App-Nachricht, die am unteren Rand des App-Bildschirms erscheint. Das Slideup enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Layout | Asset-Größe | Anmerkungen |
|--- | --- | --- |
| Bild + Text | Seitenverhältnis 1:1<br>Hochauflösend 150 x 150 px<br> Minimum 50 x 50 px | Bilder mit unterschiedlichen Seitenverhältnissen passen in einen quadratischen Bildcontainer, ohne dass sie beschnitten werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Weitere Details für Slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFs und Videos

Braze unterstützt derzeit GIFs für In-App-Nachrichten im Web (inbegriffen), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) und iOS (inbegriffen), sofern diese während der gewünschten Plattformintegration aktiviert wurden. Weitere Informationen zu Videos in In-App-Nachrichten finden Sie in unserer [Dokumentation zur Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Zusätzliche Überlegungen

In-App-Nachrichten von Braze haben sowohl globale als auch individuelle kreative Vorgaben. Weitere Informationen zur vollständigen Anpassung von In-App-Nachrichten finden Sie auf unserer Seite [Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

<br>
