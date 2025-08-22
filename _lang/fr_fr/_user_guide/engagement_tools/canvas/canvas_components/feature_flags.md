---
nav_title: Indicateurs de fonctionnalité
article_title: Indicateurs de fonctionnalité
page_order: 8
page_type: reference
description: "Cet article de référence explique comment les indicateurs de fonctionnalité peuvent être utilisés dans Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Indicateurs de fonctionnalités

> Les indicateurs de fonctionnalités vous permettent d'expérimenter et de confirmer vos hypothèses autour de nouvelles fonctionnalités. Les marketeurs peuvent utiliser les drapeaux de fonctionnalité pour segmenter votre audience dans [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) et suivre l'impact du déploiement des fonctionnalités sur les conversions. De plus, les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) vous permettent d'optimiser ces conversions en testant différents messages ou chemins les uns par rapport aux autres et en déterminant lequel est le plus efficace. Utilisez le chemin gagnant pour déployer progressivement votre fonction à une audience plus large.

Vous souhaitez en savoir plus sur les indicateurs de fonctionnalités et leur utilisation dans Braze ? Consultez nos articles consacrés aux [drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/).

## Création d'un drapeau de fonctionnalité

![Un exemple d'étape de l'indicateur de fonctionnalité pour la fonctionnalité du bouton de la ligne/instantané.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Pour créer un composant Indicateur de fonctionnalité, ajoutez d'abord une étape à votre canvas. Glissez-déposez le composant depuis la barre latérale ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Drapeau de fonctionnalité**. Ensuite, sélectionnez l’indicateur de fonctionnalité dans la liste déroulante, qui contient tous les indicateurs de fonctionnalités qui ne sont pas archivés.

## Comment cette étape fonctionne-t-elle ?

Lorsqu'un Canvas est arrêté, archivé ou qu'une étape est supprimée, tout utilisateur qui est passé par cette étape ne recevra plus le drapeau de fonctionnalité de l'étape ni ses propriétés. L'utilisateur sera toujours soumis au pourcentage de déploiement par défaut et à la segmentation de l'audience pour cette fonctionnalité et pour toute autre toile encore active.

Les propriétés d'une étape de canvas peuvent être modifiées après le lancement, et même après qu'un utilisateur a franchi l'étape. Les utilisateurs recevront toujours une version dynamique et en temps réel de l'indicateur de fonctionnalité, au lieu de l'ancienne version enregistrée.

## Écrasement des propriétés

Lors de la création d'un indicateur de fonctionnalité, vous spécifiez des propriétés par défaut. Lors de la configuration d'une étape Canvas avec indicateur de fonctionnalité, vous pouvez soit conserver les valeurs par défaut, soit écraser les valeurs pour les utilisateurs qui entrent dans cette étape.

![Une fonctionnalité "Preference Center" avec "Chaîne de caractères" comme propriété, "url" comme clé de propriété et une valeur.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Allez dans **Messagerie** > **Indicateurs de fonctionnalité** pour modifier, ajouter ou supprimer des propriétés supplémentaires.

## Différences de canvas et de déploiement

Le canvas et le déploiement d'un drapeau de fonctionnalité (en faisant glisser le curseur) peuvent fonctionner indépendamment l'un de l'autre. Attention : l'entrée dans une étape du canvas écrase toute configuration de déploiement par défaut. Cela signifie que si un utilisateur ne remplit pas les conditions requises pour bénéficier d'un indicateur de fonctionnalité, une étape du canvas peut activer la fonctionnalité pour cet utilisateur.

De même, si un utilisateur se qualifie pour le déploiement d'un indicateur de fonctionnalité avec certaines propriétés, s'il entre également dans l'étape du canvas, il recevra toutes les valeurs écrasées de cette étape du canvas.

