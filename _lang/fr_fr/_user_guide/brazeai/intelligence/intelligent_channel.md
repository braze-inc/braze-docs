---
nav_title: Filtre de canal
article_title: Filtre de canal intelligent
page_order: 1.5
description: "Cet article traite du filtre \"The Intelligent Channel\", un filtre qui sélectionne la partie de votre audience pour laquelle le canal d'envoi de messages sélectionné est le meilleur. Dans ce cas, le meilleur moyen a la plus grande probabilité d'engagement, compte tenu de l'historique de l'utilisateur."
search_rank: 11
---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Filtre du canal intelligent

> Le filtre `Intelligent Channel` (précédemment `Most Engaged`) sélectionne la partie de votre audience pour laquelle le canal d'envoi de messages sélectionné est leur "meilleur" canal. 

## À propos du filtre de canaux

Le filtre du canal intelligent avec un menu déroulant pour les différents canaux qui peuvent être sélectionnés.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Dans ce cas, le meilleur canal est celui qui a la plus forte probabilité d'engagement, compte tenu de l'historique de l'utilisateur. Vous pouvez sélectionner l'e-mail, le SMS, WhatsApp, le push web ou le push mobile (y compris tout OS ou appareil mobile disponible) comme canal.

Le canal intelligent calcule le taux d'engagement de chaque utilisateur pour chacun des trois canaux en prenant le rapport entre les interactions avec les messages (ouvertures ou clics) et le nombre de messages reçus au cours des six derniers mois d'activité. Les chaînes disponibles sont classées en fonction de leur taux d'engagement respectif, et la chaîne présentant le taux le plus élevé est la "plus engagée" pour cet utilisateur. 

Chaque fois qu'un message est envoyé à un utilisateur, ou qu'un utilisateur interagit avec un message, le ratio d'engagement est recalculé en quelques secondes. Un utilisateur ne peut être compté comme ayant interagi avec un message qu'une seule fois (par exemple, une ouverture et un clic sur le même e-mail feront que ce message sera marqué comme ayant été engagé une seule fois, et non deux). 

Pour activer le filtre de canal intelligent, sélectionnez le filtre de **canal intelligent** sur la page **Audiences cibles** lors de la création d'une campagne d'e-mail, de push web ou de push mobile.

{% alert important %}
Pour calculer le taux d'engagement du canal SMS, activez le [raccourcissement des liens SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) avec suivi avancé et le suivi des clics. Sans ce suivi, le SMS peut être sélectionné comme canal intelligent pour un taux d'engagement de 0 % en raison de notre [comportement de départage]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## L'option "Pas assez de données".

Pour que Braze puisse déterminer quel est le "meilleur" canal, il faut qu'il y ait suffisamment de données. Cela signifie qu'un utilisateur doit avoir reçu au moins trois messages par canal sur au moins deux des trois canaux disponibles. Les messages ne doivent pas nécessairement avoir été ouverts. 

Si les utilisateurs n'ont pas reçu suffisamment de messages à travers les canaux, ils tomberont dans l'option "Pas assez de données" de ce filtre. Cela vous permet d'utiliser n'importe lequel des trois canaux d'envoi de messages disponibles pour cibler ces utilisateurs.

Par exemple, disons que vous voulez que les utilisateurs qui préfèrent les messages push reçoivent un push et que les utilisateurs qui n'ont pas assez de données reçoivent le même message push. Dans ce cas, vous pourriez définir le filtre du canal intelligent sur **Mobile push** et utiliser **OR** pour ajouter un second filtre du canal intelligent défini sur **Not Enough Data.** Une campagne distincte, dans laquelle le filtre du canal intelligent est réglé sur l'e-mail, pourrait s'adresser aux utilisateurs qui préfèrent l'e-mail.

!Filtres de canaux intelligents pour le push mobile ou pas assez de données.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Les campagnes et les étapes du canvas qui ignorent la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ne seront pas prises en compte par le canal intelligent et ne pourront pas contribuer aux exigences en matière de données.
{% endalert %}

## L'option "Mobile push

Le push mobile intègre les canaux Android, iOS, Kindle et les autres canaux d'appareils mobiles disponibles sur Braze. Lors du calcul du canal intelligent, Braze examine chaque type d'appareil mobile séparément et choisit ensuite le taux d'engagement le plus élevé parmi eux pour représenter la catégorie "Mobile Push" lors de la comparaison avec l'e-mail et le Web push. 

Par exemple, si un utilisateur possède plusieurs appareils mobiles, son taux d'engagement mobile sera conseillé par le taux le plus élevé affiché sur l'ensemble des appareils. Cela n'obligerait toutefois pas l'utilisateur à recevoir des notifications push exclusivement sur cet appareil. Ce taux n'est utilisé que pour comparer les taux par rapport à l'e-mail et au web push.

## Canaux individuels

Plutôt que de laisser Braze choisir le meilleur canal pour un utilisateur, vous pouvez aussi vous contenter de filtrer les utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifique que vous aurez choisi. Pour cela, vous pouvez utiliser le filtre de vraisemblance de l'envoi des messages dans les [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Bonnes pratiques et stratégie d'utilisation efficace

### Rupture d'égalité

Comme certains utilisateurs recevront peu de messages, il n'est pas rare d'avoir des taux d'engagement égaux entre les canaux disponibles pour un utilisateur donné (par exemple, un utilisateur a un taux d'engagement de 0,2 à la **fois** pour l'e-mail et le push mobile). Dans ce cas, les ex aequo seront départagés en donnant la priorité (un rang plus élevé) au canal dont les événements ouverts sont les plus récents.

### Canaux inaccessibles

Lorsque l'utilisateur dispose de suffisamment de données pour qu'un classement soit déterminé, mais qu'il devient injoignable sur son canal le plus engagé, l'utilisateur "tombera" et ne recevra aucun message. Les utilisateurs qui sont injoignables sur des canaux spécifiques doivent être ciblés séparément.

### Taille de l'audience

Le canal intelligent vous permet de cibler sélectivement à l'avance la fraction d'utilisateurs qui ont une probabilité beaucoup plus élevée de s'engager avec un message que le reste de votre audience. Il est peu probable que cela conseille une majorité d'utilisateurs dans une audience typique. Vous pouvez plutôt vous attendre à ce que ce filtre trouve les 5 à 20 % de votre audience habituelle qui ont l'habitude de s'engager sur un canal particulier.


