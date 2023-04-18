---
nav_title: "Migration des données utilisateur"
article_title: Migration des données utilisateur SMS non natives
page_order: 4
description: "Le présent article de référence passe en revue tous les aspects qu’un utilisateur SMS non natif doit garder à l’esprit lors de la migration des données utilisateur vers Braze."
page_type: reference
channel:
  - SMS
  
---

# Migration des données utilisateur

> Le présent article de référence détaille toutes les considérations que vous devez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze. 

## Formater les numéros de téléphone utilisateurs suivant les normes de l’opérateur

Les opérateurs de téléphonie ont un type de format spécifique auquel ils s’attendent, appelé E.164, qui est le plan international de numérotation téléphonique qui garantit que chaque appareil dispose d’un numéro unique à l’échelle mondiale. C’est ce qui permet d’acheminer correctement les appels téléphoniques et les messages texte vers des téléphones individuels dans différents pays. Les numéros E.164 sont formatés comme indiqué dans l’image suivante et ils peuvent comporter au maximum quinze chiffres. En savoir plus sur les [numéros de téléphone des utilisateurs][userphone].

![][image]{: style="max-width:50%;border: 0;"}

## Ajout d’alias aux profils utilisateur

Des alias sont nécessaires pour pouvoir capturer des événements personnalisés ou des [réponses par mot clé personnalisées][customkeyword]. Vous voudrez définir le « libellé d'alias » comme « téléphone » et le « nom d’alias » comme numéro de téléphone de l’utilisateur.

## Mettre à jour les informations historiques sur les états d’abonnement des utilisateurs

Si vous avez des informations historiques sur les [états d’abonnement][subscriptionstate] de votre utilisateur pour vos différents canaux de communication, assurez-vous de mettre à jour ces informations sur Braze. 

## Exemples d’étapes de migration

Avant de commencer à composer des campagnes SMS via Braze, vous devrez mettre à jour vos données utilisateur pour vous assurer que tout cela fonctionne. 

**Voici un bref résumé des données utilisateur que vous devrez mettre à jour sur Braze :**

1. **Importer les numéros de téléphone des utilisateurs au format correct** ([E.164][0]) exige un signe « + » et un code pays, par exemple +12408884782. Pour plus d’informations sur l’importation des numéros de téléphone utilisateur, consultez [numéros de téléphone utilisateur][userphone].
  - Utilisez l’endpoint de l'API REST [utilisateurs/suivi][1] pour attribuer la valeur `phone`.<br><br>

2. **Ajouter un alias utilisateur** à des profils d’utilisateurs identifiés avec le numéro de téléphone d’un utilisateur. Le format requis pour ce message est alias_label : 'phone' et alias_name : '+12408884782'
  - Utilisez l’endpoint API REST [users/alias/new][2] pour attribuer un alias à des profils utilisateur existants.
  - Il existe aussi des méthodes SDK pour attribuer un alias à des  utilisateurs [iOS][3] / [Android][4] / [Web][5].<br><br>

3. **Attribuer l’[état d’abonnement][subscriptionstate]** SMS de votre utilisateur (par ex., abonné ou désabonné) si vous disposez de cette information.
  - Utilisez l’endpoint API REST [subscription/status/set][6] pour définir les utilisateurs comme étant abonnés ou désabonnés de votre ou vos groupes d’abonnement SMS.
  - Notez que lorsque les groupes d’abonnement SMS ont été configurés dans votre tableau de bord, vous pourrez saisir les `subscription_group_id` nécessaires dont vous aurez besoin pour votre demande API.


[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
