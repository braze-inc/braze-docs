---
nav_title: Filtre de canal
article_title: Filtre Canal intelligent
page_order: 1.5
description: "Cet article décrit le filtre Canal intelligent, qui sélectionne la partie de votre audience pour laquelle le canal de messagerie choisi est leur « meilleur » canal. Ici, « meilleur » signifie la plus forte probabilité d'engagement selon l'historique de l'utilisateur."
search_rank: 11
---

# [![Cours Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filtre Canal intelligent

> Le filtre **Canal intelligent** (anciennement **Most Engaged**) sélectionne la partie de votre audience pour laquelle le canal de messagerie choisi est leur « meilleur » canal.

## À propos du filtre de canal

![Le filtre Canal intelligent avec un menu déroulant des différents canaux sélectionnables.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

Ici, « meilleur » signifie le canal qui a la plus forte probabilité d'engagement selon l'historique de l'utilisateur. Vous pouvez choisir l'e-mail, le SMS, WhatsApp, le push web ou le push mobile (y compris tout OS ou appareil mobile disponible) comme canal.

Le canal intelligent calcule le taux d'engagement pour chaque utilisateur et chaque canal disponible en prenant le ratio des interactions avec les messages (ouvertures ou clics) au nombre de messages reçus sur les six derniers mois. Les canaux sont classés selon leurs taux d'engagement respectifs, et le canal avec le ratio le plus élevé est le « Most Engaged » pour cet utilisateur.

Chaque fois qu'un message est envoyé à un utilisateur ou qu'un utilisateur interagit avec un message, le taux d'engagement est recalculé en quelques secondes. Un utilisateur ne peut être compté comme ayant interagi avec un message qu'une seule fois (par ex., une ouverture et un clic sur le même e-mail = une seule interaction).

Pour activer le filtre Canal intelligent, sélectionnez le filtre **Canal intelligent** sur la page **Audiences cibles** lors de la création d'une campagne e-mail, push web ou push mobile.

{% alert important %}
Pour calculer le taux d'engagement du canal SMS, activez le [raccourcissement de lien SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) avec suivi avancé et suivi des clics. Sans ce suivi, le SMS peut être sélectionné comme canal intelligent avec un taux d'engagement de 0 % en raison de notre [comportement de départage]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#tie-breaking).
{% endalert %}

## Option « Données insuffisantes »

Pour que Braze détermine quel canal est « meilleur », il faut suffisamment de données : un utilisateur doit avoir reçu au moins trois messages par canal sur au moins deux des trois canaux disponibles (les messages n'ont pas besoin d'avoir été ouverts).

Les utilisateurs n'ayant pas reçu assez de messages sur les canaux entrent dans l'option « Données insuffisantes » de ce filtre. Vous pouvez alors utiliser l'un des trois canaux pour cibler ces utilisateurs.

Par exemple, pour envoyer un push aux utilisateurs qui préfèrent le push et le même push aux utilisateurs sans assez de données : définissez le filtre Canal intelligent sur **Push mobile** et ajoutez avec **OR** un second filtre Canal intelligent réglé sur **Données insuffisantes**. Une campagne séparée avec le filtre Canal intelligent sur e-mail peut cibler les utilisateurs qui préfèrent l'e-mail.

![Filtres Canal intelligent pour push mobile ou données insuffisantes.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Les campagnes et étapes Canvas qui ignorent la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ne sont pas prises en compte par le canal intelligent et ne contribuent pas aux exigences de données.
{% endalert %}

Pour les bonnes pratiques sur le départage, les canaux inaccessibles et la taille d'audience, consultez la version complète de cet article dans le sommaire à gauche ou l'aide du tableau de bord Braze.
