---
page_order: 2.1
nav_title: ChatGPT-Apps
article_title: Integrieren Sie Braze in ChatGPT-Apps
description: "Erfahren Sie, wie Sie Braze in ChatGPT-Apps integrieren können, um Analysen und Ereignisprotokollierung in KI-gestützten Anwendungen zu ermöglichen."
platform:
  - ChatGPT Apps
---

# Integrieren Sie Braze in ChatGPT-Apps.

> Dieser Leitfaden beschreibt, wie Sie die Integration von Braze in ChatGPT-Apps realisieren können, um Analytics und Ereignisprotokollierung in KI-gestützten Anwendungen zu ermöglichen.

![Eine in die ChatGPT-App integrierte Content-Card.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Übersicht

ChatGPT-Apps bieten eine leistungsstarke Plattform für die Entwicklung von KI-basierten Konversationsanwendungen. Durch die Integration von Braze in Ihre ChatGPT-App können Sie auch im Zeitalter der KI weiterhin die Kontrolle über Ihre First-Party-Daten behalten, einschließlich der folgenden Aspekte:

- Verfolgen Sie das Engagement und das Verhalten der Nutzer:innen innerhalb Ihrer ChatGPT-App (z. B. indem Sie ermitteln, welche Fragen oder Chat-Features Ihre Nutzer:innen nutzen).
- Segmentieren und Retargeten Sie Braze-Kampagnen auf der Grundlage von KI-Interaktionsmustern (z. B. indem Sie E-Mails an Nutzer:innen senden, die den Chat mehr als dreimal pro Woche genutzt haben).

### Wesentliche Vorteile

- **Übernehmen Sie die Verantwortung für die Customer Journey:** Während die Nutzer:innen über ChatGPT mit Ihrer Marke interagieren, behalten Sie Einblick in ihr Verhalten, ihre Präferenzen und ihr Engagement. Diese Daten werden direkt in die Braze-Nutzerprofile übertragen und nicht nur in die Analytics der KI-Plattform.
- **Plattformübergreifendes Retargeting:** Verfolgen Sie die Interaktionen der Nutzer in Ihrer ChatGPT-App und sprechen Sie sie über Ihre Owned Channels (E-Mail, SMS, Push-Benachrichtigungen, In-App-Nachrichten) mit personalisierten Kampagnen an, die auf ihren KI-Nutzungsmustern basieren.
- **Geben Sie 1:1-Aktionen an ChatGPT-Konversationen zurück:** Versenden Sie Braze[-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) und mehr direkt innerhalb Ihrer ChatGPT-Erfahrung, indem Sie die benutzerdefinierten Konversations-UI-Komponenten verwenden, die Ihr Team für Ihre App entwickelt hat.
- **Umsatz-Attribution:** Verfolgen Sie Käufe und Konversionen, die aus Interaktionen mit der ChatGPT-App stammen.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Voraussetzungen

Bevor Sie die Integration von Braze in Ihre ChatGPT-App durchführen, müssen Sie über Folgendes verfügen:

- Eine neue Web-App und ein API-Schlüssel in Ihrem Braze-Workspace
- Eine [ChatGPT-App,](https://openai.com/index/introducing-apps-in-chatgpt/) die auf der OpenAI-Plattform erstellt wurde ([OpenAI-Beispielapp](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

