---
nav_title: Examiner les actions
article_title: Examiner les actions de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Apprenez à examiner et approuver les actions lorsque BrazeAI Operator propose des modifications dans le tableau de bord."
---

# Examiner les actions de BrazeAI Operator

> Apprenez à examiner et approuver les actions lorsque BrazeAI Operator<sup>TM</sup> propose des modifications dans le tableau de bord.

![Operator présentant des cartes d'action suggérées pour examen.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Fonctionnement des cartes d'action

Lorsqu'Operator propose des modifications dans le tableau de bord (par ex. remplir des champs de formulaire, mettre à jour des paramètres ou générer des images), chaque modification est présentée sous forme de carte d'action à examiner.

1. **Operator résume le plan :** Operator explique ce qu'il prévoit de faire avant d'afficher les cartes d'action.
2. **Les cartes d'action individuelles apparaissent :** Chaque modification proposée est présentée sur une carte distincte indiquant ce qu'Operator souhaite modifier ou faire dans le tableau de bord. Pour les modifications de valeurs existantes, l'ancienne et la nouvelle valeur sont affichées côte à côte.
3. **Examiner et approuver :** Examinez chaque carte et approuvez-la ou refusez-la.
4. **L'action s'exécute :** Les actions approuvées sont exécutées dans Braze. Les actions refusées ne sont pas appliquées.

Si une action échoue après approbation, Operator vous en informe avec les détails de l'échec.

### Disponibilité

Les cartes d'action sont prises en charge dans les éditeurs suivants :

- Messages in-app (éditeur traditionnel uniquement)
- Content Cards
- E-mail (éditeur HTML uniquement)
- Notifications push
- SMS/MMS/RCS
- Webhooks

Sur les autres pages, Operator fournit une liste d'étapes à suivre dans l'interface au lieu d'exécuter les actions lui-même. Les fonctionnalités d'Operator sont régulièrement améliorées et une couverture élargie des outils de création est prévue.

## Modifier un plan

Pour modifier le plan d'Operator, approuvez ou rejetez d'abord les actions en attente. Ensuite, décrivez la modification souhaitée dans un nouveau message de chat.

Les actions approuvées ne peuvent pas être annulées via Operator. Décrivez la nouvelle modification à Operator ou effectuez les modifications manuellement dans le tableau de bord.

## Approbation automatique des actions

Le bouton **Approbation automatique des actions** se trouve dans le panneau de chat Operator.

- **Activé :** Les actions suggérées par Operator s'exécutent immédiatement sans approbation manuelle. Certaines actions nécessitent encore une approbation explicite pour des raisons de sécurité, comme la génération d'images ou les modifications au niveau de l'espace de travail.
- **Désactivé (par défaut) :** Toutes les actions proposées suivent le processus d'examen manuel décrit.

![Le bouton d'approbation automatique et la fenêtre de confirmation dans le panneau de chat Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

L'approbation automatique est réinitialisée lorsque vous actualisez la page, ouvrez un nouvel onglet ou vous déconnectez et reconnectez. Passer d'une page à l'autre dans le tableau de bord ne la réinitialise pas. Vous pouvez désactiver l'approbation automatique à tout moment.
