---
nav_title: Dépannage
article_title: Dépannage pour Xamarin
platform:
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "Cet article couvre le dépannage iOS et Android pour la plate-forme Xamarin."
---

# Dépannage

## Android

### Push n'apparaît pas après que l'application soit fermée à partir du sélecteur de tâches

Si vous constatez que les notifications push n'apparaissent plus après la fermeture de l'application à partir du sélecteur de tâches, votre application est probablement en mode débogage. Xamarin ajoute un échafaudage en mode Debug qui empêche les applications de recevoir des push après que leur processus ait été tué. Si vous exécutez votre application en mode Release (Release Mode), vous devriez voir push même après que l'application soit fermée à partir du sélecteur de tâches.

### La configuration d'usine de notification personnalisée n'est pas correcte

Les usines de notification personnalisées (et toutes les délégations) doivent étendre [`Java.Lang.Object`][2] pour fonctionner correctement à travers la fracture C#/Java. Voir la documentation [de Xamarin sur l'implémentation des interfaces Java][1] pour plus d'informations.

[1]: https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces
[2]: https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/
