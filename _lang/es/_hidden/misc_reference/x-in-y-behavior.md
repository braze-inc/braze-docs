---
nav_title: Comportamiento del filtro X en Y
permalink: /x-in-y-behavior/
---

# Comportamiento actual del filtro X en Y

El comportamiento de estos filtros seguirá siendo en gran medida el mismo y se definirá por las siguientes características:

- Ejecútalo configurando Días del calendario (finalizando a medianoche).
- Los "días" se definen en UTC.
- El día UTC actual se define como "0".

## Casos de uso

La campaña que se muestra a continuación se envía a las 21:00 horas del 16 de abril. La segmentación de la audiencia es "Ha realizado más de 2 compras en los últimos 3 días".

![Calendario de la campaña][1]

Las 21 h ET del 16 de abril son la 1 h UTC del 17 de abril.

El 17 de abril sería el día "0", el 16 de abril sería el día "1", el 15 de abril sería el día "2" y el 14 de abril sería el día "3".

El historial desde las 12 h UTC del 14 de abril hasta la hora actual (1 h UTC del 17 de abril).
Esto se acumularía en una ventana que incluye 73 horas del historial del usuario.

## En días calendario

Los Días del Calendario se utilizan en más capacidades que sólo en los Filtros "X en Y":

- Programación de mensajes
- Limitación de frecuencia
- "Filtros "X en Y

`Calendar Days` se refieren al periodo de tiempo dentro de un día numerado, que comienza a las 12:00 h y termina a las 23:59 h de ese mismo día (de las 12:00 h del 8 de junio a las 23:59 h del 8 de junio sería un único día del calendario).

### Limitación de frecuencia

Los días del calendario se utilizan cuando seleccionas "días" o "semanas" en `Frequency Capping`.

- `Every 1 day` limitará la limitación al día natural actual en la hora local de tu usuario (finalizando a medianoche hora local).
- `Every 2 days` limitará la limitación a los días naturales anterior y actual en la hora local de tu usuario (finalizando a medianoche hora local del día natural actual).

### Empresa y hora local

El Día del Calendario actual en la zona horaria de la empresa cuenta como día `0`.

`Send in 1 Calendar days at 11:05 am company time` o `send in 1 Calendar days at 11:05 am local time` añadirían `1` día al día del calendario actual en la zona horaria de la empresa o en la zona horaria local, respectivamente, y luego programarían el mensaje a las próximas 11:05 h, hora de la empresa.

Si la empresa u hora local es la hora del Pacífico, y el usuario introduce el paso en Canvas a las 20:00 h PT del 13/4, Braze programará este paso en Canvas para las 11:05 h PT del 14/4.

## Anterior Comportamiento del filtro X en Y

Braze tiene una categoría específica de filtros de segmentación llamada "Filtros X en Y". Cada uno de estos filtros tiene una funcionalidad similar definida por las siguientes características:

- Ejecútalo configurando Días del calendario (finalizando a medianoche).
- Los "días" se definen en UTC.
- El día UTC actual se define como "1".



[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
