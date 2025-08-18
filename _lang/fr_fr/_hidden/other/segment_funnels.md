---
nav_title: Entonnoirs de segments
permalink: /segment_funnels/
hidden: true
page_type: reference
---

# Entonnoirs de segments

> Les entonnoirs de segments sont parfaits pour limiter la taille de votre audience pour un cas d’utilisation de campagne spécifique, apprendre de cette audience et de ses interactions, et utiliser ces connaissances afin d’élaborer des stratégies et de concevoir des campagnes efficaces.

Les entonnoirs de segments vous permettent de voir comment chaque filtre que vous ajoutez affecte les statistiques de votre segment. Lorsque vous créez un segment, une ligne de données apparaîtra sous chaque filtre. Ces données fourniront les informations suivantes sur les utilisateurs ciblés par tous les filtres à ce moment-là :

- Nombre total d’utilisateurs ciblés et pourcentage de votre audience de base
- Valeur à vie et valeur à vie pour les utilisateurs payants  
- Nombre d’utilisateurs pouvant recevoir des e-mails
- Nombre d’utilisateurs abonnés aux communications par e-mail
- Nombre d’utilisateurs ayant activé les notifications push  
- Nombre d’utilisateurs abonnés aux notifications push

![]({% image_buster /assets/img_archive/segment_funnel_example.png %})

## Bonnes pratiques

- Ajouter des filtres qui documentent votre flux utilisateur vous permet de voir à quel endroit vous perdez des utilisateurs. Par exemple, si vous avez une application de réseau social et que vous voulez voir à quelle étape vous risquez de perdre des utilisateurs pendant votre processus d’onboarding, vous pouvez ajouter des filtres de données personnalisés pour s’inscrire, ajouter des amis et envoyer un premier message. Si vous découvrez que 85 % des utilisateurs s’inscrivent et ajoutent des amis, mais que seulement 45 % ont envoyé un premier message, alors vous saurez qu’il vous faut encourager les utilisateurs à envoyer plus de messages pendant vos campagnes d’onboarding et de marketing.

- Les entonnoirs de segments vous permettent de comparer le pourcentage d’utilisateurs qui effectuent différentes actions. Par instance, les utilisateurs actifs, ou ceux dont la LTV est élevée, ont-ils [tendance à interagir davantage avec le push ou l'e-mail](#push-email)? Pour en savoir plus, créez un segment d’utilisateurs actifs avec un ou plusieurs filtres, puis voyez comment les statistiques changent lorsque vous ajoutez un filtre pour s’abonner aux notifications push et lorsque vous ajoutez un filtre pour s’abonner aux communications par e-mail.

- Analysez la façon dont la valeur à vie change lorsque vous ajoutez des filtres. Pour les utilisateurs actifs, ceux qui se connectent à Facebook ou ceux qui se connectent à X (anciennement Twitter) ont-ils une LTV plus élevée ? Ou encore, la valeur à vie est-elle considérablement plus élevée pour les personnes qui se sont connectées aux deux ? Si vous constatez, par exemple, que la connexion à X (anciennement Twitter) a très peu d'impact sur la valeur vie client, mais que la connexion à Facebook en a beaucoup, vous pouvez décider d’encourager les connexions à Facebook dans vos campagnes marketing.

## Cas d’utilisation

### Impact d’une action utilisateur spécifique sur les conversions {#push-email}

En analysant l’impact d’une certaine action effectuée par un utilisateur (comme l’ajout d’articles à une liste d’envies) sur une conversion (comme effectuer des achats), vous pouvez répondre aux questions suivantes :

- L’action de l’utilisateur coïncide-t-elle avec davantage d’achats ?
- Quelle est l’importance de l’action de l’utilisateur ? Devez-vous créer des campagnes marketing qui encouragent davantage cette action ?

Supposons par exemple que vous ayez un groupe dans lequel tous les utilisateurs qui ont ajouté des articles à une liste d’envies ont également effectué un achat. Étant donné que seul un petit pourcentage d’utilisateurs ont ajouté des articles à une liste d’envies, l’application peut souhaiter encourager ce comportement à travers des campagnes marketing.

![Exemple d’entonnoir de segments avec les filtres suivants : "Dernière utilisation de ces applications il y a moins de 30 jours", Dernier ajout à la liste d'attente il y a moins de 30 jours" et Dernier achat il y a moins de 30 jours" pour atteindre 4 302 utilisateurs.]({% image_buster /assets/img_archive/Wish_List_2.png %})

### Comparer les canaux de messagerie

Créez un segment d’utilisateurs actifs (ou d’utilisateurs ayant les traits souhaités) et comparez leurs interactions avec différents canaux d’engagement, comme les e-mails et les notifications push. Par exemple, si les utilisateurs les plus loyaux sont abonnés aux notifications push, vous pourriez passer plus de temps à envoyer des campagnes par notification push aux utilisateurs actifs. Cependant, si vous constatez que la valeur à vie est plus élevée pour les personnes qui sont abonnées aux communications par e-mail, vous pourriez inviter plus d’utilisateurs actifs à s’abonner aux e-mails.

![Entonnoir de segments pour une campagne par e-mail avec les filtres suivants : "Dernier achat effectué il y a moins de 30 jours", "Dernière utilisation de ces applications il y a moins de 30 jours", "Push Enabled est vrai", et "Email Subscription Status est Opted In" pour atteindre 2 799 utilisateurs.]({% image_buster /assets/img_archive/Wish_List_Email.png %})

### Abonnements aux notification push Android ou iOS

Ce cas d’utilisation tire parti du filtre « Notification push activée pour l’app » pour cibler les utilisateurs iOS ou Android qui se sont abonnés aux notifications push.

![]({% image_buster /assets/img/seg_filter_examples/ios.png %})

![]({% image_buster /assets/img/seg_filter_examples/android.png %})

### Audience totalement abonnée aux notifications push

Ce cas d’utilisation tire parti du filtre « Notification push activée » pour cibler les utilisateurs qui se sont abonnés aux notifications push.

![]({% image_buster /assets/img/seg_filter_examples/both.png %})

### Groupe de contrôle global d’une audience ayant activé les notifications push

Ce cas d’utilisation tire parti des filtres « Notification push activée » et « Nombre de compartiments aléatoire » pour cibler les utilisateurs qui font partie du groupe de contrôle global qui s’est abonné aux notifications push.

![]({% image_buster /assets/img/seg_filter_examples/global_control.png %})

### Acheteurs récents

Ce cas d’utilisation tire parti du filtre « A effectué un achat pour la dernière fois » pour cibler les utilisateurs qui ont effectué un achat il y a moins de 7 jours.

![]({% image_buster /assets/img/seg_filter_examples/recent_purchase.png %})

### Engagement envers les notifications push

Ce cas d’utilisation tire parti du filtre « A effectué l’événement personnalisé pour la dernière fois » pour lequel l’événement personnalisé est « a ouvert n’importe quelle notification push » pour cibler les utilisateurs qui ont montré un engagement envers les notifications push durant les 21 derniers jours.

![]({% image_buster /assets/img/seg_filter_examples/push_engagement.png %})

### Argent dépensé dans l’application

Ce cas d’utilisation tire parti du filtre « Argent dépensé » pour cibler les utilisateurs qui ont dépensé au moins 1000 dollars.

![]({% image_buster /assets/img/seg_filter_examples/moneyspent.png %})


