---
nav_title: Medienbibliothek
article_title: Medienbibliothek
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Mediathek. Hier erfahren Sie, wie Sie Ihre Assets an einem einzigen, zentralen Ort verwalten, Bilder mithilfe von KI generieren und auf Medien in Ihrem Message Composer zugreifen können."
tool: Media

---

# Medienbibliothek

> Mit der Mediathek können Sie Ihre Assets an einem einzigen, zentralisierten Ort verwalten. 

## Media library vs. CDN

Using the media library instead of a Content Delivery Network (CDN) provides better caching and performance for in-app messages. Alle Mediathek-Assets, die Sie in einer In-App-Nachricht finden, werden für eine schnellere Anzeige zwischengespeichert und stehen für die Offline-Anzeige zur Verfügung. Darüber hinaus ist die Medienbibliothek mit Braze Composers integriert, was es Marketern erlaubt, Bilder auszuwählen oder zu taggen, anstatt Bild-URLs zu kopieren und einzufügen.

## Accessing the media library

In der Bibliothek sehen Sie den Asset-Typ, die Größe, die Abmessungen, die URL, das Datum, an dem es der Bibliothek hinzugefügt wurde, und weitere Informationen. To access your Braze media library, go to THIS > **Templates**. Here, you can:

* Mehrere Bilder auf einmal hochladen
* Virtuelle Kontaktdateien (.vcf) hochladen
* Hochladen von Videodateien zur Verwendung in WhatsApp Nachrichten
* Laden Sie einen Ordner mit Ihren Bildern hoch (maximal 50 Bilder)
* [Generieren Sie ein Bild mit Hilfe von KI](#generate-ai) und speichern Sie es in der Medienbibliothek
* Schneiden Sie ein vorhandenes Bild zu, um das richtige Verhältnis für Ihre Nachrichten zu schaffen.
* Fügen Sie Tags oder Teams hinzu, um Ihre Bilder besser zu organisieren.
* Suche nach Tags oder Teams in der Medienbibliothek
* Ziehen Sie die hochzuladenden Bilder oder Ordner per Drag & Drop.
* Bilder löschen

![Seite der Mediathek, die einen Bereich "In die Bibliothek hochladen" enthält, in den Sie Dateien per Drag-and-Drop ziehen oder hochladen können. Es gibt auch eine Liste der hochgeladenen Inhalte in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_main.png %})

Later when drafting a message in Braze, you can pull in your images from the media library.

![Je nach Nachrichten-Editor gibt es zwei gängige Möglichkeiten, auf die Bibliothek zuzugreifen. Eine zeigt den E-Mail-Drag-and-Drop-Editor mit dem Titel "Bilder und GIFs" und einem Button "Aus der Medien-Bibliothek hinzufügen". Die andere zeigt die Standard-Editoren, wie Push- und In-App-Nachrichten, mit dem Titel "Medien" und einem Button "Bild hinzufügen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Weitere Hilfe zur Bibliothek finden Sie in unseren [Templates & Medien FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Bild-Spezifikationen

Alle Bilder, die in die Medienbibliothek hochgeladen werden, müssen kleiner als 5 MB sein. Unterstützte Dateitypen sind PNG, JPEG, GIF und SVG. Spezielle Bildempfehlungen für die einzelnen Nachrichtenkanäle finden Sie in den folgenden Abschnitten.

### Content-Cards

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-Mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### In-App-Nachrichten

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Weitere Informationen finden Sie unter [Details zur Gestaltung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
For additional resources, see [Push image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Video

Videos, die in die Mediathek hochgeladen werden, können vorerst nur in WhatsApp Nachrichten verwendet werden. Weitere Informationen finden Sie unter [Erstellen einer Whatsapp Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generating images with BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Before using this feature, review [how your data is used and sent to OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
