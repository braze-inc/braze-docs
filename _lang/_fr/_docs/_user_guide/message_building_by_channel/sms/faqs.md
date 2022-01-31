---
nav_title: Foire aux questions
article_title: FAQ SMS
page_order: 8
description: "Cet article répond à certaines des questions les plus fréquemment posées lors de la mise en place de campagnes de SMS."
page_type: Foire Aux Questions
channel:
  - SMS
---

# FAQ SMS

> Sur cette page, nous allons essayer de répondre à vos questions les plus strictes sur les SMS!

### Pouvez-vous inclure des liens dans un SMS?

Vous pouvez inclure n'importe quel lien dans n'importe quelle campagne SMS que vous souhaitez. Toutefois, il y a quelques préoccupations à considérer:

- Les liens peuvent prendre une grande partie de la limite de 160 caractères pour les SMS. Si vous incluez un lien et un texte, cela peut entraîner deux messages SMS au lieu d'un seul.
- Les entreprises utilisent souvent des raccourcis de liens pour limiter l'impact du nombre de caractères d'un lien. Cependant, si vous envoyez un lien raccourci via un code long, les transporteurs peuvent bloquer ou refuser le message, car ils peuvent se méfier de la redirection du lien.
- Utiliser un [code court]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) serait le type de numéro le plus fiable pour inclure des liens.

### Quels sont les cas d'utilisation de SMS que Braze ne prend pas en charge ?

Il y a trois cas d'utilisation de SMS courants que Braze ne prend actuellement pas en charge :
- Autorisation à deux facteurs
- Bots de chat
- Appels téléphoniques

### Les messages de test sont-ils comptés dans les limites ?

Oui, ils le font. Veuillez garder cela à l'esprit lors du test des messages.

### Un utilisateur doit-il faire partie d'un groupe d'abonnement par SMS pour recevoir des messages de test SMS ?

Non. Cependant, les messages de test SMS ne peuvent être envoyés qu'à des numéros de téléphone valides dans la base de données.

### Vous avez besoin de limiter la vitesse d'envoi des SMS?

La vitesse par défaut de la concurrence et du débit permettent environ 360 000 messages par heure par code court. Le débit supplémentaire nécessite des codes courts supplémentaires.

### Comment puis-je éviter les excédentaires?

Bien que nous ne puissions pas vous promettre que vous n'aurez pas occasionnellement un surage, vous pouvez suivre ces précautions pour réduire les chances de dépasser vos limites allouées :

- Faites attention au nombre de caractères de votre SMS. Envoi involontaire de plus d'un segment pourrait provoquer des dépassements. Plus de détails [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calculez soigneusement vos caractères SMS pour tenir compte de Liquid ou du contenu connecté. Le compositeur de SMS Braze dans votre tableau de bord n'estime pas l'utilisation de l'une ou l'autre de ces fonctionnalités.
- Considérez le type d'encodage que votre message utilise - si votre message utilise l'encodage GSM-7, vous pouvez généralement estimer que vous pouvez envoyer un message avec 128 caractères par segment de message. Si votre message utilise l'encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) , vous pouvez généralement estimer que vous pouvez envoyer un message de 67 caractères par segment de message.
- Tester, tester et tester ! Testez toujours vos messages SMS avant le lancement, en particulier lorsque vous utilisez Liquid et le contenu connecté.

### Quelles sont les meilleures pratiques d'envoi pour éviter la détection de spam pour les SMS?

1. Assurez-vous que les instructions opt-in et opt-out sont claires.
2. Assurez-vous que vous (la marque) avez une relation avec le client.
3. Assurez-vous que le contenu est pertinent pour la relation et ce que l'utilisateur a choisi de recevoir.

