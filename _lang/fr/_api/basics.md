---
nav_title: "Overview API"
article_title: Overview API
page_order: 2.1
description: "Cet article de référence couvre les fondamentaux de l’API, y compris ce qu’est une API REST, sa terminologie et un aperçu des clés API."
page_type: reference
alias: /api/api_key/
---

# Overview API

> Cet article de référence couvre les fondamentaux de l’API, y compris sa terminologie courante, un aperçu des clés API REST, des permissions et de la manière de les sécuriser. 

## Définitions relatives aux API

Voici un aperçu des termes que vous pouvez rencontrer dans la documentation de l’API REST de Braze.

### Endpoints

Braze gère plusieurs instances différentes pour notre tableau de bord et nos Endpoints REST. Une fois votre compte provisionné ; vous vous connecterez à l’une des URL suivantes. Utilisez le bon Endpoint REST en vous basant sur l’instance qui vous a été provisionnée. Si vous n’êtes pas sûr, créez un [ticket de support][support] ou utilisez le tableau ci-dessous pour faire correspondre l’URL du tableau de bord que vous utilisez au bon Endpoint REST.

{% alert important %}
Quand vous utilisez des endpoints pour des appels API, utilisez le « Endpoint REST ».

Pour l’intégration SDK, utilisez le [« Endpoint SDK »]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), et non pas le « Endpoint REST ».
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

### Limites de l’API

Pour la plupart des API, la limite de débit par défaut définie par Braze est de 250 000 requêtes par heure. Cependant, certains types de requêtes ont leur propre limite de débit pour une meilleure gestion des grands volumes de données de notre base client. Consultez les [limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus d’informations

### ID utilisateur 

- **ID utilisateur externe** : Le `external_id` sert d’identifiant utilisateur unique pour lequel vous soumettez des données. Cet identifiant doit être identique à celui que vous avez défini dans le SDK Braze afin d’éviter de créer plusieurs profils pour le même utilisateur.
- **ID d’identifiant Braze** : `braze_id` est un identifiant utilisateur unique défini par Braze. Cet identifiant peut être utilisé pour supprimer des utilisateurs via l’API REST, en plus des external_ids.

Pour plus d’informations, consultez l’article suivant spécifique à votre plateforme : [iOS][9], [Android][10] et [Web][13].

## Clé API REST

Une clé d’interface de programmation d’application REST (clé API REST) est un code unique qui est passé dans une API pour authentifier l’appel API et identifier l’application ou l’utilisateur d’appel. L’accès API s’effectue à l’aide des requêtes Web HTTPS dans l’endpoint de l’API REST de votre entreprise.  Chez Braze, nous utilisons conjointement les clés API REST et nos clés d’identification App pour accéder aux données, et les suivre, les envoyer, les exporter et les analyser afin de vous assurer que tout fonctionne bien de votre côté et du nôtre. 

Les groupes d’apps et les clés API vont de pair chez Braze. Les groupes d’apps sont conçus pour héberger les versions de la même application sur plusieurs plateformes. De nombreux clients utilisent également des groupes d’apps pour avoir des versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le constater, ces groupes d’apps utilisent également l’API REST et possèdent leurs propres clés API REST. Ces clés peuvent être personnalisées individuellement pour inclure l’accès à des endpoints spécifiques sur l’API. Chaque appel d’API doit inclure une clé ayant accès à l’endpoint.

Nous faisons référence à la clé API REST et à la clé API du groupe d’apps comme `api_key`. La `api_key` est incluse dans chaque requête comme en-tête de requête et sert de clé d’authentification qui vous permet d’utiliser nos API REST. Ces API REST sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur, etc. Quand vous créez une nouvelle clé d’API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

![Volet Clés API REST sur l’onglet API Settings (Paramètres API) de la Developer Console (Console du développeur).][27]

{% alert tip %}
En plus des clés API REST, il existe un troisième type appelé Clés d’identification qui permet de référencer des objets spécifiques tels que des apps, des modèles, des Canvas, des campagnes, des cartes de contenu et des segments de l’API. Pour plus d’informations, consultez la rubrique [Types d’identifiant API]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### Autorisations de clé API REST

Les autorisations de clés API sont des autorisations que vous pouvez affecter à un utilisateur ou un groupe pour limiter leur accès à certains appels API.

{% tabs %}
{% tab User Data %}

| Autorisation | Description  |
|---|---|---|
| `users.track` | Enregistrer les attributs utilisateur, les événements personnalisés et les achats  |
| `users.delete` | Supprimer un utilisateur. |
| `users.alias.new` | Créer un nouvel alias pour un utilisateur existant.  |
| `users.identify` | Requête pour les informations de profil utilisateur par ID utilisateur.  |
| `users.export.ids` | Requête pour les informations de profil utilisateur par Identifiant, par exemple device_id, email_address et external_id.  |
| `users.export.segment` | Requête pour les informations de profil utilisateur par segment. |
| `users.external_ids.rename` | Renommer l’ID externe existant d’un utilisateur. |
| `users.external_ids.remove` | Supprimer l’ID externe obsolète d’un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Email %}

