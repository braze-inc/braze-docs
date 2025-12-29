---
nav_title: Onboarding avec enquête sur les préférences
article_title: Onboarding avec enquête sur les préférences
page_order: 5.5
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour favoriser l'adoption précoce avec un flux d'onboarding guidé pour présenter votre marque aux nouveaux utilisateurs et recueillir leurs préférences pour les maintenir engagés à long terme."
tool: Canvas
---

# Onboarding avec enquête sur les préférences

> Utilisez le modèle d'enquête sur l'onboarding avec préférences pour créer un flux de travail d'onboarding guidé qui cible les nouveaux utilisateurs. Présentez-leur votre marque, aidez-les à démarrer et recueillez leurs préférences pour qu'ils restent engagés à long terme.

Cet article vous guidera à travers un cas d'utilisation du modèle d'**enquête Onboarding with preferences**, qui est conçu pour l'étape de considération du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui envoie des e-mails et des messages in-app aux utilisateurs lorsqu'ils commencent une session et lorsqu'ils n'ont pas terminé leur onboarding.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un e-mail de bienvenue qui invite les utilisateurs à commencer l'onboarding.
- Un e-mail de suivi qui comprend des conseils pour démarrer avec l'application pour les utilisateurs qui ont onboardé.
- Un e-mail de suivi pour inciter les utilisateurs à terminer leur onboarding.
- Une [enquête]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) contenant plusieurs questions pour déterminer les préférences de l'utilisateur.

## Adapter le modèle à vos besoins

Imaginons que nous travaillions pour StyleRyde, une application de covoiturage à la demande qui permet aux gens de se rendre là où ils le souhaitent. Avant de créer le Canvas, nous avons [mis en]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) place [une enquête simple]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) qui comprend une série de questions engageantes pour déterminer l'expérience et l'impression d'un utilisateur lors de son premier trajet avec l'application.

Pour accéder au modèle, lorsque vous créez un nouveau canvas, sélectionnez **Utiliser un modèle de canvas** > **Modèles de Braze**. Ensuite, en regard de l'**enquête Onboarding with preferences**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour préciser qu'il s'agit de cibler les nouveaux utilisateurs lorsqu'ils utilisent l'appli pour la première fois.
3\. Mettez à jour la description pour expliquer que ce canvas contient des messages personnalisés.
4\. Ajoutez l'étiquette **Onboarding** afin de pouvoir la filtrer sur la page d'accueil de Canvas.

\![Le nouveau nom, la nouvelle description et le nouveau tag de la toile.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Étape 2 : Attribuer des événements de conversion

Mettez à jour l'**événement de conversion principal - A** vers **Performs Custom Event.** Sélectionnez ensuite **Dernière application utilisée** pour l'événement personnalisé.

\![Last Used App comme nom d'événement personnalisé sélectionné pour l'événement de conversion.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Étape 3 : Adapter la planification de l'entrée

Gardons la planification d'entrée comme **Basée sur l'action** afin que les utilisateurs entrent dans notre Canvas lorsqu'ils démarrent une session dans l'application. De cette manière, nous pouvons commencer à créer nos relations avec un engagement opportun.

Nous ferons une mise à jour de cette section en ajustant la **fenêtre d'entrée** à la date et à l'heure souhaitées.

\!["Fenêtre d'inscription" avec l'heure de début le 30 janvier 2025 à 12 heures.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Étape 4 : Sélectionner l'audience ciblée

Nous conserverons l'audience cible telle quelle pour cibler nos utilisateurs qui ont utilisé l'appli StyleRyde pour la première fois il y a moins d'un jour.

Le filtre "Première utilisation de ces applications il y a moins d'un jour" a permis de cibler l'audience d'entrée.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications avec les heures calmes activées, et nous ignorerons les autres paramètres (limite de fréquence et groupes initiateurs).

!section "Paramètres d'envoi" avec les paramètres d'abonnement pour les utilisateurs qui sont abonnés ou opt-in avec les heures calmes activées entre 12 heures et 20 heures.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre Canvas en personnalisant le contenu qui sera envoyé aux utilisateurs. 

1. Pour le premier message de l'étape **Email de bienvenue**, nous allons mettre à jour cette étape pour inclure notre e-mail de bienvenue StyleRyde.
2. Ensuite, nous conservons l'étape du parcours d'action telle quelle. Cette étape divise nos utilisateurs en deux groupes dans une fenêtre de trois jours :

- Les utilisateurs qui ont démarré une session ou cliqué sur l'e-mail d'onboarding.
- Les utilisateurs qui n'ont pas démarré de session ou cliqué sur l'e-mail d'onboarding.

Une étape du parcours d'action est divisée en deux parcours, l'un pour les utilisateurs qui ont commencé une session et l'autre pour tous les autres.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

À partir de là, nous ciblerons nos utilisateurs et nos envois de messages en fonction des groupes susmentionnés.

#### Ciblez vos utilisateurs engagés

Pour nos utilisateurs qui ont commencé une session ou se sont engagés avec notre e-mail d'onboarding à partir de la première étape Message, nous mettrons à jour l'étape Message **Conseils de démarrage** pour inclure les conseils de voyage et de sécurité essentiels pour nos nouveaux utilisateurs StyleRyde.

Une fois que l'utilisateur a terminé son onboarding, il quitte le Canvas.

Ensuite, mettez à jour l'étape du message relative **à l'enquête sur les préférences en matière de contenu** afin d'y inclure notre enquête sur les préférences qui invite nos utilisateurs à sélectionner les sujets sur lesquels ils souhaitent recevoir des informations à l'avenir.

Un aperçu de l'enquête sur les préférences qui invite les utilisateurs à sélectionner tous les intérêts qui s'appliquent.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Pousser les utilisateurs qui n'ont pas encore commencé l'onboarding. 

Pour nos autres utilisateurs, nous mettrons à jour l'étape **Winback Nudge** Message avec notre e-mail de suivi pour inciter les utilisateurs à terminer leur onboarding.

Comme dernière étape de réengagement, nous renommerons l'étape **2** en **Final Winback Nudge** et mettrons à jour l'étape avec notre message in-app pour inciter nos nouveaux utilisateurs à terminer leur onboarding.

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour s'assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Lancer le canvas.**

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}