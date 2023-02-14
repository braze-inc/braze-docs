---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Roku
platform: Roku
page_order: 0
page_type: reference
description: "Cette page décrit les étapes de configuration initiales du SDK Roku de Braze"
search_rank: 1
---

# Intégration initiale du SDK Roku

L’installation du SDK Roku de Braze vous fournira des fonctionnalités d’analyse et de segmentation basiques.

## Étape 1 : Ajouter des fichiers

Les fichiers SDK Braze sont disponibles dans le répertoire `sdk_files` dans le [référentiel de SDK Roku de Braze.][1].

1. Ajouter `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajouter `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

## Étape 2 : Ajouter des références

Ajouter une référence à `BrazeSDK.brs` dans votre scène principale, en utilisant l’élément `script` :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Étape 3 : Configurer

Dans `main.brs`, définissez la configuration Braze sur le nœud global :

```
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Vous pouvez trouver votre clé [Endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) et API dans le tableau de bord de Braze.

## Étape 4 : Initialiser Braze

Initialiser l’instance Braze :

```
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Activer la journalisation (facultatif) {#logging}

Pour déboguer votre intégration Braze, vous pouvez afficher la console de débogage Roku pour les journaux Braze. Consulter le [Code de débogage](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de Roku Developers pour en savoir plus.

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application avec le SDK Roku de Braze. 

Consultez les articles suivants concernant la manière de [journaliser des attributs][2], des [événements][3] et des [achats][4] sur notre SDK.

Pour en savoir plus sur la messagerie in-app de Roku, consultez notre [guide d’intégration des messages in-app][5].


[1]: https://github.com/braze-inc/braze-roku-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