| Nom | Description |
|---|---|---|
| `email.unsubscribe` | Requête pour les adresses e-mail non souscrites.  |
| `email.status` | Modifier l’état de l’adresse e-mail. |
| `email.hard_bounces` | Requête pour les adresses e-mail avec rebond élevé. |
| `email.bounce.remove` | Supprimer les adresses e-mail de votre liste de rebonds élevés. |
| `email.spam.remove` | Supprimer les adresses e-mail de votre liste de spam. |
| `email.blacklist` | Ajouter les adresses e-mail à la liste noire |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Messages %}

| Nom | Description |
|---|---|---|
| `messages.send` | Envoyer un message immédiat et ad hoc à des utilisateurs spécifiques. |
| `messages.schedule.create` | Planifier un message à envoyer à un moment précis. |
| `messages.schedule.update` | Mettre à jour un message planifié. |
| `messages.schedule.delete` | Supprimer un message planifié. |
| `messages.schedule_broadcasts` | Interroger tous les messages de diffusion programmés. |
| `messages.live_activity.update` | Mettre à jour une activité iOS Live. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Campaigns %}

| Nom | Description |
|---|---|---|
| `campaigns.trigger.send` | Déclencher l’envoi d’une campagne existante. |
| `campaigns.trigger.schedule.create` | Planifier le futur envoi d’une campagne avec une livraison déclenchée par API. |
| `campaigns.trigger.schedule.update` | Mettre à jour une campagne planifiée avec une livraison déclenchée par API. |
| `campaigns.trigger.schedule.delete` | Supprimer une campagne planifiée avec une livraison déclenchée par API |
| `campaigns.list` | Requête pour une liste de campagnes. |
| `campaigns.data_series` | Requête pour une analyse de campagne sur une période donnée. |
| `campaigns.details` | Requête pour les informations d’une campagne spécifique. |
| `sends.data_series` | Requête pour l’analyse des messages envoyés sur une période donnée. |
| `sends.id.create` | Créer un ID d’envoi pour le suivi des messages. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| Nom | Description |
|---|---|---|
| `canvas.trigger.send` | Déclencher l’envoi d’un Canvas existant. |
| `canvas.trigger.schedule.create` | Planifier le futur envoi d’un Canvas avec une livraison déclenchée par API. |
| `canvas.trigger.schedule.update` | Mettre à jour un Canvas planifié avec une livraison déclenchée par API. |
| `canvas.trigger.schedule.delete` | Supprimer un Canvas programmé avec une livraison déclenchée par API. |
| `canvas.list` | Requête pour une liste de Canvas. |
| `canvas.data_series` | Requête pour analyse de Canvas sur une période donnée. |
| `canvas.details` | Requête pour les informations d’un Canvas spécifique. |
| `canvas.data_summary` | Requête pour les cumuls de l’analyse de Canvas sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Segments %}

| Nom | Description |
|---|---|---|
| `segments.list` | Requête pour une liste de segments. |
| `segments.data_series` | Requête pour l’analyse de segment sur une période donnée. |
| `segments.details` | Requête pour les informations d’un segment spécifique. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Purchases %}

| Nom | Description |
|---|---|---|
| `purchases.product_list` | Requête pour une liste de produits achetés dans votre application. |
| `purchases.revenue_series` | Requête pour le montant total des dépenses par jour dans votre application sur une période donnée. |
| `purchases.quantity_series` | Requête pour le nombre total d’achats par jour dans votre application sur une période. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Events %}

| Nom | Description |
|---|---|---|
| `events.list` | Requête pour une liste d’événements personnalisés. |
| `events.data_series` | Requête pour les occurrences d’un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab News Feed %}

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

| Nom | Description |
|---|---|---|
| `feed.list` | Requête pour une liste de cartes de fil d’actualité. |
| `feed.data_series` | Requête pour l’analyse du fil d’actualité sur une période donnée. |
| `feed.details` | Requête pour plus d’informations sur un fil d’actualité spécifique. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Sessions %}

| Nom | Description |
|---|---|---|
| `sessions.data_series` | Requête pour les sessions par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab KPIs %}

| Nom | Description |
|---|---|---|
| `kpi.mau.data_series` | Requête pour les utilisateurs actifs uniques sur une fenêtre de 30 jours glissants sur une période donnée. |
| `kpi.dau.data_series` |  Requête pour les utilisateurs actifs uniques par jour sur une période donnée. |
| `kpi.new_users.data_series` | Requête pour les nouveaux utilisateurs par jour sur une période donnée. |
| `kpi.uninstalls.data_series` | Requête pour les désinstallations d’applications par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Templates %}

