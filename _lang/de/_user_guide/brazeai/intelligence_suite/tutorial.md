---
nav_title: "Tutorial: Schnellrestaurant"
article_title: Intelligence-Suite-Tutorial
page_order: 10
search_rank: 12
description: "Neu bei der Braze Intelligence Suite? Starten Sie mit diesem Tutorial."
tool:
  - Dashboard
---

# Intelligence-Suite-Tutorial

> Neu bei der Braze Intelligence Suite? Starten Sie mit diesem Tutorial! Allgemeine Informationen finden Sie unter [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutorial: Schnellrestaurant

Stellen Sie sich vor, Sie arbeiten bei SandwichEmperor, einem Schnellrestaurant mit einem neuen zeitlich begrenzten Menüpunkt: dem Royal Roast. Wir nutzen zwei Intelligence-Suite-Funktionen, um personalisierte Aktionen in einem Canvas zu senden.

### Schritt 1: Intelligent Timing für den Zeitpunkt der Benachrichtigungen nutzen

Wir nutzen Intelligent Timing, um die vergangenen Interaktionen unserer Nutzer mit der App und jedem Nachrichtenkanal zu analysieren und automatisch die beste Zeit zu wählen, um jedem Nutzer den Royal Roast zu promoten. Manche Nutzer erhalten die Aktion nachmittags, andere abends.

Für Nutzer ohne ausreichend vergangene Interaktionen geben wir eine Fallback-Zeit vor: die bei allen Nutzern beliebteste App-Nutzungszeit.

![Intelligent-Timing-Zustelleinstellungen für einen Nachrichten-Schritt.]({% image_buster /assets/img/intelligence_suite1.png %})

### Schritt 2: Intelligent Selection für die Auswahl der Aktion nutzen

Für die eigentlichen Werbenachrichten nutzen wir Intelligent Selection, um drei verschiedene Nachrichten (Push, E-Mail und SMS) für den Royal Roast zu testen. Intelligent Selection analysiert zweimal täglich die Performance aller Werbenachrichten und sendet schrittweise mehr von den besten und weniger von den übrigen.

Sobald Intelligent Selection genug Daten hat, um die beste Nachricht zu ermitteln, wird diese Nachricht bei 100 % der künftigen Sendungen verwendet.

![A/B-Testing-Bereich eines Canvas mit aktivierter Intelligent Selection.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Schritt 3: Canvas starten

Mit Intelligent Timing und Intelligent Selection haben wir die Royal-Roast-Aktionen für Zeitpunkt und Nachricht optimiert. Wir können den Canvas starten und beobachten, wie die Sendungen sich an die Nutzerpräferenzen anpassen.
