---
nav_title: Desactivar el seguimiento del SDK
article_title: Desactivar la recopilación de datos para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Este artículo muestra cómo desactivar la recopilación de datos para tu aplicación Android o FireOS."

---

# Desactivar el seguimiento del SDK

> Este artículo muestra cómo desactivar la recopilación de datos para tu aplicación Android o FireOS.

Para cumplir la normativa sobre privacidad de datos, la actividad de seguimiento de datos en el SDK de Android puede detenerse por completo utilizando el método [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). Este método hará que se cancelen todas las conexiones de red, y el SDK de Braze no pasará ningún dato a los servidores de Braze. Si deseas reanudar la recopilación de datos en un momento posterior, puedes utilizar el método [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) para reanudar la recopilación de datos en el futuro.

Además, puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) para borrar completamente todos los datos del lado del cliente almacenados en el dispositivo.

