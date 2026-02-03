---
page_order: 2.1
nav_title: Applications ChatGPT
article_title: Intégrer Braze aux applications ChatGPT
description: "Découvrez comment intégrer Braze à ChatGPT Apps pour permettre l'analyse/analytique et l'enregistrement des événements au sein d'applications alimentées par l'intelligence artificielle."
platform:
  - ChatGPT Apps
---

# Intégrer Braze aux applications ChatGPT

> Ce guide explique comment intégrer Braze aux apps ChatGPT pour permettre l'analyse/analytique et l'enregistrement des événements au sein des applications alimentées par l'intelligence artificielle.

![Une carte de contenu intégrée à l'application ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Aperçu

Les apps ChatGPT constituent une plateforme puissante pour créer des applications conversationnelles d'intelligence artificielle. En intégrant Braze à votre app ChatGPT, vous pouvez continuer à maintenir le contrôle des données first-party à l'ère de l'intelligence artificielle, y compris comment :

- Suivre l'engagement et le comportement des utilisateurs au sein de votre application ChatGPT (par exemple, identifier les questions ou les fonctionnalités de chat que vos clients utilisent).
- Segmenter et recibler les campagnes Braze en fonction des schémas d'interaction avec l'intelligence artificielle (par exemple, envoyer un e-mail aux utilisateurs qui ont utilisé le chat plus de trois fois par semaine).

### Principaux avantages

- **Appropriez-vous votre parcours client :** Pendant que les utilisateurs interagissent avec votre marque par le biais de ChatGPT, vous gardez une visibilité sur leur comportement, leurs préférences et leurs modèles d'engagement. Ces données affluent directement sur les profils utilisateurs de Braze, et pas seulement sur les analyses/analytiques de la plateforme d'intelligence artificielle.
- **Reciblage multiplateforme :** Suivez les interactions des utilisateurs dans votre appli ChatGPT et reciblez-les sur vos canaux propriétaires (e-mail, SMS, notifications push, messages in-app) avec des campagnes personnalisées basées sur leurs schémas d'utilisation de l'intelligence artificielle.
- **Renvoyez du contenu promotionnel 1:1 dans les conversions de ChatGPT :** Diffusez des [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), des [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) et plus encore de Braze directement dans votre expérience sur l'application ChatGPT à l'aide des composants d'interface utilisateur conversationnelle personnalisés que votre équipe a créés pour votre application.
- **Attribution des chiffres d'affaires :** Suivez les achats et les conversions qui proviennent des interactions avec l'appli ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Conditions préalables

Avant d'intégrer Braze à votre application ChatGPT, vous devez disposer des éléments suivants :

- Une nouvelle application web et une clé API dans votre espace de travail Braze
- Une [application ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) créée dans la plateforme OpenAI[(OpenAI sample app)](https://github.com/openai/openai-apps-sdk-examples)

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

