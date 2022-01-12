---
nav_title: Étape des chemins d'action
article_title: Étape des chemins d'action
alias: /fr/action_paths/
page_order: 1
page_type: Référence
description: "Cet article de référence couvre les Chemins d'Action et comment les utiliser dans vos Canvases."
tool: Toile
---

# Étape des chemins d'action

Les chemins d'action dans Canvas vous permettent de trier vos utilisateurs en fonction de leurs actions. En utilisant les chemins d'action, vous pouvez faire ce qui suit :

* Personnaliser les chemins de l'utilisateur en fonction d'une action spécifique
* Conservez les utilisateurs pendant une durée donnée pour prioriser leur chemin suivant en fonction de leurs actions pendant cette période d'évaluation

{% alert note %}
Les chemins d'action sont progressivement déployés vers toutes les instances de Braze, donc il y a une chance que vous ne puissiez pas encore voir le composant Chemins d'Action dans votre Toile. Si vous souhaitez un accès immédiat, veuillez contacter votre responsable de compte Braze ou votre représentant pour la réussite de la clientèle.
{% endalert %}

## Créer des chemins d'action

!\[canvas_actionpath\]\[1\]{: style="float:right;max-width:40%;margin-left:15px;"}

Pour créer des chemins d'action, ajoutez une étape à votre Canevas. Ensuite, en utilisant le menu déroulant en haut de la nouvelle étape, sélectionnez **Chemins d'action**.

### Définir les paramètres d'action

Dans le module **Paramètres d'action** , vous pouvez choisir la durée de conservation des utilisateurs dans l'étape d'action.

Lorsque le classement **** est désactivé, les utilisateurs qui effectuent des actions après avoir entré le chemin de l'action et avant la fin de la fenêtre d'évaluation vont immédiatement passer par le groupe d'action concerné dès qu'ils effectuent l'action. Les utilisateurs qui n'effectuent pas une action pertinente pendant la période d'évaluation passeront par le groupe par défaut **Tout le monde d'autre** à la fin de la période d'évaluation.

Lorsque le **Classement** est activé, tous les utilisateurs seront tenus jusqu'à la fin de la période d'évaluation. À la fin de la période d'évaluation, les utilisateurs passeront par le groupe d'action prioritaire auquel ils sont éligibles. Les utilisateurs qui n'effectuent aucune action pendant la période d'évaluation passeront par le groupe par défaut **Tout le monde d'autre**.

### Définir les groupes d'action

Ajoutez un déclencheur ou plusieurs déclencheurs pour définir vos groupes d'action.

Lorsque le classement **** est désactivé, les utilisateurs qui effectuent un ou plusieurs des déclencheurs avanceront immédiatement à travers le groupe d'action concerné.

Quand **le classement** est activé, vous pouvez prioriser les groupes d'action. L'utilisateur poursuivra vers le bas le groupe de priorité le plus élevé auquel il est admissible à la fin de la période d'évaluation.

### Canevas avec rééligibilité

Si les utilisateurs entrent dans un chemin d'action plusieurs fois et ont plusieurs entrées dans le chemin d'action en même temps, le comportement attendu varie en fonction du **Classement**:

| Filtre de Classement | Comportement du chemin d'action                                                                                                                                                                                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Désactivé**        | * Lorsqu'une action pertinente est effectuée, Braze dédupliquera les entrées et fera avancer immédiatement l'entrée la plus précoce à travers le groupe d'action concerné. <br /> * Lorsqu'une action pertinente n'est pas effectuée, toutes les entrées avanceront à la fin de la fenêtre d'évaluation pertinente. Aucune déduplication ne se produira. |
| **Activé**           | Toutes les inscriptions se feront à la fin de la fenêtre d'évaluation pertinente. Aucune déduplication ne se produira.                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}
[1]: {% image_buster /assets/img/canvas_actionpath.png %} 