Pour plus de directives sur la prévention du spam détection, consultez [les lois SMS et les directives de régulation](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

### Comment créer une logique pour les opt-ins sélectifs pour les SMS afin que les utilisateurs soient dans le bon groupe d'abonnement ?

Les mots-clés personnalisés seraient écrits en tant qu'événements personnalisés, vous souhaiteriez donc créer des segments en fonction des mots-clés dans lesquels les clients peuvent écrire. Par exemple, si un utilisateur opte pour les SMS pour les messages VIP, mais pas les alertes, vous pouvez créer un segment VIP et un segment d'alerte, puis assigner l'utilisateur au segment approprié.

### Combien de caractères un émoji utilise-t-il ?

Les émojis peuvent être délicats, car il n'y a pas de nombre de personnages standard sur tous les émojis. Il y a le risque que les émoticônes dépassent la limite de caractères et fractionnent le SMS en plusieurs messages, malgré qu'il se montre comme un message dans le compositeur de Braze. Quand QA vos messages, vous pouvez mieux vérifier si un message sera divisé en utilisant [cet outil]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Si un utilisateur écrit "Stop" à notre code court, se désabonne-t-il du groupe d'abonnement ?

À quoi cela ressemble-t-il sur le profil de l'utilisateur ? Le groupe d'abonnement retournera à 2 tirets (-), et il y aura des événements personnalisés pour s'abonner et se désabonner.

### Y a-t-il un moyen de voir si un alias existe sur un profil utilisateur ?

Les alias ne sont pas visibles sur le profil de l'utilisateur. Vous devrez utiliser les points de terminaison [Exporter les données utilisateur]({{site.baseurl}}/api/endpoints/export/) pour confirmer que des alias sont définis.

### Quels sont les codes courts partagés ?

Avec un code court partagé, tous les messages textuels, quelle que soit l'entreprise ou l'organisation qui les envoie, arriver sur un appareil mobile d'un consommateur à partir du même numéro de téléphone à 5-6 chiffres. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise n'aura pas de code court dédié.

Parmi les inconvénients de cette approche, citons :

- Si vos clients se désintègrent des messages d'une autre entreprise qui ont un code court partagé avec vous, ils auront également choisi de ne plus recevoir vos messages.
- Si une entreprise viole les règles, tous les messages de l'entreprise sont suspendus.
- Problèmes de sécurité

### Comment pouvez-vous mettre en liste blanche les URLs pour les SMS?

Avant d'envoyer des messages SMS contenant des URLs aux utilisateurs de certains pays (par exemple, La Suède ou les pays nordiques), vous devez obtenir ces URLs enregistrées auprès du transporteur. Contactez votre responsable du service à la clientèle Braze pour vous aider. Ce processus prendra environ cinq jours.

### Que se passe-t-il si plusieurs utilisateurs ont le même numéro de téléphone ?

Lorsque plusieurs profils d'utilisateurs qui partagent un numéro de téléphone (activé pour SMS) sont éligibles pour une campagne ou Canvas pas en même temps, déclenché par l'événement d'un SMS entrant, Braze va déduper les utilisateurs au niveau de l'étape Canvas . Cela permettra de s'assurer que les utilisateurs ne reçoivent pas plus d'un SMS pour une étape de Canvas même si plusieurs utilisateurs partagent le même numéro de téléphone.

Braze utilisera le flux suivant pour déterminer le profil du destinataire :
- Vérifiez quel profil a reçu le SMS le plus récemment (il y a jusqu'à 7 jours); si on existe, envoyez-le à cet utilisateur.
- Si aucun des deux n'a reçu de SMS il y a 7 jours, envoyer à l'utilisateur qui a un alias d'utilisateur de "téléphone" qui correspond au numéro de téléphone.
- Si aucun des deux n'existe, envoyer à un profil aléatoire entre ceux disponibles.

Si vous recevez un mot clé "START" ou "STOP" du numéro de téléphone partagé, tous les profils des utilisateurs seront abonnés et activés pour les SMS ou se désabonner.

{% alert important %}
Si vous étourdissez vos utilisateurs dans une toile et que vous avez des horaires différents pour chaque étape de Canvas vous pouvez envoyer un utilisateur avec le même e-mail ou téléphone en double messages.
{% endalert %}

### Les propriétés de l'évènement SMS captureront-elles des mots-clés dans une phrase ?

Pour qu'un mot clé soit reconnu dans une phrase, (p. ex. "s'il vous plaît arrêter de m'envoyer un texte"), vous devrez utiliser une instruction Liquid dans le message pour reconnaître le mot spécifique. Les propriétés d'événement ont une limite de caractères de 256 ; sinon, il n'y a pas de limite de caractères.

### Pourquoi le tableau de bord Braze m'avertira-t-il que je pourrais être facturé pour des segments de messages supplémentaires lorsque mon message est de moins de 160 caractères (GCM-7) ou 70 caractères (UCS-2) ?

Vous pourriez être facturé des segments de messages supplémentaires si la personnalisation de Liquid est incluse dans votre message. Le modèle de bloc de contenu ne se produit pas jusqu'à ce que le message se prépare à être envoyé. Lorsque vous éditez un SMS avec un bloc de contenu, Braze ne sait pas ce que le bloc de contenu contiendra mais fournit une estimation approximative. Nous recommandons aux utilisateurs d'utiliser le volet de test pour prévisualiser le message afin de mieux comprendre ce à quoi s'attendre.

### Qu'est-ce qu'un `app_id` dans l'objet API SMS ?

L'identifiant de l'application clé API ou `app_id` est un paramètre associant une activité à une application spécifique dans votre groupe d'applications. Il désigne l'application avec laquelle vous interagissez dans le groupe d'applications. Par exemple, vous trouverez que vous aurez un `app_id` pour votre application iOS, un `app_id` pour votre application android et un `app_id` pour votre intégration web.

Votre `app_id` peut être trouvé sur le tableau de bord en naviguant sur **Console développeur -> Paramètres API -> Identification**.

### Comment serai-je facturé pour les SMS ?

En plus des frais pour les codes courts et longs, la facturation se fait par le nombre de segments de messages envoyés par pays. Pour en savoir plus sur la façon dont les segments de messages sont calculés, consultez notre guide [Segments de messages et Copier les limites]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Pour les excédents, votre gestionnaire de compte vous contactera pour vous informer si vous êtes près d'atteindre votre maximum, fournir des rapports pertinents pour vous aider à vous informer. Pour de plus amples questions concernant les excédents, veuillez contacter votre représentant de Braze.

### Si un message est envoyé à une ligne fixe, le message compte-t-il toujours pour mon nombre d'envoi de SMS ?

Aux États-Unis, au Canada et au Royaume-Uni :
- Si un SMS est envoyé à une ligne fixe, il sera marqué comme **non distribué**. Notez que Twilio facturera quand même la tentative de livraison, donc les messages marqués comme **Envoyés**, **Livré**, ou **Non délivré** dans vos journaux de messages seront facturés.
- Au Royaume-Uni, certains opérateurs convertiront le SMS en messagerie vocale, diffusant le message.

Dans d'autres pays:
- Twilio lancera une erreur et vous ne serez pas facturé pour la tentative de message SMS. 
