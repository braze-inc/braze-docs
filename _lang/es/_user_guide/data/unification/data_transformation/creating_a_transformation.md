---
nav_title: Crear una transformación
article_title: Crear una transformación
page_order: 1
page_type: reference
description: "Este artículo de referencia proporciona los pasos para crear una transformación utilizando la Transformación de Datos Braze."
---

# Crear una transformación

> La Transformación de Datos Braze te habilita para construir y administrar integraciones webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estas integraciones de webhook pueden impulsar casos de uso de marketing aún más sofisticados. Puedes construir tu Transformación de Datos a partir de código predeterminado, o utilizando nuestra biblioteca de plantillas dedicada para ayudarte a empezar con determinadas plataformas externas.

## Requisitos previos 

| Requisito | Descripción |
| --- | --- |
| Autenticación de dos factores o SSO | Debes tener habilitada la [autenticación de dos factores]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) o [el inicio de sesión único]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) para tu cuenta. |
| Permisos correctos | Debes ser administrador de una cuenta o de un espacio de trabajo, o tener permisos de usuario para "Gestionar transformaciones". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Paso 1: Identificar una plataforma de origen

Identifica una plataforma externa que quieras conectar a Braze y comprueba que la plataforma admite webhooks. Estas configuraciones se denominan a veces "notificaciones API" o "solicitudes de servicio Web".

