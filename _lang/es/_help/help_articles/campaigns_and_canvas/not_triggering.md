---
nav_title: Campaña sin desencadenar o Canvas
article_title: Campaña sin desencadenar o Canvas
page_order: 5

page_type: solution
description: "Este artículo de ayuda te guía a través de los pasos para resolver problemas con campañas o Lienzos que no se desencadenan como se esperaba."
tool: 
- Campaigns
- Canvas
---

# Campaña no desencadenada o Canvas

Hay varias razones por las que no has conseguido el comportamiento de desencadenamiento esperado. La solución para el error más común es asegurarte de que la campaña que estás desencadenando no utiliza el mismo evento desencadenante en el segmento.

## Desencadenantes de campaña

La pertenencia a un segmento se evalúa antes de desencadenar acciones. Esto significa que si el usuario no entra primero en el segmento, no recibirá la campaña aunque realice el desencadenamiento.

Si tu campaña se desencadena a partir de un evento personalizado, deberás asegurarte de que este evento no está prefiltrado por un segmento que quieras utilizar en la campaña. 

Por ejemplo, si el segmento incluye el evento `SessionStart` "Ha utilizado la aplicación más de una vez" y el evento que desencadena la campaña es `SessionStart`, el usuario recibirá el mensaje, pero no será necesariamente para la primera sesión. Esto se debe a que durante el primer paso, cuando se comprueba si un usuario debe recibir una campaña, la campaña está revisando la audiencia objetivo del segmento. 

En resumen, evita configurar una campaña basada en acciones o Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). Puede darse una [condición de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/) en la que el usuario no esté en la audiencia cuando realice el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de la campaña, asegúrese de ponerse en contacto con el servicio de asistencia de Braze en los 30 días siguientes a la aparición del problema, ya que sólo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

_Última actualización: 25 de junio de 2024_

