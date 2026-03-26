---
nav_title: Chemins d’expérience
article_title: Chemins d’expérience 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Cet article couvre les chemins d’expérience, un composant qui vous permet de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur."
tool: Canvas
---

# Chemins d’expérience

> Les chemins d’expérience vous permettent de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur. Grâce à ce composant, vous pouvez suivre les performances des parcours afin de prendre des décisions éclairées concernant votre parcours canvas.

Lorsque vous incluez une étape des chemins d’expérience dans votre parcours utilisateur, celle-ci attribuera de manière aléatoire les utilisateurs à différents chemins d’expérience (ou à un groupe de contrôle facultatif) que vous aurez créés. Une partie de l'audience sera affectée à différents parcours en fonction des pourcentages que vous aurez sélectionnés, ce qui vous permettra de tester différents messages ou parcours les uns par rapport aux autres et de déterminer lequel est le plus efficace. 

![Une étape des chemins d’expérience qui se divise en parcours 1, parcours 2 et contrôle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Cas d’utilisation

Les chemins d’expérience sont les mieux adaptés pour tester la livraison, la cadence, la copie de message et les combinaisons de canaux.

- **Livraison :** Comparez les résultats entre les messages envoyés avec différents [délais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), en fonction des actions des utilisateurs ([Chemins d'Action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), et en utilisant [Minutage Intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadence :** Tester plusieurs flux d’envoi de messages sur une période donnée. Par exemple, vous pourriez tester deux cadences d’onboarding différentes :
    - Cadence 1 : Envoyer 2 messages dans les 2 premières semaines de l’utilisateur
    - Cadence 2 : Envoyer 3 messages dans les 2 premières semaines de l’utilisateur
    
    Vous pouvez également tester l’efficacité d’envoyer deux messages de reconquête dans une semaine, ou en envoyer juste un lorsque vous ciblez les utilisateurs inactifs.
- **Texte du message :** Similaire à un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/), vous pouvez tester différents messages pour voir quelle formulation entraîne un taux de conversion plus élevé.<br><br>
- **Combinaisons de chaînes:** Tester l’efficacité de différentes combinaisons de canaux de messages. Par exemple, vous pouvez comparer l’impact entre un seul e-mail et un e-mail combiné à une notification push.

## Prérequis

Pour utiliser les chemins d’expérience, votre canevas doit inclure des événements de conversion. Bien qu'il ne soit pas possible d'ajouter des événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et ajouter des événements de conversion pour ajouter des chemins d’expérience.

## Création d'un chemin d'expérience

Pour créer un composant de chemins d'expérience, ajoutez d'abord une étape à votre canvas. Faites glisser et déposez le composant de la barre latérale, ou cliquez sur le <i class="fas fa-plus-circle"></i> bouton plus en bas d'une étape et sélectionnez **Chemins d'Expérimentation**. 

Dans la configuration par défaut de ce composant, il existe deux parcours par défaut, **Parcours 1** et **Parcours 2**, 50 % de l’audience étant envoyés vers chaque parcours. Cliquez sur le composant pour développer le panneau **Paramètres de l'expérience**, et vous verrez les options de configuration pour le composant.

### Étape 1 : Choisissez le nombre de chemins et la répartition de l’audience

Vous pouvez ajouter jusqu'à quatre chemins en cliquant sur **Ajouter un chemin** et un groupe de contrôle facultatif en cochant **Ajouter un groupe de contrôle**. À l’aide des cases de pourcentage de chaque chemin, vous pouvez indiquer le pourcentage de l’audience qui doit être associé à chaque chemin et le groupe de contrôle. Le total des pourcentages indiqués, additionnés doit être de 100 % pour continuer. Si vous souhaitez définir rapidement tous les chemins disponibles (et contrôler) au même pourcentage, cliquez sur **Répartir les chemins uniformément**.

Vous pouvez également choisir si les utilisateurs du groupe de contrôle doivent continuer sur le Canvas ou sortir après la fenêtre de suivi de conversion pour le **Comportement du groupe de contrôle**. Optionnellement, vous pouvez ajouter une description pour expliquer aux autres ce que ce chemin d'expérimentation vise à tester ou inclure des informations supplémentaires qui pourraient être utiles à noter.

![Paramètres d’expérience dans lesquels vous pouvez ajouter des chemins et distribuer le pourcentage d’utilisateurs dans chaque chemin.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité Canvas est activée, les utilisateurs qui accèdent à Canvas et à un chemin choisi de manière aléatoire, accèderont à nouveau au même chemin s’ils deviennent rééligibles et accèdent à nouveau au Canvas. Ce processus permet de conserver la validité de l’expérience et l’analyse associée. Si vous souhaitez que l'étape randomise toujours l'attribution des chemins, sélectionnez **Chemins aléatoires dans les chemins d'expérience**. Cette option n'est pas disponible lors de l'utilisation des chemins gagnants ou personnalisés.
{% endalert %}

### Étape 2 : Activez le chemin gagnant ou les chemins personnalisés (facultatif) {#step-2}

Vous pouvez choisir d'optimiser votre expérience en activant [Chemin Gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) ou [Chemins Personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Les deux options fonctionnent en testant initialement vos chemins avec une partie de votre audience. Une fois l'expérience terminée, les utilisateurs restants et suivants sont dirigés soit vers le parcours le plus performant dans l'ensemble (parcours gagnant), soit vers le parcours le plus performant pour chaque utilisateur (parcours personnalisés).

### Étape 3 : Créer des chemins

Enfin, vous devez créer vos chemins en aval. Sélectionnez **Terminé** et revenez au créateur de Canvas. Cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> sous chaque chemin pour commencer la création des parcours à l’aide des outils habituels Canvas comme bon vous semble et lancez le Canvas quand vous êtes prêt.

![Ajout d’étapes à chaque chemin qui se sépare d'un composant Chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Gardez à l'esprit que les chemins et leurs étapes en aval ne peuvent pas être supprimés d'une toile après leur création. Cependant, une fois lancé, vous pouvez modifier la distribution de l'audience entre les chemins comme bon vous semble. Par exemple, si un jour après le lancement d’un Canvas vous concluez qu’un chemin est supérieur au reste en fonction de l’analyse, vous pouvez définir ce chemin sur 100 % et les autres sur 0 %. Ou, selon vos besoins, vous pouvez continuer l’envoi des utilisateurs vers plusieurs chemins.

{% alert important %}
Afin d'éviter toute contamination de l'expérience, si votre canevas comporte une expérience Winning Path ou Personalized Path active ou en cours et que vous mettez à jour le canevas actif, que vous mettiez à jour ou non l'étape du chemin d’expérience elle-même, l'expérience en cours prendra fin et l'étape du chemin d’expérience ne déterminera pas de chemin gagnant ni de chemins personnalisés. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. Dans le cas contraire, les utilisateurs suivront le chemin d’expérience comme si aucune méthode d’optimisation n’avait été sélectionnée. Vous ne pouvez pas non plus activer les chemins personnalisés ou les chemins gagnants pour un canvas déjà actif avec une étape Chemin d’expérience.<br><br>Pour plus d'informations, consultez [Modification d’un canvas après son lancement]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Suivi de la performance

Dans la page **Canvas Analytics**, veuillez sélectionner le chemin d’expérience pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identique à l’onglet **Analyser les variantes** afin de comparer les statistiques détaillées de performance et de conversion entre les différents chemins. Vous pouvez également exporter la table via CVS et comparer le pourcentage de modifications pour les indicateurs d’intérêt par rapport au chemin ou au contrôle que vous sélectionnez.

Chaque étape de chaque parcours affiche des statistiques dans la vue [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), comme n'importe quelle étape du canvas. Veuillez toutefois noter que l'analyse des étapes individuelles et l'analyse du chemin d’expérience mesurent les conversions différemment :

- **Les analyses du chemin d’expérience** suivent les conversions à partir du moment où l'utilisateur entre dans l'étape du chemin d’expérience. Il s'agit de la vue recommandée pour comparer les performances entre les chemins, car tous les chemins partagent le même point de départ.
- **Les analyses par étape individuelles** (telles que les analyses par étape de message) suivent les conversions à partir du moment où l'utilisateur reçoit cette étape spécifique (par exemple, lorsque le message est envoyé).

Étant donné que ces fenêtres de conversion ont des points de départ différents, elles peuvent afficher des taux de conversion différents pour un même parcours, en particulier lorsqu'il y a des délais entre l'étape de l'expérience et un message en aval. Pour obtenir la comparaison la plus fiable entre les différents chemins, veuillez utiliser les analyses de chemin d’expérience.

### Performance du chemin gagnant et des chemins personnalisés

Tirez parti des chemins gagnants pour suivre la performance au cours du temps puis envoyez automatiquement les utilisateurs suivants sur le chemin ayant la meilleure performance. Pour plus d'informations sur l'analyse lorsque **Winning Path** ou **Personalized Paths** sont activés pour votre expérience, consultez :

- [Chemin gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Chemins personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Paramètres supplémentaires

Les chemins d’expérience enregistrent les utilisateurs qui franchissent chaque étape et effectuent une conversion dans le chemin attribué. Ceci permet de suivre tous les événements de conversion spécifiés dans la configuration de Canvas. Dans l'onglet **Paramètres supplémentaires**, veuillez indiquer le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La période que vous indiquez ici détermine la durée pendant laquelle les événements de conversion (sélectionnés dans la configuration Canvas) sont suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration Canvas ne s'appliquent pas au suivi de l'étape du canvas et sont remplacées par cette fenêtre de conversion.

La fenêtre de conversion commence lorsque l'utilisateur accède à l'étape des chemins d'expérience, et non lorsqu'un message en aval est envoyé. Si un chemin comprend des délais, tels qu'une étape de délai ou [un timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), ces délais occupent une partie de la fenêtre de conversion.

{% alert important %}
Si vous utilisez la fonctionnalité de timing intelligent sur une étape Message dans un chemin d’expérience, le délai entre l’entrée dans l’expérience et l’envoi effectif du message réduit la fenêtre de conversion effective pour ce chemin d’expérience. Par exemple, si votre expérience dispose d'une fenêtre de conversion de 5 jours et que la fonctionnalité de timing intelligent retarde le message de 2 jours, les utilisateurs suivant ce parcours ne disposent que de 3 jours après réception du message pour effectuer une conversion dans la fenêtre de l'expérience, même si les analyses de l'étape Message suivent les conversions à partir du moment où le message est envoyé.<br><br>Pour une analyse plus claire des expériences, veuillez placer les délais (tels que les étapes Delay) **avant** l'étape des chemins d'expérience plutôt que dans un chemin d’expérience. De cette manière, tous les chemins partent du même point et les retards n'affectent pas la fenêtre de conversion.
{% endalert %}