---
nav_title: Vérifier les actions
article_title: Examen des actions de BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator propose des modifications dans le tableau de bord."
---

# Examen des actions de l'opérateur BrazeAI

> Découvrez comment examiner et approuver les actions lorsque BrazeAI Operator<sup>TM</sup> propose des modifications dans le tableau de bord.

![L'opérateur présente les cartes d'action suggérées pour examen.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Fonctionnement des cartes Action

Lorsque l'opérateur propose des modifications dans le tableau de bord (telles que remplir des champs de formulaire, mettre à jour des paramètres ou générer des images), il présente chaque modification sous forme de carte d'action à examiner.

1. **L'opérateur résume le plan :** L'opérateur explique ce qu'il prévoit de faire avant de montrer les cartes d'action.
2. **Les cartes d'action individuelles apparaissent :** Chaque modification proposée est présentée sous forme de carte distincte qui indique ce que l'opérateur souhaite modifier ou effectuer dans le tableau de bord. Pour les modifications apportées aux valeurs existantes, la valeur précédente et la valeur proposée sont présentées côte à côte à des fins de comparaison.
3. **Veuillez examiner et approuver :** Veuillez examiner chaque carte et l'approuver ou la refuser.
4. **L'action est exécutée :** Les actions approuvées sont exécutées dans Braze. Les actions refusées ne sont pas appliquées.

Si une action échoue après avoir été approuvée, l'opérateur vous informera des détails de l'échec.

### Disponibilité

Les cartes d'action sont prises en charge dans les éditeurs suivants :

- Message in-app (éditeur traditionnel uniquement)
- Cartes de contenu
- E-mail (éditeur HTML uniquement)
- Notifications push
- SMS/MMS/RCS
- Webhooks

Sur d'autres pages, Operator fournit une liste d'étapes à suivre dans l'interface utilisateur au lieu d'agir lui-même. Les fonctionnalités de l'opérateur sont régulièrement améliorées, et une couverture élargie pour les outils de création est prévue.

## Modifier un plan

Pour modifier le plan de l'opérateur, veuillez d'abord approuver ou rejeter les actions en attente. Veuillez ensuite décrire le changement souhaité dans un nouveau message instantané.

Les actions approuvées ne peuvent pas être annulées via Operator. Veuillez décrire la nouvelle modification à l'opérateur ou effectuer les modifications manuellement dans le tableau de bord.

## Actions d'approbation automatique

Le bouton **pour basculer entre les modes d'approbation automatique des actions** se trouve dans le panneau de discussion de l'opérateur.

- **Activé :** Les actions suggérées par l'opérateur sont exécutées immédiatement sans nécessiter d'approbation manuelle. Certaines actions nécessitent toujours une autorisation explicite pour des raisons de sécurité, telles que la génération d'images ou la modification des paramètres au niveau de l'espace de travail.
- **Désactivé (par défaut) :** Toutes les actions proposées suivent le processus de révision manuelle décrit.

![Le bouton d'approbation automatique et la fenêtre modale de confirmation dans le panneau de discussion de l'opérateur.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

La fonction d'approbation automatique se réinitialise lorsque vous actualisez la page, ouvrez un nouvel onglet ou vous déconnectez puis vous reconnectez. Le fait de passer d'une page à l'autre dans le tableau de bord ne le réinitialise pas. La fonction d'approbation automatique peut être désactivée à tout moment.