| Nom | Description |
|---|---|---|
| `templates.email.create` | Créer un nouveau modèle d’e-mail sur le tableau de bord. |
| `templates.email.update` | Mettre à jour un modèle d’e-mail stocké sur le tableau de bord. |
| `templates.email.info` | Requête pour les informations d’un modèle spécifique. |
| `templates.email.list` | Requête pour une liste de modèles d’e-mail. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab SSO %}

| Nom | Description |
|---|---|---|
| `sso.saml.login` |  Configurer la connexion initiée par le fournisseur d’identité. Lisez notre documentation pour plus d’informations. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Content Blocks %}

| Nom | Description |
|---|---|---|
| `content_blocks.info` | Requête pour les informations d’un modèle spécifique. |
| `content_blocks.list` | Requête pour une liste de blocs de contenu. |
| `content_blocks.create` | Créer un nouveau bloc de contenu sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Subscription %}

| Nom | Description |
|---|---|---|
| `subscription.status.set` | Définir le statut du groupe d’abonnement. |
| `subscription.status.get` | Obtenir le statut du groupe d’abonnement. |
| `subscription.groups.get` | Obtenir le statut des groupes d’abonnement auxquels les utilisateurs spécifiques sont explicitement abonnés/désabonnés. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Créer et gérer des clés d’API REST

![][28]{: style="max-width:20%;float:right;margin-left:15px;"}

Pour créer une nouvelle clé d’API REST, allez sur la **Developer Console** sur le Tableau de bord de Braze. Cette page affiche vos clés API existantes. Pour créer une nouvelle clé, cliquez sur **Create New API Key (Créer une nouvelle clé d’API)**.

Vous pourrez ensuite :

- Nommer votre nouvelle clé pour pouvoir l’identifier facilement
- Sélectionner les autorisations que vous souhaitez associer à votre nouvelle clé
- Spécifier les sous-réseaux et adresses IP autorisés pour cette nouvelle clé

Les clés API REST existantes peuvent être visualisées ou supprimées en cliquant sur les paramètres <i class="fas fa-gear"></i> et en sélectionnant l’option correspondante.

![][29]

{% alert important %}
Gardez à l’esprit qu’une fois que vous avez créé une nouvelle clé API, vous ne pouvez plus modifier les autorisations ni la liste des adresses IP autorisées. Cette restriction est en place pour des raisons de sécurité. Si vous devez modifier le périmètre d’une clé, créez une nouvelle clé avec les autorisations mises à jour et implémentez cette clé à la place de l’ancienne. Une fois que votre implémentation est terminée, vous pouvez supprimer l’ancienne clé.
{% endalert %}

## Sécurité clé API REST

Les clés d’API servent à authentifier les appels de l’API. Quand vous créez une nouvelle clé API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

Étant donné que les clés API REST permettent d’accéder à des endpoints API REST potentiellement sensibles, sécurisez ces clés et partagez-les uniquement avec des partenaires de confiance. Elles ne doivent jamais être exposées publiquement. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.

Une bonne pratique de sécurité est d’accorder à un utilisateur uniquement les accès nécessaires pour qu’il puisse accomplir son travail ; ce principe peut également être appliqué aux Clés API en affectant des autorisations pour chaque clé. Ces autorisations vous offrent une meilleure sécurité et un meilleur contrôle sur les différentes parties de votre compte. 

![Autorisations de clé API disponibles lors de la création d’une clé API.][25]

{% alert warning %}
Comme les clés d’API REST permettent d’accéder à des endpoints de l’API REST potentiellement sensibles, veillez à ce qu’elles soient stockées et utilisées de façon sécurisée. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.
{% endalert %}

En cas d’exposition accidentelle d’une clé, elle pourra être supprimée à partir de la Developer Console. Pour obtenir de l’aide pour ce processus, créez un [ticket de support][support].

### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez spécifier une liste d’adresses IP et de sous-réseaux autorisés à faire des requêtes API REST pour une clé API REST spécifique. C’est ce que l’on appelle une « liste autorisée » ou « liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les dans la section **Liste blanche d’adresses IP** lors de la création d’une clé API REST : 

![Possibilité de créer une liste blanche d’adresses IP lors de la création d’une clé API][26]

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre liste [d’adresses IP à autoriser]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Ressources complémentaires

### Bibliothèque client Ruby

Si vous utilisez Ruby pour implémenter Braze, vous pouvez utiliser notre [Bibliothèque Client Ruby](https://github.com/braze-inc/braze-api-client-ruby) pour réduire le temps d’importation des données. Une bibliothèque cliente est une collection de code spécifique à un langage de programmation (dans ce cas, Ruby) qui facilite l’utilisation d’une API.

La bibliothèque client Ruby prend en charge les [Endpoints Utilisateur]({{site.baseurl}}/api/endpoints/#user-data).

{% alert note %}
Cette bibliothèque cliente est actuellement en version bêta. Voulez-vous nous aider à améliorer cette bibliothèque ? Envoyez vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[support]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
