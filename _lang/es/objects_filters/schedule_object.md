---
nav_title: "Objeto de programación"
article_title: Objeto de programación de API
page_order: 12
page_type: reference
description: "Este artículo de referencia enumera y explica los diferentes objetos de programación utilizados en Braze."

---

# Objeto de programación

> Los parámetros de los puntos finales de creación de campañas y programación de Canvas son idénticos a los del punto final de envío y añaden el parámetro `schedule`, que te permite especificar cuándo quieres que tus usuarios objetivo reciban tu mensaje. Si sólo incluyes el parámetro `time` en el objeto `schedule`, todos tus usuarios recibirán mensajes en ese momento.

Si configuras `in_local_time` para que sea `true`, obtendrás una respuesta de error si el parámetro de la hora ha pasado en todas las zonas horarias. Si estableces `at_optimal_time` como verdadero, tus usuarios recibirán el mensaje en la fecha designada a la hora óptima (independientemente de la hora que tú indiques). Cuando utilices el envío de hora local u óptima, no proporciones designadores de zona horaria en el valor del parámetro de hora (por ejemplo, utiliza `"2015-02-20T13:14:47"` en lugar de `"2015-02-20T13:14:47-05:00"`).

La respuesta te proporcionará una dirección `schedule_id` que deberás guardar por si más adelante necesitas cancelar o actualizar el mensaje programado:

## Cuerpo del objeto

Inserta este objeto cuando sea necesario para programar tus mensajes.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Respuesta de ID de programación

Recibirás un `schedule_id` para el mensaje programado que creaste.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

Si utilizas la API para llamadas de servidor a servidor, puede que tengas que permitir la URL de la API correspondiente si están detrás de un cortafuegos.

Las respuestas del punto final de programación de mensajes incluirán la dirección `dispatch_id` del mensaje como referencia para el envío del mensaje. El `dispatch_id` es el ID del envío del mensaje (ID único para cada "transmisión" enviada desde Braze).

