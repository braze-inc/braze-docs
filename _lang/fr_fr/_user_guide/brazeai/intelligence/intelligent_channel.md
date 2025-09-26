---
nav_title: Filtre de canal
article_title: Filtre de canal intelligent
page_order: 1.5
description: "Le filtre de canal intelligent sélectionne la partie de votre audience pour laquelle le canal de communication sélectionné est son meilleur canal. Dans ce cas, « le meilleur » signifie celui qui a la plus forte probabilité d’engagement, compte tenu de l’historique de l’utilisateur."
search_rank: 11
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtre de canal intelligent

> Le filtre `Intelligent Channel` (précédemment `Most Engaged`) sélectionne la partie de votre audience pour laquelle le canal d'envoi de messages sélectionné est leur "meilleur" canal. 

## À propos du filtre de canaux

![Le filtre du canal intelligent avec une liste déroulante pour les différents canaux qui peuvent être sélectionnés.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Dans ce cas, « le meilleur » signifie le canal qui a la plus forte probabilité d’engagement, compte tenu de l’historique de l’utilisateur. Vous pouvez sélectionner l’e-mail, le SMS, WhatsApp, les notifications push Web ou mobile (incluant tout système d’exploitation ou appareil mobile disponible) en tant que canal.

Le canal intelligent calcule le taux d’engagement pour chaque utilisateur pour chacun des trois canaux en prenant le rapport entre les interactions avec le message (ouverture ou clics) et le nombre de messages reçus au cours des six derniers mois d’activité. Les canaux disponibles sont classés selon leurs taux d’engagement respectifs et le canal ayant le rapport le plus élevé est considéré être celui avec « Le plus d’interactions » pour cet utilisateur. 

Chaque fois qu’un message est envoyé à un utilisateur ou qu’un utilisateur interagit avec un message, le rapport d’engagement est recalculé en quelques secondes. Un utilisateur ne peut être compté comme ayant interagi avec un message qu'une seule fois (par exemple, une ouverture et un clic sur le même e-mail feront que ce message sera marqué comme ayant été engagé une seule fois, et non deux). 

Pour activer le filtre de canal intelligent, sélectionnez le filtre de **canal intelligent** sur la page **Audiences cibles** lors de la création d'une campagne d'e-mail, de push web ou de push mobile.

{% alert important %}
Pour calculer le taux d'engagement du canal SMS, activez le [raccourcissement des liens SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) avec suivi avancé et le suivi des clics. Sans ce suivi, le SMS peut être sélectionné comme canal intelligent pour un taux d'engagement de 0 % en raison de notre [comportement de départage]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## Option « Données insuffisantes »

Pour que Braze détermine quel canal est « le meilleur », il doit posséder assez de données. Cela signifie qu’un utilisateur doit avoir reçu trois messages au minimum sur au moins deux des trois canaux disponibles. Les messages n’ont pas nécessairement besoin d’avoir été ouverts. 

Si les utilisateurs n’ont pas reçu suffisamment de messages sur les différents canaux, ces utilisateurs basculeront dans l’option « Données insuffisantes » de ce filtre. Cela vous permet d’utiliser n’importe lequel des trois canaux de communication disponibles pour cibler ces utilisateurs.

Supposons par exemple que vous souhaitiez que les utilisateurs qui préfèrent des messages de notification push en reçoivent et que les utilisateurs qui ne disposent pas de données suffisantes reçoivent le même message de notification push. Dans ce cas, vous pourriez définir le filtre du canal intelligent sur **Mobile push** et utiliser **OR** pour ajouter un second filtre du canal intelligent défini sur **Not Enough Data.** Une campagne séparée avec le filtre de canal intelligent réglé sur l’envoi par e-mail peut traiter les utilisateurs qui préfèrent recevoir un e-mail.

![Filtres de canaux intelligents pour le push mobile ou pas assez de données.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Les campagnes et les étapes du canvas qui ignorent la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ne seront pas prises en compte par le canal intelligent et ne pourront pas contribuer aux exigences en matière de données.
{% endalert %}

## Option « Notification push mobile »

La notification push mobile intègre Android, iOS, Kindle ainsi que les autres canaux d’appareils mobiles disponibles sur Braze. Lors du calcul du canal intelligent, Braze examine chaque type d’appareil mobile séparément puis choisit le taux d’engagement le plus élevé parmi eux pour représenter la catégorie « Notification push mobile » lors de la comparaison entre l’e-mail et la notification push Web. 

Par exemple, si un utilisateur dispose de plusieurs appareils mobiles, son taux d’engagement mobile serait représenté par le taux le plus élevé affiché parmi les appareils. Cependant, il n’est pas possible de forcer l’utilisateur à recevoir des notifications push exclusivement sur cet appareil. Ce taux est uniquement utilisé lors de la comparaison des taux entre e-mail et notification push Web.

## Canaux individuels

Plutôt que de laisser Braze choisir le meilleur canal pour un utilisateur, vous pouvez aussi vous contenter de filtrer les utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifique que vous aurez choisi. Pour cela, vous pouvez utiliser le filtre Probabilité d’ouverture des messages dans les [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood).

## Bonnes pratiques et stratégie d’utilisation efficace

### Départager les égalités

Comme certains utilisateurs recevront peu de messages, il n'est pas rare d'avoir des taux d'engagement égaux entre les canaux disponibles pour un utilisateur donné (par exemple, un utilisateur a un taux d'engagement de 0,2 à la **fois** pour l'e-mail et le push mobile). Dans ce cas, les liens seront divisés en priorisant (en donnant un classement plus élevé) au canal avec les événements ouverts les plus récents.

### Canaux inaccessibles

Lorsque l’utilisateur dispose de suffisamment de données pour déterminer un classement, mais qu’il devient inaccessible sur son « canal le plus engagé », l’utilisateur va « sortir » et ne recevra aucun message. Les utilisateurs inaccessibles sur des canaux spécifiques doivent être ciblés séparément.

### Dimensionnement de l’audience

Le canal intelligent vous permet de cibler de manière sélective et en avance la part des utilisateurs qui ont une probabilité beaucoup plus élevée d’interagir avec un message que le reste de votre audience. Cela ne représente probablement pas la majorité des utilisateurs d’une audience typique. Au contraire, vous pouvez vous attendre à ce que ce filtre trouve que 5 à 20 % de votre audience habituelle on un bilan clair d’engagement sur un canal particulier.


