---
nav_title: Cycle de vie du profil de l'utilisateur
article_title: Cycle de vie du profil de l'utilisateur
page_order: 2
page_type: reference
description: "Cet article de référence décrit le cycle de vie du profil de l'utilisateur dans Braze, et les différentes façons d’identifier et de référencer un profil utilisateur."

---

# Cycle de vie du profil de l'utilisateur

> Cet article décrit le cycle de vie du profil de l'utilisateur dans Braze, et les différentes façons d’identifier et de référencer un profil utilisateur. Si vous cherchez à mieux comprendre votre cycle de vie client, regardez plutôt notre cours d'apprentissage Braze sur le [Mappage des cycles de vie utilisateur](https://learning.braze.com/mapping-customer-lifecycles).

Toutes les données persistantes associées à un utilisateur sont stockées sur un profil utilisateur.

Une fois qu’un profil utilisateur est créé, soit après que l’utilisateur est reconnu par le SDK ou créé via API, il existe un certain nombre d’identifiants pouvant être attribués à un profil pour identifier ou référencer cet utilisateur. 

Ces identifiants sont les suivants :

* `braze_id`
* `external_id`
* Nombre d’alias que vous choisissez de définir pour votre base d’utilisateurs.

## Profils d’utilisateurs anonymes

Initialement, lorsqu’un profil utilisateur est reconnu via le SDK, un profil utilisateur anonyme est créé avec un `braze_id`associé  (un identifiant utilisateur unique défini par Braze). Cet identifiant peut être utilisé pour supprimer des utilisateurs via l’API REST.

Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l’appareil de l’utilisateur.

## Profils d’utilisateurs identifiés

Dès qu’un utilisateur est reconnaissable dans votre application (en fournissant un type d’ID utilisateur ou d’adresse e-mail), nous vous suggérons d’[attribuer un ID_externe][23] au profil de cet utilisateur. L’objectif est de reconnaître le même utilisateur sur plusieurs appareils en utilisant un seul profil utilisateur.

Voici d’autres avantages des ID Utilisateur : 

- Offrir une expérience utilisateur cohérente sur les divers appareils et plates-formes (par ex., ne pas envoyer de notifications inutiles à la tablette Android d’un utilisateur alors qu’il accède tout le temps à l’application sur son iPhone).
- Améliorer la précision des analyses en s’assurant que les utilisateurs ne créent pas un profil utilisateur chaque fois qu’ils désinstallent et réinstallent, ou installent l’application sur un autre appareil.
- Permettre l’importation des données utilisateur provenant de sources en dehors de l’application via l’[API Utilisateur]({{site.baseurl}}/api/endpoints/user_data/) et cibler les utilisateurs avec des messages transactionnels utilisant via l’[API Messaging]({{site.baseurl}}/api/endpoints/messaging/).
- Rechercher des utilisateurs individuels avec nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) « Test » dans le segmenteur et sur la page [Recherche d’utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/).

{% alert warning %}
N’attribuez pas un `external_id` à un profil utilisateur avant de pouvoir l’identifier de façon unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez pas le remettre en utilisateur anonyme.
{% endalert %} 

La définition d’un `external_id` fusionnera toutes les données de profil utilisateur pertinentes du profil utilisateur anonyme avec les données du profil utilisateur identifié existantes, et elle supprimera de notre base de données les données restantes non pertinentes du profil précédemment anonyme. Cette méthode peut empêcher un utilisateur orphelin de recevoir une campagne qui a déjà été reçue ou ouverte par l’utilisateur identifié. Elle empêche aussi diverses erreurs si vous avez des doublons d’utilisateurs dans Braze. Ces utilisateurs orphelins ne sont pas pris en compte dans votre base utilisateurs et ils ne recevront pas de communications.

Dans la première instance d’attribution d’un `external_id` à un profil utilisateur inconnu, toutes les données de profil utilisateur existantes seront migrées vers le nouveau profil utilisateur.

{% alert warning %}
Un `external_id` ne peut pas être modifié une fois qu’il a été défini sur un profil utilisateur. Toute tentative de définir un autre `external_id` pendant la session d’un utilisateur créera un nouveau profil utilisateur avec le nouveau `external_id` associé. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %}

Pour plus d’informations sur la manière de définir un `external_id` sur un profil utilisateur voir notre documentation ([iOS][24], [Android][30], [Web][31]).

## Alias utilisateurs

