---
nav_title: Badges
article_title: Compte des badges de notification Push pour iOS
platform: Swift
page_order: 2
description: "Cet article traite de l’implémentation du décompte des badges iOS pour le SDK Swift."
channel:
  - push

---

# Badges

> Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. Vous pouvez spécifier un nombre de badges dans la rubrique [**Paramètres**]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/) lorsque vous composez une notification push à l'aide du tableau de bord de Braze. Vous pouvez également mettre à jour le nombre de badges manuellement par l'intermédiaire de la propriété [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) de votre application ou par le biais de la [notification à distance](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

Braze efface automatiquement le décompte des badges lorsqu'une notification Braze est reçue alors que l'application est au premier plan. Le fait de régler manuellement le numéro de badge sur 0 permet également d'effacer les notifications dans le centre de notification. 

Si vous n’avez pas planifié une stratégie pour effacer les badges dans le cadre du fonctionnement normal de l’application ou en envoyant des notifications push qui effacent le badge, vous devez effacer le badge lorsque l’application devient active en ajoutant le code suivant à la méthode de délégation`applicationDidBecomeActive:` de votre application :

{% tabs %}
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
{% endtabs %}

