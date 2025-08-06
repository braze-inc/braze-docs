---
nav_title: Contenido
article_title: Contenido
description: "Este artículo de referencia describe la asociación entre Braze y Contentful, un sistema de gestión de contenidos que te permite utilizar dinámicamente el Contenido Conectado para extraer contenido de Contentful en tus campañas Braze."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contenido

>[Contentful](https://www.contentful.com/) es un sistema de gestión de contenidos sin cabeza que te permite crear, gestionar y distribuir contenidos a cualquier plataforma. A diferencia de un sistema de gestión de contenidos (CMS), Contentful te permite crear tu modelo de contenidos para que puedas decidir qué contenidos quieres gestionar.<br><br>Esta página proporciona una guía paso a paso para configurar el contenido conectado de Braze para obtener datos de la API de entrega de contenido de Contentful. 

Una vez integrado, puedes utilizar las API RESTful de Contentful para entregar tu contenido a través de múltiples canales, como sitios web, aplicaciones móviles (iOS, Android y Windows) o muchas otras plataformas. También puedes extraer contenido dinámicamente de Contentful para utilizarlo en tus campañas Braze.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                        |
|-----------------------|------------------------------------|
| A Cuenta de contenido | Necesitas una cuenta de Contentful con acceso a la API de entrega de contenidos. |
| Una cuenta Braze | Necesitas una cuenta Braze con acceso a la característica Contenido conectado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Obtén tus credenciales API de Contentful

1. [Inicia sesión en Contentful](https://app.contentful.com/login) con tus credenciales.
2. Crea o recupera tokens de acceso a la API en el panel de control de Contentful yendo a **Configuración** > **Claves de API**. Si aún no tienes una clave de API, crea una nueva:<br>2.1 Selecciona **Añadir clave de API**.<br>2.2 Introduce los datos necesarios y selecciona el entorno adecuado.<br>2.3 Selecciona **Guardar** y anota el **ID del espacio** y el **token de acceso a la API de entrega de contenidos**.
3. Identifica el modelo de contenido al que quieres acceder a través de la API de Contentful.

### Paso 2: Configurar contenido conectado Braze

1. [Inicia sesión en Braze](https://dashboard.braze.com/sign_in) con tus credenciales.
2. En el panel de Braze, ve a **Plantillas** > **Bloques de contenido** > **Crear bloque de contenido** > **Bloque de contenido HTML**.
3. Crea una solicitud de contenido conectado a la [URL de la API de entrega de contenido de Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). Un ejemplo de URL de la API de entrega de contenidos de Contentful es ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> Recuperar distintos activos requiere incluir variables específicas. El ejemplo de solicitud de URL de contenido conectado se dirige al punto final de [entrada](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) de Contentful. Este punto final necesita variables como `{space_id}` y `{environment_id}`, o `{entry_id}` y `{access_token}`. Se pueden tomar de tu instancia de Contentful. En este ejemplo de Bloque de contenido, las variables deben sustituirse por tu ID de espacio de Contentful y tu ID de entorno.<br><br>La URL de la API de entrega de contenidos de ejemplo utiliza sólo uno de los puntos finales disponibles de Contentful. Se pueden conseguir diferentes casos de uso aprovechando diferentes URL. Por ejemplo, la [API de Imagen](https://www.contentful.com/developers/docs/references/images-api/) puede utilizarse para capturar imágenes almacenadas en Contentful. Para más información, consulta [la API de entrega de contenidos](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Diferentes puntos finales pueden requerir nuevas variables, por ejemplo la API de Imágenes requiere un `{asset_id}`, `{unique_id},` y `{name}`. Para más información, ponte en contacto con Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. Utiliza "Punto final de prueba" para comprobar que Braze puede conectarse correctamente a la API de Contentful y recuperar los datos deseados.
5\. Selecciona **Hecho** para guardar tu Bloque de contenido.
6\. Dale a tu bloque de contenido un nombre descriptivo, como "API Contentful", y luego selecciona **Lanzar bloque de contenido**.

### Paso 3: Utiliza contenido conectado en campañas y lonas

1. En Braze, crea una nueva campaña o edita una existente.
2. Utiliza el bloque de contenido conectado para insertar datos obtenidos de Contentful. Utiliza las rutas de datos que definiste durante la configuración para rellenar dinámicamente el contenido de la campaña.<br><br>
- **Ruta de respuesta:** Tras incluir el Bloque de contenido en una campaña Braze o Canvas, la respuesta estará disponible cuando insertes la variable `{response}` en tu mensaje.<br><br>La notación de puntos JSON te permite especificar qué parte del cuerpo de la respuesta de Contentful quieres incluir en tu mensaje. Esto variará en función de tu caso de uso. Por ejemplo, puedes utilizar el valor del título ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) del punto final Entrada de Contentful y recibir una respuesta como ésta:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. Vista previa y prueba tu campaña para confirmar que los datos de Contenido conectado se muestran correctamente.
4\. Cuando estés satisfecho con la configuración, lanza tu campaña.

## Solución de problemas

### Respuesta API

Asegúrate de que tus credenciales de la API de Contentful y la URL del punto final son correctas. Comprueba si hay mensajes de error en Braze que puedan indicar problemas con la llamada a la API.

### Mapeado de datos

Comprueba que los mapeados de la ruta de respuesta están correctamente configurados y que la estructura de respuesta de la API se ajusta a tus expectativas.

## Recursos adicionales

- [Documentación de la API de entrega de contenidos Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Contenido conectado Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Bloques de contenido Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
