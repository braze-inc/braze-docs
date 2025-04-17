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

Sie finden die **Medienbibliothek** unter **Vorlagen**.

Sie können die **Mediathek** verwenden, um:

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

![Die Seite "Medienbibliothek" enthält einen Bereich "In die Bibliothek hochladen", in den Sie Dateien per Drag & Drop ziehen oder hochladen können. Es gibt auch eine Liste der hochgeladenen Inhalte in der Medienbibliothek.][1]

{% alert tip %} Weitere Hilfe zur Mediathek finden Sie in unseren [FAQ zu Vorlagen und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Bild-Details

In der Bibliothek sehen Sie den Asset-Typ, die Größe, die Abmessungen, die URL, das Datum, an dem es der Bibliothek hinzugefügt wurde, und weitere Informationen. 

### Verwendung der Mediathek im Vergleich zu einem CDN

Die Verwendung der Medienbibliothek bietet eine bessere Zwischenspeicherung und Performance für In-App-Nachrichten. Alle Mediathek-Assets, die Sie in einer In-App-Nachricht finden, werden für eine schnellere Anzeige zwischengespeichert und stehen für die Offline-Anzeige zur Verfügung. Darüber hinaus ist die Medienbibliothek mit Braze Composers integriert, was es Marketern erlaubt, Bilder auszuwählen oder zu taggen, anstatt Bild-URLs zu kopieren und einzufügen.

## Bild-Spezifikationen

Alle Bilder, die in die Medienbibliothek hochgeladen werden, müssen kleiner als 5 MB sein. Unterstützte Dateitypen sind PNG, JPEG, GIF und SVG. Spezielle Bildempfehlungen für die einzelnen Nachrichtenkanäle finden Sie in den folgenden Abschnitten.

### Content-Cards

{% multi_lang_include image_specs.md variable_name='Inhaltskarten' %}

### E-Mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### In-App-Nachrichten

{% multi_lang_include image_specs.md variable_name="In-App-Nachrichten"  %}

Weitere Informationen finden Sie unter [Details zur Gestaltung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="Push-Benachrichtigungen"  %}

##### Mehr Ressourcen

- [Push-Spezifikationen für Bild und Text]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### Video

Videos, die in die Mediathek hochgeladen werden, können vorerst nur in WhatsApp Nachrichten verwendet werden. Weitere Informationen finden Sie unter [Erstellen einer Whatsapp Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
Das Hinzufügen von Videos zu WhatsApp Nachrichten befindet sich derzeit in der Early Access Phase. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Zugriff auf die Medienbibliothek von einem Nachrichten-Editor aus

Die Medienbibliothek fungiert als zentraler Standort Ihres Dashboards, da alle Bilder direkt in sie hochgeladen werden. So können Sie Bilder in verschiedenen Nachrichten wiederverwenden.

![Je nach Nachrichten-Editor gibt es zwei gängige Möglichkeiten für den Zugriff auf die Medienbibliothek. Eine zeigt den E-Mail-Drag-and-Drop-Editor mit dem Titel "Bilder und GIFs" und einem Button "Aus der Medien-Bibliothek hinzufügen". Die andere zeigt die Standard-Editoren, wie Push- und In-App-Nachrichten, mit dem Titel "Medien" und einem Button "Bild hinzufügen".][1.5]{: style="border:none"}

## Ein Bild mit KI generieren {#generate-ai}

Sie können mit [DALL·E 3](https://openai.com/index/dall-e-3/), einem KI-System von OpenAI, einem Drittanbieter von Braze, Bilder für Ihre Medienbibliothek generieren. Dieses System kann realistische Bilder und Kunstwerke aus einer Beschreibung in natürlicher Sprache erstellen. Jede Anfrage generiert vier Variationen Ihres Prompts, und Ihr Unternehmen kann 10 Mal pro Tag Bilder generieren. Diese Summe gilt für alle Benutzer in Ihrem Unternehmen.

1. Wählen Sie in der Medienbibliothek <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator**.
2. Geben Sie eine Beschreibung des Bildes ein, das Sie generieren möchten (bis zu 300 Zeichen). Je detaillierter die Beschreibung ist, desto besser ist Ihr Ergebnis. Dieses Feature unterstützt nur Texteingaben - das Hochladen eines Bildes als Referenzieren ist nicht möglich.
3. Wählen Sie **Bilder generieren**. Es kann etwa eine Minute dauern, bis die Bilder generiert sind.
4. Wählen Sie <i class="fas fa-download" title="Bild zur Mediathek hinzufügen"></i> auf die Bilder, die Sie zu Ihrer Mediathek hinzufügen möchten.

![KI-Bildgenerator Modal in der Medienbibliothek.][6]{: style="max-width:75%"}

Zwischen Ihnen und Braze sind alle mit DALL·E 3 generierten Bilder Ihr geistiges Eigentum. Braze erhebt keinen Anspruch auf das Urheberrecht an solchen Bildern und übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte oder Bilder.

Um Bilder zu erzeugen, sendet Braze Ihre Anfrage an die API-Plattform von OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert. Das bedeutet, dass OpenAI nicht in der Lage ist, festzustellen, von wem die Abfrage gesendet wurde, es sei denn, Sie geben eindeutig identifizierbare Informationen in die von Ihnen bereitgestellten Eingaben ein. Wie in den [API Platform Commitments von OpenAI](https://openai.com/policies/api-data-usage-policies) beschrieben, werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern ihrer Modelle verwendet und nach 30 Tagen gelöscht. Bitte stellen Sie sicher, dass Sie die für Sie relevanten Richtlinien von OpenAI einhalten, die unter anderem die [Nutzungsrichtlinie](https://openai.com/policies/usage-policies) und der [Richtlinie zur gemeinsamen Nutzung und Veröffentlichung](https://openai.com/policies/sharing-publication-policy) umfassen können. Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
