---
nav_title: "Migration des données utilisateur"
article_title: Migration de données utilisateur SMS
page_order: 4
description: "Cet article de référence passe en revue toutes les considérations que vous devrez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze pour envoyer des SMS."
page_type: Référence
channel:
  - SMS
---

# Migration des données utilisateur

Parlons de toutes les considérations que vous devrez garder à l’esprit lorsque vous migrez vos données utilisateur vers Braze.

{% alert important %}
Êtes-vous actuellement un client SMS non-natif ? Si c'est le cas, veuillez visiter la [documentation SMS non-native](/docs/user_guide/message_building_by_channel/sms/non_native/) pour votre article de migration de données utilisateur correspondante.
{% endalert %}

## Formater les numéros de téléphone des utilisateurs selon les normes de l'opérateur

Les opérateurs téléphoniques ont un format spécifique qu'ils s'attendent à appeler E. 64 qui est le plan international de numérotation téléphonique qui assure que chaque appareil a un numéro unique à l'échelle mondiale. C'est ce qui permet aux appels téléphoniques et aux SMS d'être correctement acheminés vers des téléphones individuels dans différents pays. Les numéros E.164 sont formatés comme indiqué ci-dessous et peuvent avoir un maximum de quinze (15) chiffres. [En savoir plus ici.][userphone]<br> !\[e164\]\[picture\]{: style="max-width:50%;border: 0;"}

## Mettre à jour l'historique des informations sur les états d'abonnement des utilisateurs

Si vous avez des informations historiques sur les [états d'abonnement de votre utilisateur][subscriptionstate] pour vos différents canaux de messagerie, Assurez-vous de mettre à jour cette information au Brésil.

## Étapes de migration d'exemple

Avant de commencer à rédiger des campagnes SMS via Braze, vous devrez mettre à jour vos données utilisateur pour vous assurer que tout cela fonctionne.

__Voici un bref résumé des données utilisateur dont vous aurez besoin pour mettre à jour au Brésil :__

1. __Importer les numéros de téléphone des utilisateurs dans le format correct__ ([E.164][]) formatage nécessite un '+' et un code de pays, par exemple +12408884782. Pour plus d'informations sur la façon d'importer les numéros de téléphone de l'utilisateur, consultez notre [documentation][userphone].
  - Utilisez le point de terminaison [utilisateurs/piste][1] de l'API REST pour affecter la valeur du `téléphone`.<br><br>

2. __Assigner l'état d'abonnement [SMS de votre utilisateur][subscriptionstate]__ (par exemple, souscrit ou désabonné) si vous avez ces informations.
  - Utilisez le point de terminaison [abonnement/statut/set][6] de l'API REST pour définir les utilisateurs comme abonnés ou désabonnés de votre/vos groupe(s) d'abonnement SMS.
  - Notez qu'une fois que les groupes d'abonnement SMS ont été configurés dans votre tableau de bord, vous pourrez récupérer les `subscription_group_id nécessaires` dont vous aurez besoin pour votre requête API.
[picture]: {% image_buster /assets/img/sms/e164.jpg %}

[E.164]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
