---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des toiles
page_order: 11
page_type: reference
description: "Cette page présente les étapes de résolution des problèmes pour les toiles."
tool: Canvas
---

# Résolution des problèmes des toiles

> Cette page vous aide à résoudre les problèmes liés à vos toiles.

## Pourquoi un utilisateur n'a-t-il pas reçu une étape du canvas déclenchée ?

Tout d'abord, confirmez que l'événement personnalisé est transmis à Braze. Accédez à **Analyse/analytique** > **Rapport sur les événements personnalisés**, puis sélectionnez l'événement personnalisé et la plage de dates correspondants. Si l'événement ne s'affiche pas, vérifiez qu'il est correctement configuré et que l'utilisateur a effectué la bonne action.

Si l'événement personnalisé s'affiche, poursuivez la résolution des problèmes en procédant comme suit :

- Vérifiez le téléchargement du profil utilisateur pour confirmer qu'il a déclenché l'événement et quand il l'a fait. Si l'événement a été déclenché, comparez l'horodatage du déclenchement de l'événement à la durée en ligne/en production/instantanée du Canvas. L'événement peut avoir été déclenché avant que la toile ne soit mise en ligne/en production/instantanée.
- Examinez les journaux des modifications pour le Canvas et tous les segments utilisés dans le ciblage afin de déterminer si l'utilisateur se trouvait dans le segment lorsque son événement personnalisé a été déclenché. S'ils n'étaient pas dans le segment, ils n'auraient pas reçu l'étape du canvas.
- Vérifiez si l'utilisateur a été intégré dans un groupe de contrôle par le biais de la segmentation et, par conséquent, s'il n'a pas pu bénéficier de l'étape du canvas.
- En cas de retard planifié, vérifiez si l'événement personnalisé de l'utilisateur a été déclenché avant le retard. Si l'événement avait été déclenché avant le délai, ils n'auraient pas reçu l'étape du canvas.

{% alert note %}
Les messages in-app ne peuvent être déclenchés que par des événements envoyés via le SDK, et non via l'API REST.
{% endalert %}

## Pourquoi mon canvas ne s'envoie-t-il pas comme prévu ?

Les Canvas sont robustes et complexes, et nous savons que vous passez du temps à les créer. Par conséquent, si vous constatez que votre Canvas ne fonctionne pas comme vous le souhaitez, nous vous recommandons de vérifier votre planification Canvas, votre audience et vos paramètres d'entrée, et de revoir les étapes de [création d'un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

### Calendrier

- Le canvas est-il [correctement planifié]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types) ?
- Avez-vous sélectionné les bonnes dates et heure ?
- Pour la [livraison/distribution par événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types), les utilisateurs ont-ils effectué les actions spécifiées depuis que vous avez lancé le Canvas ?

### Paramètres d'entrée

