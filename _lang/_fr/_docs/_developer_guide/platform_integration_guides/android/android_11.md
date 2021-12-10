---
nav_title: Guide de mise à jour d'Android 11
article_title: Guide de mise à jour d'Android 11
page_order: 9
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la mise à jour du SDK Android 11, mettant en évidence des changements tels que le lien profond, la compatibilité SDK, et plus encore."
hidden: vrai
---

# Guide de mise à jour pour Android 11 SDK

Ce guide décrit les changements pertinents introduits dans Android 11 (publié le 8 septembre 2020) et les étapes de mise à jour requises pour votre intégration à Braze Android SDK.

Pour un guide de migration complet d'Android 11, consultez la [Documentation pour les développeurs Android](https://developer.android.com/preview/migration).

## Compatibilité avec Braze SDK

Toutes les applications _ciblant_ Android 11 (API 30) doivent passer à [Braze Android SDK v8. .0+][1] afin de continuer à utiliser les fonctions de messagerie de Braze.

{% alert important %}
En raison des changements dans les API d'Android 11, les applications ciblant Android 11 qui ne passent pas à Braze Android SDK v8.1. + rencontrera des problèmes avec les liens profonds depuis les composants de Braze UI et n'affichera pas correctement les messages HTML personnalisés dans l'application.
{% endalert %}

### Liens profonds

Les applications ciblant Android 11 ou supérieur (API Version 30+) doivent passer à [Braze Android SDK v8. .0][1] pour continuer à utiliser des liens profonds dans les messages de Braze. En raison d'un changement dans les API Android 11, les applications qui ne sont pas mises à niveau vers au moins Android SDK v8.1. rencontrera des problèmes avec des liens profonds dans les messages Braze (Messages In-App ou Cartes de Contenu).

### Messages HTML dans l'application

Les applications ciblant Android 11 ou supérieur (API Version 30+) doivent passer à Braze Android SDK v8.1.0 pour continuer à utiliser les messages personnalisés HTML In-App. En raison d'un changement dans les paramètres de WebView d'Android 11, Les messages HTML In-App ne s'afficheront pas correctement sur les applications Android 11 avant la mise à niveau vers [Braze Android SDK v8. .0][1].

### Autorisations de localisation

Les applications utilisant les autorisations de localisation doivent suivre les [meilleures pratiques](https://developer.android.com/preview/privacy/location#change-details) d'Android lors de la demande d'accès à la localisation. Aucune modification de votre intégration Braze n'est nécessaire pour ces mises à jour de localisation.

## Changements de comportement d'Android 11

### Autoriser une fois les autorisations

Les utilisateurs peuvent désormais accorder des autorisations, telles que la collecte de localisation, sur une base unique (voir les [Docs Android](https://developer.android.com/preview/privacy/location#one-time-access) pour plus d'informations). Une fois qu'une application est fermée, ou en arrière-plan assez longtemps, cette autorisation sera automatiquement révoquée. L'application devra demander à nouveau cette autorisation si nécessaire dans le futur. Les applications qui suivent déjà le flux recommandé pour demander des autorisations de localisation prendront déjà en charge les autorisations ponctuelles.

!\[Android Allow Once Permission\]\[3\]{: height="230px" }

### Autorisation d'accès à l'emplacement de l'arrière-plan

Android 11 nécessitera que les applications demandent d'abord l'autorisation de localisation en premier plan, puis après que l'application est en arrière-plan, il peut demander à nouveau à l'utilisateur l'autorisation d'emplacement en arrière-plan. Les clients qui utilisent Geofences doivent s'assurer que leur application suit les recommandations d'Android sur la collecte des autorisations de localisation en arrière-plan. Pour plus d'informations, voir la [documentation Android](https://developer.android.com/preview/privacy/location#background-location).
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#810

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#810
