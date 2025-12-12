---
nav_title: Adoption de fonctionnalités
article_title: Fonctionnalité Adoption
page_order: 3
page_type: reference
description: "Cet article décrit comment utiliser un modèle de Braze Canvas pour envoyer des messages personnalisés au moment opportun afin de mettre en évidence les avantages et les conseils d'utilisation."
tool: Canvas
---

# Adoption de fonctionnalités

> Ce modèle est personnalisé pour stimuler l'utilisation de vos nouvelles fonctionnalités, de vos produits existants, de vos offres supplémentaires ou de tout autre domaine que vous aimeriez faire découvrir à vos clients. En tirant parti d'une communication personnalisée et d'un ensemble structuré de messages, vous pouvez présenter de façon fluide/sans heurts de nouvelles fonctionnalités aux utilisateurs et obtenir d'eux un retour d'information précieux. 

Dans cet article, nous allons vous présenter un cas d'utilisation du modèle **Adoption des fonctionnalités**, qui est destiné aux étapes de rétention et de fidélisation du cycle de vie de l'utilisateur. À l'issue de cet article, vous aurez personnalisé un parcours client qui encourage les utilisateurs à utiliser de nouvelles fonctionnalités et recueille le sentiment des utilisateurs.

## Conditions préalables

Pour utiliser ce modèle avec succès, vous devez créer un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) qui indique que les utilisateurs ont utilisé la fonctionnalité.

## Adapter le modèle à vos besoins

Imaginons que vous travailliez chez Calorie Rocket, une appli de réception/distribution de nourriture, qui a récemment lancé Cruise Control, une fonctionnalité permettant de planifier des livraisons de nourriture récurrentes, et que vous souhaitiez encourager davantage d'utilisateurs à adopter cette nouvelle fonctionnalité. Dans notre exemple, nous utiliserons l'événement personnalisé `scheduled_delivery` pour savoir quand les utilisateurs ont essayé la fonctionnalité de régulation de vitesse.

Pour accéder au modèle en stock, lorsque vous créez une nouvelle toile, sélectionnez **Utiliser un modèle de toile** > **Modèles de Braze**. Ensuite, en regard de **Adoption des fonctionnalités**, sélectionnez **Appliquer le modèle.** Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Régler les détails

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Modifier** à côté du nom du modèle.

