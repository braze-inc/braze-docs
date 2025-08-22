---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques relatives aux campagnes
page_order: 0
description: "Cet article fournit les bonnes pratiques relatives à la création et à la personnalisation de vos campagnes."
tool: Campaign

---

# Bonnes pratiques relatives aux campagnes

## Les quatre T de Braze

Braze vous recommande de n’envoyer que les données utilisateurs que vous désirez utiliser sur la plateforme Braze. Prenez en compte la philosophie des « Quatre T de Braze » pour vous assurer de n’envoyer que les données que vous utiliserez pour :

- **Ciblez** vos audiences en créant des [segments d'audience]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Déclenchez** vos messages avec une livraison [par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou une [réception/distribution par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Modélisez** et personnalisez vos messages à l'aide de la [logique conditionnelle Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Assurez le suivi** de l’efficacité de vos campagnes grâce au [suivi des conversions]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Ceci vous permettra d’optimiser les données que vous enverrez à Braze et de simplifier votre capacité à envoyer des messages à vos utilisateurs en vous prémunissant contre le suivi de points de données pouvant ne pas être utiles à votre équipe sur le long terme. 

## Ciblage des utilisateurs

Au fur et à mesure que vous construisez vos campagnes, vous pourriez constater des défaillances de vos audiences. À ce stade crucial, vous pouvez cibler vos [utilisateurs retardataires]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) avec une campagne spécialisée à l'aide de la segmentation. 

### Identifiez votre audience

Utilisez à votre avantage les segments et les filtres en définissant votre audience. Considérez les utilisateurs ciblés par votre campagne et vos messages. Grâce à ces informations clés, vous pouvez créer des [campagnes multicanales]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) qui offrent la possibilité de créer vos messages dans différents canaux afin de répondre aux préférences de votre audience en matière de communication.

Il est également important de comprendre vos [utilisateurs actifs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) pour montrer votre appréciation à vos utilisateurs constants.

## Campagnes multicanales

### Connaissance des fonctionnalités

Si votre objectif est d'attirer vos utilisateurs vers une nouvelle fonctionnalité ou une nouvelle version de l'appli, utilisez une stratégie multicanal en privilégiant les canaux in-app. Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) et les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) sont généralement moins perturbants si un utilisateur ne souhaite pas effectuer une mise à jour immédiate. 

Veillez à inclure des [liens profonds]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers le magasin d'applications approprié.

Il peut être difficile de persuader les utilisateurs de mettre à jour leur application ou modifier l’utilisation qu’ils en font. Faites-leur donc comprendre les avantages de la nouvelle version ou fonctionnalité et en quoi elle améliorera leur expérience avec votre application. 

### Timing d’envoi

Le timing est la clé ! Lorsque votre objectif est de convaincre les utilisateurs de mettre à jour leur application, attendez qu’ils aient une expérience positive à l’intérieur avant de leur demander. Pour garder l’engagement de votre audience, évitez les envois de messages répétitifs qui peuvent sembler intrusifs.

Au fil du temps, vos utilisateurs peuvent oublier certaines fonctionnalités ou ne pas en remarquer de nouvelles. Lorsque de nouvelles fonctionnalités sont ajoutées, veillez à en informer vos utilisateurs à l'aide de [messages in-app.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) Si les utilisateurs n’interagissent pas avec des fonctionnalités fondamentales dans l’application, il peut être bon de les leur rappeler quand ils utilisent votre application et quand il existe de nouvelles fonctionnalités qui pourraient être utiles. Notre article sur l' [abonnement aux données]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) contient plus d'informations sur la manière de s'assurer que votre demande correspond aux attentes des utilisateurs en matière de flux de travail. 

## Évaluations élevées

Obtenir des évaluations à cinq étoiles dans l’App Store est le rêve de chaque spécialiste du marketing mobile. Obtenir des commentaires positifs n’est toutefois pas facile, car ils nécessitent un effort supplémentaire de la part de vos utilisateurs. En appliquant nos fonctionnalités de manière astucieuse, nous pouvons vous aider à accroître l'engagement de vos clients.

### Ciblage des utilisateurs principaux

Les utilisateurs principaux peuvent préconiser votre application. Ils interagissent souvent avec votre application régulièrement et peuvent fournir des commentaires pour l’améliorer. Bien qu’ils diffèrent entre les applications, les utilisateurs avertis ont tendance à posséder les caractéristiques suivantes :

- Avoir enregistré beaucoup de sessions
- Avoir utilisé l’application récemment
- Dépenser de l’argent et faire des achats

Pour garantir des évaluations plus élevées, demandez à vos utilisateurs principaux de noter votre application dans l’App Store étant donné qu’ils ont plus de chance d’avoir de bons commentaires à fournir. Par exemple, vous pouvez créer un segment nommé « Utilisateurs principaux » avec ces filtres :
- A utilisé ces applications plus de 10 fois au cours des 14 derniers jours
- A dépensé plus de 50 dollars

![Exemple de segmentation ciblant les utilisateurs intensifs d'une application.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Le fait de visiter l’App Store prend du temps de la part de vos utilisateurs. Pour maximiser la probabilité qu’ils fournissent cet effort supplémentaire, demandez une évaluation ou une critique après qu’ils aient eu une expérience positive avec votre application. Par exemple, demandez-leur une fois qu’ils ont battu un niveau de jeu ou effectué un achat à l’aide d’un code de réduction. Notre article sur l' [abonnement aux données]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) contient plus d'informations sur les moyens de s'assurer que votre demande correspond aux attentes des utilisateurs en matière de flux de travail.

## Planification de vos campagnes

Lorsque vous modifiez des planifications de campagne ou des audiences, tenez compte des meilleures pratiques suivantes :

- **Campagnes à planification unique :** Vous pouvez modifier la campagne jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Vous pouvez modifier la campagne jusqu'à l'heure d'envoi planifiée.
- **Campagnes d'envoi local :** Ne modifiez pas vos documents 24 heures avant l'heure d'envoi prévue.
- **Campagnes d'envoi optimales :** N'effectuez pas de modifications 24 heures avant minuit le jour où l'envoi de la campagne est planifié.

{% alert note %}
Si vous modifiez une campagne en ligne et que vous changez la réception/distribution en **heure locale**, un nouveau lot de messages sera mis en file d'attente, ce qui signifie que vos utilisateurs recevront le message deux fois en raison de la double mise en file d'attente. Pour éviter cela, arrêtez d'abord la campagne originale, puis lancez-en une copie après avoir mis à jour la planification.
{% endalert %}

