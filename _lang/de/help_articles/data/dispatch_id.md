---
nav_title: Verhalten bei der ID-Versendung
article_title: Verhalten der ID für den Versand
page_order: 0

page_type: solution
description: "Dieser Hilfeartikel befasst sich mit dem Verhalten der Versand-ID, einschließlich ihrer Verwendung, Auswirkungen und Einschränkungen."
---

# Verhalten bei der ID-Versendung

Eine `dispatch_id` ist die ID des Nachrichtenversands - eine eindeutige ID für jede von Braze gesendete "Übertragung". Nutzer:innen, die eine zeitlich geplante Nachricht erhalten, erhalten dieselbe `dispatch_id`. Normalerweise erhalten aktionsbasierte oder API-getriggerte Nachrichten eine eindeutige `dispatch_id` pro Nutzer:in, aber Nachrichten, die in engem Abstand zueinander gesendet werden, können dieselbe `dispatch_id` für mehrere Nutzer:in verwenden.

Dies kann dazu führen, dass zwei verschiedene Nutzer:innen unterschiedliche Versand-IDs für eine einzige Kampagne haben, wenn die Nachrichten zu zwei verschiedenen Zeiten gesendet wurden. Das liegt oft daran, dass die API-Anfragen separat gestellt wurden. Wenn beide Nutzer:innen in einer Kampagne zur gleichen Zielgruppe gehören, sind ihre Versand-IDs identisch.

## Verhalten der ID in Kampagnen

Geplante Kampagnen-Nachrichten erhalten die gleiche `dispatch_id`. Aktionsbasierte oder API-getriggerte Kampagnen-Nachrichten können eine eindeutige `dispatch_id` pro Nutzer erhalten, oder die `dispatch_id` kann für mehrere Nutzer:innen dieselbe sein, wenn sie in unmittelbarer Nähe oder mit demselben API-Aufruf gesendet werden, wie oben beschrieben. Zwei Nutzer:innen in Ihrer Zielgruppe für geplante Kampagnen haben beispielsweise jedes Mal, wenn die Kampagne geplant wird, dieselbe `dispatch_id`. Zwei Nutzer:innen in der Zielgruppe einer durch eine API getriggerten Kampagne können jedoch unterschiedliche IDs haben, wenn sie in separaten API-Aufrufen gesendet wurden und nicht in unmittelbarer Nähe zueinander liegen.

Kampagnen mit mehreren Kanälen verhalten sich genauso wie bei der Zustellung beschrieben.

{% alert warning %}
Eine `dispatch_id` wird für alle Canvas-Schritte zufällig generiert, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie "geplant" sind. Dies kann zu Inkonsistenzen bei der Generierung der IDs führen. Manchmal hat eine Canvas-Komponente eine eindeutige `dispatch_id` pro Nutzer:in und pro Sendung, oder sie hat gemeinsame IDs für alle Nutzer:innen pro Sendung.
{% endalert %}

## Template Versand ID in Nachrichten mit Liquid

Wenn Sie den Versand einer Nachricht aus der Nachricht heraus verfolgen möchten (z.B. in einer URL), können Sie ein Template im `dispatch_id` verwenden. Die Formatierung dafür finden Sie unter Canvas Attribute in unserer Liste der [unterstützten Tags für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Dies verhält sich genauso wie `api_id`, da `api_id` bei der Erstellung der Kampagne nicht verfügbar ist, wird es als Platzhalter eingefügt und in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt. Die ID wird generiert, bevor die Nachricht gesendet wird, und wird in die Sendezeit einbezogen.

{% alert warning %}
Das Liquid-Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Versand ID Currents Feld für E-Mail

Im Bestreben, unsere Currents-Funktionen weiter zu verbessern, ist `dispatch_id` auch ein Feld in Currents E-Mail-Ereignissen für alle Konnektoren. Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung bzw. Sendung generiert wird.

Während alle Kund:innen, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, bekommen Kunden, die entweder aktionsbasierte oder API-getriggerte Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Kampagne für die Konversion verantwortlich ist. So erhalten Sie mehr Insights und Informationen darüber, welche Arten von Kampagnen dazu beitragen, Ihre Geschäftsziele zu erreichen.

Sie können `dispatch_id` als [Tag für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [Ereignissen für das Engagement von Nachrichten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) oder bei der Verwendung von [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) oder [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) für Currents verwenden.

_Zuletzt aktualisiert am 15\. Juli 2021_
