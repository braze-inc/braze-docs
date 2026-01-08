---
nav_title: Meilleures pratiques
article_title: Meilleures pratiques pour les campagnes
page_order: 0
description: "Cet article présente les meilleures pratiques pour créer et personnaliser vos campagnes."
tool: Campaign

---

# Meilleures pratiques en matière de campagnes

## Les quatre T de la Braze

Braze vous recommande de n'envoyer que les données personnalisées que vous avez l'intention d'utiliser sur la plateforme de Braze. Tenez compte de la philosophie des "quatre T de Braze" pour vous assurer que vous n'envoyez que des données qui vous seront utiles :

- **Ciblez** vos audiences en créant des [segments d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Déclenchez** vos messages avec une livraison [par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou une [réception/distribution par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Modélisez** et personnalisez vos messages à l'aide de la [logique conditionnelle Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Suivez l** 'efficacité de vos campagnes grâce au [suivi des conversions]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Cela vous permet d'optimiser les données que vous envoyez à Braze et de rationaliser votre capacité à envoyer des messages à vos utilisateurs tout en vous garantissant contre le suivi de points de données que votre équipe pourrait ne pas trouver utiles à long terme. 

## Ciblage des utilisateurs

Au fur et à mesure que vous créez vos campagnes, il se peut que vous constatiez des baisses d'audience. À ce stade crucial, vous pouvez cibler vos [utilisateurs retardataires]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) avec une campagne spécialisée à l'aide de la segmentation. 

### Identifier votre audience

Exploitez les segments et les filtres à votre avantage en définissant votre audience. Réfléchissez au ciblage de votre campagne et de vos messages. Grâce à ces informations clés, vous pouvez créer des [campagnes multicanales]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) qui offrent la possibilité de créer vos messages dans différents canaux afin de répondre aux préférences de votre audience en matière de communication.

Il est également important de comprendre vos [utilisateurs actifs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) pour montrer votre appréciation à vos utilisateurs constants.

## Campagnes multicanal

### Sensibilisation à la fonctionnalité

Si votre objectif est d'attirer vos utilisateurs vers une nouvelle fonctionnalité ou une nouvelle version de l'appli, utilisez une stratégie multicanal en privilégiant les canaux in-app. Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) et les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) sont généralement moins perturbants si un utilisateur ne souhaite pas effectuer une mise à jour immédiate. 

Veillez à inclure des [liens profonds]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers le magasin d'applications approprié.

Persuader les utilisateurs de mettre à jour leur application ou de changer la façon dont ils l'utilisent peut être difficile, alors faites-leur part de tous les avantages de la nouvelle version ou des nouvelles fonctionnalités et de la façon dont cela améliorera leur expérience sur votre application. 

### Envoi du calendrier

Le choix du moment est essentiel ! Lorsque votre objectif est de convaincre les utilisateurs de mettre à jour leur application, attendez qu'ils aient une expérience sur l'application positive pour leur poser la question. Pour maintenir l'intérêt de votre audience, évitez les envois de messages répétitifs qui peuvent paraître intrusifs.

Au fil du temps, vos utilisateurs risquent d'oublier certaines fonctionnalités ou de ne pas remarquer les nouvelles. Lorsque de nouvelles fonctionnalités sont ajoutées, veillez à en informer vos utilisateurs à l'aide de [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Si les utilisateurs n'utilisent pas les principales fonctionnalités de l'application, il est préférable de leur rappeler qu'ils utilisent votre application et que cette nouvelle fonctionnalité pourrait leur être utile. Notre article sur l' [abonnement aux données]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) contient plus d'informations sur la manière de s'assurer que votre demande correspond aux attentes des utilisateurs en matière de flux de travail. 

## Notations élevées

Obtenir une note de cinq étoiles dans la boutique d'applications fait partie des souhaits de tous les marketeurs mobiles. Obtenir des avis positifs n'est cependant pas une tâche facile, car cela demande un travail supplémentaire de la part de vos utilisateurs. En appliquant nos fonctionnalités de manière astucieuse, nous pouvons vous aider à accroître l'engagement de vos clients.

### Le ciblage des utilisateurs intensifs

Les utilisateurs expérimentés peuvent être des défenseurs de votre application. Souvent, ils interagissent régulièrement avec votre application et peuvent fournir un retour d'information pour l'améliorer. Bien qu'ils diffèrent d'une application à l'autre, les utilisateurs expérimentés ont tendance à avoir les caractéristiques suivantes :

- Enregistrement de nombreuses sessions
- Utilisation récente de l'application
- Dépenser de l'argent et faire des achats

Pour obtenir un meilleur classement, demandez à vos utilisateurs les plus performants d'évaluer votre application dans le magasin d'applications, car ils sont plus susceptibles d'avoir de bonnes choses à dire. Par exemple, vous pouvez créer un segment nommé "Power users" avec ces filtres :
- A utilisé ces applications plus de 10 fois au cours des 14 derniers jours
- A dépensé plus de 50 dollars

Exemple de segmentation ciblant les utilisateurs expérimentés d'une application.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visiter le magasin d'applications prend du temps à vos utilisateurs. Pour maximiser la probabilité qu'ils fassent cet effort supplémentaire, demandez une note ou un avis alors qu'ils viennent d'avoir une expérience positive avec votre application. Par exemple, posez-leur la question après qu'ils ont franchi un niveau de jeu ou effectué un achat à l'aide d'un code de réduction. Notre article sur l' [abonnement aux données]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) contient plus d'informations sur les moyens de s'assurer que votre demande correspond aux attentes des utilisateurs en matière de flux de travail.

## Planification de vos campagnes

Lorsque vous modifiez des planifications de campagne ou des audiences, tenez compte des meilleures pratiques suivantes :

- **Campagnes à planification unique :** Vous pouvez modifier la campagne jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Vous pouvez modifier la campagne jusqu'à l'heure d'envoi planifiée.
- **Campagnes d'envoi local :** Ne modifiez pas vos documents 24 heures avant l'heure d'envoi prévue.
- **Campagnes d'envoi optimales :** N'effectuez pas de modifications 24 heures avant minuit le jour où l'envoi de la campagne est planifié.

{% alert note %}
Si vous modifiez une campagne en ligne et que vous changez la réception/distribution en **heure locale**, un nouveau lot de messages sera mis en file d'attente, ce qui signifie que vos utilisateurs recevront le message deux fois en raison de la double mise en file d'attente. Pour éviter cela, arrêtez d'abord la campagne originale, puis lancez-en une copie après avoir mis à jour la planification.
{% endalert %}

