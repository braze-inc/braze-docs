---
nav_title: Verhalten bei der Versand-ID
article_title: Verhalten bei der Versand-ID
page_order: 0

page_type: solution
description: "Dieser Hilfe-Artikel behandelt das Verhalten der Versand-ID, einschließlich ihrer Verwendung, Auswirkungen und Einschränkungen."
---

# Verhalten der Versand-ID

Eine `dispatch_id` ist die ID des Nachrichtenversands - eine eindeutige ID für jede von Braze gesendete "Übertragung". Benutzer, denen eine geplante Nachricht gesendet wird, erhalten dieselbe `dispatch_id`. Normalerweise erhalten aktionsbasierte oder API-ausgelöste Nachrichten eine eindeutige `dispatch_id` pro Benutzer, aber Nachrichten, die in engem Abstand zueinander gesendet werden, können dieselbe `dispatch_id` für mehrere Benutzer verwenden.

Dies kann dazu führen, dass zwei verschiedene Benutzer unterschiedliche Versand-IDs für eine einzige Kampagne haben, wenn die Nachrichten zu zwei verschiedenen Zeiten gesendet wurden. Das liegt oft daran, dass die API-Anfragen separat gestellt wurden. Wenn beide Benutzer in einer einzigen Sendung zur gleichen Kampagnenzielgruppe gehören, sind ihre Versand-IDs identisch.

## Verhalten der Versand-ID in Kampagnen

Geplante Kampagnennachrichten erhalten die gleiche `dispatch_id`. Aktionsbasierte oder API-ausgelöste Kampagnennachrichten können eine eindeutige `dispatch_id` pro Benutzer erhalten, oder die `dispatch_id` kann für mehrere Benutzer dieselbe sein, wenn sie in unmittelbarer Nähe oder mit demselben API-Aufruf gesendet werden, wie oben beschrieben. Zwei Benutzer in Ihrer geplanten Kampagne haben zum Beispiel jedes Mal, wenn die Kampagne geplant wird, dieselbe `dispatch_id`. Zwei Benutzer in der Zielgruppe einer API-ausgelösten Kampagne können jedoch unterschiedliche Versand-IDs haben, wenn sie in getrennten API-Aufrufen und nicht in unmittelbarer Nähe zueinander gesendet wurden.

Für Multichannel-Kampagnen gilt das gleiche Verhalten wie für ihre Versandart beschrieben.

{% alert warning %}
Eine `dispatch_id` wird zufällig für alle Canvas-Schritte generiert, da Braze Canvas-Schritte als ausgelöste Ereignisse behandelt, auch wenn sie "geplant" sind. Dies kann zu Inkonsistenzen bei der Generierung der IDs führen. Manchmal hat eine Canvas-Komponente eine eindeutige `dispatch_id` pro Benutzer und Sendung, oder sie hat gemeinsame Versand-IDs für alle Benutzer und Sendungen.
{% endalert %}

## Vorlage Versand-ID in Nachrichten mit Liquid

Wenn Sie den Versand einer Nachricht aus der Nachricht heraus verfolgen wollen (z.B. in einer URL), können Sie in der Vorlage `dispatch_id`. Die Formatierung dafür finden Sie unter Canvas-Attribute in unserer Liste der [unterstützten Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Dies verhält sich genau wie `api_id`, da `api_id` bei der Erstellung der Kampagne nicht verfügbar ist, wird es als Platzhalter eingefügt und in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt. Die ID wird generiert, bevor die Nachricht gesendet wird, und wird in die Sendezeit eingerechnet.

{% alert warning %}
Liquid Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Versand-ID Aktuelles Feld für E-Mail

In dem Bestreben, unsere Currents-Funktionen weiter zu verbessern, ist `dispatch_id` auch ein Feld in Currents-E-Mail-Ereignissen für alle Verbindungsarten. Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung oder Sendung generiert wird.

Während alle Kunden, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, erhalten Kunden, die entweder aktionsbasierte oder API-ausgelöste Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Kampagne für die Konversion verantwortlich ist. So erhalten Sie mehr Einblicke und Informationen darüber, welche Arten von Kampagnen dazu beitragen, Ihre Geschäftsziele zu erreichen.

Sie können `dispatch_id` als [Tag für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [Ereignissen zur Einbindung von Nachrichten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) oder bei der Verwendung von [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) oder [Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/) für Currents verwenden.

_Zuletzt aktualisiert am 15\. Juli 2021_
