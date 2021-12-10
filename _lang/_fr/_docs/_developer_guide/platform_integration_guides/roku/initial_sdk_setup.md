---
nav_title: Configuration initiale du SDK
article_title: Configuration initiale du SDK pour Roku
platform: Roku
page_order: 0
page_type: Référence
description: "Cette page décrit les étapes initiales de l'installation du SDK Braze Roku."
---

# Intégration initiale de Roku SDK

L'installation du SDK Braze Roku vous fournira des fonctionnalités d'analyse et de segmentation de base.

## Étape 1 : Ajouter des fichiers

Les fichiers SDK Braze peuvent être trouvés dans le répertoire `sdk_files` dans le repo [Braze Roku SDK](https://github.com/Appboy/appboy-roku-sdk).

1. Ajoutez `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajoutez `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `composants`.

## Étape 2 : Ajouter des références

Ajouter une référence à `BrazeSDK.brs` dans votre scène principale en utilisant l'élément `script` suivant :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Étape 3 : Configurer

Dans `main.brs`, définissez la configuration de Braze sur le nœud global :

```
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
' exemple endpoint "https://sdk. ad-01.braze.com/"
config[config_fields.ENDPOINT] = "VOTRE_ENDPOINT_ICRE"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## Étape 4 : Initialiser Braze

Initialiser l'instance Braze :

```
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Intégration de base du SDK terminée

Braze devrait maintenant recueillir des données de votre application avec le Braze Roku SDK. Veuillez consulter les sections suivantes sur la façon de [enregistrer les attributs]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/), [événements]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)et [acheter]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/) à notre SDK.
