---
nav_title: "Types d’identifiant API"
article_title: Types d’identifiant API
page_order: 2.2
description: "Cet article de référence couvre les différents types d’identifiants API qui existent dans le tableau de bord de Braze, où vous pouvez les trouver et ce à quoi ils servent. 
page_type: reference

---

# Types d’identifiant API

> Ce guide de référence aborde les différents types d’identifiants API que vous trouverez dans le tableau de bord de Braze, leur but, où vous pouvez les trouver et comment ils sont généralement utilisés. Pour plus d’informations sur les clés API REST ou les clés API du groupe d’apps, reportez-vous à la [présentation de la clé API Rest]({{site.baseurl}}/api/api_key/)

Les identifiants suivants peuvent être utilisés pour accéder à votre modèle, Canvas, campagne, segment, envoi ou carte depuis l’API externe de Braze. Tous les messages doivent suivre le codage [UTF-8][1].

{% tabs %}
{% tab App Ids %}

## L’identifiant de l’application

L’identifiant de l’application ou `app_id` est un paramètre associant une activité à une application spécifique dans votre groupe d’apps. Il désigne l’application dans le groupe d’apps que vous utilisez. Par exemple, vous pouvez avoir un `app_id` pour votre application iOS, un `app_id` pour votre application Android et un `app_id` pour votre intégration Web. Chez Braze, il se peut que vous disposiez de plusieurs applications pour la même plateforme sur les différents types de plateformes que Braze prend en charge.

#### Où puis-je le trouver ?

Il existe deux façons de localiser votre `app_id`:

1. Vous pouvez trouver ce `app_id` ou identifiant d’application dans la **Developer Console (Console du développeur)**, sous **Settings (Paramètres)**. Sur cette nouvelle page, dans **Identification**, vous pourrez voir tous les `app_id` qui existent pour vos applications.
2. Accédez à **Manage Settings (Gérer les paramètres)** dans **Settings (Paramètres)**. Depuis cette nouvelle page, dans l’onglet **Settings (Paramètres)**, au milieu de la page, vous trouverez une « clé API pour **NOM DE L’APPLICATION** sur **PLATEFORME** » (par ex. « clé API Key pour Ice Cream sur iOS). Cette clé API est l’identifiant de votre application.

#### À quoi cela sert-il ?

Les identifiants d’application chez Braze sont utilisés lors de l’intégration du SDK et pour référencer une application spécifique dans les appels API REST. Avec le `app_id` vous pouvez faire de nombreuses choses comme extraire des données pour un événement personnalisé qui s’est produit pour une application particulière, récupérer les statistiques de désinstallation, les statistiques de nouveaux utilisateurs, les statistiques d’utilisateur actif quotidien et les statistiques de début de session pour une application particulière.

{% alert note %}
Parfois, vous pouvez être invité à renseigner un `app_id` alors que vous ne travaillez pas avec une application, car il s’agit d’un champ hérité d’une plateforme spécifique. Vous pouvez « omettre » ce champ en incluant une chaîne de caractères comme marque substitutive pour ce paramètre requis.
{% endalert %}

#### Identifiants d’application multiples

Lors de la configuration du SDK, le cas d’usage le plus fréquent avec les identifiants d’application multiples est de séparer ces identifiants entre les variantes de version de débogage et de publication.
Pour basculer facilement entre plusieurs identifiants d’application dans vos versions, nous vous recommandons de créer un fichier `braze.xml` pour chaque [variante de version][3]. Une variante de version est une combinaison du type de version et de la variété du produit. Remarquez que par défaut, un nouveau projet Android est configuré avec les types de version `debug` et `release`, et aucune variété de produit.

