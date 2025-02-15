---
nav_title: Desactivar el seguimiento del SDK de iOS
article_title: Desactivar el seguimiento del SDK para iOS
platform: Swift
page_order: 8
description: "En este artículo se muestra cómo desactivar la recopilación de datos para el SDK Swift."

---

# Desactivar el seguimiento del SDK de iOS

> Para cumplir la normativa sobre privacidad de datos, la actividad de seguimiento de datos en el SDK de iOS puede detenerse por completo configurando la propiedad [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) a `false` en tu instancia de Braze. 

Cuando `enabled` está configurado como `false`, el SDK de Braze ignora cualquier llamada a la API pública. El SDK también cancela todas las acciones en vuelo, como solicitudes de red, procesamiento de eventos, etc. Para reanudar la recopilación de datos, configura [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) a `true`.

También puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para borrar completamente los datos SDK almacenados localmente en el dispositivo de un usuario. Si utilizas la versión 5.7.0 o anterior del SDK de Swift, o `useUUIDAsDeviceId` está configurado en `false`, también tendrás que realizar una solicitud posterior a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) ya que se utilizará tu Identificador para Vendedores (IDFV) como ID de su dispositivo. Para las versiones 7.0.0 y posteriores de Braze Swift, el SDK y el método `wipeData()` generan aleatoriamente un UUID para su ID de dispositivo.
