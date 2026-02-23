---
page_order: 2.1
nav_title: ChatGPT Apps
article_title: Integration von Braze mit ChatGPT Apps
description: "Erfahren Sie, wie Sie Braze in ChatGPT Apps integrieren, um Analytics und Ereignisprotokollierung in KI-gesteuerten Anwendungen zu ermöglichen."
platform:
  - ChatGPT Apps
---

# Integration von Braze in ChatGPT-Apps

> In diesem Leitfaden erfahren Sie, wie Sie Braze in ChatGPT-Apps integrieren, um Analytics und Ereignisprotokollierung in KI-gesteuerten Anwendungen zu ermöglichen.

![Eine in die ChatGPT App integrierte Content-Card.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Übersicht

ChatGPT Apps bieten eine leistungsstarke Plattform für den Aufbau von KI-Konversationsanwendungen. Durch die Integration von Braze in Ihre ChatGPT App können Sie auch im Zeitalter der KI die Kontrolle über First-Party-Daten behalten, einschließlich der Frage, wie Sie diese kontrollieren können:

- Tracking des Engagements und des Verhaltens von Nutzern:innen in Ihrer ChatGPT App (z.B. um festzustellen, welche Fragen oder Features Ihre Nutzer:innen nutzen)
- Segmentierung und Retargeting von Braze Kampagnen auf der Grundlage von KI-Interaktionsmustern (z. B. Mailen von Nutzer:innen, die den Chat mehr als dreimal pro Woche genutzt haben)

### Wichtigste Vorteile

- **Machen Sie sich Ihre Customer Journey zu eigen:** Während die Nutzer:innen über ChatGPT mit Ihrer Marke interagieren, behalten Sie den Überblick über ihr Verhalten, ihre Vorlieben und ihr Engagement. Diese Daten fließen direkt in die Nutzerprofile von Braze ein, nicht nur in die Analytics-Plattform der KI.
- **Plattformübergreifendes Retargeting:** Verfolgen Sie die Interaktionen von Nutzern in Ihrer ChatGPT App und richten Sie sie über Ihre Owned Kanäle (E-Mail, SMS, Push-Benachrichtigungen, In-App-Nachrichten) mit personalisierten Kampagnen auf der Grundlage ihres KI-Nutzungsverhaltens erneut an.
- **Geben Sie 1:1 Werbeinhalte an ChatGPT-Konversationen zurück:** Stellen Sie [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) und mehr von Braze direkt in Ihrem ChatGPT-Erlebnis bereit, indem Sie die speziell entwickelten UI-Komponenten für die Konversation nutzen, die Ihr Team für Ihre App entwickelt hat.
- **Attribution von Erträgen:** Verfolgen Sie Käufe und Konversionen, die durch Interaktionen mit der ChatGPT App zustande kommen.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Voraussetzungen

Bevor Sie Braze in Ihre ChatGPT App integrieren können, müssen Sie über Folgendes verfügen:

- Eine neue Internet App und ein API-Schlüssel in Ihrem Braze Workspace
- Eine [ChatGPT App](https://openai.com/index/introducing-apps-in-chatgpt/), die auf der OpenAI Plattform erstellt wurde[(OpenAI Beispiel-App](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

