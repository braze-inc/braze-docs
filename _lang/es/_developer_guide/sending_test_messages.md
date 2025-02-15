---
nav_title: Cómo enviar mensajes de prueba
article_title: Cómo enviar mensajes de prueba
page_order: 6
description: "Este artículo de referencia trata del envío de mensajes de prueba para distintos canales."

---

# Envío de mensajes de prueba

> Antes de enviar una campaña de mensajería a tus usuarios, quizá quieras probarla para asegurarte de que tiene el aspecto adecuado y funciona de la forma prevista. Crear y enviar mensajes de prueba a determinados dispositivos o miembros de tu equipo es muy sencillo con las herramientas del dashboard.

## Creación de un segmento de prueba designado <a class="margin-fix" name="test-segment"></a>

Una vez configurado un segmento de prueba, puedes utilizarlo para probar **cualquiera** de nuestros canales de mensajería. Si se configura correctamente, el proceso solo tendrá que hacerse una vez.

Para configurar un segmento de prueba, ve a la página **Segmentos** del panel y crea un nuevo segmento. Haz clic en **Añadir filtro** para elegir uno de los filtros de prueba que se encuentran en la parte inferior del menú desplegable.

![Una campaña de prueba Braze que muestra los filtros disponibles en el paso de segmentación.]({% image_buster /assets/img_archive/testmessages1.png %})

Dos de estos filtros de prueba te permiten seleccionar usuarios con direcciones de correo electrónico específicas o [ID de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) externos.

![Un menú desplegable que muestra varios filtros listados bajo un encabezamiento que dice Probando]({% image_buster /assets/img_archive/testmessages2.png %})

Los filtros de dirección de correo electrónico e ID externo de usuario tienen tres opciones:

  1) **"Equals"** \- Buscará una coincidencia exacta del correo electrónico o ID de usuario que proporciones. Utilízalo si solo quieres enviar las campañas de prueba a dispositivos asociados a un único correo electrónico o ID de usuario.

  2) **"No es igual"** \- Utilízalo si quieres excluir un correo electrónico o ID de usuario concreto de las campañas de prueba.

  3) **"Coincidencias"** \- Esto encontrará usuarios que tengan direcciones de correo electrónico o ID de usuario que coincidan con parte del término de búsqueda que proporciones. Podrías utilizarlo para encontrar sólo a los usuarios que tengan una dirección "@yourcompany.com", lo que te permitiría enviar mensajes a todos los miembros de tu equipo.

Puedes seleccionar varios correos electrónicos específicos utilizando la opción "coincidencias" y separando las direcciones de correo electrónico con un carácter | (por ejemplo, "coincidencias" "email1@braze.com | email2@braze.com").

Estos filtros también pueden utilizarse de manera combinada para reducir tu lista de usuarios de prueba. Por ejemplo, el segmento de prueba podría incluir un filtro de dirección de correo electrónico que "coincida" con "@braze.com" y otro filtro que "no coincida" con "sales@braze.com". 

Después de añadir los filtros de prueba a tu segmento de prueba, puedes comprobar que has seleccionado sólo a los usuarios que pretendías haciendo clic en **Vista previa** en la parte superior del editor de segmentos o exportando los datos de usuario de ese segmento a CSV haciendo clic en el icono de engranaje de la esquina derecha del editor y seleccionando **CSV Exportar todos los datos de usuario** en el menú desplegable.

![Una sección de una campaña Braze titulada Detalles del segmento]({% image_buster /assets/img_archive/testmessages3.png %})

>  Exportar los datos de usuario del segmento en formato CSV te dará la imagen más precisa de quién se incluye en ese segmento. La pestaña **Vista previa** es sólo una muestra de los usuarios del segmento y, por tanto, puede parecer que no se han seleccionado todos los miembros previstos.

## Enviar una notificación push de prueba o mensajes dentro de la aplicación <a class="margin-fix" name="push-inapp-test"></a>

