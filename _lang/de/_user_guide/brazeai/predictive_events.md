---
nav_title: Voraussichtliche Events
article_title: Voraussichtliche Events
description: "Dieser Artikel befasst sich mit Predictive Events (früher Predictive Purchases), einem Tool, mit dem Marketingexperten Nutzer auf der Grundlage ihrer Wahrscheinlichkeit, ein Ereignis auszuführen, identifizieren und benachrichtigen können."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Voraussichtliche Events

> Mit Predictive Events erhalten Marketingexperten ein leistungsstarkes Tool zur Identifizierung und Ansprache von Nutzern auf der Grundlage der Wahrscheinlichkeit, dass sie ein Ereignis durchführen. Wenn Sie eine Ereignisvorhersage erstellen, trainiert Braze ein Modell für maschinelles Lernen mit Hilfe von [Gradient Boosted Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um aus früheren Aktivitäten zu lernen und zukünftige Aktivitäten vorherzusagen.

## Informationen zu voraussichtlichen Events

Nachdem eine Prognose erstellt wurde, wird den Nutzer:innen ein [Wahrscheinlichkeitswert]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) zwischen 0 und 100 zugewiesen, der angibt, wie wahrscheinlich es ist, dass sie Ihr ausgewähltes Ereignis durchführen. Je höher die Punktzahl ist, desto wahrscheinlicher ist es, dass ein:e Nutzer:in dieses Event ausführt. Die Benutzer werden auch nach Kategorien mit niedriger, mittlerer und hoher Wahrscheinlichkeit sortiert.

Der wahre Wert von Predictive Events liegt in der Verwendung der Vorhersageergebnisse zur Erstellung eines Segments oder einer Kampagne. Vermarkter können gezielte Kampagnen direkt auf der **Vorhersageseite** erstellen, um sofortige umsatzsteigernde Ergebnisse zu erzielen, oder ein Segment für eine zukünftige Kampagne oder ein Canvas speichern. Sie wissen nicht, wen Sie zuerst ansprechen sollen? Lesen Sie unsere [strategischen Überlegungen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) zur Benachrichtigung von Nutzern auf der Grundlage ihres Wahrscheinlichkeitswertes.

\![Grafik mit dem Titel "Wie Prognosen funktionieren", die zeigt, wie Nutzerdaten in das Modell des maschinellen Lernens getunnelt werden. Die Beschriftung lautet: "Trainieren Sie mit historischen Daten, vergleichen Sie das Verhalten der Nutzer:innen, die das Ereignis in einem bestimmten Zeitraum durchgeführt haben, mit denen, die es nicht durchgeführt haben." Es zeigt auch die Ergebnisse des maschinellen Lernens, bei dem die Nutzer:innen nach der geringsten bis zur höchsten Wahrscheinlichkeit, das Event durchzuführen, eingestuft werden. Die Beschriftung lautet: "Prognostizieren Sie die Wahrscheinlichkeit zukünftiger Ereignisse, weisen Sie den Nutzer:innen einen Wahrscheinlichkeitswert zu, um ein präzises und bequemes Targeting zu ermöglichen."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Zugriff auf prognostizierte Ereignisse

Die Seite **Prognosen** befindet sich im Bereich **Analysen**. Für einen vollständigen Zugang wenden Sie sich bitte an Ihren Kundenbetreuer.

Bevor Sie dieses Feature kaufen, ist es in der Vorschau verfügbar. Dies erlaubt es Ihnen, eine Demo-Prognose mit synthetischen Daten zu sehen und jeweils eine Vorschau eines Prognosemodells zu erstellen. Diese Vorhersage wird auf der Grundlage Ihrer tatsächlichen Nutzerdaten erstellt, ermöglicht es Ihnen jedoch nicht, Nutzer entsprechend ihrer Wahrscheinlichkeitsbewertung für Nachrichten anzusprechen. Es wird auch nicht regelmäßig nach der Erstellung aktualisiert.

Mit der Vorschau können Sie auch diese eine Vorhersage bearbeiten und neu erstellen oder sie archivieren und weitere erstellen, um die erwartete [Vorhersagequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) für [verschiedene Zielgruppen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) zu testen und sich mit den Analysen vertraut zu machen.
