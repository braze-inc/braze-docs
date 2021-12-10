---
nav_title: Cycle de vie du profil utilisateur
article_title: Cycle de vie du profil utilisateur
page_order: 2
page_type: Référence
description: "Cet article de référence décrit le cycle de vie du profil utilisateur au Brésil, et les différentes façons d'identifier et de référencer un profil utilisateur."
---

# Cycle de vie du profil utilisateur

> Cet article décrit le cycle de vie du profil utilisateur au Brésil, et les différentes façons d'identifier et de référencer un profil utilisateur. Si vous souhaitez mieux comprendre le cycle de vie de votre client, consultez notre cours LAB sur [Mapping User Lifecycles](https://lab.braze.com/mapping-customer-lifecycles) à la place.

Toutes les données persistantes associées à un utilisateur seront stockées dans un profil utilisateur.

Une fois qu'un profil utilisateur est créé, soit après qu'un utilisateur soit reconnu par le SDK ou créé par API, il y a un certain nombre d'identifiants qui peuvent être assignés à un profil pour identifier ou référencer cet utilisateur.

Ces identifiants sont les suivants :

* `braze_id`
* `id externe`
* N'importe quel nombre d'alias que vous choisissez de définir pour votre base d'utilisateurs.

## Profils utilisateurs anonymes

Initialement, lorsqu'un profil utilisateur est reconnu via le SDK, un profil utilisateur anonyme est créé avec un `braze_id`associé : un identifiant utilisateur unique défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l'API REST.

Le `braze_id` est automatiquement assigné par Braze, ne peut pas être édité, et est spécifique à l'appareil.

## Profils utilisateur identifiés

Une fois qu'un utilisateur est reconnaissable dans votre application (en fournissant une forme d'identifiant utilisateur ou d'adresse e-mail) nous suggérons [d'assigner un external_id][23] au profil de cet utilisateur. Le but est de reconnaître le même utilisateur à travers plusieurs périphériques à un seul profil d'utilisateur.

Parmi les avantages supplémentaires des identifiants d’utilisateur figurent les suivants :

