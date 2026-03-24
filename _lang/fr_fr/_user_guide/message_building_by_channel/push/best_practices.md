---
page_order: 20
nav_title: Bonnes pratiques
article_title: Bonnes pratiques de notification push
description: "Cette page contient des bonnes pratiques et des cas d'utilisation pour les notifications push, afin de vous assurer que vos messages push suscitent l'engagement plutôt que l'agacement."
channel: push
---

# Bonnes pratiques de notifications push

Les notifications push sont des outils puissants pour interagir avec les utilisateurs de votre application, mais elles doivent être utilisées avec précaution pour garantir la diffusion de messages opportuns et pertinents. Avant d'envoyer votre message push, consultez les bonnes pratiques suivantes pour savoir ce que vous devez vérifier et garder à l'esprit.

{% alert important %}
Vos messages de notification push doivent être conformes aux directives de l'App Store d'Apple et aux politiques du Google Play Store, en particulier concernant l'utilisation de messages push en tant que publicités, spam, promotions, etc. En savoir plus sur les [réglementations des notifications push mobiles]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Rédiger votre message de notification push

En guise de bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre optionnel que pour le corps du message, à environ 30-40 caractères dans une notification push mobile. Notez que le compteur de caractères du composeur ne tient pas compte des caractères Liquid. Cela signifie que le nombre final de caractères d'un message dépend du rendu Liquid pour chaque utilisateur. En cas de doute, gardez le contenu bref et concis.

## Réduire la taille du PAYLOAD des notifications push

La taille maximale du PAYLOAD dépend de la plateforme.

| Plateforme | Taille maximale du PAYLOAD |
| --- | --- |
| Web | 3 807 octets |
| Android | 3 930 octets |
| iOS | 3 960 octets |
| Kindle | 5 985 octets |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Si votre push dépasse la taille maximale du PAYLOAD, le message risque de ne pas être envoyé. La bonne pratique consiste à limiter votre PAYLOAD à quelques centaines d'octets.

### Qu'est-ce qu'un PAYLOAD push ?

Les fournisseurs de services push déterminent si votre notification push peut être affichée à un utilisateur en examinant la taille en octets de l'ensemble du PAYLOAD push. Le PAYLOAD est limité à **4 Ko (4 096 octets)** pour la plupart des services de notifications push, notamment :

- Apple Push Notification service (APNs)
- Firebase Cloud Messaging (FCM) d'Android
- Push Web
- Notification push Huawei

Ces services push refuseront toute notification dépassant cette limite.

Braze réserve une partie du PAYLOAD push à des fins d'intégration et d'analytique. Dans ces conditions, la taille maximale de notre PAYLOAD est de **3 807 octets**. Si votre push dépasse cette taille, le message risque de ne pas être envoyé. La bonne pratique consiste à limiter votre PAYLOAD à quelques centaines d'octets.

Les éléments suivants constituent le PAYLOAD de votre push :

