---
nav_title: "Parcours d'action"
article_title: Parcours d’actions 
alias: /action_paths/
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser les parcours d’action, un composant qui vous permet de trier les utilisateurs en fonction de leurs actions."
tool: Canvas
---

# Parcours d’actions 

> Les parcours d’action dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions. 

![Une étape « Parcours d’action » dans un parcours utilisateur Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Les parcours d’action vous permettent d’effectuer les tâches suivantes :

* Personnaliser des chemins d’utilisateur en fonction d’une action spécifique, dont des événements d’engagement d’utilisateur et des événements personnalisés
* Conserver des utilisateurs pendant une certaine durée pour prioriser leur parcours suivant en fonction de leurs actions au cours de cette période d’évaluation

## Créer un parcours d'action

Pour créer un parcours d’actions, ajoutez un composant à votre Canvas. Glissez-déposez le composant à partir de la barre latérale ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Parcours d'action.**

### Paramètres d’action

Dans les **paramètres de l'action**, définissez la **fenêtre d'évaluation** pour déterminer la durée pendant laquelle les utilisateurs sont maintenus dans l'étape. Par défaut, les utilisateurs sont évalués en un jour, mais vous pouvez paramétrer cette fenêtre pour afficher des secondes, des minutes, des heures, des jours ou des semaines, selon votre Canvas. La fenêtre d'évaluation maximale pour un parcours d'action est de 31 jours.

Dans les **paramètres d'action**, vous pouvez également activer l'ordre de classement de vos composants en basculant sur l'option **Avancer les utilisateurs en fonction de l'ordre de classement**.

![Les paramètres d'action avec une fenêtre d'évaluation d'un jour.]({% image_buster /assets/img/actionpath_settings.png %})

Par défaut, le **classement** est désactivé. Lorsqu'un utilisateur entre dans le parcours d’action et déclenche le déclencheur associé à un groupe d’actions, il effectue immédiatement l’avancement dans le groupe d’actions concerné en fonction de la **première action admissible** qu’il effectue après être entré dans l’étape. Si un utilisateur effectue une deuxième action correspondant à un groupe d'actions différent, il ne change pas de chemin : la première action détermine son itinéraire. Si un utilisateur ne déclenche pas d'événement, il passe dans le groupe par défaut **« Tout le monde »** à la fin de la période d'évaluation.

Lorsque **l'option « Utilisateurs avancés basés sur l'ordre de classement** » est activée, cela signifie que **le classement** est activé. Par conséquent, tous les utilisateurs sont retenus jusqu'à la fin de la période d'évaluation. À la fin de la période d'évaluation, l'avancement des utilisateurs se fait dans le groupe d'actions prioritaires le plus élevé auquel ils sont éligibles à la fin de la période d'évaluation. Les utilisateurs qui n'effectuent aucune des actions pendant la période d'évaluation progressent dans le groupe par défaut **« Tout le monde** ».

{% alert tip %}
Pour diriger les utilisateurs en fonction de leurs attributs actuels ou de leur appartenance à un segment plutôt que des actions qu'ils effectuent, veuillez utiliser [les parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/).
{% endalert %}

Veuillez noter que vous pouvez déclencher un parcours d’action lorsqu’un objet d’attribut personnalisé imbriqué change, mais pas pour les tableaux d’attributs personnalisés imbriqués ou les modifications apportées aux types de données des tableaux d’objets.

#### in-app Messages

Veuillez noter que lorsque le déclencheur du groupe d'actions lance une session et que l'étape suivante est un message in-app, l'utilisateur doit effectuer deux démarrages de session pour recevoir le message in-app. La première session affecte l’utilisateur au groupe d’actions dans le parcours d’action, et la deuxième session déclenche le message in-app.

#### Exemple de statut de classement

Supposons que vous ayez un parcours d’action avec une période d’évaluation d’un jour avec deux groupes d’actions : Groupe 1 et Groupe 2. Le Groupe 1 a un événement déclencheur « Démarrer une session » et le Groupe 2 « Effectuer un achat ». Si le **classement** est activé, tous les utilisateurs du parcours d'action sont "retenus" pendant un jour. À la fin de la journée, si un utilisateur a démarré une session et effectué un achat, il passe au parcours de classement le plus élevé. Dans ce cas, l’utilisateur passerait au Groupe 1. 

Dans l'exemple précédent, si **le classement** est désactivé et qu'un utilisateur effectue l'un des événements déclencheurs (« Démarrer une session » ou « Effectuer un achat »), cet utilisateur bénéficie d'un avancement dans le groupe d'actions pertinent en fonction de l'action de déclenchement.

Notez que les propriétés d’entrée Canvas diffèrent des propriétés de l’événement. Les propriétés d’entrée Canvas sont des propriétés issues de l’événement qui a déclenché le Canvas. Ces propriétés peuvent être uniquement utilisées dans la première étape complète d’un Canvas lorsque vous utilisez le flux de travail Canvas d’origine. Lorsque vous utilisez Canvas, les propriétés d'entrées persistantes sont activées et permettent de réutiliser les propriétés d'entrées dans l'ensemble de Canvas. Inversement, les propriétés de l’événement proviennent d’un événement ou d’une action qui se produit lorsque l’utilisateur accède à son flux de travail.

### Groupes d’actions

Ajoutez un ou plusieurs déclencheurs pour définir vos groupes d’actions. Ici, vous pouvez sélectionner une série de déclencheurs, par exemple si les utilisateurs :

- Effectuer un achat
- Lancer une session
- Exécuter un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Effectuer un événement de conversion
- Ajouter une adresse e-mail
- Modifier la valeur d'un attribut personnalisé.
  - Cela inclut l'ajout d'un nouvel attribut avec une valeur à un profil utilisateur pour la première fois (lorsque l'attribut n'était pas présent auparavant).
  - Les déclencheurs d'attributs ne sont pas disponibles pour les attributs de tableau.
- Mettre à jour leur statut du groupe d'abonnement ou leur statut du groupe d'abonnement
- Interagir avec une campagne ou une carte de contenu
- Saisir un emplacement
- Déclencher un géorepérage
- Envoyer un message entrant par SMS ou WhatsApp

![Un groupe d'action nommé « Groupe 1 » pour les utilisateurs qui effectuent un achat.]({% image_buster /assets/img/actionpath_group.png %})

Dans chaque configuration de groupe d'actions, vous avez également la possibilité de cocher la case **Je souhaite que ce groupe quitte Canvas**, ce qui signifie que les utilisateurs de ce groupe quitteront Canvas à la fin de la période d'évaluation.

### Canvas avec rééligibilité

Si les utilisateurs entrent plusieurs fois dans un parcours d'action et ont plusieurs entrées dans le parcours d'action en même temps, le comportement attendu varie en fonction de l'état du **classement**.

| Statut de classement | Comportement de parcours d’action |
|---|--------------|
| **Désactivé** | Lorsqu'une action pertinente est effectuée, Braze déduplique les entrées et effectue immédiatement l'avancement de l'entrée la plus ancienne dans le groupe d'actions pertinent. <br><br> Lorsqu'aucune action pertinente n'est effectuée, l'avancement de toutes les entrées se fait à la fin de la fenêtre d'évaluation correspondante. Aucune déduplication n'est effectuée. |
| **Activé** | Le processus d'avancement des candidatures se déroule à la fin de la période d'évaluation correspondante. Aucune déduplication n'est effectuée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Notez que les classements ne sont pas [modifiables après le lancement]({{site.baseurl}}/post-launch_edits/).
