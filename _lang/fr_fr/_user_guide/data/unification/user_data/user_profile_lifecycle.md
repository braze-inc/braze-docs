---
nav_title: Cycle de vie du profil utilisateur
article_title: Cycle de vie du profil utilisateur
page_order: 2
page_type: reference
description: "Cet article de référence décrit le cycle de vie du profil utilisateur Braze, ainsi que les différentes façons dont un profil utilisateur peut être identifié et référencé."

---

# Cycle de vie du profil utilisateur

> Cet article décrit le cycle de vie du profil utilisateur de Braze et les différentes manières d'identifier et de référencer un profil utilisateur. Si vous cherchez à mieux comprendre le cycle de vie de vos clients, consultez plutôt notre cours d'apprentissage Braze sur [le mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles).

Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur. Après la création d'un profil utilisateur, soit par l'API, soit après la reconnaissance d'un utilisateur par le SDK, vous pouvez attribuer un certain nombre de paramètres à ce profil afin d'identifier et de référencer cet utilisateur. 

Ces paramètres sont les suivants

* `braze_id` (attribué par Braze)
* `external_id`
* `email`
* `phone`
* Un nombre quelconque d'alias d'utilisateurs personnalisés que vous définissez

## Profils utilisateurs anonymes

Tout utilisateur n'ayant pas de `external_id` désigné est appelé [utilisateur anonyme]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/). Par exemple, il peut s'agir d'utilisateurs qui ont visité votre site web mais ne se sont pas inscrits, ou d'utilisateurs qui ont téléchargé votre application mobile mais n'ont pas créé de profil.

Au départ, lorsqu'un utilisateur est reconnu par le SDK, un profil utilisateur anonyme est créé avec un `braze_id` associé : un identifiant unique qui est automatiquement attribué par Braze, qui ne peut pas être modifié et qui est spécifique à l'appareil. Cet identifiant peut être utilisé pour mettre à jour le profil utilisateur via l'[API]({{site.baseurl}}/api/endpoints/user_data/).

## Profils utilisateurs identifiés

Une fois qu'un utilisateur est reconnaissable dans votre appli (en fournissant une forme d'ID utilisateur ou d'adresse e-mail), nous suggérons d'attribuer un `external_id` au profil de cet utilisateur en utilisant la méthode `changeUser` [(web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Une adresse `external_id` vous permet d'identifier le même profil utilisateur sur plusieurs appareils.

L'utilisation d'un site `external_id` présente d'autres avantages : 

- Offrir une expérience sur l'application cohérente sur plusieurs appareils et plateformes (par exemple, ne pas envoyer de notifications d'utilisateur caduque sur la tablette Android d'un utilisateur alors qu'il est un utilisateur fidèle de l'application iPhone).
- Améliorez la précision de vos analyses/analytiques en confirmant que les utilisateurs ne créent pas un nouveau profil utilisateur chaque fois qu'ils désinstallent et réinstallent l'application ou qu'ils l'installent sur un autre appareil.
- Activez l'importation de données utilisateur à partir de sources extérieures à l'app à l'aide des [endpoints de données utilisateur]({{site.baseurl}}/api/endpoints/user_data/) et ciblez les utilisateurs avec des messages transactionnels à l'aide de nos [endpoints d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/)
- Recherchez des utilisateurs individuels à l'aide de nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) "Test" dans le segmentation, et sur la page d'accueil du site. [**Recherche d'utilisateurs**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) et sur la page Recherche d'utilisateurs.

### Considérations relatives aux ID externes

{% alert warning %}
N'attribuez pas de `external_id` à un profil utilisateur avant de pouvoir l'identifier de manière unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez plus le rendre anonyme.
<br><br>
Un site `external_id` peut être mis à jour en utilisant l'[endpoint`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). Cependant, toute tentative de définir un autre `external_id` pendant la session d'un utilisateur créera un nouveau profil utilisateur auquel sera associé le nouveau `external_id`. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %} 

#### Risque lié à l'utilisation d'un e-mail ou d'un e-mail haché comme ID externe

L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités dans l'ensemble de vos sources de données. Cependant, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.

- **Informations à deviner :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.

### Que se passe-t-il lorsque vous identifiez des utilisateurs anonymes ?

Deux cas de figure peuvent se présenter lorsque vous identifiez des utilisateurs anonymes :

1) **Un utilisateur anonyme devient un nouvel utilisateur identifié :** <br>Si le site `external_id` n'existe pas encore dans Braze, l'utilisateur anonyme devient un nouvel utilisateur identifié et conserve tous les attributs et l'historique de l'utilisateur anonyme. 

2) **Un utilisateur anonyme est identifié comme un utilisateur déjà existant :** <br>Si le site `external_id` existe déjà dans Braze, c'est que cet utilisateur a été précédemment identifié comme utilisateur dans le système d'une autre manière, par exemple via un autre appareil (comme une tablette) ou des données d'utilisateur importées. 

En d'autres termes, vous avez déjà un profil utilisateur pour cet utilisateur. Dans cette instance, Braze prend les mesures suivantes :
1. Orphelin de l'utilisateur anonyme
2. Fusionner les [champs spécifiques du profil utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) qui n'existent pas déjà sur le profil utilisateur identifié à partir du profil anonyme.
3. Supprimez le profil anonyme de votre base d'utilisateurs afin de ne pas gonfler le nombre d'utilisateurs.

