---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Roku
platform: Roku
page_order: 0
page_type: reference
description: "Cette page décrit les étapes de configuration initiales du SDK Roku de Braze"
search_rank: 1
---

# Intégration SDK initiale

> Cet article de référence explique comment installer le SDK Braze pour Roku. L’installation du SDK Roku de Braze vous fournira des fonctionnalités d’analyse et de segmentation basiques.

{% alert tip %}
Consultez notre exemple d'application Roku sur GitHub : [TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv).
{% endalert %}

## Étape 1 : Ajouter des fichiers

Les fichiers du SDK Braze sont disponibles dans le répertoire `sdk_files` du [référentiel SDK Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Ajouter `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajouter `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

## Étape 2 : Ajouter des références

Ajouter une référence à `BrazeSDK.brs` dans votre scène principale, en utilisant l’élément `script` :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Étape 3 : Configurer

Dans `main.brs`, définissez la configuration Braze sur le nœud global :

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Vous trouverez votre [endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) et votre clé API dans le tableau de bord de Braze.

## Étape 4 : Initialiser Braze

Initialiser l’instance Braze :

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Activer la journalisation (facultatif) {#logging}

Pour déboguer votre intégration Braze, vous pouvez afficher la console de débogage Roku pour les journaux Braze. Pour en savoir plus, reportez-vous au [Code de débogage](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) des développeurs Roku.

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application avec le SDK Roku de Braze. 

Consultez les articles suivants pour savoir comment [enregistrer des attributs]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/), des [événements]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/) et des [achats]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/) dans notre SDK.

Pour en savoir plus sur l'envoi de messages in-app sur Roku, consultez notre [guide d'intégration des messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).


