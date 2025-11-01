---
nav_title: División de decisiones
article_title: División de decisiones 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar divisiones de decisiones en tu Canvas."
tool: Canvas

---

# División de decisiones 

> El componente División de decisiones en Canvas te permite entregar experiencias personalizadas y en tiempo real a tus usuarios.

\![Un paso para la división de decisiones llamado "¿Push habilitado?" para usuarios que no están habilitados para push y usuarios que sí lo están.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Este componente puede utilizarse para crear ramas Canvas en función de si un usuario coincide con una consulta.

## Crear una división de decisiones 

Para crear una división de decisiones en tu flujo de trabajo, añade un paso a tu Canvas. A continuación, arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **División de decisiones**.

### Define tu división

¿Cómo quieres dividir a tus usuarios? Puedes utilizar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) y filtros para trazar la línea. Esencialmente, estás creando una consulta en `true` o `false` que evaluará a tus usuarios y luego los embudo hacia un paso u otro. Debes utilizar al menos un segmento o un filtro. No es necesario que utilices tanto un segmento como un filtro.

\![Un paso para la división de decisiones con el filtro "Push en primer plano habilitado es verdadero" seleccionado.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Por defecto, los segmentos y filtros de un paso para la división de decisiones se comprueban justo después de recibir un paso anterior, a menos que añadas un retraso.
{% endalert %} 

## Utiliza tu división

Utilizar una división de decisiones puede ayudarte a distinguir las rutas de tus usuarios en función de su segmento o sus atributos, ¡incluso si utilizan determinados canales de mensajería para recibir tus mensajes!

Digamos que estás creando un flujo de incorporación. Puedes empezar con un correo electrónico de bienvenida al registrarte. Luego, dos días después, quieres enviar un mensaje push, pero sólo a los usuarios habilitados para push. Después, todos los usuarios reciben otro correo electrónico tres días después de haberse registrado. También puedes utilizar tu división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tengan habilitado push para animarles a habilitarlo.

Si no hay ningún paso siguiendo uno de los caminos, los usuarios que recorran ese camino saldrán del Canvas. 

\![Un paso para la división de decisiones llamado "¿Push habilitado?" para los usuarios que no están habilitados para push y los que sí lo están. Los usuarios que no estén habilitados para push, experimentarán un retraso de 3 días y recibirán un mensaje de correo electrónico. Los usuarios habilitados para push experimentarán un retraso de 1 día, recibirán una notificación push seguida de un retraso de 2 días y, a continuación, recibirán el mismo mensaje de correo electrónico que los usuarios no habilitados para push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análisis

Consulta la tabla siguiente para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
| _Entró en_ | El número total de veces que se ha introducido el paso. Si tu Canvas tiene reelegibilidad y un usuario entra dos veces en un paso para la división de decisiones, se registrarán dos entradas. |
| _Sí_ | El número de entradas que cumplieron los criterios especificados y siguieron el camino del "sí". |
| _No_ | El número de entradas que no cumplieron los criterios especificados y siguieron el camino "no". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

