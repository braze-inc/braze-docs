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

## Pourquoi mon Canvas n'est-il pas envoyé comme prévu ?

Les Canvas sont robustes et complexes, et nous savons que vous passez du temps à les créer. Si vous constatez que votre Canvas n'est pas envoyé comme vous le souhaitez, nous vous recommandons de vérifier la planification, l'audience et les paramètres d'entrée de votre Canvas, et de revoir les étapes de la [création d'un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

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
- Avez-vous confirmé que le segment contient des utilisateurs ?
- Avez-vous ajouté des filtres supplémentaires qui limiteraient le nombre d’utilisateurs entrant dans le Canvas ?
- Les utilisateurs sont-ils qualifiés pour recevoir la première étape de vos variantes ? Par exemple, si la première étape de votre Canvas est une notification push et que l’audience d’entrée a désactivé les notifications push, aucun utilisateur ne recevra de messages.

## Pourquoi mon audience ne s'est-elle pas répartie équitablement entre le groupe de contrôle et le groupe variante ?

Lors de la création de votre Canvas, vous vous attendiez peut-être à ce que votre audience se répartisse de manière égale entre votre groupe de contrôle et votre groupe variante, comme dans le [cas d'utilisation](#use-case) suivant. Voyons pourquoi et comment y remédier !

Le groupe que rejoint un utilisateur dépend de ses paramètres. Il peut s’agir du groupe de contrôle ou du groupe de variantes. Un utilisateur entrera dans un canvas lorsqu'il répondra à tous les critères définis dans l'[étape d'entrée.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) Lors de la configuration de votre Canvas, vous définissez quel pourcentage d’utilisateurs entreront dans chaque variante et dans le groupe de contrôle.

Si la taille de votre groupe de contrôle est importante par rapport à votre groupe de variantes (et que ce n’était pas votre intention), nous vous recommandons ce qui suit :
1. Le filtre d'audience de votre entrée **est Foreground Push Enabled (poussée au premier plan activée**).
2. Définissez votre filtre d'audience d'entrée pour l'**état de l'abonnement en mode push**, l'**état de l'abonnement par e-mail**, ou les deux, sur **Abonné** ou **Inscrit**.

Lorsque vous créez un Canvas avec un groupe de contrôle, confirmez que tous les utilisateurs de l'audience d'entrée sont en mesure de recevoir des messages dans le Canvas (par exemple, le Canvas contient des messages push et des e-mails).

### Cas d’utilisation

Imaginons le scénario suivant :
- Un Canvas a une seule variante et un groupe de contrôle.
- La première étape de la variante est une notification push.
- 90 % des utilisateurs ont été sélectionnés pour entrer dans la variante et 10 % pour entrer dans le groupe de contrôle.

![Exemple de canvas avec 90% de variante et 10% de groupe de contrôle.]({% image_buster /assets/img_archive/trouble15.png %})

Dans ce scénario, 90 % des utilisateurs qui entrent dans Canvas entreront dans la variante. 

Si nous regardons les utilisateurs actifs, nous pouvons voir que même s'il y a 29,8 millions d'utilisateurs, seulement 64% d'entre eux ont activé la fonction "push" :

![Segment avec le filtre "Push Enabled" réglé sur "true", et des utilisateurs estimés à 29,8k.]({% image_buster /assets/img_archive/trouble16.png %})

Cela signifie que même si nous avons indiqué que 90 % des utilisateurs doivent entrer dans la variante, tous ces utilisateurs ne peuvent pas recevoir une notification push. Ces utilisateurs qui ne sont pas en mesure de recevoir une notification push entreront quand même dans la variante.