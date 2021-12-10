---
nav_title: "Migration des données utilisateur"
article_title: Migration des données des utilisateurs SMS non natifs
page_order: 4
description: "Cet article de référence passe à travers toutes les considérations qu'un utilisateur SMS non-natif devrait garder à l'esprit lors de la migration des données utilisateur vers Braze."
page_type: Référence
channel:
  - SMS
---

# Migration des données utilisateur

Parlons de toutes les considérations que vous devrez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze.

## Formater les numéros de téléphone des utilisateurs selon les normes de l'opérateur

Les opérateurs téléphoniques ont un format spécifique qu'ils s'attendent à appeler E. 64 qui est le plan international de numérotation téléphonique qui assure que chaque appareil a un numéro unique à l'échelle mondiale. C'est ce qui permet aux appels téléphoniques et aux SMS d'être correctement acheminés vers des téléphones individuels dans différents pays. Les numéros E.164 sont formatés comme indiqué ci-dessous et peuvent avoir un maximum de quinze (15) chiffres. [En savoir plus ici.][userphone]<br> !\[e164\]\[picture\]{: style="max-width:50%;border: 0;"}

## Ajout d'alias aux profils de l'utilisateur

Les alias sont nécessaires pour pouvoir capturer des événements personnalisés ou des [réponses personnalisées de mots clés][customkeyword]. Vous devrez définir l'étiquette de l'alias à « téléphone» et le « pseudo» au numéro de téléphone de l'utilisateur.

## Mettre à jour l'historique des informations sur les états d'abonnement des utilisateurs

Si vous avez des informations historiques sur les [états d'abonnement de votre utilisateur][subscriptionstate] pour vos différents canaux de messagerie, Assurez-vous de mettre à jour cette information au Brésil.

## Étapes de migration d'exemple

Avant de commencer à rédiger des campagnes SMS via Braze, vous devrez mettre à jour vos données utilisateur pour vous assurer que tout cela fonctionne.

__Voici un bref résumé des données utilisateur dont vous aurez besoin pour mettre à jour au Brésil :__

1. __Importer les numéros de téléphone des utilisateurs dans le format correct__ ([E.164][]) formatage nécessite un '+' et un code de pays, par exemple +12408884782. Pour plus d'informations sur la façon d'importer les numéros de téléphone de l'utilisateur, consultez notre [documentation][userphone].
  - Utilisez le point de terminaison [utilisateurs/piste][1] de l'API REST pour affecter la valeur du `téléphone`.<br><br>

2. __Ajouter un alias d'utilisateur__ aux profils d'utilisateurs identifiés avec le numéro de téléphone d'un utilisateur. Le format requis pour cela est alias_label: 'téléphone' et '+12408884782'
  - Utilisez le point de terminaison de l'API REST [utilisateurs/alias/nouveau][2] pour assigner un alias aux profils d'utilisateurs existants.
  - There are also SDK methods for Aliasing Users [iOS][3] / [Android][4] / [Web][5].<br><br>

3. __Assigner l'état d'abonnement [SMS de votre utilisateur][subscriptionstate]__ (par exemple, souscrit ou désabonné) si vous avez ces informations.
  - Utilisez le point de terminaison [abonnement/statut/set][6] de l'API REST pour définir les utilisateurs comme abonnés ou désabonnés de votre/vos groupe(s) d'abonnement SMS.
  - Notez qu'une fois que les groupes d'abonnement SMS ont été configurés dans votre tableau de bord, vous pourrez récupérer les `subscription_group_id nécessaires` dont vous aurez besoin pour votre requête API.
[picture]: {% image_buster /assets/img/sms/e164.jpg %}


[E.164]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
