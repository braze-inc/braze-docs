---
nav_title: "Objeto del evento"
article_title: Objeto de evento API
page_order: 6
page_type: reference
description: "Este artículo de referencia repasa el objeto evento, qué es y cómo es una parte crucial de las estrategias de campaña basadas en eventos."

---

# Objeto del evento

> Este artículo explica los distintos componentes de un objeto evento, cómo puedes utilizarlo y ejemplos en los que inspirarte.

## ¿Qué es un objeto de evento?

Un objeto de evento es un objeto que se pasa a través de la API cuando se produce un evento específico. Los objetos de eventos se alojan en una matriz de eventos. Cada objeto evento de la matriz de eventos representa una única ocurrencia de un evento personalizado por un usuario concreto en el valor de tiempo designado. El objeto evento tiene muchos campos diferentes que te permiten personalizar mediante la configuración y el uso de propiedades del evento en los mensajes, la recopilación de datos y la personalización.

Para saber cómo configurar eventos personalizados para una plataforma concreta, consulta la Guía de integración de plataformas en la [Guía del desarrollador]({{site.baseurl}}/developer_guide/home/). Consulta el artículo correspondiente según tu plataforma:

- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Cuerpo del objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [ID usuario externo]({{site.baseurl}}/api/basics/#user-ids)
- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)
- [Código de tiempo ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

#### Actualizar solo los perfiles existentes

Para actualizar sólo los perfiles de usuario existentes en Braze, debes pasar la clave `_update_existing_only` con un valor de `true` dentro del cuerpo de tu solicitud. Si se omite este valor, Braze creará un nuevo perfil de usuario si `external_id` no existe ya.

{% alert note %}
Si estás creando un perfil de usuario de sólo alias a través del punto final `/users/track`, `_update_existing_only` debe estar configurado como `false`. Si se omite este valor, no se creará el perfil de solo alias.
{% endalert %}

## Objeto de propiedades del evento

Los eventos personalizados y las compras pueden tener propiedades del evento. Los valores de las "propiedades" deben ser un objeto en el que las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de las propiedades deben ser cadenas no vacías de menos o igual a 255 caracteres, sin signos de dólar ($) al principio.

Los valores de propiedad pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [números enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | `true` o `false` |
| Fechas y horas | Deben formatearse como cadenas en el formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) o en cualquiera de los siguientes formatos: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>No se admite dentro de matrices. <br><br>Ten en cuenta que la "T" es un indicador de tiempo, no un marcador de posición, y no debe cambiarse ni eliminarse. <br><br>Los atributos de tiempo sin zona horaria serán predeterminados a medianoche UTC (y se formatearán en el panel como el equivalente a medianoche UTC en la zona horaria de la empresa). <br><br> Los eventos con marcas de tiempo en el futuro serán predeterminados a la hora actual.  |
| Cadenas | 255 caracteres o menos. |
| Matrices | Las matrices no pueden incluir fechas. |
| Objetos | Los objetos se ingestarán como cadenas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 100 KB.

### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades del evento personalizado:

- `time`
- `event_name`

{% alert important %}
El uso de claves reservadas como nombres de propiedades de eventos personalizados provocará errores de API al enviar solicitudes al punto final `/users/track`.
{% endalert %}

### Persistencia de las propiedades del evento

Las propiedades del evento están diseñadas para filtrar los mensajes desencadenados por sus eventos principales y para personalizarlos con Liquid. De forma predeterminada, no persisten en el perfil de usuario de Braze. Para utilizar los valores de las propiedades del evento en la segmentación, consulta los [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/), donde se detallan los distintos enfoques para almacenar los valores de las propiedades del evento a largo plazo.

#### Solicitud de ejemplo de evento

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [Wiki de código de hora ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)

## Objetos de evento

Utilizando el ejemplo proporcionado, podemos ver que alguien vio recientemente un tráiler y después alquiló una película. Aunque no podemos entrar en una campaña y segmentar a los usuarios en función de estas propiedades, sí podemos utilizarlas estratégicamente utilizándolas en forma de recibo, para enviar un mensaje personalizado a través de un canal utilizando Liquid. Por ejemplo, "Hola **Beth**, Gracias por alquilar **El huevo triste** de **Dan Alexander**, aquí tienes algunas películas recomendadas basadas en tu alquiler..."


