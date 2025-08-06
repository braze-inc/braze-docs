---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Este artículo de referencia describe la asociación entre Braze y Radar, una plataforma de geofencing, para añadir contexto de localización y seguimiento a tus aplicaciones iOS y Android."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) es la principal plataforma de geovallado y seguimiento de ubicación. La plataforma Radar tiene tres productos principales: [Geovallas](https://radar.io/product/geofencing), [seguimiento de viajes](https://radar.io/product/trip-tracking) y [API geográficas](https://radar.io/product/api). La combinación de la plataforma de interacción líder del sector Braze y las capacidades de geovallado líderes del sector de Radar te permite impulsar los ingresos y la fidelización a través de una amplia gama de experiencias de productos y servicios basadas en la ubicación. Entre ellas se incluyen el seguimiento de la recogida y la entrega, las notificaciones activadas por la ubicación, la personalización contextual, la verificación de la ubicación, los localizadores de tiendas, la función de autocompletar direcciones, etc.

_Esta integración está mantenida por Radar._

## Sobre la integración

La integración de Braze y Radar le permite acceder a sofisticados activadores de campañas basados en la ubicación y al enriquecimiento del perfil del usuario con datos de ubicación enriquecidos y de primera mano. Cuando se generan eventos de geovalla Radar o de seguimiento de viajes, los eventos personalizados y los atributos de usuario se envían a Braze en tiempo real. Estos eventos y atributos pueden utilizarse para lanzar campañas basadas en la localización, impulsar operaciones de recogida y entrega en el último kilómetro, supervisar la logística de flotas y envíos o crear segmentos de usuarios basados en patrones de localización. 

Además, las Geo API de Radar pueden aprovecharse para enriquecer o personalizar sus campañas de marketing a través [del Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta radar | Se necesita una cuenta Radar para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Identificador de la aplicación | Puede encontrar [el identificador de su aplicación]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) en el panel de control de Braze, en **Configuración** > **Claves de API**. |
| Clave API de iOS<br>Clave API de Android | Estas claves API se pueden encontrar en el panel de control de Braze desde **Configuración** > **Configuración de la aplicación**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

Para asignar datos entre los SDK de Braze y Radar, debe establecer los mismos ID de usuario o alias de usuario en ambos sistemas. Esto puede hacerse utilizando el método `changeUser()` del SDK de Braze y el método `setUserId()` del SDK de Radar.

Para activar la integración:

1. En Radar, en la página [Integraciones](https://radar.com/documentation/integrations), localice Braze.
1. Establezca **Activado** en **Sí**.
3. Introduce el identificador de tu aplicación y las claves API.

{% alert note %}
Puedes establecer claves de API distintas para los entornos de prueba y en vivo.
{% endalert %}

{:start="4"}
4\. Selecciona tu punto final Braze.
5\. Introduzca cualquier filtro de eventos o atributos de eventos para garantizar que sólo se envían a Braze los datos relevantes para el marketing de captación. Siempre que se generen eventos Radar, Radar enviará eventos personalizados y atributos de usuario a Braze. Los eventos de dispositivos iOS se enviarán utilizando sus claves API de iOS; los eventos y atributos de usuario de dispositivos Android se enviarán utilizando sus claves API de Android.

{% alert note %}
Por defecto, Radar `userId` mapea a los `external_id` de Braze para los usuarios registrados. Sin embargo, puede realizar un seguimiento de los usuarios que han cerrado sesión o especificar asignaciones personalizadas configurando Radar `metadata.brazeAlias` o `metadata.brazeExternalId`. Si establece `metadata.brazeAlias`, también debe añadir un alias correspondiente en Braze con la etiqueta `radarAlias`.
{% endalert %}

## Casos de uso basados en eventos y atributos

Puede utilizar eventos personalizados y atributos de usuario para crear segmentos basados en la ubicación o activar campañas basadas en la ubicación.

### Activar una notificación de llegada a la tienda para la recogida en acera 

Envía una notificación push al usuario con instrucciones de llegada cuando llegue a tu tienda para una recogida en acera.

![Una campaña de entrega basada en acciones que muestra que la campaña se entregará cuando se produzca el evento personalizado "arrived_at_trip_destination" y los "trip_metadata" sean iguales a "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})

### Crear un segmento de audiencia de visitantes recientes de la tienda

Por ejemplo, diríjase a cualquier usuario que haya visitado su tienda en los últimos 7 días, tanto si ha realizado una compra como si no.

![Un segmento en el que "radar_geofence_tags" incluye el valor my_store y "radar_updated_at" fue hace menos de 7 días.]({% image_buster /assets/img_archive/radar-segment.png %})

## Contenido conectado

El siguiente ejemplo muestra cómo realizar una promoción para llevar a los usuarios cercanos a la tienda con una oferta digital. 

![Una imagen de Android de un mensaje push de contenido conectado que muestra "Nuevas ofertas en tienda, Walmart y Target cerca de ti".]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

Para empezar, necesitará tener a mano su clave de API publicable de Radar para utilizarla en sus URL de solicitud.

A continuación, dentro de una etiqueta `connected_content`, haz una petición GET a [la API Search Places](https://radar.io/documentation/api#search-places). La API de búsqueda de lugares devuelve ubicaciones cercanas basadas en [Radar Places](https://radar.io/documentation/places): una base de datos de ubicaciones de lugares, cadenas y categorías que proporciona una visión completa del mundo.

El siguiente fragmento de código es un ejemplo de lo que Radar devolverá como objeto JSON de la llamada a la API:

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Para construir el mensaje Braze personalizado y orientado al contenido conectado, puede aprovechar el atributo Braze `most_recent_location` como entrada para el parámetro `near` en la URL de la solicitud de API. El atributo `most_recent_location` se recoge a través de la integración de eventos Radar o directamente a través del SDK Braze.

En el siguiente ejemplo, el filtrado de la cadena Radar se aplica a las ubicaciones de Target y Walmart, y el radio de búsqueda de las ubicaciones cercanas se establece en 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Como puede ver en la etiqueta `connect_content`, el objeto JSON se almacena en la variable local `nearbyplaces` añadiendo `:save nearbyplaces` después de la URL.
Puedes probar cuál debería ser la salida consultando {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Uniendo nuestro caso de uso, he aquí cómo sería la sintaxis de la campaña. El siguiente código itera a través del objeto `nearbyplaces.places`, extrayendo valores únicos y concatenándolos con delimitadores legibles por humanos adecuados para el mensaje.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
Visita [la documentación de Radar](https://radar.io/documentation/api) para ver todas las API de Radar que pueden aprovecharse en el contenido conectado.
{% endalert %}


