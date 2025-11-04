---
nav_title: Utilisateur déchu
article_title: Utilisateur déchu
page_order: 4
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour faire revenir les utilisateurs sur votre appli grâce à des incitations basées sur leurs engagements passés."
tool: Canvas
---

# Utilisateur déchu

> Utilisez le modèle de l'utilisateur déchu pour rappeler aux utilisateurs la valeur que votre marque leur apporte, et encouragez-les à revenir en leur proposant des offres et des incitations intéressantes basées sur leurs engagements passés.

Cet article vous guidera à travers un cas d'utilisation du modèle **Utilisateur déchu**, qui est conçu pour l'étape de rétention et de fidélisation du cycle de vie de l'utilisateur. Lorsque vous aurez terminé, vous aurez créé un Canvas qui encourage les utilisateurs à revenir sur votre application avec des promotions qui varient en fonction de leur comportement, par exemple s'ils ont démarré une session dans votre application après avoir reçu un message promotionnel.

## Conditions préalables

Pour utiliser avec succès le modèle d'utilisateur déchu, vous devez configurer Braze [Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) avec les partenaires et les audiences que vous utilisez.

## Adapter le modèle à vos besoins

Disons que nous travaillons pour MovieCanon, un service de streaming qui propose des contenus exclusifs pour des films et des émissions. Nous pouvons utiliser le modèle de l'utilisateur déchu pour promouvoir des avantages et du contenu premium pour les utilisateurs qui n'ont pas visité notre application depuis 30 jours.

Avant de créer le Canvas, nous avons configuré l'intégration Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) afin de pouvoir ajouter les données comportementales des utilisateurs de Braze à Google Audiences pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle d'utilisateur de laçage, lorsque vous créez une nouvelle toile, sélectionnez **Utiliser un modèle de toile** > **Modèles de Braze**. Ensuite, en regard de **Utilisateur défaillant**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails 

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour spécifier que ce Canvas enverra des messages aux utilisateurs avec des promotions et effectuera une synchronisation d'audience pour ceux qui démarrent une session.
3\. Mettez à jour la description pour expliquer que ce Canvas contient des avantages et des promotions.
4\. Ajoutez l'étiquette **Lapsing/Retention** afin de pouvoir filtrer cette toile sur la page d'accueil de la toile.

\!["Set Up Canvas Details" étape du canvas avec le nom du canvas "Lapsed User - Visit App" et une brève description du canvas]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Étape 2 : Attribuez vos événements de conversion

Mettez à jour l'**événement de conversion principal - A** pour cibler les utilisateurs de notre application (MovieCanon), et laissez l'**événement de conversion principal - B** comme valeur par défaut pour tout achat.

\!["Assigner des événements de conversion" avec un événement de conversion principal d'un utilisateur démarrant une session dans une application spécifique.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Étape 3 : Adapter la planification de l'entrée

Gardons la planification d'entrée en tant que **Planifié** et les options par défaut basées sur le temps, de sorte que le Canvas vérifie quotidiennement les utilisateurs déchus.

Nous allons apporter deux Adjust à cette étape : 

1. Sélectionnez une date et une heure de début.
2. Sélectionnez les paramètres de fin : **à une date précise** et dans deux mois. Supposons que nous ayons un autre canevas d'utilisateur caduc que nous voulons commencer après celui-ci.

\!["Étape du canevas d'entrée" pour un canevas planifié qui entre les utilisateurs à une heure désignée.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Étape 4 : Sélectionner notre audience cible

Nous conserverons les paramètres par défaut pour l'audience d'entrée, qui est définie sur les utilisateurs qui n'ont pas utilisé notre application depuis plus de 30 jours. Nous conserverons également les contrôles d'entrée par défaut afin que les utilisateurs puissent réintroduire le Canvas après quatre semaines. Cela signifie que chaque fois qu'un utilisateur ne visite pas notre application pendant plus de 30 jours d'affilée, il sera inscrit dans le Canvas.

\!["Target Audience" étape de ciblage des utilisateurs qui ont utilisé les applications pour la dernière fois dans les 30 jours.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons la plupart des paramètres d'abonnement par défaut :

- N'envoyez des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications.
- Appliquez nos [règles de limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) afin de ne pas submerger notre audience par le nombre de messages qu'elle reçoit. Dans ce cas, nous avons défini notre limite de fréquence pour limiter à deux par semaine le nombre de campagnes ou d'étapes Canvas étiquetées avec " Abandon/Rétention " qu'un utilisateur peut recevoir.
- N'envoyez pas de messages pendant les heures calmes de l'heure locale de l'utilisateur (de 12 heures à 8 heures).

Le seul paramètre que nous modifierons est le comportement à adopter lorsqu'un message se déclenche pendant les heures calmes. Au lieu d'annuler le message, sélectionnez **Envoyer au prochain moment disponible** afin que nos utilisateurs ne manquent aucune promotion.

\!["Heures calmes"] avec une heure de début à 12 heures et une heure de fin à 8 heures.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Étape 6 : Personnalisez votre canvas

Nous allons maintenant créer notre canvas en personnalisant les étapes du canevas :

1. Personnalisez le premier e-mail qui sera envoyé à tous les utilisateurs qui n'ont pas visité notre application depuis plus de 30 jours. Pour notre cas d'utilisation, nous allons personnaliser un e-mail qui indique aux utilisateurs qu'ils débloqueront de nouveaux avantages lorsqu'ils visiteront notre application aujourd'hui. 

!étape du message canvas pour un e-mail qui indique aux utilisateurs de débloquer de nouveaux avantages lors de leur visite d'aujourd'hui.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. Personnalisez le composant du parcours d'action intitulé "Démarrer la session ?" en sélectionnant notre application pour le parcours **Démarrer la session**. 

!parcours d'action pour les sessions lancées dans une application spécifique.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. Conservez la valeur par défaut de l'étape de l'arbre décisionnel intitulée "Sessions ?", qui définit le groupe ">1 session" comme les utilisateurs qui ont utilisé notre application plus d'une fois au cours du dernier jour calendrier.
4\. Personnalisez l'étape Message pour les utilisateurs qui appartiennent au groupe ">1 session". Dans notre cas d'utilisation, nous allons remercier les utilisateurs d'avoir visité notre application et mettre en avant les avantages qu'ils ont débloqués.
5\. Assurez-vous que notre synchronisation Google Audience est configurée dans l'étape de mise à jour de l'audience publicitaire, afin de mettre à jour et de synchroniser les données des utilisateurs qui ont eu plusieurs sessions après avoir reçu notre premier e-mail.
6\. Conservez la valeur par défaut du composant [Chemin d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) appelé "Test A/B". Cela permettra d'envoyer de manière aléatoire l'une des deux promotions (que nous personnaliserons à l'étape suivante) aux utilisateurs qui ont eu moins de deux sessions.
7\. Personnalisez les deux promotions qui seront envoyées aux utilisateurs dans le cadre du chemin d'expérience. Dans notre cas d'utilisation, nous ferons une promotion de 20 % pour un abonnement de trois mois et une promotion de 10 % pour un abonnement d'un mois.

!étapes du canvas avec des chemins de ramification basés sur le nombre de sessions d'un utilisateur.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Étape 7 : Testez et lancez le Canvas

Après avoir testé et examiné notre canvas pour s'assurer qu'il fonctionne comme prévu, nous le lancerons en sélectionnant **Lancer le canvas.** Désormais, nos utilisateurs qui n'ont pas visité notre appli depuis plus de 30 jours et qui se sont abonnés à nos canaux d'envoi de messages recevront des e-mails les encourageant à revenir !

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}