Si l'utilisateur anonyme et l'utilisateur connu ont tous deux un prénom, le prénom de l'utilisateur connu est conservé. Si l'utilisateur connu a une valeur nulle et que l'utilisateur anonyme a une valeur, la valeur de l'utilisateur anonyme est fusionnée dans le profil de l'utilisateur connu si la valeur correspond à ces [champs spécifiques du profil de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

Pour savoir comment définir une `external_id` par rapport à un profil utilisateur, consultez notre documentation[(iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)).

## Alias de l'utilisateur

Pour désigner les utilisateurs par des identifiants autres que le `external_id` de Braze, définissez des alias d'utilisateur par rapport à un profil utilisateur. Tout alias d'un profil utilisateur s'ajoutera au `braze_id` ou au `external_id` de l'utilisateur et ne le remplacera pas. Il n'y a pas de limite au nombre d'aliases que vous pouvez associer à un profil utilisateur.

Chaque alias fonctionne comme une paire clé-valeur composée de deux parties : un `alias_label`, qui définit la clé de l'alias, et un `alias_name`, qui définit la valeur. Une adresse `alias_name` pour un label donné doit être unique pour l'ensemble de votre base d'utilisateurs (comme pour `external_id`). Si vous essayez de mettre à jour un deuxième profil utilisateur avec une combinaison d'étiquette et de nom préexistante, le profil utilisateur ne sera pas mis à jour.

### Mise à jour des alias utilisateurs

Un alias peut être mis à jour avec un nouveau nom pour un libellé donné après qu'il a été défini, soit en utilisant nos [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint), soit en transmettant un nouveau nom par l'intermédiaire du SDK. L'alias d'utilisateur sera alors visible lors de l'exportation des données de cet utilisateur.

Deux profils utilisateurs différents pour des utilisateurs distincts avec le même libellé d'alias utilisateur mais des noms d'alias différents.]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Taguer des utilisateurs anonymes

Les alias d'utilisateurs vous permettent également de taguer les utilisateurs anonymes avec un identifiant. Par exemple, si un utilisateur fournit son adresse e-mail à votre site de commerce électronique mais ne s'est pas encore inscrit, l'adresse e-mail peut être utilisée comme alias pour cet utilisateur anonyme. Ces utilisateurs peuvent ensuite être exportés à l'aide de leurs alias ou référencés par l'API.

### Comportement des aliases sur les profils utilisateurs anonymes

Si un profil utilisateur anonyme doté d'un alias est reconnu ultérieurement par une adresse `external_id`, il sera traité comme un profil utilisateur identifié normal, mais conservera son alias existant et pourra toujours être référencé par cet alias.

### Définition d'aliases sur des profils utilisateurs connus

Un alias utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID externe connu. Par exemple, un utilisateur peut avoir un ID d'outil d'aide à la décision (comme un ID d'Amplitude) que vous souhaitez référencer dans Braze.

Pour savoir comment définir un alias d'utilisateur, consultez notre documentation pour chaque plateforme[(iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)).

Organigramme du cycle de vie d'un profil utilisateur dans Braze. Lorsque changeUser() est appelé pour un utilisateur anonyme, celui-ci devient un utilisateur identifié et les données sont migrées vers son profil d'utilisateur identifié. L'utilisateur identifié dispose d'un ID Braze et d'un ID externe. À ce stade, si un deuxième utilisateur anonyme fait appel à changeUser(), les champs de données de l'utilisateur qui n'existent pas encore sur l'utilisateur identifié seront fusionnés. Si l'utilisateur identifié a un alias ajouté à son profil utilisateur existant, aucune donnée ne sera affectée mais il deviendra un utilisateur identifié avec alias. Si un troisième utilisateur anonyme ayant le même libellé d'alias que l'utilisateur identifié mais un nom d'alias différent est appelé changeUser(), tous les champs qui n'existent pas dans le profil de l'utilisateur identifié seront fusionnés et le libellé d'alias dans le profil de l'utilisateur identifié sera maintenu.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Vous avez du mal à imaginer ce que cela peut donner pour le cycle de vie du profil utilisateur de vos personnalisés ? Consultez la rubrique " [Meilleures pratiques]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/) " pour connaître les meilleures pratiques en matière de collecte de données sur les utilisateurs.
{% endalert %}

## Cas d'utilisation avancé

Vous pouvez définir un nouvel alias d'utilisateur pour des profils utilisateurs identifiés existants via notre SDK et notre API à l'aide des [endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint). Cependant, les aliases de l'utilisateur ne peuvent pas être définis via l'API pour un profil utilisateur inconnu existant.

Les aliasing de l'utilisateur sont également fusionnés au cours du processus. Toutefois, si l'utilisateur à rendre orphelin et l'utilisateur cible ont tous deux un alias portant le même libellé, seul l'alias de l'utilisateur cible est conservé.

La désinstallation et la réinstallation d'une application génèrent une nouvelle adresse `braze_id` anonyme pour cet utilisateur.

### Résolution des problèmes avec les ID d'utilisateurs

Tous les ID peuvent être utilisés pour trouver et identifier des utilisateurs dans votre tableau de bord à des fins de test. Pour trouver votre utilisateur dans le tableau de bord de Braze, reportez-vous à la section [Ajout d'utilisateurs test]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

{% alert important %}
Braze interdira ou bloquera les utilisateurs ayant plus de 5 000 000 de sessions ("utilisateurs fictifs") et n'ingérera plus leurs événements SDK, car ces utilisateurs sont généralement le résultat d'une mauvaise intégration. Si vous constatez que cela est arrivé à un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}