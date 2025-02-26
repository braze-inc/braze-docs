---
nav_title: "Cycle de vie du profil de l'utilisateur"
article_title: "Cycle de vie du profil de l'utilisateur"
page_order: 2
page_type: reference
description: "Cet article de référence décrit le cycle de vie du profil de l'utilisateur de Braze et les différentes façons d’identifier et de référencer un profil utilisateur."

---

# Cycle de vie du profil de l'utilisateur

> Cet article décrit le cycle de vie du profil utilisateur de Braze et les différentes manières d'identifier et de référencer un profil utilisateur. Si vous cherchez à mieux comprendre le cycle de vie de vos clients, consultez plutôt notre cours d'apprentissage Braze sur [le mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

Toutes les données persistantes associées à un utilisateur sont stockées dans leur profil utilisateur. Après la création d'un profil utilisateur, soit par l'API, soit après la reconnaissance d'un utilisateur par le SDK, vous pouvez attribuer un certain nombre de paramètres à ce profil afin d'identifier et de référencer cet utilisateur. 

Ces paramètres comprennent :

* `braze_id`
* `external_id`
* Le nombre d’alias d’utilisateur personnalisés que vous définissez

## Profils d’utilisateurs anonymes

Tout utilisateur sans `external_id` désigné est appelé un utilisateur anonyme. Par exemple, il peut s'agir d'utilisateurs qui ont visité votre site web mais ne se sont pas inscrits, ou d'utilisateurs qui ont téléchargé votre application mobile mais n'ont pas créé de profil.

Au départ, lorsqu'un utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec un `braze_id` associé : un identifiant unique qui est automatiquement attribué par Braze, ne peut pas être modifié et est spécifique à l'appareil. Cet identifiant peut être utilisé pour mettre à jour le profil utilisateur via l'[API]({{site.baseurl}}/api/endpoints/user_data/).

## Profils d’utilisateurs identifiés

Une fois qu'un utilisateur est reconnaissable dans votre appli (en fournissant une forme d'ID utilisateur ou d'adresse e-mail), nous suggérons d'attribuer un `external_id` au profil de cet utilisateur en utilisant la méthode `changeUser` [(web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69), [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)). Un `external_id` vous permet d’identifier le même profil utilisateur sur plusieurs appareils. 

Les autres avantages de l’utilisation d’un `external_id` sont les suivants : 

- Offrir une expérience sur l'application cohérente sur plusieurs appareils et plateformes (par exemple, ne pas envoyer de notifications d'utilisateur caduque sur la tablette Android d'un utilisateur alors qu'il est un utilisateur fidèle de l'application iPhone).
- Améliorez la précision de vos analyses/analytiques en confirmant que les utilisateurs ne créent pas un nouveau profil utilisateur chaque fois qu'ils désinstallent et réinstallent l'application ou qu'ils l'installent sur un autre appareil.
- Activez l'importation de données utilisateur à partir de sources extérieures à l'app à l'aide des [endpoints de données utilisateur]({{site.baseurl}}/api/endpoints/user_data/) et ciblez les utilisateurs avec des messages transactionnels à l'aide de nos [endpoints d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/)
- Recherchez des utilisateurs individuels à l'aide de nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) "Test" dans le segmentation, et sur la page d'accueil du site. [**Recherche d'utilisateurs**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) et sur la page Recherche d'utilisateurs.

{% alert warning %}
N'attribuez pas de `external_id` à un profil utilisateur avant de pouvoir l'identifier de manière unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez plus le rendre anonyme.
<br><br>
En outre, un site `external_id` est immuable une fois qu'il a été associé à un profil utilisateur. Toute tentative de définir un autre `external_id` pendant la session d’un utilisateur créera un nouveau profil utilisateur avec le nouveau `external_id` associé. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %} 

### Que se passe-t-il lorsque vous identifiez des utilisateurs anonymes ?

Deux cas de figure peuvent se présenter lorsque vous identifiez des utilisateurs anonymes :

1) **Un utilisateur anonyme devient un nouvel utilisateur identifié :** <br>Si le site `external_id` n'existe pas encore dans Braze, l'utilisateur anonyme devient un nouvel utilisateur identifié et conserve tous les attributs et l'historique de l'utilisateur anonyme. 

2) **Un utilisateur anonyme est identifié comme un utilisateur déjà existant :** <br>Si le site `external_id` existe déjà dans Braze, c'est que cet utilisateur a été précédemment identifié comme utilisateur dans le système d'une autre manière, par exemple via un autre appareil (comme une tablette) ou des données d'utilisateur importées. 

En d'autres termes, vous avez déjà un profil utilisateur pour cet utilisateur. Dans cette instance, Braze procédera comme suit :
1. Orphelin de l'utilisateur anonyme
2. Fusionner les [champs spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) qui n'existent pas déjà sur le profil utilisateur identifié à partir du profil anonyme.
3. Supprimez le profil anonyme de votre base d'utilisateurs afin de ne pas gonfler le nombre d'utilisateurs.

Si l'utilisateur anonyme et l'utilisateur connu ont tous deux un prénom, le prénom de l'utilisateur connu est conservé. Si l'utilisateur connu a une valeur nulle et que l'utilisateur anonyme a une valeur, la valeur de l'utilisateur anonyme est fusionnée dans le profil de l'utilisateur connu si la valeur correspond à ces [champs spécifiques du profil de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

