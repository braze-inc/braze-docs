---
nav_title: Étape de parcours d’action
article_title: Étape de parcours d’action
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Cet article de référence aborde les parcours d’action et la façon de les utiliser dans votre Canvas."
tool: Canvas
---

# Étape de parcours d’action

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Les parcours d’action dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions. Les parcours d’action vous permettent d’effectuer les tâches suivantes : 
 
* Personnaliser des chemins d’utilisateur en fonction d’une action spécifique, dont des événements d’engagement d’utilisateur et des événements personnalisés
* Conserver des utilisateurs pendant une certaine durée pour prioriser leur parcours suivant en fonction de leurs actions au cours de cette période d’évaluation.

## Créer des parcours d’action

Pour créer des parcours d’action, ajoutez une étape à votre Canvas. Puis, à l’aide du menu déroulant en haut de la nouvelle étape, sélectionnez **Parcours d’action**.

### Paramètres d’action

Dans le module **Paramètres d’action**, vous pouvez définir la durée pendant laquelle les utilisateurs doivent être maintenus dans l’étape d’action en paramétrant la **Fenêtre d’évaluation**. Par défaut, les utilisateurs sont évalués en un jour, mais vous pouvez paramétrer cette fenêtre pour afficher des secondes, des minutes, des heures, des jours ou des semaines, selon votre Canvas.

Dans les **Paramètres d’action**, vous pouvez également activer l’ordre de classement pour vos étapes en basculant sur l’option **Avancer les utilisateurs en fonction de l’ordre de classement**.

![][4]

Par défaut, le **Classement** est désactivé. Lorsqu’un utilisateur accède au parcours d’action et effectue l’événement déclencheur annexe à tout groupe d’actions, il passe automatiquement au groupe d’actions pertinent. Si un utilisateur n’effectue pas d’élément déclencheur, il passe au groupe **Tout le monde** à la fin de la période d’évaluation.

Lorsque l’option **Utilisateurs avancés en fonction de l’ordre de classement** est activée, cela signifie que le **Classement** est activé. Tous les utilisateurs seront donc conservés jusqu’à la fin de la fenêtre d’évaluation. À la fin de la période d’évaluation, les utilisateurs passeront au groupe d’actions de priorité absolue auquel ils sont éligibles à la fin de la fenêtre d’évaluation. Les utilisateurs qui n’effectuent aucune des actions pendant la fenêtre d’évaluation passeront au groupe par défaut **Tout le monde**.

#### Exemple de statut de classement

Supposons que vous ayez un parcours d’action avec une période d’évaluation d’un jour avec deux groupes d’actions : Groupe 1 et Groupe 2. Le Groupe 1 a un événement déclencheur « Démarrer une session » et le Groupe 2 « Effectuer un achat ». Si l’option **Classement** est activée, tous les utilisateurs dans le parcours d’action sont « conservés » pendant un jour. À la fin de la journée, si un utilisateur a démarré une session et effectué un achat, il passe au parcours de classement le plus élevé. Dans ce cas, l’utilisateur passerait au Groupe 1. 

Dans l’exemple précédent, si l’option **Classement** est désactivée et qu’un utilisateur effectue l’un des événements déclencheurs (« Démarrer une session » ou « Effectuer un achat »), cet utilisateur passe au groupe d’actions pertinent en fonction de l’action de déclenchement.

Notez que les propriétés d’entrée Canvas diffèrent des propriétés de l’événement. Les propriétés d’entrée Canvas sont des propriétés issues de l’événement qui a déclenché le Canvas. Ces propriétés peuvent être uniquement utilisées dans la première étape complète d’un Canvas. Inversement, les propriétés de l’événement proviennent d’un événement ou d’une action qui se produit lorsque l’utilisateur accède à son flux de travail.

### Groupes d’actions

Ajoutez un ou plusieurs déclencheurs pour définir vos groupes d’actions. À ce niveau, vous pouvez sélectionner une série d’événements déclencheurs tels que des [événements personnalisés][2], des événements d’engagement, par exemple des interactions avec votre application, et bien plus.

![][3]

Dans chacun des paramètres de groupe d’actions, vous pouvez également cocher la case **Je souhaite que ce groupe quitte Canvas**, ce qui signifie que les utilisateurs de ce groupe quitteront le Canvas à la fin de la période d’évaluation.

### Canvas avec rééligibilité

Si des utilisateurs accèdent plusieurs fois à un parcours d’action et disposent de plusieurs entrées dans ce dernier simultanément, le comportement prévu dépend du statut de **Classement**. 

| Statut de classement | Comportement de parcours d’action |
|---|--------------|
| **Désactivé** | Lorsqu’une action pertinente est exécutée, Braze dédupliquera les entrées et la première entrée passera au groupe d’actions pertinent. <br><br/> Lorsqu’aucune action pertinente n’est exécutée, toutes les entrées seront repoussées vers le bas de la fenêtre d’évaluation pertinente. Aucune déduplication n’est effectuée. |
| **Activé** | Toutes les entrées seront repoussées vers le bas de la fenêtre d’évaluation pertinente. Aucune déduplication n’est effectuée. |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {% image_buster /assets/img/canvas_actionpath.png %} 
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events
[3]: {% image_buster /assets/img/actionpath_group.png %} 
[4]: {% image_buster /assets/img/actionpath_settings.png %} 
