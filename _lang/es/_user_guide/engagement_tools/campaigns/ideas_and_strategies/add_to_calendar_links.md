---
nav_title: Enlaces para añadir al calendario
article_title: Enlaces para añadir al calendario
page_order: 1
page_type: tutorial
description: "Este artículo describe cómo incluir un enlace para añadir al calendario en tus campañas de correo electrónico."
channel: email

---

# Enlaces para añadir al calendario

> Cuando promocione un evento, una venta o una cita, puede ayudar a los usuarios a guardar fácilmente el evento en su calendario añadiendo un enlace "añadir al calendario" a sus correos electrónicos.

Para ello, redacte su correo electrónico y determine dónde quiere que estén sus enlaces. A continuación, añade dos opciones: una para Google Calendar y otra para otros calendarios (como iCal o Outlook). Por ejemplo, "Añadir a Google Calendar" y "Añadir a iCal o Outlook".

![Diálogo de enlace al añadir un enlace en el panel. Se selecciona la pestaña "Información del enlace" y el texto se establece en "Añadir a Google Calendar".][1]{: style="max-width:50%"}

## Formato URL

Añada la siguiente URL a sus enlaces, sustituyendo los marcadores de posición. La única diferencia entre estas dos URL es que Google Calendar necesita un parámetro adicional: `&format=gcal`.

{% tabs %}
{% tab Calendario de Google %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal o Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Sustituye lo siguiente:

- `EVENT_SUBJECT`: Título del evento
- `EVENT_LOCATION`: Ubicación del evento
- `START_TIME`: Hora de inicio del evento en formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC
- `END_TIME`: Hora de finalización del evento en formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC
- `EVENT_DESCRIPTION`: Descripción del evento

Sustituya los espacios por el código de escape HTML `%20`. Por ejemplo, un asunto de "Meet Braze" sería "Meet%20Braze".

Aquí tienes un ejemplo de URL "Añadir a Google Calendar":

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Parámetros adicionales

Los siguientes parámetros son opcionales y pueden utilizarse para definir aspectos adicionales de un evento.

- **Nombre del organizador:** `&organizer=name`
- **Adjuntar URL relacionada con el evento:** `&attach=http://www.example.com/`
- **Duración:** `duration=30M`, como alternativa a la hora de finalización del evento (dtend), especifica una duración como 1H o 30M
- **Hora de la alarma recordatoria, en minutos:** `&reminder=15`
- **Todo el día:** `&allday=1`
- **UID:** parámetro opcional para codificar el identificador único del evento, lo que permite a algunas aplicaciones de calendario actualizar el evento a lo largo del tiempo. La cadena @ics.agical.io se añade automáticamente al valor.

También puede añadir parámetros adicionales para los eventos recurrentes:
- **Eventos semanales:** `&recur=weekly`
- **Eventos mensuales:** `&recur=monthly`
- **Fin de la recurrencia:** `&recuruntil=END_DATE`, donde `END_DATE` es la fecha y hora en que finaliza la recurrencia en formato ISO 8601 (AAAA-MM-DDTHH:MM:SSZ) como UTC

## Comportamiento de los enlaces

Cuando un usuario hace clic en el enlace, los calendarios transforman automáticamente las marcas de tiempo UTC en las URL para reflejar la zona horaria del usuario establecida en su calendario.

Por ejemplo, si abres el enlace de ejemplo "Añadir a Google Calendar" y tu calendario está configurado en CST, la hora del evento se rellenará de acuerdo con lo que son las 3 pm UTC en CST (10 am).

### Calendario de Google

Al hacer clic, Google Calendar se abre en una nueva pestaña o ventana con los detalles del evento rellenados previamente en la invitación y listos para que el usuario los guarde. Esto ocurre tanto en el móvil como en el ordenador.

![Diálogo de Google Calendar para añadir un evento con los detalles del evento añadidos y listo para guardar.][2]{: style="max-width:75%"}

### iCal o Outlook

Al hacer clic en el escritorio, se descarga un archivo ICS. A continuación, el usuario debe abrir el archivo ICS, que abrirá iCal o Outlook y le pedirá que añada el evento a su calendario.

![Calendario iCal con un cuadro de diálogo para añadir un nuevo evento, que pide al usuario que seleccione un calendario y confirme.][3]{: style="max-width:75%"}

![Calendario iCal con el evento añadido.][4]{: style="max-width:81%"}

En el móvil, los usuarios tienen que mantener pulsado el enlace, que les pide que lo añadan a su calendario.

![Ventana emergente de iOS cuando mantienes pulsado un enlace de calendario, que incluye un botón para "Añadir al calendario".][5]{: style="max-width:50%"}

Para más información, consulte:
* [Crear eventos para Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Crear un enlace Añadir al calendario en un mensaje de correo electrónico](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


[1]: {% image_buster /assets/img_archive/calendar_1.png %}
[2]: {% image_buster /assets/img_archive/calendar_2.png %}
[3]: {% image_buster /assets/img_archive/calendar_3.png %}
[4]: {% image_buster /assets/img_archive/calendar_4.png %}
[5]: {% image_buster /assets/img_archive/calendar_5.png %}