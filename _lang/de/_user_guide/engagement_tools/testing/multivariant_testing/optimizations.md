---
nav_title: Optimierungen
article_title: Optimieren von A/B-Tests mit Gewinnervarianten oder personalisierten Varianten
page_order: 1
page_type: reference
description: "Erfahren Sie, wie Sie die Varianten „Gewinnvariante“ oder „Personalisierte Variante“ bei der Erstellung von multivariaten und A/B-Tests verwenden können."
---

# Optimierung von A/B-Tests mit Winning Variant oder personalisierten Varianten

Bei der [Erstellung eines A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) für E-Mail-, Push-, Webhook-, SMS- und WhatsApp-Kampagnen, die für einen einmaligen Versand geplant sind, können Sie eine Optimierung auswählen. Es gibt zwei Optimierungsmöglichkeiten: **Gewinnende Variante** und **personalisierte Variante**.

\![Optimierungsoptionen, die im Abschnitt A/B-Tests aufgeführt sind, wenn Sie Ihre Zielgruppe auswählen. Es werden drei Optionen aufgeführt: Keine Optimierung, Gewinnende Variante und Personalisierte Variante. Personalisierte Variante ist ausgewählt.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Beide Optionen funktionieren, indem Sie einen ersten Test an einen Prozentsatz Ihres Zielsegments senden. Nach Beendigung des Tests wird den verbleibenden Nutzern Ihrer Zielgruppe entweder die Variante mit der besten Leistung (Gewinnvariante) oder die Variante, mit der sie sich am ehesten beschäftigen werden (personalisierte Variante), zugesandt.

{% alert tip %}
Optimierungen finden Sie im Schritt **Zielgruppen** bei der Kampagnenerstellung unter **A/B-Tests**.
{% endalert %}

## Gewinnervariante

Das Versenden der Gewinner-Variante ist ähnlich wie ein normaler A/B-Test. Benutzer in dieser Gruppe erhalten die Gewinnvariante, wenn der erste Test abgeschlossen ist.

1. Wählen Sie **Gewinnvariante** und geben Sie dann an, welcher Prozentsatz Ihrer Kampagnenzielgruppe der Gewinnvariante zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- | 
| Gewinnervariante ermitteln | Die Metrik, für die Sie optimieren müssen. Wählen Sie zwischen *Unique Opens* oder *Clicks* für E-Mail, *Opens* für Push oder *Primary Conversion Rate* für alle Kanäle. Die Wahl von *Öffnungen* oder *Klicks* zur Ermittlung des Gewinners hat keinen Einfluss darauf, was Sie für die [Conversion-Ereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) der Kampagne wählen. <br><br>Denken Sie daran, dass bei Verwendung einer Kontrollgruppe die Benutzer in der Kontrollgruppe keine *Öffnungen* oder *Klicks* durchführen können, so dass die Leistung der Kontrollgruppe garantiert `0` ist. Folglich kann die Kontrollgruppe den A/B-Test nicht bestehen. Möglicherweise möchten Sie dennoch eine Kontrollgruppe verwenden, um andere Metriken für Nutzer:innen zu tracken, die keine Nachricht erhalten haben. |
| Gewinnervariante – Sendungsuhrzeit | Das Datum und die Uhrzeit, zu der die Gewinnvariante gesendet wird. |
| Wenn keine Gewinnervariante ermittelt werden kann | Was passiert, wenn keine Variante mit einem statistisch signifikanten Vorsprung gewinnt? Wählen Sie, ob Sie die Variante mit der besten Leistung trotzdem versenden möchten oder ob Sie den Test beenden und keine weiteren Nachrichten versenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Personalisierte Variante

Verwenden Sie personalisierte Varianten, um jedem Nutzer in Ihrem Zielsegment die Variante zu senden, mit der er sich am ehesten beschäftigt.

Um die beste Variante für jeden Nutzer zu ermitteln, sendet Braze einen ersten Test an einen Teil Ihrer Zielgruppe, um nach Zusammenhängen zwischen Nutzereigenschaften und Nachrichtenpräferenzen zu suchen. Anhand der Reaktionen der Nutzer:innen auf die einzelnen Varianten im ersten Test wird anhand dieser Merkmale bestimmt, welche verbleibenden Nutzer:innen die einzelnen Varianten erhalten. Wenn keine Assoziationen gefunden werden und keine Personalisierungen vorgenommen werden können, wird die Gewinnervariante automatisch an die verbleibenden Benutzer gesendet. Wenn Sie mehr darüber erfahren möchten, wie personalisierte Varianten ermittelt werden, lesen Sie bitte die [Analyse von multivariaten und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Wählen Sie **Personalisierte Variante** und geben Sie dann an, welcher Prozentsatz Ihrer Kampagnenzielgruppe der Gruppe Personalisierte Variante zugewiesen werden soll.
2. Konfigurieren Sie die folgenden zusätzlichen Einstellungen.

| Feld | Beschreibung |
| --- | --- | 
| Personalisierte Variante ermitteln | Die Metrik, für die Sie optimieren müssen. Wählen Sie zwischen *Unique Opens* oder *Clicks* für E-Mail, *Opens* für Push oder *Primary Conversion Rate* für alle Kanäle. Die Wahl von *Öffnungen* oder *Klicks* zur Ermittlung des Gewinners hat keinen Einfluss darauf, was Sie für die [Conversion-Ereignisse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) der Kampagne wählen. <br><br>Denken Sie daran, dass bei Verwendung einer Kontrollgruppe die Benutzer in der Kontrollgruppe keine *Öffnungen* oder *Klicks* durchführen können, so dass die Leistung der Kontrollgruppe garantiert `0` ist. Folglich kann die Kontrollgruppe den A/B-Test nicht bestehen. Möglicherweise möchten Sie dennoch eine Kontrollgruppe verwenden, um andere Metriken für Nutzer:innen zu tracken, die keine Nachricht erhalten haben. |
| Personalisierte Variante – Sendungsuhrzeit | Das Datum und die Uhrzeit, zu der die personalisierte Variante gesendet wird. |
| Wenn keine personalisierte Variante ermittelt werden kann | Was passiert, wenn keine personalisierten Varianten gefunden werden? Wählen Sie, ob Sie stattdessen die Gewinner-Variante senden möchten oder ob Sie den Test beenden und keine weiteren Nachrichten senden möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analytics

Wenn Sie mehr über die Ergebnisse Ihres A/B-Tests mit einer Optimierung erfahren möchten, lesen Sie die [Analyse von multivariaten und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

