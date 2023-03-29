---
nav_title: Guide de mise à niveau iOS 16
article_title: Guide de mise à niveau iOS 16
page_order: 7
platform: 
  - iOS
description: "Cet article de référence couvre iOS 16, comment mettre à jour, les mises à jour SDK, etc."
---

# Guide de mise à jour SDK iOS 16

Ce guide décrit les modifications pertinentes introduites dans iOS 16 (2022) et leur impact sur votre intégration SDK Braze pour iOS. Pour un guide de migration complet, reportez-vous aux [Notes de mise à jour iOS 16][2].

## Modifications dans iOS 16

### Notifications Push Safari Web {#safari-web-push}

Apple a annoncé deux changements de sa fonctionnalité Push Web.

#### Notifications Push Desktop Web (MacOS) {#macos-push}

Auparavant, Apple prenait en charge les notifications push sur macOS (desktop) en utilisant leurs propres API Push Safari.

À partir de macOS Ventura (publiée le 24 octobre 2022), [ Safari a ajouté une assistance](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) pour les API de notifications push Web en plus des notifications push de Safari. Il s’agit d’une norme d’API multi-navigateurs existante utilisée par d’autres navigateurs de renom.

Si vous envoyez déjà des notifications push Web pour Safari via Braze, aucune modification n’est nécessaire.

#### Notification push Web Safari Mobile (iOS et iPadOS) {#ios-push}

Auparavant, Safari sur iPhone et iPad ne prenait pas en charge la réception de notifications push.

En 2023, Apple ajoutera sa prise en charge pour les appareils iPhone et iPad sur Internet via Safari.

Braze prendra en charge ces nouvelles notifications push pour iOS et iPadOS sans nécessiter de modifications ou de mises à niveau supplémentaires.

## Préparation pour iOS 16 {#next-steps}

Si vous ne souhaitez pas mettre à jour votre SDK iOS Braze pour iOS 16, voici deux mises à jour intéressantes :

1. Braze a lancé un [nouveau SDK Swift][3]. Il améliore les performances, dispose de nouvelles fonctionnalités et de nombreuses améliorations.
2. Notre Braze Swift SDK prendre en charge une nouvelle [fonction de base de notification push « sans code »][7] !

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md
[3]: https://github.com/braze-inc/braze-swift-sdk
[2]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
