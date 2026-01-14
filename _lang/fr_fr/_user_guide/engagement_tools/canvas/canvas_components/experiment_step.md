---
nav_title: "Chemins d'expérience"
article_title: "Chemins d'expérience" 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Cet article traite des chemins d'expérience, un composant qui vous permet de tester plusieurs chemins Canvas les uns par rapport aux autres ainsi qu'un groupe de contrôle à n'importe quel moment du parcours de l'utilisateur."
tool: Canvas
---

# Chemins d'expérience

> Les chemins d'expérience vous permettent de tester plusieurs chemins Canvas les uns par rapport aux autres ainsi qu'un groupe de contrôle à n'importe quel moment du parcours de l'utilisateur. Grâce à ce composant, vous pouvez suivre les performances des chemins pour prendre des décisions éclairées sur votre parcours Canvas.

Lorsque vous incluez une étape des chemins d'expérience dans votre parcours utilisateur, elle affectera de manière aléatoire les utilisateurs à différents chemins (ou à un groupe de contrôle facultatif) que vous aurez créés. Des parties de l'audience seront affectées à différents parcours en fonction des pourcentages que vous aurez sélectionnés, ce qui vous permettra de tester différents messages ou parcours les uns par rapport aux autres et de déterminer lequel est le plus efficace. 

