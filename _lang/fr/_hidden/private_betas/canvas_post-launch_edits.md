---
nav_title: Modifications post-lancement
permalink: "/post-launch_edits/"
hidden: true
---

# Modifications post-lancement

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Dans le workflow Canvas V2, vous pouvez maintenant modifier vos Canvas après leur lancement. Ceci inclut la suppression des éléments suivants :

- [Composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components)
- Variantes de Canvas 
- Connexions entre les étapes de Canvas  

Vous pouvez modifier les connexions entre les composants Canvas en cliquant sur la connexion entre les composants Canvas et en les déplaçant ailleurs. Vous voulez supprimer une étape ? Cliquez sur l’icône en forme d’engrenage correspondant à l’étape appropriée, et sélectionnez **Delete** (Supprimer).

Si vous supprimez une [étape de délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou une [étape de parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), vous pouvez éventuellement rediriger les utilisateurs actuellement en attente sur une autre étape Canvas V2. Pour les étapes de délai, les utilisateurs resteront dans l’étape jusqu’à la fin de la période en question. Pour les étapes des parcours d’action, les utilisateurs resteront dans l’étape jusqu’à la fin de la fenêtre d’évaluation.

{% alert important %}
Vous ne pouvez effectuer des modifications post-lancement que sur le worklow Canvas V2. Si votre Canvas utilise le workflow Canvas V1, vous devez d’abord migrer le Canvas vers Canvas V2 :
{% endalert %}

## Modifier votre Canvas

Il y a plusieurs choses à garder à l’esprit lors de la modification ou de l’ajout à votre Canvas après son lancement. Si vous souhaitez modifier ou ajouter des étapes à votre Canvas, les détails suivants s’appliqueront :
- Après avoir créé une nouvelle étape, les utilisateurs qui n’ont pas encore saisi le Canvas seront éligibles pour saisir cette nouvelle étape. 
- Les utilisateurs ayant déjà réussi les étapes créées seront éligibles lors du prochain accès, si vous les autorisez à accéder à nouveau au Canvas dans les options Entrée de Canvas.
- Les utilisateurs actuellement sur un Canvas peuvent recevoir des étapes Canvas ajoutées depuis peu.

Notez les informations suivantes pour modifier les étapes de Canvas avec un délai :
- Si vous mettez à jour le délai dans Étape de délai ou la fenêtre d’évaluation dans l’étape de parcours d’action, seuls les nouveaux utilisateurs accédant au Canvas et les utilisateurs n’ayant pas été mis en file d’attente pour cette étape recevront les messages une fois le délai temporel mis à jour.
- Si vous supprimez une étape avec un délai (étape de délai ou étape de parcours d’action) et décidez de rediriger ces utilisateurs sur une autre étape Canvas, les utilisateurs ne seront redirigés que lorsque le délai de l’étape sera écoulé. Supposons que vous supprimez une étape de délai (un jour) et redirigez ces utilisateurs sur une étape Message. Dans ce cas, les utilisateurs ne seront redirigés que lorsque le délai d’un jour est écoulé.

Si votre Canvas contient une ou plusieurs [étapes de parcours d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/), supprimer des étapes peut invalider les résultats de cette étape.

Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent dans une étape. Si vous réactivez le Canvas et que les utilisateurs attendent toujours, ils finiront l’étape et passeront à la suivante. Cependant, si le délai durant lequel l’utilisateur aurait dû passer à l’étape suivante est dépassé, il quittera le Canvas. 

Supposons que vous avez créé un Canvas créé à l’aide du workflow Canvas V2, paramétré pour être exécuté à 14h00 avec une variante et deux étapes : une étape de délai (une heure), puis une étape Message. Un utilisateur saisit le dessin (Canvas) à 14h01 et saisit l’étape de délai en même temps. Cela signifie que l’utilisateur sera programmé pour passer à l’étape suivante (l’étape Message) à 15h01. Si vous arrêtez le Canvas à 14h30 et que vous le réactivez à 15h30, l’utilisateur quittera Canvas puisque 15h01 est passée. Cependant, si vous réactivez le Canvas à 14h40, l’utilisateur passera à l’étape Message comme prévu à 15h01.

[1]: {% image_buster /assets/img_archive/canvasv2_delete_step_post-launch.png %} 