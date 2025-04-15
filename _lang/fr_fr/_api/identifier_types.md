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

Les identifiants suivants peuvent être utilisés pour accéder à votre modèle, Canvas, campagne, segment, envoi ou carte depuis l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8.](https://en.wikipedia.org/wiki/UTF-8) 

## Identifiant d’application

L'identifiant de l'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous pouvez avoir un `app_id` pour votre application iOS, un `app_id` pour votre application Android et un `app_id` pour votre intégration Web. Chez Braze, il se peut que vous disposiez de plusieurs applications pour la même plateforme sur les différents types de plateformes que Braze prend en charge.

### Où puis-je le trouver ?

Il existe deux façons de localiser votre `app_id`:

{% tabs local %}
{% tab Identificateurs d'applications %}
Allez dans **Paramètres** > **API et identifiants** > **Identifiants d'application**. Votre clé API pour chaque application est indiquée dans la colonne **Identifiant**.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), **App Identifiers** se trouve dans **Developer Console** > **API Settings.**
{% endalert %}
{% endtab %}

{% tab Paramètres de l'application %}
Allez dans **Réglages** > **Réglages de l'application**. Votre clé API est indiquée à côté du champ **Clé API** dans la section des paramètres.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), vous pouvez  accéder aux **paramètres des applications** en sélectionnant **Gérer les paramètres** > **Paramètres**.
{% endalert %}
{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

Les identifiants d’application chez Braze sont utilisés lors de l’intégration du SDK et pour référencer une application spécifique dans les appels API REST. Avec le `app_id` vous pouvez faire de nombreuses choses comme extraire des données pour un événement personnalisé qui s’est produit pour une application particulière, récupérer les statistiques de désinstallation, les statistiques de nouveaux utilisateurs, les statistiques d’utilisateur actif quotidien et les statistiques de début de session pour une application particulière.

{% alert tip %}
Parfois, vous pouvez être invité à renseigner un `app_id` alors que vous ne travaillez pas avec une application, car il s’agit d’un champ hérité d’une plateforme spécifique. Vous pouvez « omettre » ce champ en incluant une chaîne de caractères comme marque substitutive pour ce paramètre requis.
{% endalert %}

### Identifiants d’application multiples

Lors de la configuration du SDK, le cas d’usage le plus fréquent avec les identifiants d’application multiples est de séparer ces identifiants entre les variantes de version de débogage et de publication.

Pour passer facilement d'un identifiant d'application à l'autre dans vos builds, nous vous recommandons de créer un fichier `braze.xml` distinct pour chaque [variante de build](https://developer.android.com/studio/build/build-variants.html) concernée. Une variante de version est une combinaison du type de version et de la variété du produit. Par défaut, un nouveau projet Android est configuré avec les types de construction `debug` et `release` et aucun produit.

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

Les modèles sont parfaits si votre entreprise établit des contrats sur vos conceptions HTML pour les campagnes. Une fois les modèles créés, vous disposez maintenant d'un modèle qui n'est pas spécifique à une campagne mais qui peut être appliqué à une série de campagnes comme une newsletter.

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de modèle de deux manières :

{% tabs local %}
{% tab Modèles %}
Cliquez sur **Modèles**, puis sélectionnez une page modèle et choisissez un modèle préexistant. Si le modèle que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page de modèle individuel, vous trouverez votre identifiant de modèle.
{% endtab %}

{% tab Clés API %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), vous pouvez trouver les identifiants d'API dans la **console de développement** > **Paramètres d'API**.
{% endalert %}
{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Mettre à jour les modèles sur API
- Saisir des informations sur un modèle spécifique

## Identifiant Canvas

Un identifiant de [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) ou ID Canvas est une clé aléatoire générée par Braze pour un Canvas donné au sein du tableau de bord. Les ID de Canvas sont uniques pour chaque Canvas et peuvent être utilisés pour référencer des Canvas via l’API. 

Gardez à l'esprit que si vous avez un canvas avec des variantes, il existe un ID global pour le canvas ainsi que des ID individuels pour les variantes, imbriqués dans le canvas principal. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de Canvas dans le tableau de bord. Allez dans **Messagerie** > **Canvas** et sélectionnez un Canvas préexistant. Si le Canvas que vous voulez n’existe pas encore, créez-en un et enregistrez-le. En bas d'une page individuelle de Canvas, cliquez sur **Analyser variantes**. Une fenêtre apparaît avec l’identifiant de l’API de Canvas situé en bas.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), **Canvas** se trouve sous **Engagement**.
{% endalert %}

### À quoi cela sert-il ?

- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances du Canvas
- Obtenir des informations sur un Canvas spécifique
- Avec Currents pour apporter des données au niveau de l'utilisateur pour une approche plus globale de Canvases.
- Avec la livraison déclenchée par API afin de collecter des statistiques pour les messages transactionnels

## Identifiant de campagne

Un identifiant de [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou ID de campagne est une clé aléatoire générée par Braze pour une campagne donnée dans le tableau de bord. Les ID de campagne sont uniques pour chaque campagne et peuvent être utilisés pour référencer des campagnes via l’API. 

Gardez à l'esprit que si vous avez une campagne avec des variantes, il y a à la fois un ID de campagne global et des ID de campagne de variante individuels imbriqués sous la campagne principale. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de campagne de deux manières :

{% tabs local %}
{% tab Campagnes %}
Allez dans **Envoi de messages** > **Campagnes** et sélectionnez une campagne préexistante. Si la campagne que vous souhaitez n’existe pas encore, créez-en une et enregistrez-la. Au bas de la page de la campagne individuelle, vous pourrez trouver votre **identifiant API de campagne.**

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), les **campagnes** se trouvent sous **Engagement**.
{% endalert %}
{% endtab %}

{% tab Clés API %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), les **clés API** sont situées dans **Developer Console** > **API Settings.**
{% endalert %}
{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances de la campagne
- Obtenir des informations sur une campagne spécifique
- Avec Currents pour apporter des données au niveau utilisateur pour bénéficier d’un « tableau général » des campagnes
- Avec la livraison déclenchée par API afin de collecter des statistiques pour les messages transactionnels
- Pour [rechercher une campagne spécifique]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) sur la page **Campagnes** à l'aide du filtre `api_id:YOUR_API_ID`

## Identifiant de segment

Un identifiant de [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) ou ID de segment est une clé aléatoire générée par Braze pour un segment donné au sein du tableau de bord. Les ID de segment sont uniques pour chaque segment et peuvent être utilisés pour référencer les segments via l’API. 

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de segment de deux manières :

{% tabs local %}
{% tab Segmentations %}
Allez dans **Audience** > **Segments** et sélectionnez un segment préexistant. Si le segment que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page du segment individuel, vous trouverez votre identifiant de segment.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), les **segments se** trouvent sous **Engagement**.
{% endalert %}
{% endtab %}

{% tab Clés API %}
Cliquez sur **Paramètres** > \*\***API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), les **clés API** sont situées dans **Developer Console** > **API Settings.**
{% endalert %}
{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?
- Obtenir des informations sur un segment spécifique
- Récupérer l’analyse d’un segment spécifique
- Récupérer le nombre de fois où un événement personnalisé a été enregistré pour un segment particulier
- Spécifier et envoyer une campagne à un membre d’un segment depuis l’API

## Identifiant de carte

Un identifiant de carte ou ID de carte est une clé générée aléatoirement générée par Braze pour une carte de fil d’actualité donnée dans le tableau de bord. Les ID des cartes sont uniques à chaque carte de [fil d'actualité]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) et peuvent être utilisés pour référencer les cartes par le biais de l'API. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

### Où puis-je le trouver ?

Vous pouvez trouver votre ID de carte de deux manières :

{% tabs local %}
{% tab Fil d'actualité %}
Allez dans **Envoi de messages** > **Fil d'actualité** et sélectionnez un fil d'actualité préexistant. Si le fil d’actualité que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page du fil d’actualité individuel, vous trouverez votre identifiant unique de carte.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), le **fil d'actualité** se trouve sous **Engagement**.
{% endalert %}
{% endtab %}

{% tab Clés API %}
Allez dans **Paramètres** > **API et identifiants**. Ici, Braze propose une recherche d'**identifiants d'API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), les **clés API** sont situées dans **Developer Console** > **API Settings.**
{% endalert %}
{% endtab %}
{% endtabs %}

### À quoi cela sert-il ?

- Récupérer les informations pertinentes sur une carte
- Suivre les événements liés aux cartes de contenu et à l’engagement

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
