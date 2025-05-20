# Actualización a Android 13

> En esta guía se describen los cambios relevantes introducidos en Android 13 (2022) y los pasos de actualización necesarios para tu integración del SDK para Android de Braze.

Consulta la [documentación para desarrolladores de Android](https://developer.android.com/about/versions/13) 13 para obtener una guía completa de migración.

## SDK para Android 13 de Braze

Para prepararte para Android 13, actualiza tu SDK de Braze a la [última versión (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Si lo haces, tendrás acceso a nuestra nueva [ característica push primer "sin código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Cambios en Android 13

### Permiso de notificaciones push {#push-permission}

Android 13 introduce un [cambio importante](https://developer.android.com/about/versions/13/changes/notification-permission) en la forma en que los usuarios administran las aplicaciones que envían notificaciones push. En Android 13, las aplicaciones deben obtener permisos antes de poder mostrar las notificaciones push. 

![Un mensaje push de Android que pregunta "¿Permitir que Kitchenerie te envíe notificaciones?" con dos botones "Permitir" y "No permitir" en la parte inferior del mensaje.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Este nuevo permiso sigue un patrón similar al de iOS y notificación push web, donde solo tienes un intento para obtener el permiso. Si un usuario elige `Don't Allow` o rechaza el aviso, tu aplicación no podrá volver a pedir permiso.

Ten en cuenta que se concede una [exención](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) a las aplicaciones para los usuarios que anteriormente tenían habilitadas las notificaciones push antes de actualizar a Android 13. Estos usuarios [seguirán siendo elegibles](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) para recibir push cuando actualicen a Android 13 sin tener que solicitar permiso.

#### Momento de la solicitud de permiso {#push-permission-timing}

**Segmentación de Android 13**

Las aplicaciones dirigidas a Android 13 pueden controlar cuándo solicitar permiso y mostrar el aviso push nativo. 

Si tu usuario actualiza de Android 12 a 13, tu aplicación estaba previamente instalada y ya enviabas notificaciones push, el sistema preconcede automáticamente el nuevo permiso de notificación a todas las aplicaciones elegibles. En otras palabras, estas aplicaciones pueden seguir enviando notificaciones a los usuarios, y éstos no ven una solicitud de permiso en tiempo de ejecución.

Para más detalles al respecto, consulta la documentación para desarrolladores de Android para conocer [los efectos sobre las actualizaciones de las aplicaciones existentes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Segmentación de Android 12 o anterior**

Si tu aplicación aún no está orientada a Android 13, y un nuevo usuario de Android 13 instala tu aplicación, verá automáticamente un aviso de permiso push cuando tu aplicación cree su primer canal de notificación (a través de `notificationManager.createNotificationChannel`). A los usuarios que ya tienen instalada tu aplicación y luego se actualizan a Android 13 nunca se les muestra un aviso y se les concede automáticamente el permiso push.

{% alert note %}
El SDK v23.0.0 de Braze crea automáticamente un canal de notificación predeterminado si aún no existe cuando se recibe una notificación push. Si no te diriges a Android 13, esto hará que se muestre el aviso de permiso push, necesario para mostrar la notificación.
{% endalert %}

## Preparación para Android 13 {#next-steps}

Se recomienda encarecidamente que tu aplicación se dirija a Android 13 para controlar cuándo se solicita permiso push a los usuarios.

Esto te permitirá optimizar tus [tasas de adhesión voluntaria push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) al solicitar permiso a los usuarios en momentos más apropiados y mejorará la experiencia del usuario en cuanto a cómo y cuándo tu aplicación solicita permiso push.

Para empezar a utilizar nuestra nueva [ característica push primer "sin código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), actualiza tu SDK de Android a la [última versión (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).