Para enviar notificaciones push de prueba o mensajes dentro de la aplicación, tienes que dirigirte a tu segmento de prueba creado previamente. Empieza creando tu campaña y siguiendo los pasos habituales. Cuando llegues al paso **Usuarios objetivo**, selecciona tu segmento de prueba en el menú desplegable.

![Una campaña de prueba Braze que muestra los segmentos disponibles en el paso de segmentación.]({% image_buster /assets/img_archive/test_segment.png %})

Termina de confirmar tu campaña y lánzala para probar tus notificaciones push y mensajes dentro de la aplicación.

>  Asegúrate de seleccionar **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la parte **Programa** del creador de campañas si pretendes utilizar una única campaña para enviarte un mensaje de prueba a ti mismo más de una vez.

## Envío de un mensaje de correo electrónico de prueba

Si sólo estás probando mensajes de correo electrónico, no tienes que configurar necesariamente un segmento de prueba. En el primer paso del compositor de campañas, donde redactas el mensaje de correo electrónico de tu campaña, haz clic en **Enviar prueba** e introduce la dirección de correo electrónico a la que deseas enviar un correo de prueba. 

![Una campaña Braze con la pestaña Envío de prueba seleccionada]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
También puedes habilitar o deshabilitar que se añada [TEST (o SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) a tus mensajes de prueba.
{% endalert %}

## Prueba desde la línea de comandos

Alternativamente, si quieres probar las notificaciones push a través de la línea de comandos, puedes seguir los siguientes ejemplos para cada plataforma.

### Probar push con aplicaciones iOS mediante cURL

Puedes enviar una sola notificación a través del terminal mediante CURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` - disponible en **Configuración** > **Claves de API**
- `YOUR_EXTERNAL_USER_ID` - disponible en la página **Buscar usuarios** 
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), estas páginas se encuentran en una ubicación diferente: <br>- **Las claves de API** se encuentran en **Consola para desarrolladores** > **Configuración de API** <br>- **Buscar usuarios** se encuentra en **Usuarios** > **Búsqueda de usuarios**
{% endalert %}

>  Los siguientes ejemplos muestran los puntos finales de API adecuados para los clientes en la instancia `US-01`. Si no estás en esta instancia, consulta [la documentación de nuestra API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para saber a qué punto final debes hacer las solicitudes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Probar push con aplicaciones Android mediante cURL

Puedes enviar una sola notificación a través del terminal mediante cURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` (Ve a **Configuración** > **Claves de API**).
- `YOUR_EXTERNAL_USER_ID` (Busca un perfil en la página **Buscar usuarios** ).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

>  Los siguientes ejemplos muestran los puntos finales de API adecuados para los clientes en la instancia `US-01`. Si no estás en esta instancia, consulta [la documentación de nuestra API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) para saber a qué punto final debes hacer las solicitudes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Probar push con aplicaciones Kindle mediante cURL

Puedes enviar una sola notificación a través del terminal mediante cURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` - disponible en la página **Consola del desarrollador** 
- `YOUR_EXTERNAL_USER_ID` - disponible en la página **Búsqueda de usuarios** 
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Limitaciones de los mensajes de prueba

Hay algunas situaciones en las que los mensajes de prueba no tienen una paridad de características completa con el lanzamiento de una campaña o Canvas a un conjunto real de usuarios. En estas instancias, para validar este comportamiento, debes lanzar la campaña o el Canvas a un conjunto limitado de usuarios de prueba.

- Ver el [centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) Braze desde **Mensajes de prueba** hará que el botón de envío aparezca en gris
- La cabecera lista-cancelar suscripción no se incluye en los correos electrónicos enviados por la funcionalidad de mensajes de prueba
- Para los mensajes dentro de la aplicación y las tarjetas de contenido, el usuario de destino debe tener un token de notificaciones push para el dispositivo de destino

