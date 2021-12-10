---
nav_title: Septembre
page_order: 4
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour septembre 2021."
---

# Septembre 2021

## Synchronisation Google Audience

L'intégration de Braze [Synchronisation de l'audience vers Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) permet aux marques d'étendre la portée de leurs trajets clients inter-canaux à Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant les données de vos clients de première partie, vous pouvez livrer des publicités en toute sécurité en fonction des déclencheurs de comportement, de la segmentation et plus encore. Tous les critères que vous utilisez généralement pour déclencher un message (par exemple, push, email, SMS, etc.). dans le cadre d'un Braze Canvas peut être utilisé pour déclencher une publicité pour cet utilisateur via Google Customer Match.

## Guide d'intégration des meilleures pratiques pour iOS SDK

Ce guide SDK facultatif d'intégration [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/ios_sdk_integration/) vous emmène étape par étape dans la mise en place des meilleures pratiques lors de l'intégration du SDK iOS et de ses composants principaux dans votre application. Ce guide vous aidera à construire un `Gestionnaire de Brase. wift` fichier d'aide qui découplera toutes les dépendances du Braze iOS SDK du reste de votre code de production. ce qui a entraîné une `importation AppboyUI` dans toute votre application. Cette approche limite les problèmes liés aux importations excessives de SDK, facilitant le suivi, le débogage et le changement de code.

## Achats prédictifs

Les achats prédictifs offrent aux marketeurs un outil puissant pour identifier et envoyer des messages en fonction de leur probabilité de faire un achat. Lorsque vous créez une prévision d'achat, Braze forme un modèle d'apprentissage automatique à l'aide de [arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité d'achat précédente et prédire l'activité d'achat future. Visitez notre documentation [Achats prédicitvés]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/) pour en savoir plus.

## Editeur Glisser & Déposer

Avec Braze Email, vous pouvez créer des messages électroniques personnalisés et personnalisés dans les campagnes ou Canvas en utilisant notre nouvelle expérience d'édition par glisser & Déposer. Les utilisateurs peuvent maintenant faire glisser des blocs d'éditeur dans leurs e-mails, permettant une personnalisation plus intuitive. Pour savoir comment commencer avec l'éditeur Drag & Drop, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/).

## Import des alias de l'utilisateur

Pour cibler les utilisateurs qui n'ont pas d' `external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateur. Un alias sert d'identifiant d'utilisateur unique alternatif. Cela peut être utile si vous essayez de commercialiser des utilisateurs anonymes qui n'ont pas créé de compte avec votre application. Visitez notre [documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) pour en savoir plus.

## Guide de mise à jour iOS 15

Ce [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) décrit les changements introduits dans iOS 15 (WWDC21) et les étapes nécessaires à la mise à jour de votre intégration dans Braze iOS SDK.

## Guide de mise à jour d'Android 12

Ce [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) décrit les changements pertinents introduits dans Android 12 (2021) et les étapes de mise à jour requises pour votre intégration à Braze Android SDK.

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