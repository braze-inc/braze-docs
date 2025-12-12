---
nav_title: Voraussichtliche Abwanderung
article_title: Voraussichtliche Abwanderung
description: "Diese Landing-Page befasst sich mit Predictive Churn, einem Tool, mit dem Sie definieren können, was Abwanderung für Ihr Unternehmen bedeutet und welche Nutzer:innen Sie von der Abwanderung abhalten möchten."
page_order: 2.0
alias: /predictive_churn/
search_rank: 2
---

# Voraussichtliche Abwanderung

> Mit Predictive Churn können Sie definieren, was voraussichtliche Abwanderung für Ihr Unternehmen bedeutet und die Nutzer:innen identifizieren, die Sie behalten möchten. Wenn Sie eine Prognose erstellen, trainiert Braze ein Modell des maschinellen Lernens mit Hilfe von [gradientenverstärkten Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um gefährdete Nutzer:innen zu erkennen, indem es Muster aus dem vergangenen Verhalten analysiert - sowohl von Nutzer:innen, die abgewandert sind, als auch von solchen, die nicht abgewandert sind.

{% alert tip %}
Weitere Informationen finden Sie unter [Churn-Definition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) und [Prognose Zielgruppe]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## Über voraussichtliche Abwanderung

Nachdem das Prognosemodell erstellt wurde, wird den Nutzern:innen der Zielgruppe ein [Churn-Risiko-Score]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/#churn_score) zwischen 0 und 100 zugewiesen, der angibt, wie wahrscheinlich es ist, dass sie nach Ihrer Definition abwandern. Je höher die Punktzahl, desto wahrscheinlicher ist es, dass ein:e Nutzer:in abwandert. 

Die Aktualisierung der Risikobewertungen für die Zielgruppe der Prognosen kann in einem [von Ihnen gewählten Rhythmus]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-predictions) erfolgen. Auf diese Weise können Sie Nutzer, bei denen das Risiko besteht, dass sie abwandern, erreichen, bevor sie es tatsächlich tun, und verhindern, dass es überhaupt dazu kommt. Mithilfe von bis zu drei aktiven Prognosen können Sie Predictive Churn nutzen, um individuelle Modelle zu erstellen, mit denen Sie die Abwanderung in bestimmten Segmenten Ihrer Nutzer:innen verhindern können, die Sie als besonders wertvoll erachten.

![Eine Übersicht über die Abwanderung, die eine Zielgruppe für Prognosen in der Vergangenheit mit Training mit historischen Daten umfasst. Dies trägt zur Vorhersage des Risikos zukünftiger Abwanderung bei, indem die heutige prognostizierte Zielgruppe mit einem Abwanderungs-Risiko-Score gemessen wird.]({% image_buster /assets/img/churn/churn_overview.png %})

## Zugriff auf voraussichtliche Abwanderung

Die Seite **Prognosen** befindet sich im Bereich **Analysen**. Für einen vollständigen Zugang wenden Sie sich bitte an Ihren Kundenbetreuer.

Bevor Sie dieses Feature kaufen, ist es in der Vorschau verfügbar. Dies erlaubt Ihnen, eine Demo-Prognose der Abwanderung mit synthetischen Daten zu sehen und jeweils ein Prognosemodell für die Abwanderung auf der Grundlage Ihrer Nutzerdaten zu erstellen. Diese Vorschau erlaubt es Ihnen nicht, Nutzer:innen für Messaging nach dem Abwanderungsrisiko zusammenzustellen und wird nach der Erstellung nicht regelmäßig aktualisiert.

Mit der Vorschau können Sie auch Ihre eine Vorhersage bearbeiten und neu erstellen oder sie archivieren und weitere erstellen, um die erwartete [Vorhersagequalität]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) verschiedener [Definitionen]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) zu testen.
