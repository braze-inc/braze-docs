---
nav_title: août
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version d’août 2021."
---

# Août 2021

## Google Audience Sync

L'intégration de Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) permet aux marques d'étendre la portée de leurs parcours clients cross-canal à Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant vos données client propriétaires, vous pouvez livrer des publicités en toute sécurité en fonction de déclencheurs comportementaux dynamiques, de segmentations et bien plus encore. Tous les critères que vous utilisez habituellement pour déclencher un message (par exemple, push, e-mail, SMS, etc.) dans le cadre d'un Braze Canvas peuvent être utilisés pour déclencher un message publicitaire à l'intention de cet utilisateur via le service Customer Match de Google.

## Guide sur les meilleures pratiques d’intégration du SDK iOS

Ce guide facultatif sur [l'intégration du SDK iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk) vous accompagne pas à pas dans la configuration des meilleures pratiques lors de la première intégration du SDK iOS et de ses composants de base dans votre application. Ce guide vous aidera à créer un fichier d’aide `BrazeManager.swift` qui dédoublera toutes les dépendances sur le SDK Braze pour iOS du reste de votre code de production, ce qui entraînera une `import AppboyUI` dans toute votre application. Cette approche limite les problèmes liés aux importations excessives de SDK, ce qui facilite le suivi, le débogage et la modification du code. 

## Achats prédictifs

Les achats prédictifs fournissent aux spécialistes du marketing un outil puissant pour identifier et communiquer avec les utilisateurs en fonction de leur probabilité de réaliser un achat.  Lorsque vous créez une prédiction d'achat, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par le gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre des activités d'achat précédentes et prédire les activités d'achat futures. Consultez notre documentation sur les [prédictions d'achat]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) pour en savoir plus. 

## Éditeur par glisser-déposer

Avec Braze Email, vous pouvez créer des messages e-mail entièrement personnalisés dans des campagnes ou des canevas en utilisant notre nouvelle [expérience de communication par glisser-déposer.]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/) Les utilisateurs peuvent désormais faire glisser des Blocs éditeurs dans leurs e-mails, ce qui offre une personnalisation plus intuitive. 

## Importation d’alias utilisateur

Pour cibler les utilisateurs qui n'ont pas de `external_id`, vous pouvez [importer une liste d'utilisateurs ayant un aliasing de l'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). Un alias sert d’identifiant utilisateur unique alternatif. Cela peut être utile si vous essayez de vendre à des utilisateurs anonymes qui ne sont pas abonnés ou n’ont pas créé de compte sur votre application. 

## Guide de mise à niveau iOS 15

Ce [guide de mise à niveau iOS 15]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) présente les changements introduits dans iOS 15 (WWDC21) et les étapes de mise à niveau requises pour votre intégration SDK iOS de Braze.

## Guide de mise à niveau Android 12

Ce [guide de mise à niveau Android 12]({{site.baseurl}}/developer_guide/platforms/android/android_13/) décrit les modifications pertinentes introduites dans Android 12 (2021) et les étapes de mise à niveau requises pour votre intégration SDK Android de Braze.

## A2P 10DLC

A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d’envoyer des communications de type Application à personne (A2P) via un numéro de téléphone standard à 10 chiffres en code long (10DLC). Les codes longs à 10 chiffres sont traditionnellement conçus pour le trafic de personne à personne (P2P), ce qui limite le débit des entreprises et renforce le filtrage. Ce service aide à atténuer ces problèmes, améliorant la livrabilité globale des messages, en permettant aux marques d’envoyer des messages à grande échelle, y compris des liens et appels à l’action, et en protégeant les consommateurs contre les messages indésirables. 

Tous les clients qui ont actuellement et/ou utilisent des codes longs américains pour envoyer à des clients américains doivent enregistrer leurs codes longs pour 10DLC. Pour en savoir plus sur les spécificités du 10DLC et les raisons pour lesquelles il est nécessaire, consultez notre article dédié au [10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Réinitialisation de l’authentification à deux facteurs

Les utilisateurs qui rencontrent des problèmes pour se connecter via l'authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour [réinitialiser leur authentification à deux facteurs]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## Nouveaux partenariats Braze

### Hightouch - Automatisation du flux de travail

L'intégration de Braze et [Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) vous permet de créer de meilleures campagnes sur Braze avec des données clients actualisées provenant de votre entrepôt de données. Vous voulez fournir des interactions pertinentes et opportunes à vos clients, et cela dépend fortement de l’exactitude et de la « fraîcheur » des données de votre compte Braze. En synchronisant automatiquement les données client de votre entrepôt de données dans Braze, vous n’aurez plus à vous soucier de la cohérence des données et vous gagnerez un temps précieux pour créer des expériences client de premier plan.

### Transcend - Confidentialité des données et conformité 

Le partenariat entre Braze et [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/) aide les utilisateurs à automatiser les demandes de confidentialité en orchestrant les données à travers des dizaines de systèmes de données. Au final, cela aide les équipes à se conformer aux réglementations telles que le RGPD et le CCPA et cela permet aux utilisateurs d’avoir le contrôle sur leurs données.

### Tinyclues - Importation de cohortes

[Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/) est une fonctionnalité de création d'audience qui offre la possibilité d'augmenter le nombre de campagnes et le chiffre d'affaires sans nuire à l'expérience client, ainsi que des analyses permettant de suivre les performances des campagnes CRM en ligne et hors ligne. L’intégration entre Braze et Tinyclues permet aux utilisateurs d’améliorer leur stratégie CRM et la planification des campagnes CRM pour envoyer davantage de campagnes ciblées, trouver de nouvelles opportunités de produits et augmenter leurs revenus via une interface utilisateur incroyablement conviviale.

### optilyz - Publipostage

[Optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/) est une plateforme d'automatisation du publipostage qui vous permet de mener des campagnes de publipostage plus axées sur le client, plus durables et plus rentables. Optilyz est utilisé par des centaines d'entreprises à travers l'Europe et vous permet d'intégrer des lettres, des cartes postales et des self-mailers dans votre marketing cross-canal ainsi que d'automatiser et de mieux personnaliser les campagnes. Utilisez l’intégration entre le webhook d’optilyz et Braze pour envoyer des publipostages à vos clients. 