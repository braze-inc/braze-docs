---
nav_title: Badges
article_title: Compte des badges de notification Push pour iOS
platform: iOS
page_order: 3.1
description: "Cet article de référence traite de la manière d’implémenter le compte des badges dans vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Badges

Vous pouvez spécifier le nombre de badges souhaité lorsque vous composez une notification push via le tableau de bord Braze. Vous pouvez également mettre à jour manuellement le nombre de vos badges via la propriété [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) de votre application ou la [charge utile de notification à distance](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). Braze efface également le nombre de badges lorsqu’une notification Braze est reçue pendant que l’application est au premier plan. 

Si vous n’avez pas planifié une stratégie pour effacer les badges dans le cadre du fonctionnement normal de l’application ou en envoyant des notifications push qui effacent le badge, vous devez effacer le badge lorsque l’application devient active en ajoutant le code suivant à la méthode de délégation`applicationDidBecomeActive:` de votre application :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Notez que définir le numéro de badge sur 0 effacera également les notifications dans le centre de notification. Ainsi, même si vous ne définissez pas de numéro de badge dans les charges utiles des notifications push, vous pouvez toujours définir le numéro de badge sur 0 pour supprimer la ou les notifications push dans le centre de notification après que les utilisateurs ont cliqué sur la notification.

