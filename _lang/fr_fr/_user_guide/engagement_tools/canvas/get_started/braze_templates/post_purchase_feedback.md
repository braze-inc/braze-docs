---
nav_title: "Rétroaction après l'achat"
article_title: "Rétroaction après l'achat"
page_order: 6
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour orchestrer des expériences personnalisées qui vous permettent de répondre aux commentaires et de créer une relation avec vos utilisateurs."
tool: Canvas
---

# Retour d'information après l'achat

> Utilisez le modèle de feedback post-achat pour obtenir des informations essentielles sur la manière dont vos clients interagissent avec votre marque et vous assurer qu'ils continuent à avoir des expériences positives. En tirant parti d'une communication personnalisée et d'un ensemble structuré de messages, vous pouvez continuer à créer et à développer vos relations avec vos clients.

Cet article vous guidera à travers un cas d'utilisation du modèle **Feedback post-achat**, qui est conçu pour l'étape de conversion du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui encourage les utilisateurs à donner leur avis sur votre application.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) à référencer pour les résultats de l'enquête de satisfaction.
- Un Braze [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) configuré avec les partenaires et les audiences que vous utilisez.

## Adapter le modèle à vos besoins

Supposons que nous travaillions pour Decorumsoft, un développeur de jeux vidéo mobiles. Nous utiliserons le modèle de retour d'information après achat pour évaluer les réactions à notre dernier jeu vidéo, Proxy War 3 : La guerre de la soif. Ces commentaires nous permettront d'élaborer nos plans de développement pour le pack d'extension Liquid Mirage.

Avant de créer le Canvas, nous avons configuré l'intégration Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) afin de pouvoir ajouter les données comportementales des utilisateurs de Braze à Google Audiences pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle de retour d'information après achat, lorsque vous créez un nouveau canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**. Ensuite, en regard de **Feedback post-achat**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails de Canvas

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

