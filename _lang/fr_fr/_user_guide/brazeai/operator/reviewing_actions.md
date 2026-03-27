---
nav_title: Vérifier les actions
article_title: Examen des actions de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator propose des modifications dans le tableau de bord."
---

# Examen des actions de BrazeAI Operator

> Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator<sup>TM</sup> propose des modifications dans le tableau de bord.

![Operator présente les cartes d'action suggérées pour examen.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Fonctionnement des cartes d'action

Lorsque Operator propose des modifications dans le tableau de bord (telles que remplir des champs de formulaire, mettre à jour des paramètres ou générer des images), il présente chaque modification sous forme de carte d'action à examiner.

1. **Operator résume le plan :** Operator explique ce qu'il prévoit de faire avant d'afficher les cartes d'action.
2. **Les cartes d'action individuelles apparaissent :** Chaque modification proposée est présentée sous forme de carte distincte qui indique ce qu'Operator souhaite modifier ou effectuer dans le tableau de bord. Pour les modifications apportées à des valeurs existantes, la valeur précédente et la valeur proposée sont affichées côte à côte pour comparaison.
3. **Examinez et approuvez :** Passez en revue chaque carte, puis approuvez-la ou refusez-la.
4. **L'action est exécutée :** Les actions approuvées sont exécutées dans Braze. Les actions refusées ne sont pas appliquées.

Si une action échoue après approbation, Operator vous en informe avec les détails de l'échec.

### Disponibilité

Les cartes d'action sont prises en charge dans les éditeurs et pages suivants.

- **Éditeurs de messages :**
    - Messages in-app (éditeur traditionnel uniquement)
    - Cartes de contenu
    - E-mail (éditeur HTML uniquement)
    - Notifications push
    - SMS/MMS/RCS
    - Webhooks
- Page [Créer un agent personnalisé]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
 
Sur les autres pages, Operator fournit une liste d'étapes à suivre dans l'interface utilisateur au lieu d'agir lui-même. Les fonctionnalités d'Operator sont régulièrement améliorées, et une couverture élargie des outils de création est prévue.

## Modifier un plan

Pour modifier le plan d'Operator, commencez par approuver ou rejeter les actions en attente. Décrivez ensuite le changement souhaité dans un nouveau message.

Les actions approuvées ne peuvent pas être annulées via Operator. Décrivez la nouvelle modification à Operator ou effectuez les changements manuellement dans le tableau de bord.

## Approbation automatique des actions

Le bouton **Approbation automatique des actions** se trouve dans le panneau de discussion d'Operator.

- **Activé :** Les actions suggérées par Operator sont exécutées immédiatement sans nécessiter d'approbation manuelle. Certaines actions nécessitent toujours une approbation explicite pour des raisons de sécurité, comme la génération d'images ou la modification de paramètres au niveau de l'espace de travail.
- **Désactivé (par défaut) :** Toutes les actions proposées suivent le processus de vérification manuelle décrit ci-dessus.

![Le bouton d'approbation automatique et la boîte de dialogue modale de confirmation dans le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

L'approbation automatique se réinitialise lorsque vous actualisez la page, ouvrez un nouvel onglet ou vous déconnectez puis vous reconnectez. Naviguer entre les pages du tableau de bord ne la réinitialise pas. L'approbation automatique peut être désactivée à tout moment.