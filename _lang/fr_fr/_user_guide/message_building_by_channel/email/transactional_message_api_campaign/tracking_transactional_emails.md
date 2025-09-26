---
nav_title: Suivi des e-mails transactionnels
article_title: Suivi des e-mails transactionnels
page_order: 1
description: "Cet article de référence explique comment implémenter le suivi en temps réel pour les campagnes d'e-mails transactionnels."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Suivi des e-mails transactionnels

> Cette page décrit comment implémenter le suivi en temps réel pour les [campagnes d'e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/). Pour plus d'informations sur l'endpoint lui-même, reportez-vous à la section [Envoyer des e-mails transactionnels à l'aide de la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/).

Lorsque vous envoyez des e-mails transactionnels, tels que des confirmations de commande ou des réinitialisations de mot de passe, il est essentiel de savoir s'ils atteignent vos clients. Avec les retours d'événements HTTP transactionnels de Braze, vous obtiendrez des informations en temps réel sur l'état de chaque e-mail transactionnel, ce qui vous permettra d'agir rapidement en cas de problème.

Utilisez cette fonctionnalité pour :

- **Surveillez vos e-mails en temps réel :** Voyez immédiatement si les messages sont envoyés, traités, livrés ou s'ils rencontrent des problèmes.
- **Réagissez de manière proactive :** Réessayez les messages, passez à un autre canal, comme les SMS, ou utilisez des systèmes de secours pour vous assurer que vos communications sont bien transmises.

## Suivi de vos e-mails transactionnels

{% multi_lang_include http_event_postback.md %}


