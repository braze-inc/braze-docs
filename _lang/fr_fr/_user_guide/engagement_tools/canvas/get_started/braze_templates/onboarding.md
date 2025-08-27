---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "Cet article décrit comment utiliser un modèle Braze Canvas pour créer des parcours d'onboarding qui favorisent une forte adoption initiale et encouragent des relations durables avec vos utilisateurs."
tool: Canvas
---

# Onboarding

> Commencez le parcours de vos utilisateurs avec ce modèle d'onboarding. Ce modèle est conçu pour favoriser une forte adoption initiale et encourager des relations durables avec vos utilisateurs. En tirant parti d'une communication personnalisée et d'un ensemble structuré d'envois, vous pouvez présenter votre marque à vos utilisateurs de façon fluide/sans heurts et amorcer le début d'une relation durable.

Dans cet article, nous allons vous présenter un cas d'utilisation du modèle **Onboarding**, destiné à l'étape de considération du cycle de vie de l'utilisateur, afin de créer un parcours d'onboarding fluide pour les nouveaux utilisateurs. À l'issue de cet article, vous aurez personnalisé ce modèle de toile Braze avec des messages personnalisés pour ces nouveaux utilisateurs.

## Conditions préalables

Avant d'utiliser ce modèle, vous devez créer les [modèles d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) suivants à référencer dans le Canvas :

- Un e-mail de bienvenue à tous les utilisateurs de votre application.
- Un e-mail contenant des conseils sur l'utilisation de votre application.
- Un e-mail de retour d'information comprenant une enquête auprès des utilisateurs

## Adapter le modèle à vos besoins

Disons que nous travaillons chez PantsLabyrinth, et que notre objectif est d'améliorer l'engagement des utilisateurs, de créer un climat de confiance et de loyauté avec eux, et de les encourager à rester engagés. Pour ce faire, nous voulons nous concentrer sur le ciblage des messages destinés aux nouveaux utilisateurs qui n'ont pas encore interagi avec l'application.

Pour accéder au modèle d'onboarding, lorsque vous créez un nouveau Canvas, sélectionnez **Utiliser un modèle de Canvas** > **Modèles de Braze**. Ensuite, à côté de **Onboarding**, sélectionnez **Apply Template**. Commençons à personnaliser ce modèle pour l'adapter à notre cas d'utilisation.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

![Titre et description actuels de la toile.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour préciser qu'il s'agit d'un Canvas destiné à l'onboarding des nouveaux utilisateurs.
3\. Mettez à jour la description pour préciser que le Canvas mappe un parcours utilisateur qui favorise la confiance et la loyauté des utilisateurs.
4\. Ajoutez l'étiquette **Onboarding** afin de pouvoir la filtrer sur la page d'accueil de Canvas.

![Le nouveau nom, la nouvelle description et le nouveau tag de la toile.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Étape 2 : Attribuez vos événements de conversion

Ensuite, attribuons nos événements de conversion. Les événements de conversion sont un type d'indicateurs qui peuvent être utilisés pour mesurer le succès du canvas. Pour **Nom de l'événement personnalisé**, sélectionnez **Clic e-mail** comme événement personnalisé.

![Événement de conversion principal - Un événement dont le type de conversion est "Exécution d'un événement personnalisé" et dont le nom d'événement personnalisé est "Clic sur l'e-mail". Le délai de conversion est de 4 jours.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Cela signifie que les nouveaux utilisateurs ont jusqu'à quatre jours pour cliquer sur l'e-mail de bienvenue. Dans ce cas, nous voulons que nos nouveaux utilisateurs ressentent un sentiment d'urgence à s'engager avec PantsLabyrinth et à s'abonner à une réception/distribution récurrente sur des vêtements de saison.

### Étape 3 : Définir une planification d'entrée

L'objectif étant de cibler les nouveaux utilisateurs de PantsLabyrinth, le Canvas sera basé sur l'action. Pour **Démarrer la session**, sélectionnez **Démarrer la session dans n'importe quelle** application pour permettre aux utilisateurs qui démarrent une session dans n'importe quelle application d'entrer dans le Canvas.

Ajustez ensuite la **fenêtre d'entrée** pour déterminer quand les utilisateurs peuvent entrer dans le Canvas. Supposons qu'un abonnement à PantsLabyrinth soit lancé à la fin du mois d'octobre. C'est ici que nous fixerons l'heure de début à **2024/10/28 8:00 am.** En option, nous pouvons également permettre aux utilisateurs de saisir le Canvas dans leur fuseau horaire local.

![Une fenêtre d'entrée avec l'heure de début le 28 octobre 2024 à 8h. Les utilisateurs entreront ce message dans leur fuseau horaire local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Étape 4 : Ciblez votre audience

En ciblant la bonne audience, nous pouvons engager efficacement le dialogue avec de nouveaux utilisateurs. Par exemple, ce modèle cible tous les utilisateurs qui ont utilisé une application pour la première fois il y a moins d'un jour, ce qui est exact pour notre cas d'utilisation. Nous laisserons donc cette section telle quelle.

### Étape 5 : Régler les paramètres d'envoi

Par défaut, ce Canvas est envoyé aux utilisateurs qui sont abonnés ou qui ont choisi de s'abonner et suit les règles de limite de fréquence. Nous conserverons ces paramètres tels quels.

### Étape 6 : Personnalisez votre canvas

Maintenant, créons le Canvas en personnalisant les étapes du canevas.

#### Configurez l'e-mail de bienvenue

1. Sélectionnez l'étape du message intitulée "Welcome Email".
2. Sélectionnez **Modifier le message** pour remplacer l'e-mail du modèle par notre e-mail de bienvenue.
3. Sélectionnez **Terminé**.

Désormais, nos utilisateurs recevront cet e-mail de bienvenue après avoir démarré une session dans notre appli. Afin de ne pas submerger les utilisateurs avec des messages répétés, nous recommandons d'utiliser l'étape du délai dans le cadre du parcours de l'utilisateur.

#### Personnaliser le parcours d'audience

Dans l'étape du parcours d'audience nommée **Fractionnement de l'audience**, nous pouvons personnaliser le filtre pour nos utilisateurs engagés. Dans le modèle, le filtre est **L'e-mail cliqué pour l'étape Email de bienvenue**, ce qui signifie que les utilisateurs sont divisés en deux groupes : les utilisateurs qui ont cliqué sur l'e-mail de bienvenue et ceux qui ne l'ont pas fait.

![Une étape de fractionnement de l'audience avec un parcours pour les utilisateurs engagés et un parcours pour tous les autres.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

En tant que retailing de vêtements en ligne, PantsLabyrinth dispose également d'un groupe actif d'utilisateurs mobiles. Ainsi, dans un Canvas d'onboarding séparé, nous pouvons également sélectionner le filtre suivant pour identifier et répartir nos utilisateurs mobiles dans ces segments :

- **A cliqué sur la carte de contenu pour l'étape Carte de contenu de bienvenue**
- **Tous les autres**

#### Ciblez davantage d'utilisateurs grâce aux parcours d'audience

À partir de l'ensemble des utilisateurs qui n'ont pas interagi avec notre application, nous pouvons cibler davantage ces utilisateurs en modifiant l'étape "Check for Clicks" et l'étape "Winback Nudge".

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour vous assurer qu'il fonctionne comme prévu, sélectionnez **Lancer le** canvas pour lancer le canvas. Désormais, nous pouvons offrir à nos nouveaux utilisateurs une expérience d'onboarding personnalisée pour encourager une relation durable !

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}