A continuación se muestra un ejemplo de [webhook de Typeform](https://www.typeform.com/help/a/webhooks-360029573471/), que se puede configurar iniciando sesión en su plataforma:

\![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Paso 2: Crea una transformación

{% multi_lang_include create_transformation.md location="default" %}

## Paso 3: Envía un webhook de prueba (recomendado)

Este paso es opcional, pero te recomendamos que envíes un webhook de prueba desde tu plataforma de origen a tu transformación recién creada.

1. Copia la URL de tu transformación.
2. En tu plataforma de origen, busca la función "Enviar prueba" para que genere un webhook de muestra que enviar a esta URL. 
- Si tu plataforma de origen te pide un tipo de solicitud, selecciona **POST**.
- Si tu plataforma de origen proporciona opciones de autenticación, selecciona **Sin autenticación**.
- Si tu plataforma de origen te pide secretos, selecciona **Sin secretos**.
3. Actualiza tu página en el panel de Braze para ver si se ha recibido el webhook. Si se ha recibido, deberías ver la carga útil del webhook en **Webhook más reciente**.

Esto es lo que parece para Typeform:

\![Ejemplo de código de transformación de datos que mapea el webhook a perfiles de usuario Braze.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Es posible que la Transformación de Datos Braze aún no admita plataformas externas que requieran una verificación o autenticación especial para los webhooks. Considera la posibilidad de dejar [comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) si estás interesado en utilizar este tipo de plataforma con Braze Data Transformation.
{% endalert %}

## Paso 4: Escribe el código de transformación

Si tienes poca o ninguna experiencia con código JavaScript o prefieres instrucciones más detalladas, sigue las instrucciones de **Principiante - POST: Seguimiento de usuarios** o **Principiante - PUT: Actualizar varios elementos del catálogo** pestaña para escribir tu código de transformación.

Si eres desarrollador o tienes mucha experiencia con el código JavaScript, sigue las instrucciones de **Avanzado - POST: Seguimiento de usuarios** pestaña para obtener instrucciones de alto nivel sobre cómo escribir tu código de transformación.

{% alert tip %}
La Transformación de Datos Braze tiene un copiloto de IA que pide a ChatGPT que te ayude a escribir tu código. Para acceder al copiloto de IA, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Generar código de transformación**. Para utilizarlo, hay que enviar un webhook a tu transformación. También puedes acceder a la biblioteca de plantillas seleccionando **Insertar código** > **Insertar plantilla**.

\![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

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
2\. Para incluir atributos personalizados, eventos personalizados y compras en tus llamadas de transformación, salta al paso 3. Si no, elimina las secciones que no necesites.<br><br>
3\. Cada atributo, evento y objeto de compra requiere un identificador de usuario, ya sea `external_id`, `user_alias`, `braze_id`, `email` o `phone`. Busca el identificador de usuario en la carga útil del webhook entrante, y plantilla ese valor en tu código de transformación mediante una línea de carga útil. Utiliza la notación por puntos para acceder a las propiedades del objeto carga útil. <br><br>
4\. Busca los valores del webhook que te gustaría representar como atributos, eventos o compras, y plantilla esos valores en tu código de transformación mediante una línea de carga útil. Utiliza la notación por puntos para acceder a las propiedades del objeto carga útil.<br><br>
5\. Para cada atributo, evento y objeto de compra, examina el valor `_update_existing_only`. Establécelo en `false` si quieres que la transformación cree un nuevo usuario que puede no existir. Déjalo como `true` para actualizar sólo los perfiles existentes.<br><br>
6\. Haz clic en **Validar** para obtener una vista previa de la salida de tu código y comprobar si se trata de una solicitud aceptable de `/users/track`.<br><br>
7\. Activa tu transformación. Para obtener ayuda adicional con tu código antes de activarlo, ponte en contacto con tu director de cuentas Braze.<br><br>
7\. Haz que tu plataforma de origen comience a enviar webhooks. Tu código de transformación se ejecutará para cada webhook entrante, y los perfiles de usuario comenzarán a actualizarse. 

¡Tu integración webhook ya está completa!

{% endtab %}
{% tab Beginner - Update catalog items %}

Aquí puedes escribir código de transformación para definir cómo quieres mapear varios valores de webhook a actualizaciones de elementos del catálogo Braze.

1. Las nuevas transformaciones incluirán esta plantilla predeterminada en la sección **Código de transformación**:

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
2\. Las transformaciones para destinos `/catalogs` requieren que `catalog_name` defina el catálogo específico que se va a actualizar. Puedes codificar este campo o crear una plantilla con un campo webhook a través de una línea de carga útil. Utiliza la notación por puntos para acceder a las propiedades del objeto carga útil.<br><br>
3\. Define qué elementos quieres actualizar en el catálogo con los campos `id` de la matriz de elementos. Puedes utilizar código duro en estos campos, o una plantilla en un campo webhook a través de una línea de carga útil. <br><br> Ten en cuenta que `catalog_column` es un valor marcador de posición. Asegúrate de que los objetos de artículo sólo contienen campos que existen en el catálogo.<br><br>
4\. Selecciona **Validar** para obtener una vista previa de la salida de tu código y comprobar si es una solicitud aceptable para el [punto final Actualizar varios elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items).<br><br>
5\. Activa tu transformación. Para obtener ayuda adicional con tu código antes de activarlo, ponte en contacto con tu director de cuentas Braze.<br><br>
6\. Asegúrate de comprobar si tu plataforma de origen tiene una configuración para iniciar el envío de webhooks. Tu código de transformación se ejecutará para cada webhook entrante, y los elementos del catálogo comenzarán a actualizarse.

¡Tu integración webhook ya está completa!

{% endtab %}
{% tab Advanced - Track users %}

En este paso, transformarás la carga útil del webhook de la plataforma de origen en un valor de retorno de objeto JavaScript. Este valor de retorno debe seguir el formato del cuerpo de la solicitud del punto final `/users/track`:

- El código de transformación se acepta en el lenguaje de programación JavaScript. Se admite cualquier flujo de control estándar de JavaScript, como la lógica if/else.
- El código de transformación accede al cuerpo de la solicitud del webhook a través de la variable `payload`. Esta variable es un objeto rellenado al analizar el JSON del cuerpo de la solicitud.
- Se admite cualquier característica de nuestro punto final `/users/track`, incluida:
  - Objetos de atributos de usuario, objetos de evento y objetos de compra
  - Atributos anidados y propiedades de eventos personalizados anidados
  - Actualizaciones del grupo de suscripción
  - Dirección de correo electrónico como identificador

Selecciona **Validar** para obtener una vista previa de la salida de tu código y comprobar si es una solicitud aceptable de `/users/track`.

{% alert note %}
Actualmente no se admiten solicitudes de red externa, bibliotecas de terceros ni webhooks que no sean JSON.
{% endalert %}

{% endtab %}
{% endtabs %}

## Paso 5: Controla tu transformación

Tras activar tu transformación, consulta los análisis de la página principal de **Transformaciones** para ver un resumen del rendimiento.

* **Solicitudes entrantes:** Es el número de webhooks recibidos en la URL de esta transformación. Si las solicitudes entrantes son 0, tu plataforma de origen no ha enviado ningún webhook, o no se puede establecer la conexión.
* **Entregas:** Tras recibir las solicitudes entrantes, Transformación de Datos aplica tu código de transformación para enviarlas al destino Braze que hayas seleccionado.

Es un buen objetivo que el 100% de las solicitudes entrantes den lugar a entregas. El número de entregas nunca superará el número de solicitudes recibidas.

### Solución de problemas

Para una supervisión y solución de problemas más detalladas, consulta la página **Registros** para ver registros específicos, que es donde se registran las últimas 1.000 peticiones entrantes a todas las transformaciones de tus espacios de trabajo. Puedes seleccionar cada registro para ver el cuerpo de la solicitud entrante, la salida de la transformación y el cuerpo de la respuesta del destino de la transformación.

Si no hay entregas, comprueba que tu código de transformación no contenga errores de sintaxis y confirma que el código se compila. A continuación, comprueba si la salida es una petición de destino válida.

Las entregas inferiores al número de solicitudes entrantes indican que al menos algunos webhooks se entregan correctamente. Consulta los registros de transformación para ver ejemplos de errores, y comprueba si la salida de la transformación es la esperada. Es posible que tu código de transformación no tenga en cuenta todas las variaciones de los webhooks recibidos.