Pour savoir comment définir un `external_id` par rapport à un profil utilisateur, consultez notre documentation[(iOS][24], [Android][30], [Web][31]).

## Alias utilisateurs

Pour désigner les utilisateurs par des identifiants autres que le `external_id` de Braze, définissez des alias d'utilisateur par rapport à un profil utilisateur. Tout alias défini pour un profil utilisateur sera une addition au `braze_id` ou `external_id` de l’utilisateur plutôt qu’un remplacement. Le nombre d’alias que vous pouvez définir sur un profil utilisateur est illimité.

Chaque alias fonctionne comme une paire clé-valeur composée de deux parties : un `alias_label`, qui définit la clé de l'alias, et un `alias_name`, qui définit la valeur. Une adresse `alias_name` pour un label donné doit être unique pour l'ensemble de votre base d'utilisateurs (comme pour `external_id`). Si vous essayez de mettre à jour un deuxième profil utilisateur avec une combinaison d'étiquette et de nom préexistante, le profil utilisateur ne sera pas mis à jour.

### Mise à jour des alias utilisateurs

Contrairement à `external_id`, un alias peut être mis à jour avec un nouveau nom pour un libellé d'alias donné une fois qu'il a été défini, soit en utilisant nos [User Data endpoints][32] ], soit en transmettant un nouveau nom par l'intermédiaire du SDK. L’alias utilisateur sera alors visible lors de l’exportation des données de cet utilisateur.

![Deux profils utilisateurs différents pour des utilisateurs distincts avec le même libellé d'alias utilisateur mais des noms d'alias différents.][29]

### Taguer des utilisateurs anonymes

Les alias utilisateurs vous permettent également de tagger les utilisateurs anonymes avec un identifiant. Par exemple, si un utilisateur fournit son adresse e-mail à votre site de commerce électronique mais ne s'est pas encore inscrit, l'adresse e-mail peut être utilisée comme alias pour cet utilisateur anonyme. Ces utilisateurs peuvent alors être exportés à l’aide de leurs alias ou référencés par l’API.

### Comportement des aliases sur les profils utilisateurs anonymes

Si un profil utilisateur anonyme avec un alias est reconnu ultérieurement avec un `external_id`, il sera traité comme un profil utilisateur normal identifié, mais il conservera son alias existant et pourra toujours être référencé par cet alias.

### Définition d'aliases sur des profils utilisateurs connus

Un alias utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID externe connu. Par exemple, un utilisateur peut avoir un ID d’outil d’aide à la décision (comme un ID Amplitude) que vous souhaitez pouvoir référencer dans Braze.

Pour savoir comment définir un alias d'utilisateur, consultez notre documentation pour chaque plateforme[(iOS][1], [Android][2], [Web][3]).

![Organigramme du cycle de vie d’un profil utilisateur dans Braze. Lorsque changeUser() est appelé pour un utilisateur anonyme, l’utilisateur devient un utilisateur identifié et les données sont migrées vers son profil d’utilisateur identifié. L’utilisateur identifié a un ID Braze et un ID externe. À ce stade, si un deuxième utilisateur anonyme fait appel à changeUser(), les champs de données de l'utilisateur qui n'existent pas encore sur l'utilisateur identifié seront fusionnés. Si l’utilisateur identifié a un alias ajouté à son profil utilisateur existant, aucune donnée n’est affectée, mais il deviendra un utilisateur identifié avec alias. Si un troisième utilisateur anonyme ayant le même libellé d'alias que l'utilisateur identifié mais un nom d'alias différent est appelé changeUser(), tous les champs qui n'existent pas dans le profil de l'utilisateur identifié seront fusionnés et le libellé d'alias dans le profil de l'utilisateur identifié sera maintenu.][26]

{% alert tip %}
Vous avez du mal à voir ce que ça peut donner pour le cycle de vie du profil de l'utilisateur de vos clients ? Consultez la rubrique " [Meilleures pratiques]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) " pour connaître les meilleures pratiques en matière de collecte de données sur les utilisateurs.
{% endalert %}

## Cas d'utilisation avancé

Vous pouvez définir un nouvel alias d'utilisateur pour des profils utilisateurs identifiés existants via notre SDK et notre API à l'aide des [endpoints de données utilisateur][27]. Cependant, les aliases de l'utilisateur ne peuvent pas être définis via l'API pour un profil utilisateur inconnu existant.

Les aliasing de l'utilisateur sont également fusionnés au cours du processus. Toutefois, si l'utilisateur à rendre orphelin et l'utilisateur cible ont tous deux un alias portant le même libellé, seul l'alias de l'utilisateur cible est conservé.

La désinstallation et la réinstallation d'une application génèrent une nouvelle adresse `braze_id` anonyme pour cet utilisateur.

### Résolution des problèmes avec les ID d'utilisateurs

Tous les identifiants utilisateur peuvent être utilisés pour trouver et identifier les utilisateurs dans votre tableau de bord pour les tests. Pour trouver votre utilisateur dans le tableau de bord de Braze, consultez [Ajouter des utilisateurs test][28].

{% alert important %}
Braze interdira ou bloquera les utilisateurs ayant plus de 5 000 000 de sessions ("utilisateurs fictifs") et n'ingérera plus leurs événements SDK, car ces utilisateurs sont généralement le résultat d'une mauvaise intégration. Si vous constatez que cela s’est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
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