- Le texte, comme le titre et le corps du message
- Le rendu final de toute personnalisation Liquid
- Les URL des images (mais pas la taille de l'image elle-même)
- Les URL des cibles de clic
- Les noms des boutons
- Les paires clé-valeur

### Conseils pour réduire la taille du PAYLOAD

Pour réduire la taille du PAYLOAD :

- Veillez à ce que votre message soit bref. Une bonne règle générale consiste à le rendre exploitable et utile en moins de 40 caractères.
- Supprimez les espaces superflus et les sauts de ligne de votre texte.
- Réfléchissez à la manière dont Liquid s'affichera lors de l'envoi. Étant donné que le rendu final de toute personnalisation Liquid varie d'un utilisateur à l'autre, Braze ne peut pas déterminer si un PAYLOAD push dépassera la limite de taille lorsque du Liquid est inclus. Si votre code Liquid génère un message plus court, cela ne devrait pas poser de problème. Cependant, si votre Liquid produit un message plus long, votre push peut dépasser la limite de taille du PAYLOAD. Testez toujours votre message push sur un appareil réel avant de l'envoyer aux utilisateurs.
- Envisagez de raccourcir les URL à l'aide d'un raccourcisseur d'URL.

## Optimiser le ciblage

### Collecter des données utilisateur pertinentes

Les notifications push doivent être traitées avec précaution pour cibler les utilisateurs avec des notifications opportunes et pertinentes. Braze collecte des informations utiles sur l'appareil et l'utilisation qui peuvent servir à cibler les segments pertinents. Ces informations doivent être complétées par des événements personnalisés et des attributs spécifiques à votre application. En exploitant ces données, vous pouvez cibler soigneusement vos messages pour augmenter les taux d'ouverture et réduire le nombre d'utilisateurs désactivant les notifications push.

### Créer une page de paramètres de notification

Vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous indiquer quelles notifications ils souhaitent recevoir. Une approche courante consiste à créer un attribut personnalisé de type booléen dans Braze correspondant au statut du paramètre de l'application. Par exemple, une application d'actualités peut proposer des paramètres d'abonnement pour les éditions spéciales, les actualités sportives ou la politique.

Lorsque l'application d'actualités souhaite créer une campagne ciblant uniquement les utilisateurs intéressés par la politique, elle ajoute le filtre d'attribut `Subscribes to Politics` au segment. Lorsqu'il est défini sur « vrai », seuls les utilisateurs abonnés aux notifications les recevront.

Pour plus d'informations sur la définition des attributs personnalisés, consultez les articles suivants pour [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) ou l'[API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Augmenter les abonnements et la pertinence

### Obtenir l'autorisation de l'utilisateur

Les statistiques générales d'activation des notifications push indiquent si l'utilisateur a approuvé les notifications auprès de son système d'exploitation. Si les utilisateurs désactivent les notifications sur iOS, ils seront automatiquement supprimés de notre système, car Apple n'autorise pas l'envoi du jeton de notification push.

Android 13 et les versions ultérieures nécessitent l'obtention d'une autorisation avant de pouvoir afficher les notifications push. Les versions plus anciennes d'Android abonnent les utilisateurs aux notifications par défaut.

### Préparer les utilisateurs aux notifications push

Vous n'avez qu'une seule chance de demander à un utilisateur l'autorisation d'envoyer des notifications push, et après un refus, il est très difficile de le convaincre de réactiver les notifications push dans les paramètres de son appareil. C'est pourquoi vous devriez préparer vos utilisateurs aux notifications push en utilisant un message in-app avant d'afficher l'invite système. Consultez [Messages in-app d'amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour en savoir plus sur l'augmentation des abonnements.

### Ajouter des contrôles d'abonnement push

Pour éviter que les utilisateurs ne désactivent les notifications au niveau de l'appareil, ce qui supprime complètement leur jeton de notification push de premier plan, permettez-leur de contrôler leur abonnement aux notifications directement dans votre application. Pour plus de détails, consultez [Mise à jour des états d'abonnement aux notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Comprendre les états d'abonnement push

L'état d'abonnement push ne garantit pas qu'une notification push sera livrée — les utilisateurs doivent également être activés pour les notifications push afin de les recevoir. En effet, un profil utilisateur peut avoir plusieurs appareils avec différentes autorisations de notification push de premier plan, mais un seul état d'abonnement push.

Si un utilisateur ne dispose pas d'un jeton de notification push de premier plan valide pour une application (c'est-à-dire qu'il a désactivé les jetons de notification push au niveau de l'appareil via les paramètres, en choisissant de ne pas recevoir de notifications), son état d'abonnement peut toujours être considéré comme `subscribed` aux notifications push. Cependant, cet utilisateur ne sera pas `Foreground Push Enabled for App` dans Braze, puisque le jeton de notification push de premier plan n'est pas valide.

De plus, si un profil utilisateur ne possède aucun jeton de notification push valide ou enregistré pour d'autres applications, son filtre `Foreground Push Enabled` dans la segmentation sera également faux.

## Mettre en œuvre une politique de désengagement pour les utilisateurs non réactifs

Même lorsque vous envoyez uniquement des notifications push pertinentes et opportunes, certains utilisateurs peuvent ne pas y répondre et les trouver indésirables. Si un utilisateur montre un historique d'ignorance répétée de vos notifications push, il est judicieux d'arrêter de lui en envoyer avant qu'il ne devienne agacé par les communications de votre application ou ne la désinstalle complètement.

Pour ce faire, créez une [politique de désengagement]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) qui finit par arrêter d'envoyer des notifications push aux utilisateurs qui n'ont pas eu d'ouverture directe ou influencée depuis longtemps.

1. Identifiez les utilisateurs non réactifs en fonction des ouvertures directes ou influencées.
2. Arrêtez progressivement d'envoyer des notifications push à ces utilisateurs.
3. Avant de supprimer complètement les notifications push, envoyez une dernière notification expliquant pourquoi ils ne les recevront plus. Cela donne aux utilisateurs la possibilité de démontrer leur intérêt pour la poursuite des notifications push en ouvrant cette notification.
4. Après l'entrée en vigueur de la politique de désengagement, utilisez un [message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) pour rappeler à ces utilisateurs que, bien qu'ils ne recevront plus de notifications push, les canaux de messagerie in-app continueront à leur fournir des informations intéressantes et utiles.

Bien que vous puissiez être réticent à arrêter d'envoyer des notifications push aux utilisateurs qui y ont initialement souscrit, rappelez-vous que d'autres canaux de communication peuvent atteindre plus efficacement ces utilisateurs, surtout s'ils ont déjà ignoré vos notifications push. Si l'utilisateur ouvre vos e-mails, les campagnes par e-mail sont un bon moyen de le joindre en dehors de votre application. Sinon, les messages in-app sont la meilleure façon de fournir du contenu sans risquer que l'utilisateur désinstalle votre application.

## Définir des événements de conversion pour les ouvertures d'application

Lors de l'attribution d'[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) à une campagne push, vous pouvez suivre les ouvertures d'application pendant une certaine période après la réception de la campagne. Définir un événement de conversion pour les ouvertures d'application fournit une perspective différente des statistiques de résultats que vous recevez normalement après une campagne push.

Bien que tous les résultats des campagnes push décomposent les ouvertures directes et les ouvertures d'un message (qui incluent à la fois les ouvertures directes et [influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), le suivi des conversions comptabilise tout type d'ouverture, qu'elle soit directe ou influencée.

En outre, en utilisant l'événement de conversion « ouvre l'application », vous suivez les ouvertures d'application qui se produisent avant la date limite de conversion (par exemple, trois jours). Ceci diffère d'une ouverture influencée en ce sens que le temps dont dispose l'utilisateur pour enregistrer une ouverture influencée peut varier d'une personne à l'autre, selon le comportement d'engagement passé de chaque utilisateur.

## Articles connexes

Vous n'avez pas trouvé ce que vous cherchiez ? Consultez ces articles de bonnes pratiques supplémentaires :

- [Spécifications d'images et de texte pour les notifications push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [Messages in-app d'amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Livrabilité pour les appareils Android chinois]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Ce qu'il faut savoir avant d'envoyer : canaux]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)