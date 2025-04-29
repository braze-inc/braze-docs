---
nav_title: Voraussichtliche Abwanderung
article_title: Voraussichtliche Abwanderung
page_order: 6.4
layout: dev_guide
alias: /predictive_churn/
search_rank: 2
guide_top_header: "Voraussichtliche Abwanderung"
guide_top_text: "Die Kundenabwanderung, auch bekannt als Kundenfluktuation oder Kundenverlust, ist eine der wichtigsten Metriken, die wachsende Unternehmen berücksichtigen müssen. Die richtigen Tools für den Umgang mit Abwanderung zu haben, ist entscheidend, um Verluste zu minimieren und die Kundenbindung zu maximieren. Um diesen potenziell abwandernden Benutzern zuvorzukommen, bietet Braze mit Predictive Churn einen proaktiven Ansatz zur Minimierung der zukünftigen Abwanderung."
description: "Diese Landing-Page befasst sich mit Predictive Churn, einem Tool, mit dem Sie definieren können, was Abwanderung für Ihr Unternehmen bedeutet und welche Nutzer:innen Sie von der Abwanderung abhalten möchten."

guide_featured_title: "Themen"
guide_featured_list:
- name: Erstellen einer Abwanderungsprognose
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Vorhersage-Analytik
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Messaging-Nutzer:innen"
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg
- name: Fehlersuche
  link: /docs/user_guide/brazeai/predictive_suite/predictive_churn/prediction_faq/
  image: /assets/img/braze_icons/annotation-question.svg

---

## Übersicht

![Eine Übersicht über die Abwanderung, die eine Zielgruppe für Prognosen mit Training mit historischen Daten umfasst. Dies trägt zur Vorhersage des Risikos zukünftiger Abwanderung bei, indem die heutige prognostizierte Zielgruppe mit einem Abwanderungs-Risiko-Score gemessen wird.][1]

> Mit Predictive Churn können Sie definieren, was Abwanderung für Ihr Unternehmen bedeutet[(Definition von Abwanderung]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn)) und welche Nutzer:innen Sie von der Abwanderung abhalten möchten[(Prognose-Zielgruppen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience)). Wenn Sie eine Vorhersage erstellen, trainiert Braze ein maschinelles Lernmodell mit [Gradient-Boosted-Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um Benutzer zu identifizieren, bei denen ein Abwanderungsrisiko besteht, indem es aus den Aktivitätsmustern früherer Benutzer lernt, die gemäß Ihrer Definition abgewandert sind und nicht.

Sobald das Prognosemodell erstellt ist, wird den Nutzern in der Prognosegruppe ein [Churn-Risiko-Score]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) zwischen 0 und 100 zugewiesen, der angibt, wie hoch die Wahrscheinlichkeit ist, dass sie nach Ihrer Definition abwandern. Je höher die Punktzahl, desto wahrscheinlicher ist es, dass ein:e Nutzer:in abwandert. 

Die Aktualisierung der Risikobewertungen für die Zielgruppe der Prognosen kann in einem [von Ihnen gewählten Rhythmus]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) erfolgen. Auf diese Weise können Sie Nutzer, bei denen das Risiko besteht, dass sie abwandern, erreichen, bevor sie es tatsächlich tun, und verhindern, dass es überhaupt dazu kommt. Mithilfe von bis zu drei aktiven Prognosen können Sie Predictive Churn nutzen, um individuelle Modelle zu erstellen, mit denen Sie die Abwanderung in bestimmten Segmenten Ihrer Nutzer:innen verhindern können, die Sie als besonders wertvoll erachten.

## Zugang zu Predictive Churn

Die Seite **Prognosen** befindet sich im Bereich **Analysen**. Für einen vollständigen Zugang wenden Sie sich bitte an Ihren Kundenbetreuer.

Bevor Sie dieses Feature kaufen, ist es in der Vorschau verfügbar. Dies erlaubt Ihnen, eine Demo-Prognose der Abwanderung mit synthetischen Daten zu sehen und jeweils ein Prognosemodell für die Abwanderung auf der Grundlage Ihrer Nutzerdaten zu erstellen. Diese Vorschau erlaubt es Ihnen nicht, Nutzer:innen für Messaging nach dem Abwanderungsrisiko zusammenzustellen und wird nach der Erstellung nicht regelmäßig aktualisiert.

Mit der Vorschau können Sie auch Ihre eine Vorhersage bearbeiten und neu erstellen oder sie archivieren und weitere erstellen, um die erwartete [Vorhersagequalität]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) verschiedener [Definitionen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) zu testen.

<br><br>

[1]: {% image_buster /assets/img/churn/churn_overview.png %}