\![Le titre et la description actuels de la toile.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Mettez à jour le nom du Canvas pour spécifier que le Canvas est destiné au ciblage des utilisateurs afin de recueillir leurs commentaires.
3\. Mettez à jour la description pour préciser que le Canvas a pour but d'encourager les utilisateurs à soumettre un retour d'information et à suivre l'avis des utilisateurs sur la nouvelle fonctionnalité de régulation de la vitesse.
4\. Ajoutez le tag **Adoption de fonctionnalité** afin que nous puissions le filtrer sur la page d'accueil de Canvas.

Le nouveau nom et la nouvelle description de la toile. La nouvelle description est la suivante : Canvas d'adoption de fonctionnalité pour suivre l'adoption et le sentiment des utilisateurs pour Cruise Control, une fonctionnalité permettant de planifier des livraisons de nourriture récurrentes".]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Étape 2 : Attribuer un événement de conversion

Ensuite, ajoutons un événement de conversion pour notre canvas afin de signaler l'adoption de la fonctionnalité. Cela nous permettra d'adapter ultérieurement le chemin d'expérience dans notre parcours utilisateur.

1. Sous **Attribuer des événements de conversion**, sélectionnez **Ajouter un événement de conversion**.
2. Sous **Événement de conversion principal - A**, sélectionnez **Exécuter un événement personnalisé** comme **type d'événement de conversion**.
3. Sélectionnez notre événement personnalisé `scheduled_delivery`.
4. Nous maintiendrons le délai de conversion à trois jours.

\![La fenêtre de l'événement de conversion dans le canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Étape 3 : Adapter la planification de l'entrée

Notre objectif est d'encourager nos utilisateurs à adopter le régulateur de vitesse, mais nous ne voulons pas que nos envois de messages soient trop fréquents. Nous conserverons donc ce Canvas en tant que réception/distribution planifiée et apporterons les ajustements suivants à la section des **options basées sur le temps**.

1. Mettez à jour la **fréquence d'entrée** en la faisant passer à **hebdomadaire**.
2. Conservez la récurrence telle quelle.
3. Sélectionnez **Mon** pour cibler les utilisateurs en début de semaine.
4. Sélectionnez l'heure de début de notre canvas.
5. Mettez à jour les **paramètres de fin** pour terminer la toile le dernier jour de l'année.

Nous conserverons l'option permettant aux utilisateurs de saisir le canvas dans leur fuseau horaire local.

### Étape 4 : Sélectionner l'audience ciblée

Maintenant, définissons notre audience cible en mettant à jour les détails suivants dans le modèle :

1. Sélectionnez le segment **Tous les utilisateurs**.
2. Supprimez les filtres supplémentaires du modèle. 
3. Créez ce filtre à l'aide de notre événement personnalisé : `Has scheduled_delivery for exactly 0 times`. Cela nous permet d'exclure les utilisateurs qui ont déjà utilisé la fonctionnalité de l'entrée dans notre Canvas.

\![Le segment pour tous les utilisateurs qui n'ont pas utilisé le régulateur de vitesse.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4\. En gardant à l'esprit que Calorie Rocket a précédemment permis à quelques utilisateurs de tester la nouvelle fonctionnalité Cruise Control, nous allons mettre à jour les critères de sortie afin d'exclure ces utilisateurs de l'entrée dans le Canvas.

### Étape 5 : Sélectionnez vos paramètres d'envoi

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou qui ont choisi de recevoir des messages ou des notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

### Étape 6 : Personnalisez votre canvas

#### Créer le parcours d'action

Ensuite, créons la première étape du parcours d'action, qui a pour but d'indiquer si nos utilisateurs sont intéressés par la nouvelle fonctionnalité. Nous allons apporter les ajustements suivants au modèle :

1. Étant donné que la fonctionnalité de contrôle de vitesse n'est disponible qu'après l'ajout d'une commande au panier, nous nommerons le premier groupe d'actions **Ajouté au panier** et nous sélectionnerons `added_to_cart` pour l'événement personnalisé.

\![Le nom du groupe d'action est défini sur "Ajouté au panier" et l'événement personnalisé est défini sur "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Conservez le deuxième groupe d'applications **Visite guidée** tel quel, car nous voulons évaluer si les utilisateurs ont fait une visite guidée de l'application, et s'ils l'ont fait, ils passeront au deuxième parcours d'actions.
3\. Pour le parcours d'action suivant, intitulé **Évaluer l'utilisation**, remplacez **Fonctionnalité utilisée >3x** par **Paramètres du régulateur de vitesse consultés**.
4\. Sélectionnez la liste déroulante **Perform Custom Event**, puis `scheduled_delivery` pour l'événement personnalisé.

\![Le nom du groupe d'action est défini sur "Used Feature >3x" et l'événement personnalisé est défini sur 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Mise en place d'une enquête de retour d'information

Ensuite, nous allons passer à l'étape Message intitulée **Enquête de retour d'information** pour inclure notre enquête de retour d'information que nos utilisateurs devront remplir après avoir utilisé le régulateur de vitesse pour la première fois. Les options de réponse à l'enquête pour nos utilisateurs sont les suivantes :

- **J'ai adoré !**
- **Pas pour moi.**

1. Pour les deux choix d'enquête, sélectionnez **Retour d'expérience** comme attribut personnalisé pour capturer et suivre le retour d'expérience sur le régulateur de vitesse. Cet attribut personnalisé aura deux valeurs pour conseiller les réponses à l'enquête (`good` et `bad`).
2. Mettez à jour les valeurs des attributs pour qu'elles correspondent aux options de l'enquête. Cela nous permettra de suivre la réponse de l'utilisateur.

### Étape 7 : Testez et lancez votre Canvas

Après avoir testé et examiné notre canvas pour vous assurer qu'il fonctionne comme prévu, sélectionnez **Lancer le** canvas pour lancer le canvas. Désormais, nous pouvons cibler les utilisateurs avec un parcours personnalisé pour les encourager à adopter notre nouvelle fonctionnalité Régulateur de vitesse.

{% alert tip %}
Consultez notre [liste de contrôle avant]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) et après le lancement pour connaître les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}