\![Une étape des chemins d'expérience qui se divise en chemin 1, chemin 2 et contrôle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Cas d'utilisation

Les chemins d'expérience sont les mieux adaptés pour tester la réception/distribution, la cadence, le texte du message et les combinaisons de canaux.

- **Réception/distribution :** Comparez les résultats entre des messages envoyés avec différents [délais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en fonction des actions de l'utilisateur[(parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), et en utilisant le [timing intelligent.]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas)<br><br>
- **Cadence :** Testez plusieurs envois de messages sur une période donnée. Par exemple, vous pourriez tester deux cadences d'onboarding différentes :
    - Cadence 1 : Envoyez 2 messages au cours des 2 premières semaines de l'utilisateur.
    - Cadence 2 : Envoyez 3 messages au cours des deux premières semaines de l'utilisateur.
    
    Lorsque vous ciblez des utilisateurs en fin de carrière, vous pouvez tester l'efficacité de l'envoi de deux messages de reconquête en une semaine par rapport à l'envoi d'un seul message.
- **Envoi de messages :** À l'instar d'un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) standard, vous pouvez tester différents textes de messages pour voir quelle formulation permet d'obtenir un taux de conversion plus élevé.<br><br>
- **Combinaisons de canaux :** Testez l'efficacité de différentes combinaisons de canaux de communication. Par exemple, vous pouvez comparer l'impact de l'utilisation d'un simple e-mail à celui d'un e-mail combiné à un push.

## Prérequis

Pour utiliser les chemins d'expérience, votre Canvas doit comporter des événements de conversion. Bien que vous ne puissiez pas ajouter d'événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et ajouter des événements de conversion pour ajouter des chemins d'expérience.

## Création d'un chemin d'expérience

Pour créer un composant Chemins d'expérience, ajoutez d'abord une étape à votre Canvas. Glissez-déposez le composant depuis la barre latérale ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Chemins d'expérience**. 

Dans la configuration par défaut de ce composant, il existe deux parcours par défaut, le **parcours 1** et le **parcours 2**, 50 % de l'audience étant envoyée sur chaque parcours. Cliquez sur le composant pour développer le panneau **Paramètres de l'expérience**, et vous verrez les options de configuration pour le composant.

### Étape 1 : Choisissez le nombre de parcours et la répartition de l'audience

Vous pouvez ajouter jusqu'à quatre chemins en cliquant sur **Ajouter un chemin** et un groupe de contrôle facultatif en cochant **Ajouter un groupe de contrôle**. En utilisant les cases de pourcentage pour chaque parcours, vous pouvez spécifier le pourcentage de l'audience qui doit aller à chaque parcours et au groupe de contrôle. La somme des pourcentages fournis doit être égale à 100 % pour que la procédure puisse être poursuivie. Si vous souhaitez définir rapidement le même pourcentage pour tous les chemins disponibles (et le contrôle), cliquez sur **Distribuer les chemins de façon homogène**.

Vous pouvez également choisir si les utilisateurs du groupe **de** contrôle doivent continuer à descendre dans le canvas ou sortir après la fenêtre de suivi des conversions pour le **comportement du groupe de contrôle.** En option, vous pouvez ajouter une description pour expliquer aux autres ce que ce chemin d'expérience a l'intention de tester ou inclure des informations supplémentaires qui pourraient être utiles à noter.

\![Paramètres d'expérience où vous pouvez ajouter des chemins et distribuer le pourcentage d'utilisateurs dans chaque chemin.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité au Canvas est activée, les utilisateurs qui entrent dans le Canvas et empruntent un chemin choisi au hasard emprunteront à nouveau le même chemin s'ils deviennent rééligibles et entrent à nouveau dans le Canvas. Cela permet de maintenir la validité de l'expérience et des analyses/analytiques associées (si utilisées anjectives). Si vous souhaitez que l'étape randomise toujours l'attribution des chemins, sélectionnez **Chemins randomisés dans Chemins d'expérience.** Cette option n'est pas disponible lorsque vous utilisez les chemins gagnants ou personnalisés.
{% endalert %}

### Étape 2 : Activer le chemin gagnant ou les chemins personnalisés (facultatif) {#step-2}

Vous pouvez choisir d'optimiser votre expérience en activant les options [Chemin gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) ou [Chemins personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Les deux options fonctionnent en testant initialement vos parcours auprès d'une partie de votre audience. À la fin de l'expérience, les utilisateurs restants et les suivants sont envoyés sur le chemin le plus performant (chemin gagnant) ou sur le chemin le plus performant pour chaque utilisateur (chemins personnalisés).

### Étape 3 : Créer des chemins

Enfin, vous devez créer vos parcours en aval. Sélectionnez **Terminé** et revenez au générateur de canvas. Cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus sous chaque chemin pour commencer à créer des parcours à l'aide des outils Canvas habituels, comme bon vous semble, et lancez le Canvas lorsque vous êtes prêt.

\![Ajout d'étapes à chaque chemin qui se sépare d'un composant de chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

N'oubliez pas que les chemins et leurs étapes en aval ne peuvent pas être supprimés d'un canvas après leur création. Cependant, une fois lancé, vous pouvez modifier la répartition de l'audience entre les parcours d'audience comme bon vous semble. Par exemple, si un jour après avoir lancé un Canvas, vous concluez qu'un chemin est supérieur aux autres sur la base des analyses/analytiques, vous pouvez définir ce chemin à 100 % et les autres à 0 %. Ou, selon vos besoins, vous pouvez continuer à envoyer les utilisateurs sur plusieurs chemins.

{% alert important %}
Pour éviter la contamination des expériences, si votre Canvas comporte une expérience de chemin gagnant ou de chemin personnalisé active ou en cours et que vous mettez à jour le Canvas actif, indépendamment du fait que vous mettiez à jour l'étape des chemins d'expérience elle-même, l'expérience en cours prendra fin et l'étape de l'expérience ne déterminera pas de chemin gagnant ou de chemins personnalisés. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. Dans le cas contraire, les utilisateurs suivront le chemin d'expérience comme si aucune méthode d'optimisation n'avait été sélectionnée. Vous ne pouvez pas non plus activer les Chemins personnalisés ou les Chemins gagnants pour un Canvas déjà actif avec une étape du chemin d'expérience.<br><br>Pour plus d'informations, reportez-vous à la section [Modifier les toiles après le lancement]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Suivi des performances

Dans la page **Canvas Analytics**, sélectionnez le chemin d'expérience pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identique à l'onglet **Analyser les variantes** afin de comparer les statistiques détaillées de performance et de conversion entre les chemins. Vous pouvez également exporter le tableau au format CSV et comparer les variations en pourcentage des indicateurs qui vous intéressent par rapport à la voie ou au contrôle que vous avez sélectionné.

Chaque étape de chaque chemin affichera des statistiques dans la vue [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) (comme n'importe quelle étape de Canvas). Cependant, gardez à l'esprit que les analyses/analytiques des différentes étapes **ne tiennent pas** compte de la structure de l'expérience. L'analyse/analytique de l'étape des chemins d'expérience doit être utilisée pour comparer les chemins.

### Performances des parcours gagnants et des parcours personnalisés

Tirez parti des parcours gagnants pour suivre les performances sur une période donnée, puis envoyez automatiquement les utilisateurs suivants sur le parcours le plus performant. Pour plus d'informations sur l'analyse/analytique lorsque le **chemin gagnant** ou les **chemins personnalisés** sont activés pour votre expérience, reportez-vous à :

- [Le chemin de la victoire]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Chemins personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Paramètres supplémentaires

Les chemins d'expérience enregistreront les utilisateurs qui entrent dans chaque étape et se convertissent pendant qu'ils se trouvent dans le chemin assigné. Cela permet de suivre tous les événements de conversion spécifiés dans la configuration de Canvas. Dans l'onglet **Paramètres supplémentaires**, indiquez le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La fenêtre temporelle que vous spécifiez ici déterminera la durée pendant laquelle les événements de conversion (choisis dans la configuration de Canvas) seront suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration du canvas ne s'appliqueront pas au suivi de cette étape et seront remplacées par cette fenêtre de conversion.

