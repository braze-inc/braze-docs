---
nav_title: Guide de mise à niveau vers Android 12
article_title: Guide de mise à niveau vers Android 12
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre la mise à jour du SDK pour Android 12, mettant en évidence des changements tels que la création de liens profonds, la compatibilité SDK, etc."
---

# Guide de mise à niveau du SDK pour Android 12

Ce guide décrit les modifications pertinentes introduites dans Android 12 (2021) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Pour obtenir un guide complet de migration vers Android 12, consultez la [documentation du développeur Android](https://developer.android.com/about/versions/12).

## Compatibilité du SDK Braze

Si vous ciblez Android 12, vous devez utiliser le [SDK Android de Braze v13.1.2+][1]. Si vous ne ciblez pas encore Android 12, la mise à niveau est recommandée quand même.

**Que se passe-t-il si je ne mets pas à jour mon SDK Android Braze ?**

* En raison d'une modification des [dialogues du système de fermeture d'](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs)Android, les anciennes versions du SDK Android de Braze enregistreront des avertissements lors de la réception de notifications push sur les appareils fonctionnant sous Android 12. Ce comportement se produit même si votre application ne cible pas Android 12.
* Les modifications apportées aux [exportations de composants](https://developer.android.com/about/versions/12/behavior-changes-12#exported), aux [intentions en attente](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) et aux [trampolines de notification](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) peuvent avoir un impact sur votre capacité à compiler votre application ou empêcher le SDK de Braze de s'initialiser. Ce comportement se produit uniquement pour les applications ayant un ciblage Android 12.
* Les modifications apportées aux [notifications push personnalisées](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) ont changé la présentation de notre nouvelle fonctionnalité de [push d'images en ligne pour Android.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/)  Ce comportement se produit uniquement pour les applications ayant un ciblage Android 12.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
