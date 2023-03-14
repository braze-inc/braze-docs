---
nav_title: Numéros de compartiment aléatoire
article_title: Numéros de compartiment aléatoire
page_order: 2
page_type: reference
description: "Cet article couvre le concept de numéros de compartiment aléatoire et la manière de les utiliser pour créer des variantes et des groupes de contrôle."
page_type: reference
tool:
  - Campagne
  - Canvas

---

# Numéros de compartiment aléatoire

> Cet article couvre le concept de numéros de compartiment aléatoire et la manière de les utiliser pour créer des variantes et des groupes de contrôle.

## Aperçu

Lorsqu’un profil d’utilisateur est créé dans Braze, l’utilisateur reçoit automatiquement un numéro de compartiment aléatoire compris entre 0 et 9999. Un numéro de compartiment aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. Vous pouvez tirer parti de ces segments pour test et l’efficacité de plusieurs campagnes ou Canvas sur les groupes d’utilisateurs au fil du temps.

Les numéros de compartiment aléatoire sont aussi utilisés dans votre groupe de contrôle global, un groupe d’utilisateurs ne recevant ni campagnes, ni Canvas. Braze sélectionne de manière aléatoire plusieurs plages de numéros de compartiment aléatoires et inclut les utilisateurs faisant partie des compartiments sélectionnés. Si vous avez défini un groupe de contrôle global et si vous voulez utiliser les numéros de compartiment aléatoire à d’autres fins [Choses à garder à l’esprit]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for).

### Quand utiliser les numéros de compartiment aléatoire

Si vous voulez effectuer des tests à long terme de l’efficacité de plusieurs campagnes ou Canvas au fil du temps, vous pouvez utiliser les numéros de compartiment aléatoire pour segmenter vos utilisateurs.

### Quand utiliser autre chose

Si vous souhaitez segmenter vos utilisateurs pour effectuer des tests au sein d’une seule campagne ou d’un seul Canvas, utilisez plutôt les [Tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) pour les campagnes. Pour les Canvas, vous pouvez créer différentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) pour les tests au niveau du parcours ou utiliser les [chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) pour les tests au niveau de l’étape.

## Créer des segments au moyen des numéros de compartiment aléatoire

Lorsque vous [créez un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), ajoutez le filtre `Numéro de compartiment aléatoire`. L’étiquette du filtre passe à **Statistical sampling ID (ID d’échantillonnage statistique)**. Vous pouvez alors spécifier un nombre ou une plage de nombres à inclure dans le segment.

![][1]

![][2]

Vous voudrez peut-être utiliser ces types de segments si vous souhaitez exécuter un test de trois variantes différentes et inclure également un groupe de contrôle. Observez le plan d’échantillonnage suivant pour la création de segments de taille égale pour trois variantes et un groupe de contrôle :

- Les numéros de compartiment 0 à 2499 correspondent au segment de contrôle
- Les numéros de compartiment 2500 à 4999 correspondent au segment qui recevra la variante 1
- Les numéros de compartiment 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de compartiment 7500 à 9999 correspondent au segment qui recevra la variante 3

Selon le nombre de segments que vous voulez et la distribution des utilisateurs au sein de chaque segment, votre plan peut différer.

Pour chacun de vos segments par numéro de compartiment aléatoire, y compris le groupe de contrôle, activez l’[Analytics Tracking (Suivi analytique)]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking). Lors de l’évaluation de la réussite des variantes par rapport au groupe de contrôle, vous pouvez vous rendre dans votre page [Custom Events (Événements personnalisés)]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data) et voir la fréquence à laquelle chaque segment a effectué certains événements personnalisés.


[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %}
[2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %}
