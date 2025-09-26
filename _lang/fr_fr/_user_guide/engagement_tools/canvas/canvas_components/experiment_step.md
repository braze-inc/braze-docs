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

> Les chemins d’expérience vous permettent de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur. Grâce à ce composant, vous pouvez suivre les performances des chemins pour prendre des décisions éclairées sur votre parcours Canvas.

Lorsque vous incluez une étape des chemins d'expérience dans votre parcours utilisateur, elle affectera de manière aléatoire les utilisateurs à différents chemins (ou à un groupe de contrôle facultatif) que vous aurez créés. Des parties de l'audience seront affectées à différents parcours en fonction des pourcentages que vous aurez sélectionnés, ce qui vous permettra de tester différents messages ou parcours les uns par rapport aux autres et de déterminer lequel est le plus efficace. 

![Une étape des chemins d'expérience qui se divise en chemin 1, chemin 2 et contrôle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

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

Pour utiliser les chemins d'expérience, votre Canvas doit comporter des événements de conversion. Bien que vous ne puissiez pas ajouter d'événements de conversion après le lancement d'un Canvas, vous pouvez cloner le Canvas lancé et ajouter des événements de conversion pour ajouter des chemins d'expérience.

## Création d'un chemin d'expérience

Pour créer un composant de chemins d'expérience, ajoutez d'abord une étape à votre canvas. Faites glisser et déposez le composant de la barre latérale, ou cliquez sur le <i class="fas fa-plus-circle"></i> bouton plus en bas d'une étape et sélectionnez **Chemins d'Expérimentation**. 

Dans la configuration par défaut de ce composant, il existe deux parcours par défaut, **Parcours 1** et **Parcours 2**, 50 % de l’audience étant envoyés vers chaque parcours. Cliquez sur le composant pour développer le panneau **Paramètres de l'expérience**, et vous verrez les options de configuration pour le composant.

### Étape 1 : Choisissez le nombre de chemins et la répartition de l’audience

Vous pouvez ajouter jusqu'à quatre chemins en cliquant sur **Ajouter un chemin** et un groupe de contrôle facultatif en cochant **Ajouter un groupe de contrôle**. À l’aide des cases de pourcentage de chaque chemin, vous pouvez indiquer le pourcentage de l’audience qui doit être associé à chaque chemin et le groupe de contrôle. Le total des pourcentages indiqués, additionnés doit être de 100 % pour continuer. Si vous souhaitez définir rapidement tous les chemins disponibles (et contrôler) au même pourcentage, cliquez sur **Répartir les chemins uniformément**.

Vous pouvez également choisir si les utilisateurs du groupe de contrôle doivent continuer sur le Canvas ou sortir après la fenêtre de suivi de conversion pour le **Comportement du groupe de contrôle**. Optionnellement, vous pouvez ajouter une description pour expliquer aux autres ce que ce chemin d'expérimentation vise à tester ou inclure des informations supplémentaires qui pourraient être utiles à noter.

![Paramètres d'expérience où vous pouvez ajouter des chemins et distribuer le pourcentage d'utilisateurs dans chaque chemin.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Si la rééligibilité Canvas est activée, les utilisateurs qui accèdent à Canvas et à un chemin choisi de manière aléatoire, accèderont à nouveau au même chemin s’ils deviennent rééligibles et accèdent à nouveau au Canvas. Ce processus permet de conserver la validité de l’expérience et l’analyse associée. Si vous souhaitez que l'étape randomise toujours l'attribution des chemins, sélectionnez **Chemins aléatoires dans les chemins d'expérience**. Cette option n'est pas disponible lors de l'utilisation des chemins gagnants ou personnalisés.
{% endalert %}

### Étape 2 : Activez le chemin gagnant ou les chemins personnalisés (facultatif) {#step-2}

Vous pouvez choisir d'optimiser votre expérience en activant [Chemin Gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) ou [Chemins Personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Les deux options fonctionnent en testant initialement vos chemins avec une partie de votre audience. À la fin de l'expérience, les utilisateurs restants et les suivants sont envoyés sur le chemin le plus performant (chemin gagnant) ou sur le chemin le plus performant pour chaque utilisateur (chemins personnalisés).

### Étape 3 : Créer des chemins

Enfin, vous devez créer vos chemins en aval. Sélectionnez **Terminé** et revenez au créateur de Canvas. Cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> sous chaque chemin pour commencer la création des parcours à l’aide des outils habituels Canvas comme bon vous semble et lancez le Canvas quand vous êtes prêt.

![Ajout d'étapes à chaque chemin qui se sépare d'un composant de chemin d'expérience.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Gardez à l'esprit que les chemins et leurs étapes en aval ne peuvent pas être supprimés d'une toile après leur création. Cependant, une fois lancé, vous pouvez modifier la distribution de l'audience entre les chemins comme bon vous semble. Par exemple, si un jour après le lancement d’un Canvas vous concluez qu’un chemin est supérieur au reste en fonction de l’analyse, vous pouvez définir ce chemin sur 100 % et les autres sur 0 %. Ou, selon vos besoins, vous pouvez continuer l’envoi des utilisateurs vers plusieurs chemins.

{% alert important %}
Pour éviter la contamination des expériences, si votre Canvas comporte une expérience active ou en cours et que vous mettez à jour le Canvas actif (même si ce n'est pas à l'étape du chemin d'expérience), l'expérience en cours prendra fin. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. Vous ne pouvez pas non plus activer les chemins personnalisés ou les chemins gagnants pour un canvas déjà actif avec une étape Chemin d’expérience.<br><br>Pour plus d'informations, consultez [Modification d’un canvas après son lancement]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Suivi de la performance

Depuis la page **Canvas Analytics**, cliquez sur le chemin d'expérimentation pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identique à l'onglet **Analyser les variantes** pour comparer les statistiques détaillées de performance et de conversion entre les chemins. Vous pouvez également exporter la table via CVS et comparer le pourcentage de modifications pour les indicateurs d’intérêt par rapport au chemin ou au contrôle que vous sélectionnez.

Chaque étape de chaque chemin affichera des statistiques dans la vue [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), tout comme n'importe quelle étape de Canvas. Cependant, gardez à l'esprit que les analyses/analytiques des différentes étapes **ne tiennent pas** compte de la structure de l'expérience. Les analyses de l’étape d’expérience doivent être utilisées pour comparer les chemins.

### Performance du chemin gagnant et des chemins personnalisés

Tirez parti des chemins gagnants pour suivre la performance au cours du temps puis envoyez automatiquement les utilisateurs suivants sur le chemin ayant la meilleure performance. Pour plus d'informations sur l'analyse lorsque **Winning Path** ou **Personalized Paths** sont activés pour votre expérience, consultez :

- [Chemin gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Chemins personnalisés]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Paramètres supplémentaires

Les chemins d’expérience enregistreront les utilisateurs qui accèdent à chaque étape et effectuent une conversion dans le chemin affecté. Ceci effectuera le suivi de tous les événements de conversion indiqués dans la configuration Canvas. Dans l'onglet **Paramètres supplémentaires**, entrez le nombre de jours (entre 1 et 30) pendant lesquels vous souhaitez que cette expérience suive les conversions. La fenêtre temporelle que vous spécifiez ici déterminera la durée pendant laquelle les événements de conversion (choisis dans la configuration de Canvas) seront suivis pour l'expérience. Les fenêtres de conversion par événement spécifiées dans la configuration du canvas ne s'appliqueront pas au suivi de cette étape et seront remplacées par cette fenêtre de conversion.

