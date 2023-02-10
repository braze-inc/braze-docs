---
nav_title: FAQ
article_title: FAQ sur les SMS
page_order: 8
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la configuration des campagnes par SMS."
page_type: FAQ
channel:
  - SMS
  
---

# FAQ sur les SMS

> Sur cette page, nous allons essayer de répondre à vos questions les plus exigeantes concernant les SMS.

### Pouvez-vous inclure des liens dans un SMS ?

Vous pouvez inclure un lien dans les campagnes par SMS. Prenez cependant ces points en compte :

- Les liens peuvent rapidement augmenter le nombre de caractères et atteindre la limite de 160 caractères des SMS. Si vous incluez un lien et du texte, deux SMS peuvent être générés au lieu d’un.
- Les entreprises utilisent souvent des raccourcissements de liens pour limiter l’impact sur le nombre de caractères. En cas d’envoi d’un lien raccourci par un code long, les opérateurs peuvent bloquer ou refuser le message, se méfiant de la redirection du lien.
- Un [code court]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) est donc le type le plus fiable pour y inclure les liens.

Braze dispose également de sa propre fonctionnalité de raccourcissement des liens qui les réduira et fournira automatiquement des analytiques de clics. Consultez la section [Raccourcissement des liens]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) pour plus d’informations.

### Quels sont les cas d’utilisation de SMS que Braze ne prend pas en charge ?

Il existe trois cas d’utilisation courants des SMS que Braze ne prend actuellement pas en charge :
- Autorisation à deux facteurs
- Chatbots
- Appels téléphoniques

### Les messages texte de test sont-ils pris en compte pour les limites ?

Oui. Gardez cela à l’esprit lorsque vous testez des messages.

### Un utilisateur doit-il faire partie d’un groupe d’abonnement de SMS pour recevoir des messages test SMS ?

Non. Cependant, les messages test SMS ne peuvent être envoyés qu’à des numéros de téléphone valides dans la base de données.

### Devez-vous limiter le débit d’envoi des SMS ?

Le débit et le rendement simultanés par défaut permettent environ 360 000 messages par heure par code court. Un débit supplémentaire requiert d’autres codes courts.

### Comment éviter les dépassements ?

Nous ne pouvons pas promettre que vous n’aurez pas de dépassement, mais vous pouvez suivre ces précautions pour réduire les risques de dépassement des limites définies :

- Faites attention au nombre de caractères dans votre SMS. L’envoi involontaire de plusieurs segments peut entraîner des dépassements. Pour plus de détails, consultez notre section [Répartition des segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calculez soigneusement les caractères de vos SMS pour tenir compte de Liquid ou du contenu connecté. L’éditeur de SMS de Braze dans votre tableau de bord n’évalue et ne considère pas l’utilisation de ces fonctionnalités.
- Pensez au type de codage que votre message utilise. Dans le cas d’un codage GSM-7, vous pouvez en général estimer que vous pouvez envoyer un message contenant 128 caractères par segment de message. Si votre message utilise le codage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), vous pouvez normalement envoyer un message contenant 67 caractères par segment de message.
- Testez encore et toujours ! Testez toujours vos messages SMS avant de réaliser un envoi, en particulier lors de l’utilisation de Liquid et de contenu connecté.

### Quelles sont les meilleures pratiques d’envoi pour éviter la détection des courriers indésirables pour les SMS ?

1. Assurez-vous que les instructions d’abonnement et de désabonnement sont claires.
2. Assurez-vous que vous (la marque) êtes en relation avec le client.
3. Assurez-vous que le contenu est pertinent pour cette relation, et qu’il correspond à ce que l’utilisateur a choisi de recevoir.

