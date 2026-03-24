---
nav_title: Werbetexten
article_title: KI-Copywriting-Assistent
page_order: 2.1
description: "Dieser Referenzartikel befasst sich mit dem KI-Copywriting-Assistenten, einem Feature, das einen kurzen Produktnamen oder eine kurze Beschreibung an das GPT-Texterstellungstool von OpenAI weitergibt, um menschenähnliche Marketingtexte zur Verwendung in Ihren Nachrichten zu erstellen."
---

# Texte erstellen mit BrazeAI

> Der KI-Copywriting-Assistent übergibt einen kurzen Produktnamen oder eine kurze Beschreibung an ein GPT-Texterstellungstool eines Drittanbieters, das OpenAI gehört, um menschenähnliche Marketingtexte zur Verwendung in Ihrem Messaging zu erstellen. Diese Funktion ist standardmäßig für die meisten Nachrichten-Editoren im Braze-Dashboard verfügbar.

## Texte generieren

### 1. Schritt: KI-Copywriter starten

Wählen Sie in Ihrem Nachrichten-Editor <i class="fa-solid fa-wand-magic-sparkles"></i> **KI-Copywriter starten** aus.

Markieren Sie im Drag-and-Drop-Editor für In-App-Nachrichten einen Textblock und wählen Sie <i class="fa-solid fa-wand-magic-sparkles" title="AI Copywriter"></i> in der Symbolleiste des Blocks.

### 2. Schritt: Details eingeben

Geben Sie einen Produktnamen oder eine Beschreibung in das Eingabefeld ein und wählen Sie dann eine ungefähre Ausgabelänge aus.

Sie können einen bestimmten Kanal für eine Ausgabelänge wählen, die auf kanalspezifischen Best Practices basiert, oder zwischen kurz (1 Satz), mittel (2–3 Sätze) oder lang (1 Absatz) wählen.

### 3. Schritt: Weiter anpassen (optional)

Um Ihren Text weiter anzupassen, können Sie:

- **Markenrichtlinien anwenden:** Nachdem Sie [mit BrazeAI<sup>TM</sup> Markenrichtlinien erstellt haben]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), können Sie diese bei der Erstellung Ihrer Texte verwenden.
- **Einen Ton wählen:** Jeder Ton erzeugt Texte in einem anderen Stil. Wählen Sie den Ton, der am besten zu Ihrer Markenstimme passt.
  
  Die Auswahl eines Tons fügt dem an OpenAI gesendeten Prompt eine Stilanweisung hinzu, sodass die genaue Ausgabe je nach Eingabe, Kanallänge, Markenrichtlinien und Modell variieren kann. 
  
  Hier ist, was jeder Ton standardmäßig bewirken soll:
  - **Formell:** Professionellere und geschliffenere Wortwahl. Vollständige Sätze, höflichere Sprache, minimaler Slang.
  - **Direkt:** Direkter und prägnanter. Weniger Adjektive, weniger „Marketing-Floskeln", klarere Handlungsaufforderungen.
  - **Locker:** Entspannter und gesprächiger. Freundlichere Formulierungen, einfachere Wörter, leichtere Stimmung.
  - **Persönlich:** Mehr 1:1 und empathisch. Häufigere Verwendung von „Sie", kann sich maßgeschneiderter anfühlen, besonders wenn Sie Personalisierung wie {% raw %}`{{${first_name}}}`{% endraw %} zu der Nachricht hinzufügen, die Sie erstellen.
  - **Aufmerksamkeitsstark:** Mehr Aufmerksamkeit erregend. Prägnantere Formulierungen, höhere Energie, stärkere Hooks und CTAs (liest sich oft mehr nach „Promo" als die anderen Töne).
  - **Anspruchsvoll:** Gehobenere, raffiniertere Sprache. Weniger locker, mehr „Premium"-Positionierung.
  - **Professionell:** Geschäftsmäßig und klar. Moderner und zugänglicher als Formell, aber dennoch mit Autorität.
  - **Passiv:** Sanftere, weniger aufdringliche Sprache. Weniger direkte Aufforderungen, mehr suggestive Formulierungen.
  - **Dringend:** Betont Unmittelbarkeit und Zeitdruck. Stärkere CTAs, Fristen, Knappheitssignale.
  - **Begeisternd:** Energischer und enthusiastischer. Betont positive Emotionen und Feierlichkeit (oft mehr Hype-orientiert als der Hook-getriebene Ansatz von Aufmerksamkeitsstark).
 
  
- **Daten aus vergangenen Kampagnen referenzieren**: Wenn diese Option aktiviert ist, werden frühere mobile Push-Benachrichtigungen, die über Ihre Kampagnen oder Canvas-Schritte verschickt wurden, als stilistische Referenz verwendet, um Ihren neuen Text zu erstellen. Weitere Informationen finden Sie unter [Verwendung früherer Kampagnendaten](#past-campaign-data).
- **Text automatisch übersetzen:** Sie können eine andere Ausgabesprache für Ihren Text wählen. Die generierten Inhalte werden in dieser Sprache ausgegeben.

### 4. Schritt: Text generieren

Wenn Sie fertig sind, wählen Sie **Generieren**. Wir verwenden die von Ihnen bereitgestellten Informationen, um GPT zu veranlassen, Texte für Sie zu schreiben. Die Antwort wird von OpenAI abgerufen und Ihnen zur Verfügung gestellt. Weitere Informationen finden Sie unter [Wie werden meine Daten verwendet und an OpenAI gesendet?](#ai-policy)

![Modal „KI-Copywriting-Assistent" mit verschiedenen verfügbaren Features]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Wir filtern Antworten auf anstößige Inhalte heraus, die gegen die [Content-Richtlinie](https://beta.openai.com/docs/usage-guidelines/content-policy) von OpenAI verstoßen.
{% endalert %}

## Über Daten vergangener Kampagnen {#past-campaign-data}

Wenn Sie „Push" als Ausgabelänge verwenden und **Daten aus früheren Kampagnen referenzieren** auswählen, werden zufällig ausgewählte frühere mobile Push-Kampagnen an OpenAI gesendet, damit GPT sie als Grundlage für die Texterstellung verwenden kann. Derzeit sendet der KI-Copywriter Push-Kampagnen an OpenAI, die keine Liquid-Syntax enthalten. Lassen Sie dieses Kästchen deaktiviert, wenn Sie diese Möglichkeit nicht nutzen möchten. In den folgenden Abschnitten finden Sie weitere Informationen darüber, wie Braze und OpenAI Ihre Daten verwenden. 

Bei Verwendung in Verbindung mit einer [Markenrichtlinie]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/) werden sowohl die Markenrichtlinie als auch die Daten der vergangenen Kampagne in die endgültige Ausgabe einbezogen.

{% multi_lang_include brazeai/generative_ai/policy.md %}