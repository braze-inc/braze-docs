---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização para iOS
platform: iOS
page_order: 6
description: "Este artigo mostra como configurar o monitoramento de localização para seu aplicativo iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Monitoramento de localização para iOS

Por padrão, a Braze desativa o monitoramento de localização. Ativamos o monitoramento de localização depois que o aplicativo host aceita o rastreamento de localização e obtém permissão do usuário. Desde que os usuários tenham aceitado o monitoramento de localização, o Braze registrará um único local para cada usuário no início da sessão.

{% alert important %}
Para que o monitoramento de localização funcione de forma confiável no iOS 14 para usuários que dão permissão de localização aproximada, é necessário atualizar a versão do SDK para, pelo menos, `3.26.1`.
{% endalert %}

## Ativação do monitoramento automático de localização

A partir do SDK da Braze para iOS `v3.17.0`, o monitoramento de localização é desativado por padrão. É possível ativar o monitoramento automático de localização usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada booleana `EnableAutomaticLocationCollection` e defina o valor como `YES`. Note que, antes do SDK da Braze para iOS v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.

Você também pode ativar o monitoramento automático de localização no momento da inicialização do app por meio do método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) método. No dicionário `appboyOptions`, defina `ABKEnableAutomaticLocationCollectionKey` como `YES`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableAutomaticLocationCollectionKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableAutomaticLocationCollectionKey : true ])
```

{% endtab %}
{% endtabs %}

### Passagem de dados de localização para a Braze

Os dois métodos a seguir podem ser usados para definir manualmente o último local conhecido do usuário.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy];

```

```objc
[[Appboy sharedInstance].user setLastKnownLocationWithLatitude:latitude
                                                     longitude:longitude
                                            horizontalAccuracy:horizontalAccuracy
                                                      altitude:altitude
                                              verticalAccuracy:verticalAccuracy];

```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy)
```

```swift
Appboy.sharedInstance()?.user.setLastKnownLocationWithLatitude(latitude: latitude, longitude: longitude, horizontalAccuracy: horizontalAccuracy, altitude: altitude, verticalAccuracy: verticalAccuracy)
```

{% endtab %}
{% endtabs %}

Consulte [`ABKUser.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKUser.h) Para saber mais.

