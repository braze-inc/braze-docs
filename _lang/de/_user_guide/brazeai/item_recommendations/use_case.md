---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Entdeckung von Inhalten nach dem Ansehen"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke die Braze AI-Artikelempfehlungen nutzt, um personalisierte Inhalte und Produktempfehlungen in wichtigen Kundenmomenten bereitzustellen."
page_type: tutorial
---

# Anwendungsfälle: Fördern Sie die Entdeckung von Inhalten nach dem Ansehen

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke die Braze AI-Artikelempfehlungen nutzt, um personalisierte Inhalte und Produktempfehlungen in wichtigen Kundenmomenten bereitzustellen. Erfahren Sie, wie Empfehlungslogik das Engagement verbessern, die Konversion steigern und den manuellen Aufwand reduzieren kann.

Nehmen wir an, Frau Camila ist CRM-Manager:in bei MovieCanon, einer Streaming-Plattform, die kuratierte Filme und Serien anbietet. 

Camilas Ziel ist es, das Engagement der Zuschauer auch nach dem Anschauen eines Videos zu erhalten. In der Vergangenheit basierten die „Das könnte Ihnen auch gefallen“-Nachrichten von MovieCanon auf einer groben Genre-Zuordnung und wurden zu beliebigen Zeitpunkten versendet – häufig Stunden oder Tage nach einer Sitzung. Das Engagement war gering, und ihr Team war sich bewusst, dass sie mehr leisten konnten.

Mithilfe von[ KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) richtet Camila ein System ein, das automatisch neue Titel basierend auf dem Verlauf jedes Nutzers empfiehlt. Diese Empfehlungen werden unmittelbar nach Beendigung eines Films oder einer Episode zugestellt. Dies ist eine intelligentere und persönlichere Methode, um Nutzern dabei zu unterstützen, Inhalte zu entdecken, die sie tatsächlich als Nächstes sehen möchten, und sie im Engagement mit der Plattform zu unterstützen.

![In-App-Nachricht mit dem Text „Als Nächstes, speziell für Sie. Da Sie „Nomads of the Sun“ angesehen haben, werden Ihnen ein Bild, der Titel, eine Beschreibung und die Aufforderung „Jetzt ansehen“ oder „Überspringen“ zur nächsten Empfehlung angezeigt.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Dieses Tutorial führt Sie durch die Vorgehensweise von Camila:

- Eine personalisierte Nachricht, die ausgelöst wird, wenn ein Nutzer:in das Ansehen eines Inhalts beendet hat.
- Empfehlungen, die auf die Präferenzen des Zuschauers zugeschnitten sind – automatisch aus dem Katalog von MovieCanon abgerufen und in die Nachricht eingefügt. 

## Schritt 1: Erstellen Sie ein Modell zur Prognose der Abwanderungsrate.

Camila beginnt damit, eine Empfehlung zu erstellen, die relevante Titel anzeigt, sobald eine Nutzer:in etwas angesehen hat. Sie wünscht sich eine dynamische Funktion, sodass die Nutzer:innen verschiedene Vorschläge erhalten, die auf ihren zuletzt angesehenen Inhalten basieren.

1. Im Braze-Dashboard navigiert Frau Camila zu **den KI-Artikelempfehlungen**.
2. Sie erstellt eine neue Empfehlung und benennt sie „Vorschläge nach dem Anschauen“.
3. Für den Empfehlungstyp wählt sie **„KI-personalisiert“**, sodass jede Nutzer:in auf der Grundlage ihres bisherigen Verhaltens personalisierte Empfehlungen erhält.
4. Sie wählt **„Keine Empfehlungen für Artikel, mit denen Nutzer:innen zuvor interagiert haben“,** damit Nutzer:innen keine Empfehlungen für Artikel erhalten, die sie bereits angesehen haben. 
5. Sie wählt den Katalog aus, der die aktuelle Bibliothek von MovieCanon enthält. Camila wählt keinen Katalog aus, da sie möchte, dass alle Artikel im Katalog für Empfehlungen in Frage kommen.
6. Camila verknüpft die Empfehlung mit dem`Watched Content`angepassten Event, das abgeschlossene Aufrufe nachverfolgt, und legt den **Eigenschaftsnamen** auf den Titel des Inhalts fest.
7. Sie erstellt die Empfehlung.

## Schritt 2: Richten Sie eine In-App-Nachricht ein.

Nachdem die Empfehlung trainiert wurde, erstellt Camila einen Messaging-Fluss, der den Nutzer:in zum richtigen Zeitpunkt erreicht: unmittelbar nachdem er einen Titel abgeschlossen hat. Die Nachricht enthält eine Liste mit drei personalisierten Vorschlägen, die direkt aus dem Katalog stammen.

1. Camila erstellt eine In-App-Nachricht-Kampagne mithilfe des Drag-and-Drop-Editors.
2. Sie stellt den Auslöser auf ihr angepasstes Event ein: `Watched Content`.
3. Sie entwirft eine mehrseitige In-App-Nachricht mit Titelbildern, Namen und einem CTA „Jetzt ansehen“.

![Öffnen Sie das Modal „Personalisierung hinzufügen” im Braze-Editor und wählen Sie als Personalisierungstyp „Artikelempfehlung” aus.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Im Nachrichtentext verwendet Camila das [Modal „Personalisierung hinzufügen”]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables), um Variablen wie den Namen, die Beschreibung und die Miniaturansicht des empfohlenen Titels mithilfe von Liquid hinzuzufügen, wodurch Inhalte aus dem Katalog dynamisch eingefügt werden. Sie erstellt ein Template in einem angepassten Attribut, um`Last Watched Movie` die Nutzer:innen darüber zu informieren, dass diese Empfehlung auf ihrem Verlauf basiert. 

![In-App-Nachrichteneditor mit Raw Liquid zur Erstellung von Templates in bestimmten Feldern aus Katalogartikeln aus der Empfehlung.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

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

5. Anschließend dupliziert Camila ihre Seite und erhöht das Liquid-Array{% raw %}(`{{ items[0]}}`to`{{items[1]}}`){% endraw %}in jeder Variablen, um das Template im nächsten Artikel der Empfehlungsliste zu erstellen.

## Schritt 3: Messen und optimieren

Während die Kampagne läuft, überwacht Frau Camila die Öffnungsraten, Klickraten und das nachfolgende Betrachtungsverhalten. Sie vergleicht die Performance mit früheren statischen Empfehlungskampagnen und stellt ein höheres Engagement sowie mehr Content-Sitzungen pro Nutzer:in fest.

Sie plant außerdem einen A/B-Test:

- Zeitpunkt (unmittelbar nach dem Betrachten oder 10 Minuten danach)
- Inhaltslayout (Karussell oder Liste)
- CTA-Varianten („Jetzt ansehen“ versus „Zur Warteschlange hinzufügen“)

Durch die Kombination von ereignisgesteuerten Nachrichten mit KI-Artikelempfehlungen verwandelt Camila die Suche nach Inhalten in ein automatisches, personalisiertes Erlebnis. MovieCanon sorgt dafür, dass Nutzer:innen ohne Spekulationen engagiert bleiben, indem es relevante Inhalte zum richtigen Zeitpunkt bereitstellt, um die Sitzungsdauer zu verlängern und die Abwanderung zu verringern.





