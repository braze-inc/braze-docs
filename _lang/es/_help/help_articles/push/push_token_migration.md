---
nav_title: Migración de tokens de notificaciones push
article_title: Migración de tokens de notificaciones push
page_order: 0

page_type: solution
description: "Este artículo de ayuda explica cómo migrar tokens de notificaciones push para que puedas seguir enviando mensajes push a tus usuarios después de cambiar a Braze."
channel: push
---

# Migración de tokens de notificaciones push

Un [token de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) es un identificador anónimo único que especifica dónde enviar las notificaciones de una aplicación. Braze se conecta con proveedores de servicios push como Firebase Cloud Messaging Service (FCM) para Android y Apple Push Notification Service (APN) para iOS, y esos proveedores envían tokens de dispositivos únicos que identifican tu aplicación. Si enviabas notificaciones push antes de integrar Braze, por tu cuenta o a través de otro proveedor, la migración de token de notificaciones push te permite seguir enviando notificaciones push a tus usuarios con tokens de notificaciones push registrados.

## Migración automática mediante SDK

El SDK de Braze migrará automáticamente el token de notificaciones push de un usuario que haya optado previamente por tus notificaciones push la primera vez que inicie sesión en tu aplicación o sitio integrado en Braze. Si integras los SDK de Braze, no necesitarás migrar tokens de notificaciones push utilizando la API.

Sin embargo, como los tokens de notificaciones push migran cuando un usuario inicia sesión por primera vez en tu aplicación, ten en cuenta que Braze no podrá enviar notificaciones push a usuarios que no hayan iniciado sesión después de tu integración de SDK. Puede que aún desees migrar manualmente los tokens de notificaciones push de Android e iOS como forma de reactivación de la interacción con estos usuarios.

{% alert note %}
Debido a la naturaleza de los tokens de notificaciones push web, cada ~60 días el token caduca y se restablece. Cualquiera que no tenga una sesión dentro de ese periodo de tiempo no tendrá un token de notificaciones push web activo. Braze no migrará tokens de notificaciones push web caducados. Habrá que reactivar a estos usuarios mediante [primers push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages).
{% endalert %}

## Migración manual mediante API

La migración manual de token de notificaciones push es el proceso de importar estas claves creadas previamente a tu plataforma Braze a través de la API.

Programa la migración de tokens de iOS (APN) y Android (FCM) a tu plataforma utilizando el [punto final `users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Puedes migrar tanto usuarios identificados (usuarios con un ID externo asociado) como usuarios anónimos (usuarios sin ID externo).

Especifica el `app_id` de tu aplicación durante la migración del token de notificaciones push para asociar el token de notificaciones push adecuado con la aplicación apropiada. Cada aplicación (iOS, Android, etc.) tiene su propio `app_id`, que puedes encontrar en la sección **Identificación** de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Asegúrate de utilizar el `app_id` de la plataforma correcta.

{% alert important %}
No es posible migrar tokens de notificaciones push web a través de la API. Esto se debe a que los tokens de notificaciones push web no se ajustan al mismo esquema que otras plataformas. 

<br>Si estás intentando migrar tokens de notificaciones push web mediante programación, es posible que aparezca un error como el siguiente: `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
Como alternativa a la migración de API, te recomendamos que integres el SDK y permitas que tu base de tokens se repoble de forma natural.
{% endalert %}

### Migración si hay ID externo
Para usuarios identificados, establece el indicador `push_token_import` en `false` (u omite el parámetro) y especifica los valores `external_id`, `app_id` y `token` en el objeto de usuario `attributes`. 

Por ejemplo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```

### Migración si el ID externo no está presente
Al importar tokens de notificaciones push de otros sistemas, no siempre se dispone de una dirección `external_id`. En este caso, configura tu flag `push_token_import` como `true` y especifica los valores `app_id` y `token`. Braze creará un perfil de usuario anónimo temporal para cada token para habilitarte a seguir enviando mensajes a estas personas. Si el token ya existe en Braze, se ignora la solicitud.

Por ejemplo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

Tras la importación, cuando el usuario anónimo inicie la versión habilitada para Braze de tu aplicación, Braze moverá automáticamente su token de notificaciones push importado a su perfil de usuario Braze y limpiará el perfil temporal.

Braze comprobará una vez al mes si hay algún perfil anónimo con la bandera `push_token_import` que no tenga un token de notificaciones push. Si el perfil anónimo ya no tiene un token de notificaciones push, eliminaremos el perfil. Sin embargo, si el perfil anónimo aún tiene un token de notificaciones push, lo que sugiere que el usuario real aún no ha iniciado sesión en el dispositivo con dicho token de notificaciones push, no haremos nada.

## Importar tokens de notificaciones push de Android

{% alert important %}
La siguiente consideración sólo se aplica a las aplicaciones Android. Las aplicaciones iOS no necesitarán estos pasos porque esa plataforma sólo tiene un marco para mostrar push, y las notificaciones push se renderizarán inmediatamente siempre que Braze tenga los tokens de notificaciones push y los certificados necesarios.
{% endalert %}

Si debes enviar notificaciones push de Android a tus usuarios antes de que se complete la integración de SDK de Braze, utiliza pares clave-valor para validar las notificaciones push. 

Debes tener un receptor para gestionar y mostrar cargas útiles push. Para notificar al receptor la carga útil push, añade los pares clave-valor necesarios a la campaña push. Los valores de estos pares dependen del socio de push específico que hayas utilizado antes de Braze.

{% alert note %}
Para algunos proveedores de notificaciones push, Braze tendrá que aplanar los pares clave-valor para que puedan interpretarse correctamente. Para aplanar los pares clave-valor de una aplicación específica de Android, ponte en contacto con tu gestor de incorporación de clientes o de éxito.
{% endalert %}

_Última actualización: 5 de diciembre de 2022_
