---
nav_title: Oppizi
article_title: Oppizi 
alias: /partners/oppizi/
description: "Este artículo de referencia describe la asociación entre Braze y Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) es el líder mundial en marketing offline, que ofrece una solución integral para que las empresas realicen campañas de correo directo y folletos mensurables y específicas.

_Esta integración está mantenida por Oppizi._

## Requisitos previos

| Requisito                    | Descripción                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Cuenta Oppizi                 | Para utilizar esta integración se necesita una cuenta activa de Oppizi.                 |
| Clave de API de Oppizi                 | Se encuentra en tu cuenta de Oppizi en **Integraciones** > **Braze**.                |
| ID de flujo de trabajo del correo directo de Oppizi | Crea un flujo de trabajo en Oppizi en la página **Flujo de trabajo de correo directo** para obtener un ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

Con la integración de Oppizi, puedes:

* **Envía postales automatizadas de correo directo** utilizando desencadenadores Braze conectados a los flujos de trabajo de webhook y correo directo de Oppizi.
* **Configura umbrales, oleadas y límites** en los flujos de trabajo de correo directo de Oppizi para controlar el envío de tus campañas.
* **Diseña postales profesionales** con la herramienta de diseño integrada de Oppizi, sin necesidad de tener experiencia en diseño.
* **Sigue el rendimiento de la campaña** en tiempo real con el panel de Oppizi.

## Integración

### Paso 1: Genera tu clave de API de Oppizi 

Para utilizar tu plantilla de webhook en Braze, primero tendrás que generar tu clave de API de Oppizi.

1. Entra en Oppizi.
2. Ve a **Integraciones** > **Braze**.
3. Genera tu clave de API.

Desde esta página puedes gestionar, revocar y crear tus claves cuando lo necesites.

### Paso 2: Crear una plantilla de webhook Braze

A continuación, crea una plantilla de webhook para Oppizi en Braze para utilizarla en futuras campañas o Lienzos.

1. En Braze, ve a **Plantillas** > **Plantillas webhook**.

En tu plantilla webhook, rellena los siguientes campos:

- **URL del webhook:** ```https://webhooks.oppizi.com/events```
- **Cuerpo de la solicitud:** **Texto sin procesar**

Para el método de solicitud y las cabeceras, Oppizi requiere que se incluya en la plantilla un método HTTP junto con las siguientes cabeceras HTTP. Rellena los siguientes campos:

- **Método HTTP:** POST
- **Encabezados de solicitud:**
  - **Autorización:** `Bearer <oppiziAPIKey>`
  - **Tipo de contenido:** `application/json`

![Un ejemplo de la cabecera del webhook Oppizi en Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Para el **Cuerpo de la solicitud**, debes incluir el campo **oppiziWorkflowID**. Este ID se genera cuando se crea un flujo de trabajo en Oppiz y es necesario para especificar a qué flujo de trabajo de correo directo deben añadirse tus destinatarios. Cada flujo de trabajo de correo directo en Oppizi tiene un ID único, así que si creas una plantilla de webhook de Oppizi en Braze, asegúrate de actualizar siempre el ID del flujo de trabajo al correcto.

{% alert note %}
Comprueba que los atributos personalizados requeridos están configurados en tu cuenta Braze para las direcciones postales de tus destinatarios, ya que son necesarios para enviar correo directo.
{% endalert %}

![Un ejemplo de plantilla de webhook Oppizi en Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

A continuación se muestra un ejemplo de cuerpo de solicitud:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Paso 3: Crear un flujo de trabajo de correo directo en Oppizi

1. En Oppizi, ve a **Flujo de trabajo de correo directo** > **Crear flujo de trabajo**
2. Configura los detalles del flujo de trabajo, incluyendo umbrales, ondas, formato de postal e ilustraciones.
3. En la sección de detalles del webhook, encontrarás un cuerpo de solicitud listo para usar, incluido el ID de tu flujo de trabajo, que puedes pegar directamente en Braze.

### Paso 4: Vista previa y prueba de tu solicitud en Braze

Después de añadir el cuerpo de tu solicitud con el ID del flujo de trabajo de Oppizi, realiza una prueba para confirmar que tu configuración funciona como esperabas.

Para ejecutar la prueba, actualiza `requestType` de `live` a `test` en el cuerpo de la solicitud. Ten en cuenta que este paso es crucial para evitar añadir destinatarios de prueba a tu audiencia de correo directo.

Cuando termines las pruebas, actualiza `requestType` de nuevo a `live` y guarda tu Canvas. Ahora ya estás listo para lanzar tus campañas automatizadas de correo directo.
