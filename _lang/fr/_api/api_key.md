---
nav_title: "Overview de la clé API"
article_title: Overview de la clé API REST
page_order: 2.1
description: "Cet article de référence couvre le concept des clés API, à quoi elles servent et comment elles sont utilisées." 
page_type: reference

---

# Overview de la clé API REST

>  Cet article de référence couvre deux des trois principaux types de clés que vous verrez chez Braze, la clé API REST ou la clé API du groupe d’apps, appelée `api_key`, et la clé d’identification de l’application, appelée `app_id`, ainsi que ce que sont ces clés, la façon dont elles sont utilisées chez Braze, leurs autorisations et la manière de les garder en sécurité. 

En plus de ces clés, il existe un troisième type appelé Clés d’identification pouvant être utilisé pour référencer des objets spécifiques tels que des modèles, des Canvas, des campagnes, des cartes de contenu et des segments de l’API. Pour plus d’informations, consultez la rubrique [Types d’identifiant API][2].

## Qu’est-ce qu’une clé API REST/API groupe d’apps ?

Une clé d’interface de programmation d’application REST (clé API REST) est un code unique qui est passé dans une API pour authentifier l’appel API et identifier l’application ou l’utilisateur d’appel. L’accès API est effectué en utilisant les requêtes Web HTTPS dans l’endpoint REST API de votre entreprise. Nous utilisons les clés API REST chez Braze en tandem avec nos clés d’identification App pour suivre, accéder, envoyer, exporter et analyser les données afin de vous assurer que tout fonctionne bien de votre côté et du nôtre. 

Les groupes d’apps et les clés API vont de pair chez Braze. Les groupes d’apps sont conçus pour héberger les versions de la même application sur plusieurs plateformes. De nombreux clients utilisent également des groupes d’apps pour contenir des versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le constater, ces groupes d’apps utilisent également l’API REST et possèdent leurs propres clés API REST. Ces clés peuvent être personnalisées individuellement pour inclure l’accès à des endpoints spécifiques sur l’API. Chaque appel d’API doit inclure une clé ayant accès à l’endpoint.

Nous faisons référence à la clé API REST et à la clé API du groupe d’apps comme `api_key`. Le `api_key` est inclus dans chaque requête comme en-tête de requête et sert de clé d’authentification qui vous permet d’utiliser nos API REST. Ces API REST sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur, etc.  Quand vous créez une nouvelle clé d’API REST, vous devez lui accorder l’accès à des endpoints spécifiques. En affectant des autorisations spécifiques à une clé API, vous pouvez limiter de façon précise les appels qu’une clé API peut authentifier.

### Où puis-je le trouver ?

Vos clés API sont toujours disponibles dans le tableau de bord de Braze dans **Developer Console (Console du développeur)** dans **Settings (Paramètres)**. En haut de cette nouvelle page, vous trouverez la section **REST API Keys (Clés API REST)**. Ici, vous pouvez afficher toutes les clés API REST/groupe d’apps disponibles et créer de nouvelles clés API.

### Comment puis-je l’utiliser ?

Avant avril 2020, les clés API étaient incluses dans le corps de demande API ou dans l’URL de demande comme paramètre. Braze a mis à jour la façon dont nous lisons les clés API. Les clés API sont maintenant définies avec l’en-tête de demande d’autorisation HTTP, rendant vos clés API plus sécurisées.

Bien que l’ancienne façon de transmettre les clés API continue de fonctionner, elle va être définitivement supprimée dans quelque temps. Nous encourageons donc les utilisateurs à mettre à jour les appels API en conséquence. 

{% alert important %}
**Vous recherchez le paramètre `api_key` dans vos endpoints Braze ?**<br>

En mai 2020, Braze a modifié la façon dont nous lisons les clés API pour plus de sécurité. Les clés API doivent être transmises comme en-tête de demande, voir VOTRE CLÉ-API-REST dans chaque demande d’exemple d’endpoint.
<br><br>
Braze continuera à prendre en charge le `api_key` transmis par le corps de la demande et les paramètres d’URL, mais finira par l’abandonner. Mettez donc à jour vos appels API en conséquence.
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
| `users.export.ids` | Requête pour les informations de profil utilisateur par identifiant, par ex., device_id, email_address, external_id.  |
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
| `kpi.mau.data_series` | Requête pour les utilisateurs actifs uniques sur une fenêtre de 30 jours glissants sur une période donnée. |
| `kpi.dau.data_series` |  Requête pour les utilisateurs actifs uniques par jour sur une période donnée. |
| `kpi.new_users.data_series` | Requête pour les nouveaux utilisateurs par jour sur une période donnée. |
| `kpi.uninstalls.data_series` | Requête pour les désinstallations d’applications par jour sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Templates %}

