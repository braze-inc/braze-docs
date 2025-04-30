---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes Push
page_order: 23
page_type: reference
description: "Cette page contient des étapes de résolution des problèmes pour divers problèmes liés au canal de communication Push."
channel: push
---

# Résolution des problèmes Push

> Cette page vous aide à résoudre les problèmes que vous pouvez rencontrer avec le canal de communication Push.

## Notifications push manquantes

Vous rencontrez des difficultés de livraison sur vos notifications push ? Il y a un certain nombre d’étapes que vous pouvez suivre pour résoudre ce problème, notamment en vérifiant :

- [Statut d’abonnement aux push](#push-subscription-status)
- [Segment](#segment)
- [Limites de notification push](#push-notification-caps)
- [Limites de débit](#rate-limits)
- [Statut du groupe de contrôle](#control-group-status)
- [Jeton push valide](#valid-push-token)
- [Notification push envoyée](#push-notification-type)
- [Application actuelle](#current-app)

#### Statut d’abonnement aux push

Les pushs ne peuvent être envoyés qu'aux utilisateurs abonnés ou ayant opté pour un abonnement. Vérifiez votre profil utilisateur dans l'onglet [Engagement de][1] la section **Profil utilisateur** pour confirmer si vous êtes activement inscrit à push pour l'espace de travail que vous testez. Si vous êtes inscrit à plusieurs applications, vous les trouverez dans le champ **Poussée inscrite pour :** 

![Push enregistré pour][2]

Vous pouvez également exporter les profils utilisateur à l’aide des endpoints d’exportation de Braze :
- [Utilisateurs par identifiant][12]
- Utilisateurs par segment][13]

Chaque endpoint renvoie un objet de jeton de notification push qui inclut des informations d’activation de notification push par appareil.

#### Segment

Assurez-vous de tomber dans le segment que vous visez (s’il s’agit d’une campagne réelle et non d’un test). Dans le **Profil de l'utilisateur**, vous verrez une liste de segments dans lesquels l'utilisateur se trouve actuellement. N’oubliez pas qu’il s’agit d’une variable qui évolue constamment, car la segmentation est mise à jour en temps réel.

![Liste des segments][3]

Vous pouvez également confirmer que l'utilisateur fait partie de la segmentation en utilisant la **recherche d'utilisateurs** lors de la création d'un segment.

![Section de recherche d'utilisateurs avec un champ de recherche.][14]{: style="max-width:80%;"}

#### Limites de notification push

Vérifiez les limites de fréquence générales. Il est possible que vous n'ayez pas reçu la notification push car votre espace de travail a une limitation de fréquence globale en place et que vous avez déjà atteint votre limite de notifications push pour la période spécifiée.

Vous pouvez le faire en vérifiant [global frequency capping][4] dans le tableau de bord. Si la campagne est définie pour suivre des règles de limite de fréquence, un certain nombre d’utilisateurs sont affectés par ces paramètres

![Détails de la campagne][5]

#### Limites de débit

Si vous avez une limite de fréquence définie pour votre campagne ou Canvas, le taux de réception de vos messages peut être impacté si vous avez dépassé cette limite. Pour plus d'informations, consultez [Limitation du débit][9].

#### Statut du groupe de contrôle

S’il s’agit d’une campagne à canal unique ou d’un Canvas avec un groupe de contrôle, il est possible que vous tombiez dans le groupe témoin.

  1. Vérifiez la distribution des variantes][6] pour voir s'il y a un groupe témoin.
  2. Si c'est le cas, créez un segment filtrant pour [dans le groupe de contrôle de la campagne][7] puis [exportez le segment][8] et vérifiez si votre identifiant utilisateur figure sur cette liste.

#### Jeton push valide
Un jeton push est un identifiant qui permet aux expéditeurs de cibler des appareils spécifiques avec une notification push. Ainsi, si l’appareil n’a pas de jeton push valide, il n’y a aucun moyen d’envoyer une notification push. 

#### Notification push envoyée

Vérifiez que vous utilisez le type correct de notification push. Par exemple, si vous souhaitez cibler un FireTV, vous devez utiliser une notification push Kindle et pas une campagne Push Android. De même, si vous souhaitez cibler un Android, utilisez une notification push Android et non une campagne push iOS. Consultez les articles suivants pour plus d’informations sur les flux de travail dans Braze pour :
- [Notification Push Apple][10]
- [Messagerie Cloud Firebase][11]

#### Application actuelle

Lorsque vous testez les envois push avec des utilisateurs internes, assurez-vous que l'utilisateur qui doit recevoir la notification push est actuellement connecté à l'application concernée. Cela peut conduire à ce que l'utilisateur ne reçoive pas de push ou reçoive un push pour lequel vous pensez qu'il n'est pas segmenté.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/données_et_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platforms/android/push_notifications/troubleshooting/
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment
[14]: {% image_buster /assets/img_archive/user_lookup.png %}