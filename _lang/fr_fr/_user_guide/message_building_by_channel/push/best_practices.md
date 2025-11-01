---
page_order: 20
nav_title: Meilleures pratiques
article_title: Meilleures pratiques de poussée
description: "Cette page contient les meilleures pratiques de push et des cas d'utilisation pour s'assurer que vos messages push inspirent l'engagement plutôt que l'agacement."
channel: push
---

# Pousser les bonnes pratiques

Les notifications push sont des outils d'engagement puissants avec les utilisateurs de votre appli, mais elles doivent être utilisées avec précaution pour s'assurer qu'elles délivrent des messages opportuns et pertinents. Avant d'envoyer votre message push, reportez-vous aux bonnes pratiques suivantes pour connaître et vérifier les éléments à prendre en compte.

{% alert important %}
Vos messages in-app doivent respecter les règles de l'App Store d'Apple et du Play Store de Google, notamment en ce qui concerne l'utilisation des messages in-app comme publicités, spams, promotions, etc. En savoir plus sur les [réglementations relatives au push mobile.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps)
{% endalert %}

## Composez votre message push

En guise de bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre optionnel que pour le corps du message, à environ 30-40 caractères dans une notification push mobile. Notez que le compteur de caractères du compositeur ne tient pas compte des caractères liquides. Cela signifie que le nombre final de caractères d'un message dépend du rendu de Liquid pour chaque utilisateur. En cas de doute, faites court et doux.

## Réduire la taille de la charge utile des notifications push

La taille maximale de la charge utile dépend de la plate-forme.

| Plateforme | Taille maximale de la charge utile |
| --- | --- |
| Web | 3 807 octets |
| Android | 3 930 octets |
| iOS | 3 960 octets |
| Kindle | 5 985 octets |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si votre push dépasse la taille maximale de la charge utile, le message risque de ne pas être envoyé. La meilleure pratique consiste à limiter votre charge utile à quelques centaines d'octets.

### Qu'est-ce qu'une charge utile de poussée ?

Les fournisseurs de services push calculent si votre notification push peut être affichée à un utilisateur en examinant la taille en octets de l'ensemble de la charge utile push. La charge utile est limitée à **4 Ko (4 096 octets** ) pour la plupart des services "push", notamment :

- Service de notification push d'Apple (APN)
- Firebase Cloud Messaging (FCM) d'Android
- Poussée sur le web
- Poussée de Huawei

Ces services push refuseront toute notification dépassant cette limite.

Braze réserve une partie de la charge utile du push à des fins d'intégration et d'analyse/analytique. Dans ces conditions, la taille maximale de notre charge utile est de **3 807 octets**. Si votre push dépasse cette taille, le message risque de ne pas être envoyé. La meilleure pratique consiste à limiter votre charge utile à quelques centaines d'octets.

Les éléments suivants constituent la charge utile de votre push :

