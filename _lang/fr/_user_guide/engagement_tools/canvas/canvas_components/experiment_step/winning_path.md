---
nav_title: Chemin gagnant 
article_title: Chemin gagnant dans les chemins d’expérience 
page_order: 1
page_type: reference
description: "Cet article de référence couvre le chemin gagnant, une fonctionnalité qui vous permet d’automatiser vos tests A/B lorsqu’ils sont activés pour une étape des chemins d'expérience."
tool: Canvas
---

# Chemin gagnant dans les chemins d’expérience

Le Chemin gagnant est équivalant à la [Variante gagnante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) dans les campagnes et vous permet d’automatiser vos tests A/B. Lorsque le chemin gagnant est activé dans une étape des chemins d'expérience, après une période spécifiée, tous les utilisateurs suivants seront envoyés sur le chemin avec le taux de conversion le plus élevé.

Cette fonctionnalité est le mieux pour les Canvas avec des entrées récurrentes ou déclenchées, mais qui peuvent être utilisées pour les Canvas avec une entrée unique avec [quelques étapes supplémentaires](#one-time-entry).

{% alert important %}
Winning Path est actuellement en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Utilisation du chemin gagnant

Ajouter un [Chemin d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) sur votre Canvas, puis activez **Chemin gagnant**. 

![Paramètres des chemins d’expérience intitulés "Distribute Subsequent Users to Winning Path" (Envoyez les utilisateurs suivants dans le chemin gagnant). La section comprend une bascule pour le chemin gagnant et des options pour configurer l’événement de conversion et la fenêtre d’expérience.][1]

Pour définir un chemin gagnant, spécifiez l’événement de conversion devant déterminer le gagnant. Si aucun événement de conversion n’est disponible, retournez à la première étape de la configuration Canvas et [attribuez des événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events).

Définissez ensuite la **Fenêtre d’expérience**. La **Fenêtre d’expérience** définit pendant combien de temps doit s’exécuter l’expérience avant que le chemin gagnant ne soit défini et que tous les utilisateurs suivants soient envoyés dessus. Cette fenêtre débute au moment où le premier utilisateur accède à l’étape.

## Utiliser des chemins gagnants avec une entrée unique {#one-time-entry}

Étant donné que le gagnant est choisi après une période de temps choisie, le chemin gagnant est le meilleur pour les Canvas où les utilisateurs entrent de manière récurrente ou déclenchée. Un Canvas avec entrée unique ne peut pas envoyer les utilisateurs à un chemin gagnant plus tard, car tous les utilisateurs passent par des chemins simultanément. 

Cependant, vous pouvez accomplir ce cas d’utilisation en ajoutant une étape des chemins d'expérience préliminaire supplémentaire, qui retarde la partie souhaitée des utilisateurs jusqu’à ce que l’expérience soit terminée.

![Une version préliminaire du Canvas montrant comment utiliser la fonctionnalité Chemin gagnant dans une Canvas avec une entrée unique.][2]{: style="max-width:80%"}

### Étapes

1. Ajoutez une étape des chemins d'expérience initiale (avec le chemin gagnant désactivé) pour diviser les utilisateurs entre le groupe d’envoi final et le groupe de tests qui passera par l’étape avec les chemins gagnants activés. 
2. Ajoutez une étape de retard au chemin de groupe d’envoi final. 
3. Ajoutez une deuxième étape des chemins d'expérience au groupe de tests (avec le chemin gagnant activé). Cette étape fonctionne normalement, avec des utilisateurs répartis de manière égale entre plusieurs chemins que vous souhaitez tester.

La durée de l’étape de retard doit être légèrement plus longue que la fenêtre d’expérience pour s’assurer que l’expérience a été terminée une fois que les utilisateurs ont avancé après le délai. Une fois que l’étape avec les chemins gagnants activée sélectionne un gagnant, elle définira 100 % des futurs utilisateurs vers le chemin gagnant. Les utilisateurs qui attendent l’étape de retard seront libérés et passeront au chemin gagnant.

{% alert note %}
Si vous souhaitez que cette fonctionnalité soit intégrée à Winning Path, veuillez en informer l’équipe produit Braze en [votant pour elle sur le portail du produit Braze](https://portal.productboard.com/ko5rgqefrdssb5wesynqswxp/c/206-winning-path-for-one-time-sends?utm_medium=social&utm_source=portal_share).
{% endalert %}

[1]: {% image_buster /assets/img/experiment_step/experiment_winning_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_onetime_workaround.png %}
