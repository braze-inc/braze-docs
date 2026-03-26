---
nav_title: Inscription par e-mail avec double abonnement
article_title: Inscription par e-mail avec Double Opt-In
page_order: 2
page_type: reference
description: "Cet article explique comment utiliser un modèle Braze Canvas pour élargir votre audience grâce à des inscriptions par e-mail vérifiées."
tool: Canvas
---

# Inscription par e-mail avec double abonnement

> Utilisez le modèle d'inscription par e-mail avec double abonnement pour étendre votre portée avec des inscriptions par e-mail vérifiées. Ciblez les nouveaux utilisateurs pour capturer leur e-mail, confirmer leur abonnement et recevoir un code de promotion, le tout en un seul parcours fluide/sans heurts/de façon homogène, etc.

Cet article vous guidera à travers un cas d'utilisation du modèle d'**inscription par e-mail avec double abonnement**, conçu pour l'étape de considération du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui envoie des e-mails et des messages in-app aux utilisateurs lorsqu'ils commencent une session ou lorsqu'ils n'ont pas terminé leur onboarding.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous avez besoin des éléments suivants :

- Un [message in-app de plusieurs pages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) avec une page pour capturer les e-mails de vos utilisateurs et une autre pour communiquer un message de réussite. 
- Un e-mail de confirmation permettant aux utilisateurs de vérifier leur adresse e-mail.
- Un e-mail de bienvenue avec un code de promotion exclusif pour les utilisateurs qui font un double abonnement.

## Adapter le modèle à vos besoins

Supposons que vous travailliez pour Steppington, une application de santé réputée pour ses fonctionnalités telles que le suivi des calories, les cours de sport en ligne et les marathons flash mob. Avant de créer le Canvas, vous [configurez des messages multipages in-app et dans le navigateur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) qui comprennent une série de questions pertinentes afin de déterminer l'expérience et l'impression d'un utilisateur lors de sa première utilisation de l'application.

Pour accéder au modèle, lorsque vous créez un nouveau canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**. Ensuite, à côté de **Inscription par e-mail avec double abonnement**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Veuillez ajuster les détails du canvas afin qu'ils reflètent votre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

![Le titre et la description actuels du canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour préciser qu'il s'agit de cibler les nouveaux utilisateurs lorsqu'ils utilisent l'appli pour la première fois.
3\. Veuillez mettre à jour la description afin d'expliquer que ce canvas contient des messages personnalisés invitant les utilisateurs à s'abonner.
4\. Ajoutez le tag **Email** afin que nous puissions le filtrer sur la page d'accueil de Canvas.

![Le nouveau nom, la nouvelle description et la nouvelle étiquette pour le canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Étape 2 : Attribuer des événements de conversion

Ensuite, veuillez attribuer nos événements de conversion. Les événements de conversion constituent un type d'indicateur que vous pouvez utiliser pour mesurer le succès du Canvas. Pour le **type d'événement de conversion**, sélectionnez **Effectue un événement personnalisé.** Ensuite, veuillez sélectionner**email_opt_in**pour le **nom de l'événement personnalisé**.

![Section « Attribuer des événements de conversion » pour le type d'événement de conversion consistant en un abonnement pour recevoir des e-mails.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Veuillez respecter le délai de conversion de trois jours prévu dans le modèle, car il est important de réaliser un ciblage précis de vos utilisateurs les plus récents.

### Étape 3 : Adapter la planification de l'entrée

Veuillez conserver la planification d'entrée basée sur **les actions** afin que les utilisateurs accèdent à votre Canvas lorsqu'ils démarrent une session dans l'application. De cette manière, vous pouvez commencer à créer votre relation en vous engageant de manière opportune.

En outre, envisagez de conserver les **options basées sur les actions** telles quelles afin que les utilisateurs n'accèdent au canvas que lorsqu'ils démarrent une session.

![Une planification d'entrée basée sur les actions pour enregistrer les utilisateurs qui commencent une session dans Canvas.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Pour la **fenêtre d'entrée**, veuillez mettre à jour l'**heure** **de début (obligatoire)** en indiquant la date et l'heure souhaitées.

![Une fenêtre d'entrée avec l'heure de début le 16 janvier 2025 à 12h30. Les utilisateurs saisiront ce message dans leur fuseau horaire local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Étape 4 : Sélectionner l'audience cible

Veuillez définir votre public cible comme étant les utilisateurs de Steppington qui n'ont pas d'adresse e-mail dans leur profil utilisateur en conservant le [filtre de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) par`Email Available is false` défaut du modèle.

![Audience d'entrée avec le filtre « Adresse e-mail disponible est fausse ».]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Étape 5 : Sélectionner vos paramètres d’envoi

Veuillez conserver les paramètres d'abonnement par défaut afin d'envoyer des messages uniquement aux utilisateurs qui se sont abonnés ou qui ont accepté de recevoir des messages ou des notifications, et ignorez les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

![Options d'envoi par défaut pour envoyer uniquement aux utilisateurs abonnés ou qui ont donné leur consentement.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Étape 6 : Personnalisez votre canvas

Ensuite, veuillez créer le canvas en personnalisant les canaux et le contenu que vous souhaitez envoyer aux utilisateurs. Étant donné que vous vous concentrez sur la vérification des inscriptions par e-mail, il n'est pas nécessaire d'ajouter ou de supprimer des étapes du canvas et des canaux du modèle.

1. Sélectionnez la première étape du message intitulée **Inscription par e-mail.** C'est ici que vous mettez à jour le modèle afin d'utiliser notre message in-app multipages (et dans le navigateur).

- La page 1 contient les e-mails.
- La page 2 affiche un message de confirmation.

![Deux pages d'un message in-app pour recueillir les adresses e-mail des utilisateurs et afficher un message de confirmation.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. À partir de là, veuillez conserver l'étape « Parcours d’action **souscrit** » telle quelle. Cette étape permet de diviser nos utilisateurs en deux groupes dans une fenêtre d'une journée :

- Les utilisateurs qui se sont abonnés à Steppington avec leur e-mail
- Utilisateurs qui ne se sont pas abonnés à Steppington avec leur e-mail

{:start="3"}
3\. Ensuite, remplacez le corps de l'e-mail par l'e-mail de confirmation de notre marque pour l'étape **Vérifier l’e-mail** de Message. Cela enverra un e-mail à nos utilisateurs abonnés et les invitera à confirmer leur adresse e-mail et à s'abonner à notre service d'envoi de messages.
4\. Conservez l'étape **Confirmer l’abonnement** de Parcours d’action telle qu'elle est. Cette étape permet de distinguer davantage nos utilisateurs entre ceux qui ont confirmé leur adresse e-mail et ceux qui ne l'ont pas encore fait, avec un délai d'une semaine.
5\. Enfin, mettez à jour l'étape Message de **bienvenue + remise** avec notre e-mail de confirmation qui comprend un code de promotion exclusif.

{% alert note %}
L'étape « **Vérifier** le message **d'e-mail** » est déclenchée lors de la deuxième session de l'utilisateur. En effet, le premier événement de début de session déclencherait le canvas, mais une deuxième session doit être lancée après que l'utilisateur ait atteint la première étape du message **d'inscription par e-mail** pour que l'utilisateur soit éligible au déclenchement du deuxième message in-app.
{% endalert %}

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et vérifié votre canvas afin de vous assurer qu'il fonctionne comme prévu, veuillez le lancer en sélectionnant **« Lancer canvas** ».

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}
