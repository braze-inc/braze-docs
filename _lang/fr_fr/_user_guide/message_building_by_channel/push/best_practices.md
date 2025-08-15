---
page_order: 20
nav_title: Bonnes pratiques
article_title: Bonnes pratiques de notification push
description: "Cette page contient des meilleures pratiques de push et des cas d'utilisation pour s'assurer que vos messages push inspirent l'engagement plutôt que l'agacement."
channel: push
---

# Bonnes pratiques de notifications push

Les notifications push sont des outils puissants pour interagir avec les utilisateurs de votre application, mais elles doivent être utilisées avec précaution pour garantir qu'elles délivrent des messages opportuns et pertinents. Avant d'envoyer votre message push, consultez les meilleures pratiques suivantes pour les choses que vous devez savoir et vérifier.

{% alert important %}
Vos messages de notification push doivent être conformes aux directives de l’App Store d’Apple et des politiques de Google Play Store, en particulier concernant l’utilisation de messages de notification push en tant que publicités, spam, promotions, etc. En savoir plus sur les [réglementations des notifications push mobiles]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Composer votre message de notification push

En guise de bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre optionnel que pour le corps du message, à environ 30-40 caractères dans une notification push mobile. Notez que le compteur de caractères du compositeur ne tient pas compte des caractères Liquid. Cela signifie que le nombre final de caractères d'un message dépend du rendu de Liquid pour chaque utilisateur. En cas de doute, gardez le contenu bref et agréable.

## Optimiser le ciblage

### Collecter des données utilisateur pertinentes

Les notifications push doivent être traitées avec précaution pour cibler les utilisateurs avec des notifications opportunes et pertinentes. Braze collectera des informations utiles sur l’appareil et l’utilisation qui peuvent être utilisées pour cibler les segments pertinents. Ces informations doivent être complétées par des événements personnalisés et des attributs spécifiques à votre application. En utilisant ces données, vous pouvez cibler soigneusement les messages pour augmenter les taux d'ouverture et diminuer les cas d'utilisateurs désactivant les notifications push.

### Créer une page de paramètres de notification

Vous pouvez créer une page de paramètres dans votre application qui permet aux utilisateurs de vous indiquer quelles notifications ils souhaitent recevoir. Une approche courante consiste à créer un attribut personnalisé booléen dans Braze correspondant au statut des paramètres de l'application. Par exemple, une application d’actualités peut avoir des paramètres d’abonnement pour les éditions spéciales, les actualités sportives ou politiques.

Lorsque l'application de nouvelles souhaite créer une campagne ciblant uniquement les utilisateurs intéressés par la politique, elle ajoute le filtre d'attribut `Subscribes to Politics` au segment. Lorsqu’il est défini sur « vrai », seuls les utilisateurs qui s’abonnent aux notifications les recevront.

Pour plus d'informations sur la définition des attributs personnalisés, consultez les articles suivants pour [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) ou [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Augmenter les abonnements et la pertinence

### Obtenir l'autorisation de l'utilisateur

Les statistiques générales pour l'activation des notifications push se rapporteront à savoir si l'utilisateur a approuvé les notifications avec son système d'exploitation. Si les utilisateurs désactivent les notifications sur iOS, ils seront automatiquement supprimés de notre système car Apple n'autorisera pas l'envoi du jeton de notification.

Android 13 et les versions ultérieures nécessitent l'obtention d'une autorisation pour afficher les notifications push. Les versions plus anciennes d’Android abonneront par défaut les utilisateurs aux notifications.

### Préparer les utilisateurs pour les notifications push

Vous n'avez qu'une seule chance de demander à un utilisateur l'autorisation d'envoyer des notifications push, et après qu'il ait refusé, il est très difficile de le convaincre de réactiver les notifications push dans les paramètres de son appareil. Pour cette raison, vous devriez préparer vos utilisateurs aux notifications push en utilisant un message in-app avant d’afficher l’invite système. Voir [Messages in-app d’amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) pour en savoir plus sur l'augmentation des abonnements.

### Ajouter des contrôles d'abonnement push

Pour éviter que les utilisateurs désactivent les notifications au niveau de l'appareil, ce qui supprime complètement leur jeton de push en premier plan, laissez les utilisateurs contrôler leur abonnement aux notifications directement dans votre application. Pour plus d’informations, voir [Mise à jour des états d’abonnement aux notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Comprendre les états d'abonnement push