Pour plus d’informations sur le fonctionnement des systèmes de détection des courriers indésirables, consultez les [directives relatives aux lois et réglementations sur les SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

### Comment créez-vous une logique pour les abonnements sélectifs aux SMS afin que les utilisateurs figurent dans le bon groupe d’abonnement ?

Les mots-clés personnalisés sont écrits comme des événements personnalisés. Pensez à créer des segments basés sur des mots-clés dans lesquels les clients peuvent entrer du texte. Par exemple, si un utilisateur s’abonne aux SMS pour les messages VIP mais pas pour les alertes, vous pouvez créer un segment VIP et un segment d’alertes, puis affecter l’utilisateur au segment approprié.

### Combien de caractères utilise un émoji ?

Les émojis peuvent être complexes car ils ne partagent pas un nombre de caractères standard. L’émoji risque de dépasser la limite de caractères et diviser le SMS en plusieurs messages, même s’il s’affiche en un seul message dans l’éditeur de Braze. L’assurance qualité de vos messages vous permet de mieux vérifier s’ils seront divisés à l’aide de notre [calculatrice de segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Si un utilisateur envoie un SMS « Stop » à notre code court, est-il désabonné du groupe d’abonnement ?

Comment le profil utilisateur le l’illustre-t-il ? Le groupe d’abonnement récupère 2 tirets (--) et des événements personnalisés sont disponibles pour s’abonner et se désabonner.

### Est-il possible de voir s’il existe un alias dans un profil utilisateur ?

Les alias ne sont pas visibles dans le profil utilisateur. Vous devez utiliser les endpoints [Export User Data]({{site.baseurl}}/api/endpoints/export/) (Exporter les données utilisateur) pour confirmer les alias définis.

### Qu’est-ce qu’un code court partagé ?

Avec un code court partagé, tous les messages texte, quelle que soit l’identité de l’entreprise ou de l’organisation, parviennent à l’appareil mobile d’un consommateur avec le même numéro de téléphone à 5 à 6 chiffres. Les codes courts partagés étant relativement économiques et disponibles immédiatement, votre entreprise n’aura pas de code court dédié.

Voici quelques inconvénients de cette approche :

- Si vos clients ne s’abonnent pas aux messages d’une autre entreprise qui partagent un code court partagé, ils ne seront pas non plus abonnés à vos messages.
- Si une entreprise viole les règles, les messages de toutes les entreprises sont suspendus.
- Problèmes de sécurité

### Comment ajoutez-vous des URL à une liste blanche pour les SMS ?

Avant d’envoyer des SMS contenant des URL aux utilisateurs dans certains pays (comme la Suède ou les pays nordiques), vous devez faire enregistrer ces URL par l’opérateur. Adressez-vous à votre gestionnaire du service client de Braze pour obtenir de l’aide. Ce processus prend environ cinq jours.  

### Que se passe-t-il si plusieurs utilisateurs ont le même numéro de téléphone ?

Lorsque plusieurs profils utilisateur avec le même numéro de téléphone (SMS activés) sont éligibles à une campagne ou à un composant Canvas en même temps et déclenchés par un SMS entrant, Braze déduplique les utilisateurs au niveau du composant Canvas. Les utilisateurs ne reçoivent donc pas plus d’un SMS pour un composant Canvas, même si plusieurs utilisateurs partagent le même numéro de téléphone.

Braze utilisera le processus suivant pour déterminer le profil du destinataire :
- Vérifiez le profil ayant reçu des SMS récemment (jusqu’à 7 jours auparavant) et envoyez à cet utilisateur le cas échéant.
- Si aucun n’a reçu de SMS au cours de 7 derniers jours, envoyez à l’utilisateur avec pour alias d’utilisateur « téléphone » correspondant au numéro de téléphone.
- Si aucun n’existe, envoyez à un profil aléatoire parmi ceux disponibles. 

Si vous recevez un mot-clé « START » ou « STOP » provenant du numéro de téléphone partagé, tous les profils utilisateur seront abonnés aux SMS (qui deviennent alors activés), ou désabonnés le cas échéant. Ceci s’applique également aux changements d’état API. Par exemple, si plusieurs profils avec différents ID externes ont le même numéro de téléphone, un changement d’état du groupe d’abonnement via l’API mettra à jour tous les profils ayant ce numéro de téléphone, même si un seul ID externe est spécifié.

{% alert important %} 
Si vous échelonnez vos utilisateurs dans un Canvas et avez des heures de planification différentes pour chaque composant Canvas, vous pouvez envoyer à un utilisateur les mêmes messages par e-mail ou téléphone en double. 
{% endalert %}

### Les propriétés de l’événement SMS enregistrent-elles les mots-clés dans une phrase ?

Pour qu’un mot-clé soit reconnu dans une phrase (par exemple, « arrêtez de m’envoyer des SMS »), vous devez utiliser une instruction Liquid dans le message pour la reconnaissance du mot spécifique. Les propriétés de l’événement ont une limite de 256 caractères. Sinon, aucune limite n’est appliquée.

### Pourquoi le tableau de bord de Braze m’avertit que des segments de messages supplémentaires peuvent m’être facturés alors que mon message comporte moins de 160 (GCM-7) ou 70 (UCS-2) caractères ?

Vous pouvez recevoir des frais pour des segments de messages supplémentaires si une personnalisation Liquid est incluse dans votre message. La modélisation du bloc de contenu n’est pas effectuée tant que le message n’est pas prêt pour envoi. Lorsque vous modifiez un SMS avec un bloc de contenu, Braze ignore ce que ce bloc de contenu contiendra mais propose une estimation approximative. Nous recommandons aux utilisateurs d’utiliser le volet Test pour prévisualiser le message et mieux comprendre à quoi s’attendre.

### Qu’est-ce qu’un `app_id` dans l’objet API SMS ?

La clé API de l’identifiant d’application, ou `app_id`, est un paramètre associant une activité à une application spécifique dans votre groupe d’apps. Il désigne l’application dans le groupe d’apps que vous utilisez. Par exemple, vous pouvez voir un `app_id` pour votre application iOS, un `app_id` pour votre application Android, et un `app_id` pour votre intégration Web. 

Votre `app_id` se trouve dans le tableau de bord, dans **Developer Console (Console développeur) > API Settings (Paramètres API) > Identification**.

### Comment serai-je facturé pour les SMS ?

Outre les frais pour les codes courts et longs, la facturation est effectuée par le nombre de segments de messages envoyés par pays. Pour en savoir plus sur la manière dont les segments de messages sont calculés, consultez notre guide [Segments de message et limites de texte]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). 
Concernant les dépassements, votre gestionnaire de compte vous contactera pour vous informer si vous êtes proche de votre limite, avec des rapports pertinents pour illustrer la situation. Pour plus d’informations sur les dépassements, contactez votre conseiller Braze.

### Si un message est envoyé à un téléphone fixe, est-il toujours comptabilisé comme un envoi de SMS ?

Aux États-Unis, au Canada et au Royaume-Uni :
- Si un SMS est envoyé à un téléphone fixe, il est marqué comme **Non livré**. Notez que Twilio continuera à facturer les tentatives de livraison. Les messages marqués comme **Envoyé**, **Livré** ou **Non livré** dans vos registres de messages seront donc facturés.
- Au Royaume-Uni, certains opérateurs convertissent les SMS en messages vocaux et assurent ainsi leur livraison.

Dans d’autres pays :
- Twilio lance une erreur et vous n’êtes pas facturé pour le message SMS. 

### Si un utilisateur se désabonne et envoie un mot-clé à notre code court et long, reçoit-il la réponse que nous avons configurée pour ce mot-clé dans Braze ?

Si un utilisateur se désabonne et envoie un mot-clé de l’une des [catégories de mots-clés par défaut]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout), il reçoit la réponse pour ce mot-clé. Si un utilisateur se désabonne et envoie un [mot-clé personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling), il ne reçoit pas la réponse pour ce mot-clé. 
