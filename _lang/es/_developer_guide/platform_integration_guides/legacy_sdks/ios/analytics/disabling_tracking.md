---
nav_title: Desactivar el seguimiento del SDK de iOS
article_title: Desactivar el seguimiento del SDK para iOS
platform: iOS
page_order: 8
description: "Este artículo muestra cómo desactivar la recopilación de datos para tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Desactivar la recopilación de datos para iOS

Para cumplir la normativa sobre privacidad de datos, la actividad de seguimiento de datos en el SDK de iOS puede detenerse por completo mediante el método [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733). Este método hará que se cancelen todas las conexiones de red, y el SDK de Braze no pasará ningún dato a nuestros servidores. Si deseas reanudar la recopilación de datos más adelante, puedes utilizar el método [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) para reanudar la recopilación de datos.

Además, puedes utilizar el método [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) para borrar completamente todos los datos del lado del cliente almacenados en el dispositivo.

A menos que un usuario desinstale todas las aplicaciones de un proveedor en un dispositivo determinado, la siguiente ejecución del SDK y de la aplicación Braze después de llamar a `wipeDataAndDisableForAppRun()` hará que nuestro servidor vuelva a identificar a ese usuario a través de su identificador de dispositivo (IDFV). Para eliminar por completo todos los datos de usuario, debes combinar una llamada a `wipeDataAndDisableForAppRun` con una solicitud de eliminación de datos en el servidor a través de la [API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint) de Braze.

## SDK para iOS v5.7.0+
Para los dispositivos que utilicen el SDK de iOS versión 5.7.0 y superior, al [desactivar la recopilación de IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfv-collection---swift/), la llamada a [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) no hará que nuestro servidor vuelva a identificar a ese usuario a través del identificador de su dispositivo (IDFV).