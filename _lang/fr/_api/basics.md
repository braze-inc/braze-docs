---
nav_title: Overview
article_title: Overview API
page_order: 0
description: "Cet article de référence couvre les fondamentaux de l’API, y compris ce qu’est une API REST et sa terminologie, et décrit brièvement les clés et les limites de l’API."
page_type: reference

---
# Overview API

> Braze fournit une API REST haute performance qui vous permet de suivre vos utilisateurs, d’envoyer des messages, d’exporter des données et plus encore. Cet article de référence explique ce qu’est une API REST, sa terminologie et décrit brièvement les Clés API et les limites de l’API.

## Qu'est-ce qu'une API REST ?

Une API REST est un moyen de transférer par programme des informations sur le Web à l'aide d'un schéma prédéfini. Braze a créé de nombreux endpoints différents qui effectuent diverses actions et/ou renvoient diverses données.

{% alert note %}
Les clients qui utilisent la base de données EU de Braze doivent utiliser le endpoint `https://rest.fra-01.braze.eu/`. Cet endpoint sera utilisé pour configurer le SDK Braze [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#compile-time-endpoint-configuration-recommended), le SDK Braze [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml), et le SDK Braze [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).
{% endalert %}

## Définitions relatives aux API

Voici une brève overview des termes que vous pouvez rencontrer dans la documentation de l’API REST de Braze.

### Endpoints

Braze gère plusieurs instances différentes pour notre tableau de bord et nos Endpoints REST. Une fois votre compte provisionné ; vous vous connecterez à l’une des URL suivantes. Utilisez le bon Endpoint REST en vous basant sur l’instance qui vous a été provisionnée. Si vous n’êtes pas sûr, créez un [ticket de support][support] ou utilisez le tableau ci-dessous pour faire correspondre l’URL du tableau de bord que vous utilisez au bon Endpoint REST.

{% alert important %}
Quand vous utilisez des endpoints pour des appels API, utilisez le « REST Endpoint ».

Pour l’ intégration SDK, utilisez le [« Endpoint SDK "]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), et non pas le « Endpoint REST ».
{% endalert %}

|Instance|URL|Endpoint REST|Endpoint SDK|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Explication (secret d’entreprise)

Le `company_secret` était auparavant inclus avec toutes les requêtes API, mais il est obsolète depuis octobre 2014. Ce champ sera ignoré pour toutes les futures requêtes API pour assurer la rétrocompatibilité.

### Clés API du Groupe REST d’Apps

{% alert note %}
Pour mieux comprendre les différents types de Clé API disponibles avec Braze, consultez nos articles de référence consacrés aux <a href="{{site.baseurl}}/api/api_key/">Clés API</a> et aux<a href="{{site.baseurl}}/api/identifier_types/">Types d’Identifiants pour les API.</a>

{% endalert %}

Le `api_key` inclus dans chaque requête sert de clé d’authentification qui permet au code de votre serveur d’utiliser nos API REST. Au sein de votre entreprise, chaque Groupe d'apps aura un ensemble unique de Clés API REST. Elles sont disponibles sur le Tableau de bord de Braze en allant sur la section Developer Console de chaque groupe d’apps. Pour utiliser l’API REST pour un Groupe d'apps donné, vous devez créer des clés et leur attribuer des permissions.

![Volet Clés API REST sur l’onglet Paramètres API de la Developer Console.][27]

#### Permissions de clé API

Les clés d’API servent à authentifier les appels de l’API. Quand vous créez une nouvelle clé d’API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des permissions spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

Une bonne pratique de sécurité est d’accorder à un utilisateur uniquement les accès nécessaires pour qu’il puisse accomplir son travail ; ce principe peut également être appliqué aux Clés API en affectant des permissions pour chaque clé. Ces autorisations vous offrent une meilleure sécurité et un meilleur contrôle sur les différentes parties de votre compte.

![Permissions de clé API disponibles lors de la création d’une clé API.][25]

{% alert warning %}
Comme les clés d’API REST permettent d’accéder à des endpoints de l’API REST potentiellement sensibles, veillez à ce qu’elles soient stockées et utilisées de façon sécurisée. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.
{% endalert %}

En cas d’exposition accidentelle d’une clé, elle pourra être supprimée à partir de la [Developer Console][8]. Pour obtenir de l’aide pour ce processus, créez un [ticket de support][support].

#### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez spécifier une liste d’adresses IP et de sous-réseaux autorisés à faire des requêtes API REST pour une clé API REST spécifique. C’est ce que l’on appelle une « liste autorisée » ou « liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez les dans la section **Liste Blanche d’adresses IP** lors de la création d’une clé API REST : 

![Possibilité de créer une liste blanche d’adresses IP lors de la création d’une clé API][26]

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre liste [d’adresses IP à autoriser]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

#### Créer et gérer des clés d’API REST

![][28]{: style="max-width:20%;float:right;margin-left:15px;"}

Pour créer une nouvelle clé d’API REST, allez sur la [Developer Console][8] sur le Tableau de bord de Braze. Cette page affiche vos clés API existantes. Pour créer une nouvelle clé, cliquez sur **Créer une nouvelle clé d’API**.

Vous pourrez ensuite :

- Nommer votre nouvelle clé pour pouvoir l’identifier facilement
- Sélectionner les permissions que vous souhaitez associer à votre nouvelle clé
- Spécifier les sous-réseaux et adresses IP autorisés pour cette nouvelle clé

Les clés API REST existantes peuvent être visualisées ou supprimées en cliquant sur paramètres <i class="fas fa-gear"></i> et en sélectionnant l’option correspondante.

![][29]

{% alert important %}
Gardez à l’esprit qu’une fois que vous avez créé une nouvelle clé API, vous ne pouvez plus modifier les permissions ou la liste des adresses IP autorisées. Cette restriction est en place pour des raisons de sécurité. Si vous devez modifier le périmètre d’une clé, créez une nouvelle clé avec les permissions mises à jour et implémentez cette clé à la place de l’ancienne. Une fois que votre implémentation est terminée, vous pouvez supprimer l’ancienne clé.
{% endalert %}

### Description des ID Utilisateur Externes

Le `external_id` sert d’identifiant utilisateur unique pour lequel vous soumettez des données. Cet identifiant doit être identique à celui que vous avez défini dans le SDK Braze afin d’éviter de créer plusieurs profils pour le même utilisateur.

### Description des ID Utilisateur Braze

Le `braze_id` est un identifiant utilisateur unique défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l’API REST en plus des identifiants_externes.

#### Ressources supplémentaires

Pour plus d’informations, consultez l’article suivant spécifique à votre plateforme :

- [Définir des ID Utilisateur - iOS][9]
- [Définir des ID Utilisateur - - Android][10]
- [Définir des ID Utilisateur - - Windows Universal][13]

## Limites de l’API

Pour la plupart des API, la limitation du taux par défaut définie par Braze est de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limitation du taux pour une meilleure gestion des grands volumes de données de notre base client. Consultez les [limitation du taux de l’API]({{site.baseurl}}/api/api_limits/) pour plus de détails.

## Ressources complémentaires

### Bibliothèque client Ruby

Si vous utilisez Ruby pour implémenter Braze, vous pouvez utiliser notre [Bibliothèque Client Ruby](https://github.com/braze-inc/braze-api-client-ruby) pour réduire le temps d’importation des données. Une bibliothèque cliente est une collection de code spécifique à un langage de programmation (dans ce cas, Ruby) qui facilite l'utilisation d'une API.

La Bibliothéque client Ruby prend en charge les [Endpoints Utilisateur]({{site.baseurl}}/api/endpoints/#user-data).

{% alert note %}
Cette bibliothèque cliente est actuellement en version bêta. Voulez-vous nous aider à améliorer cette bibliothèque ? Envoyez vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[8]: https://dashboard-01.braze.com/app_settings/developer_console/ "Developer Console"
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#setting-user-ids
[support]: {{site.baseurl}}/braze_support/
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
