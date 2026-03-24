---
nav_title: De retour en stock
article_title: En stock
page_order: 2
page_type: reference
description: "Cet article explique comment utiliser un modèle Braze Canvas pour stimuler les achats en informant vos utilisateurs lorsqu'un article est de nouveau disponible en stock grâce à l'envoi de messages personnalisés."
tool: Canvas
---

# De retour en stock

> Veuillez utiliser le modèle « De nouveau en stock » pour créer des messages destinés aux utilisateurs qui ont précédemment consulté ou manifesté leur intérêt pour un article qui était en rupture de stock, mais qui est désormais disponible à l'achat. Cela permet aux utilisateurs d'obtenir les produits qu'ils souhaitent en les informant au moment crucial où un produit redevient disponible.

Cet article vous guidera à travers un cas d'utilisation du modèle **« Back In Stock** » (De nouveau en stock), conçu pour l'étape de conversion du cycle de vie de l'utilisateur. Une fois terminé, vous aurez créé un canvas qui enverra une notification push (web ou mobile), un SMS ou un e-mail aux utilisateurs lorsqu'un article sera de nouveau en stock, ainsi que jusqu'à deux rappels.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) contenant des informations sur votre article
- [Les notifications de réapprovisionnement]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) doivent être configurées pour l'article concernant lequel vous souhaitez envoyer des messages aux utilisateurs.

## Adapter le modèle à vos besoins

Supposons que nous travaillons pour PantsLabyrinth, un détaillant de vêtements en vente directe aux consommateurs, spécialisé dans les pantalons, les jeans, les jupes-culottes et de nombreux autres types de pantalons. Nous pouvons utiliser le modèle « De nouveau en stock » pour informer nos clients sur divers canaux lorsqu'un modèle de jeans très prisé, le Classic Straight Leg, est de nouveau disponible.

Avant de créer le canvas, nous [avons établi un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) contenant des informations sur notre stock de pantalons à coupe droite et [configuré des notifications de réapprovisionnement]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) pour les jeans Classic Straight Leg. Nous avons fait en sorte que les utilisateurs s'abonnent aux notifications après avoir effectué l'événement personnalisé consistant à ajouter le jean Classic Straight Leg à leurs favoris dans l'application.

Pour accéder au modèle « De retour en stock », lorsque vous créez un nouveau canvas, veuillez sélectionner **« Utiliser un modèle de canvas** » > **« Modèles Braze** ». Ensuite, à côté de **« De nouveau en stock** », veuillez sélectionner **« Appliquer le modèle** ». Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

