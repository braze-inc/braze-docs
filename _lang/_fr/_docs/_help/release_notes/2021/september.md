---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for September 2021."
---

# September 2021

## Google Audience Sync

The Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) integration enables brands to extend the reach of their cross-channel customer journeys to Google Search, Google Shopping, Gmail, YouTube, and Google Display. Using your first-party customer data, you can securely deliver ads based upon dynamic behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (e.g., push, email, SMS, etc.) as part of a Braze Canvas can be used to trigger an ad to that user via Google's Customer Match.

## Best practice iOS SDK integration guide

This optional [iOS integration SDK guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/ios_sdk_integration/) takes you on a step-by-step journey on setup best practices when first integrating the iOS SDK and its core components into your application. This guide will help you build a `BrazeManager.swift` helper file that will decouple any dependencies on the Braze iOS SDK from the rest of your production code, resulting in one `import AppboyUI` in your entire application. This approach limits issues that arise from excessive SDK imports, making it easier to track, debug, and alter code.

## Predictive Purchases

Predictive Purchases give marketers a powerful tool for identifying and messaging users based on their likelihood to make a purchase. When you create a Purchase Prediction, Braze trains a machine learning model using [gradient boosted decision trees](https://en.wikipedia.org/wiki/Gradient_boosting) to learn from previous purchase activity and predict future purchase activity. Visit our [Predicitve Purchases]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/) doc to learn more.

## Drag & Drop Editor

With Braze Email, you can create completely custom and personalized email messages in either Campaigns or Canvas using our new Drag & Drop editing experience. Users can now drag editor blocks into their emails, allowing more intuitive customization. To learn how to get started with the Drag & Drop Editor, visit our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/).

## User alias import

To target users who don't have an `external_id`, you can import a list of users with user aliases. An alias serves as an alternative unique user identifier. It can be helpful if you are trying to market to anonymous users who haven't signed up or made an account with your app. Visit our [documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) to learn more.

## iOS 15 upgrade guide

This [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) outlines changes introduced in iOS 15 (WWDC21) and the required upgrade steps for your Braze iOS SDK integration.

## Android 12 upgrade guide

This [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) describes relevant changes introduced in Android 12 (2021) and the required upgrade steps for your Braze Android SDK integration.

## A2P 10DLC

A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type Application-to-Person (A2P) via un numéro de téléphone standard à 10 chiffres long code (10DLC). Les codes à 10 chiffres ont traditionnellement été conçus pour le trafic de personne à personne (P2P), ce qui a pour effet de contraindre les entreprises à un débit limité et à un filtrage accru. Ce service aide à soulager ces problèmes, améliorant la délivrance globale des messages, permettant aux marques d'envoyer des messages à l'échelle, y compris les liens et les appels à l'action, et aider à protéger davantage les consommateurs des messages indésirables.

Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer aux clients américains doivent enregistrer leurs codes longs pour 10DLC. Pour en savoir plus sur les spécificités de 10DLC et pourquoi il est nécessaire, visitez notre [article 10DLC dédié]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).

## Réinitialisation de l'authentification à deux facteurs

Les utilisateurs rencontrant des problèmes de connexion via l'authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Visitez notre [documentation]({{site.baseurl}}/user_guide/administrative/company_settings/security_settings/#user-authetication-reset) pour en savoir plus.

## Nouveaux partenariats Braze

### Hightouch - Automatisation du flux de travail

L'intégration de Braze et de [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) vous permet de construire de meilleures campagnes sur Braze avec des données clients actualisées à partir de votre entrepôt de données. Vous souhaitez fournir des interactions pertinentes et opportunes à vos clients, et le faire repose fortement sur les données dans votre compte Braze pour être précis et frais. En synchronisant automatiquement les données clients de votre entrepôt de données dans Braze, vous n'avez plus besoin de vous soucier de la cohérence des données, et vous pouvez vous concentrer sur la construction d'expériences de classe mondiale.

### Transcend - Confidentialité des données & Conformité

Le partenariat Braze et [Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/) aide les utilisateurs à automatiser les demandes de confidentialité en orchestrant les données sur des dizaines de systèmes de données. En fin de compte, cela aide les équipes à se conformer à la réglementation comme le RGPD et l’ACCP et place les personnes sur le siège du conducteur en ce qui concerne leurs données.

### Tinyindices - Importation de cohortes

[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/) est une fonctionnalité de création d'audience qui offre la capacité d'augmenter le nombre de campagnes et de revenus sans nuire à l'expérience du client. et analytiques pour suivre les performances des campagnes CRM en ligne et hors ligne. Ensemble, l’intégration de Braze et Tinyclues offre aux utilisateurs une voie vers une meilleure planification et une meilleure stratégie de CRM permettant aux utilisateurs d'envoyer plus de campagnes de ciblage, de trouver de nouvelles opportunités de produits et d'augmenter leurs revenus à l'aide d'une interface utilisateur incroyablement conviviale.

### optilyz - Mail direct

[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/) est une plate-forme d'automatisation de messagerie directe qui vous permet d'exécuter des campagnes de messagerie directe plus axées sur le client, durables et rentables. optilyz est utilisé par des centaines d'entreprises à travers l'Europe et vous permet d'intégrer des lettres, des cartes postales et les auto-mailers dans vos campagnes de marketing inter-canaux et automatiser et mieux personnaliser vos campagnes. Utilisez l'intégration optilyz et Braze webhook pour envoyer du courrier direct à vos clients.