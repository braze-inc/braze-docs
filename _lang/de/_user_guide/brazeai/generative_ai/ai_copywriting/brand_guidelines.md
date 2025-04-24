---
nav_title: Markenrichtlinien
article_title: Markenrichtlinien für KI-Werbetexte
page_order: 1
description: "Dieser Referenzartikel behandelt die Markenrichtlinien für den KI-Texter-Assistenten, eine Funktion, mit der Sie den Stil der vom KI-Texter-Assistenten generierten Texte an die Stimme und den Stil Ihrer Marke anpassen können."
---

# Markenrichtlinien für KI-Texterassistenten

> Passen Sie den Stil Ihrer KI-generierten Texte mit Hilfe von individuellen Markenrichtlinien an die Stimme und Persönlichkeit Ihrer Marke an.

## Erstellen von Markenrichtlinien {#steps}

Folgen Sie diesen Schritten, um Markenrichtlinien im KI-Texterstellungsassistenten zu erstellen. Sie können Markenrichtlinien auch auf der Einstellungsseite für [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/) erstellen.

### Schritt 1: Markenrichtlinie erstellen

1. Wählen Sie in Ihrem Nachrichten-Editor<i class="fa-solid fa-wand-magic-sparkles"></i> **KI-Copywriter starten** aus.
   * Markieren Sie im Drag-and-Drop-Editor für In-App-Nachrichten einen Textblock und wählen Sie <i class="fa-solid fa-wand-magic-sparkles" title="AI Texter"></i> in der Symbolleiste des Blocks.
2. Wählen Sie **Markenrichtlinien anwenden** und dann **Markenrichtlinien erstellen**.
3. Geben Sie einen Namen für diese Leitlinie ein. Es handelt sich um die Beschriftung, die Sie in der vorherigen Auswahl sehen.
4. Fügen Sie bei **Wann werden Sie diese Markenrichtlinien verwenden?** Details hinzu, um Ihren Kollegen (und Ihnen in Zukunft) den Kontext für die Verwendung dieser Richtlinien zu erläutern.
5. Wenn Sie möchten, dass dies der Standard-Markenleitfaden für den aktuellen Workspace ist, markieren Sie **Als Standard-Markenleitfaden verwenden**.

![Ansicht zur Erstellung von Markenrichtlinien.][1]

### Schritt 2: Beschreiben Sie Ihre Markenpersönlichkeit

Überlegen Sie bei der **Markenpersönlichkeit**, was Ihre Marke einzigartig macht. Fügen Sie Merkmale, Werte, Sprachstil und alle Archetypen hinzu, die Ihre Marke definieren. Hier sind einige Merkmale, die Sie beachten sollten:

| **Charakteristisch**       | **Definition**                                                                       | **Beispiel**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation               | Wie Ihre Marke auf dem Markt wahrgenommen werden soll.                               | Wir sind dafür bekannt, die zuverlässigste und kundenorientierteste Marke in unserer Branche zu sein. |
| Persönlichkeitsmerkmale       | Menschenähnliche Eigenschaften, die den Charakter Ihrer Marke beschreiben.                     | Unsere Marke ist freundlich, sympathisch und immer optimistisch.          |
| Werte                   | Grundwerte, die das Handeln und die Entscheidungen Ihrer Marke leiten.                           | Wir legen Wert auf Nachhaltigkeit, Transparenz und Gemeinschaft.            |
| Differenzierung          | Einzigartige Eigenschaften, die Ihre Marke von der Konkurrenz abheben.                         | Wir zeichnen uns durch einen persönlichen Kundenservice aus, der weit über das übliche Maß hinausgeht. |
| Sprachstil der Marke              | Der Ton und der Stil der Kommunikation, die Ihre Marke verwendet.                                 | Unser Ton ist leger und doch informativ und sorgt für Klarheit, ohne zu förmlich zu sein. |
| Archetyp der Marke          | Der Archetyp, der die Persona Ihrer Marke vertritt (Der Held, Der Schöpfer usw.).    | Wir verkörpern den Archetypus des 'Entdeckers', der immer auf der Suche nach neuen Herausforderungen und Abenteuern ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Definieren Sie Sprache, die vermieden werden sollte (optional)

Listen Sie unter **Ausschlüsse** alle Sprachen oder Stile auf, die nicht mit Ihrer Marke übereinstimmen. Zum Beispiel sollten Sie „Sarkasmus“, „negative Haltungen“ oder einen „herablassenden“ Sprachstil vermeiden.

### Schritt 4: Richtlinien testen

Testen Sie Ihre Richtlinien, um zu sehen, wie sie funktionieren. Erweitern Sie **Richtlinien testen**, um Beispieltexte zu erstellen und bei Bedarf anzupassen.

### Schritt 5: Speichern Sie Ihre Richtlinien

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Markenrichtlinien speichern** aus. Ihre neuen Richtlinien werden in Ihrem Arbeitsbereich zur späteren Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache unabhängig von der Sprache Ihrer Kopie ändern, aber weder Braze noch OpenAI garantieren die Qualität der Übersetzung. Testen und verifizieren Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Richtlinien für die Bearbeitung

So bearbeiten Sie Ihre bestehenden Markenrichtlinien:

1. Öffnen Sie den KI-Assistenten für Werbetexte.
2. Wenden Sie die Markenrichtlinien an, die Sie ändern möchten. In der Nähe des Feldes wird eine Schaltfläche angezeigt.
3. Wählen Sie **Leitfaden bearbeiten**.

## Wie werden meine Daten verwendet und an OpenAI gesendet?

Um Texte anhand einer Markenrichtlinie zu erstellen, sendet Braze Ihre Anfrage mit dem Inhalt Ihrer Richtlinie an OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert. Das bedeutet, dass OpenAI nicht in der Lage ist, festzustellen, von wem die Abfrage gesendet wurde, es sei denn, Sie geben eindeutig identifizierbare Informationen in den von Ihnen bereitgestellten Eingaben oder in Ihren früheren Kampagnendaten an, wenn Sie die Option "Frühere Kampagnendaten referenzieren" aktivieren. Gemäß der [Richtlinien von OpenAI](https://openai.com/policies/api-data-usage-policies) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern ihrer Modelle verwendet und nach 30 Tagen gelöscht. Zwischen Ihnen und Braze ist jeder mit GPT erstellte Inhalt Ihr geistiges Eigentum. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Inhalten und übernimmt keinerlei Garantie für KI-generierte Inhalte.


[1]: {% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} „Markenrichtlinien“
