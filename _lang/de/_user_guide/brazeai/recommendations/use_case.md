---
nav_title: Anwendungsfall
article_title: Anwendungsfälle Drive Content Discovery After Viewing
description: "Dieses Beispiel zeigt, wie eine fiktive Marke Braze AI Artikel-Empfehlungen verwendet, um personalisierte Inhalte und Produktvorschläge für wichtige Kund:in zugestellt zu bekommen."
page_type: tutorial
---

# Anwendungsfälle: Entdecken Sie Inhalte nach dem Ansehen

> Dieses Beispiel zeigt, wie eine fiktive Marke Braze AI Artikel-Empfehlungen verwendet, um personalisierte Inhalte und Produktvorschläge für wichtige Kund:in zugestellt zu bekommen. Erfahren Sie, wie die Empfehlungslogik das Engagement verbessern, die Konversionen erhöhen und den manuellen Aufwand reduzieren kann.

Nehmen wir an, Camila ist CRM Managerin bei MovieCanon, einer Streaming-Plattform, die kuratierte Filme und Serien anbietet. 

Camilas Ziel ist es, das Engagement der Zuschauer zu erhalten, nachdem sie etwas gesehen haben. In der Vergangenheit basierten die Nachrichten von MovieCanon "Das könnte Ihnen auch gefallen" auf einem breiten Genre-Matching und wurden zu willkürlichen Zeitpunkten verschickt - oft Stunden oder Tage nach einer Sitzung. Das Engagement war gering, und ihr Team wusste, dass sie es besser machen konnten.

Mit Hilfe von [KI-Artikel-Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) richtet Camila ein System ein, das auf der Grundlage des Verlaufs jedes Zuschauers automatisch neue Titel empfiehlt, die sofort zugestellt werden, wenn ein Nutzer:innen einen Film oder eine Folge beendet hat. Es ist ein intelligenter, personalisierter Weg, um Nutzer:innen dabei zu helfen, Inhalte zu entdecken, die sie tatsächlich als nächstes sehen möchten, und sie auf der Plattform zu halten.

In-App-Nachricht: "Als Nächstes, nur für Sie. Weil Sie "Nomaden der Sonne" gesehen haben, mit einem Bild, einem Titelnamen, einer Beschreibung und einer CTA zum "Jetzt ansehen" oder "Überspringen" zur nächsten Empfehlung.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

In dieser Anleitung erfahren Sie, wie Camila:

- Eine personalisierte Nachricht, die ausgelöst wird, wenn ein Nutzer:in etwas zu Ende schaut
- Empfehlungen, die auf die Vorlieben des Zuschauers zugeschnitten sind - automatisch aus dem Katalog von MovieCanon gezogen und in die Nachricht eingefügt 

## Schritt 1: Erstellen Sie ein Modell zur Prognose der Abwanderung

Camila erstellt zunächst eine Empfehlung, die relevante Titel anzeigt, sobald ein Nutzer:in etwas zu Ende geschaut hat. Sie möchte, dass es dynamisch ist, so dass Nutzer:innen unterschiedliche Vorschläge erhalten, je nachdem, was sie in letzter Zeit gesehen haben.

1. Im Braze-Dashboard navigiert Camila zu **KI-Artikel-Empfehlungen**.
2. Sie erstellt eine neue Empfehlung und nennt sie "Vorschläge nach dem Anschauen".
3. Als Empfehlungstyp wählt sie **KI Personalisiert**, so dass jeder Nutzer:in maßgeschneiderte Empfehlungen auf der Grundlage seines bisherigen Verhaltens erhält.
4. Sie wählt die Option **Keine Artikel empfehlen aus, mit denen Nutzer:innen bereits interagiert haben**, so dass Nutzer:innen keine Empfehlungen für etwas erhalten, das sie bereits gesehen haben. 
5. Sie wählt den Katalog aus, der die aktuelle Bibliothek von MovieCanon enthält. Camila fügt keine Katalogauswahl hinzu, da sie möchte, dass alle Artikel im Katalog für eine Empfehlung in Frage kommen.
6. Camila verknüpft die Empfehlung mit dem angepassten Event `Watched Content`, das abgeschlossene Aufrufe verfolgt, und setzt den **Property Name** auf den Titel des Inhalts.
7. Sie erstellt die Empfehlung.

## Schritt 2: Einrichten einer In-App-Nachricht

Nachdem die Empfehlung trainiert wurde, erstellt Camila einen Messaging-Fluss, der die Nutzer:innen im richtigen Moment erreicht: unmittelbar nachdem sie einen Titel beendet haben. Die Nachricht enthält eine Liste mit drei personalisierten Vorschlägen, die direkt aus dem Katalog stammen.

1. Camila erstellt eine In-App-Nachricht-Kampagne mit dem Drag-and-Drop-Editor.
2. Sie setzt den Auslöser auf ihr angepasstes Event: `Watched Content`.
3. Sie entwirft eine mehrseitige In-App-Nachricht mit Titelbildern, Namen und einem CTA "Jetzt ansehen".

\!["Modal "Personalisierung hinzufügen" im Braze-Editor geöffnet, wobei "Artikelempfehlung" als Personalisierungstyp ausgewählt ist.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Im Nachrichtentext verwendet Camila das [Modal Personalisierung hinzufügen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables), um Variablen wie den Namen des empfohlenen Titels, die Beschreibung und die Miniaturansicht mit Hilfe von Liquid hinzuzufügen, das dynamisch Inhalte aus dem Katalog auffüllt. Sie passt ein angepasstes Attribut für `Last Watched Movie` an, damit die Nutzer:innen wissen, dass diese Empfehlung auf ihrem Uhrenverlauf basiert. 

\![In-App-Nachricht-Editor mit Raw Liquid als Template in bestimmten Feldern von Katalogartikeln aus der Empfehlung.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Camila dupliziert dann ihre Seite und erhöht das Liquid-Array {% raw %} (`{{ items[0]}}` bis `{{items[1]}}`) {% endraw %} in jeder Variablen zum Template im nächsten Artikel der Empfehlungsliste.

## Schritt 3: Messen und optimieren

Wenn die Kampagne live ist, überwacht Camila die Öffnungsraten, die CTRs und das weitere Anzeigeverhalten. Sie vergleicht die Performance mit früheren Kampagnen für statische Empfehlungen und stellt ein höheres Engagement und mehr Inhaltssitzungen pro Nutzer:in fest.

Sie plant auch A/B-Tests:

- Timing (sofort oder 10 Minuten nach dem Anschauen)
- Layout der Inhalte (Karussell oder Liste)
- CTA-Varianten ("Jetzt ansehen" versus "Zur Warteschlange hinzufügen")

Durch die Verbindung von ereignisgesteuertem Messaging mit KI-Empfehlungen für Artikel macht Camila die Entdeckung von Inhalten zu einem automatischen, personalisierten Erlebnis. MovieCanon hält das Engagement der Nutzer:innen ohne Rätselraten aufrecht, indem es relevante Inhalte genau zum richtigen Zeitpunkt zustellt, um die Sitzungstiefe zu erhöhen und die ABWANDERUNG VERRINGERN.





