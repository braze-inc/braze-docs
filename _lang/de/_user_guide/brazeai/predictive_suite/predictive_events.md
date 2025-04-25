---
nav_title: Voraussichtliche Events
article_title: Voraussichtliche Events
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "Voraussichtliche Events"
guide_top_text: "Zu wissen, welche Ihrer Nutzer:innen mit hoher Wahrscheinlichkeit ein bestimmtes Ereignis - z.B. einen Kauf - durchführen werden, ist ein wichtiger Insight für wachsende Unternehmen. Wie können Sie ohne sie entscheiden, welche Kampagnen Sie erstellen wollen? Wer sollte Ermäßigungen und Werbeaktionen erhalten? Wohin mit einem begrenzten Budget? Braze hilft bei der Beantwortung dieser Fragen mit Predictive Events (früher Predictive Purchases), einem Modell für maschinelles Lernen, das es Marketingteams leicht macht, zukünftiges Verhalten zu verstehen und ihre Ressourcen auf Engagement und umsatzmaximierende Kampagnen zu konzentrieren."
description: "Dieser Artikel befasst sich mit Predictive Events (früher Predictive Purchases), einem Tool, mit dem Marketingexperten Nutzer auf der Grundlage ihrer Wahrscheinlichkeit, ein Ereignis auszuführen, identifizieren und benachrichtigen können."

guide_featured_title: "Themen"
guide_featured_list:
- name: Erstellen einer Vorhersage
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Vorhersage-Analytik
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Messaging-Nutzer:innen"
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## Übersicht

![Grafik mit dem Titel „Wie prädiktive Events funktionieren“, die Nutzerdaten anzeigt, die in das maschinelle Lernmodell eingespeist werden. Die Beschriftung lautet: "Trainieren Sie mit historischen Daten, vergleichen Sie das Verhalten der Nutzer:innen, die das Ereignis in einem bestimmten Zeitraum durchgeführt haben, mit denen, die es nicht durchgeführt haben." Es zeigt auch die Ergebnisse des maschinellen Lernens, bei dem die Nutzer:innen nach der geringsten bis zur höchsten Wahrscheinlichkeit, das Event durchzuführen, eingestuft werden. Die Beschriftung lautet: "Prognostizieren Sie die Wahrscheinlichkeit zukünftiger Ereignisse, weisen Sie den Nutzer:innen einen Wahrscheinlichkeitswert zu, um ein präzises und bequemes Targeting zu ermöglichen."][1]

> Mit Predictive Events erhalten Marketingexperten ein leistungsstarkes Tool zur Identifizierung und Ansprache von Nutzern auf der Grundlage der Wahrscheinlichkeit, dass sie ein Ereignis durchführen. Wenn Sie eine Ereignisvorhersage erstellen, trainiert Braze ein Modell für maschinelles Lernen mit Hilfe von [Gradient Boosted Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um aus früheren Aktivitäten zu lernen und zukünftige Aktivitäten vorherzusagen.

Sobald eine Vorhersage erstellt wurde, wird dem Benutzer ein [Wahrscheinlichkeitswert]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) zwischen 0 und 100 zugewiesen, der angibt, wie wahrscheinlich es ist, dass er Ihr ausgewähltes Ereignis ausführt. Je höher die Punktzahl ist, desto wahrscheinlicher ist es, dass ein:e Nutzer:in dieses Event ausführt. Die Benutzer werden auch nach Kategorien mit niedriger, mittlerer und hoher Wahrscheinlichkeit sortiert.

Der wahre Wert von Predictive Events liegt in der Verwendung der Vorhersageergebnisse zur Erstellung eines Segments oder einer Kampagne. Vermarkter können gezielte Kampagnen direkt auf der **Vorhersageseite** erstellen, um sofortige umsatzsteigernde Ergebnisse zu erzielen, oder ein Segment für eine zukünftige Kampagne oder ein Canvas speichern. Sie wissen nicht, wen Sie zuerst ansprechen sollen? Lesen Sie unsere [strategischen Überlegungen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) zur Benachrichtigung von Nutzern auf der Grundlage ihres Wahrscheinlichkeitswertes.

## Zugriff auf voraussichtliche Events

Die Seite **Prognosen** befindet sich im Bereich **Analysen**. Für einen vollständigen Zugang wenden Sie sich bitte an Ihren Kundenbetreuer.

Bevor Sie dieses Feature kaufen, ist es in der Vorschau verfügbar. Dies erlaubt es Ihnen, eine Demo-Prognose mit synthetischen Daten zu sehen und jeweils eine Vorschau eines Prognosemodells zu erstellen. Diese Vorhersage wird auf der Grundlage Ihrer tatsächlichen Nutzerdaten erstellt, ermöglicht es Ihnen jedoch nicht, Nutzer entsprechend ihrer Wahrscheinlichkeitsbewertung für Nachrichten anzusprechen. Es wird auch nicht regelmäßig nach der Erstellung aktualisiert.

Mit der Vorschau können Sie auch diese eine Vorhersage bearbeiten und neu erstellen oder sie archivieren und weitere erstellen, um die erwartete [Vorhersagequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) für [verschiedene Zielgruppen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) zu testen und sich mit den Analysen vertraut zu machen.

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

