---
nav_title: Desativar o rastreamento do SDK para iOS
article_title: Desativar o rastreamento do SDK para iOS
platform: iOS
page_order: 8
description: "Este artigo mostra como desativar a coleta de dados para seu app para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Desativar a coleta de dados para iOS

Para cumprir as normas de privacidade de dados, a atividade de rastreamento de dados no SDK do iOS pode ser interrompida completamente usando o método [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733). Esse método fará com que todas as conexões de rede sejam canceladas, e o SDK da Braze não passará nenhum dado para os servidores da Braze. Para retomar a coleta de dados, use o método [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b).

Além disso, você pode usar o método [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) para limpar completamente todos os dados do lado do cliente armazenados no dispositivo.

A menos que um usuário desinstale todos os aplicativos de um fornecedor em um determinado dispositivo, a próxima execução do Braze SDK e do app após chamar `wipeDataAndDisableForAppRun()` resultará na reidentificação desse usuário pelo nosso servidor por meio do identificador do dispositivo (IDFV). Para remover totalmente todos os dados de usuários, você deve combinar uma chamada para `wipeDataAndDisableForAppRun` com uma solicitação para excluir dados no servidor por meio da [API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint) do Braze.

## iOS SDK v5.7.0+
Para dispositivos que usam o iOS SDK v5.7.0 e superior, ao [desativar a coleta de IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfv-collection---swift/), chamar [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) não fará com que nosso servidor reidentifique o usuário por meio do identificador do dispositivo (IDFV).