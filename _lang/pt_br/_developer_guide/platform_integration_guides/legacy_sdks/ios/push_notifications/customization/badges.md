---
nav_title: Emblemas
article_title: Contagens de emblemas de notificação por push para iOS
platform: iOS
page_order: 3.1
description: "Este artigo de referência aborda como implementar contagens de emblemas em suas notificações por push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Emblemas

Você pode especificar a contagem de emblemas desejada ao compor uma notificação por push através do dashboard do Braze. Você também pode atualizar a contagem de seu emblema manualmente através da propriedade [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) do seu aplicativo ou da [carga útil de notificação remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). A Braze também zerará a contagem de emblemas quando uma notificação da Braze for recebida enquanto o app estiver em primeiro plano. 

Se você não tiver um plano para limpar os badges como parte da operação normal do app ou enviando notificações que limpam o badge, você deve limpar o badge quando o app se tornar ativo adicionando o seguinte código ao método de delegado do seu app `applicationDidBecomeActive:`:

{% tabs %}
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

Vale lembrar que zerar o número de emblemas também limpará as notificações na central de notificações. Portanto, mesmo que você não defina o número do badge nas cargas úteis de push, ainda poderá definir o número do badge como 0 para remover a(s) notificação(ões) por push na central de notificações após os usuários clicarem no push.

