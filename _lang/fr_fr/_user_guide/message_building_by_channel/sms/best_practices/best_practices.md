---
nav_title: "Meilleures pratiques en matière de SMS/MMS"
article_title: Meilleures pratiques en matière de SMS/MMS
page_order: 1
description: "Cet article de référence couvre les meilleures pratiques en matière de SMS/MMS."
page_type: reference
channel:
  - SMS
  
---

# Meilleures pratiques en matière de SMS/MMS

> Découvrez les bonnes pratiques pour les SMS/MMS avec Braze, y compris nos recommandations pour le contrôle des désabonnements et le pompage du trafic.

## Recommandations pour le contrôle des désabonnements

La loi exige de respecter les demandes des destinataires de ne pas recevoir de communications. Le non-respect des demandes des destinataires de ne pas recevoir de SMS peut entraîner des sanctions, y compris des amendes, et peut donner lieu à des poursuites judiciaires. Braze a mis en place des fonctionnalités permettant une gestion efficace des abonnements aux SMS/MMS, ainsi que des mécanismes permettant de s'assurer que les demandes sont correctement traitées.

En vertu des contrats d'abonnement qu'ils ont conclus avec nous, nos clients sont seuls responsables du respect de la législation applicable dans le cadre de leur utilisation de nos services. Par conséquent, nous recommandons vivement aux clients de veiller à configurer correctement leur dispositif de SMS, de tester ces dispositifs de manière approfondie, de prendre des mesures pour contrôler le respect de l'obligation de désabonnement et d'agir rapidement s'ils constatent des cas de non-respect des demandes de désabonnement.

Lorsque vous définissez les paramètres des SMS/MMS dans Braze pour gérer les abonnements et les désabonnements, reportez-vous à la liste de ressources suivante :
* [les groupes d'abonnement SMS :]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) Groupes d'abonnement et méthodes et statuts d'abonnement/de désabonnement.
* [API REST pour les groupes d’abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) : Comment traiter les abonnements et les désabonnements reçus d'une source autre qu'une réponse directe à un message.
* [Traitement des mots-clés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords): Explications sur la manière dont Braze aborde le traitement des mots-clés et leur gestion.
* [Double abonnement aux SMS :]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/) Oblige les utilisateurs à confirmer explicitement leur intention d'abonnement avant de pouvoir recevoir des messages SMS. Le double abonnement aux SMS est obligatoire dans certains pays, c'est pourquoi Braze recommande de le configurer.
* [Envoi de messages SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/sms_sending/) : Principes de base de l'envoi de SMS chez Braze, notamment l'importance des groupes d'abonnement, les exigences en matière de segments SMS et de corps de message, etc.

### Considérations

Lorsque des SMS/MMS ont été configurés dans plusieurs instances et qu'en raison d'une mauvaise configuration, des désabonnements à une campagne ou à Canvas sont envoyés au mauvais espace de travail.

* Braze a mis en place un système de contrôle pour identifier de telles instances. Si ce comportement est signalé, Braze renverra les désabonnements à l'instance correcte et compensera tous les désabonnements survenus au cours de la période.
* Nous recommandons vivement aux clients de tester les désabonnements pour chaque groupe d'abonnement dont ils disposent dans Braze. Il est préférable d'identifier ce problème avant de lancer un message plutôt que de l'atténuer après qu'il a été identifié.

Braze gère les abonnements SMS/MMS au niveau du profil utilisateur (`user_id`) et du numéro de téléphone (`channel_id`). Lorsqu'un numéro de téléphone fait l'objet d'un abonnement ou d'un retrait, la mise à jour s'applique à tous les profils qui partagent ce numéro. Dans le cas où un utilisateur final s'est abonné avec un certain numéro de téléphone, mais change ensuite de numéro de téléphone, le nouveau numéro de téléphone héritera du statut groupe d'abonnement de l'utilisateur. En conséquence, si un utilisateur final s'est désabonné, mais qu'il réintègre l'appli ou le site web avec un nouveau numéro de téléphone, il ne recevra pas de messages indésirables.

## Recommandations pour le pompage du trafic

### Qu'est-ce que le pompage de trafic ?

Le pompage de trafic est une forme de fraude qui se produit lorsqu'un acteur mal intentionné utilise un formulaire en ligne pour déclencher l'envoi de messages SMS à un volume élevé (par exemple des messages d'abonnement ou des mots de passe à usage unique). L'acteur malveillant crée un numéro de téléphone surtaxé pour l'envoi de ces messages et réclame à l'opérateur mobile auprès duquel le numéro surtaxé a été créé une part des recettes, générant ainsi des chiffres d'affaires illicites.

### Comment repérer le pompage du trafic

* Les numéros surtaxés qui permettent ce type d'escroquerie sont souvent, mais pas toujours, installés dans des pays qui ne font pas partie de votre zone d'envoi habituelle.
* Des pics inhabituels dans l'envoi de messages à partir de formulaires en ligne peuvent indiquer un pompage du trafic.
    * Nous vous recommandons de mettre en place des [alertes de campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) pour plafonner et notifier l'envoi d'un nombre invraisemblablement élevé de messages.
* Des formulaires en ligne incomplets peuvent indiquer un remplissage programmatique.
* Lorsque vous créez des formulaires en ligne, nous vous recommandons de définir des règles pour vous assurer que les formulaires sont entièrement remplis et d'utiliser des outils tels que le CAPTCHA pour minimiser les risques.

### Impact du pompage du trafic

Les clients sont responsables du contrôle du trafic qu'ils envoient et seront facturés pour tous les SMS envoyés par l'intermédiaire de leur compte. Entre Braze et le client, le client est la partie la mieux placée pour détecter et empêcher le pompage de trafic.

