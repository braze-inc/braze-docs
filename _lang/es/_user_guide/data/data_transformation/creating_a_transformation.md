---
nav_title: Crear una transformación
article_title: Crear una transformación
page_order: 1
page_type: reference
description: "Este artículo de referencia proporciona los pasos para crear una transformación utilizando la Transformación de Datos Braze."
---

# Crear una transformación

> Braze Data Transformation le permite crear y gestionar integraciones webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estas integraciones de webhooks pueden impulsar casos de uso de marketing aún más sofisticados. Puede crear su transformación de datos a partir del código predeterminado o utilizando nuestra biblioteca de plantillas específica para ayudarle a empezar con determinadas plataformas externas.

## Requisitos previos 

| Requisito | Descripción |
| --- | --- |
| Autenticación de dos factores o SSO | Debe tener activada [la autenticación de dos factores]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) o [el inicio de sesión único]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) para su cuenta. |
| Permisos correctos | Debe ser administrador de la cuenta o del espacio de trabajo, o tener permisos de usuario para "Gestionar transformaciones". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Paso 1: Identificar una plataforma de origen

Identifica una plataforma externa que quieras conectar a Braze y comprueba que la plataforma admite webhooks. Estas configuraciones se denominan a veces "notificaciones API" o "solicitudes de servicio Web".

A continuación se muestra un ejemplo de [webhook de Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), que se puede configurar iniciando sesión en su plataforma:

![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Paso 2: Crear una transformación

{% multi_lang_include create_transformation.md location="default" %}

## Paso 3: Enviar un webhook de prueba (recomendado)

Este paso es opcional, pero recomendamos enviar un webhook de prueba desde su plataforma de origen a su transformación recién creada.

1. Copie la URL de su transformación.
2. En su plataforma de origen, busque la función "Enviar prueba" para que genere un webhook de ejemplo para enviarlo a esta URL. 
- Si su plataforma de origen le pide un tipo de solicitud, seleccione **POST**.
- Si tu plataforma de origen proporciona opciones de autenticación, selecciona **Sin autenticación**.
- Si tu plataforma de origen te pide secretos, selecciona **Sin secretos**.
3. Actualiza tu página en el panel de Braze para ver si se ha recibido el webhook. Si se ha recibido, deberías ver la carga útil del webhook en **Webhook más reciente**.

Esto es lo que parece para Typeform:

![Ejemplo de código de transformación de datos que mapea el webhook a perfiles de usuario Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Es posible que Braze Data Transformation aún no admita plataformas externas que requieran una verificación o autenticación especial para los webhooks. Considere la posibilidad de dejar [comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) si está interesado en utilizar este tipo de plataforma con Braze Data Transformation.
{% endalert %}

## Paso 4: Escribir código de transformación

Si tiene poca o ninguna experiencia con código JavaScript o prefiere instrucciones más detalladas, siga las instrucciones de **Beginner - POST: Seguimiento de usuarios** o **Principiante - PUT: Actualizar varios elementos del catálogo** pestaña para escribir su código de transformación.

Si eres desarrollador o tienes mucha experiencia con código JavaScript, sigue las instrucciones de **Avanzado - POST: Seguimiento de usuarios** pestaña para obtener instrucciones de alto nivel en la escritura de su código de transformación.

{% alert tip %}
La Transformación de Datos Braze tiene un copiloto de IA que pide a ChatGPT que te ayude a escribir tu código. Para acceder al copiloto de IA, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Generar código de transformación**. Para utilizarlo, debe enviarse un webhook a su transformación. También puede acceder a la biblioteca de plantillas seleccionando **Insertar código** > **Insertar plantilla**.

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Principiante - Seguimiento de usuarios %}

Aquí, escribe código de transformación para definir cómo mapear varios valores de webhook a perfiles de usuario Braze.

1. Las nuevas transformaciones tienen esta plantilla predeterminada en la sección **Código de transformación**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Para incluir atributos personalizados, eventos personalizados y compras en tus llamadas de transformación, salta al paso 3. Si no, suprime las secciones que no necesites.<br><br>
3\. Cada atributo, evento y objeto de compra requiere un identificador de usuario, ya sea `external_id`, `user_alias`, `braze_id`, `email` o `phone`. Encuentra el identificador de usuario en la carga útil del webhook entrante, y la plantilla en ese valor en su código de transformación a través de una línea de carga útil. Utilice la notación de puntos para acceder a las propiedades del objeto de carga útil. <br><br>
4\. Encuentra los valores webhook que te gustaría representar como atributos, eventos o compras, y plantilla esos valores en tu código de transformación a través de una línea de carga útil. Utilice la notación de puntos para acceder a las propiedades del objeto de carga útil.<br><br>
5\. Para cada atributo, evento y objeto de compra, examina el valor `_update_existing_only`. Establézcalo en `false` si desea que la transformación cree un nuevo usuario que puede no existir. Déjelo en `true` para actualizar sólo los perfiles existentes.<br><br>
6\. Haga clic en **Validar** para obtener una vista previa de la salida de su código y comprobar si se trata de una solicitud aceptable de `/users/track`.<br><br>
7\. Activa tu transformación. Para obtener ayuda adicional con su código antes de activarlo, póngase en contacto con su gestor de cuenta Braze.<br><br>
7\. Haga que su plataforma de origen comience a enviar webhooks. Su código de transformación se ejecutará para cada webhook entrante, y los perfiles de usuario comenzarán a actualizarse. 

La integración del webhook ya está completa.

{% endtab %}
{% tab Principiante - Actualizar elementos del catálogo %}

Aquí puedes escribir código de transformación para definir cómo quieres mapear varios valores de webhook a actualizaciones de elementos del catálogo Braze.

1. Las nuevas transformaciones incluirán esta plantilla por defecto en la sección **Código de transformación**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. Las transformaciones para destinos `/catalogs` requieren que `catalog_name` defina el catálogo específico que se va a actualizar. Puedes codificar este campo o crear una plantilla con un campo webhook a través de una línea de carga útil. Utilice la notación de puntos para acceder a las propiedades del objeto de carga útil.<br><br>
3\. Define qué elementos quieres actualizar en el catálogo con los campos `id` de la matriz de elementos. Usted puede codificar estos campos, o la plantilla en un campo webhook a través de una línea de carga útil. <br><br> Ten en cuenta que `catalog_column` es un valor marcador de posición. Asegúrese de que los objetos de artículo sólo contienen campos que existen en el catálogo.<br><br>
4\. Selecciona **Validar** para obtener una vista previa de la salida de tu código y comprobar si es una solicitud aceptable para el [punto final Actualizar varios elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5\. Activa tu transformación. Para obtener ayuda adicional con su código antes de activarlo, póngase en contacto con su gestor de cuenta Braze.<br><br>
6\. Asegúrese de comprobar si su plataforma de origen tiene una configuración para iniciar el envío de webhooks. Su código de transformación se ejecutará para cada webhook entrante, y los elementos del catálogo comenzarán a actualizarse.

La integración del webhook ya está completa.

{% endtab %}
{% tab Avanzado - Seguimiento de usuarios %}

En este paso, transformarás la carga útil del webhook de la plataforma de origen en un valor de retorno de objeto JavaScript. Este valor de retorno debe seguir el formato del cuerpo de la solicitud del punto final `/users/track`:

- El código de transformación se acepta en el lenguaje de programación JavaScript. Se admite cualquier flujo de control estándar de JavaScript, como la lógica if/else.
- El código de transformación accede al cuerpo de la solicitud del webhook a través de la variable `payload`. Esta variable es un objeto poblado por el análisis del cuerpo de la solicitud JSON.
- Se admite cualquier característica de nuestro punto final `/users/track`, incluidos:
  - Objetos de atributos de usuario, objetos de evento y objetos de compra
  - Atributos anidados y propiedades anidadas de eventos personalizados
  - Actualizaciones de grupos de suscripción
  - Dirección de correo electrónico como identificador

Seleccione **Validar** para obtener una vista previa de la salida de su código y comprobar si se trata de una solicitud aceptable de `/users/track`.

{% alert note %}
Actualmente no se admiten solicitudes de red externa, bibliotecas de terceros ni webhooks que no sean JSON.
{% endalert %}

{% endtab %}
{% endtabs %}

## Paso 5: Supervise su transformación

Tras activar tu transformación, consulta los análisis de la página principal de **Transformaciones** para ver un resumen del rendimiento.

* **Solicitudes entrantes:** Es el número de webhooks recibidos en la URL de esta transformación. Si las solicitudes entrantes son 0, su plataforma de origen no ha enviado ningún webhook, o la conexión no se puede realizar.
* **Entregas:** Tras recibir las solicitudes entrantes, Data Transformation aplica su código de transformación para enviarlas al destino Braze seleccionado.

Es un buen objetivo que el 100 % de las solicitudes entrantes den lugar a entregas. El número de entregas nunca superará el número de solicitudes entrantes.

### Solución de problemas

Para una supervisión y solución de problemas más detalladas, consulta la página **Registros** para ver registros específicos, que es donde se registran las últimas 1.000 peticiones entrantes a todas las transformaciones de tus espacios de trabajo. Puedes seleccionar cada registro para ver el cuerpo de la solicitud entrante, la salida de la transformación y el cuerpo de la respuesta del destino de la transformación.

Si no hay entregas, comprueba que tu código de transformación no contenga errores de sintaxis y confirma que el código se compila. A continuación, comprueba si la salida es una solicitud de destino válida.

Las entregas inferiores al número de solicitudes entrantes indican que al menos algunos webhooks se entregan correctamente. Consulte los registros de transformación para ver ejemplos de errores y compruebe si la salida de la transformación es la esperada. Es posible que su código de transformación no tenga en cuenta todas las variaciones de los webhooks recibidos.


