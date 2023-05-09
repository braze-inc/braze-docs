---
nav_title: Septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2021."
---

# Septembre 2021

## Google Audience Sync

L’intégration entre Braze et [Audience Sync to Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) permet aux marques d’étendre la portée de leurs parcours client multicanal sur Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant vos données client propriétaires, vous pouvez livrer des publicités en toute sécurité en fonction de déclencheurs comportementaux dynamiques, de segmentations et bien plus encore. Les critères que vous utilisez généralement pour déclencher un message (par ex., notification push, e-mail, SMS, etc.) dans le cadre d’un Canvas Braze peuvent être utilisés pour envoyer une publicité à cet utilisateur via la fonction Customer Match (Correspondance client) de Google.

## Guide sur les meilleures pratiques d’intégration du SDK iOS

Ce [Guide d’intégration du SDK iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/ios_sdk_integration/) vous guide étape par étape sur les meilleures pratiques de configuration lors de la première intégration du SDK iOS, et de ses principaux composants, dans votre application. Ce guide vous aidera à créer un fichier d’aide `BrazeManager.swift` qui dédoublera toutes les dépendances sur le SDK Braze pour iOS du reste de votre code de production, ce qui entraînera une `import AppboyUI` dans toute votre application. Cette approche limite les problèmes liés aux importations excessives de SDK, ce qui facilite le suivi, le débogage et la modification du code. 

## Achats prédictifs

Les achats prédictifs donnent aux marketeurs un outil puissant pour identifier et communiquer avec les utilisateurs en fonction de leur probabilité de réaliser un achat.  Lorsque vous créez une prédiction d’achat, Braze entraîne un modèle de machine learning en utilisant des [arbres de décision à gradient renforcé](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l’activité d’achat précédente et prévoir la future. Consultez notre documentation sur les [achats prédictifs]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/) pour en savoir plus. 

## Éditeur Drag & Drop

Avec Braze Email, vous pouvez créer des e-mails personnalisés entièrement sur mesure dans vos campagnes ou Canvas en utilisant notre nouvelle [Expérience de modification en Drag & Drop]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/). Les utilisateurs peuvent désormais faire glisser des Blocs éditeurs dans leurs e-mails, ce qui offre une personnalisation plus intuitive. 

## Importation d’alias utilisateur

Pour cibler les utilisateurs qui n’ont pas de `external_id`, vous pouvez [importer une liste d’utilisateurs avec des alias utilisateurs.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) Un alias sert d’identifiant utilisateur unique alternatif. Cela peut être utile si vous essayez de vendre à des utilisateurs anonymes qui ne sont pas abonnés ou n’ont pas créé de compte sur votre application. 

## Guide de mise à niveau iOS 15

Ce [Guide de mise à niveau iOS 15]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) décrit les modifications introduites dans iOS 15 (WWDC21) et les étapes de mise à niveau requises pour votre intégration du SDK Braze pour iOS.

## Guide de mise à niveau Android 12

Ce [Guide de mise à niveau Android 12]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) décrit les modifications pertinentes introduites dans Android 12 (2021) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

## A2P 10DLC

L’A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d’envoyer des messages de type d’application à personne (A2P) via un numéro de téléphone standard à 10 chiffres long (10DLC). Les codes à 10 chiffres ont traditionnellement été conçus pour le trafic de personne à personne (P2P), ce qui limitait les entreprises à cause du débit limité et du filtrage accru. Ce service aide à atténuer ces problèmes, améliorant la délivrabilité globale des messages, en permettant aux marques d’envoyer des messages à grande échelle, y compris des liens et appels à l’action, et en protégeant les consommateurs contre les messages indésirables. 

Tous les clients qui ont actuellement et/ou utilisent des codes longs américains pour envoyer à des clients américains doivent enregistrer leurs codes longs pour 10DLC. Pour en savoir plus sur les spécificités du 10DLC et pourquoi il est nécessaire, consultez notre [Article 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).

## Réinitialisation de l’authentification à deux facteurs

Les utilisateurs qui rencontrent des problèmes se connectant via une authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour [réinitialiser leur authentification à deux facteurs]({{site.baseurl}}/user_guide/administrative/company_settings/security_settings/#user-authetication-reset).

## Nouveaux partenariats Braze

### Hightouch - Automatisation du flux de travail

L’intégration entre Braze et [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) vous permet de créer de meilleures campagnes Braze en utilisant les données client actualisées de votre entrepôt de données. Vous voulez fournir des interactions pertinentes et opportunes à vos clients, et cela dépend fortement de l’exactitude et de la « fraîcheur » des données de votre compte Braze. En synchronisant automatiquement les données client de votre entrepôt de données dans Braze, vous n’aurez plus à vous soucier de la cohérence des données et vous gagnerez un temps précieux pour créer des expériences client de premier plan.

### Transcend - Confidentialité des données et conformité 

Le partenariat entre Braze et [Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/) permet aux utilisateurs d’automatiser les demandes de confidentialité en orchestrant les données issues de dizaines de systèmes de données. Au final, cela aide les équipes à se conformer aux réglementations telles que le RGPD et le CCPA et cela permet aux utilisateurs d’avoir le contrôle sur leurs données.

### Tinyclues - Importation de cohortes

[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/) est une fonction de développement d’audiences qui vous permet de lancer davantage de campagnes et d’augmenter vos revenus sans nuire à l’expérience client, et qui offre également des analyses pour suivre le rendement de vos campagnes CRM en ligne et hors ligne. L’intégration entre Braze et Tinyclues permet aux utilisateurs d’améliorer leur stratégie CRM et la planification des campagnes CRM pour envoyer davantage de campagnes ciblées, trouver de nouvelles opportunités de produits et augmenter leurs revenus via une interface utilisateur incroyablement conviviale.

### optilyz - Publipostage

[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/) est une plateforme d’automatisation de publipostage qui vous permet d’exécuter des campagnes axées sur le client, durables et rentables. Optilyz est utilisé par des centaines d’entreprises en Europe et vous permet d’intégrer des lettres, des cartes postales et des auto-mails à votre marketing multicanal, pour automatiser et mieux personnaliser vos campagnes. Utilisez l’intégration entre le webhook d’optilyz et Braze pour envoyer des publipostages à vos clients. 