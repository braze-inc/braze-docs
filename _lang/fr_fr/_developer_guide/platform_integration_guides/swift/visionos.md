---
nav_title: Support de visionOS
article_title: Support de visionOS
page_order: 7.2
platform: 
  - iOS
description: "Cet article aborde les fonctionnalités prises en charge sur visionOS."
---

# Support de visionOS

> À partir de la version [8.0.0 du SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), vous pouvez utiliser Braze avec [visionOS](https://developer.apple.com/visionos/), la plateforme de calcul spatial d'Apple pour l'Apple Vision Pro. Pour connaître un exemple d'application visionOS utilisant Braze, voir [Exemples d'applications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/).

## Fonctionnalités entièrement prises en charge

La plupart des fonctionnalités disponibles sur iOS sont également disponibles sur visionOS, notamment :

- Analyse/analytique (sessions, événements personnalisés, achats, etc.)
- Envoi de messages in-app (modèles de données et interface utilisateur)
- Cartes de contenu (modèles de données et interface utilisateur)
- Notifications push (visibles par l'utilisateur grâce à des boutons d'action et à des notifications silencieuses)
- Indicateurs de fonctionnalité
- Analyse des localisations

## Fonctionnalités partiellement prises en charge

Certaines fonctionnalités ne sont que partiellement prises en charge sur visionOS, mais Apple devrait y remédier à l'avenir :

- Rich Push Notifications
  - Les images sont prises en charge.
  - Les GIF et les vidéos affichent la vignette de prévisualisation, mais ne peuvent pas être lus.
  - La lecture audio n'est pas prise en charge.
- Contenu push
  - Le défilement et la sélection de la page "Push Story" sont pris en charge.
  - La navigation entre les pages de Push Story à l'aide de **Next** n'est pas prise en charge.

## Fonctions non prises en charge

- La surveillance des géorepérages n'est pas prise en charge. Apple n'a pas mis à disposition sous visionOS les API de localisation de base pour la surveillance des régions.
- Les activités en ligne/instantanées ne sont pas prises en charge. Actuellement, ActivityKit n'est disponible que sur iOS et iPadOS.
