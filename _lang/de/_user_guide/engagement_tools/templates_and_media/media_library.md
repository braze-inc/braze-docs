---
nav_title: Medienbibliothek
article_title: Medienbibliothek
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Medienbibliothek. Hier erfahren Sie, wie Sie Ihre Assets an einem einzigen, zentralen Ort verwalten, Bilder mithilfe von KI generieren und auf Medien in Ihrem Nachrichten-Editor zugreifen können."
tool: Media

---

# Medienbibliothek

> Mit der Medienbibliothek können Sie Ihre Assets an einem einzigen, zentralen Ort verwalten. 

## Medienbibliothek im Vergleich zu CDN

Die Verwendung der Medienbibliothek anstelle eines Content Delivery Network (CDN) bietet besseres Caching und eine bessere Performance für In-App-Nachrichten. Alle Medienbibliothek-Assets, die in einer In-App-Nachricht enthalten sind, werden für eine schnellere Anzeige vorab zwischengespeichert und stehen für die Offline-Anzeige zur Verfügung. Darüber hinaus ist die Medienbibliothek in die Braze-Editoren integriert, sodass Marketer Bilder auswählen oder taggen können, anstatt Bild-URLs zu kopieren und einzufügen.

## Zugriff auf die Medienbibliothek

In der Medienbibliothek sehen Sie den Asset-Typ, die Größe, die Abmessungen, die URL, das Datum, an dem es der Bibliothek hinzugefügt wurde, und weitere Informationen. Um auf Ihre Braze-Medienbibliothek zuzugreifen, gehen Sie zu **Templates** > **Medienbibliothek**. Hier können Sie:

* Mehrere Bilder auf einmal hochladen
* Virtuelle Kontaktdateien (.vcf) hochladen
* Videodateien zur Verwendung in WhatsApp-Nachrichten hochladen
* Einen Ordner mit Ihren Bildern hochladen (maximal 50 Bilder)
* [Ein Bild mit Hilfe von KI generieren](#generate-ai) und es in der Medienbibliothek speichern
* Ein vorhandenes Bild zuschneiden, um das richtige Verhältnis für Ihre Nachrichten zu erstellen
* Tags oder Teams hinzufügen, um Ihre Bilder besser zu organisieren
* Nach Tags oder Teams im Raster der Medienbibliothek suchen
* Bilder oder Ordner per Drag-and-Drop hochladen
* Bilder löschen

![Die Seite „Medienbibliothek" enthält einen Bereich „In die Bibliothek hochladen", in den Sie Dateien per Drag-and-Drop ziehen oder hochladen können. Es gibt auch eine Liste der hochgeladenen Inhalte in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_main.png %})

Später, beim Verfassen einer Nachricht in Braze, können Sie Ihre Bilder aus der Medienbibliothek einfügen.

![Je nach Nachrichten-Editor gibt es zwei gängige Möglichkeiten für den Zugriff auf die Medienbibliothek. Eine zeigt den E-Mail-Drag-and-Drop-Editor mit dem Titel „Bilder und GIFs" und einem Button „Aus der Medienbibliothek hinzufügen". Die andere zeigt die Standard-Editoren, wie Push- und In-App-Nachrichten, mit dem Titel „Medien" und einem Button zum Hinzufügen eines Bildes.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Weitere Informationen zur Medienbibliothek finden Sie in den [häufig gestellten Fragen zu Templates und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Bildspezifikationen

Alle Bilder, die in die Medienbibliothek hochgeladen werden, müssen kleiner als 5&nbsp;MB sein. Unterstützte Dateiformate sind PNG, JPEG, GIF, SVG und WebP. Spezielle Bildempfehlungen für die einzelnen Messaging-Kanäle finden Sie in den folgenden Abschnitten.

{% alert important %}
GIFs mit sehr langgestreckten Formen (z. B. 3000 x 2 Pixel) oder 300 oder mehr Frames können möglicherweise nicht hochgeladen werden, selbst wenn die Gesamtdateigröße gering ist.
{% endalert %}

### Content-Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-Mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### In-App-Nachrichten

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Weitere Informationen finden Sie unter [Details zur Gestaltung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

#### Empfohlene Nachrichtenlängen

Für optimale Ergebnisse beachten Sie die folgenden Richtlinien zur Nachrichtenlänge beim Verfassen von Push-Nachrichten. Je nach Vorhandensein eines Bildes, dem Benachrichtigungsstatus (iOS) und der Anzeigeeinstellung des Geräts sowie der Gerätegröße kann es zu Abweichungen kommen.

| Nachrichtentyp | Empfohlene Länge (nur Text) | Empfohlene Länge (Rich) |
| --- | --- | --- |
| iOS-Sperrbildschirm | 160 Zeichen | 130 Zeichen |
| iOS Notification Center | 160 Zeichen | 130 Zeichen |
| iOS-Bannerbenachrichtigung | 80 Zeichen | 65 Zeichen |
| Android-Sperrbildschirm | 49 Zeichen | N/A |
| Android-Benachrichtigungsleiste | 597 Zeichen | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Weitere Informationen zu iOS-Zeichenanzahlen finden Sie unter [Richtlinien zur iOS-Zeichenanzahl]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

#### Web-Push

{% tabs %}
{% tab Bilder %}

| Browser | Empfohlene Symbolgröße |
| --- | --- |
| Chrome | 192 x 192 px oder größer |
| Firefox | 192 x 192 px oder größer |
| Safari | 192 x 192 px oder größer (pro Kampagne konfigurierbar mit Safari 16 auf macOS 13+) |
| Opera | 192 x 192 px oder größer |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| Browser | Plattform | Große Bildgröße |
| --- | --- | --- |
| Chrome | Android | 2:1 Seitenverhältnis |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 Seitenverhältnis |
| Edge | Windows | 2:1 Seitenverhältnis |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 Seitenverhältnis |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| Browser | Plattform | Maximale Titellänge | Maximale Textlänge |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### Beispiele für Push-Benachrichtigungen

{% tabs %}
{% tab iOS %}

![iOS-Push-Benachrichtigung mit dem Text: „Hi! Dies ist ein iOS-Push mit einem Bild" und einem Emoji. Neben dem Text befindet sich ein kleines Bild.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS-Push-Benachrichtigung als Hard Push mit demselben Text wie die vorherige Nachricht und einem erweiterten Bild vor dem Text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Android-Push-Benachrichtigung mit einem großen Bild unter dem Nachrichtentext.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Benachrichtigungen mit großen Bildern werden am besten mit einem Bild von mindestens 600 x 300 Pixeln angezeigt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Video

In die Medienbibliothek hochgeladene Videos können ausschließlich in WhatsApp-Nachrichten verwendet werden. Weitere Informationen finden Sie unter [Erstellen einer WhatsApp-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Bilder mit BrazeAI<sup>TM</sup> generieren {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Bevor Sie dieses Feature nutzen, lesen Sie bitte nach, [wie Ihre Daten verwendet und an OpenAI gesendet werden]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}