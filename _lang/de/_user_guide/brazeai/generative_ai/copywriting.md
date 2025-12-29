---
nav_title: Werbetexten
article_title: KI-Copywriting-Assistent
page_order: 2.1
description: "Dieser Referenzartikel befasst sich mit dem KI-Texterstellungsassistenten, einer Funktion, die einen kurzen Produktnamen oder eine kurze Beschreibung an das GPT-Texterstellungstool von OpenAI weitergibt, um menschenähnliche Marketingtexte zur Verwendung in Ihren Mitteilungen zu erstellen."
---

# Erzeugen einer Kopie mit <sup>BrazeAITM</sup>

> Der KI-Copywriting-Assistent übergibt einen kurzen Produktnamen oder eine kurze Beschreibung an ein GPT-Texterstellungstool eines Drittanbieters, das OpenAI gehört, um menschenähnliche Marketingtexte zur Verwendung in Ihrem Messeging zu erstellen. Diese Funktion ist standardmäßig für die meisten Nachrichten-Editoren im Braze Dashboard verfügbar.

## Erzeugen einer Kopie

### Schritt 1: KI-Texterin starten

Wählen Sie in Ihrem Nachrichten-Editor<i class="fa-solid fa-wand-magic-sparkles"></i> **KI-Copywriter starten** aus.

Markieren Sie im Drag-and-Drop-Editor für In-App-Nachrichten einen Textblock und wählen Sie <i class="fa-solid fa-wand-magic-sparkles" title="AI Texter"></i> in der Symbolleiste des Blocks.

### Schritt 2: Geben Sie die Details ein

Geben Sie einen Produktnamen oder eine Beschreibung in das Eingabefeld ein, und wählen Sie dann eine ungefähre Ausgabelänge aus.

Sie können einen bestimmten Kanal für eine Ausgabelänge wählen, die auf kanalspezifischen Best Practices basiert, oder zwischen kurz (1 Satz), mittel (2 bis 3 Sätze) oder lang (1 Absatz) wählen.

### Schritt 3: Weiter anpassen (optional)

Um Ihre Kopie weiter anzupassen, können Sie:

- **Wenden Sie Markenrichtlinien an:** Nachdem Sie [mit <sup>BrazeAITM</sup> Markenrichtlinien erstellt haben]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), können Sie diese bei der Erstellung Ihrer Texte verwenden.
- **Wählen Sie einen Ton:** Jeder Ton erzeugt Texte in einem anderen Stil. Wählen Sie den Ton, der am besten zu Ihrer Marke passt.
- **Referenzieren Sie Daten aus vergangenen Kampagnen**: Wenn diese Funktion aktiviert ist, werden frühere Push-Benachrichtigungen, die über Ihre Kampagnen oder Canvas-Schritte verschickt wurden, als stilistische Referenz verwendet, um Ihre neue Kopie zu erstellen. Weitere Informationen finden Sie unter [Verwendung früherer Kampagnen-Daten](#past-campaign-data).
- **Automatisch übersetzte Kopie:** Sie können eine andere Ausgabesprache für Ihre Kopie wählen. Die generierten Inhalte werden in dieser Sprache ausgegeben.

### Schritt 4: Erstellen Sie Ihre Kopie

Wenn Sie fertig sind, wählen Sie **Generieren**. Wir verwenden die von Ihnen bereitgestellten Informationen, um GPT zu veranlassen, Texte für Sie zu schreiben. Die Antwort wird von OpenAI abgerufen und Ihnen zur Verfügung gestellt. Weitere Informationen finden Sie unter [Wie werden meine Daten verwendet und an OpenAI gesendet?](#ai-policy)

![KI-Texterassistent Modal mit verschiedenen Features"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Wir filtern Antworten auf anstößige Inhalte heraus, die gegen die [Content-Richtlinie](https://beta.openai.com/docs/usage-guidelines/content-policy) von OpenAI verstoßen.
{% endalert %}

## Daten zu vergangenen Kampagnen {#past-campaign-data}

Wenn Sie Push als Ausgabelänge verwenden und **Daten vergangener Kampagnen referenzieren**, werden zufällig ausgewählte frühere mobile Push-Kampagnen an OpenAI gesendet, so dass GPT sie als Grundlage für seine Kopiererstellung verwenden kann. Derzeit sendet der KI-Texter Push-Kampagnen an OpenAI, die keine Liquid-Syntax haben. Lassen Sie dieses Kästchen deaktiviert, wenn Sie diese Möglichkeit nicht nutzen möchten. In den folgenden Abschnitten finden Sie weitere Informationen darüber, wie Braze und OpenAI Ihre Daten verwenden. 

Bei Verwendung in Verbindung mit einem [Markenleitfaden]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/) werden sowohl der Markenleitfaden als auch die Daten der vergangenen Kampagne in die endgültige Ausgabe einbezogen.

{% multi_lang_include brazeai/generative_ai/policy.md %}