- Copie, telle que le titre et le corps du message
- Rendu final de toute personnalisation liquide
- URL des images (mais pas la taille de l'image elle-même)
- URL des cibles de ciblage
- Noms des boutons
- Paires clé-valeur

### Conseils pour réduire la taille de la charge utile

Pour réduire la taille de la charge utile :

- Veillez à ce que votre message soit bref. Une bonne ligne de conduite générale consiste à faire en sorte que les informations soient exploitables et utiles en moins de 40 caractères.
- Oubliez les espaces blancs et les sauts de ligne dans votre texte.
- Réfléchissez à la manière dont Liquid s'affichera lors de l'envoi. Étant donné que le rendu final de toute personnalisation Liquid varie d'un utilisateur à l'autre, Braze ne peut pas déterminer si une charge utile de push dépassera la limite de taille lorsque Liquid est inclus. Si votre liquid rend un message plus court, vous pouvez vous en sortir. Toutefois, si votre Liquid donne lieu à un message plus long, votre push peut dépasser la limite de taille de la charge utile. Testez toujours votre message push sur un appareil réel avant de l'envoyer aux utilisateurs.
- Envisagez de raccourcir les URL à l'aide d'un raccourcisseur d'URL.

## Optimiser le ciblage

### Collecter des données pertinentes sur les utilisateurs

Les notifications push doivent être traitées avec soin pour cibler les utilisateurs avec des notifications opportunes et pertinentes. Braze recueillera des informations utiles sur les appareils et l'utilisation qui peuvent être utilisées pour cibler des segments pertinents. Ces informations doivent être complétées par des événements et attributs personnalisés propres à votre application. Grâce à ces données, vous pouvez cibler soigneusement les messages afin d'augmenter les taux d'ouverture et de réduire le nombre d'utilisateurs qui désactivent le système push.

### Créer une page de paramètres de notification

Vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous indiquer les notifications qu'ils souhaitent recevoir. Une approche courante consiste à créer dans Braze un attribut personnalisé booléen correspondant à l'état du paramétrage de l'application. Par exemple, une application d'actualités peut proposer des paramètres d'abonnement pour les actualités de dernière minute, les actualités sportives ou les actualités politiques.

Lorsque l'application d'actualités souhaite créer une campagne ciblant uniquement les utilisateurs intéressés par la politique, elle ajoute le filtre d'attribut `Subscribes to Politics` au segment. Si la valeur est "true", seuls les utilisateurs qui se sont abonnés aux notifications les recevront.

Pour plus d'informations sur la définition des attributs personnalisés, consultez les articles suivants pour [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) ou l'[API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Augmenter les abonnements et la pertinence

### Obtenir l'autorisation de l'utilisateur

Les statistiques générales relatives à l'activation de la fonction "push" indiquent si l'utilisateur a approuvé les notifications dans son système d'exploitation. Si les utilisateurs désactivent les notifications sur iOS, ils seront automatiquement supprimés de notre système car Apple n'autorisera pas l'envoi du jeton push.

À partir d'Android 13, il est nécessaire d'obtenir une autorisation avant de pouvoir afficher des notifications push. Les anciennes versions d'Android abonnent les utilisateurs aux notifications par défaut.

### Des utilisateurs privilégiés pour le push

Vous n'avez qu'une seule chance de demander à un utilisateur l'autorisation de pousser, et après qu'il ait refusé, il est très difficile de le convaincre de réactiver le push dans les paramètres de son appareil. C'est pourquoi vous devez amorcer les utilisateurs pour le push à l'aide d'un message in-app avant d'afficher l'invite du système. Consultez les [messages in-app de Push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour en savoir plus sur l'augmentation des abonnements.

### Ajouter des contrôles d'abonnement push

Pour éviter que les utilisateurs ne désactivent les notifications au niveau de l'appareil, ce qui supprime complètement leur jeton push de premier plan, laissez-les contrôler leur abonnement push directement dans votre application. Pour plus d'informations, consultez la section [Mise à jour des états d'abonnement au service de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Comprendre les états de l'abonnement push

L'état de l'abonnement push ne garantit pas qu'un push sera délivré - les utilisateurs doivent également être activés pour recevoir des notifications push. En effet, un profil utilisateur peut avoir plusieurs appareils avec différentes autorisations de push au premier plan, mais un seul état d'abonnement au push.

Si un utilisateur n'a pas de jeton push valide au premier plan pour une application (c'est-à-dire qu'il désactive les jetons push au niveau de l'appareil via les paramètres, en choisissant de ne pas recevoir de notifications), son état d'abonnement peut toujours être considéré comme `subscribed` to push. Cependant, cet utilisateur ne sera pas `Foreground Push Enabled for App` dans Braze car le jeton de poussée d'avant-plan n'est pas valide.

En outre, si un profil utilisateur n'a pas de jeton de poussée valide ou enregistré pour d'autres applications, son filtre `Foreground Push Enabled` dans la segmentation sera également faux.

## Mettre en œuvre une politique de temporisation pour les utilisateurs qui ne répondent pas.

Même lorsque vous n'envoyez que des notifications push pertinentes et opportunes, certains utilisateurs peuvent ne pas y répondre et les trouver spammy. Supposons qu'un utilisateur ait l'habitude d'ignorer vos notifications push à plusieurs reprises. Dans ce cas, il est préférable d'arrêter de leur envoyer des messages avant qu'ils ne s'agacent des communications de votre application ou qu'ils ne la désinstallent complètement. 

Pour ce faire, créez une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) qui finit par cesser d'envoyer des notifications push aux utilisateurs qui n'ont pas eu d'ouverture directe ou influencée depuis longtemps.

1. Identifiez les utilisateurs qui ne réagissent pas en fonction des ouvertures directes ou influencées.
2. Arrêtez progressivement d'envoyer des notifications push à ces utilisateurs.
3. Avant de supprimer complètement les notifications push, envoyez une dernière notification expliquant pourquoi ils ne les recevront plus. Les utilisateurs ont ainsi la possibilité de montrer leur intérêt pour des pushs continus en ouvrant cette notification.
4. Après l'entrée en vigueur de la politique de temporisation, utilisez un [message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) pour rappeler à ces utilisateurs que même s'ils ne recevront plus de push, les canaux d'envoi de messages in-app continueront à fournir des informations intéressantes et utiles.

Bien que vous puissiez être réticent à l'idée d'arrêter d'envoyer des pushs aux utilisateurs qui y ont initialement souscrit, n'oubliez pas que d'autres canaux de communication peuvent atteindre plus efficacement ces utilisateurs, en particulier s'ils ont précédemment ignoré vos pushs. Si l'utilisateur ouvre vos e-mails, les campagnes d'e-mails sont un bon moyen de l'atteindre en dehors de votre appli. Si ce n'est pas le cas, alors les messages in-app sont le meilleur moyen de diffuser du contenu sans risquer que l'utilisateur désinstalle votre application.

## Définir des événements de conversion pour les ouvertures d'applications

Lorsque vous attribuez des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) à une campagne push, vous pouvez suivre les ouvertures d'apps pendant une certaine période après la réception de la campagne. La définition d'un événement de conversion pour les ouvertures d'applis offre des informations différentes des statistiques de résultats que vous recevez normalement après une campagne push.

Alors que tous les résultats des campagnes de communication ventilent les ouvertures directes d'un message et les ouvertures (qui comprennent à la fois les [ouvertures]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) directes et [influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), le suivi des conversions permet de suivre tout type d'ouverture, qu'elle soit directe ou influencée.

En outre, en utilisant l'événement de conversion "ouvre l'application", vous suivez les ouvertures d'applications qui ont lieu avant la date limite de conversion (par exemple, trois jours). Cela diffère d'une ouverture influencée dans la mesure où le temps dont dispose un utilisateur pour enregistrer une ouverture influencée peut varier d'une personne à l'autre, en fonction du comportement d'engagement antérieur de chaque utilisateur.

## Articles connexes

Vous n'avez pas trouvé ce que vous cherchiez ? Consultez ces autres articles sur les meilleures pratiques :

- [Formats d'envoi de messages et d'images en mode push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Messages in-app push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Livrabilité pour les appareils Android chinois]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Sachez avant d'envoyer : les canaux]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
