---
nav_title: Cycle de vie du profil de l'utilisateur
article_title: Cycle de vie du profil de l'utilisateur
page_order: 2
page_type: reference
description: "Cet article de référence décrit le cycle de vie du profil de l'utilisateur de Braze et les différentes façons d’identifier et de référencer un profil utilisateur."

---

# Cycle de vie du profil de l'utilisateur

> Cet article décrit le cycle de vie du profil de l'utilisateur dans Braze, et les différentes façons d’identifier et de référencer un profil utilisateur. Si vous cherchez à mieux comprendre votre cycle de vie client, regardez plutôt notre cours d'apprentissage Braze sur le [Mappage des cycles de vie utilisateur](https://learning.braze.com/mapping-customer-lifecycles).

Toutes les données persistantes associées à un utilisateur sont stockées dans leur profil utilisateur.

Une fois qu’un profil utilisateur est créé, soit après que l’utilisateur est reconnu par le SDK ou créé via l’API, il existe un certain nombre de paramètres pouvant être attribués à ce profil pour identifier et référencer cet utilisateur. 

Ces paramètres comprennent :

* `braze_id`
* `external_id`
* Le nombre d’alias d’utilisateur personnalisés que vous définissez

## Profils d’utilisateurs anonymes

Tout utilisateur sans `external_id` désigné est appelé un utilisateur anonyme. Il peut, par exemple, s’agir d’utilisateurs qui ont visité votre site Web, mais qui ne se sont pas inscrits ou ont téléchargé votre application mobile, mais qui n’ont pas créé de profil.

Initialement, lorsqu’un utilisateur est reconnu via le SDK, un profil utilisateur anonyme est créé avec un `braze_id`associé (un identifiant unique défini par Braze). Cet identifiant peut être utilisé pour mettre à jour le profil utilisateur via l’[API]({{site.baseurl}}/api/endpoints/user_data/).

Le `braze_id` est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l’appareil de l’utilisateur.

## Profils d’utilisateurs identifiés

Dès qu’un utilisateur est reconnaissable dans votre application (en fournissant un type d’ID utilisateur ou d’adresse e-mail), nous vous suggérons d’attribuer un `external_id` à ce profil utilisateur en utilisant la méthode `changeUser` ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69), [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)). Un `external_id` vous permet d’identifier le même profil utilisateur sur plusieurs appareils. 

Les autres avantages de l’utilisation d’un `external_id` sont les suivants : 

- Offrir une expérience utilisateur cohérente sur les divers appareils et plates-formes (par ex., ne pas envoyer de notifications inutiles à la tablette Android d’un utilisateur alors qu’il accède tout le temps à l’application sur son iPhone).
- Améliorer la précision des analyses en s’assurant que les utilisateurs ne créent pas un profil utilisateur chaque fois qu’ils désinstallent et réinstallent, ou installent l’application sur un autre appareil.
- Permettre l’importation des données utilisateur provenant de sources en dehors de l’application via les [données d’endpoint de l’utilisateur]({{site.baseurl}}/api/endpoints/user_data/) et cibler les utilisateurs avec des messages transactionnels utilisant via l’[endpoint d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/).
- Rechercher des utilisateurs individuels avec nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) de « Test » dans le segmenteur et sur la page [User Search (Recherche d’utilisateur)]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/).

{% alert warning %}
N’attribuez pas un `external_id` à un profil utilisateur avant de pouvoir l’identifier de façon unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez pas le remettre en utilisateur anonyme.
<br><br>
De plus, un `external_id` ne peut pas être modifié une fois qu’il a été défini sur un profil utilisateur. Toute tentative de définir un autre `external_id` pendant la session d’un utilisateur créera un nouveau profil utilisateur avec le nouveau `external_id` associé. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %} 

Deux scénarios se produisent lorsque vous identifiez des utilisateurs anonymes :

1) **Un utilisateur anonyme devient un nouvel utilisateur identifié :** Si le `external_id` n’existe pas encore sur la plateforme de Braze, l’utilisateur anonyme devient un nouvel utilisateur identifié et conserve les mêmes attributs et l’historique de l’utilisateur anonyme. 

2) **Un utilisateur anonyme est identifié comme un utilisateur déjà existant :** Si le `external_id` existe déjà sur la plateforme de Braze, cet utilisateur a été identifié précédemment comme utilisateur dans le système d’une autre manière, par exemple, via un autre appareil (comme sur une tablette) ou via des données utilisateur importées. En tant que tel, vous avez déjà un profil utilisateur pour cet utilisateur. Dans ce cas, Braze rend orphelin l’utilisateur anonyme, en le supprimant de votre base d’utilisateurs afin que nous ne gonflions pas incorrectement le nombre d’utilisateurs. Les analyses de campagne/Canvas et les informations sur les appareils sont fusionnées à partir du profil anonyme, mais les attributs et les événements ne seront pas fusionnés et doivent être traités manuellement.

