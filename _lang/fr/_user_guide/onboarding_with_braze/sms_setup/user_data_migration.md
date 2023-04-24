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

{% alert important %}
Êtes-vous actuellement un client SMS non natif (n’avez-vous pas ou ne passerez-vous pas à la capacité de traitement des mots clés natifs de Braze) ? Si oui, consultez notre collection d'[articles sur les SMS non natifs ](/docs/user_guide/message_building_by_channel/sms/non_native/)pour obtenir votre document de migration des données utilisateur correspondant.
{% endalert %}

## Formater les numéros de téléphone utilisateurs suivant les normes de l’opérateur

Les opérateurs de téléphonie ont un type de format spécifique auquel ils s’attendent, appelé E.164, qui est le plan international de numérotation téléphonique qui garantit que chaque appareil dispose d’un numéro unique à l’échelle mondiale. C’est ce qui permet d’acheminer correctement les appels téléphoniques et les messages texte vers des téléphones individuels dans différents pays. Les nombres E.164 sont formatés comme indiqué sur l’image suivante et peuvent comporter un maximum de 15 chiffres.

![Le format E.164 comprend un signe plus, un code pays, un indicatif régional et un numéro de téléphone][picture]{: style="max-width:50%;border: 0;"}

Pour plus d’informations, consultez [Numéros de téléphone utilisateur][userphone].

## Mettre à jour les informations historiques sur les états d’abonnement des utilisateurs

Si vous avez des informations historiques sur les [états d’abonnement][subscriptionstate] de votre utilisateur pour vos différents canaux de communication, assurez-vous de mettre à jour ces informations sur Braze.

## Exemples d’étapes de migration

Avant de commencer à composer des campagnes SMS via Braze, vous devrez mettre à jour vos données utilisateur pour vous assurer que tout cela fonctionne.

**Voici un bref résumé des données utilisateur que vous devrez mettre à jour sur Braze :**

1. **Importer les numéros de téléphone des utilisateurs au format correct** ([E.164][0]). Le formatage nécessite un signe plus « + » et un cmode pays, par ex. +12408884782. Pour plus d’informations sur l’importation des numéros de téléphone des utilisateurs, consultez [Numéros de téléphone utilisateur][userphone].
    * Utilisez l’endpoint de l'API REST [users/track][1] pour attribuer la valeur `phone`.<br><br>

2. **Attribuer l’[état d’abonnement][subscriptionstate]** SMS de votre utilisateur (par ex., abonné ou désabonné) si vous disposez de cette information.
    * Utilisez l’endpoint API REST [subscription/status/set][6] pour définir les utilisateurs comme étant abonnés ou désabonnés à vos groupes d’abonnement SMS.

{% alert note %}
Une fois que vous avez configuré les groupes d’abonnement SMS dans votre tableau de bord, vous pourrez saisir les `subscription_group_id`, dont vous aurez besoin pour votre requête API.
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
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states
