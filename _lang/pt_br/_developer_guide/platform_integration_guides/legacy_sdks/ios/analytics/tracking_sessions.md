---
nav_title: Sessões de rastreamento
article_title: Sessões de rastreamento para iOS
platform: iOS
page_order: 0
description: "Este artigo de referência mostra como assinar atualizações de sessão para seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Rastreamento de sessão para iOS

O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que contabilizam a duração da sessão e a contagem de sessões visualizáveis no dashboard do Braze com base na seguinte semântica de sessão.

## Ciclo de vida da sessão

Uma sessão é iniciada quando você chama `[[Appboy sharedInstance]` `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions]`, após o que, por padrão, as sessões começam quando a notificação `UIApplicationWillEnterForegroundNotification` é disparada (por exemplo, quando o aplicativo entra em primeiro plano) e terminam quando o aplicativo sai do primeiro plano (por exemplo, quando a notificação `UIApplicationDidEnterBackgroundNotification` é disparada ou quando o aplicativo morre).

{% alert note %}
Se precisar forçar uma nova sessão, basta mudar de usuário.
{% endalert %}

## Personalização do tempo limite da sessão

A partir do SDK da Braze para iOS v3.14.1, você pode definir o tempo limite da sessão usando o arquivo Info.plist. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada `SessionTimeout` number e defina o valor como seu tempo limite de sessão personalizado. Note que, antes do SDK da Braze para iOS v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.

Como alternativa, você pode definir a chave `ABKSessionTimeoutKey` como o valor inteiro desejado em seu objeto `appboyOptions` passado para [`startWithApiKey`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#afd911d60dfe7e5361afbfb364f5d20f9).

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Sets the session timeout to 60 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKSessionTimeoutKey : @(60) }];
```

{% endtab %}
{% tab swift %}

```swift
// Sets the session timeout to 60 seconds
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKSessionTimeoutKey : 60 ])
```
{% endtab %}
{% endtabs %}

Se você tiver definido um tempo limite da sessão, a semântica da sessão se estenderá até esse tempo limite personalizado.

{% alert note %}
O valor mínimo para `sessionTimeoutInSeconds` é 1 segundo. O valor padrão é 10 segundos.
{% endalert %}

## Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até **App Usage (Uso do aplicativo** ) no perfil do usuário. Você pode confirmar que o rastreamento de sessões está funcionando verificando se a métrica "Sessões" aumenta quando você espera que isso aconteça.

![A seção de uso do app de um perfil de usuário que mostra o número de sessões, a data da última utilização e a data da primeira utilização.]({% image_buster /assets/img_archive/test_session.png %})