Pour plus d’informations sur la manière de définir un `external_id` sur un profil utilisateur voir notre documentation ([iOS][24], [Android][30], [Web][31]).

## Alias utilisateurs

Pour vous référer aux utilisateurs par d’autres identifiants plutôt que par l’`external_id` Braze uniquement, définissez des alias d’utilisateur sur un profil utilisateur. Tout alias défini pour un profil utilisateur sera une addition au `braze_id` ou `external_id` de l’utilisateur plutôt qu’un remplacement. Le nombre d’alias que vous pouvez définir sur un profil utilisateur est illimité.

Chaque alias se compose de deux parties : un libellé, qui définit la clé de l’alias, et un nom, qui définit la valeur. Chaque libellé doit avoir un nom d’alias unique dans la base utilisateur. Si vous tentez de mettre à jour un deuxième profil utilisateur avec une combinaison de libellés et de noms existants, le profil utilisateur ne sera pas mis à jour.

Contrairement à un `external_id`, un alias peut être mis à jour avec un nouveau nom pour une étiquette donnée une fois défini via [l’endpoint des données utilisateur][32] ou en transmettant un nouveau nom via le SDK. L’alias utilisateur sera alors visible lors de l’exportation des données de cet utilisateur.

![Deux profils utilisateur différents pour les utilisateurs distincts avec le même le libellé d’alias utilisateur, mais les valeurs d’alias différentes][29]

Les alias utilisateurs vous permettent également de tagger les utilisateurs anonymes avec un identifiant. Par exemple, si un utilisateur fournit son adresse e-mail à votre site d’e-commerce, mais ne s’est pas encore inscrit, l’adresse e-mail peut être utilisée comme alias pour cet utilisateur anonyme. Ces utilisateurs peuvent alors être exportés à l’aide de leurs alias ou référencés par l’API.

Si un profil utilisateur anonyme avec un alias est reconnu ultérieurement avec un `external_id`, il sera traité comme un profil utilisateur normal identifié, mais il conservera son alias existant et pourra toujours être référencé par cet alias.

Un alias utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID externe connu. Par exemple, un utilisateur peut avoir un ID d’outil d’aide à la décision (comme un ID Amplitude) que vous souhaitez pouvoir référencer dans Braze.

Pour plus d’informations sur la manière de définir un alias utilisateur, consultez notre documentation pour votre plateforme ([iOS][1], [Android][2], [Web][3]).

![Organigramme du cycle de vie d’un profil utilisateur dans Braze. Lorsque changeUser() est appelé pour un utilisateur anonyme, l’utilisateur devient un utilisateur identifié et les données sont migrées vers son profil d’utilisateur identifié. L’utilisateur identifié a un ID Braze et un ID externe. À ce stade, si un deuxième utilisateur anonyme appelle la fonction changeUser(), les données anonymes de son utilisateur seront orphelines. Si l’utilisateur identifié a un alias ajouté à son profil utilisateur existant, aucune donnée n’est affectée, mais il deviendra un utilisateur identifié avec alias. Si un troisième utilisateur anonyme ayant le même le libellé d’alias que l’utilisateur identifié, mais un nom d’alias différent appelle la fonction changeUser(), les données existantes sont supprimées et seul le libellé d’alias sur le profil utilisateur identifié est maintenu.][26]

{% alert tip %}
Vous avez du mal à voir ce que ça peut donner pour le cycle de vie du profil de l'utilisateur de vos clients ? Consultez les [Meilleures pratiques]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) pour optimiser votre collecte de données utilisateur.
{% endalert %}

## Cas d’utilisation avancées

Vous pouvez définir un nouvel alias utilisateur pour les profils d’utilisateurs identifiés existants via notre SDK et notre API en utilisant [l’endpoint d’alias utilisateur][27]. Cependant, les alias utilisateur ne peuvent pas être définis via l’API sur un profil utilisateur inconnu.

Si vous tentez de définir un `external_id` préexistant sur un profil utilisateur anonyme qui partage un nom d’alias correspondant, mais qui a des libellés différents, seul le libellé d’alias sur le profil utilisateur connu préexistant sera maintenu.

L’installation et la réinstallation d’une application entraîneront la génération d’un nouvel `braze_id` utilisateur anonyme pour cet utilisateur.

### Comment résoudre les problèmes avec les ID utilisateur

Tous les identifiants utilisateur peuvent être utilisés pour trouver et identifier les utilisateurs dans votre tableau de bord pour les tests. Pour trouver votre utilisateur dans le tableau de bord de Braze, consultez [Ajouter des utilisateurs de test][28].

{% alert important %}
Braze interdit ou bloque les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et cesse d’ingérer leurs événements SDK, car ces utilisateurs sont généralement le résultat d’une mauvaise intégration. Si vous constatez que cela s’est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[25]: {{site.baseurl}}/developer_guide/home/
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %}
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
