---
nav_title: "Anleitung: Restaurant mit schnellem Dienst"
article_title: Intelligence Suite-Anleitung
page_order: 10
search_rank: 12
description: "Sind Sie neu in der Braze Intelligence Suite? Beginnen Sie mit diesem Lernprogramm."
tool:
  - Dashboard
---

# Intelligence Suite-Anleitung

> Neu in der Braze Intelligence Suite? Beginnen Sie mit dieser Anleitung! Weitere allgemeine Informationen finden Sie unter [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/).

## Anleitung: Restaurant mit schnellem Dienst

Stellen wir uns vor, wir arbeiten bei SandwichEmperor, einem Schnellrestaurant, das ein neues, zeitlich begrenztes Menüangebot hat: den Royal Roast. Wir werden zwei Features der Intelligence Suite verwenden, um personalisierte Aktionen in einem Canvas zu versenden.

### Schritt 1: Verwenden Sie intelligentes Timing für den Versand von Benachrichtigungen

Wir verwenden Intelligent Timing, um die vergangenen Interaktionen unserer Nutzer mit unserer App und den einzelnen Nachrichtenkanälen zu analysieren und dann automatisch den besten Zeitpunkt auszuwählen, um den Royal Roast für jeden Nutzer zu bewerben. Einige Nutzer erhalten die Aktion vielleicht am Nachmittag, andere am Abend. 

Für Benutzer, die nicht über genügend frühere Interaktionen verfügen, die analysiert werden können, bieten wir einen Ausweichzeitpunkt an: die beliebteste Zeit für die Nutzung der App unter allen Benutzern.

\![Intelligente Timing Zustellung für einen Schritt der Nachricht.]({% image_buster /assets/img/intelligence_suite1.png %})

### Schritt 2: Verwenden Sie die intelligente Auswahl, um die Aktion auszuwählen

Für die eigentlichen Werbebotschaften werden wir Intelligent Selection verwenden, um drei verschiedene Nachrichten (Push-Benachrichtigung, E-Mail und SMS) für den Royal Roast zu testen. Intelligent Selection analysiert die Leistung aller unserer Werbebotschaften zweimal täglich und sendet dann nach und nach mehr von den leistungsstärksten Botschaften und weniger von den anderen.

Nachdem die Intelligente Auswahl genügend Daten gesammelt hat, um die Nachricht mit der besten Leistung zu ermitteln, wird diese Nachricht bei 100 % aller zukünftigen Sendungen verwendet.

\![A/B-Tests Abschnitt eines Canvas mit aktivierter intelligenter Auswahl.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Schritt 3: Starten Sie das Canvas

Mit Intelligent Timing und Intelligent Selection haben wir unsere Royal Roast-Promotions so gestaltet, dass sie in Bezug auf Timing und Botschaft optimiert sind. Wir können unseren Canvas starten und beobachten, wie sich unsere Sendungen an die Vorlieben der Nutzer:innen anpassen.