Les [paramètres d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=basics#selecting-entry-controls) sont importants pour comprendre comment vos toiles sont envoyées. Vérifiez si vous avez limité le nombre de personnes qui entreront potentiellement dans le Canvas.

Les utilisateurs peuvent également quitter un canvas s'ils ne sont plus autorisés à recevoir des messages. Par exemple, si le Canvas ne contient que des notifications push et qu’un utilisateur refuse les notifications push après avoir reçu la première étape, alors l’utilisateur sortira du Canvas. Envisagez d'utiliser [différentes étapes du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) pour ajouter des parcours utilisateurs alternatifs.

### Segmentation de votre audience

Réfléchissez aux questions suivantes pour votre audience cible :

- Avez-vous sélectionné le bon segment ?
- Comment le segment est-il configuré ?
- Avez-vous vérifié que le segment contient des utilisateurs ?
- Avez-vous ajouté des filtres supplémentaires qui limiteraient le nombre d’utilisateurs entrant dans le Canvas ?
- Les utilisateurs sont-ils qualifiés pour recevoir la première étape de vos variantes ? Par exemple, si la première étape de votre Canvas est une notification push et que l’audience d’entrée a désactivé les notifications push, aucun utilisateur ne recevra de messages.

## Pourquoi aucun utilisateur n'a-t-il accédé au programme de planification quotidien Canvas le jour du passage à l'heure d'été ?

Lors des jours de transition à l'heure d'été, les Canvases planifiés quotidiennement peuvent s'exécuter jusqu'à une heure plus tôt ou plus tard que d'habitude. Si vos critères d'admissibilité reposent sur des attributs personnalisés ou des événements avec des horodatages situés dans l'heure précédant l'heure d'entrée prévue, il est possible que les utilisateurs ne soient pas encore admissibles le jour du passage à l'heure d'été, car l'attribut ou l'événement n'a pas encore été enregistré.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour des attributs personnalisés à 15 h p.mdans le fuseau horaire de votre canvas et que votre canvas s'exécute quotidiennement à 15 h 30 p.mdans ce même fuseau horaire. Lors d'un jour de passage à l'heure d'été, canvas peut évaluer les utilisateurs jusqu'à une heure plus tôt que d'habitude par rapport à cette mise à jour d'attribut, avant que l'attribut n'ait été enregistré. Si la rééligibilité est désactivée, les utilisateurs qui ont participé les jours précédents ne peuvent pas participer à nouveau, ce qui entraîne un nombre de participations nul pour ce jour-là.

Pour éviter cela, veuillez vous assurer que vos mises à jour d'attributs personnalisés ou d'événements personnalisés ont lieu plus d'une heure avant l'heure d'entrée prévue dans Canvas.

## Pourquoi mon audience n'a-t-elle pas été répartie de manière égale entre le groupe de contrôle et le groupe variant ?

Lors de la création de votre Canvas, vous vous attendiez peut-être à ce que votre audience se répartisse de manière égale entre votre groupe de contrôle et votre groupe de variante, comme dans le [cas d'utilisation](#use-case) suivant. Examinons pourquoi il en est ainsi et comment y remédier.

Le groupe que rejoint un utilisateur dépend de ses paramètres. Il peut s’agir du groupe de contrôle ou du groupe de variantes. Un utilisateur accède à un canvas lorsqu'il répond à tous les critères que vous avez définis dans l'[étape]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) [d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule). Lors de la configuration de votre Canvas, vous définissez quel pourcentage d’utilisateurs entreront dans chaque variante et dans le groupe de contrôle.

Si la taille de votre groupe de contrôle est importante par rapport à votre groupe de variantes (et que ce n’était pas votre intention), nous vous recommandons ce qui suit :
1. Veuillez configurer votre filtre d'audience d'entrée sur **« Activation de la notification push en avant-plan** ».
2. Veuillez définir votre filtre d'audience d'entrée pour **le statut d'abonnement aux notifications push**, **le statut d'abonnement aux e-mails**, ou les deux, sur **« Opted In** » (Abonnement) ou **« Subscribed** » (Abonné).

Lors de la création d'un canvas avec un groupe de contrôle, veuillez vous assurer que tous les utilisateurs de l'audience cible sont en mesure de recevoir des messages dans le canvas (par exemple, si le canvas contient des messages push et des e-mails).

### Cas d’utilisation

Imaginons le scénario suivant :
- Un Canvas a une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante et 10 % pour entrer dans le groupe de contrôle.

![Exemple de canvas avec 90 % de variante et 10 % de groupe de contrôle.]({% image_buster /assets/img_archive/trouble15.png %})

Dans ce scénario, 90 % des utilisateurs qui entrent dans Canvas entreront dans la variante. 

Si nous examinons les utilisateurs actifs, nous constatons que, bien qu'il y ait 29 800 utilisateurs, seuls 64 % d'entre eux ont activé la fonction push :

![Segment avec le filtre « Push Enabled » (Push activé) défini sur « true » (vrai) et estimation de 29 800 utilisateurs.]({% image_buster /assets/img_archive/trouble16.png %})

Cela signifie que même si nous avons indiqué que 90 % des utilisateurs doivent entrer dans la variante, tous ces utilisateurs ne peuvent pas recevoir une notification push. Ces utilisateurs qui ne sont pas en mesure de recevoir une notification push entreront quand même dans la variante.