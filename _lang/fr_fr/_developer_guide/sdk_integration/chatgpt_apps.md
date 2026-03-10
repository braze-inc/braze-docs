---
page_order: 2.1
nav_title: Applications ChatGPT
article_title: Intégrer Braze aux applications ChatGPT
description: "Découvrez comment intégrer Braze à ChatGPT Apps afin de permettre l'analyse/analytique et la journalisation des événements dans les applications basées sur l'intelligence artificielle."
platform:
  - ChatGPT Apps
---

# Intégrer Braze aux applications ChatGPT

> Ce guide explique comment intégrer Braze aux applications ChatGPT afin de permettre l'analyse/analytique et la journalisation des événements dans les applications basées sur l'intelligence artificielle.

![Une carte de contenu intégrée à l'application ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Aperçu

Les applications ChatGPT offrent une plateforme performante pour créer des applications conversationnelles basées sur l'intelligence artificielle. En intégrant Braze à votre application ChatGPT, vous pouvez continuer à contrôler vos données first-party à l'ère de l'intelligence artificielle, notamment en :

- Suivez l'engagement et le comportement des utilisateurs au sein de votre application ChatGPT (par exemple, en identifiant les questions ou les fonctionnalités de chat que vos clients utilisent).
- Segmentez et reciblez les campagnes Braze en fonction des modèles d'interaction basés sur l'intelligence artificielle (par exemple, en envoyant des e-mails aux utilisateurs qui ont utilisé le chat plus de trois fois par semaine).

### Principaux avantages

- **Maîtrisez le parcours client :** Lorsque les utilisateurs interagissent avec votre marque via ChatGPT, vous conservez une visibilité sur leur comportement, leurs préférences et leurs habitudes d'engagement. Ces données sont directement transférées vers les profils utilisateurs Braze, et non pas uniquement vers les analyses de la plateforme d'intelligence artificielle.
- **Reciblage multiplateforme :** Suivez les interactions des utilisateurs dans votre application ChatGPT et reciblez-les sur vos canaux propriétaires (e-mails, SMS, notifications push, messages in-app) avec des campagnes personnalisées basées sur leurs habitudes d'utilisation de l'intelligence artificielle.
- **Renvoyer du contenu promotionnel 1:1 aux conversations ChatGPT :** Diffusez [des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) Braze, [des cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) et bien plus encore directement dans votre expérience ChatGPT à l'aide des composants d'interface utilisateur conversationnelle personnalisés que votre équipe a créés pour votre application.
- **Attribution du chiffre d'affaires :** Suivez les achats et les conversions provenant des interactions avec l'application ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Conditions préalables

Avant d'effectuer l'intégration de Braze à votre application ChatGPT, vous devez disposer des éléments suivants :

- Une nouvelle application web et une clé API dans votre espace de travail Braze
- Une [application ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) développée sur la plateforme OpenAI ([application exemple OpenAI](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

