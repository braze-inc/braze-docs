---
nav_title: "Types d’identifiant API"
article_title: Types d’identifiant API
page_order: 2.2
toc_headers: h2
description: "Cet article de référence traite des différents types d'identifiants d'API qui existent dans le tableau de bord de Braze, de l'endroit où vous pouvez les trouver et de leur utilité." 
page_type: reference

---

# Types d’identifiant API

> Ce guide de référence aborde les différents types d’identifiants API que vous trouverez dans le tableau de bord de Braze, leur but, où vous pouvez les trouver et comment ils sont généralement utilisés. Pour plus d'informations sur les clés API REST ou les clés API de l'espace de travail, reportez-vous à l'[aperçu de l'API.]({{site.baseurl}}/api/api_key/)

Les identifiants suivants peuvent être utilisés pour accéder à votre modèle, Canvas, campagne ou segment à partir de l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8.](https://en.wikipedia.org/wiki/UTF-8) 

## Identifiant de l'application

L'identifiant de l'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous pouvez avoir un `app_id` pour votre application iOS, un `app_id` pour votre application Android et un `app_id` pour votre intégration Web. Chez Braze, il se peut que vous disposiez de plusieurs applications pour la même plateforme sur les différents types de plateformes que Braze prend en charge.

### Où puis-je le trouver ?

Il existe deux façons de localiser votre `app_id`:

{% tabs local %}
{% tab App Identifiers %}
Allez dans **Paramètres** > **API et identifiants** > **Identifiants d'application**. Votre clé API pour chaque application est indiquée dans la colonne **Identifiant**.
{% endtab %}

{% tab App Settings %}
Allez dans **Réglages** > **Réglages de l'application**. Votre clé API est indiquée à côté du champ **Clé API** dans la section des paramètres.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

Les identifiants d’application chez Braze sont utilisés lors de l’intégration du SDK et pour référencer une application spécifique dans les appels API REST. Avec le `app_id` vous pouvez faire de nombreuses choses comme extraire des données pour un événement personnalisé qui s’est produit pour une application particulière, récupérer les statistiques de désinstallation, les statistiques de nouveaux utilisateurs, les statistiques d’utilisateur actif quotidien et les statistiques de début de session pour une application particulière.

{% alert tip %}
Il peut arriver que l'on vous demande un `app_id`, mais que vous ne travailliez pas avec une application, car il s'agit d'un champ de plateforme traditionnelle spécifique, vous pouvez omettre ce champ en incluant n'importe quelle chaîne de caractères comme marque substitutive pour ce paramètre obligatoire.
{% endalert %}

### Identifiants d’application multiples

Lors de la configuration du SDK, le cas d’usage le plus fréquent avec les identifiants d’application multiples est de séparer ces identifiants entre les variantes de version de débogage et de publication.

Pour basculer facilement entre plusieurs identifiants d'applications dans vos builds, nous vous recommandons de créer un fichier `braze.xml` distinct pour chaque [variante de build](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de version est une combinaison du type de version et de la variété du produit. Par défaut, un nouveau projet Android est configuré avec les types de construction `debug` et `release` et aucun produit.

Pour chaque variante de version pertinente, créez un nouveau `braze.xml` pour elle dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Lorsque la variante de version est compilée, elle utilisera le nouvel identifiant.

## Identifiant du modèle

Un identifiant de [modèle]({{site.baseurl}}/api/endpoints/templates/) ou ID de modèle est une clé aléatoire générée par Braze pour un modèle donné au sein du tableau de bord. Les ID de modèle sont uniques pour chaque modèle et peuvent être utilisés pour référencer les modèles via l’API. 

Les modèles sont très utiles si votre entreprise sous-traite vos conceptions HTML pour des campagnes. Une fois les modèles créés, vous disposez maintenant d'un modèle qui n'est pas spécifique à une campagne mais qui peut être appliqué à une série de campagnes, comme une lettre d'information.

### Où puis-je le trouver ?

Vous pouvez trouver l'ID de votre modèle de deux façons :

{% tabs local %}
{% tab Templates %}
Cliquez sur **Modèles**, puis sélectionnez une page modèle et choisissez un modèle préexistant. Si le modèle que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page de modèle individuel, vous trouverez votre identifiant de modèle.
{% endtab %}

{% tab API Keys %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Mettre à jour les modèles à l'aide de l'API
- Saisir des informations sur un modèle spécifique

## Identifiant Canvas

Un identifiant de [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) ou ID Canvas est une clé aléatoire générée par Braze pour un Canvas donné au sein du tableau de bord. Les ID de Canvas sont uniques pour chaque Canvas et peuvent être utilisés pour référencer des Canvas via l’API. 

Gardez à l'esprit que si vous avez un canvas avec des variantes, il existe un ID global pour le canvas ainsi que des ID individuels pour les variantes, imbriqués dans le canvas principal. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de Canvas dans le tableau de bord. Allez dans **Messagerie** > **Canvas** et sélectionnez un Canvas préexistant. Si le Canvas que vous voulez n’existe pas encore, créez-en un et enregistrez-le. En bas d'une page individuelle de Canvas, cliquez sur **Analyser variantes**. Une fenêtre apparaît avec l’identifiant de l’API de Canvas situé en bas.

### À quoi cela sert-il ?

- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances du Canvas
- Obtenir des informations sur un Canvas spécifique
- Avec Currents pour apporter des données au niveau de l'utilisateur pour une approche plus globale de Canvases.
- Avec réception/distribution déclenchée par l'API pour collecter des statistiques sur les messages transactionnels.

## Identifiant de campagne

Un identifiant de [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou ID de campagne est une clé aléatoire générée par Braze pour une campagne donnée dans le tableau de bord. Les ID de campagne sont uniques pour chaque campagne et peuvent être utilisés pour référencer des campagnes via l’API. 

Gardez à l'esprit que si vous avez une campagne avec des variantes, il y a à la fois un ID de campagne global et des ID de campagne de variante individuels imbriqués sous la campagne principale. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de campagne de deux façons :

{% tabs local %}
{% tab Campaigns %}
Allez dans **Envoi de messages** > **Campagnes** et sélectionnez une campagne préexistante. Si la campagne que vous souhaitez n’existe pas encore, créez-en une et enregistrez-la. Au bas de la page de la campagne individuelle, vous pourrez trouver votre **identifiant API de campagne.**

{% endtab %}

{% tab API Keys %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances de la campagne
- Obtenir des informations sur une campagne spécifique
- Avec Currents pour apporter des données au niveau utilisateur pour bénéficier d’un « tableau général » des campagnes
- Avec réception/distribution déclenchée par l'API pour collecter des statistiques sur les messages transactionnels.
- Pour [rechercher une campagne spécifique]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) sur la page **Campagnes** à l'aide du filtre `api_id:YOUR_API_ID`

## Identifiant de segment

Un identifiant de [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) ou ID de segment est une clé aléatoire générée par Braze pour un segment donné au sein du tableau de bord. Les ID de segment sont uniques pour chaque segment et peuvent être utilisés pour référencer les segments via l’API. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de segmentation de deux façons :

{% tabs local %}
{% tab Segments %}
Allez dans **Audience** > **Segments** et sélectionnez un segment préexistant. Si le segment que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page du segment individuel, vous trouverez votre identifiant de segment.

{% endtab %}

{% tab API Keys %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Obtenir des informations sur un segment spécifique
- Récupérer l’analyse d’un segment spécifique
- Récupérer le nombre de fois où un événement personnalisé a été enregistré pour un segment particulier
- Spécifiez et envoyez une campagne aux membres d'une segmentation à partir de l'API.

## Identifiant d’envoi

Un identifiant d'envoi, ou ID d'envoi, est une clé générée par Braze ou créée par vous pour un envoi de message donné, sous laquelle l'analyse/analytique doit être suivie. L'identifiant d'envoi vous permet d'obtenir des analyses/analytiques pour une instance spécifique d'une campagne envoyée via l'[endpoint`/sends/data_series`.]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)

### Où puis-je le trouver ?

Les API et campagnes déclenchées par API qui sont envoyées en tant que diffusion génèrent automatiquement un identifiant d’envoi si un identifiant d’envoi n’est pas fourni. Si vous souhaitez spécifier votre propre identifiant d'envoi, vous devrez d'abord en créer un via l'[endpoint`/sends/id/create`.]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) L’identifiant ne peut comporter que des caractères ASCII et ne peut faire plus de 64 caractères. Vous pouvez réutiliser un identifiant d’envoi sur plusieurs envois de la même campagne si vous souhaitez regrouper les analyses de ces envois.

### À quoi cela sert-il ?
Envoyer et suivre par programme les performances des messages, sans création de campagne pour chaque envoi.

## Identifiant du groupe d'abonnement

Un identifiant de groupe d'abonnement, ou ID de groupe d'abonnement, est une clé générée par Braze pour un groupe d'abonnement donné. Les ID sont uniques à chaque groupe d'abonnement et peuvent être utilisés pour référencer les groupes d'abonnement via l'API.

### Où puis-je le trouver ?

Allez dans **Audience** > **Abonnements** et copiez l'ID à côté du groupe d'abonnement concerné.

### À quoi cela sert-il ?

- Liste des groupes d'abonnement d'un utilisateur
- Obtenir le statut du groupe d'abonnement d'un utilisateur
- Mise à jour du statut du groupe d'abonnement d'un utilisateur
