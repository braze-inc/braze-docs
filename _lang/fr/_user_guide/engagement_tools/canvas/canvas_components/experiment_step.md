---
nav_title: Étape des chemins d’expérience
article_title: Étape des chemins d’expérience
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Les chemins d’expérience vous permettent de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur."
tool: Canvas
---

# Étape des chemins d’expérience

> L’étape des chemins d’expérience vous permet de tester plusieurs chemins Canvas les uns par rapport aux autres et un groupe de contrôle, à tout moment dans le parcours de l’utilisateur. Ces étapes vous permettront de suivre la performance du chemin pour prendre des décisions éclairées concernant votre parcours Canvas.

Une étape des chemins d’expérience Canvas affectera au hasard des utilisateurs à différents chemins (ou un groupe de contrôle facultatif) que vous créez. Des parties de ce public seront affectées à différents chemins selon les pourcentages que vous sélectionnez, vous permettant de tester différents messages ou chemins les uns par rapport aux autres et de déterminer le plus efficace.

![][0]{: style="max-width:80%"}

Après le lancement, l’analytique vous permettra de suivre la performance et de voir si les résultats diffèrent dans les différents chemins, pour vous aider à déterminer quel chemin doit être associé à quelle proportion d’utilisateurs (ou à tous !).


## Créer une étape des chemins d’expérience

Pour créer une étape des chemins d’expérience, ajoutez l’étape à votre Canvas. Puis, à l’aide du menu déroulant en haut de la nouvelle étape, sélectionnez **Chemins d’expérience**.

Dans la configuration par défaut de cette étape, il existe deux chemins par défaut, **Chemin 1** et **Chemin 2**, avec 50 % du public envoyé vers chaque chemin. Cliquez sur l’étape des chemins d’expérience pour développer le panneau **Paramètres d’expérience**, vous verrez alors les options de configuration pour l’étape. 

### Étape 1 : Choisissez le nombre de chemins et la répartition du public

Vous pouvez ajouter jusqu’à quatre chemins en cliquant sur **Ajouter chemin** et un groupe de contrôle facultatif en sélectionnant **Ajouter un groupe de contrôle**. À l’aide des cases de pourcentage de chaque chemin, vous pouvez indiquer le pourcentage du public qui doit être associé à chaque chemin et le groupe de contrôle. Le total des pourcentages indiqués, additionnés doit être de 100 % pour continuer. Si vous souhaitez définir (et contrôler) rapidement tous les chemins disponibles sur le même pourcentage, cliquez sur **Répartir les chemins uniformément**.

Vous pouvez également décider si des utilisateurs du groupe de contrôle doivent continuer d’avancer dans le Canvas ou le quitter après la conversion de la fenêtre de suivi pour le **Comportement de groupe de contrôle**. De manière facultative, vous pouvez ajouter une description pour expliquer aux autres les éléments que cette étape des chemins d’expérience doit tester ou inclure des informations supplémentaires pouvant être utiles, à retenir.

![Paramètres d’expérience][1]

{% alert note %}
Si la rééligibilité Canvas est activée, les utilisateurs qui accèdent à Canvas et à un chemin choisi de manière aléatoire, accèderont à nouveau au même chemin s’ils deviennent rééligibles et accèdent à nouveau au Canvas. Ce processus permet de conserver la validité de l’expérience et l’analytique associée.
{% endalert %}

### Étape 2 : Sélectionnez la durée des conversions de suivi

L’étape des chemins d’expérience enregistrera les utilisateurs qui accèdent à chaque étape et effectuera une conversion dans le chemin affecté. Cette étape effectuera le suivi de tous les événements de conversion indiqués dans la configuration Canvas. Utilisez la zone de saisie en bas du panneau pour saisir le nombre de jours (compris entre 1 et 30) pendant lequel vous souhaitez que cette expérience effectue le suivi des conversions. Notez que la fenêtre de temps que vous indiquez ici déterminera la durée du suivi des conversions (indiquée dans la configuration Canvas) pour l’étape des chemins d’expérience. La fenêtre de conversion par événement indiquée dans la configuration Canvas ne s’appliquera pas au suivi de l’étape des chemins d’expérience. 

### Étape 3 : Créer des chemins

Enfin, vous devez créer vos chemins en aval. Sélectionnez **Effectué** et revenez à l’éditeur de Canvas. Cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus sous chaque chemin pour commencer la création des parcours à l’aide des outils habituels Canvas comme bon vous semble et lancez le Canvas quand vous êtes prêt. 

Souvenez-vous que les **chemins et leurs étapes en aval ne peuvent pas être supprimés d’un Canvas** une fois qu’ils ont été créés. Cependant, après le lancement, vous pouvez modifier la répartition de public dans les chemins comme bon vous semble. Par exemple, si un jour après le lancement d’un Canvas vous concluez qu’un chemin est supérieur au reste en fonction de l’analytique, vous pouvez définir ce chemin sur 100 % et les autres sur 0 %. Ou, selon vos besoins, vous pouvez continuer l’envoi des utilisateurs vers plusieurs chemins.

## Suivi de la performance

Chaque chemin affiche des statistiques dans la vue [Analytique Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/), comme toute Canvas Step. De plus, en cliquant sur l’Étape des chemins d’expérience dans Canvas, l’analytique ouvrira une [table détaillée]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) identique à l’onglet **Analyser des variantes** pour comparer la performance détaillée et les statistiques de conversion dans les chemins. Vous pouvez également exporter la table via CVS et comparer le pourcentage de modifications pour les métriques d’intérêt par rapport au chemin ou au contrôle que vous sélectionnez.

[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %}
[1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}