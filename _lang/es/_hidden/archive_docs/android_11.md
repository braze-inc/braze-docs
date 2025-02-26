---
nav_title: Guía de actualización a Android 11
article_title: Guía de actualización a Android 11
page_order: 9
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre la actualización del SDK de Android 11, destacando cambios como la vinculación en profundidad, la compatibilidad con el SDK y mucho más."
hidden: true
---

# Guía de actualización del SDK de Android 11

Esta guía describe los cambios relevantes introducidos en Android 11 (publicado el 8 de septiembre de 2020) y los pasos de actualización necesarios para tu integración de SDK de Android Braze.

Para una guía completa de migración de Android 11, consulta la [documentación para desarrolladores de Android](https://developer.android.com/preview/migration).

## Compatibilidad con el SDK Braze

Todas las aplicaciones _orientadas a_ Android 11 (API 30) deben actualizarse a [Braze Android SDK v8.1.0+][1] para seguir utilizando las características de mensajería de Braze.

{% alert important %}
Debido a los cambios en las API de Android 11, las aplicaciones destinadas a Android 11 que no se actualicen a Braze Android SDK v8.1.0+ experimentarán problemas con la vinculación en profundidad desde los componentes de la interfaz de usuario de Braze y no mostrarán correctamente los mensajes dentro de la aplicación en HTML personalizado.
{% endalert %}

### Vínculos en profundidad

Las aplicaciones destinadas a Android 11 o posterior (API versión 30+) deben actualizarse al [SDK para Android de Braze v8.1.0][1] para seguir utilizando los vínculos profundos dentro de los mensajes Braze. Debido a un cambio en las API de Android 11, las aplicaciones que no se actualicen al menos al SDK para Android v8.1.0 experimentarán problemas con los vínculos profundos dentro de los mensajes Braze (mensajes dentro de la aplicación o tarjetas de contenido).

### Mensajes HTML dentro de la aplicación

Las aplicaciones destinadas a Android 11 o posterior (API versión 30+) deben actualizarse a Braze Android SDK v8.1.0 para seguir utilizando mensajes HTML personalizados dentro de la aplicación. Debido a un cambio en la configuración de Android 11 WebView, los mensajes HTML dentro de la aplicación no se mostrarán correctamente en las aplicaciones orientadas a Android 11 hasta que se actualice a [Braze Android SDK v8.1.0][1]. 

### Permisos de ubicación

Las aplicaciones que utilicen permisos de ubicación deben seguir las [mejores prácticas](https://developer.android.com/preview/privacy/location#change-details) de Android cuando soliciten acceso a la ubicación. No es necesario realizar cambios en tu integración Braze para estas actualizaciones de ubicación.

## Cambios en el comportamiento de Android 11

### Permitir una vez permisos

Ahora los usuarios pueden conceder permisos, como la recopilación de ubicaciones, una sola vez (consulta [los documentos de Android](https://developer.android.com/preview/privacy/location#one-time-access) para obtener más información). Cuando una aplicación esté cerrada o en segundo plano durante el tiempo suficiente, ese permiso se revocará automáticamente. La aplicación tendría que volver a solicitar este permiso cuando lo necesitara en el futuro. Las aplicaciones que ya siguen el flujo recomendado para solicitar permisos de ubicación admitirán permisos de una sola vez.

![][3]{: height="230px" }

### Permiso de ubicación de fondo

Android 11 exigirá a las aplicaciones que soliciten primero el permiso de ubicación en primer plano y, después, cuando la aplicación esté en segundo plano, puede volver a solicitar al usuario el permiso de ubicación en segundo plano.
Los clientes que utilicen geovallas deben asegurarse de que su aplicación sigue las recomendaciones de Android sobre la recopilación de permisos de ubicación en segundo plano. Para más información, consulta [los documentos de Android](https://developer.android.com/preview/privacy/location#background-location).

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
