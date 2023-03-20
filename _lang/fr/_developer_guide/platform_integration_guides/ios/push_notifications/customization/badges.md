---
nav_title: Badges
article_title: Compte des badges de notification Push pour iOS
platform: iOS
page_order: 3.1
description: "Cet article de référence traite de la manière d’implémenter le compte des badges dans vos notifications push iOS."
channel:
  - Notification push

---

# Badges

Vous pouvez spécifier le nombre de badges souhaité lorsque vous rédigez une notification push via le tableau de bord de Braze. Vous pouvez également mettre manuellement à jour votre badge par l’intermédiaire de la propriété [`applicationIconBadgeNumber`][20] de votre application ou de la [charge utile de notification à distance][21]. Braze efface également le nombre de badges lorsqu’une notification Braze est reçue pendant que l’application est au premier plan. 

Si vous n’avez pas planifié une stratégie pour effacer les badges dans le cadre du fonctionnement normal de l’application ou en envoyant des notifications push qui effacent le badge, vous devez effacer le badge lorsque l’application devient active en ajoutant le code suivant à la méthode de délégation`applicationDidBecomeActive:` de votre application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Notez que définir le numéro de badge sur 0 effacera également les notifications dans le centre de notification. Ainsi, même si vous ne définissez pas de numéro de badge dans les charges utiles des notifications push, vous pouvez toujours définir le numéro de badge sur 0 pour supprimer la ou les notifications push dans le centre de notification après que les utilisateurs ont cliqué sur la notification.

[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1