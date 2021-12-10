---
nav_title: Canal Intelligent
article_title: Filtre de canal intelligent
page_order: 0
description: "Le filtre Canal Intelligent sélectionne la portion de votre auditoire pour laquelle le canal de messagerie sélectionné est leur meilleur canal. Dans ce cas, les meilleurs moyens ont la plus grande probabilité d'engagement, compte tenu de l'historique de l'utilisateur."
---

# Filtre de canal intelligent

Le filtre de canal Intelligent, ou "Le plus engagé", sélectionne la portion de votre auditoire pour laquelle le canal de messagerie sélectionné est leur "meilleur". Dans ce cas, "meilleur" signifie "a la plus grande probabilité d'engagement, compte tenu de l'histoire de l'utilisateur". Vous pouvez sélectionner Email, Web Push, ou Mobile Push (qui comprend tout système d'exploitation ou appareil mobile disponible) comme chaîne. !\[Intelligent Channel Filter\]\[1\]{: style="float:right;max-width:60%;margin-left:10px;margin-top:10px"}

Le canal Intelligent calcule le taux d'engagement de chaque utilisateur pour chacun des trois canaux en prenant le ratio d'interactions de messages (ouverture ou clics) par rapport au nombre de messages reçus au cours des 6 derniers mois d'activité. Les canaux disponibles sont classés en fonction de leurs ratios d'engagement respectifs, et le canal avec le plus haut ratio est le "Plus Engagé" pour cet utilisateur. Chaque fois qu'un message est envoyé à un utilisateur et chaque fois qu'il interagit avec un message, le canal intelligent est actualisé en quelques secondes. Toute interaction avec un message ne peut être considérée comme "interagissant avec" qu'une seule fois, par ex. une ouverture et un clic sur le même courriel feront que ce message sera marqué comme ayant été engagé avec une seule fois, pas deux fois.

## L'option "pas assez de données"

Pour que Braze détermine quel canal est le « meilleur », il doit y avoir des données adéquates. Cela signifie qu'un utilisateur doit avoir reçu au moins trois (3) messages ou plus sur au moins deux (2) des trois (3) canaux disponibles. Les messages n'ont pas nécessairement besoin d'être ouverts.

Donc, si un utilisateur n'a que des données pour un (1) canal, ou moins de trois (3) messages reçus sur deux (2) ou trois (3) canaux, cet utilisateur sera alors sous l'option "Données insuffisantes" de ce filtre. Cela vous permettra de choisir d'utiliser le canal de messagerie que vous souhaitez pour les utilisateurs qui n'ont pas de "canal intelligent" calculé de manière fiable.

Par exemple, si vous voulez que les utilisateurs qui préfèrent _les messages push_ reçoivent un push, ainsi que les utilisateurs pour lesquels il n'y a pas assez de données pour recevoir le même message push, vous pouvez définir le filtre "Intelligent Channel" comme "Mobile" et utiliser __OU__ pour ajouter un second filtre "Intelligent Channel" à "Not Enough Data". De cette façon, les utilisateurs qui préfèrent push recevront aussi bien qu'un utilisateur pour qui il n'y a pas assez de données à savoir. Une campagne séparée avec le filtre le plus Engagé réglé sur "Email" pourrait cibler les utilisateurs qui préfèrent le courriel.

{% alert note %}
Campagnes et pas de Canvas qui ignorent le [plafonnement de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ne seront pas comptabilisés par le canal intelligent et ne peuvent pas contribuer aux exigences de données ci-dessus.
{% endalert %}

## L'option "Push mobile"

Mobile Push intègre Android, iOS, Windows, Kindle et tous les autres canaux mobiles disponibles sur Brésil. Lors de l'informatique du canal intelligent, Braze regarde chaque type d'appareil mobile séparément, mais choisit ensuite le taux d'engagement le plus élevé parmi eux pour représenter la catégorie "Mobile Push" lors de la comparaison avec le courrier électronique et Web Push. Donc un utilisateur avec un iPhone, téléphone Android, et iPad avec des taux d'engagement de 0,1, 0.2, et 0. 5, respectivement, aurait leur taux d'engagement Mobile Push être calculé comme le meilleur de tous ces appareils : 0,45. Mais cela ne serait pas le cas. forcer cet utilisateur à recevoir des notifications Push sur l’iPad — elles peuvent toujours être considérées comme préférant “Pousser Mobile” même lorsque vous utilisez le filtre sur un message push Android.

## Meilleures pratiques et stratégie d'utilisation efficace

### Délimité

Parce que certains utilisateurs auront un faible nombre de messages reçus, Il n'est pas rare d'avoir des "liens" dans les taux d'engagement sur les canaux disponibles pour un seul utilisateur donné (un seul utilisateur a un 0. Taux d'engagement pour __à la fois__ Email et Mobile Push). Dans de tels cas, les liens seront rompus en priorisant (donnant un rang supérieur à) le canal avec les événements ouverts les plus récents.

### Chaînes injoignables

Quand l'utilisateur a suffisamment de données pour qu'un classement soit déterminé mais devient inaccessible sur son "Canal Intelligent", l'utilisateur "tombera" et ne recevra aucun message. Les utilisateurs qui ne sont pas joignables sur certains canaux doivent être ciblés séparément.

### Taille de l'audience

Le canal intelligent vous permet de cibler sélectivement à l'avance la fraction d'utilisateurs qui ont une probabilité beaucoup plus élevée de s'engager avec un message que le reste de votre public. Il est peu probable que cela représente une majorité d'utilisateurs dans un public typique. Au contraire, vous pouvez vous attendre à ce que ce filtre trouve les 5-20% de votre public habituel qui ont un record établi de s'engager sur un canal particulier.
[1]: {% image_buster /assets/img/intelligent_channel_filter.png %} "Filtre de canal intelligent"
