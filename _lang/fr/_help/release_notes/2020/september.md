---
nav_title: Septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2020."
---

# Septembre

## Rapports d’entonnoir

Le rapport d’entonnoir offre un rapport visuel qui vous permet d’analyser les parcours effectués par vos clients après la réception d’une [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) ou d’un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports).

## Guide de mise à niveau iOS 14

Conformément aux modifications annoncées dans la nouvelle version iOS 14 d’Apple, certains changements et éléments d’action liés à Braze sont requis pour les intégrations du SDK iOS de Braze. Pour plus d’informations, consultez ce [Guide de mise à niveau]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/).

## Modifications apportées à IDFA et IDFV pour iOS 14

Dans iOS 14, les utilisateurs doivent décider s’ils souhaitent s’abonner au suivi publicitaire et laisser les applications et les réseaux publicitaires lire leur IDFA quand ils sont sur une application. Par conséquent, la stratégie de Braze consiste à utiliser plutôt l’« identifiant pour les fournisseurs » (c.-à-d. IDFV) afin que vous puissiez continuer à suivre les utilisateurs sur différents appareils. Pour plus d’informations, consultez le [Guide de mise à niveau iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa).

## Validation de l’e-mail

Ce nouveau processus de validation de syntaxe d’e-mail est une mise à niveau du processus de Braze. C’est pour vérifier que les adresses e-mail mises à jour ou importées dans Braze sont correctes. Pour plus d’informations, consultez [ces directives et notes]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation).

## Événement utilisateur «compartiment aléatoire » dans Currents

Le numéro de compartiment aléatoire (c.-à-d. RBN) survient chaque fois qu’un nouvel utilisateur est créé au sein de son groupe d’apps. Au cours de cet événement, chaque nouvel utilisateur reçoit un numéro de compartiment aléatoire que vous pouvez ensuite utiliser pour créer des segments  d’utilisateurs aléatoires distribués uniformément Utilisez cette option pour regrouper une série de valeurs de numéro de compartiment aléatoire et comparer les performances à travers vos campagnes et variantes de campagne. Pour voir si cet événement est disponible, consultez le glossaire [des événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) Currents.

## Composants Canvas - Prochainement !

Braze a ajouté quatre nouveaux composants Canvas pour améliorer la flexibilité et la fonctionnalité de vos Canvas. Ces nouveaux composants comprennent : [Étape de fractionnement des décisions ]({{site.baseurl}}/decision_split/), [Étape de délai]({{site.baseurl}}/delay_step/), [Étapes de message]({{site.baseurl}}/message_step/) et [Synchronisation du public avec Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Décision de séparation Canvas, délai et étapes d’envoi de messages**<br>Les décisions de séparation peuvent être utilisées pour créer des branches Canvas selon qu’un utilisateur corresponde à une requête définie. Les étapes de délai vous permettent d’ajouter un délai distinct à votre Canvas sans avoir besoin d’un message correspondant. Les étapes de message vous permettent d’ajouter un message indépendant où vous voulez dans votre flux Canvas.
- **Synchronisation de l’audience vers Facebook**<br>En utilisant la synchronisation de l’audience Braze vers Facebook, les marques peuvent choisir d’ajouter les données de leurs propres utilisateurs à partir de leur intégration Braze aux audiences personnalisées de Facebook Custom afin de proposer des publicités basées sur des déclencheurs comportementaux, des segmentations, etc. Les critères que vous utilisez généralement pour déclencher un message (notification push, e-mail, SMS, Webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent maintenant être utilisés pour déclencher une publicité pour cet utilisateur dans Facebook via Custom Audiences (Audiences personnalisées).

## Événements de réception de SMS entrant

Un nouvel événement d’engagement de messagerie a été ajouté à Currents. Cet événement se produit lorsque l’un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l’un de vos groupes d’abonnement SMS Braze. Pour plus d’informations, consultez notre glossaire[ des événements de messages et d’engagement Currents ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).
