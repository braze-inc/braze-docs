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

- Les liens peuvent prendre une grande partie de la limite de 160 caractères pour les SMS. Si vous incluez un lien et un texte, cela peut entraîner deux messages SMS, au lieu d'un seul.
- Les entreprises utilisent souvent des raccourcis de liens pour limiter l'impact du nombre de caractères d'un lien. Cependant, si vous envoyez un lien raccourci via un code long, les transporteurs peuvent bloquer ou refuser le message, car ils peuvent se méfier de la redirection du lien.
- Utiliser un [code court]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) serait le type de numéro le plus fiable pour inclure des liens.

### Les messages de test sont-ils comptés dans les limites ?

Oui, ils le font. Veuillez garder cela à l'esprit lors du test des messages.

### Vous avez besoin de limiter la vitesse d'envoi des SMS?

La vitesse par défaut de la concurrence et du débit permet environ 360 000 messages par heure par code court. Le débit supplémentaire nécessite des codes courts supplémentaires.

### Comment puis-je éviter les excédentaires?

Bien que nous ne puissions pas vous promettre que vous n'aurez pas occasionnellement un surage, vous pouvez suivre ces précautions pour réduire les chances de dépasser vos limites allouées :

- Faites attention au nombre de caractères de votre SMS. Envoi involontaire de plus d'un segment pourrait provoquer des dépassements. Plus de détails [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calculez soigneusement vos caractères SMS pour tenir compte de Liquid ou du contenu connecté. Le compositeur de SMS Braze dans votre tableau de bord n'estime pas l'utilisation de l'une ou l'autre de ces fonctionnalités.
- Considérez le type d'encodage que votre message utilise - si votre message utilise l'encodage GSM-7, vous pouvez généralement estimer que vous pouvez envoyer un message avec 128 caractères par segment de message. Si votre message utilise l'encodage [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) , vous pouvez généralement estimer que vous pouvez envoyer un message de 67 caractères par segment de message.
- Test de test ! Testez toujours vos messages SMS avant le lancement, en particulier lorsque vous utilisez Liquid et le contenu connecté.

### Comment créer une logique pour les opt-ins sélectifs pour les SMS afin que les utilisateurs soient dans le bon groupe d'abonnement ?

Les mots-clés personnalisés seraient écrits en tant qu'événements personnalisés, vous souhaiteriez donc créer des segments en fonction des mots-clés dans lesquels les clients peuvent écrire. Par exemple, si un utilisateur opte pour les SMS pour les messages VIP, mais pas les alertes, vous pouvez créer un segment VIP et un segment Alertes, puis assigner l'utilisateur au segment approprié.

### Combien de caractères un émoji utilise-t-il ?

Les émojis peuvent être un peu délicats, car il n'y a pas de nombre de personnages standard sur tous les émojis. Il y a le risque que les émoticônes dépassent la limite de caractères et fractionnent le SMS en plusieurs messages, malgré qu'il se montre comme un message dans le compositeur de Braze. Quand QA vos messages, vous pouvez mieux vérifier si un message sera divisé en utilisant [cet outil]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Comment serai-je facturé pour les SMS ?

En plus des frais pour les codes courts et longs, la facturation est effectuée par le nombre de segments de messages envoyés par pays. Pour en savoir plus sur la façon dont les segments de messages sont calculés, consultez notre guide [Segments de messages et Copier les limites]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Pour les excédents, votre gestionnaire de compte vous contactera pour vous informer si vous êtes près d'atteindre votre maximum, fournir des rapports pertinents pour vous aider à vous informer. Pour de plus amples questions concernant les excédents, veuillez contacter votre représentant de Braze.

### Si les textes d'un utilisateur s'arrêtent à notre code court, se désabonnent-ils du groupe d'abonnement ?

À quoi cela ressemble-t-il sur le profil de l'utilisateur ? Le groupe d'abonnement retournera à 2 tirets (-), et il y aura des événements personnalisés pour s'abonner et se désabonner.

### Y a-t-il un moyen de voir si un alias existe sur un profil utilisateur ?

Les alias ne sont pas visibles sur le profil de l'utilisateur, vous devrez utiliser les points de terminaison d'exportation des données utilisateur pour confirmer les alias à définir.

### Quels sont les codes courts partagés ?

Avec un code court partagé, tous les messages textuels, quelle que soit l'entreprise ou l'organisation qui les envoie, arriver sur un appareil mobile d'un consommateur à partir du même numéro de téléphone à 5-6 chiffres. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise n'aura pas de code court dédié.

Parmi les inconvénients de cette approche, citons :

- Si vos clients se désintègrent des messages d'une autre entreprise qui ont un code court partagé avec vous, ils auront également choisi de ne plus recevoir vos messages.
- Si une entreprise viole les règles, tous les messages de l'entreprise sont suspendus.
- Problèmes de sécurité

### Que se passe-t-il si plusieurs utilisateurs ont le même numéro de téléphone ?

Braze va déduper les utilisateurs au niveau de l'étape de Canvas il ne devrait donc pas être possible pour un utilisateur de recevoir plus d'un SMS pour une étape de Canvas même si plusieurs utilisateurs partagent le même numéro de téléphone.

{% alert important %} Si vous étourdissez vos utilisateurs dans une toile et que vous avez des horaires différents pour chaque étape de Canvas vous pouvez envoyer un utilisateur avec le même e-mail ou téléphone en double messages. {% endalert %}

### Les propriétés de l'évènement SMS captureront-elles des mots-clés dans une phrase ?

Pour qu'un mot clé soit reconnu dans une phrase, (p. ex. "s'il vous plaît arrêter de m'envoyer un texte") vous devrez utiliser une instruction Liquid dans le message pour reconnaître le mot spécifique. Les propriétés d'événement ont une limite de caractères de 256, sinon, il n'y a pas de limite de caractères.

