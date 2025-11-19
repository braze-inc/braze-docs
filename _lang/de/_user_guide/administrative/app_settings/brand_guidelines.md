---
nav_title: Markenrichtlinien
article_title: Markenrichtlinien
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, wie Sie Markenrichtlinien erstellen, verwalten und verwenden, die Sie mit dem KI Copywriting Assistant auf Ihre Nachrichten anwenden können."
---

# Markenrichtlinien

> Passen Sie den Stil Ihrer von der KI generierten Texte mit personalisierten Markenrichtlinien an die Stimme, den Ton und die Persönlichkeit Ihrer Marke an.

Sie können Ihre Markenrichtlinien erstellen und verwalten, indem Sie zu **Einstellungen** > **Markenrichtlinien** gehen. Sie können sie auch mit dem [KI-Texterstellungsassistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines/) erstellen.

## Erstellen von Markenrichtlinien

### Schritt 1: Markenrichtlinie erstellen

Wählen Sie auf der Seite **Markenrichtlinien** die Option **Neu erstellen** aus. Wenn Sie möchten, dass diese Markenrichtlinie der Standard für den Workspace ist, markieren Sie **Als Standard-Markenrichtlinie verwenden**. Sie können einen Standard pro Workspace haben.

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

![Das Fenster "Markenrichtlinie erstellen" mit Feldern zur Eingabe des Namens, der Beschreibung, der Persönlichkeit, der Ausschlüsse und des Tons.]({% image_buster /assets/img/guidelines_create.png %})

### Schritt 4: Richtlinien testen

Testen Sie Ihre Richtlinien, um zu sehen, wie sie funktionieren. Erweitern Sie **Richtlinien testen**, um Beispieltexte zu erstellen und bei Bedarf anzupassen.

### Schritt 5: Speichern Sie Ihre Richtlinien

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Markenrichtlinien speichern** aus. Ihre neuen Richtlinien werden in Ihrem Arbeitsbereich zur späteren Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache ändern, unabhängig davon, in welcher Sprache Ihre Kopie vorliegt, aber weder Braze noch OpenAI garantieren die Qualität der Übersetzung. Testen und verifizieren Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Verwaltung von Markenrichtlinien

Sie können Markenrichtlinien bearbeiten, indem Sie sie auf der Seite **Markenrichtlinien** auswählen. Archivieren Sie eine Markenrichtlinie, um sie inaktiv zu machen und sie aus dem KI-Texterstellungsassistenten zu entfernen. Um sie wieder aktiv und auswählbar zu machen, können Sie nach archivierten Markenrichtlinien filtern und dann die Archivierung aufheben.

![Die Seite "Markenrichtlinien" wurde nach archivierten Markenrichtlinien gefiltert.]({% image_buster /assets/img/unarchive_brand_guideline.png %})

## Verwendung von Markenrichtlinien

Wenn Sie eine Nachricht verfassen, öffnen Sie den [KI-Texter-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) und wählen Sie Ihre Markenrichtlinien im Dropdown-Menü **Markenrichtlinien anwenden** aus. Wenn Sie eine bestimmte Markenrichtlinie als Standard festlegen, wird diese automatisch in der Dropdown-Liste ausgewählt, aber Sie können auch eine andere Richtlinie wählen. 

!["KI-Textwerkstatt-Assistent mit "Important Alerts!!" als Markenleitlinie ausgewählt.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}