Pour chaque variante de version pertinente, créez un nouveau `braze.xml` pour elle dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```
Lorsque la variante de version est compilée, elle utilisera le nouvel identifiant.

{% endtab %}
{% tab Template Ids %}

## Identifiant du modèle

Un identifiant de [modèle]({{site.baseurl}}/api/endpoints/templates/) ou ID modèle est une clé générée aléatoirement générée par Braze pour un modèle donné dans le tableau de bord. Les ID de modèle sont uniques pour chaque modèle et peuvent être utilisés pour référencer les modèles via l’API. 

Les modèles sont parfaits si votre entreprise établit des contrats sur vos conceptions HTML pour les campagnes. Une fois les modèles construits, vous disposez d’un modèle qui n’est pas spécifique à une campagne, mais qui peut être appliqué à une série de campagnes, comme un bulletin d’information.

#### Où puis-je le trouver ?
Vous pouvez trouver votre ID de modèle de deux manières :

1. Dans le tableau de bord, ouvrez **Templates & Media (Modèles et médias)** dans **Engagement** et sélectionnez un modèle préexistant. Si le modèle que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page de modèle individuel, vous trouverez votre identifiant de modèle.<br><br>
2. Braze propose une recherche des **identifiants API supplémentaires**. Vous pouvez rapidement y rechercher des identifiants spécifiques. Elle se trouve au bas de l’onglet **API Settings (Paramètres API)** sur la page **Developer Console (Console du développeur)**.

#### À quoi cela sert-il ?

- Mettre à jour les modèles sur API
- Saisir des informations sur un modèle spécifique

<br>
{% endtab %}
{% tab Canvas IDs %}

## Identifiant Canvas

Un identifiant [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) ou ID Canvas est une clé générée aléatoirement générée par Braze pour un Canvas donné dans le tableau de bord. Les ID de Canvas sont uniques pour chaque Canvas et peuvent être utilisés pour référencer des Canvas via l’API. 

Notez que si vous disposez d’un Canvas qui comporte des variantes, il existe un ID de Canvas global ainsi que des ID de Canvas pour chaque variante individuelle, imbriqués dans le Canvas principal. 

#### Où puis-je le trouver ?
Vous pouvez trouver votre ID de Canvas dans le tableau de bord. Ouvrez **Canvas** dans **Engagement** et sélectionnez un Canvas préexistant. Si le Canvas que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas d’une page Canvas distincte, cliquez sur **Analyze Variants (Analyser les variantes)**. Une fenêtre apparaît avec l’identifiant de l’API de Canvas situé en bas.

#### À quoi cela sert-il ?
- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances du Canvas
- Obtenir des informations sur un Canvas spécifique
- Avec Currents pour apporter des données au niveau utilisateur pour bénéficier d’un « tableau général » des Canvas
- Avec la livraison déclenchée par API afin de collecter des statistiques pour les messages transactionnels

<br>
{% endtab %}
{% tab Campaign IDs %}

## Identifiant de campagne

Un identifiant de [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou ID de campagne est une clé générée aléatoirement générée par Braze pour une campagne donnée dans le tableau de bord. Les ID de campagne sont uniques pour chaque campagne et peuvent être utilisés pour référencer des campagnes via l’API. 

Notez que si vous disposez d’une campagne qui comporte des variantes, il existe un ID de campagne global ainsi que des ID de campagne aux variantes distinctes imbriqués dans la campagne principale. 

#### Où puis-je le trouver ?
Vous pouvez trouver votre ID de campagne de deux manières :

1. Dans le tableau de bord, ouvrez **Campagnes** dans **Engagement** et sélectionnez une campagne préexistante. Si la campagne que vous souhaitez n’existe pas encore, créez-en une et enregistrez-la. Au bas de la page de campagne individuelle, vous trouverez votre **identifiant API de campagne**.<br><br>
2. Braze propose une recherche des **identifiants API supplémentaires**. Vous pouvez rapidement y rechercher des identifiants spécifiques. Vous pouvez la trouver au bas de l’onglet **API Settings (Paramètres API)** dans la **Developer Console (Console du développeur)**.

#### À quoi cela sert-il ?
- Suivre l’analyse d’un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances de la campagne
- Obtenir des informations sur une campagne spécifique
- Avec Currents pour apporter des données au niveau utilisateur pour bénéficier d’un « tableau général » des campagnes
- Avec la livraison déclenchée par API afin de collecter des statistiques pour les messages transactionnels
- Pour [rechercher une campagne spécifique]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) sur la page **Campaigns** en utilisant le filtre `api_id:YOUR_API_ID`

<br>
{% endtab %}
{% tab Segment IDs %}

## Identifiant de segment

Un identifiant de [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) ou ID de segment est une clé générée aléatoirement générée par Braze pour un segment donné dans le tableau de bord. Les ID de segment sont uniques pour chaque segment et peuvent être utilisés pour référencer les segments via l’API. 

#### Où puis-je le trouver ?
Vous pouvez trouver votre ID de segment de deux manières :

1. Dans le tableau de bord, ouvrez **Segments** dans **Engagement** et sélectionnez un segment préexistant. Si le segment que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page du segment individuel, vous trouverez votre identifiant de segment. <br><br>
2. Braze propose une recherche des **identifiants API supplémentaires**. Vous pouvez rapidement y rechercher des identifiants spécifiques. Elle se trouve au bas de l’onglet **API Settings (Paramètres API)** sur la page **Developer Console (Console du développeur)**.

#### À quoi cela sert-il ?
- Obtenir des informations sur un segment spécifique
- Récupérer l’analyse d’un segment spécifique
- Récupérer le nombre de fois où un événement personnalisé a été enregistré pour un segment particulier
- Spécifier et envoyer une campagne à un membre d’un segment depuis l’API

{% endtab %}
{% tab Card IDs %}

## Identifiant de carte

Un identifiant de carte ou ID de carte est une clé générée aléatoirement générée par Braze pour une carte de fil d’actualité donnée dans le tableau de bord. Les ID de carte sont uniques pour chaque carte de [fil d’actualité]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) et peuvent être utilisés pour référencer les cartes via l’API. 

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

#### Où puis-je le trouver ?
Vous pouvez trouver votre ID de carte de deux manières :

1. Dans le tableau de bord, ouvrez **Fil d’actualité** dans **Engagement** et sélectionnez un fil d’actualité préexistant. Si le fil d’actualité que vous voulez n’existe pas encore, créez-en un et enregistrez-le. Au bas de la page du fil d’actualité individuel, vous trouverez votre identifiant unique de carte. <br><br>
2. Braze propose une recherche des **identifiants API supplémentaires**. Vous pouvez rapidement y rechercher des identifiants spécifiques. Elle se trouve au bas de l’onglet **API Settings (Paramètres API)** sur la page **Developer Console (Console du développeur)**.

#### À quoi cela sert-il ?
- Récupérer les informations pertinentes sur une carte
- Suivre les événements liés aux cartes de contenu et à l’engagement

<br>
{% endtab %}
{% tab Send IDs %}

## Identifiant d’envoi

Un identifiant d’envoi ou ID d’envoi est une clé générée par Braze ou créée par vous pour un message donné et envoyé dans le cadre duquel l’analyse doit être suivie. L’identifiant d’envoi vous permet de récupérer des analyses pour une instance spécifique d’une campagne envoyée via l’endpoint [`sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/).

#### Où puis-je le trouver ?

Les API et campagnes déclenchées par API qui sont envoyées en tant que diffusion génèrent automatiquement un identifiant d’envoi si un identifiant d’envoi n’est pas fourni. Si vous souhaitez spécifier votre propre identifiant d’envoi, vous devrez d’abord en créer un via l’endpoint [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/). L’identifiant ne peut comporter que des caractères ASCII et ne peut faire plus de 64 caractères. Vous pouvez réutiliser un identifiant d’envoi sur plusieurs envois de la même campagne si vous souhaitez regrouper les analyses de ces envois.

#### À quoi cela sert-il ?
Envoyer et suivre par programme les performances des messages, sans création de campagne pour chaque envoi.

<br>
{% endtab %}
{% endtabs %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[3]: https://developer.android.com/studio/build/build-variants.html
