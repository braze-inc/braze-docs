---
nav_title: KI-Copywriting-Assistent
article_title: KI-Copywriting-Assistent
page_order: 4
description: "Dieser Referenzartikel befasst sich mit dem KI-Texterstellungsassistenten, einer Funktion, die einen kurzen Produktnamen oder eine kurze Beschreibung an das GPT-Texterstellungstool von OpenAI weitergibt, um menschenähnliche Marketingtexte zur Verwendung in Ihren Mitteilungen zu erstellen."
---

# KI-Copywriting-Assistent

> Der KI-Copywriting-Assistent übergibt einen kurzen Produktnamen oder eine kurze Beschreibung an ein GPT-Texterstellungstool eines Drittanbieters, das OpenAI gehört, um menschenähnliche Marketingtexte zur Verwendung in Ihrem Messeging zu erstellen. Diese Funktion ist standardmäßig für die meisten Nachrichten-Editoren im Braze Dashboard verfügbar.

## Erstellen einer Kopie {#steps}

Um mit dem KI-Copywriting-Assistent Texte zu erstellen, gehen Sie folgendermaßen vor:

1. Wählen Sie in Ihrem Nachrichten-Editor<i class="fa-solid fa-wand-magic-sparkles"></i> **KI-Copywriter starten** aus.
   * Markieren Sie im Drag-and-Drop-Editor für In-App-Nachrichten einen Textblock und wählen Sie <i class="fa-solid fa-wand-magic-sparkles" title="AI Texter"></i> in der Symbolleiste des Blocks.
2. Geben Sie einen Produktnamen oder eine Beschreibung in das Eingabefeld ein.
3. Wählen Sie eine ungefähre Ausgabelänge. Sie können einen bestimmten Kanal für eine Ausgabelänge wählen, die auf kanalspezifischen Best Practices basiert, oder zwischen kurz (1 Satz), mittel (2 bis 3 Sätze) oder lang (1 Absatz) wählen. 
4. (Optional) Erstellen Sie eine Markenrichtlinie oder wenden Sie sie an, um diese Kopie an Ihre Marke anzupassen. Diese Richtlinien werden in Ihrem Arbeitsbereich gespeichert und können nach ihrer Erstellung wiederverwendet werden. Weitere Informationen finden Sie unter [Erstellen von Markenrichtlinien]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).
5. (Optional) Wählen Sie einen Nachrichtenton aus den verfügbaren Optionen. Dies bestimmt den Stil der erzeugten Kopie.
6. (Optional) Verfügbar für Push-Benachrichtigungen: Wählen Sie **Vergangene Kampagnendaten referenzieren**, um Ihre früheren mobilen Push-Nachrichten (Kampagnen und Canvas-Schritte) als stilistische Referenz für die Erstellung neuer Texte zu verwenden. Wenn Sie diese Option auswählen, wird die Ausgabe den Stil Ihrer vorherigen Nachrichten imitieren.
7. Wählen Sie die Ausgabesprache. Diese kann sich von Ihrer Eingabesprache unterscheiden.
8. Wählen Sie **Erzeugen**.

Wir verwenden die von Ihnen bereitgestellten Informationen, um GPT zu veranlassen, Texte für Sie zu schreiben. Die Antwort wird von OpenAI abgerufen und Ihnen zur Verfügung gestellt. 

![Modal „KI-Copywriting-Assistent“ mit verschiedenen verfügbaren Funktionen"][1]{: style="max-width:70%;"}

{% alert important %}
Wir filtern Antworten auf anstößige Inhalte heraus, die gegen die [Content-Richtlinie](https://beta.openai.com/docs/usage-guidelines/content-policy) von OpenAI verstoßen.
{% endalert %}

## Verwenden von Daten vergangener Kampagnen

Wenn Sie Push als Ausgabelänge wählen, werden zufällig ausgewählte frühere mobile **Push-Kampagnen** an OpenAI gesendet, sodass GPT sie als Grundlage für die Erstellung von Kopien verwenden kann. Lassen Sie dieses Kästchen deaktiviert, wenn Sie diese Möglichkeit nicht nutzen möchten. In den folgenden Abschnitten finden Sie weitere Informationen darüber, wie Braze und OpenAI Ihre Daten verwenden. 

Bei Verwendung in Verbindung mit einem [Markenleitfaden]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) werden sowohl der Markenleitfaden als auch die Daten der vergangenen Kampagne in die endgültige Ausgabe einbezogen.

## Was ist GPT?

[GPT](https://openai.com/product/gpt-4) ist OpenAIs hochmodernes Tool zur Generierung natürlicher Sprache auf der Grundlage künstlicher Intelligenz. Das Tool kann eine Vielzahl von Aufgaben in natürlicher Sprache ausführen, wie z. B. Texterstellung, -vervollständigung und -klassifizierung. Wir haben es in das Braze-Dashboard integriert, um Ihre Texte direkt bei der Arbeit zu inspirieren und zu diversifizieren.

## Wie werden meine Daten verwendet und an OpenAI gesendet?

Um eine Kopie zu erstellen, sendet Braze Ihre Anfrage an OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert. Das bedeutet, dass OpenAI nicht in der Lage ist, festzustellen, von wem die Abfrage gesendet wurde, es sei denn, Sie geben eindeutig identifizierbare Informationen in den von Ihnen bereitgestellten Eingaben oder in Ihren früheren Kampagnendaten an, wenn Sie die Option "Frühere Kampagnendaten referenzieren" aktivieren. Gemäß der [Richtlinien von OpenAI](https://openai.com/policies/api-data-usage-policies) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern ihrer Modelle verwendet und nach 30 Tagen gelöscht. Zwischen Ihnen und Braze ist jeder mit GPT erstellte Inhalt Ihr geistiges Eigentum. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Inhalten und übernimmt keinerlei Garantie für KI-generierte Inhalte.

## Mehr KI-Tools

Sie können auch [ein Bild mit AI]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) aus der Mediathek [erstellen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai). Dabei kommt [DALL-E 3](https://openai.com/index/dall-e-3/) zum Einsatz, ein KI-System von OpenAI, das realistische Bilder und Kunst aus einer Beschreibung in natürlicher Sprache erstellen kann.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"
