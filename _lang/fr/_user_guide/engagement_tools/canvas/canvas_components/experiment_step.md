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

> Les chemins d’expérience vous permettent de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur. 

Ces composants vous permettront de suivre la performance du chemin pour prendre des décisions éclairées concernant votre parcours Canvas.

Lorsque vous ajoutez un composant de chemin, il affectera au hasard des utilisateurs à différents chemins (ou un groupe de contrôle facultatif) que vous créez. Des parties de cette audience seront affectées à différents chemins selon les pourcentages que vous sélectionnez, vous permettant de tester différents messages ou chemins les uns par rapport aux autres et de déterminer le plus efficace.

![][0]{: style="float:right;max-width:50%;margin-left:15px;"}

Tirez parti des chemins gagnants pour suivre la performance au cours du temps puis envoyez automatiquement les utilisateurs suivants sur le chemin ayant la meilleure performance.

## Cas d’utilisation

Les chemins d’expérience sont les mieux adaptés pour tester la livraison, la cadence, la copie de message et les combinaisons de canaux.

- **Livraison :** Comparer les résultats entre les messages envoyés avec un temps de [retards]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) différent, en fonction des actions de l’utilisateur ([Chemins d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)) et en utilisant le [Timing Intelligent]({{site.baseurl}}/docs/user_guide/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadence :** Tester plusieurs flux d’envoi de messages sur une période donnée. Par exemple, vous pourriez tester deux cadences d’onboarding différentes :
    - Cadence 1 : Envoyer 2 messages dans les 2 premières semaines de l’utilisateur
    - Cadence 2 : Envoyer 3 messages dans les 2 premières semaines de l’utilisateur
    
    Vous pouvez également tester l’efficacité d’envoyer deux messages de reconquête dans une semaine, ou en envoyer juste un lorsque vous ciblez les utilisateurs inactifs.
- **Copie du message :** Similaire à une norme [Test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/), vous pouvez tester différentes copies de message pour voir quels sont les résultats de conversion dans un taux de conversion plus élevé.<br><br>
- **Combinaisons de canaux :** Tester l’efficacité de différentes combinaisons de canaux de messages. Par exemple, vous pouvez comparer l’impact entre un seul e-mail et un e-mail combiné à une notification push.

## Créer des chemins d’expériences

Pour créer des chemins d’expérience, ajoutez d’abord une étape à votre Canvas. 

Glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **Experiment Paths (Chemins d’expérience)**. 

Dans la configuration par défaut de ce composant, il existe deux chemins par défaut, **Chemin 1** et **Chemin 2**, avec 50 % de l’audience envoyée vers chaque chemin. Cliquez sur le composant pour développer le panneau **Experiment Settings (Paramètres d’expérience)** et vous verrez alors les options de configuration pour le composant.

### Étape 1 : Choisissez le nombre de chemins et la répartition de l’audience

Vous pouvez ajouter jusqu’à quatre chemins en cliquant sur **Add Path (Ajouter chemin)** et un groupe de contrôle facultatif en sélectionnant **Add a Control Group (Ajouter un groupe de contrôle)**. À l’aide des cases de pourcentage de chaque chemin, vous pouvez indiquer le pourcentage de l’audience qui doit être associé à chaque chemin et le groupe de contrôle. Le total des pourcentages indiqués, additionnés doit être de 100 % pour continuer. Si vous souhaitez définir (et contrôler) rapidement tous les chemins disponibles sur le même pourcentage, cliquez sur **Distribute Paths Evenly (Répartir les chemins uniformément)**.

Vous pouvez également décider si des utilisateurs du groupe de contrôle doivent continuer d’avancer dans le Canvas ou le quitter après la conversion de la fenêtre de suivi pour le **Comportement de groupe de contrôle**. De manière facultative, vous pouvez ajouter une description pour expliquer aux autres les éléments que ces chemins d’expérience doivent tester ou inclure des informations supplémentaires pouvant être utiles à retenir.

![Paramètres d’expérience dans lesquels vous pouvez ajouter des chemins et distribuer le pourcentage d’utilisateurs dans chaque chemin.][1]

{% alert note %}
Si la rééligibilité Canvas est activée, les utilisateurs qui accèdent à Canvas et à un chemin choisi de manière aléatoire, accèderont à nouveau au même chemin s’ils deviennent rééligibles et accèdent à nouveau au Canvas. Ce processus permet de conserver la validité de l’expérience et l’analytique associée.
{% endalert %}

### Étape 2 : Activer le chemin gagnant (optionnel)

Le Chemin gagnant est équivalant à la [Variante gagnante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) dans les campagnes et vous permet d’automatiser vos tests A/B. Lorsque Winning Path est activé, après une période spécifiée, tous les utilisateurs suivants seront envoyés sur le chemin avec le taux de conversion le plus élevé.

Pour en savoir plus, consultez [Chemin gagnant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path).


### Étape 3 : Créer des chemins

Enfin, vous devez créer vos chemins en aval. Sélectionnez **Done (Effectué)** et revenez à l’éditeur de Canvas. Cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> sous chaque chemin pour commencer la création des parcours à l’aide des outils habituels Canvas comme bon vous semble et lancez le Canvas quand vous êtes prêt.

![Ajouter des étapes à chaque chemin qui se sépare d’un composant de chemin d’expérience.][3]{: style="max-width:75%"}

Souvenez-vous que les chemins et leurs étapes en aval ne peuvent pas être supprimés d’un Canvas une fois qu’ils ont été créés. Cependant, après le lancement, vous pouvez modifier la répartition de l’audience dans les chemins comme bon vous semble. Par exemple, si un jour après le lancement d’un Canvas vous concluez qu’un chemin est supérieur au reste en fonction de l’analytique, vous pouvez définir ce chemin sur 100 % et les autres sur 0 %. Ou, selon vos besoins, vous pouvez continuer l’envoi des utilisateurs vers plusieurs chemins.

## Suivi de la performance

Depuis la page Analytiques Canvas, cliquez sur Experiment Path (Chemins d’expérience) pour ouvrir un [tableau détaillé]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identique à l’onglet **Analyze Variants (Analyser des variantes)** pour comparer la performance détaillée et les statistiques de conversion entre les chemins. Vous pouvez également exporter la table via CVS et comparer le pourcentage de modifications pour les indicateurs d’intérêt par rapport au chemin ou au contrôle que vous sélectionnez.

Chaque étape de chaque chemin affiche des statistiques dans la vue [Canvas Analytics (Analytique Canvas)]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/), comme tout Canvas Step. Cependant, gardez à l’esprit que les analyses des étapes individuelles ne prennent **pas** en compte la structure de l’expérience. Les analyses de l’étape d’expérience doivent être utilisées pour comparer les chemins.

