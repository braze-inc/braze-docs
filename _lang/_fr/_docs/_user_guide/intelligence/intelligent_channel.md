---
nav_title: Canal Intelligent
article_title: Filtre de canal intelligent
page_order: 0
description: "Le filtre Canal Intelligent sélectionne la portion de votre auditoire pour laquelle le canal de messagerie sélectionné est leur meilleur canal. Dans ce cas, les meilleurs moyens ont la plus grande probabilité d'engagement, compte tenu de l'historique de l'utilisateur."
---

# Filtre de canal intelligent

> Cet article décrit le filtre de la Chaîne Intelligente et fournit les meilleures pratiques pour utiliser efficacement cette fonctionnalité. Pour en savoir plus sur ce qu'est le canal intelligent, comment il fonctionne, ses avantages, reportez-vous à notre cours LAB [Intelligent Channel](https://lab.braze.com/most-engaged-channel).

Le filtre Intelligent ou `Canal` le plus engagé sélectionne la portion de votre public pour laquelle le canal de messagerie sélectionné est leur « meilleur» canal. Dans ce cas, "le meilleur" désigne le canal qui a la plus grande probabilité d'engagement, compte tenu de l'historique de l'utilisateur. Vous pouvez sélectionner le courrier électronique, le Web push, ou la push mobile (y compris tout système d'exploitation mobile ou appareil disponible) en tant que canal.

!\[Intelligent Channel filter\]\[1\]{: style="float:right;max-width:50%;margin-left:10px;margin-top:10px;border:0"}

Le canal Intelligent calcule le taux d'engagement de chaque utilisateur pour chacun des trois canaux en prenant le ratio d'interactions de messages (ouverture ou clics) par rapport au nombre de messages reçus au cours des six derniers mois d'activité. Les canaux disponibles sont classés en fonction de leurs ratios d'engagement respectifs, et le canal avec le plus grand ratio est le "plus âgé" pour cet utilisateur.

Chaque fois qu'un message est envoyé à un utilisateur ou qu'un utilisateur interagit avec un message, le canal intelligent est recalculé en quelques secondes. Toute interaction avec un message ne peut être considérée comme "interagissant avec" qu'une seule fois (par ex. une ouverture et un clic sur le même courriel feront que ce message sera marqué comme ayant été engagé avec une seule fois, pas deux fois).

Pour activer le filtre du canal intelligent, sélectionnez le filtre **Canal Intelligent** sur la page **Utilisateurs cibles** lors de la création d'un e-mail, Web push, ou campagne de push mobile.

## L'option "Pas assez de données"

Pour que Braze détermine quel canal est le « meilleur », il doit y avoir des données adéquates. Cela signifie qu'un utilisateur doit avoir reçu au moins trois messages ou plus sur au moins deux des trois canaux disponibles. Les messages n'ont pas nécessairement besoin d'être ouverts.

Si les utilisateurs n'ont pas reçu suffisamment de messages sur les canaux, ces utilisateurs entreront dans l'option "Données insuffisantes" de ce filtre. Cela vous permet d'utiliser l'un des trois canaux de messagerie disponibles pour cibler ces utilisateurs.

Par exemple, supposons que vous voulez que les utilisateurs qui préfèrent les messages push reçoivent un push et que les utilisateurs qui n'ont pas assez de données pour recevoir le même message push. Dans ce cas, vous pouvez définir le filtre du canal intelligent à **Mobile** et utiliser **OU** pour ajouter un second filtre du canal intelligent à **Données insuffisantes**. Une campagne séparée avec le filtre de canal intelligent défini sur l'email pourrait cibler les utilisateurs qui préfèrent l'email.<br>!\[Intelligent Channel exemple\]\[2\]

{% alert note %}
Campagnes et pas de Canvas qui ignorent le [plafonnement de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ne seront pas comptabilisés par le canal intelligent et ne peuvent pas contribuer aux exigences de données ci-dessus.
{% endalert %}

## L'option "Mobile push"

Mobile push intègre Android, iOS, Windows, Kindle et d'autres canaux mobiles disponibles sur Braze. Lors du calcul du canal intelligent, Braze regarde chaque type d'appareil mobile séparément et choisit ensuite le taux d'engagement le plus élevé parmi eux pour représenter la catégorie "Mobile Push" lors de la comparaison avec le courrier électronique et Web Push.

Par exemple, si un utilisateur a plusieurs appareils mobiles, leur taux d'engagement mobile serait représenté par le taux le plus élevé affiché sur tous les appareils. Cela ne forcerait toutefois pas l'utilisateur à recevoir des notifications push exclusivement sur cet appareil. Ce tarif n'est utilisé que lorsque vous comparez les tarifs avec les messages électroniques et les messages push sur le Web.

## Meilleures pratiques et stratégie d'utilisation efficace

### Délimité

Parce que certains utilisateurs auront un faible nombre de messages reçus, Il n'est pas rare d'avoir des "liens" dans les taux d'engagement sur les canaux disponibles pour un utilisateur donné (i. ., un seul utilisateur a un taux d'engagement de 0,2 pour **à la fois** email et push mobile. Dans de tels cas, les liens seront rompus en priorisant (donnant un rang supérieur à) le canal avec les événements ouverts les plus récents.

### Chaînes injoignables

Quand l'utilisateur a suffisamment de données pour qu'un classement soit déterminé mais devient inaccessible sur son "Canal Intelligent", l'utilisateur "tombera" et ne recevra aucun message. Les utilisateurs qui ne sont pas joignables sur certains canaux doivent être ciblés séparément.

### Taille de l'audience

Le canal intelligent vous permet de cibler sélectivement à l'avance la fraction d'utilisateurs qui ont une probabilité beaucoup plus élevée de s'engager avec un message que le reste de votre public. Il est peu probable que cela représente une majorité d'utilisateurs dans un public typique. Au contraire, vous pouvez vous attendre à ce que ce filtre trouve les 5-20% de votre public habituel qui ont un record établi de s'engager sur un canal particulier.
[1]: {% image_buster /assets/img/intelligent_channel_filter.png %} "Filtre de canal intelligent" [2]: {% image_buster /assets/img/intelligent_example.png %}