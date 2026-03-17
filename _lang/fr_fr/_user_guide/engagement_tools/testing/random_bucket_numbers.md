---
nav_title: Numéros de compartiment aléatoire
article_title: Numéros de compartiment aléatoire
page_order: 2
page_type: reference
description: "Cet article couvre le concept de numéros de compartiment aléatoire et la manière de les utiliser pour créer des variantes et des groupes de contrôle."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Numéros de compartiment aléatoire

> Un numéro de compartiment aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. 

## Aperçu

Lorsqu’un profil d’utilisateur est créé dans Braze, l’utilisateur reçoit automatiquement un numéro de compartiment aléatoire compris entre 0 et 9999. Vous pouvez utiliser ces segments pour évaluer l'efficacité de plusieurs campagnes ou canevas sur des groupes d'utilisateurs au fil du temps.

### Utilisation du groupe de contrôle global

Des numéros de compartiment aléatoires sont utilisés dans votre groupe de contrôle global, un groupe d'utilisateurs qui ne reçoivent aucune campagne ni aucune canevas. Braze sélectionne de manière aléatoire plusieurs plages de numéros de compartiment aléatoires et inclut les utilisateurs faisant partie des compartiments sélectionnés. Les numéros de compartiments aléatoires sont attribués sans pondération ni prise en compte des numéros récemment attribués. 

{% alert note %}
Lorsqu'un utilisateur est supprimé puis recréé, un nouveau numéro de compartiment aléatoire lui est attribué, car il est considéré comme un nouvel utilisateur.
{% endalert %}

Si vous avez configuré un groupe de contrôle global et souhaitez utiliser des numéros de compartiment aléatoires pour d'autres cas d'utilisation, veuillez consulter [la section Points à surveiller]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for).

### Quand utiliser les numéros de compartiment aléatoire

Si vous souhaitez effectuer des tests à long terme sur l'efficacité de plusieurs campagnes ou Canvases au fil du temps, vous pouvez utiliser des numéros de compartiments aléatoires pour réaliser la segmentation de vos utilisateurs.

### Quand utiliser autre chose

Si vous souhaitez segmenter les utilisateurs à des fins de test au sein d'une seule campagne ou d'un seul canvas, veuillez utiliser [les tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) pour les campagnes. Pour les toiles, vous pouvez créer différentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) pour les tests au niveau du parcours, ou utiliser des [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) pour les tests au niveau de l'étape.

## Créer des segments au moyen des numéros de compartiment aléatoire

Lors de [la création d'un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), veuillez ajouter le filtre « Random Bucket # ». Veuillez ensuite indiquer un nombre ou une plage de nombres à inclure dans votre segment.

![Filtre de segment destiné aux numéros de compartiments aléatoires ne dépassant pas « 3000 ».]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Vous voudrez peut-être utiliser ces types de segments si vous souhaitez exécuter un test de trois variantes différentes et inclure également un groupe de contrôle. Observez le plan d’échantillonnage suivant pour la création de segments de taille égale pour trois variantes et un groupe de contrôle :

- Les numéros de compartiment 0 à 2499 correspondent au segment de contrôle
- Les numéros de compartiment 2500 à 4999 correspondent au segment qui recevra la variante 1
- Les numéros de compartiment 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de compartiment 7500 à 9999 correspondent au segment qui recevra la variante 3

Selon le nombre de segments que vous voulez et la distribution des utilisateurs au sein de chaque segment, votre plan peut différer.

Pour chacun de vos segments de numéros de compartiments aléatoires, y compris le groupe de contrôle, veuillez activer [le suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Pour évaluer le succès des variantes par rapport au groupe de contrôle, vous pouvez vous rendre sur votre page [de custom events]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) et consulter la fréquence à laquelle chaque segment a réalisé certains événements personnalisés.

{% alert tip %}
Lorsque vous utilisez des segments de numéros de compartiments aléatoires dans un canevas, par exemple comme filtre dans une étape [de l'arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/), veuillez vous assurer que vos [critères de sortie]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/) du canevas, vos filtres d'audience et vos étapes en amont ne réalisent pas de ciblage sur des segments qui chevauchent l'une de vos plages de compartiments. Si tel est le cas, les utilisateurs situés dans cette plage pourraient être supprimés de manière disproportionnée avant d'atteindre la division, ce qui entraînerait une répartition inégale entre les chemins.
{% endalert %}

### Réadmission aléatoire de l'audience à l'aide de numéros de compartiment aléatoires

La réintégration aléatoire d'audience peut être utile pour [les tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) ou pour le ciblage de groupes d'utilisateurs spécifiques dans vos campagnes. Pour effectuer une réadmission aléatoire de l’audience avec des numéros de compartiment aléatoires, procédez comme suit :

1. [Veuillez créer votre segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Veuillez définir les compartiments aléatoires. Dans votre campagne ou votre canvas, veuillez utiliser le filtre aléatoire pour répartir votre audience en différents groupes. Par exemple, vous pouvez définir précisément deux compartiments aléatoires pour répartir votre audience (50 % des utilisateurs par compartiment).
3. Dans la section **« Publics cibles** » de votre campagne ou de votre canvas, veuillez définir les paramètres du compartiment aléatoire. Cela permet à Braze d'affecter automatiquement les utilisateurs aux compartiments appropriés en fonction des pourcentages définis.
4. Configurez une logique permettant aux utilisateurs de réintégrer le segment. Par exemple, vous pouvez autoriser les utilisateurs à réintégrer le segment s'ils n'ont pas utilisé l'application pendant 15 jours.
5. Lancez votre campagne et surveillez les performances de chaque compartiment. Vous pouvez analyser des indicateurs tels que les taux d'engagement et les taux de conversion afin de déterminer l'efficacité de la réintégration aléatoire d'audience dans votre cas d'utilisation.


