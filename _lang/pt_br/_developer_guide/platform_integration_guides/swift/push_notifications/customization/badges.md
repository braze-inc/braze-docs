---
nav_title: Emblemas
article_title: Contagem de emblemas de notificações por push para iOS
platform: Swift
page_order: 2
description: "Este artigo aborda como implementar a contagem de ícones do iOS para o Swift SDK."
channel:
  - push

---

# Ícones

> Os emblemas são ícones pequenos, ideais para chamar a atenção do usuário. Você pode especificar uma contagem de crachás nas [**Configurações**]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/) ao criar uma notificação por push usando o dashboard do Braze. Você também pode atualizar a contagem de emblemas manualmente por meio da propriedade [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) do aplicativo ou da [carga útil da notificação remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

O Braze limpará automaticamente a contagem de emblemas quando uma notificação do Braze for recebida enquanto o app estiver em primeiro plano. A configuração manual do número do crachá como 0 também limpará as notificações na central de notificações. 

Se você não tiver um plano para limpar os crachás como parte da operação normal do aplicativo ou enviando pushs que limpem o crachá, deverá limpar o crachá quando o aplicativo se tornar ativo, adicionando o seguinte código ao método delegado `applicationDidBecomeActive:` do seu aplicativo:

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
{% tab OBJECTIVE C %}

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