L'état de l'abonnement push ne garantit pas qu'une notification push sera livrée—les utilisateurs doivent également être activés pour recevoir des notifications. C'est parce qu'un profil utilisateur peut avoir plusieurs appareils avec différentes autorisations de notification au premier plan, mais un seul état d'abonnement aux notifications.

Si un utilisateur ne dispose pas d’un jeton de notification push de premier plan valide pour l’application (c’est-à-dire qu’il a désactivé les jetons de notification push au niveau de l’appareil par le biais des paramètres, en choisissant de ne pas recevoir de notifications), son statut d’abonnement peut toujours être considéré comme étant `subscribed` aux notifications push. Cependant, cet utilisateur ne sera pas `Push Enabled for App` dans Braze puisque le jeton de notification push de premier plan n'est pas valide.

De plus, si un profil utilisateur n'a pas de jeton de notification push valide ou enregistré pour d'autres applications, son filtre `Push Enabled` dans la segmentation sera également faux.

## Mettre en œuvre une politique de coucher de soleil pour les utilisateurs non réactifs

Même lorsque vous envoyez uniquement des notifications push pertinentes et opportunes, certains utilisateurs peuvent encore ne pas y répondre et les trouver indésirables. Supposons qu'un utilisateur montre un historique d'ignorance répétée de vos notifications push. Dans ce cas, il est judicieux d'arrêter de leur envoyer des notifications avant qu'ils ne deviennent agacés par les communications de votre application ou ne la désinstallent complètement. 

Pour ce faire, créez une [politique de coucher de soleil]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) qui finit par arrêter d'envoyer des notifications push aux utilisateurs qui n'ont pas eu d'ouverture directe ou influencée depuis longtemps.

1. Identifier les utilisateurs non réactifs en fonction des ouvertures directes ou influencées.
2. Arrêtez progressivement d'envoyer des notifications push à ces utilisateurs.
3. Avant de supprimer complètement les notifications push, envoyez une dernière notification expliquant pourquoi ils ne les recevront plus. En ouvrant cette notification, les utilisateurs peuvent ainsi démontrer leur souhait de continuer à recevoir des notifications push.
4. Après l'entrée en vigueur de la politique de coucher du soleil, utilisez un [message intégré à l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) pour rappeler à ces utilisateurs que, bien qu'ils ne recevront plus de notifications push, les canaux de messagerie intégrée continueront à fournir des informations intéressantes et utiles.

Bien que vous puissiez être réticent à arrêter d'envoyer des notifications push aux utilisateurs qui y ont initialement souscrit, rappelez-vous que d'autres canaux de messagerie peuvent atteindre plus efficacement ces utilisateurs, surtout s'ils ont déjà ignoré vos notifications push. Si l'utilisateur ouvre vos e-mails, les campagnes par e-mail sont un bon moyen de les atteindre en dehors de votre application. Si ce n’est pas le cas, les messages in-app sont la meilleure façon de fournir du contenu sans risquer que l’utilisateur désinstalle votre application.

## Définir des événements de conversion pour les ouvertures d'applications

Lors de l'attribution d'[événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) à une campagne push, vous pouvez suivre les ouvertures d'application pendant une certaine période après la réception de la campagne. Définir un événement de conversion pour les ouvertures d'application fournit une perspective différente des statistiques de résultats que vous recevez normalement après une campagne de push.

Bien que tous les résultats des campagnes push décomposent les ouvertures directes et les ouvertures d'un message (qui incluent à la fois les ouvertures directes et [influencées]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), le suivi des conversions suivra tout type d'ouverture, qu'elle soit directe ou influencée.

En outre, en utilisant l’événement de conversion « ouvrir l’application », vous suivez l’ouverture de l’application qui se produit avant la date limite de conversion (par exemple, trois jours). Ceci diffère d’une ouverture influencée en ce sens que le temps dont dispose l’utilisateur pour enregistrer une ouverture influencée peut varier d’un individu à l’autre, selon le comportement d’engagement passé de chaque utilisateur.

## Articles connexes

Vous n'avez pas trouvé ce que vous cherchiez ? Consultez ces articles de meilleures pratiques supplémentaires :

- [Formats d’images et de messages pour les notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Messages in-app d’amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Livrabilité pour les appareils Android chinois]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Être sûr avant d’envoyer : canaux]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
