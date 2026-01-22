---
nav_title: Nachrichtentypen
article_title: LINE Nachrichtentypen
page_order: 0
description: "Dieser Artikel behandelt die verschiedenen Arten von LINE-Nachrichten."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# LINE Nachrichtentypen

> Dieser Artikel behandelt LINE-Nachrichtentypen, die Sie verfassen können, sowie Einzelaspekte und Einschränkungen.

Wenn Sie eine LINE-Nachricht verfassen, können Sie Nachrichtentypen per Drag-and-Drop in den Composer ziehen und sie dann anpassen.

\![Panel für Nachrichtentypen mit Nachrichtentypen, die Sie in den Composer-Editor ziehen können, einschließlich Text, Bild, Rich Message und kartenbasierte Nachricht.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Text

Eine LINE-Textnachricht kann bis zu 5.000 Zeichen enthalten und mit Emojis und Liquid personalisiert werden.

Zu den Anwendungsfällen gehören:
- Kündigen Sie eine zeitlich begrenzte Abverkaufsaktion an
- Senden Sie personalisierte Geburtstagsgrüße mit einzigartigen Aktionskarten
- Geben Sie schnell Informationen zu bevorstehenden Ereignissen weiter

\![Eine Textnachricht, die den Nutzer:innen daran erinnert, die Black Friday Party nicht zu vergessen und bis zu 80% vor Mitternacht zu sparen.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Bild

Eine LINE-Bildnachricht kann über die [Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/), eine URL oder Liquid hinzugefügt werden. Die Bilder sind eigenständig und enthalten keine klickbaren Links.

Zu den Anwendungsfällen gehören:
- Präsentieren Sie ein Urlaubsziel, um Benutzer zum Kauf von Flugtickets zu inspirieren.
- Heben Sie Sonderangebote zum Saisonende hervor, um die Nutzer zu ermutigen, sich mit günstigen Angeboten für die Winterkleidung des nächsten Jahres einzudecken.
- Starten Sie einen visuellen Countdown für einen ladenweiten Jahresausverkauf

\![Eine Nachricht, die für den Verkauf eines Toasters wirbt.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### URL-Bild

Verwenden Sie URL-Bilder für Anwendungsfälle mit folgenden Bestandteilen:
- Dynamische Liquid-Bilder durch Aufnahme des Liquids die Bildattribute. Sie können zum Beispiel {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} als Bild-URL einfügen, um einen Vornamen in das Bild aufzunehmen
- [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) durch Abruf von Bildern direkt von Ihrem Webserver oder öffentlich zugänglichen APIs
- [Braze-Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/) mit Bildern aus importierten CSV-Dateien und API-Endpunkten

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Länge der URL der Bilddatei | Maximal 2.000 Zeichen  |
| Bildformat          | PNG, JPEG             |
| Dateigröße     |  Maximal 10 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Reichhaltige Nachrichten (Image-Map)

Eine LINE Rich Message ist ein Bild, das einen oder mehrere Links enthält, die durch Auswahl bestimmter Bereiche des Bildes geöffnet werden. Wählen Sie eine Rich Message-Vorlage aus, um festzulegen, wie die Links auf dem Bild abgebildet werden sollen.

Zu den Anwendungsfällen gehören:
- Zeigen Sie ein Raster der neu eingetroffenen Handtaschen mit Links zu den jeweiligen Produktseiten an.
- Präsentieren Sie eine interaktive Speisekarte, die bei Auswahl eines Artikels eine Menübestellung startet.
- Legen Sie mehrere Werbeaktionen an, die der Benutzer durch Auswahl eines Rasterquadrats auswählen kann.

\![Eine Nachricht mit sechs Quadraten und einem Foto eines schwarz-weißen Gitters, auf das Nutzer:innen tippen können, um ein zufälliges Angebot zu erhalten.]({% image_buster /assets/img/line/line_rich_message.png %})

### Image-Map  

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Länge der URL der Bilddatei | Maximal 2.000 Zeichen  |
| Bildformat          | PNG (kann transparent sein), JPEG             |
| Seitenverhältnis          | 1:1 (Breite:Höhe)
| Dateigröße     |  Maximal 10 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### URI-Link 

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Zeichenanzahl      | max. 1.000 |
| Schemata              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Text 

Eine Rich-Text-Nachricht kann bis zu 400 Zeichen enthalten.

## Kartenbasiert (Karussell)

Mit einem kartenbasierten Messaging von LINE können Nutzer:innen wie in einem Karussell durch mehrere Nachrichten blättern und die für sie wichtigsten Nachrichten auswählen, indem sie eine Karte oder die Buttons einer Karte auswählen.

Anwendungsfälle umfassen:
- Rabatte auf bestimmte Artikel
- Hervorhebung der meistverkauften Jacken der Saison
- Präsentieren Sie eine Auswahl an Kochwerkzeugen und Gadgets, die in einem Kit enthalten sind

\![Eine kartenbasierte Nachricht mit mindestens zwei Karten, die für Sandwiches im Composer-Editor werben.]({% image_buster /assets/img/line/line_card_message.png %})

### Nachricht

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Spalten                  | max. 10 |
| Seitenverhältnis             | Viereckig: 1.51:1 <br> Quadratisch: 1:1  |
| Titel                    | Maximal 40 Zeichen
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Bild

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Bild-URL                 | Maximal 2.000 Zeichen |
| Bildformat              | JPEG oder PNG |
| Breite                     | 1.024 Pixel  |
| Dateigröße                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Text

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|-------------------------|----------------------------|
| Zeichen              | Maximal 120 (ohne Bild oder Titel) <br> Maximal 60 (Nachricht mit einem Bild oder einem Titel)  |
| Aktionen                 | 3 Maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