Pour permettre aux utilisateurs de se référer à plusieurs autres identifiants plutôt qu’à l’`external_id` Braze uniquement, vous pouvez également définir des alias d’utilisateur sur un profil utilisateur. Tout alias défini pour un profil utilisateur sera une addition au `braze_id` ou `external_id` de l’utilisateur plutôt qu’un remplacement. Le nombre d’alias que vous pouvez définir sur un profil utilisateur est illimité.

Chaque alias se compose de deux parties : un libellé, qui définit la clé de l’alias, et un nom, qui définit la valeur. Chaque libellé doit avoir un nom d’alias unique dans la base utilisateur. Si vous tentez de mettre à jour un deuxième profil utilisateur avec une combinaison de libellés et de noms existants, le profil utilisateur ne sera pas mis à jour.

Contrairement à un `external_id`, un alias peut être mis à jour avec un nouveau nom pour un libellé donné une fois défini. Vous pouvez le faire via l’[endpoint Nouvel Alias Utilisateur][32] ou si vous transmettez un nouveau nom via le SDK. L’alias utilisateur sera alors visible lors de l’exportation des données de cet utilisateur.

![Deux profils utilisateur différents pour des utilisateurs distincts avec le même le libellé d’alias utilisateur, mais des valeurs d’alias différentes][29]

Les alias utilisateurs vous permettent également de tagger les utilisateurs anonymes avec un identifiant. Ces utilisateurs peuvent alors être exportés à l’aide de leurs alias ou référencés par l’API.

Si un profil utilisateur anonyme avec un alias est reconnu ultérieurement avec un `external_id`, il sera traité comme un profil utilisateur normal identifié, mais il conservera son alias existant et pourront toujours être référencés par cet alias.

Un alias utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID externe connu. Par exemple, un utilisateur peut avoir un ID Amplitude et un ID d’outil BI différent que vous souhaitez pouvoir référencer dans Braze.

Pour plus d’informations sur la manière de définir un alias utilisateur, consultez notre documentation pour votre plateforme ([iOS][1], [Android][2], [Web][3]).

![Organigramme du cycle de vie d’un profil utilisateur dans Braze. Lorsque changeUser() est appelé pour un utilisateur anonyme, l’utilisateur devient un utilisateur identifié et les données sont migrées vers son profil d’utilisateur identifié. L’utilisateur identifié a un ID Braze et un ID externe. À ce stade, si un deuxième utilisateur anonyme appelle la fonction changeUser(), les données anonymes de son utilisateur seront orphelines. Si l’utilisateur identifié a un alias ajouté à son profil utilisateur existant, aucune donnée n’est affectée, mais il deviendra un utilisateur identifié avec alias. Si un troisième utilisateur anonyme ayant le même le libellé d’alias que l’utilisateur identifié, mais un nom d’alias différent appelle la fonction changeUser(), les données existantes sont supprimées et seul le libellé d’alias sur le profil utilisateur identifié est maintenu.][26]

{% alert tip %}
Vous avez du mal à voir ce que ça peut donner pour le cycle de vie du profil de l'utilisateur de vos clients ? Consultez les [Meilleures pratiques]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) pour optimiser votre collecte de données utilisateur.
{% endalert %}

## Cas d’utilisation avancées

Vous pouvez définir un nouvel alias utilisateur pour les profils d’utilisateurs identifiés existants via notre SDK et notre API en utilisant le [nouvel endpoint d’alias utilisateur][27]. Cependant, les alias utilisateur ne peuvent pas être définis via l’API sur un profil utilisateur inconnu.

Si vous tentez de définir un `external_id`préexistant sur un profil utilisateur anonyme qui partage un nom d’alias correspondant, mais qui a des libellés différents, seule le libellé d’alias sur le profil utilisateur connu préexistant sera maintenu.

L’installation et la réinstallation d’une application entraîneront la génération d’un nouvel ID utilisateur anonyme pour cet utilisateur.

## Comment résoudre les problèmes avec les ID Braze

En plus de servir de mécanisme pour organiser les données utilisateur et les profils d’utilisateurs, toutes les `braze_id` peuvent être utilisés pour trouver et identifier les utilisateurs dans votre tableau de bord pour des tests. Pour trouver votre utilisateur dans le tableau de bord de Braze, consultez [Ajouter des utilisateurs de test][28].

{% alert important %}
Braze interdit ou bloque les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et cesse d’ingérer leurs événements SDK, car ces utilisateurs sont généralement le résultat d’une mauvaise intégration. Si vous constatez que cela s’est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[25]: {{site.baseurl}}/developer_guide/home/
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %}
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
