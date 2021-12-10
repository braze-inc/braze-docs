---
nav_title: Septembre
page_order: 4
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour septembre 2020."
---

# Septembre

## Rapports de l'entonnoir

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les voyages que vos clients prennent après avoir reçu une [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) ou [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports).

## Guide de mise à jour iOS 14

Conformément aux changements annoncés dans le nouvel iOS 14 d’Apple, il y a quelques changements et éléments d’action liés au Brésil requis pour les intégrations de Braze iOS SDK. Pour plus d'informations, jetez un coup d'oeil à [ce guide de mise à jour]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/).

## Modifications apportées à IDFA et IDFV pour iOS 14

Dans iOS 14, les utilisateurs doivent décider s'ils veulent opter pour le suivi des publicités et permettre aux applications et aux réseaux de publicités de lire leur IDFA lorsqu'ils visitent une application. Par conséquent, la stratégie de Braze consiste à utiliser plutôt l’« identifiant pour les fournisseurs » (c'est-à-dire IDFV) afin que vous puissiez continuer à suivre les utilisateurs sur différents appareils. Pour plus d'informations, jetez un œil à [cette section dans le guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa).

## Validation de l'adresse e-mail

Ce nouveau processus de validation de la syntaxe par courriel est une mise à jour vers celle existante de Braze. Il s'agit d'une vérification pour vérifier que les e-mails mis à jour ou importés dans Braze sont corrects. Pour plus d'informations, jetez un coup d'oeil à [ces directives et notes]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation).

## Événement utilisateur aléatoire dans les courants

Le numéro de segment aléatoire (i.e. RBN) se produit chaque fois qu'un nouvel utilisateur est créé dans son groupe d'applications. Pendant cet événement, chaque nouvel utilisateur reçoit un numéro de segment aléatoire que vous pouvez utiliser pour créer des segments uniformément répartis entre des utilisateurs aléatoires. Utilisez ceci pour regrouper une gamme de valeurs aléatoires de numéros de bucket et comparer les performances entre vos campagnes et les variantes de campagne. Pour voir si cet événement est disponible pour vous, jetez un coup d'oeil au [glossaire des événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/).

## Composants de la toile - Bientôt disponible!

Braze a ajouté quatre nouveaux composants Canvas pour accroître la souplesse et la fonctionnalité de vos Canvases. Ces nouveaux composants incluent : [Étape de séparation de la décision]({{site.baseurl}}/decision_split/), [Étape de délai]({{site.baseurl}}/delay_step/), [Étapes de Messagerie]({{site.baseurl}}/message_step/), et [Synchronisation de l'audience sur Facebook]({{site.baseurl}}/audience_sync_facebook/).
- __Séparation de la décision sur le canevas, Délai et les Étapes de Message__<br>Les séparations de décision peuvent être utilisées pour créer des branches de Canvas selon si un utilisateur correspond à une requête définie. Les étapes de délai vous permettent d'ajouter un délai autonome à votre Canvas sans avoir besoin d'un message correspondant. Les étapes de messagerie vous permettent d'ajouter un message autonome à l'endroit que vous voulez dans votre flux Canvas .
- __Synchronisation de l'audience sur Facebook__<br>Utiliser la synchronisation de l'audience Braze sur Facebook, les marques peuvent choisir d'ajouter les données de leurs propres utilisateurs à partir de leur propre intégration Braze à Facebook Custom Audiences pour livrer des publicités basées sur des déclencheurs de comportement, la segmentation, et plus encore. Tous les critères que vous utiliserez normalement pour déclencher un message (Push, Email, SMS, Webhook, etc) dans une toile Braze basée sur vos données utilisateur peut maintenant être utilisée pour déclencher une publicité pour cet utilisateur sur Facebook via des audiences personnalisées.

## Événements SMS reçus

Un nouvel événement d'engagement de messagerie a été ajouté aux courants. Cet événement se produit lorsqu'un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l'un de vos groupes d'abonnement SMS Braze. Pour plus d'informations, consultez notre [glossaire des événements de messagerie et d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).
