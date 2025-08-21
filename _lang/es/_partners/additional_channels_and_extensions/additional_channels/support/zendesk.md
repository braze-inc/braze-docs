---
nav_title: Zendesk
article_title: Zendesk
description: "Este artículo de referencia describe la asociación entre Braze y Zendesk, una popular suite de soporte que le permite utilizar los webhooks de Braze que pueden sincronizar los datos de soporte entre las dos plataformas."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) ofrece a los negocios la posibilidad de mantener conversaciones naturales con sus clientes a través del soporte omnicanal mediante el correo electrónico, el webchat, la voz o las aplicaciones de mensajería social. Zendesk ofrece un sistema de tickets optimizado que valora el seguimiento y la priorización de las interacciones, lo que permite a los negocios tener una visión histórica unificada de sus clientes.

La integración de servidor a servidor de Braze y Zendesk permite utilizar: 
- Braze webhooks para automatizar la creación de tickets de soporte en Zendesk debido a la participación del mensaje en los recorridos del usuario en Braze. Por ejemplo, después de implantar y probar con éxito una integración, Braze puede crear un ticket de asistencia de un usuario que responda negativamente a un mensaje "¿Te gusta nuestra aplicación?" dentro de la aplicación, lo que permite a su equipo de asistencia realizar un seguimiento del cliente.
- webhooks de Zendesk para admitir casos de uso bidireccionales como la actualización del perfil de usuario en Braze debido a la actividad en Zendesk. Por ejemplo, después de resolver un ticket, registre un evento en el perfil del usuario en Braze.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta de Zendesk | Se requiere una [cuenta de administrador de Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) para aprovechar esta asociación. |
| Token de la API de Zendesk | Se necesita un token de Zendesk [API](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-) para enviar solicitudes desde Braze al punto final de tickets de Zendesk. |
| Identificador común (recomendado) | Se recomienda un [identificador común](#common-identifier) entre Braze y Zendesk. |
| Clave API Braze | Se necesita una clave de API de Braze para enviar solicitudes desde Zendesk a un punto final de Braze. Asegúrese de que la clave de API que utiliza tiene los permisos correctos para el punto final de Braze que utiliza su webhook de Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de Braze con Zendesk

### Paso 1: Cree su webhook Braze

Para crear un webhook:

- **Campañas:** Vaya a la página **Campañas** del panel de control de Braze. Haga clic en **Crear campaña** y seleccione **Webhook**.
- **Canvas:** A partir de un lienzo nuevo o existente, cree un paso completo o de mensaje en el constructor de lienzos. A continuación, haga clic en **Mensajes** y seleccione **Webhook** en las opciones de mensaje.

En tu webhook, rellena los siguientes campos:
- **URL del webhook**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Cuerpo de la solicitud**: Texto sin procesar

Otros casos de uso pueden gestionarse a través [de las API de soporte de Zendesk](https://developer.zendesk.com/rest_api/docs/support/introduction), que cambiarían en consecuencia el punto final `/api/v2/` al final de la URL del webhook.

#### Cabecera y método de la solicitud

Zendesk requiere un encabezado HTTP para la autorización y un método HTTP. En la pestaña **Configuración**, sustituya <email_address> por su correo electrónico de administrador de Zendesk y <api_token> por su token de API de Zendesk.

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: Básico {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud

Defina los detalles del ticket como tipo, asunto y estado en la carga útil de su webhook. Los detalles de los tickets se pueden ampliar y personalizar basándose en la [API de tickets de Zendesk](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Utilice el siguiente ejemplo como ayuda para estructurar su carga útil e introduzca los campos que desee.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Paso 2: Vista previa de su solicitud

Tu texto sin formato se resaltará automáticamente si es una etiqueta Braze aplicable.

Previsualiza tu petición en el panel de **Previsualización** o navega hasta la pestaña de **Prueba**, donde puedes seleccionar un usuario al azar o un usuario existente o personalizar el tuyo propio para probar tu webhook.

Por último, comprueba si el ticket se ha creado en el lado de Zendesk.

## Identificador común

Si tiene un identificador común entre Braze y Zendesk, se recomienda utilizarlo como `requester_id`. Esto ayudará a unificar los dos grupos de usuarios. Alternativamente, si este no es el caso, recomendamos pasar un conjunto de atributos identificativos como nombre, dirección de correo electrónico, número de teléfono u otros.

## Integración de Zendesk con Braze

### Paso 1: Crear un webhook

1. En el [Centro de administración](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), haga clic en **Aplicaciones e integraciones** en la barra lateral y, a continuación, seleccione **Webhooks > Webhooks**.<br><br>
2. Haga clic en **Crear webhook**.<br><br>
3. Seleccione **Activación** o **Automatización** y haga clic en **Siguiente**.<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Proporcione la siguiente información en su webhook:
- Introduzca un nombre y una descripción para el webhook.
- Introduce la URL del punto final Braze que utilizará tu webhook. {% raw %}En nuestro ejemplo utilizaremos `https://{{instance_url}}/users/track`.{% endraw %}
- Seleccione POST como método de solicitud del webhook y establezca el formato de solicitud en JSON.
- Seleccione el método de autenticación de token de portador para el webhook y proporcione su [clave de API Braze]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys).
  - Asegúrate de que la clave de API que utilizas tiene los [permisos correctos]({{site.baseurl}}/api/basics/#rest-api-key-permissions) para el punto final Braze que utiliza tu webhook.<br><br>
5. (Recomendado) Prueba el webhook para comprobar que funciona correctamente.<br><br>
6. Para los webhooks de desencadenamiento y automatización, debes conectar el webhook a un desencadenamiento o automatización antes de finalizar la configuración. Consulta el paso siguiente para ver nuestro ejemplo de creación de un desencadenador para el webhook. Una vez creado el desencadenante, puedes volver a esta página y seleccionar **Finalizar configuración**.

### Paso 2: Crear un activador o automatización

[Siga las instrucciones de Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) sobre cómo conectar su webhook a un disparador o automatización.

Nuestro ejemplo a continuación utilizará un disparador para invocar el webhook cuando el estado de un caso de soporte haya cambiado a "Resuelto" o "Cerrado". 

1. En el **Centro de administración**, haga clic en **Objetos y reglas** en la barra lateral y, a continuación, seleccione **Reglas de negocio > Desencadenantes**.<br><br>
2. Selecciona **Añadir desencadenante**.<br><br>
3. Asigne un nombre a su activador y seleccione una categoría.<br><br>
4. Selecciona **Añadir condición** para configurar qué condiciones deben desencadenar el webhook. Por ejemplo, "Categoría de estado cambiada a cerrado" o "Categoría de estado cambiada a resuelto".![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Selecciona **Añadir acción**, elige **Notificar webhook activo** y selecciona del desplegable el webhook creado en el paso anterior.<br><br>
6. Defina el cuerpo JSON para que se ajuste a su punto final Braze, usando marcadores de posición variables de Zendesk para rellenar dinámicamente los campos relevantes.<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Seleccione **Crear**.<br><br>
8. Vuelva a su webhook y haga clic en **Finalizar configuración**.


