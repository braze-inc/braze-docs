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

> Un numéro de compartiment aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. Lorsqu’un profil d’utilisateur est créé dans Braze, l’utilisateur reçoit automatiquement un numéro de compartiment aléatoire compris entre 0 et 9999. Vous pouvez utiliser ces segments pour tester l'efficacité de plusieurs campagnes ou Canvases sur des groupes d'utilisateurs au fil du temps.

## Aperçu

Les numéros de compartiment aléatoire sont utilisés dans votre groupe de contrôle global, un groupe d'utilisateurs qui ne reçoit aucune campagne ni aucune toile. Braze sélectionne de manière aléatoire plusieurs plages de numéros de compartiment aléatoires et inclut les utilisateurs faisant partie des compartiments sélectionnés. 

Si vous avez mis en place un groupe de contrôle global et que vous souhaitez utiliser des numéros de compartiment aléatoire pour d'autres cas d'utilisation, consultez les [points à surveiller.]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for)

### Quand utiliser les numéros de compartiment aléatoire

Si vous souhaitez effectuer des tests à long terme sur l'efficacité de plusieurs campagnes ou Canvases au fil du temps, vous pouvez utiliser des numéros de compartiment aléatoire pour segmenter vos utilisateurs.

### Quand utiliser autre chose

Si vous souhaitez segmenter les utilisateurs pour des essais au sein d'une même campagne ou d'un même Canvas, utilisez les [tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) pour les campagnes. Pour les toiles, vous pouvez créer différentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) pour les tests au niveau du parcours, ou utiliser des [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) pour les tests au niveau de l'étape.

## Créer des segments au moyen des numéros de compartiment aléatoire

Lors de la [création d'un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), ajoutez le filtre "Random Bucket #". Ensuite, indiquez un nombre ou une plage de nombres à inclure dans votre segmentation.

![Un filtre de segmentation pour les numéros de compartiment aléatoires ne dépassant pas "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Vous voudrez peut-être utiliser ces types de segments si vous souhaitez exécuter un test de trois variantes différentes et inclure également un groupe de contrôle. Observez le plan d’échantillonnage suivant pour la création de segments de taille égale pour trois variantes et un groupe de contrôle :

- Les numéros de compartiment 0 à 2499 correspondent au segment de contrôle
- Les numéros de compartiment 2500 à 4999 correspondent au segment qui recevra la variante 1
- Les numéros de compartiment 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de compartiment 7500 à 9999 correspondent au segment qui recevra la variante 3

Selon le nombre de segments que vous voulez et la distribution des utilisateurs au sein de chaque segment, votre plan peut différer.

Pour chacun de vos segments de numéros de compartiment aléatoires (y compris le groupe de contrôle), activez le [suivi analytique]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Pour évaluer la satisfaction des variantes par rapport au groupe de contrôle, vous pouvez vous rendre sur votre page d'[événements personnalisés]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) et voir à quelle fréquence chaque segment a réalisé certains événements personnalisés.

### Réintégration aléatoire de l'audience à l'aide de numéros de compartiment aléatoires

La réinscription aléatoire d'une audience peut être utile pour les [tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) ou le ciblage de groupes d'utilisateurs spécifiques dans vos campagnes. Pour effectuer une rentrée aléatoire de l'audience avec des numéros de compartiment aléatoires, procédez comme suit :

1. [Créez votre segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Définissez les compartiments aléatoires. Dans votre campagne ou Canvas, utilisez le filtre de compartiment aléatoire pour diviser votre audience en différents groupes. Par exemple, vous pouvez spécifier exactement deux compartiments aléatoires pour diviser votre audience (50 % des utilisateurs par compartiment).
3. Dans la section **Audiences cibles** de votre campagne ou Canvas, spécifiez les paramètres du compartiment aléatoire. Cela permet à Braze d'affecter automatiquement les utilisateurs aux compartiments appropriés en fonction des pourcentages définis.
4. Mettez en place une logique qui permette aux utilisateurs d'entrer à nouveau dans le segment. Par exemple, vous pouvez permettre aux utilisateurs de réengager le segment s'ils ne se sont pas engagés avec une appli pendant 15 jours.
5. Lancez votre campagne et surveillez les performances de chaque compartiment. Vous pouvez analyser des indicateurs tels que les taux d'engagement et les taux de conversion pour déterminer l'efficacité de la réinscription aléatoire de l'audience dans le cadre de votre cas d'utilisation.


