---
nav_title: "Aprobación de la población objetivo"
article_title: "Aprobación de la población objetivo"
permalink: "/target_approvals/"
hidden: true
description: "Este artículo describe cómo utilizar las aprobaciones de población objetivo para campañas y Lienzos con un gran volumen de envíos."
---

# Aprobación de la población objetivo

> Esta página explica cómo configurar las aprobaciones de la población objetivo para tus reglas de mensajería. Mediante la aprobación de la población objetivo, puedes establecer umbrales de volumen para campañas y Lienzos que requieran aprobación adicional para tus reglas de mensajería. De este modo, puedes tener una revisión adicional cuando tu mensajería se dirija a una audiencia mayor.

{% alert important %}
La aprobación de la población objetivo está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Requisito previo

Antes de que puedas configurar la aprobación de la población objetivo, tanto Canvas como los flujos de trabajo de aprobación de campañas deben estar activados.

Para activar los flujos de trabajo de aprobación de Canvas y de campañas, ve a **Configuración** > **Flujo de trabajo de aprobación** > **Aprobaciones siempre activas**. 

## Configuración de la aprobación de la población objetivo

1. Ve a **Configuración** > **Flujo de trabajo de aprobación** > **Reglas de mensajería**.
2. Selecciona **Crear regla**.
3. Dale un nombre a tu regla para identificarla de un vistazo (por ejemplo, "Todas las suscripciones de usuarios").
4. En **Objeto**, selecciona **Campaña**, **Canvas** o **Tanto Canvas como Campañas** para aplicar la regla de aprobación.
5. Introduce un número para **el Umbral de usuarios alcanzables**. Para más información, consulta [Estadísticas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Selecciona **Guardar**.

![Un ejemplo de regla de mensajería "Regla 1" tanto para Canvas como para campañas con 100.000 usuarios como umbral. Hay tres usuarios que pueden aprobar el Canvas y la campaña a lanzar.][1]

Puedes configurar hasta cinco reglas de mensajería. Al configurar tu regla de mensajería, pueden existir dos reglas con el mismo umbral de volumen para el mismo objeto. Por ejemplo, puedes establecer un umbral de 10.000 usuarios para Canvas y de 10.000 usuarios tanto para Canvas como para las campañas. 

Del mismo modo, si configuras dos umbrales de 10.0000 usuarios para Canvas con diferentes aprobadores, esta regla se puede guardar. De este modo, puedes organizar y separar a tus aprobadores (como tu equipo jurídico y tu equipo de diseño) en reglas específicas.

Ten en cuenta que no puedes establecer reglas con umbrales de volumen superpuestos para el mismo objeto. Por ejemplo, **no** se puede establecer la siguiente regla de mensajería: una regla con un umbral de 10.000 usuarios para Canvas y otra regla con un umbral de 1.000.000 de usuarios para Canvas.

### Seleccionar aprobadores

{% alert important %}
Opcionalmente, puedes seleccionar aprobadores que, si se cumple el umbral, tengan permiso para aprobar el Canvas o la campaña. Si no seleccionas aprobadores, se bloqueará el lanzamiento del Canvas o de la campaña.
{% endalert %}

Sólo los administradores de Braze pueden establecer reglas de mensajería, pero cualquier usuario de Braze puede ser un aprobador de la población objetivo (incluidos los usuarios sin permisos de aprobación general). 

Si se alcanza un umbral y se selecciona un **aprobador**, el usuario con permiso de aprobación podrá seleccionar **Aprobado** en el desplegable de aprobación **Audiencia objetivo**.

### Reglas en Canvas y campañas

La aprobación de la población objetivo controla quién puede aprobar el paso **Audiencia objetivo** de un Canvas y una campaña. Si se cumple una regla pero los aprobadores no están seleccionados, se desactivará el botón **Lanzar** o **Actualizar** Canvas o campaña.

![El paso "Resumen" del flujo de trabajo Canvas que muestra que necesitas una aprobación para lanzarlo.][2]

## Preguntas más frecuentes

### ¿Cambiará algo automáticamente cuando se active esta característica?

No. Una vez activada esta característica, debes introducir manualmente un umbral de volumen y seleccionar aprobadores para utilizar la característica.

### ¿Tengo que volver a configurar mis permisos para utilizar esta característica?

No es necesario que modifiques los permisos existentes. Cualquier usuario, independientemente de sus permisos actuales, puede ser seleccionado como aprobador de la población objetivo.

### ¿Se aplica el mismo umbral a todos los espacios de trabajo?

No. Debes configurar reglas de mensajería para cada espacio de trabajo.

### ¿La aprobación de la población objetivo se basa en el paso Audiencia objetivo?

Sí. La aprobación de la población objetivo no tiene en cuenta detalles como los acontecimientos desencadenantes. Por ejemplo, una campaña puede dirigirse a todos tus usuarios; sin embargo, la campaña se desencadena por eventos, por lo que el número real de usuarios que la reciben es menor.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}
[2]: {% image_buster /assets/img/non_approver_banner.png %}