![Titre et description actuels de la toile.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Mettez à jour le nom du canvas pour préciser qu'il s'agit d'un canvas destiné au ciblage des utilisateurs récents.
3\. Mettez à jour la description pour préciser que le Canvas est destiné à encourager les utilisateurs à soumettre un retour d'information.
4\. Ajoutez le tag **Feedback** pour le filtrer sur la page d'accueil de Canvas.

![Le nouveau nom et la nouvelle description de la toile. La nouvelle description est la suivante : Canevas de réactions après l'achat pour évaluer l'intérêt pour la prochaine extension de PWD3, Liquid Mirage"]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Étape 2 : Attribuer des événements de conversion

Ensuite, attribuons nos événements de conversion. Mettez à jour l'**événement de conversion principal - A** en **effectuant un achat spécifique** et sélectionnez **Guerre par procuration**.

![Section "Assigner des événements de conversion" pour le type d'événement de conversion de l'achat d'un produit du jeu Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Nous conservons le délai de conversion du modèle de trois jours car nous voulons cibler nos utilisateurs les plus récents.

### Étape 3 : Définir une planification d'entrée

1. Conservez le type de planification des entrées comme étant **basé sur des actions.**
2. Définissez l'**heure de début de** la fenêtre de saisie à la date de lancement du jeu.

### Étape 4 : Déterminer qui entre dans le Canvas

Notre audience cible pour le ciblage est constituée des utilisateurs qui ont récemment acheté Proxy War 3.

1. Sélectionnez notre segmentation cible, "Purchased Proxy War 3", qui comprend les utilisateurs qui ont acheté le jeu.
2. Sélectionnez un filtre pour inclure les utilisateurs qui ont acheté "Proxy War 3" plus de "0" fois.

![Un segment nommé "Purchased Proxy War 3" qui segmente les utilisateurs qui ont acheté le jeu.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3\. Mettez à jour les contrôles d'entrée afin de ne pas permettre aux utilisateurs d'entrer à nouveau dans la toile après la durée maximale de celle-ci.

### Étape 5 : Sélectionner vos paramètres d’envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications. 

Comme nous voulons être attentifs à nos envois, nous sélectionnerons l' **option Activer les heures calmes** pour éviter de demander des commentaires entre 23 heures et 10 heures du matin dans le fuseau horaire de nos utilisateurs et pour n'envoyer qu'à la prochaine heure disponible.

![" Envoyer les paramètres " étape de ciblage des utilisateurs abonnés ou ayant opté pour le service. Les heures calmes sont activées.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Pour notre exemple, nous ne tiendrons pas compte des autres paramètres (limite de fréquence et groupes initiateurs).

### Étape 6 : Personnalisez votre canvas

Ensuite, nous allons créer notre Canvas en personnalisant les canaux de communication et le contenu qui sera envoyé aux utilisateurs. Étant donné que nous sollicitons uniquement des commentaires par e-mail, par message in-app et par canal webhook, nous allons parcourir le modèle et supprimer les variantes SMS des étapes Message.

Nous allons commencer notre personnalisation en passant en revue chaque composant d'envoi de messages pour en mettre à jour le contenu. Notre attribut personnalisé à référencer est `Experience Feedback`.

1. Dans le générateur de canvas, sélectionnez la première étape du canvas dans le parcours de l'utilisateur.
2. Sélectionnez la variante **e-mail**.
3. Remplissez l'**info d'envoi** avec un sujet qui encourage le retour d'information des utilisateurs. 
4. Sélectionnez **Modifier le** message pour remplacer le message e-mail du modèle par le message de l'enquête de satisfaction. Il s'agit notamment de remplacer les liens pour chaque call-to-action afin de capturer l'option sélectionnée, qui sera référencée dans l'étape du parcours d'action de notre parcours utilisateur.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée du Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

#### Mise en place d'une enquête de retour d'information

Ensuite, nous allons devoir remplir les détails de la variante du **message in-app.**  C'est ici que nous devons spécifier notre attribut personnalisé `Experience Feedback` qui indique le sentiment de nos commentaires d'utilisateurs. (Nous y ferons également référence dans l'étape suivante du parcours d'action).

1. À la même étape du premier message, sélectionnez la variante **Messages in-app.**  Nous conserverons les contrôles des messages en l'état. 
2. Pour l'en-tête et le corps du texte, nous utiliserons un langage qui encourage les utilisateurs à être honnêtes au sujet de leur expérience avec Proxy War 3.
3. Comme nous voulons que leurs réponses à l'enquête soient enregistrées avec leurs profils, nous conserverons l'enquête en tant que **sélection à choix unique** et **enregistrerons les attributs lors de la soumission**.
4. Pour chacun des trois choix d'enquête, sélectionnez **Experience Feedback** comme attribut personnalisé. 
5. Nous conserverons les valeurs des attributs du profil utilisateur telles quelles, car elles correspondent à notre attribut personnalisé.

![Une enquête qui demande à l'utilisateur s'il a apprécié son récent achat de Proxy War 3 avec trois options : "J'ai adoré", "C'était bien" et "Pas pour moi".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Créer le parcours d'action

En utilisant notre attribut personnalisé `Experience Feedback` et les valeurs d'attribut de la section précédente, nous mettrons à jour le parcours d'action du modèle pour qu'il corresponde à notre attribut et à ses valeurs.

![Le groupe "Bon retour" pour l'étape du parcours d'action qui comprend les utilisateurs qui ont répondu "J'ai adoré" à notre enquête.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Mettre en place le reciblage publicitaire

Nous allons nous assurer que notre synchronisation Google Audience est configurée dans notre étape de **reciblage publicitaire.**  Vous pourrez notamment sélectionner notre compte publicitaire, une audience existante et l'option permettant d'ajouter des utilisateurs à l'audience.

### Configurer les cas de support webhook

Ensuite, configurons le webhook pour déclencher des cas d'assistance potentiels. L'analyse du retour d'expérience de nos utilisateurs peut s'avérer particulièrement riche en informations.

Pour l'étape du message intitulée **Création d'un cas d'assistance**, nous allons mettre à jour le modèle pour composer un webhook pour les utilisateurs qui ne sont pas satisfaits de leur achat et qui souhaitent un remboursement.

![Un webhook qui crée des cas de support pour les clients qui ont un sentiment négatif et qui veulent un remboursement pour leur achat de Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Étape 6 : Testez et lancez le Canvas

Après avoir testé et examiné notre canvas pour vous assurer qu'il fonctionne comme prévu, sélectionnez **Lancer le** canvas pour lancer le canvas. Désormais, nous pouvons cibler intelligemment les utilisateurs avec un parcours personnalisé pour les encourager à répondre à notre enquête de commentaires en fonction de leur récent achat de Proxy War 3 !

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}