![Le titre et la description actuels du canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Veuillez mettre à jour le nom du canvas afin d'indiquer qu'il est destiné au ciblage des utilisateurs lorsque notre produit Classic Straight Leg sera de nouveau disponible.
3\. Mettez à jour la description pour expliquer que ce canvas contient des messages personnalisés.
4\. Veuillez ajouter l'étiquette **« De nouveau en stock** », qui est imbriquée sous l'étiquette **« Promotionnel »**, afin que nous puissions la filtrer sur la page d'accueil de canvas. 

![Étape « Configurer les détails du canvas » avec le nom de canvas « De retour en stock - Jambe droite classique » et une brève description du canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Étape 2 : Attribuer des événements de conversion

Modifiez l'**événement de conversion principal - A** pour **effectuer un achat spécifique** et sélectionnez **« Classic Straight Leg** » comme nom du produit.

![Section « Attribuer des événements de conversion » pour le type d'événement de conversion « Achat du produit Classic Straight Leg » avec un délai de conversion de 7 jours.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Étape 3 : Adapter la planification de l'entrée

Veuillez conserver la planification des entrées basée sur **les actions** afin que les utilisateurs accèdent à notre canvas lorsqu'ils effectuent une action, ce qui est déjà défini dans le modèle sous « **Effectuer un événement de retour en stock** ».

Nous apporterons deux modifications à cette étape :

1. Veuillez sélectionner le catalogue contenant les informations relatives à notre jean classique à coupe droite, que nous avons nommé « pantalon à coupe droite ». 

![Étape de "planification de l'entrée" pour un Canvas basé sur l'action.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. Veuillez définir l'**heure** **de début (obligatoire)** à la date et l'heure souhaitées.

![Section "Fenêtre d'entrée" avec une heure de début fixée au 2 janvier 2025 à 12 heures.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Étape 4 : Sélectionner l'audience cible

Nous définirons notre audience cible comme étant les utilisateurs qui, selon nous, sont les plus susceptibles d'acheter le jean Classic Straight Leg.

1. Veuillez sélectionner notre segment cible « Favoris - Jeans classiques à coupe droite », qui comprend les utilisateurs ayant ajouté nos jeans classiques à coupe droite à leurs favoris sur notre application ou notre site Web.
2. Veuillez sélectionner un filtre pour inclure les utilisateurs ayant acheté des « jeans » plus de « 0 » fois.

![Étape « Public cible » avec le segment « Favoris - Jeans classiques à coupe droite ».]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. Veuillez ajuster les contrôles d'entrée afin de permettre aux utilisateurs de revenir dans le Canvas après la durée maximale de celui-ci, afin d'éviter que les utilisateurs ne déclenchent la même étape simultanément.

![Section « Contrôles d'accès » avec une case à cocher permettant aux utilisateurs de revenir sur ce canvas pendant une durée maximale.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. Veuillez ajuster les critères de sortie afin d'exclure les utilisateurs qui ont effectué l'événement personnalisé consistant à retirer le jean Classic Straight Leg de leurs favoris.

![Section « Critères de sortie » avec une exception pour les utilisateurs qui effectuent l'événement personnalisé « Supprimer des favoris ».]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Étape 5 : Sélectionner vos paramètres d’envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

![Étape « Envoyer les paramètres » avec ciblage sur les utilisateurs abonnés ou ayant donné leur consentement.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre Canvas en personnalisant les canaux et les contenus qui seront envoyés aux utilisateurs. Étant donné que nous utilisons les quatre canaux du modèle (push mobile et web, SMS et e-mail) et que nous utilisons le [canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), il n'est pas nécessaire d'en ajouter ou d'en supprimer.

{% alert tip %}
Vous pouvez utiliser [les propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour personnaliser les messages dans votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

Nous commencerons notre personnalisation en passant en revue chaque étape du message afin de mettre à jour le contenu.

1. Veuillez remplacer`!!YOURCATALOGHERE!!`par le nom de notre catalogue. (“Straight_Leg_Pants”).
2. Veuillez remplacer`[0]`par le numéro d'index du jean Classic Straight Leg, qui est « 9 » car ce jean est le dixième article dans le`items`tableau de notre catalogue. (Les tableaux sont indexés à partir de zéro dans liquid, donc le premier élément est`0`  et non `1`.)
3. Veuillez répéter les étapes 1 et 2 pour toutes les étapes restantes du message, y compris :
    - Le message&« E-mail intégré au produit » envoyé après un délai d'un jour
    - Les messages « Push+e-mail Alert » envoyés aux utilisateurs qui n'ont pas effectué d'achat
4. Veuillez mettre à jour l'étape Parcours d’action en sélectionnant le groupe d’actions **Achat**. Ensuite, veuillez sélectionner **« Effectuer un achat spécifique** » et choisir le jean « Classic Straight Leg » comme produit.

![Étape du canvas Mobile Push avec un message informant les utilisateurs qu'un produit est de nouveau disponible.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour s'assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Lancer le canvas.** Désormais, nos utilisateurs qui ont ajouté notre jean Classic Straight Leg à leurs favoris et qui se sont abonnés à nos canaux de communication recevront des notifications lorsqu'il sera de nouveau disponible.

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}