- Fournir une expérience utilisateur cohérente sur plusieurs périphériques et plateformes (par ex. ne pas envoyer de notifications utilisateur caduc à la tablette Android d'un utilisateur qui est un utilisateur fidèle de l'application sur l'iPhone).
- Améliorez la précision de vos analyses en veillant à ce que les utilisateurs ne créent pas de nouveau profil utilisateur chaque fois qu'ils désinstallent et réinstallent, ou installez l'application sur un autre appareil.
- Activer l'importation des données utilisateur depuis des sources en dehors de l'application en utilisant notre [API utilisateur]({{site.baseurl}}/api/endpoints/user_data/), et cibler les utilisateurs avec des messages transactionnels en utilisant notre [API de messagerie]({{site.baseurl}}/api/endpoints/messaging/).
- Recherchez des utilisateurs individuels en utilisant notre [« Tester »]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) dans le segmenteur, et sur la page [Recherche d'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/).

{% alert warning %}
Ne pas assigner un `external_id` à un profil utilisateur avant de pouvoir l'identifier de manière unique. Une fois que vous avez identifié un utilisateur, vous ne pouvez pas revenir à l'anonymat.
{% endalert %}

Définir un `external_id` fusionnera toutes les données de profil utilisateur pertinentes du profil utilisateur anonyme avec les données de profil utilisateur identifiées existantes et supprimera les données restantes, parties non pertinentes des données de profil précédemment anonymes de notre base de données. Cette méthode peut empêcher un utilisateur orphelin de recevoir une campagne qui a déjà été reçue ou ouverte par votre utilisateur identifié, ou empêcher diverses erreurs qui peuvent se produire lorsqu'il y a des doublons de vos utilisateurs au Brésil. Ces utilisateurs orphelins ne sont pas considérés dans votre nombre d'utilisateurs et ne seront pas envoyés.

Sur la première instance d'assignation d'un `external_id` à un profil utilisateur inconnu, toutes les données de profil utilisateur existantes seront migrées vers le nouveau profil utilisateur.

{% alert warning %}
Un `external_id` est non modifiable une fois qu'il a été réglé sur un profil utilisateur. Toute tentative de définir un `external_id` différent pendant la session d'un utilisateur créera un nouveau profil utilisateur avec le nouveau `external_id` qui lui est associé. Aucune donnée ne sera transmise entre les deux profils.
{% endalert %}

Pour plus d'informations sur la façon de définir un `external_id` par rapport à un profil d'utilisateur, veuillez consulter notre documentation ([iOS][24], [Android][30], [Web][31]).

## Alias de l'utilisateur

Pour permettre aux utilisateurs de se référer à plusieurs autres identifiants plutôt que seulement le `external_id de Braze`, vous pouvez également définir des alias utilisateur par rapport à un profil utilisateur. N'importe quel alias défini contre un profil utilisateur agira en plus du `braze_id` ou `external_id` de l'utilisateur plutôt que de le remplacer. Il n'y a pas de limite au nombre d'alias que vous pouvez définir avec un profil utilisateur.

Chaque alias se compose de deux parties : une étiquette, qui définit la clé de l'alias et un nom, qui définit la valeur. Un nom d'alias pour toute étiquette unique doit être unique dans la base d'utilisateurs. Si vous essayez de mettre à jour un second profil utilisateur avec une combinaison préexistante de libellé et de nom, le profil de l'utilisateur ne sera pas mis à jour.

Contrairement à un `external_id`, un alias peut être mis à jour avec un nouveau nom pour une étiquette donnée une fois définie. Vous pouvez le faire soit via le [nouveau point de terminaison d'alias d'utilisateur][32], soit si vous passez un nouveau nom via le SDK. L'alias de l'utilisateur sera alors visible lors de l'exportation des données de cet utilisateur.

!\[Diagramme de Label Alias\]\[29\]

Les alias d'utilisateur vous permettent également de taguer des utilisateurs anonymes avec un identifiant. Ces utilisateurs peuvent ensuite être exportés en utilisant leurs alias ou référencés par l'API.

Si un profil utilisateur anonyme avec un alias est plus tard reconnu avec un `external_id`, ils seront traités comme un profil utilisateur normal, mais conserveront leur alias existant et pourront toujours être référencés par cet alias.

Un alias d'utilisateur peut également être défini sur un profil utilisateur connu pour référencer un utilisateur connu par un autre ID connu externe. Par exemple, un utilisateur peut avoir un ID d'Amplitude et un ID d'outil de BI différent que vous souhaitez référencer au Brésil.

Pour plus d'informations sur la façon de définir un alias d'utilisateur, veuillez consulter notre documentation pour chaque plateforme ([iOS][1], [Android][2], [Web][3]).

!\[Lifecycle du profil utilisateur\]\[26\]

## Informations avancées sur le cas d'utilisation

Vous pouvez définir un nouvel alias utilisateur pour les profils d'utilisateurs identifiés existants via notre SDK et notre API en utilisant le [nouvel alias utilisateur endpoint][27]. Cependant, les alias d'utilisateurs ne peuvent pas être définis via l'API sur un profil utilisateur inconnu.

Si vous essayez de définir un `external_id préexistant` sur un profil utilisateur anonyme qui partage un nom d'alias correspondant, mais ont des étiquettes différentes, seul le libellé de l'alias sur le profil utilisateur préexistant sera maintenu.

Désinstaller et réinstaller une application provoquera la génération d'un nouvel identifiant d'utilisateur anonyme pour cet utilisateur.

## Comment résoudre les problèmes avec les identifiants de Braze

En plus d'agir en tant que mécanisme pour organiser les données utilisateur et les profils d'utilisateurs de référence, tous les `braze_id`peuvent être utilisés pour trouver et identifier les utilisateurs dans votre tableau de bord pour les tests. Pour trouver votre utilisateur dans le tableau de bord Braze, reportez-vous à [Ajouter des utilisateurs de test][28].

{% alert important %}
Braze va bannir ou bloquer les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et n'ingérera plus leurs événements SDK car ces utilisateurs sont généralement le résultat d'une désintégration. Si vous trouvez que cela est arrivé à un utilisateur légitime, veuillez contacter votre responsable de compte Braze.
{% endalert %}
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %} [29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
