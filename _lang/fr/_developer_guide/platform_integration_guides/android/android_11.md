---
nav_title: Guide de mise à niveau vers Android 11
article_title: Guide de mise à niveau vers Android 11
page_order: 9
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre la mise à niveau du SDK pour Android 11, mettant en évidence des changements tels que la création de liens profonds, la compatibilité SDK, etc."
hidden: true
---

# Guide de mise à niveau du SDK pour Android 11

Ce guide décrit les modifications pertinentes introduites dans Android 11 (publié le 8 septembre 2020) et les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android.

Pour un guide de migration complet vers Android 11, consultez la [documentation du développeur Android](https://developer.android.com/preview/migration).

## Compatibilité du SDK Braze

Toutes les applications qui _ciblent_ Android 11 (API 30) doivent être mises à niveau vers le [SDK Braze pour Android v8.1.0 et ultérieures][1] pour continuer à utiliser les fonctions de messagerie Braze.

{% alert important %}
En raison des modifications apportées aux API d’Android 11, les applications ayant un ciblage Android 11 qui ne sont pas mises à niveau vers le SDK Braze pour Android v8.1.0 et ultérieures rencontreront des problèmes avec la création de liens profonds des composants IU de Braze et n’afficheront pas correctement les messages in-app HTML personnalisés.
{% endalert %}

### Liens profonds

Les applications ayant un ciblage Android 11 ou une version ultérieure (API version 30 et ultérieures) doivent être mises à niveau vers le [SDK Braze pour Android v8.1.0][1] pour pouvoir continuer à utiliser des liens profonds dans les messages de Braze. En raison d’un changement dans les API Android 11, les applications qui ne sont pas mises à niveau vers le SDK pour Android v8.1.0 au moins rencontreront des problèmes avec les liens profonds dans les messages de Braze (messages in-app ou cartes de contenu).

### Messages in-app HTML

Les applications ayant un ciblage Android 11 ou une version ultérieure (API version 30 et ultérieures) doivent être mises à niveau vers le SDK Braze pour Android v8.1.0 pour continuer à utiliser des messages in-app HTML personnalisés. En raison d’un changement dans les paramètres WebView d’Android 11, les messages in-app HTML ne s’afficheront pas correctement sur les applications Android 11 ciblées et ce jusqu’à la mise à niveau vers le [SDK Braze pour Android v8.1.0][1]. 

### Autorisations de position

Les applications utilisant les autorisations de position doivent suivre les [meilleures pratiques](https://developer.android.com/preview/privacy/location#change-details) Android lors de la demande d’accès à l’emplacement. Aucune modification de votre intégration Braze n’est nécessaire pour ces mises à jour de position.

## Changements de comportement d’Android 11

### Permissions à autorisation unique

Les utilisateurs peuvent désormais accorder des autorisations, telles que la collecte de la position, sur une base ponctuelle (référez-vous aux [documents Android](https://developer.android.com/preview/privacy/location#one-time-access) pour plus d’informations). Une fois qu’une application est fermée ou en arrière-plan assez longtemps, cette autorisation sera révoquée automatiquement. L’application devra demander à nouveau cette autorisation lorsqu’elle en aura ultérieurement besoin. Les applications qui suivent déjà le flux recommandé pour la demande d’autorisations de position prennent en charge les autorisations ponctuelles.

![][3]{: height="230px" }

### Autorisation de position en arrière-plan

Android 11 exigera des applications qu’elles demandent d’abord l’autorisation de position en premier plan puis, une fois que l’application est en arrière-plan, elle peut demander à nouveau une autorisation de position en arrière-plan à l’utilisateur. 
Les clients utilisant des geofences doivent s’assurer que leur application respecte les recommandations d’Android concernant la collecte de l’autorisation de position en l’arrière-plan. Pour plus d’informations, référez-vous aux [documents Android](https://developer.android.com/preview/privacy/location#background-location).

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
