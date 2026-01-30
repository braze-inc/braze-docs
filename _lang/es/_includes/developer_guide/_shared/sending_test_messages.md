# Envío de mensajes de prueba

> Antes de enviar una campaña de mensajería a tus usuarios, quizá quieras probarla para asegurarte de que tiene el aspecto adecuado y funciona de la forma prevista. Puedes utilizar el panel para crear y enviar mensajes de prueba con notificaciones push, mensajes dentro de la aplicación (IAM) o correo electrónico.

## Enviar un mensaje de prueba

### Paso 1: Crea un segmento de prueba designado <a class="margin-fix" name="test-segment"></a>

Después de configurar un segmento de prueba, puedes utilizarlo para probar cualquiera de tus canales de mensajería Braze. Si se configura correctamente, sólo hay que hacerlo una vez.

Para configurar un segmento de prueba, ve a **Segmentos** y crea un nuevo segmento. Selecciona **Añadir filtro** y elige uno de los filtros de prueba.

![Una campaña de prueba de Braze que muestra los filtros disponibles en el paso de segmentación.]({% image_buster /assets/img_archive/testmessages1.png %})

Con los filtros de prueba, puedes asegurarte de que sólo se envíe el mensaje de prueba a los usuarios con una dirección de correo electrónico específica o [un ID externo de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids).

![Un menú desplegable que muestra varios filtros listados bajo un encabezamiento que dice Probando]({% image_buster /assets/img_archive/testmessages2.png %})

Tanto los filtros de dirección de correo electrónico como los de ID externo de usuario ofrecen las siguientes opciones:

| Operador          | Descripción |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | Se buscará una coincidencia exacta del correo electrónico o ID de usuario que proporciones. Utilízalo si solo quieres enviar las campañas de prueba a dispositivos asociados a un único correo electrónico o ID de usuario. |
| `does not equal` | Utilízalo si quieres excluir un determinado correo electrónico o ID de usuario de las campañas de prueba. |
| `matches`     | Esto encontrará usuarios que tengan direcciones de correo electrónico o ID de usuario que coincidan con parte del término de búsqueda que proporciones. Podrías utilizarlo para encontrar sólo a los usuarios que tengan una dirección `@yourcompany.com`, lo que te permitiría enviar mensajes a todos los miembros de tu equipo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Puedes seleccionar varios correos electrónicos específicos utilizando la opción "`matches`" y separando las direcciones de correo electrónico con un carácter |. Por ejemplo: "`matches`" "`email1@braze.com` | `email2@braze.com`". También puedes combinar varios operadores a la vez. Por ejemplo, el segmento de prueba podría incluir un filtro de direcciones de correo electrónico que "`matches`" "`@braze.com`" y otro filtro que "`does not equal`" "`sales@braze.com`". 

Después de añadir los filtros de prueba a tu segmento de prueba, puedes comprobar que funciona seleccionando **Vista previa** o seleccionando **Configuración** > **CSV Exportar todos los datos de usuario** para exportar los datos de usuario de ese segmento a un archivo CSV.

![Una sección de una campaña Braze titulada Detalles del segmento]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
Exportar los datos de usuario del segmento a un archivo CSV es el método de verificación más preciso, ya que la vista previa sólo mostrará una muestra de tus usuarios y puede que no incluya a todos los usuarios.
{% endalert %}

### Paso 2: Envía el mensaje

Puedes enviar un mensaje utilizando el panel de Braze o la línea de comandos.

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
Para enviar notificaciones push de prueba o mensajes dentro de la aplicación, tienes que dirigirte a tu segmento de prueba creado previamente. Empieza creando tu campaña y siguiendo los pasos habituales. Cuando llegues al paso **Audiencias objetivo**, selecciona tu segmento de prueba en el menú desplegable.

![Una campaña de prueba Braze que muestra los segmentos disponibles en el paso de segmentación.]({% image_buster /assets/img_archive/test_segment.png %})

Confirma tu campaña y lánzala para probar tus notificaciones push y mensajes dentro de la aplicación.

{% alert note %}
Asegúrate de seleccionar **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña** en la parte **Programa** del creador de campañas si pretendes utilizar una única campaña para enviarte un mensaje de prueba a ti mismo más de una vez.
{% endalert %}
{% endsubtab %}

{% subtab email message %}
Si sólo estás probando mensajes de correo electrónico, no tienes que configurar necesariamente un segmento de prueba. En el primer paso del compositor de campañas, donde redactas el mensaje de correo electrónico de tu campaña, haz clic en **Enviar prueba** e introduce la dirección de correo electrónico a la que deseas enviar un correo de prueba. 

![Una campaña Braze con la pestaña Envío de prueba seleccionada]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
También puedes habilitar o deshabilitar que se añada [TEST (o SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) a tus mensajes de prueba.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
Alternativamente, puedes enviar una sola notificación utilizando cURL y [la API de mensajería Braze]({{site.baseurl}}/api/endpoints/messaging/). Observa que estos ejemplos realizan una solicitud utilizando la instancia `US-01`. Para conocer los tuyos, consulta [los puntos finales de la API]({{site.baseurl}}/api/basics/#endpoints).

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

Sustituye lo siguiente:

| Marcador de posición         | Descripción                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Tu clave de API de Braze utilizada para la autenticación. En Braze, ve a **Configuración** > **Claves de API** para localizar tu clave. |
| `EXTERNAL_USER_ID` | El ID externo del usuario utilizado para enviar tu mensaje a un usuario concreto. En Braze, ve a **Audiencia** > **Buscar usuarios** y, a continuación, busca un usuario. |
| `CUSTOM_KEY`         | (Opcional) Una clave personalizada para datos adicionales.              |
| `CUSTOM_VALUE`       | (Opcional) Un valor personalizado asignado a tu clave personalizada.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Limitaciones de las pruebas

Hay algunas situaciones en las que los mensajes de prueba no tienen una paridad de características completa con el lanzamiento de una campaña o Canvas a un conjunto real de usuarios. En estas instancias, para validar este comportamiento, debes lanzar la campaña o el Canvas a un conjunto limitado de usuarios de prueba.

- Ver el [centro de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) Braze desde **Mensajes de prueba** hará que el botón de envío aparezca en gris.
- La cabecera de cancelar suscripción no se incluye en los correos electrónicos enviados por la funcionalidad de mensajes de prueba.
- Para los mensajes dentro de la aplicación y las tarjetas de contenido, el usuario de destino debe tener un token de notificaciones push para el dispositivo de destino.
