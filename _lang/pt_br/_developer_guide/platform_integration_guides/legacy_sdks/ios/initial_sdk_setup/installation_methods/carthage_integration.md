---
nav_title: Carthage
article_title: Integração do Carthage para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência mostra como integrar o SDK da Braze usando o Carthage para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração de Cartago

## Importar o SDK

A partir da versão `4.4.0`, o SDK da Braze é compatível com o XCFrameworks durante a integração via Carthage. Para importar o SDK completo, inclua estas linhas em seu `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Consulte o [guia de início rápido do Carthage](https://github.com/Carthage/Carthage#quick-start) para saber mais sobre a importação do SDK.

Ao migrar de uma versão anterior para `4.4.0`, siga o [guia de migração do Carthage para o XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Para saber mais sobre a sintaxe do `Cartfile` ou sobre recursos como a fixação de versão, consulte a [documentação do Carthage](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Para uso específico da plataforma do Carthage, consulte o [guia do usuário](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Versões anteriores

Para as versões `3.24.0` a `4.3.4`, inclua o seguinte em seu `Cartfile`:
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Para importar versões anteriores a `3.24.0`, inclua o seguinte em seu `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Substitua `<BRAZE_IOS_SDK_VERSION>` pela [versão apropriada](https://github.com/Appboy/appboy-ios-sdk/releases) do Braze iOS SDK no formato "x.y.z".

## Próximas etapas

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Integração somente do núcleo

Para usar o SDK principal sem nenhum componente ou dependência de interface, instale a versão principal do framework da Braze para Carthage incluindo a seguinte linha em seu `Cartfile`:

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

