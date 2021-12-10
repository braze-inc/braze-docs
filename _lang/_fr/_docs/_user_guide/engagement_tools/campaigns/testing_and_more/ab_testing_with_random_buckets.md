---
nav_title: Tests A/B avec Seaux Aléatoires
article_title: Tests A/B avec Seaux Aléatoires
page_order: 2
page_type: Référence
description: "Cet article décrit le concept de tests A/B et de variantes et comment vous pouvez les utiliser dans vos campagnes de Braze."
tool:
  - Campagnes
---

# Tests A/B avec segments aléatoires

> Cet article couvrira le concept de tests A/B et de variantes, comment vous pouvez les utiliser dans vos campagnes de Braze, ainsi que la façon d'affecter et d'implémenter des numéros de compartiments aléatoires pour aider à recueillir des données utiles.

Un numéro de bucket aléatoire est un attribut utilisateur qui peut être utilisé pour créer des segments uniformément distribués d'utilisateurs aléatoires. Ces segments peuvent être exploités pour effectuer des tests A/B sur des variantes de campagne sur une période prolongée.

Si vous avez [Canvas][13] sur votre plateforme Braze, vous serez en mesure d'accomplir tous ces cas d'utilisation en utilisant l'interface utilisateur Canvan.

Voici comment vous pouvez configurer un test A/B avec des compartiments aléatoires:

## Étape 1 : Segmentez vos utilisateurs par l'attribut Segcket aléatoire

Applique le filtre **Seau aléatoire #**. Une fois appliqué, l'étiquette du filtre passera à **ID d'échantillonnage statistique**.

{% alert note %}
Chaque utilisateur de votre application reçoit aléatoirement un numéro de seau aléatoire compris entre 0 et 9999 (inclus).
{% endalert %}

L'exemple ci-dessous documente partiellement la création de segments pour une campagne avec trois variantes et un groupe de contrôle. Notez que les segments qui reçoivent les variantes de la campagne et le segment de contrôle n'ont pas nécessairement besoin d'être égaux en taille.

Considérez le plan d'échantillonnage suivant pour la création de segments de taille égale pour trois variantes de la série de campagne et un contrôle :

- Les numéros du seau 0 à 2499 correspondent au segment de contrôle
- Les numéros du segment 2500 à 4999 correspondent au segment qui recevra la variante 1
- Les numéros de seau de 5000 à 7499 correspondent au segment qui recevra la variante 2
- Les numéros de seau de 7500 à 9999 correspondent au segment qui recevra la variante 3.

Vous pouvez utiliser ces types de segments si vous voulez exécuter un test de trois variantes différentes (par exemple, trois heures d'envoi différentes ou trois combinaisons différentes de canaux de messagerie) et incluent également un groupe de contrôle.

!\[Sélection de filtres\]\[1\]

!\[Filtre d'exemple\]\[2\]

Pour chacun de vos segments créés, y compris le groupe de contrôle, activez [Suivi Analytiques][14]. Lors de l'évaluation du succès des variantes par rapport au groupe de contrôle, vous serez en mesure d'aller dans votre page d'événements [Personnalisés][15] et de voir à quelle fréquence chaque segment a complété certains événements personnalisés.

## Étape 2 : Créez vos variantes de campagne

### Étape 2a : Créez votre première variante

Créer une campagne. Sur la page **Utilisateurs cibles** , sélectionnez un segment de destinataires. Le segment que vous choisissez sera celui qui a été créé à l'étape précédente.

!\[Select Campaign Recipient Segment\]\[4\]

### Étape 2b : Construire des variantes supplémentaires

[Dupliquez][18] votre variante de campagne initiale et modifiez-la en conséquence. Par exemple, vous pouvez décider de changer l'heure d'envoi ou la combinaison des canaux de messagerie utilisés. Lors du ciblage des utilisateurs, sélectionnez le segment que vous souhaitez recevoir cette nouvelle variante de campagne. Répétez cette étape pour créer vos variantes de campagne restantes. Votre groupe de contrôle ne devrait recevoir aucune variante de cette campagne.

## Étape 3 : Construire des messages supplémentaires

Si vous le souhaitez, vous pouvez continuer à envoyer des variantes de campagne à vos segments aléatoires au fil du temps en répétant l'étape 2. Un exemple de cas d'utilisation est de tester la différence entre l'envoi d'une notification de groupe 2 en une semaine, par rapport à 1.

Assurez-vous de planifier à l'avance les flux de travail des variantes de votre série de campagne afin de maintenir l'intégrité de votre test A/B.

## Cas d'utilisation courants

Parce que la création d'un [test multivarié][16] vous permet de tester facilement le contenu, utiliser des segments aléatoires est mieux adapté pour tester les combinaisons de livraison, de cadence et de canaux.

Tous les cas d'utilisation ci-dessous peuvent être réalisés dans [Canvas][13], un outil construit avec ces types d'expériences à l'esprit.

### Envoi

Vous pouvez comparer les résultats d'une campagne envoyée avec [planifié][11], [livraison basée sur l'action][17] et [timing intelligent][12].

### Cadence

Vous pouvez tester plusieurs flux de messagerie sur une période de temps. Par exemple, vous pouvez tester deux cadences d'intégration différentes : une qui envoie deux messages dans les deux premières semaines de l'utilisateur. et un qui envoie trois messages dans les deux premières semaines de l'utilisateur. Ou, en ciblant les utilisateurs qui sont en train de disparaître, vous pouvez tester l'efficacité de l'envoi de deux messages de retour en une semaine, contre en envoyant un seul.

### Canaux de messagerie

Vous pouvez tester l'efficacité de différentes combinaisons de canaux de messages. Par exemple, vous pouvez comparer l'impact de l'utilisation d'un seul email par rapport à un email combiné à un push.

### Pourcentage de variante de la campagne

Dans une campagne, si un pourcentage de variante est modifié après la création initiale, vous constaterez que les utilisateurs peuvent être redistribués à d'autres variantes.

Au départ, une variante particulière est assignée aléatoirement aux utilisateurs avant de recevoir une campagne pour la première fois. À partir de là, chaque fois que la campagne est reçue (ou que l'utilisateur rentre une variante de campagne), ils recevront la même variante à moins que les pourcentages de variante ne soient modifiés. Si les pourcentages de variante changent, les utilisateurs peuvent être redistribués à d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés. Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Les utilisateurs qui ont déjà reçu des messages ne peuvent pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne peut recevoir de message.
[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %} [2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %} [4]: {% image_buster /assets/img_archive/random_buckets_target.png %}

[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/
[12]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[13]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#turning-analytics-tracking-on-and-off
[15]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#multivariate-testing
[17]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/duplicating_segments_and_campaigns/#cloning-a-campaign
