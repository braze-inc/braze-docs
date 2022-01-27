---
nav_title: Étape des chemins d'expérimentation
article_title: Étape des chemins d'expérimentation
alias: /fr/experiment_step/
page_order: 4
page_type: Référence
description: "Les chemins d’expérience vous permettent de tester plusieurs chemins de Canvas les uns contre les autres et un groupe de contrôle à n’importe quel moment du voyage de l’utilisateur."
tool: Toile
---

# Étape des chemins d'expérimentation

> L'Étape des chemins d'expérience vous permet de tester plusieurs chemins de Canvas les uns contre les autres et un groupe de contrôle à n'importe quel moment du voyage de l'utilisateur. Ces étapes vous permettront de suivre la performance du parcours pour prendre des décisions éclairées au sujet de votre voyage sur Canvas .

Une étape des chemins d'expérience de Canvas attribuera aléatoirement des utilisateurs à différents chemins (ou un groupe de contrôle optionnel) que vous créez. Des portions du public seront assignées à différents chemins selon les pourcentages que vous sélectionnez, vous permettant de tester différents messages ou chemins les uns contre les autres et de déterminer lesquels est le plus efficace. Après le lancement, analytics vous permettra de suivre les performances et de voir si les résultats diffèrent entre les différents chemins pour vous aider à déterminer quel chemin devrait obtenir la proportion d'utilisateurs (ou tous !).

!\[Étape de l'expérience Paths\]\[0\]{: style="max-width:80%"}


## Créer un chemin d'expérience

Pour créer une étape de parcours expérimental, ajoutez une étape à votre Canevas. Ensuite, en utilisant le menu déroulant en haut de la nouvelle étape, sélectionnez **Chemins d'expérience**.

Dans la configuration par défaut de cette étape, il y a deux chemins par défaut, **Chemin 1** et **Chemin 2**, 50% du public étant envoyé dans chaque chemin. Cliquez sur l'étape Chemins d'expérience pour développer le panneau **Paramètres d'expérience** et vous verrez les options de configuration de l'étape.

### Étape 1 : Choisissez le nombre de chemins et la distribution du public

!\[Paramètres d'expérience\]\[1\]

Vous pouvez ajouter jusqu'à 4 chemins en cliquant sur **Ajouter un chemin** et un groupe de contrôle facultatif en cochant **Ajouter un groupe de contrôle**. En utilisant les cases de pourcentage au-dessus de chaque chemin, vous pouvez spécifier le pourcentage du public qui doit aller vers chaque chemin et le groupe de contrôle. Les pourcentages fournis doivent correspondre à 100 % pour continuer. Si vous voulez rapidement définir tous les chemins (et contrôle) disponibles sur le même pourcentage, cliquez sur **Distribute Paths Evenly**.

Indiquez si les utilisateurs du groupe de contrôle doivent continuer vers le bas ou quitter Canvas après la fenêtre de suivi de conversion en utilisant la case à cocher fournie.

{% alert note %}
Si la rééligibilité de Canvas est activée, les utilisateurs qui entrent dans le Canvas et descendent un chemin choisi aléatoirement reprendront le même chemin s'ils redeviennent éligibles et entreront à nouveau dans le Canvas. Ceci maintient la validité de l'expérience et des analyses associées.
{% endalert %}

Optionnellement, vous pouvez ajouter une description pour expliquer aux autres ce que cette étape des chemins d'expérience a l'intention de tester ou d'inclure d'autres informations qui pourraient être utiles à noter.

### Étape 2 : Sélectionnez le temps de suivi des conversions

L'étape des chemins d'expérience enregistre les utilisateurs qui entrent dans chaque étape et les convertiront dans le chemin assigné. Cette étape permet de suivre tous les événements de conversion spécifiés dans la configuration de Canvas . Utilisez la zone d'entrée en bas du panneau pour saisir combien de jours (entre 1 et 30) vous souhaitez que cette expérience puisse suivre les conversions.

### Étape 3 : Créer des chemins

Enfin, vous devez construire vos chemins en aval. Sélectionnez **Terminé** et retournez au constructeur Canvas . Cliquez sur <i class="fas fa-plus-circle"></i> sous chaque chemin pour commencer à créer des trajets en utilisant les outils de Canvas habituels comme bon vous semble, et lancez la Toile lorsque vous êtes prêt.

Gardez à l'esprit que **chemins et leurs étapes en aval ne peuvent pas être supprimés d'une toile** une fois créée. Cependant, une fois lancé, vous pouvez modifier la distribution du public à travers les chemins comme bon vous semble. Par exemple, si un jour après le lancement d'un Canvas, vous concluez qu'un chemin est supérieur au reste basé sur les analytiques, vous pouvez définir ce chemin à 100% et les autres à 0%. Ou, selon vos besoins, vous pouvez continuer à envoyer des utilisateurs sur plusieurs chemins.

## Performances de suivi

Chaque chemin affichera des statistiques dans la vue [Analyses de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/) , comme n'importe quelle étape de Canvas . De plus, en cliquant sur le chemin de l'expérience, pas de l'analyse de canvas ouvrira un tableau détaillé [identique à Analyser les variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) pour comparer les statistiques détaillées de performance et de conversion entre les chemins. Vous pouvez également exporter la table via CSV et comparer les changements de pourcentage pour les métriques d'intérêt par rapport au chemin ou le contrôle que vous sélectionnez.
[0]: {% image_buster /assets/img/experiment_step/experiment_step.png %} [1]: {% image_buster /assets/img/experiment_step/exp_settings.png %}