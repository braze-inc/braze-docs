---
nav_title: Notifications push manquantes
article_title: Notifications push manquantes
page_order: 3
page_type: Solution
description: "Cet article d'aide vous guide à travers les étapes de dépannage que vous pouvez prendre si les utilisateurs ne reçoivent pas vos notifications push."
channel: Pousser
---

# Notifications push manquantes

Expérimentez les défis de livraison avec les notifications push ? Il y a un certain nombre d'étapes que vous pouvez prendre pour résoudre ce problème en vérifiant le :

* [Statut de l'abonnement Push](#check-push-subscription-status)
* [Segment](#check-segment)
* [Capsules de notification push](#check-push-notification-caps)
* [Limites de taux](#check-rate-limits)
* [Contrôler le statut du groupe](#check-control-group-status)

### Statut de l'abonnement Push

Vérifiez votre profil utilisateur dans l'onglet [Engagement][1] dans la section **Profil utilisateur** pour voir si vous êtes activement inscrit pour le groupe d'application que vous testez. Si vous êtes enregistré pour plusieurs applications, vous les verrez dans le champ **Push Registered For**:

!\[Push Registered For\]\[2\]

Vous pouvez également exporter les profils d'utilisateurs à l'aide de points d'exportation Braze :
- [Utilisateurs par identifiant][12]
- [Utilisateurs par segment][13] Cela retournera un objet jeton push qui inclut les informations d'activation de push par appareil.

### Segment

Assurez-vous de tomber dans le segment que vous visez (si c'est une campagne en direct et non un test). Dans le **Profil utilisateur**, vous verrez une liste de segments dans lesquels l'utilisateur se trouve actuellement. Rappelez-vous qu'il s'agit d'une variable en constante évolution car la segmentation est mise à jour en temps réel.

!\[Liste des Segments\]\[3\]

### Capsules de notification push

Vérifiez la limite de fréquence globale. Il est possible que vous n'ayez pas reçu la notification push parce que votre groupe d'applications a un plafonnement de fréquence global en place et que vous avez déjà atteint votre limite de notification push pour la période spécifiée.

Vous pouvez le faire en vérifiant [le plafonnement de fréquence globale][4] dans le tableau de bord. Si la campagne est configurée pour se conformer aux règles de plafonnement des fréquences, il y aura un certain nombre d'utilisateurs impactés par ces paramètres

!\[Détails de la campagne\]\[5\]

### Limites de taux

Si vous avez une limite de taux définie pour votre campagne ou Canvas, vous pourriez ne plus recevoir de messages en raison du dépassement de cette limite. Pour plus d'informations, reportez-vous à la section [Limitation de taux][9].

### Contrôler le statut du groupe

S'il s'agit d'une campagne à un seul canal ou d'une Canvas avec un groupe de contrôle, il est possible que vous tombiez dans le groupe de contrôle.

  1. Vérifiez la [distribution de variantes][6] pour voir s'il y a un groupe de contrôle.
  2. Dans l'affirmative, créer un filtrage de segment pour [dans le groupe de contrôle de campagne][7] puis [exporter le segment][8] et vérifier si votre identifiant d'utilisateur est dans cette liste.

### Jeton de push valide
Un jeton push est un identifiant que les expéditeurs utilisent pour cibler des périphériques spécifiques avec une notification push. Donc, si l'appareil n'a pas de jeton push valide, alors il n'y a aucun moyen d'envoyer une notification push à lui.

### Type de notification push

Vérifiez que vous utilisez le bon type de notification push. Par exemple, si vous voulez cibler un FireTV, alors vous utiliserez une notification Kindle push, pas une campagne de push Android. Consultez les articles ci-dessous pour plus d'informations sur le déblocage du workflow de Braze pour:
- [Notification Push Apple][10]
- [Messagerie Firebase Cloud][11]

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 21 janvier 2021_
[2]: {% image_buster /assets/img_archive/trouble1.png %} [3]: {% image_buster /assets/img_archive/trouble2.png %} [5]: {% image_buster /assets/img_archive/trouble3.png %}

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment