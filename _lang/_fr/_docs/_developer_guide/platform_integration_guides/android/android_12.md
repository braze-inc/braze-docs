---
nav_title: Guide de mise à jour d'Android 12
article_title: Guide de mise à jour d'Android 12
page_order: 9
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la mise à jour d'Android 12 SDK, mettant en évidence des changements tels que le lien profond, la compatibilité SDK, et plus encore."
---

# Guide de mise à jour d'Android 12 SDK

Ce guide décrit les changements pertinents introduits dans Android 12 (2021) et les étapes nécessaires à la mise à jour de votre intégration à Braze Android SDK.

Pour un guide de migration complet d'Android 12, voir la [Documentation pour les développeurs Android](https://developer.android.com/about/versions/12).

## Compatibilité avec Braze SDK

Si vous visez Android 12, vous devez utiliser [Braze Android SDK v13.1.2+][1]. Si vous ne ciblez pas encore Android 12, la mise à jour est toujours recommandée.

**Que se passe-t-il si je ne fais pas la mise à jour de mon Braze Android SDK ?**

* En raison d'un changement dans les [Fermetures des boîtes de dialogue du système Android](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs), les anciennes versions du Braze Android SDK enregistreront les avertissements lorsque vous recevrez des notifications push sur les appareils fonctionnant sous Android 12. Ce comportement se produit même si votre application ne cible pas Android 12.
* Changements dans [exports de composants](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [intentions en attente](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability), [les trampolines de notification](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) peuvent affecter votre capacité à compiler votre application, ou peuvent empêcher le SDK de Braze d'initialiser. Ce comportement se produit uniquement pour les applications ciblant Android 12.
* Les changements dans [notifications push personnalisées](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) ont modifié la mise en page de notre nouvelle fonctionnalité [Push d'image en ligne d'Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/). Ce comportement se produit uniquement pour les applications ciblant Android 12.

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312
