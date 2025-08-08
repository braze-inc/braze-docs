---
nav_title: API e identificadores
article_title: API e identificadores
page_order: 3
page_type: reference
description: "Este artículo trata de la página de APIs e identificadores, que muestra los identificadores de API para tu espacio de trabajo."

---

# Claves de API

> La página **APIs e identificadores** es tu eje centralizado para gestionar todas tus claves de API REST en un solo lugar. Aquí puedes acceder al conjunto de claves de API e identificadores de aplicación de cada espacio de trabajo.

Puedes encontrar la página **API e identificadores** en **Configuración**.

### Claves de API

Esta sección proporciona las claves REST API de su espacio de trabajo, los identificadores únicos que le permiten acceder a sus datos para un espacio de trabajo. Se requiere una clave de API REST con cada solicitud a la API Braze. Para obtener más información sobre la creación y el uso de claves de API, consulta nuestro [resumen de claves de API REST]({{site.baseurl}}/api/api_key/).

#### Lista de direcciones IP permitidas de la API

Para mayor seguridad, puedes especificar una lista de direcciones IP y subredes a las que se permite realizar solicitudes de API REST para una clave de API REST determinada. Esto se denomina lista blanca o lista permitida. Para permitir direcciones IP o subredes específicas, añádalas a la sección **Lista blanca de IP** al crear una nueva clave de API de REST: 

![Sección de listas blancas de IP de API al crear una nueva clave de API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si no especifica ninguna, las peticiones pueden enviarse desde cualquier dirección IP.

{% alert tip %}
¿Hacer un webhook Braze-to-Braze y utilizar allowlisting? Consulta nuestra lista de [IPs en lista blanca]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### Identificadores de la aplicación

Esta sección incluye una lista de identificadores utilizados para hacer referencia a aplicaciones específicas en las solicitudes realizadas a la API Braze. Para saber más sobre los identificadores de aplicación, consulta [Identificador de aplicación clave de API]({{site.baseurl}}/api/identifier_types/).

### Otros identificadores

Para integrarse con nuestra API, puede buscar los identificadores relacionados con cualquier segmento, campaña, tarjeta de contenido, etc., a los que desee acceder desde la API externa de Braze. Todos los mensajes deben seguir la codificación [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Después de seleccionar cualquiera de ellos, el identificador aparecerá debajo del menú desplegable.

Para más información, consulta [Tipos de identificadores API]({{site.baseurl}}/api/identifier_types/).

