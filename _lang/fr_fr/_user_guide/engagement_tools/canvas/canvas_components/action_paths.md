---
nav_title: "Parcours d'action"
article_title: "Parcours d'action" 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Cet article de référence explique comment utiliser les parcours d'action, un composant qui vous permet de trier les utilisateurs en fonction de leurs actions."
tool: Canvas
---

# Parcours d'action 

> Les parcours d'action dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions. 

Une étape des parcours d'action dans un parcours utilisateur Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

En utilisant les parcours d'action, vous pouvez :

* Personnaliser les parcours d'utilisateurs en fonction d'une action spécifique, y compris les événements d'engagement utilisateur et les événements personnalisés.
* Retenir les utilisateurs pendant une durée donnée afin de hiérarchiser leur prochain parcours en fonction de leurs actions pendant cette période d'évaluation.

## Créer un parcours d'action

Pour créer un parcours d'action, ajoutez un composant à votre Canvas. Glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Parcours d'action.** 

### Paramètres d'action

Dans les **paramètres de l'action**, définissez la **fenêtre d'évaluation** pour déterminer la durée pendant laquelle les utilisateurs sont maintenus dans l'étape. Par défaut, les utilisateurs sont évalués dans un délai d'un jour, mais vous pouvez ajuster cette fenêtre en secondes, minutes, heures, jours et semaines en fonction de votre Canvas. La fenêtre d'évaluation maximale pour un parcours d'action est de 31 jours.

Dans les **paramètres d'action**, vous pouvez également activer l'ordre de classement de vos composants en basculant sur l'option **Avancer les utilisateurs en fonction de l'ordre de classement**.

L'action Paramètres dispose d'une fenêtre d'évaluation d'un jour.]({% image_buster /assets/img/actionpath_settings.png %})

Par défaut, le **classement** est désactivé. Lorsqu'un utilisateur entre dans le parcours d'action et effectue l'événement déclencheur lié à un groupe d'action, il avance immédiatement dans le groupe d'action correspondant. Si un utilisateur n'effectue pas d'événement déclencheur, il avancera dans le groupe par défaut **Tous les autres à** la fin de la période d'évaluation.

Lorsque l'option **Utilisateurs avancés en fonction de l'ordre de classement** est activée, cela signifie que l'**option Classement** est activée. Ainsi, tous les utilisateurs seront retenus jusqu'à la fin de la fenêtre d'évaluation. À la fin de la période d'évaluation, les utilisateurs avanceront dans le groupe d'action prioritaire le plus élevé auquel ils sont éligibles à la fin de la fenêtre d'évaluation. Les utilisateurs qui n'effectuent aucune des actions pendant la fenêtre d'évaluation avanceront dans le groupe par défaut **Tous les autres.** 

#### Messages in-app

Notez que lorsque le déclencheur du groupe d'applications est le démarrage d'une session et que l'étape suivante est un message in-app, l'utilisateur devra effectuer deux démarrages de session pour recevoir le message in-app. La première session affecte l'utilisateur au groupe d'applications dans le parcours d'action, et la seconde session déclenche le message in-app.

#### Exemple d'état de classement

Supposons que vous ayez un parcours d'action avec une période d'évaluation d'un jour et deux groupes d'action : Groupe 1 et Groupe 2. Le groupe 1 a un événement déclencheur "Démarrer la session" et le groupe 2 a un événement déclencheur "Effectuer un achat". Si le **classement** est activé, tous les utilisateurs du parcours d'action sont "retenus" pendant un jour. À la fin de la journée, si un utilisateur a démarré une session et effectué un achat, il avance vers le chemin de classement le plus élevé. Dans ce cas, l'utilisateur passe au groupe 1. 

Dans l'exemple précédent, si **le classement** est désactivé et qu'un utilisateur effectue l'un des événements déclencheurs ("Démarrer une session" ou "Effectuer un achat"), cet utilisateur est avancé dans le groupe d'actions approprié en fonction de l'action déclencheuse.

Notez que les propriétés d'entrée dans le canvas diffèrent des propriétés d'événement. Les propriétés d'entrée du canvas sont des propriétés de l'événement qui a déclenché le canvas. Ces propriétés ne peuvent être utilisées que dans la première étape complète d'un canvas lorsque vous utilisez le flux de travail original du canvas. Lors de l'utilisation de Canvas, les propriétés d'entrées persistantes sont activées et permettent de réutiliser les propriétés d'entrée dans l'ensemble du Canvas. À l'inverse, les propriétés d'événement proviennent d'un événement ou d'une action qui se produit lorsque l'utilisateur suit son flux de travail.

### Groupes d'action

Ajoutez un ou plusieurs déclencheurs pour définir vos groupes d'action. Ici, vous pouvez sélectionner une série de déclencheurs, par exemple si les utilisateurs :

- Effectuer un achat
- Démarrer une session
- Exécuter un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Effectuer un événement de conversion
- Ajouter une adresse e-mail
- Modifier la valeur d'un attribut personnalisé (y compris les tableaux, mais pas les attributs personnalisés imbriqués). Cela inclut l'ajout d'un nouvel attribut avec une valeur à un profil utilisateur pour la première fois (lorsque l'attribut n'était pas présent auparavant).
- Mettre à jour leur statut du groupe d'abonnement ou leur statut du groupe d'abonnement
- Interagir avec une campagne ou une carte de contenu
- Saisissez un emplacement/localisation
- Déclencher un géorepérage
- Envoyer un message entrant par SMS ou WhatsApp

Un groupe d'action nommé "Groupe 1" pour les utilisateurs qui effectuent un achat.]({% image_buster /assets/img/actionpath_group.png %})

Dans chaque paramètre de groupe d'action, vous avez également la possibilité de cocher la case **Je veux que ce groupe quitte le Canvas**, ce qui signifie que les utilisateurs de ce groupe quitteront le Canvas à la fin de la période d'évaluation.

### Toiles avec rééligibilité

Si les utilisateurs entrent plusieurs fois dans un parcours d'action et ont plusieurs entrées dans le parcours d'action en même temps, le comportement attendu varie en fonction de l'état du **classement**.

| Statut du classement | Parcours d'action Comportement |
|---|--------------|
| **Arrêt** | Lorsqu'une action pertinente est effectuée, Braze dédoublonne les entrées et fait immédiatement avancer l'entrée la plus ancienne dans le groupe d'actions concerné. <br><br/> Lorsqu'une action pertinente n'est pas effectuée, toutes les entrées avancent à la fin de la fenêtre d'évaluation concernée. Il n'y a pas de déduplication. |
| **Sur** | Toutes les candidatures seront avancées à la fin de la fenêtre d'évaluation concernée. Il n'y a pas de déduplication. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Notez que les classements ne sont pas [modifiables après le lancement]({{site.baseurl}}/post-launch_edits/).


