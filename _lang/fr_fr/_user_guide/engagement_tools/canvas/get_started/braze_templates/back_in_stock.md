---
nav_title: En stock
article_title: En stock
page_order: 2
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour stimuler les achats en notifiant vos utilisateurs lorsqu'un article est de nouveau en stock avec un envoi de messages personnalisés."
tool: Canvas
---

# En stock

> Utilisez le modèle de retour en stock pour créer des messages ciblant les utilisateurs qui ont déjà consulté ou manifesté de l'intérêt pour un article qui était en rupture de stock mais qui est désormais disponible à l'achat. Cela aide les utilisateurs à obtenir les produits qu'ils souhaitent en les engageant au moment critique où un produit redevient disponible.

Cet article vous présente un cas d'utilisation du modèle **Retour en stock**, conçu pour l'étape de conversion du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui envoie un push (web ou mobile), un SMS ou un e-mail aux utilisateurs lorsqu'un article est de nouveau en stock, et jusqu'à deux rappels.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) contenant des informations sur votre article
- Les [notifications de rupture de stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) doivent être configurées pour l'article au sujet duquel vous souhaitez envoyer des messages aux utilisateurs.

## Adapter le modèle à vos besoins

Imaginons que nous travaillions pour PantsLabyrinth, un détaillant de vêtements en vente directe au consommateur, spécialisé dans les pantalons, les jeans, les jupes-culottes et bien d'autres types de pantalons. Nous pouvons utiliser le modèle de retour en stock pour informer les clients sur différents canaux qu'une paire de jeans populaire, la Classic Straight Leg, est de nouveau en stock.

Avant de créer le Canvas, nous avons mis en [place un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) qui contient des informations sur notre stock de pantalons à jambe droite et [configuré des notifications de rupture de stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) pour les jeans Classic Straight Leg. Nous avons fait en sorte que les utilisateurs s'abonnent aux notifications après avoir réalisé l'événement personnalisé consistant à favoriser le jean Classic Straight Leg sur l'application.

Pour accéder au modèle en stock, lorsque vous créez une nouvelle toile, sélectionnez **Utiliser un modèle de toile** > **Modèles de Braze**. Ensuite, à côté de **Retour en stock**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Mettez à jour le nom du canvas pour spécifier que le canvas est destiné au ciblage des utilisateurs lorsque notre produit Classic Straight Leg est de nouveau en stock.
3\. Mettez à jour la description pour expliquer que ce canvas contient des messages personnalisés.
4\. Ajoutez le tag **Back in Stock**, qui est imbriqué dans le tag **Promotional**, afin que nous puissions le filtrer sur la page d'accueil de Canvas. 

\!["Set Up Canvas Details" étape du canvas avec un nom de canvas "Back in Stock - Classic Straight Leg" et une brève description du canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Étape 2 : Attribuer des événements de conversion

Modifiez l'**événement de conversion principal - A** en **Effectuer un achat spécifique** et sélectionnez **Jambes droites classiques** pour le nom du produit.

!section "Attribuer des événements de conversion" pour le type d'événement de conversion de l'achat du produit Classic Straight Leg avec une date limite de conversion de 7 jours.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Étape 3 : Adapter la planification de l'entrée

Gardons la planification d'entrée **basée sur l'action** pour que les utilisateurs entrent dans notre canvas lorsqu'ils effectuent une action, que le modèle a déjà définie comme **Effectuer un événement de retour en stock**.

Nous allons apporter deux Adjust à cette étape :

1. Sélectionnez le catalogue qui contient des informations sur nos jeans classiques à jambe droite, que nous avons appelés "Pantalons à jambe droite". 

\!["Planification de l'entrée" pour une étape du canvas basée sur l'action.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. Réglez l'**heure de début (obligatoire)** sur la date et l'heure de début souhaitées.

\!["Fenêtre d'inscription"] avec une heure de début fixée au 2 janvier 2025 à 12 heures.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Étape 4 : Sélectionner l'audience ciblée

Nous définirons notre audience cible comme les utilisateurs qui, selon nous, sont les plus susceptibles d'acheter le jean classique à jambe droite.

1. Sélectionnez notre segmentation cible, "Favorisé - Jeans classiques à jambe droite", qui se compose des utilisateurs qui ont favorisé nos jeans classiques à jambe droite sur notre appli ou notre site web.
2. Sélectionnez un filtre pour inclure les utilisateurs qui ont acheté "Jeans" plus de "0" fois.

\!["Target Audience" step avec le segment "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. Adjust the entry controls to allow users to re-enter the Canvas after the Canvas's maximum duration, to prevent the likelihood of users triggering the same step concurrently.

\!["Contrôle d'entrée" section avec une case à cocher pour permettre aux utilisateurs d'entrer à nouveau dans ce Canvas avec une durée maximale du Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. Adjust the exit criteria to remove users who performed the custom event of unfavouriting the Classic Straight Leg jeans.

\!["Critères de sortie" avec une exception pour les utilisateurs qui effectuent l'événement personnalisé "Défavorable".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

\!["Paramètres d'envoi" étape de ciblage des utilisateurs qui sont abonnés ou opt-in.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre Canvas en personnalisant les canaux et les contenus qui seront envoyés aux utilisateurs. Comme nous utilisons les quatre canaux du modèle (push mobile et web, SMS et e-mail) et que nous utilisons le filtre de [canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), nous n'avons pas besoin d'en ajouter ou d'en supprimer.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée du Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

Nous allons commencer notre personnalisation en passant par chaque étape du message pour mettre à jour le contenu.

1. Remplacez `!!YOURCATALOGHERE!!` par le nom de notre catalogue (“Straight_Leg_Pants”).
2. Remplacez `[0]` par le numéro d'index du jean Classic Straight Leg, qui est "9" parce que le jean est le dixième article du tableau `items` de notre catalogue. (Les tableaux sont indexés par zéro dans Liquid, de sorte que le premier élément est `0` et non `1`).
3. Répétez les étapes 1 et 2 pour toutes les étapes restantes de l'envoi de messages, y compris :
    - Le message "In-Product Msg & Email" qui est envoyé après le délai d'un jour.
    - Les messages "Push+Email Alert" qui sont envoyés aux utilisateurs qui n'ont pas effectué d'achat.
4. Mettez à jour l'étape Parcours d'action en sélectionnant le groupe d'action **Achat**. Ensuite, sélectionnez **Faire un achat spécifique** et choisissez Jean classique à jambe droite pour le produit.

\![Mobile Push Canvas étape avec un message informant les utilisateurs qu'un produit est de nouveau en stock.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour s'assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Lancer le canvas.** Désormais, nos utilisateurs qui ont favorisé nos jeans classiques à jambe droite et se sont abonnés à nos canaux de communication recevront des notifications lorsqu'ils seront de nouveau en stock !

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}

