---
nav_title: Chemin gagnant 
article_title: Chemin gagnant dans les chemins d’expérience 
page_type: reference
description: "Cet article de référence couvre le chemin gagnant, une fonctionnalité qui vous permet d’automatiser vos tests A/B lorsqu’ils sont activés pour une étape des chemins d'expérience."
tool: Canvas
---

# Chemin gagnant dans les chemins d’expérience

> Le chemin gagnant (Winning Path) est similaire à la [variante gagnante (Winning Variant)]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) dans les campagnes, et vous permet d'automatiser vos tests A/B.

Lorsque le chemin gagnant est activé dans une étape des chemins d'expérience, après une période spécifiée, tous les utilisateurs suivants seront envoyés sur le chemin avec le taux de conversion le plus élevé.

## Utilisation du chemin gagnant

### Étape 1 : Ajouter une étape des chemins chemins d'expérience

Ajoutez un [chemin d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) à votre canvas, puis activez l'option **Chemin gagnant**.

![Paramètres des chemins d’expérience intitulés "Distribute Subsequent Users to Winning Path" (Envoyez les utilisateurs suivants dans le chemin gagnant). La section comprend un basculeur pour le chemin gagnant et des options pour configurer l'événement de conversion et la fenêtre d'expérience.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Étape 2 : Configurer les paramètres du chemin gagnant

Pour définir un chemin gagnant, spécifiez l’événement de conversion devant déterminer le gagnant. Si aucun événement de conversion n'est disponible, revenez à la première étape de la configuration de Canvas et [attribuez des événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Notez que si vous déterminez le gagnant à l’aide des ouvertures et des clics, seul le premier message du chemin qui génère des ouvertures ou des clics contribuera à déterminer le gagnant.

Ensuite, définissez la **fenêtre d'expérience**. La **fenêtre d'expérience** spécifie la durée de l'expérience avant que le chemin gagnant ne soit déterminé et que tous les utilisateurs qui suivent ne soient envoyés sur ce chemin. Cette fenêtre débute au moment où le premier utilisateur accède à l’étape.

![Paramètres du chemin d'expérience gagnante avec l'événement de conversion "Clics" sélectionné pour une fenêtre d'expérience de 12 heures.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Étape 3 : Déterminer la solution de secours {#statistical-significance}

Par défaut, si les résultats du test ne sont pas suffisants pour déterminer un vainqueur statistiquement significatif, tous les utilisateurs futurs seront envoyés sur le chemin le plus performant.

Vous pouvez également sélectionner **Continuer à envoyer le mélange de chemins à tous les futurs utilisateurs**. Cette option enverra les futurs utilisateurs dans la combinaison de chemins selon les pourcentages spécifiés dans la distribution des chemins d'expérience.

!["Continuer à envoyer à tous les futurs utilisateurs la combinaison de chemins" sélectionné comme ce qui arrivera aux utilisateurs si le résultat du test n'est pas statistiquement significatif.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Un groupe retardé apparaîtra dans votre distribution de chemins uniquement si votre canvas est configuré pour une entrée unique et que votre étape d'expérience comporte trois chemins ou moins. Les toiles récurrentes et déclenchées n'auront pas de groupe de retard lorsque le chemin gagnant est activé.
{% endalert %}

### Étape 4 : Ajoutez vos chemins et lancez le Canvas

Un seul composant Chemin d'expérience peut contenir jusqu'à quatre chemins. Toutefois, si votre Canvas est configuré pour une [entrée unique](#one-time-entry), un chemin doit être réservé au groupe de retard que Braze ajoute automatiquement lorsque le chemin gagnant est activé. Cela signifie que pour les toiles à entrée unique, vous pouvez ajouter jusqu'à trois chemins d'expérience.

Terminez la configuration de votre canvas si nécessaire, puis lancez-le. Lorsque le premier utilisateur est entré dans l'expérience, vous pouvez consulter le Canvas pour voir les analyses/analytiques au fur et à mesure qu'elles arrivent et [suivre les performances de votre expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Après la conclusion d'un chemin gagnant, tous les utilisateurs suivants qui entrent dans le Canvas suivront le chemin gagnant, y compris les utilisateurs qui sont entrés à nouveau et qui faisaient auparavant partie du groupe de contrôle de l'étape du chemin d'expérience.

## Analyses {#analytics}

Si l'option Chemin gagnant est activée, la vue analytique est séparée en deux onglets : **Expérience d’origine** et **Chemin gagnant**.

- **Première expérience :** Affiche les indicateurs de chaque chemin pendant la fenêtre d’expérimentation. Vous pouvez consulter un résumé des performances de tous les chemins d'accès pour les événements de conversion spécifiés et voir quel chemin d'accès a été sélectionné comme vainqueur.
- **Chemin gagnant (Winning Path) :** Affiche uniquement les indicateurs pour le chemin gagnant à partir du moment où l’expérience d’origine est terminée.

## Choses à savoir

### Entrée unique {#one-time-entry}

Lorsque vous utilisez des parcours gagnants dans un canvas où les utilisateurs ne sont autorisés à entrer qu'une seule fois, un groupe de retard est automatiquement inclus. Pendant la durée de l'expérience, un pourcentage d'utilisateurs sera maintenu dans le groupe de retard pendant que les autres utilisateurs entreront dans vos chemins d'expérience.

![Étape des chemins d'expérience avec un groupe interne pour le chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Lorsque le test est terminé et qu'un chemin gagnant est déterminé, les utilisateurs affectés au groupe de retardement seront dirigés vers le chemin choisi et continueront à travers le Canvas.

![Étape des chemins d'expérience d'un groupe interne envoyé sur le chemin gagnant]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Diffusion selon l'heure locale

Nous vous déconseillons d’utiliser la livraison à l'heure locale dans les Canvas utilisant des chemins gagnants. En effet, les fenêtres d’expérience débutent lorsque le premier utilisateur les franchit. Les utilisateurs qui se trouvent dans des fuseaux horaires très précoces peuvent entrer dans l'étape et déclencher le début de la fenêtre d'expérience beaucoup plus tôt que prévu, ce qui peut avoir pour conséquence que l'expérience se termine avant que la majorité de vos utilisateurs se trouvant dans des fuseaux horaires plus classiques n'aient eu le temps d'entrer dans le Canvas ou de se convertir, ou les deux à la fois. 

Sinon, si vous souhaitez utiliser la diffusion selon l’heure locale, utilisez une fenêtre d’expérience de 24 à 48 heures ou plus. De cette manière, les utilisateurs des premiers fuseaux horaires entrent dans le Canvas et déclenchent le démarrage de l'expérience, mais il reste encore beaucoup de temps dans la fenêtre d'expérience. Les utilisateurs situés dans des fuseaux horaires plus tardifs auront encore suffisamment de temps pour entrer dans le Canvas et l'étape des chemins d'expérience avec des voies gagnantes et éventuellement se convertir avant l'expiration de la fenêtre d'expérience.

