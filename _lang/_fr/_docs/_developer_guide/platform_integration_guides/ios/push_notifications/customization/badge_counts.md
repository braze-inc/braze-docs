---
nav_title: Nombre de badges
article_title: Nombre de badges de notification push pour iOS
platform: iOS
page_order: 0.2
description: "Cet article couvre la façon d'implémenter le nombre de badges dans vos notifications push iOS."
channel:
  - Pousser
---

## Nombre de badges

Vous pouvez spécifier le nombre de badges désirés lorsque vous composez une notification push via le tableau de bord de Brase. Vous pouvez également mettre à jour manuellement votre nombre de badges via la propriété [`applicationIconBadgeNumber`][20] de votre application ou via la [charge utile de notification distante][21]. Braze effacera également le nombre de badges quand une notification Braze est reçue pendant que l'application est au premier plan. Si vous n'avez pas de plan pour effacer les badges dans le cadre de l'opération normale de l'application ou en envoyant des pushes qui effacent le badge, vous devriez effacer le badge lorsque l'application devient active en ajoutant le code suivant à l'application `de votre applicationDidBecomeActive:` méthode de déléguation :

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

Veuillez noter que la définition du numéro de badge à 0 effacera également les notifications dans le centre de notification. Donc, même si vous ne définissez pas de numéro de badge dans les bloc push, vous pouvez toujours définir le numéro de badge à 0 pour supprimer le(s) notification(s) push(s) dans le centre de notification après avoir cliqué sur le push.

[20]: https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber
[21]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1