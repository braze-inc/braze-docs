---
nav_title: Aperçu
article_title: Aperçu de l'API
page_order: 0
description: "Cet article de référence couvre les bases de l'API, y compris ce qu'est une API REST, la terminologie, un bref aperçu des clés de l'API, et les limites de l'API."
page_type: Référence
---

# Aperçu de l'API

> Braze fournit une API REST haute performance pour vous permettre de suivre les utilisateurs, d'envoyer des messages, d'exporter des données, et plus encore. Cet article de référence couvre ce qu'est une API REST, la terminologie, un bref aperçu des clés de l'API, et des limites de l'API.

## Qu'est-ce qu'une API REST?

Une API REST est un moyen de transférer des informations par programme sur le Web en utilisant un schéma prédéfini. Braze a créé de nombreux terminaux différents qui effectuent diverses actions et/ou retournent différentes données.

{% alert note %}
Les clients qui utilisent la base de données européenne de Braze doivent utiliser le point de terminaison `https://rest.fra-01.braze.eu/`. Ce point de terminaison sera utilisé lors de la configuration des SDK Braze [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#compile-time-endpoint-configuration-recommended), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml)et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).
{% endalert %}

## Définitions de l'API

Voici une terminologie que vous pouvez voir dans la documentation de Braze REST API et ce que cela signifie.

### Points de terminaison

Braze gère un certain nombre d'instances différentes pour notre tableau de bord et nos terminaux REST. Lorsque votre compte est provisionné, vous vous connecterez à l'une des URL correspondantes ci-dessous. Utilisez le bon point de terminaison REST en fonction de l'instance à laquelle vous êtes fournis. Si vous n'êtes pas sûr, ouvrir un [ticket de support][support] ou utiliser le tableau ci-dessous pour correspondre à l'URL du tableau de bord que vous utilisez au bon point de terminaison REST.

{% alert important %}
Lorsque vous utilisez des points de terminaison pour les appels API, utilisez le "REST Endpoint" situé ci-dessous.

Pour l'intégration au SDK, utilisez le ["SDK Endpoint"]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), pas le "REST Endpoint".
{% endalert %}

| Instance | URL                              | Point de terminaison REST       | Point de terminaison SDK |
| -------- | -------------------------------- | ------------------------------- | ------------------------ |
| US-01    | `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com`   |
| US-02    | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com`   |
| US-03    | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com`   |
| US-04    | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com`   |
| US-05    | `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com`   |
| US-06    | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com`   |
| US-08    | `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com`   |
| EU-01    | `https://dashboard-01.braze.eu`  | `https://rest.fra-01.braze.eu`  | `sdk.fra-01.braze.eu`    |
| EU-02    | `https://dashboard-02.braze.eu`  | `https://rest.fra-02.braze.eu`  | `sdk.fra-02.braze.eu`    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Explication secrète de l'entreprise

Le `company_secret` a été précédemment inclus avec toutes les requêtes API mais a été obsolète en octobre 2014. Ce champ sera ignoré pour toutes les requêtes futures de l'API afin d'assurer la compatibilité ascendante.

### Groupe d'applications clés API REST

{% alert note %}
Pour une plongée plus profonde sur les différents types de clés API ici à Braze, Consultez nos articles de référence dédiés aux <a href="{{site.baseurl}}/api/api_key/">clés API</a> et <a href="{{site.baseurl}}/api/identifier_types/">API Identifier Types</a>.

{% endalert %}

La `api_key` incluse dans chaque requête agit comme une clé d'authentification qui permet à votre code serveur d'utiliser nos API REST. Au sein de votre entreprise, chaque groupe d'applications aura un ensemble unique de clés d'API REST. Ils peuvent être trouvés dans le tableau de bord de Braze en naviguant dans la section Console développeur pour chaque groupe d'applications. Pour utiliser l'API REST pour un groupe d'applications donné, vous devez créer des clés et leur donner des autorisations.

!\[Clefs de l'API REST\]\[27\]

#### Autorisations de la clé API

Les clés API sont utilisées pour authentifier un appel API. Lorsque vous créez une nouvelle clé d'API REST, vous devez lui donner accès à des points de terminaison spécifiques. En assignant des permissions spécifiques à une clé API, vous pouvez limiter exactement quels appels une clé API peut s'authentifier.

Une bonne pratique de sécurité est d'assigner un utilisateur seulement autant d'accès que nécessaire pour terminer son travail : ce principe peut également être appliqué aux clés API en assignant des permissions à chaque clé. Ces autorisations vous donnent une meilleure sécurité et un meilleur contrôle sur les différentes zones de votre compte.

!\[Autorisations de clés de l'API REST\]\[25\]

{% alert warning %}
Étant donné que les clés d'API REST permettent d'accéder à des terminaux d'API REST potentiellement sensibles, assurez-vous qu'elles sont stockées et utilisées en toute sécurité. Par exemple, n'utilisez pas cette clé pour passer des appels AJAX à partir de votre site Web ou pour l'exposer d'une autre manière publique.
{% endalert %}

Si une clé est exposée accidentellement, elle peut être supprimée de la [console développeur][8]. Pour obtenir de l'aide sur ce processus, veuillez ouvrir un [ticket de support][support].

#### Liste des autorisations IP de l'API

Pour plus de sécurité, vous pouvez spécifier une liste d'adresses IP et de sous-réseaux qui sont autorisés à faire des requêtes d'API REST pour une clé REST donnée. On l'appelle liste d'autorisation, ou liste blanche. Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les à la section **Liste blanche des IPs** lors de la création d'une nouvelle clé API REST :

!\[Liste blanche IP de l'API\]\[26\]

Si vous n'en spécifiez aucune, les requêtes peuvent être envoyées depuis n'importe quelle adresse IP.

{% alert tip %}
Faire un webhook Brase-to-Braze et utiliser le droit d'inscription? Consultez notre liste d'adresses IP [pour la whitelist]({{site.baseurl}}/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

#### Création et gestion des clés API REST

!\[Créer une nouvelle clé API\]\[28\]{: style="max-width:20%;float:right;margin-left:15px;"}

Pour créer une nouvelle clé d'API REST, visitez la [console de développement][8] sur votre tableau de bord Braze. Cette page affiche vos clés API existantes. Pour créer une nouvelle clé, cliquez sur **Créer une nouvelle clé API**.

Vous pouvez ensuite faire ce qui suit :

- Donnez en un coup d'œil à votre nouvelle clé un nom pour l'identification
- Sélectionnez les permissions que vous souhaitez associer à votre nouvelle clé
- Spécifier les adresses IP et sous-réseaux autorisés pour la nouvelle clé

Les clés d'API REST existantes peuvent être consultées ou supprimées en cliquant sur l'icône d'engrenage et en sélectionnant l'option correspondante.

!\[Options de la clé API\]\[29\]

{% alert important %}
Gardez à l'esprit qu'une fois que vous avez créé une nouvelle clé d'API, vous ne pouvez pas modifier la portée des permissions ou les adresses IP autorisées. Cette limitation est en place pour des raisons de sécurité. Si vous avez besoin de changer la portée d'une clé, créer une nouvelle clé avec les permissions mises à jour et implémenter cette clé à la place de l'ancienne clé. Une fois que vous avez terminé votre implémentation, continuez et supprimez l'ancienne clé.
{% endalert %}

### Explication d'ID d'utilisateur externe

Le `external_id` sert d'identifiant utilisateur unique pour lequel vous soumettez des données. Cet identifiant devrait être le même que celui que vous avez défini dans le SDK Braze afin d'éviter de créer plusieurs profils pour le même utilisateur.

### Explication de l'identifiant de l'utilisateur Braze

Le `braze_id` sert d'identifiant utilisateur unique qui est défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l'API REST en plus des external_ids.

#### Plus de ressources

Pour plus d'informations, reportez-vous à l'article suivant basé sur votre plateforme :

- [Paramétrage des identifiants d'utilisateur - iOS][9]
- [Paramétrage des identifiants d'utilisateur - Android][10]
- [Réglage des identifiants d'utilisateur - Windows Universal][13]

## Limites de l'API

Pour la plupart des API, Braze a une limite par défaut de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limite de taux pour mieux gérer les volumes élevés de données sur notre clientèle. Pour plus de détails, reportez-vous aux [limites de taux de l'API]({{site.baseurl}}/api/api_limits/).
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %} [26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %} [27]: {% image_buster /assets/img_archive/rest-api-key. ng %} [28]: {% image_buster /assets/img_archive/create-new-key.png %} [29]: {% image_buster /assets/img_archive/api-key-options.png %}

[8]: https://dashboard-01.braze.com/app_settings/developer_console/ "Developer Console"
[8]: https://dashboard-01.braze.com/app_settings/developer_console/ "Developer Console"
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#setting-user-ids
[support]: {{site.baseurl}}/braze_support/
