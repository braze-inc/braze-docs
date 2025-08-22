---
nav_title: Reglas de mensajería
article_title: Reglas de mensajería
page_order: 1
page_type: reference
description: "Esta página explica cómo utilizar las reglas de mensajería en el flujo de trabajo de aprobación para campañas y Lienzos con un gran volumen de envíos."
---

# Normas de mensajería

> Utiliza reglas de mensajería en tu flujo de trabajo de aprobación para limitar el número de usuarios alcanzables antes de que se requiera una aprobación adicional; de este modo, puedes revisar tus campañas y Canvases antes de dirigirte a una audiencia mayor.

## Cómo funciona

Las reglas de mensajería se aplican a un espacio de trabajo y se componen de un tipo de mensaje y un número máximo de usuarios alcanzables.

- **Tipo de mensaje:** Define a qué tipo de mensaje se aplicará la regla: campaña, Canvas, o tanto Canvas como campañas.
- **Máximo de usuarios accesibles:** Determina qué tamaño de audiencia requerirá una aprobación adicional.

### Tipos de mensajes compartidos y usuarios máximos alcanzables

Pueden existir dos reglas con el mismo número de usuarios accesibles para el mismo tipo de mensaje. Por ejemplo, puedes establecer un máximo de 10.000 usuarios para Canvas y de 10.000 usuarios tanto para Canvas como para campañas. 

### Aprobadores separados

Dos reglas pueden compartir el mismo usuario máximo para que puedas organizar y separar tus reglas por aprobadores. Por ejemplo, crea las dos reglas siguientes:

- Regla A para Canvas con un máximo de 100.000 usuarios con aprobadores en tu equipo legal
- Regla B para Canvas con un máximo de 100.000 usuarios con aprobadores en tu equipo de marketing 

### No hay usuarios accesibles solapados

No puedes establecer reglas con un número solapado de usuarios para el mismo tipo de mensaje. Por ejemplo, **no** se puede establecer la siguiente regla de mensajería: 

- Regla C para Canvas con un máximo de 10.000 usuarios 
- Regla D para Canvas con un máximo de 1.000.000 de usuarios

## Crear una regla de mensajería

### Requisitos previos

Sólo los administradores de Braze pueden establecer reglas de mensajería, pero cualquier usuario de Braze puede ser un aprobador de reglas de mensajería (incluidos los usuarios sin permisos de aprobación general).

### Paso 1: Añadir una regla

{% alert note %}
Puedes crear hasta CINCO reglas de mensajería.
{% endalert %}

1. Ve a **Configuración** > **Flujo de trabajo de aprobación** > **Reglas de mensajería**.
2. Selecciona **Crear regla**.
3. Dale un nombre a esta regla (por ejemplo, "Todas las suscripciones de usuarios").
4. En **Tipo de mensaje**, selecciona **Campaña**, **Canvas** o **Tanto Canvas como Campañas** para aplicar la regla de aprobación.
5. Introduce un número para **el máximo de usuarios accesibles**. Para más información, consulta [Estadísticas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Seleccione **Guardar**.

![Un ejemplo de regla de mensajería "Regla 1" para campañas con 100.000 usuarios como máximo. Hay un usuario que puede aprobar el Canvas y la campaña a lanzar.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Paso 2: Determinar el lanzamiento con aprobación (opcional)

Selecciona **Permitir lanzamiento con aprobación**. A continuación, en **Con aprobación de**, selecciona los aprobadores que tienen permiso para aprobar el Canvas o la campaña si se cumple el máximo.

Toma nota de los siguientes detalles sobre el lanzamiento de mensajes con aprobación:

- Si se cumple el máximo y se selecciona un **aprobador**, el usuario Braze con el permiso de aprobación podrá seleccionar **Aprobado** en el desplegable de aprobación **Audiencia objetivo**.
- Si se alcanza el máximo y no se selecciona una aprobación, se impedirá el lanzamiento del Canvas o de la campaña.

![El paso "Resumen" del flujo de trabajo Canvas que muestra que necesitas una aprobación para lanzarlo.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Preguntas más frecuentes

### ¿Tengo que volver a configurar mis permisos para utilizar las reglas de mensajería?

No. Cualquier usuario, independientemente de sus permisos actuales, puede ser seleccionado como aprobador de la población objetivo.

### ¿Cómo se relacionan las reglas de mensajería con el paso Audiencia objetivo?

Las reglas de mensajería no tienen en cuenta detalles como los eventos desencadenantes. Por ejemplo, una campaña puede dirigirse a todos tus usuarios. Sin embargo, la campaña se desencadena por eventos, por lo que el número real de usuarios que la reciben es menor.

### ¿Cambiará algo automáticamente cuando se activen las reglas de mensajería?

No. Una vez activada esta característica, debes introducir manualmente el número máximo de usuarios y seleccionar los aprobadores para utilizar la característica.