| Nom | Description |
|---|---|---|
| `templates.email.create` | Créez un nouveau modèle d’e-mail sur le tableau de bord. |
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
| `subscription.groups.get` | Obtenez le statut des groupes d’abonnement auxquels les utilisateurs spécifiques sont explicitement abonnés/désabonnés. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

Pour une description complète de ces endpoints d’API, consultez notre [Indice d’endpoints d’ API]({{site.baseurl}}/api/endpoints/) ou notre [collection Postman][6].

{% alert important %}
Une fois que vous avez créé une nouvelle clé API, vous ne pouvez plus modifier les autorisations ou la liste blanche des adresses IP. Cette restriction est en place pour des raisons de sécurité. Si vous devez modifier le périmètre d’une clé, créez une nouvelle clé avec les autorisations mises à jour et implémentez cette clé à la place de l’ancienne. Une fois que votre implémentation est terminée, vous pouvez supprimer l’ancienne clé.
{% endalert %}

## La clé API de l’identifiant de l’application

La clé API de l’identifiant de l’application ou `app_id` est un paramètre associant une activité à une application spécifique dans votre groupe d’apps. Elle désigne l’application dans le groupe d’apps avec laquelle vous interagissez. Par exemple, vous pouvez voir un `app_id` pour votre application iOS, un `app_id` pour votre application Android, et un `app_id` pour votre intégration Web. Chez Braze, il se peut que vous disposiez de plusieurs applications pour la même plateforme sur les différents types de plateformes que Braze prend en charge.

Les identifiants d’application chez Braze sont utilisés lors de l’intégration du SDK et pour référencer une application spécifique dans les appels API REST. Avec le `app_id` vous pouvez faire de nombreuses choses comme extraire des données pour un événement personnalisé qui s’est produit pour une application particulière, récupérer les statistiques de désinstallation, les statistiques de nouveaux utilisateurs, les statistiques d’utilisateur actif quotidien et les statistiques de début de session pour une application particulière.

Parfois, vous pouvez être invité à renseigner un `app_id` alors que vous ne travaillez pas avec une application, car il s’agit d’un champ hérité spécifique à une plateforme spécifique, vous pouvez « omettre » ce champ en incluant une chaîne de caractères comme marque substitutive pour ce paramètre requis.

### Où puis-je le trouver ?

Il existe deux façons de localiser votre `app_id`:

1. Vous pouvez trouver ce `app_id` ou identifiant d’application dans **Developer Console (Console du développeur)** dans **Settings (Paramètres)**. Sur cette nouvelle page, dans **Identification**, vous pourrez voir tous les `app_id` qui existe pour vos applications.

2. Accédez à **Manage Settings (Gérer les paramètres)** dans **Settings (Paramètres)**. Depuis cette nouvelle page, dans l’onglet **Settings (Paramètres)**, au milieu de la page, vous trouverez une « clé API pour **NOM DE L’APPLICATION** sur **PLATEFORME** » (par ex. « clé API Key pour Ice Cream sur iOS). Cette clé API est votre identifiant d’application.

### Clés API d’identifiant d’application multiple

Lors de la configuration du SDK, le cas d’usage le plus fréquent pour les clés API multiples est la séparation des clés API entre les variantes de version de débogage et de publication.
Pour basculer facilement entre plusieurs clés API d’identifiant d’application dans vos versions, nous vous recommandons de créer un fichier `braze.xml` pour chaque [variante de version][3]. Une variante de version est une combinaison du type de version et de la variété du produit. Remarquez que par défaut, un nouveau projet Android est configuré avec les types de version `debug` et `release`, et aucune variété de produit.

Pour chaque variante de version pertinente, créez un nouveau `braze.xml` pour elle dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```
Lorsque la variante de version est compilée, elle utilisera la nouvelle clé API.

## Sécurité clé API REST

La sécurité est de la plus haute importance chez Braze. Étant donné que les clés API REST permettent d’accéder aux endpoints API REST potentiellement sensibles, sécurisez ces clés et partagez-les uniquement avec des partenaires de confiance. Elles ne doivent jamais être exposées publiquement. Par exemple, n’utilisez pas cette clé pour faire des appels AJAX depuis votre site Web ou pour l’exposer autrement de façon publique.

Une bonne pratique de sécurité est d’accorder à un utilisateur uniquement les accès nécessaires pour qu’il puisse accomplir son travail ; ce principe peut également être appliqué aux Clés API en affectant des autorisations pour chaque clé. Ces autorisations vous offrent une meilleure sécurité et un meilleur contrôle sur les différentes parties de votre compte. 

Avec les identifiants d’application, le `app_id` est attribué par Braze et les autorisations ne peuvent pas être assignées ou révoquées. En raison de la nature de la relation entre `app_id` et le SDK, garder cet identifiant sécurisé est **crucial** pour la sécurité de votre application.


[2]: {{site.baseurl}}/api/identifier_types/
[3]: https://developer.android.com/studio/build/build-variants.html
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
