---
nav_title: Intelligentes Timing
article_title: Intelligentes Timing
page_order: 1.3
description: "Dieser Artikel gibt einen Überblick über Intelligentes Timing (früher Intelligent Delivery) und wie Sie diese Funktion in Kampagnen und Canvases nutzen."
---

# [![Braze Learning-Kurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligentes Timing

> Nutzen Sie Intelligentes Timing, um Ihre Nachricht jedem Nutzer zu dem von Braze ermittelten optimalen Sendezeitpunkt zuzustellen – dem Zeitpunkt, zu dem ein Nutzer am ehesten interagiert (öffnet oder klickt). So stellen Sie leichter sicher, dass Sie Ihre Nutzer zu ihrer bevorzugten Zeit ansprechen, was zu höherem Engagement führen kann.

## Über Intelligentes Timing

Braze berechnet den optimalen Sendezeitpunkt anhand einer statistischen Auswertung der vergangenen Interaktionen Ihrer Nutzer mit Ihrer App und mit jedem Nachrichtenkanal. Dabei werden u. a. folgende Interaktionsdaten verwendet:

- Sitzungszeiten
- Push Direct Opens
- Push Influenced Opens
- E-Mail-Klicks
- E-Mail-Opens (ohne [Machine Opens]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))
- SMS-Klicks (nur bei aktivierter [Link-Verkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) und erweitertem Tracking)

Hat ein Nutzer keine relevanten Engagement-Daten für die Berechnung des optimalen Sendezeitpunkts, können Sie eine Fallback-Zeit angeben.

## Anwendungsfälle

- Wiederkehrende Kampagnen senden, die nicht zeitkritisch sind
- Kampagnen mit Nutzern in mehreren Zeitzonen automatisieren
- Wenn Sie Ihre engagiertesten Nutzer ansprechen (sie haben die meisten Engagement-Daten)

Ausführliche Konfigurationsschritte für Kampagnen und Canvases, Quiet Hours, Fallback-Zeit, Einschränkungen und FAQ finden Sie in der vollständigen Version dieses Artikels im linken Inhaltsverzeichnis oder in der Braze-Dashboard-Hilfe.
