---
nav_title: "Migration des données utilisateur"
article_title: Migration des données utilisateur
page_order: 4
description: "Le présent article de référence s’exécute dans toutes les considérations que vous devez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze."
page_type: reference
channel:
  - SMS
noindex: true

---

# Migration des données utilisateur

> Le présent article détaille toutes les considérations que vous devez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze.

## Formater les numéros de téléphone utilisateurs suivant les normes de l’opérateur

Les opérateurs de téléphonie ont un type de format spécifique qu'ils attendent appelé E.164, qui est le plan de numérotation téléphonique international qui garantit que chaque appareil a un numéro unique au monde. C'est ce qui permet aux appels téléphoniques et aux messages texte d'être correctement acheminés vers des téléphones individuels dans différents pays. E.164 les numéros sont formatés comme indiqué dans l'image suivante et peuvent avoir un maximum de 15 chiffres.

![E.164 format consiste en un signe plus, un indicatif de pays, un indicatif régional et un numéro de téléphone][image]{: style="max-width:50%;border: 0;"}

Pour plus d'informations, consultez [Numéros de téléphone utilisateur][userphone].

## Mettre à jour les informations historiques sur les états d’abonnement des utilisateurs

Si vous avez des informations historiques sur les [états d'abonnement][état d'abonnement] de vos utilisateurs pour vos différents canaux de messagerie, assurez-vous de mettre à jour ces informations dans Braze.

## Exemples d’étapes de migration

Avant de commencer à composer des campagnes SMS via Braze, vous devrez mettre à jour vos données utilisateur pour vous assurer que tout cela fonctionne.

**Voici un résumé rapide des données utilisateur que vous devrez mettre à jour dans Braze :**

1. **Importer les numéros de téléphone des utilisateurs dans le bon format** ([E.164][0]) le formatage nécessite un signe plus (+) et un indicatif de pays. Un exemple est +12408884782. Pour plus d'informations sur la façon d'importer des numéros de téléphone des utilisateurs, consultez [Numéros de téléphone des utilisateurs][userphone].
    * Utilisez le point de terminaison [`/users/track`][1] pour attribuer la valeur `phone`.<br><br>

2. **Attribuez l'[état d'abonnement][subscription state]** aux SMS de votre utilisateur (par exemple, abonné ou désabonné) si vous disposez de cette information.
    * Utilisez le [`/subscription/status/set` endpoint][6] pour définir les utilisateurs comme abonnés ou désabonnés de vos groupes d'abonnement SMS.

{% alert note %}
Après avoir configuré les Groupes d'Abonnement SMS dans votre tableau de bord, vous pourrez récupérer le `subscription_group_id` associé, dont vous aurez besoin pour votre demande d'API.
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword] : {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate] : {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
