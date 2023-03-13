---
nav_title: Guide de mise à niveau vers Android 12
article_title: Guide de mise à niveau vers Android 12
page_order: 9
hidden: true
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre la mise à jour du SDK pour Android 12, mettant en évidence des changements tels que la création de liens profonds, la compatibilité SDK, etc."
---

# Guide de mise à niveau du SDK pour Android 12

Ce guide décrit les modifications pertinentes introduites dans Android 12 (2021) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Pour un guide de migration complet vers Android 12, consultez la [documentation du développeur pour Android](https://developer.android.com/about/versions/12).

## Compatibilité du SDK Braze

Si vous utilisez Android 12, vous devez utiliser le [SDK Braze pour Android v13.1.2+][1]. Si vous ne ciblez pas encore Android 12, la mise à niveau est recommandée quand même.

**Que se passe-t-il si je ne mets pas à niveau mon SDK Braze pour Android ?**

* En raison d’un changement dans les [boîtes de dialogue du système de fermeture](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs) d’Android, les versions antérieures du SDK Braze pour Android enregistreront des avertissements lors de la réception de notifications push sur les périphériques fonctionnant sous Android 12. Ce comportement se produit même si votre application ne cible pas Android 12.
* Les modifications dans les [exportations de composants](https://developer.android.com/about/versions/12/behavior-changes-12#exported), les [intentions en attente](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) et les [notifications indirectes](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) peuvent avoir un impact sur votre capacité à compiler votre application ou empêcher le SDK Braze de s’initialiser. Ce comportement se produit uniquement pour les applications ayant un ciblage Android 12.
* Les modifications dans les [notifications push personnalisées](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) ont transformé la mise en page pour notre nouvelle fonction de [notification push d’image intégrée à Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/). Ce comportement se produit uniquement pour les applications ayant un ciblage Android 12.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
