---
nav_title: Abandon de panier
article_title: Abandon de panier
page_order: 1
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour dialoguer avec les utilisateurs en temps réel afin de les inciter à finaliser leurs achats."
tool: Canvas
---

# Abandon de panier

> Dialoguez avec les utilisateurs en temps réel pour les encourager à terminer leurs achats. Utilisez ce modèle pour créer un parcours utilisateur axé sur l'envoi de messages personnalisés en temps opportun qui rappellent aux utilisateurs leurs paniers abandonnés en mettant en avant les avantages du produit et en proposant des incitations, telles que des codes de réduction.

Dans cet article, nous allons vous présenter un cas d'utilisation du modèle d' **intention abandonnée**, qui est destiné à l'étape de considération du cycle de vie de l'utilisateur. À l'issue de cet article, vous aurez personnalisé un parcours client qui encourage les achats des utilisateurs qui n'ont pas effectué d'achats après avoir ajouté des articles à leur panier.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un canevas distinct de parcours de l'utilisateur après l'achat, car le fait d'effectuer un achat dans ce canevas amènera les utilisateurs à quitter le canevas.
- Un Braze [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) configuré avec les partenaires et les audiences que vous utilisez.

## Adapter le modèle à vos besoins

Disons que nous travaillons chez Kitchenerie, une marque de retail spécialisée dans les ustensiles de cuisine, et que notre objectif est de réengager les utilisateurs qui ont ajouté le dernier produit "Enormous Paper Plate" à leur panier, mais qui n'ont pas effectué leurs achats.

Avant de créer le Canvas, nous avons configuré l'intégration Braze [Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) afin de pouvoir ajouter les données utilisateurs de Braze à Facebook Audiences pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle d'intention abandonnée, lorsque vous créez une nouvelle toile, sélectionnez **Utiliser un modèle de toile** > **Modèles de Braze**. Ensuite, en regard de l'**intention abandonnée**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Mettez à jour le nom du canvas pour spécifier que le canvas est destiné au ciblage des utilisateurs dont les paniers ont été abandonnés.
3\. Mettez à jour la description pour préciser que la toile est destinée à encourager les utilisateurs à effectuer des achats à partir du dernier lancement saisonnier d'ustensiles de cuisine.
4\. Ajoutez l'étiquette **Abandon de panier** pour que nous puissions la filtrer sur la page d'accueil de Canvas.

\![Le nouveau nom, la nouvelle description et le nouveau tag de la toile.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Étape 2 : Attribuez vos événements de conversion

Ensuite, attribuons notre événement de conversion. Étant donné que nous nous concentrons sur notre produit "Enormous Paper Plate", nous procéderons comme suit pour l'**événement de conversion principal A :**

1. Pour le **type d'événement de conversion**, sélectionnez **Effectue un achat.**
2. Sélectionnez **Effectuer un achat spécifique**. Cela nous permet de sélectionner un nom de produit spécifique.
3. Sélectionnez **Enormous Paper Plate**.

\![Événement de conversion principal - A avec le type de conversion "Fait un achat" avec le nom de produit "Enormous Paper Plate". Le délai de conversion est de 3 jours.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Étape 3 : Définir une planification d'entrée

Bien que la planification d'entrée de ce modèle soit définie sur **API-Triggered**, notre cas d'utilisation bénéficiera davantage d'une entrée basée sur l'action pour ce Canvas puisque nous voulons nous concentrer sur les utilisateurs qui ont abandonné leur panier (ce qui est une action).

1. Sélectionnez **Action-Based** comme type de planification d'entrée.
2. Sélectionnez **Abandon de panier** comme déclencheur.
3. Pour la fenêtre de saisie, sélectionnez la date de début.
4. Sélectionnez l'option permettant aux utilisateurs d'entrer leur fuseau horaire local. Cela permet de conserver la pertinence de nos messages et d'augmenter l'engagement si les messages sont envoyés à des moments optimaux.

\![Un canvas basé sur l'action qui cible les utilisateurs qui ont abandonné leur panier, avec la fenêtre d'entrée 15 octobre 2024 15h20 au fuseau horaire local des utilisateurs.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Étape 4 : Déterminer qui entre dans le Canvas

Ensuite, définissons notre audience cible comme les utilisateurs qui ont effectué des achats exclusivement en ligne chez nous au cours des 90 derniers jours. Cela nous permet de restreindre notre audience aux utilisateurs dont nous savons qu'ils s'intéressent à nos produits. 

\!["Segment des acheteurs en ligne - 90 jours" comme segment des utilisateurs à cibler pour ce Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Nous laisserons les contrôles d'entrée tels quels, de sorte que les utilisateurs ne soient pas autorisés à entrer à nouveau dans ce canvas et qu'il n'y ait pas de limite au nombre de personnes pouvant potentiellement entrer dans ce canvas.

En ce qui concerne les critères de sortie, les utilisateurs quitteront la toile s'ils ont acheté l'"énorme assiette en papier". Ainsi, ils ne recevront pas d'autres messages concernant un article qu'ils ont déjà acheté.

\![Critère de sortie qui détermine que les utilisateurs qui effectuent un achat spécifique pour l'énorme assiette en papier quitteront le Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications, et nous laisserons les autres paramètres tels quels.

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre canvas en personnalisant les étapes du canevas :

1. Sélectionnez l'étape Parcours d'action, puis le nom du groupe d'action **Achat**.
2. Pour **Effectuer un achat**, sélectionnez **Effectuer un achat spécifique** et choisissez **Enormous Paper Plate** pour le produit. Comme pour les critères de sortie, les utilisateurs qui achètent ce produit quitteront le Canvas.

\!["Fait l'achat" groupe d'action qui quittera le Canvas si l'utilisateur achète l'énorme assiette en papier.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3\. Pour l'étape Message, sélectionnez **Modifier le** message pour personnaliser l'e-mail qui sera envoyé à nos utilisateurs, les informant des articles présents dans leur abandon de panier.
4\. Conservez l'étape du délai telle qu'elle est.
5\. Dans les étapes Message qui suivent l'étape Parcours d'audience, nous personnaliserons l'e-mail et le message SMS que nos utilisateurs recevront. C'est ici que nous voulons encourager nos utilisateurs à acheter des produits grâce à des messages personnalisés.

\![Un aperçu du message SMS que les utilisateurs recevront : "Bonjour, vous avez oublié l'énorme assiette en carton dans votre panier ! Complétez votre achat maintenant et améliorez votre jeu d'hébergement. Utilisez le code MYPLATE à la caisse pour 20 % de réduction sur votre commande !"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6\. Dans l'étape suivante des parcours d'action, sélectionnez le groupe d'actions **Achat**. Ensuite, sélectionnez **Faire un achat spécifique** et choisissez **Enormous Paper Plate** comme produit. Cette étape reflétera la première étape des parcours d'action en excluant les utilisateurs qui ont acheté notre produit afin qu'ils ne reçoivent plus d'envoi de messages.
7\. Assurez-vous que l'étape de synchronisation de l'audience est configurée pour se synchroniser avec Facebook. Cela facilitera encore le reciblage publicitaire.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée du Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

### Étape 7 : Testez et lancez le Canvas

Après avoir testé et examiné notre canvas pour vous assurer qu'il fonctionne comme prévu, sélectionnez **Lancer le** canvas pour lancer le canvas. Désormais, nous pouvons cibler intelligemment les utilisateurs avec un parcours personnalisé pour les encourager à passer à la caisse le produit qu'ils ont ajouté à leur panier !

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}

