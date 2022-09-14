---
nav_title: Guide de mise à niveau iOS 16
article_title: Guide de mise à niveau iOS 16
page_order: 7
platform: 
  - iOS
description: "Cet article couvre iOS 16, les mises à jour SDK, etc."
---

# Guide de mise à jour SDK iOS 16

Ce guide décrit les modifications pertinentes introduites dans iOS 16 (2022) et leur impact sur votre intégration SDK Braze pour iOS. Pour un guide de migration complet, reportez-vous aux [Notes de mise à jour iOS 16][2].

{% alert note %}
iOS 16 est toujours en version bêta. Vérifiez régulièrement, car les API Apple peuvent changer avec les versions bêta futures.<br>
(Mis à jour le 22 juin 2022)
{% endalert %}

## Modifications dans iOS 16

À partir d’iOS 16 Beta 2, aucune modification fonctionnelle ayant affecté votre intégration SDK Braze n’a été apportée à iOS 16. Cela peut changer à mesure qu’Apple publie de nouvelles versions bêta d’iOS 16, alors revenez régulièrement ici pour vérifier.

### Notifications push pour Safari Web {#safari-web-push}

Apple a annoncé deux changements de sa fonctionnalité Push Web.

#### Desktop Web Push (macOS) {#macos-push}

Auparavant, Apple prenait en charge les notifications push sur macOS (desktop) en utilisant leurs propres API Push Safari.

À partir de macOS Ventura, [ajoutera la prise en charge](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) des API Push Web en plus de Safari Push. Il s’agit d’une norme d’API multi-navigateurs existante utilisée par d’autres navigateurs de renom.

Si vous envoyez déjà des notifications push Web pour Safari via Braze, aucune modification n’est nécessaire.

#### Mobile Web Push (iOS et iPadOS) {#iOS-push}

Auparavant, Safari sur iPhone et iPad ne prenait pas en charge la réception de notifications push.

En 2023, Apple ajoutera sa prise en charge pour les périphériques iPhone et iPad sur Internet via Safari.

Braze prendra en charge ces nouvelles notifications push pour iOS et iPadOS sans nécessiter de modifications ou de mises à niveau supplémentaires.

## Préparation pour iOS 16 {#next-steps}

Sur la base de la bêta iOS actuelle, vous n’aurez pas besoin de mettre à niveau votre SDK Braze pour iOS. Cependant, il existe deux autres formidables mises à jour :

1. Braze a lancé un [nouveau SDK Swift][3]. Il améliore les performances, dispose de nouvelles fonctionnalités et de nombreuses améliorations.
2. Notre SDK Braze Swift va bientôt prendre en charge une nouvelle [fonction de base de notification push « sans code »][7] !

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md
[3]: https://github.com/braze-inc/braze-swift-sdk
[2]: https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes
[7]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/push_primer_messages/
