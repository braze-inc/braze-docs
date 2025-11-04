---
nav_title: Inscription par e-mail avec double abonnement
article_title: Inscription par e-mail avec Double Opt-In
page_order: 2
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour étendre votre portée grâce à des inscriptions vérifiées par e-mail."
tool: Canvas
---

# Inscription par e-mail avec double abonnement

> Utilisez le modèle d'inscription par e-mail avec double abonnement pour étendre votre portée avec des inscriptions par e-mail vérifiées. Ciblez les nouveaux utilisateurs pour capturer leur e-mail, confirmer leur abonnement et recevoir un code de promotion, le tout en un seul parcours fluide/sans heurts/de façon homogène, etc.

Cet article vous guidera à travers un cas d'utilisation du modèle d'**inscription par e-mail avec double abonnement**, conçu pour l'étape de considération du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui envoie des e-mails et des messages in-app aux utilisateurs lorsqu'ils commencent une session ou lorsqu'ils n'ont pas terminé leur onboarding.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [message in-app de plusieurs pages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) avec une page pour capturer les e-mails de vos utilisateurs et une autre pour communiquer un message de réussite.
- Un e-mail de confirmation permettant aux utilisateurs de vérifier leur adresse e-mail.
- Un e-mail de bienvenue avec un code de promotion exclusif pour les utilisateurs qui font un double abonnement.

## Adapter le modèle à vos besoins

Imaginons que nous travaillions pour Steppington, une application de santé connue pour ses fonctionnalités telles que le suivi des calories, les cours d'exercices numériques et les marathons flash-mob. Avant de créer le Canvas, nous avons mis [en place des messages in-app et in-browser multi-pages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) qui comprennent une série de questions engageantes pour déterminer l'expérience et l'impression d'un utilisateur lors de sa première utilisation de l'application.

Pour accéder au modèle, lorsque vous créez un nouveau canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**. Ensuite, à côté de **Inscription par e-mail avec double abonnement**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour préciser qu'il s'agit de cibler les nouveaux utilisateurs lorsqu'ils utilisent l'appli pour la première fois.
3\. Mettez à jour la description pour expliquer que ce Canvas contient des messages personnalisés pour que les utilisateurs puissent bénéficier d'un double abonnement.
4\. Ajoutez le tag **Email** afin que nous puissions le filtrer sur la page d'accueil de Canvas.

\![Le nouveau nom, la nouvelle description et le nouveau tag de la toile.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Étape 2 : Attribuer des événements de conversion

Ensuite, attribuons nos événements de conversion. Les événements de conversion sont un type d'indicateurs qui peuvent être utilisés pour mesurer le succès du canvas. Pour le **type d'événement de conversion**, sélectionnez **Effectue un événement personnalisé.** Sélectionnez ensuite **email_opt_in** pour le **nom de l'événement personnalisé**.

\!["Attribuer des événements de conversion" pour le type d'événement de conversion de l'abonnement à l'e-mail.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Nous conservons le délai de conversion du modèle de trois jours car nous voulons cibler nos utilisateurs les plus récents.

### Étape 3 : Adapter la planification de l'entrée

Gardons la planification d'entrée comme **Basée sur l'action** afin que les utilisateurs entrent dans notre Canvas lorsqu'ils démarrent une session dans l'application. De cette manière, nous pouvons commencer à créer nos relations avec un engagement opportun.

Nous conserverons également les **options basées sur l'action** telles quelles afin que les utilisateurs n'entrent dans le Canvas que lorsqu'ils démarrent une session.

!Une planification d'entrée basée sur l'action pour entrer dans le Canvas les utilisateurs qui démarrent une session.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Pour la **fenêtre d'entrée**, nous mettrons à jour l' **heure de début (obligatoire)** en fonction de la date et de l'heure souhaitées.

Une fenêtre d'entrée avec l'heure de début le 16 janvier 2025 à 12h30. Les utilisateurs saisiront ce message dans leur fuseau horaire local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Étape 4 : Sélectionner l'audience ciblée

Nous définirons notre audience cible comme étant les utilisateurs de Steppington qui n'ont pas d'adresse e-mail dans leur profil utilisateur. Pour ce faire, nous conserverons le [filtre de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) par défaut du modèle `Email Available is false`.

!Audience d'entrée avec le filtre d'audience "L'e-mail disponible est faux".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

\![Options d'envoi par défaut pour n'envoyer qu'aux utilisateurs qui sont abonnés ou qui ont opté pour l'option d'envoi.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre Canvas en personnalisant les canaux et les contenus qui seront envoyés aux utilisateurs. Comme nous nous concentrons sur la vérification des inscriptions par e-mail, nous n'avons pas besoin d'ajouter ou de supprimer les étapes et canaux Canvas du modèle.

1. Sélectionnez la première étape du message intitulée **Inscription par e-mail.** C'est ici que nous mettrons à jour le modèle pour utiliser notre message in-app (et in-browser) multi-pages.

- La page 1 contient les e-mails.
- Un message de confirmation s'affiche à la page 2.

!Deux pages d'un message in-app pour capturer les e-mails des utilisateurs et afficher un message de réussite.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. À partir d'ici, nous conserverons l'étape du parcours d'action **abonné** telle qu'elle est. Cette étape permet de diviser nos utilisateurs en deux groupes dans une fenêtre d'une journée :

- Les utilisateurs qui se sont abonnés à Steppington avec leur e-mail
- Utilisateurs qui ne se sont pas abonnés à Steppington avec leur e-mail

{:start="3"}
3\. Ensuite, remplacez le corps de l'e-mail par l'e-mail de confirmation de notre marque pour l'étape **Vérifier le** message de **l'e-mail.**  Cela permettra d'envoyer un e-mail aux utilisateurs abonnés et de leur demander de confirmer leur adresse e-mail et de s'abonner à nos envois de messages.
4\. Conservez l'étape **Confirmer le** parcours d'action de l'**abonnement** telle qu'elle est. Cette étape permet de répartir nos utilisateurs entre ceux qui ont confirmé leur e-mail et ceux qui ne l'ont pas fait, avec une fenêtre d'une semaine.
5\. Enfin, mettez à jour l'étape Message de **bienvenue + remise** avec notre e-mail de confirmation qui comprend un code de promotion exclusif.  

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour s'assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Lancer le canvas.**

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}