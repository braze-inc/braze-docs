---
nav_title: Parcours d’actions 
article_title: Parcours d’actions 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Cet article de référence explique comment utiliser les parcours d’action, un composant qui vous permet de trier les utilisateurs en fonction de leurs actions."
tool: Canvas
---

# Parcours d’actions 

> Les parcours d’action dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions. 

![Une étape des parcours d'action dans un parcours utilisateur Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les parcours d’action vous permettent d’effectuer les tâches suivantes :

* Personnaliser des chemins d’utilisateur en fonction d’une action spécifique, dont des événements d’engagement d’utilisateur et des événements personnalisés
* Conserver des utilisateurs pendant une certaine durée pour prioriser leur parcours suivant en fonction de leurs actions au cours de cette période d’évaluation

## Créer un parcours d'action

Pour créer un parcours d’actions, ajoutez un composant à votre Canvas. Glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Parcours d'action.** 

### Paramètres d’action

Dans les **paramètres de l'action**, définissez la **fenêtre d'évaluation** pour déterminer la durée pendant laquelle les utilisateurs sont maintenus dans l'étape. Par défaut, les utilisateurs sont évalués en un jour, mais vous pouvez paramétrer cette fenêtre pour afficher des secondes, des minutes, des heures, des jours ou des semaines, selon votre Canvas. La fenêtre d'évaluation maximale pour un parcours d'action est de 31 jours.

Dans les **paramètres d'action**, vous pouvez également activer l'ordre de classement de vos composants en basculant sur l'option **Avancer les utilisateurs en fonction de l'ordre de classement**.

![L'action Paramètres avec une fenêtre d'évaluation d'un jour.]({% image_buster /assets/img/actionpath_settings.png %})

Par défaut, le **classement** est désactivé. Lorsqu’un utilisateur accède au parcours d’action et effectue l’événement déclencheur annexe à tout groupe d’actions, il passe automatiquement au groupe d’actions pertinent. Si un utilisateur n'effectue pas d'événement déclencheur, il avancera dans le groupe par défaut **Tous les autres** à la fin de la période d'évaluation.

Lorsque l'option **Utilisateurs avancés en fonction de l'ordre de classement** est activée, cela signifie que l'**option Classement** est activée. Tous les utilisateurs seront donc conservés jusqu’à la fin de la fenêtre d’évaluation. À la fin de la période d’évaluation, les utilisateurs passeront au groupe d’actions de priorité absolue auquel ils sont éligibles à la fin de la fenêtre d’évaluation. Les utilisateurs qui n'effectuent aucune des actions pendant la fenêtre d'évaluation avanceront dans le groupe par défaut **Tous les autres.**

#### in-app Messages

Notez que lorsque le déclencheur du groupe d’actions est le démarrage d’une session et que l’étape suivante est un message in-app, l’utilisateur devra effectuer deux démarrages de session pour recevoir le message in-app. La première session affecte l’utilisateur au groupe d’actions dans le parcours d’action, et la deuxième session déclenche le message in-app.

#### Exemple de statut de classement

Supposons que vous ayez un parcours d’action avec une période d’évaluation d’un jour avec deux groupes d’actions : Groupe 1 et Groupe 2. Le Groupe 1 a un événement déclencheur « Démarrer une session » et le Groupe 2 « Effectuer un achat ». Si le **classement** est activé, tous les utilisateurs du parcours d'action sont "retenus" pendant un jour. À la fin de la journée, si un utilisateur a démarré une session et effectué un achat, il passe au parcours de classement le plus élevé. Dans ce cas, l’utilisateur passerait au Groupe 1. 

Dans l'exemple précédent, si **le classement** est désactivé et qu'un utilisateur effectue l'un des événements déclencheurs ("Démarrer une session" ou "Effectuer un achat"), cet utilisateur est avancé dans le groupe d'actions approprié en fonction de l'action déclencheuse.

Notez que les propriétés d’entrée Canvas diffèrent des propriétés de l’événement. Les propriétés d’entrée Canvas sont des propriétés issues de l’événement qui a déclenché le Canvas. Ces propriétés peuvent être uniquement utilisées dans la première étape complète d’un Canvas lorsque vous utilisez le flux de travail Canvas d’origine. Lorsque vous utilisez Canvas Flow, les Propriétés d’entrées persistantes sont activées et permettent de saisir des propriétés qui peuvent être réutilisées dans le Canvas tout entier. Inversement, les propriétés de l’événement proviennent d’un événement ou d’une action qui se produit lorsque l’utilisateur accède à son flux de travail.

### Groupes d’actions

Ajoutez un ou plusieurs déclencheurs pour définir vos groupes d’actions. Ici, vous pouvez sélectionner une série de déclencheurs, par exemple si les utilisateurs :

- Effectuer un achat
- Lancer une session
- Exécuter un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Effectuer un événement de conversion
- Ajouter une adresse e-mail
- Modifier la valeur d'un attribut personnalisé (pas les attributs personnalisés imbriqués)
- Mettre à jour leur statut du groupe d'abonnement ou leur statut du groupe d'abonnement
- Interagir avec une campagne ou une carte de contenu
- Saisir un emplacement
- Déclencher un géorepérage
- Envoyer un message entrant par SMS ou WhatsApp

![Un groupe d'action nommé "Groupe 1" pour les utilisateurs qui effectuent un achat.]({% image_buster /assets/img/actionpath_group.png %})

Dans chaque paramètre de groupe d'action, vous avez également la possibilité de cocher la case **Je veux que ce groupe quitte le Canvas**, ce qui signifie que les utilisateurs de ce groupe quitteront le Canvas à la fin de la période d'évaluation.

### Canvas avec rééligibilité

Si les utilisateurs entrent plusieurs fois dans un parcours d'action et ont plusieurs entrées dans le parcours d'action en même temps, le comportement attendu varie en fonction de l'état du **classement**.

| Statut de classement | Comportement de parcours d’action |
|---|--------------|
| **Désactivé** | Lorsqu’une action pertinente est effectuée, Braze va dupliquer les entrées et faire avancer immédiatement l’entrée la plus ancienne vers le groupe d’action pertinent. <br><br/> Lorsqu’une action pertinente n’est pas effectuée, toutes les entrées seront repoussées vers le bas de la fenêtre d’évaluation pertinente. Aucune déduplication n’est effectuée. |
| **Activé** | Toutes les entrées seront repoussées vers le bas de la fenêtre d’évaluation pertinente. Aucune déduplication n’est effectuée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Notez que les classements ne sont pas [modifiables après le lancement]({{site.baseurl}}/post-launch_edits/).


