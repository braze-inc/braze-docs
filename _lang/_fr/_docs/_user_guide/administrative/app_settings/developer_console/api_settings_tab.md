---
nav_title: Paramètres de l'API
article_title: Paramètres de l'API
page_order: 0
page_type: Référence
description: "Cet article de référence couvre la page des paramètres de l'API, qui affiche les identifications API pour votre groupe d'applications."
---

# Onglet Paramètres API

L'onglet **API Settings** affiche les identifications API pour votre groupe d'applications. La première section sur **Services** liste les articles pertinents pour différentes utilisations de l'API Braze ([Données Utilisateurs][3],[Messaging][4], [Email Sync][5], ou [Export][6]).

La page des **Paramètres de l'API** est ensuite divisée en les sections suivantes :

- Clés API REST
- Identification
- Identifiants d'API supplémentaires

### Clés API REST

Cette section fournit vos clés API REST Groupe d'Apps, les identifiants uniques qui vous permettent d'accéder à vos données pour un groupe d'applications. Une clé d'API REST est requise avec chaque requête à l'API Braze. Pour plus d'informations sur la création et l'utilisation de clés API, reportez-vous à notre [aperçu de la clé API REST]({{site.baseurl}}/api/api_key/).

#### Liste des autorisations IP de l'API

Pour plus de sécurité, vous pouvez spécifier une liste d'adresses IP et de sous-réseaux qui sont autorisés à faire des requêtes d'API REST pour une clé REST donnée. On l'appelle liste d'autorisation, ou liste blanche. Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les à la section **Liste blanche des IPs** lors de la création d'une nouvelle clé API REST :

!\[Liste blanche IP de l'API\]\[26\]

Si vous n'en spécifiez aucune, les requêtes peuvent être envoyées depuis n'importe quelle adresse IP.

{% alert tip %}
Faire un webhook Brase-to-Braze et utiliser le droit d'inscription? Consultez notre liste d'adresses IP [pour la whitelist]({{site.baseurl}}/docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### Identification

La section **Identification** inclut une liste d'identifiants qui sont utilisés pour référencer des applications spécifiques dans les requêtes faites à l'API Braze. Pour en savoir plus sur les identifiants de l'application, reportez-vous à la [clé API d'identification de l'application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key).

### Identifiants API supplémentaires

Pour s'intégrer à notre API, vous pouvez rechercher les identifiants liés à n'importe quel segment, campagnes, cartes et plus que vous voulez accéder à partir de l'API externe de Braze. Tous les messages doivent suivre l'encodage [UTF-8][12]. Une fois que vous en avez sélectionné une, l'identifiant sera affiché sous le menu déroulant. .

Pour plus d'informations, reportez-vous à [API Identifier Types]({{site.baseurl}}/api/identifier_types/).
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}

[3]: {{site.baseurl}}/api/endpoints/user_data/
[4]: {{site.baseurl}}/api/endpoints/messaging/
[5]: {{site.baseurl}}/api/endpoints/email/
[6]: {{site.baseurl}}/api/endpoints/export/
[12]: https://en.wikipedia.org/wiki/UTF-8
