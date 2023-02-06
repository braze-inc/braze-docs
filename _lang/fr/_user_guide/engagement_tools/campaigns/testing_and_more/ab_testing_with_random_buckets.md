---
nav_title: Tests A/B avec des compartiments aléatoires
article_title: Tests A/B avec des compartiments aléatoires
page_order: 2
page_type: tutorial
description: "Le présent article pratique passe en revue le concept de tests A/B et de variantes et la manière dont vous pouvez les utiliser dans vos campagnes Braze."
page_type: reference
tool:
  - Campagne

---

# Tests A/B avec des compartiments aléatoires

> Le présent article couvrira le concept des tests A/B et des variantes, comment vous pouvez les utiliser dans vos campagnes Braze, ainsi que la manière d’attribuer et d’implémenter des numéros de compartiment aléatoire pour aider à recueillir des données utiles.

Un numéro de compartiment aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. Ces segments peuvent être utilisés pour réaliser des tests A/B pour les Campaign Variants sur une période prolongée.

Si vous avez [Canvas][13] sur votre plateforme Braze, vous pourrez accomplir tous ces cas d’utilisation à l’aide de l’IU de Canvas.

Voici comment configurer un test A/B avec des compartiments aléatoires :

## Étape 1 : Segmenter vos utilisateurs par attribut de compartiment aléatoire

Appliquez le filtre **Random Bucket #** (N° de compartiment aléatoire). Une fois appliqué, l’étiquette du filtre passe à **Statistical sampling ID** (ID d’échantillonnage statistique).

{% alert note %}
Chaque utilisateur de votre application se voit affecter aléatoirement au numéro de compartiment aléatoire compris entre 0 et 9999 (inclus).
{% endalert %}

L’exemple suivant documente partiellement la création de segments pour une campagne avec trois variantes et un groupe de contrôle. Notez que les segments recevant les Campaign Variants et le segment de contrôle ne doivent pas nécessairement être égaux.

Observez le plan d’échantillonnage suivant pour la création de segments de taille égale pour trois variantes de séries de campagnes et un groupe de contrôle : 

- Les numéros de compartiment 0 à 2499 correspondent au segment de contrôle
- Les numéros de compartiment 2500 à 4999 correspondent au segment qui recevra la variante 1 
- Les numéros de compartiment 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de compartiment 7500 à 9999 correspondent au segment qui recevra la variante 3. 

Vous voudrez peut-être utiliser ces types de segments si vous souhaitez exécuter un test de trois variantes différentes (par exemple, trois heures d’envoi différentes ou trois combinaisons différentes de canaux de messages) et inclure également un groupe de contrôle.

![][1]

![][2]

Pour chacun de vos segments créés, y compris le groupe de contrôle, activez l’[Suivi analytique][14]. Lors de l’évaluation de la réussite des variantes par rapport au groupe de contrôle, vous serez en mesure de vous rendre dans votre page [Événements personnalisés][15] et voir la fréquence à laquelle chaque segment a effectué certains événements personnalisés.

## Étape 2 : Créer vos variantes de campagne {#campaign-variants}

### Étape 2a : Créer votre première variante

Créez une campagne. À l’étape **Target Users** (Utilisateurs cibles) sélectionnez un segment de destinataires. Le segment que vous choisissez sera celui créé à l’étape précédente.

![][4]

### Étape 2b : Créer des variantes supplémentaires

[Dupliquez][18] votre Campaign Variant initiale et modifiez-la en conséquence. Par exemple, vous pouvez décider de modifier l’heure d’envoi ou la combinaison de canaux de messagerie utilisés. Lors du ciblage des utilisateurs, sélectionnez le segment qui doit recevoir cette nouvelle Campaign Variant. Répétez cette étape pour créer vos Campaign Variants restants. Votre groupe de contrôle ne doit pas recevoir de variante de cette campagne.

### Modifier les pourcentages de Campaign Variant

Dans une campagne, si un pourcentage de variante est modifié après la création initiale, les utilisateurs peuvent être redistribués vers d’autres variantes.

Les utilisateurs sont affectés de manière aléatoire à une variante spécifique avant qu’ils ne reçoivent la campagne pour la première fois. À chaque réception de campagne (ou lorsque l’utilisateur entre à nouveau dans une Canvas Variant), ils recevront la même variante à moins que les pourcentages de variante soient modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes. Les utilisateurs restent alors dans ces variantes jusqu’à ce que les pourcentages soient à nouveau modifiés. Les utilisateurs ne seront redistribués que pour les variantes qui ont été modifiées. Par exemple, si vous n’avez modifié que la variante A et la variante B, les utilisateurs de votre troisième variante C ne seraient pas redistribués, car le pourcentage de la variante C n’a pas été modifié.

Les groupes de contrôles restent uniformes si le pourcentage de variantes est inchangé. Les utilisateurs ayant précédemment reçu des messages ne peuvent pas accéder à un groupe de contrôle lors d’un envoi ultérieur, tout comme un utilisateur du groupe de contrôle ne peut recevoir un message.

## Étape 3 : Créer des messages supplémentaires

Si vous le souhaitez, vous pouvez continuer à envoyer des Campaign Variants à vos segments de compartiment aléatoire au fil du temps en répétant l’[étape 2](#campaign-variants). Un exemple de cas d’utilisation consiste à tester la différence entre l’envoi de 2 notifications en une semaine à un groupe au lieu d’une seule. 

Assurez-vous de planifier les flux de travail des variantes de votre série de campagnes à l’avance afin de préserver l’intégrité de votre test A/B.

## Cas d’utilisation courants

Étant donné que la création d’un [test multivarié][16] vous permet de tester facilement le contenu, utiliser des compartiments aléatoires convient mieux pour tester les combinaisons de livraison, de cadence et de canaux.

Tous les cas d’utilisation suivants peuvent être atteints avec [Canvas][13], un outil construit pour ces types d’expériences.

### Livraison

Vous pouvez comparer les résultats entre une campagne envoyée par [livraison programmée][11], [livraison par événement][17] et à [timing intelligent][12].

### Cadence

Vous pouvez tester plusieurs flux de messagerie sur une période donnée. Par exemple, vous pouvez tester deux cadences d’onboarding différentes : une qui envoie deux messages au cours des deux premières semaines de l’utilisateur et une qui envoie trois messages sur la même période. Vous pouvez également tester l’efficacité d’envoyer deux messages de rappel dans une semaine, ou en envoyer juste un lorsque vous ciblez les utilisateurs inactifs.

### Canaux de communication

Vous pouvez tester l’efficacité de différentes combinaisons de canaux de messages. Par exemple, vous pouvez comparer l’impact entre un seul e-mail et un e-mail combiné à une notification push.


[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %}
[2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %}
[4]: {% image_buster /assets/img_archive/random_buckets_target.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/
[12]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[13]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[15]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[17]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/duplicating_segments_and_campaigns/#cloning-a-campaign
