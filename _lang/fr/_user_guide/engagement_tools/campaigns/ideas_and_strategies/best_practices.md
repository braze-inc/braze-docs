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

- **Cibler** vos audiences en créant des [segments d’audience]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Déclencher** vos messages avec une livraison [par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou [déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Modéliser** et personnaliser vos messages avec une [logique conditionnelle Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Suivre** l’efficacité de vos campagnes avec le [suivi de conversions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events?redirected=true#conversion-events).

Ceci vous permettra d’optimiser les données que vous enverrez à Braze et de simplifier votre capacité à envoyer des messages à vos utilisateurs en vous prémunissant contre le suivi de points de données pouvant ne pas être utiles à votre équipe sur le long terme. 

## Ciblage des utilisateurs

Au fur et à mesure que vous construisez vos campagnes, vous pourriez constater des défaillances de vos audiences. À ce moment crucial, vous pouvez cibler vos [utilisateurs inactifs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) avec une campagne spécialisée en utilisant la segmentation. 

### Identifiez votre audience

Utilisez à votre avantage les segments et les filtres en définissant votre audience. Considérez les utilisateurs ciblés par votre campagne et vos messages. Avec ces informations clés, vous pouvez créer des [campagnes multicanales]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) qui donnent la flexibilité nécessaire pour construire vos messages dans différents canaux pour vous conformer aux préférences de notification de votre audience.

Il est également important de comprendre vos [utilisateurs actifs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) pour montrer que vous appréciez ceux qui sont réguliers.

## Campagnes multicanales

### Connaissance des fonctionnalités

Si votre objectif est d’attirer vos utilisateurs vers une nouvelle fonctionnalité ou une nouvelle version de l’application, utilisez une stratégie multicanale en vous concentrant sur les canaux in-app. Les [messages in-app][5] et les [cartes de contenu][7] perturbent moins si l’utilisateur ne souhaite pas mettre à jour immédiatement. Assurez-vous d’inclure des [liens profonds]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers l’App Store approprié.

Il peut être difficile de persuader les utilisateurs de mettre à jour leur application ou modifier l’utilisation qu’ils en font. Faites-leur donc comprendre les avantages de la nouvelle version ou fonctionnalité et en quoi elle améliorera leur expérience avec votre application. 

### Timing d’envoi

Le timing est la clé ! Lorsque votre objectif est de convaincre les utilisateurs de mettre à jour leur application, attendez qu’ils aient une expérience positive à l’intérieur avant de leur demander. Pour garder l’engagement de votre audience, évitez les envois de messages répétitifs qui peuvent sembler intrusifs.

Au fil du temps, vos utilisateurs peuvent oublier certaines fonctionnalités ou ne pas en remarquer de nouvelles. Lorsque de nouvelles fonctionnalités sont ajoutées, assurez-vous de prévenir vos utilisateurs avec des [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Si les utilisateurs n’interagissent pas avec des fonctionnalités fondamentales dans l’application, il peut être bon de les leur rappeler quand ils utilisent votre application et quand il existe de nouvelles fonctionnalités qui pourraient être utiles. Notre article sur les [données d’abonnement][7] contient de plus amples informations sur les manières de garantir que votre demande est conforme aux attentes des utilisateurs en matière de flux de travail. 

## Évaluations élevées

Obtenir des évaluations à cinq étoiles dans l’App Store est le rêve de chaque marketeur mobile. Obtenir des commentaires positifs n’est toutefois pas facile, car ils nécessitent un effort supplémentaire de la part de vos utilisateurs. En utilisant de façon intelligente la fonctionnalité de Braze, nous pouvons vous aider à augmenter votre engagement client.

### Ciblage des utilisateurs principaux

Les utilisateurs principaux peuvent préconiser votre application. Ils interagissent souvent avec votre application régulièrement et peuvent fournir des commentaires pour l’améliorer. Bien qu’ils diffèrent entre les applications, les utilisateurs avertis ont tendance à posséder les caractéristiques suivantes :

- Avoir enregistré beaucoup de sessions
- Avoir utilisé l’application récemment
- Dépenser de l’argent et faire des achats

Pour garantir des évaluations plus élevées, demandez à vos utilisateurs principaux de noter votre application dans l’App Store étant donné qu’ils ont plus de chance d’avoir de bons commentaires à fournir. Par exemple, vous pouvez créer un segment nommé « Utilisateurs principaux » avec ces filtres :
- A utilisé ces applications plus de 10 fois au cours des 14 derniers jours
- A dépensé plus de 50 dollars

![][6]

Le fait de visiter l’App Store prend du temps de la part de vos utilisateurs. Pour maximiser la probabilité qu’ils fournissent cet effort supplémentaire, demandez une évaluation ou une critique après qu’ils aient eu une expérience positive avec votre application. Par exemple, demandez-leur une fois qu’ils ont battu un niveau de jeu ou effectué un achat à l’aide d’un code de réduction. Notre article sur les [données d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) contient de plus amples informations sur les manières de garantir que votre demande est conforme aux attentes des utilisateurs en matière de flux de travail.


[6]: {% image_buster /assets/img_archive/ratings_power_users.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/