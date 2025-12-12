---
nav_title: Tracking von Transaktions-E-Mails
article_title: Tracking von Transaktions-E-Mails
page_order: 1
description: "Dieser referenzierte Artikel beschreibt, wie Sie Realtime Tracking für Transaktions-E-Mails Kampagnen einrichten können."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Tracking von Transaktions-E-Mails

> Auf dieser Seite wird beschrieben, wie Sie das Realtime Tracking für [Transaktions-E-Mails Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) einrichten. Weitere Informationen über den Endpunkt selbst finden Sie unter [Senden von Transaktions-E-Mails mit API-getriggerter Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Wenn Sie Transaktions-E-Mails wie Auftragsbestätigungen oder die Rücksetzung von Passwörtern versenden, ist es wichtig zu wissen, ob diese Ihre Kund:in erreichen. Mit Braze Transaktions-HTTP-Event-Postbacks erhalten Sie Insights in Realtime über den Status jeder Transaktions-E-Mail, so dass Sie bei Problemen schnell handeln können.

Verwenden Sie dieses Feature, um:

- **Überwachen Sie Ihre E-Mails in Realtime:** Sehen Sie sofort, ob Nachrichten gesendet, verarbeitet und zugestellt werden oder ob Probleme auftreten.
- **Reagieren Sie proaktiv:** Wiederholen Sie Nachrichten, wechseln Sie zu einem anderen Kanal wie SMS oder verwenden Sie Fallback-Systeme, um sicherzustellen, dass Ihre Mitteilungen zugestellt werden.

## Tracking Ihrer Transaktions-E-Mails

{% multi_lang_include http_event_postback.md %}