### Performance du chemin gagnant

Si Chemin gagnant est activé, votre affichage d’analytiques est séparé en deux onglets : **Expérience d’origine** et **Chemin gagnant**.

- **Expérience d’origine (Initial Experiment) :** Affiche les indicateurs de chaque chemin pendant la fenêtre d’expérimentation. Vous pouvez voir un aperçu de tous les chemins suivis pour les événements de conversion de données et quel chemin a été déterminé comme gagnant.
- **Chemin gagnant (Winning Path) :** Affiche uniquement les indicateurs pour le chemin gagnant à partir du moment où l’expérience d’origine est terminée.

### Paramètres supplémentaires

Les chemins d’expérience enregistreront les utilisateurs qui accèdent à chaque étape et effectuent une conversion dans le chemin affecté. Ceci effectuera le suivi de tous les événements de conversion indiqués dans la configuration Canvas. Dans l’onglet Additional Settings (Paramètres supplémentaires), utilisez l’entrée pour saisir le nombre de jours (entre 1 et 30) que vous souhaitez que cette expérience suive les conversions. Notez que la fenêtre de temps que vous indiquez ici déterminera la durée du suivi des événements de conversion (indiquée dans la configuration Canvas) pour les chemins d’expérience. La fenêtre de conversion par événement indiquée dans la configuration Canvas ne s’appliquera pas au suivi de cette étape et sera remplacée par cette fenêtre de conversion.


[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %}
[1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}

