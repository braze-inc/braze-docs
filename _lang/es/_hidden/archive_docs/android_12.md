---
nav_title: Guía de actualización a Android 12
article_title: Guía de actualización a Android 12
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre la actualización del SDK de Android 12, destacando cambios como la vinculación en profundidad, la compatibilidad con el SDK y mucho más."
---

# Guía de actualización del SDK de Android 12

Esta guía describe los cambios relevantes introducidos en Android 12 (2021) y los pasos de actualización necesarios para tu integración de SDK de Android Braze.

Para obtener una guía completa de migración a Android 12, consulta la [documentación para desarrolladores de Android](https://developer.android.com/about/versions/12).

## Compatibilidad con el SDK Braze

Si tu objetivo es Android 12, debes utilizar [Braze Android SDK v13.1.2+][1]. Si aún no tienes Android 12 como objetivo, se recomienda actualizarlo.

**¿Qué ocurre si no actualizo mi SDK para Android de Braze?**

* Debido a un cambio en los [diálogos del sistema de cierre](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs) de Android, las versiones anteriores del SDK para Android de Braze registrarán advertencias al recibir notificaciones push en dispositivos que ejecuten Android 12. Este comportamiento se produce incluso si tu aplicación no está destinada a Android 12.
* Los cambios en las [exportaciones de componentes](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [intenciones pendientes](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) y [trampolines de notificación](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) pueden afectar a tu capacidad para compilar tu aplicación o pueden impedir que se inicialice el SDK de Braze. Este comportamiento sólo se produce en las aplicaciones destinadas a Android 12.
* Los cambios en las [notificaciones push personalizadas](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) han modificado el diseño de nuestra nueva característica [push de imágenes en línea para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/). Este comportamiento sólo se produce en las aplicaciones destinadas a Android 12.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
