---
nav_title: División de decisiones 
article_title: División de decisiones 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar divisiones de decisión en el lienzo."
tool: Canvas

---

# División de decisiones 

> El componente Decision Split de Canvas le permite ofrecer experiencias personalizadas y en tiempo real a sus usuarios.

![Un paso para la división de decisiones llamado "¿Push habilitado?" para usuarios que no están habilitados para push y usuarios que sí lo están.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Este componente puede utilizarse para crear ramas Canvas en función de si un usuario coincide con una consulta.

## Crea una división de decisiones 

Para crear una división de decisiones en tu flujo de trabajo, añade un paso a tu Canvas. A continuación, arrastra y suelta el componente desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **División de decisiones**.

### Define tu división

¿Cómo quiere dividir a sus usuarios? Puedes utilizar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) y filtros para trazar la línea. Básicamente, está creando una consulta en `true` o `false` que evaluará a sus usuarios y luego los dirigirá a un paso u otro. Debe utilizar al menos un segmento o un filtro. No es necesario utilizar a la vez un segmento y un filtro.

![Un paso para la división de decisiones con el filtro "Push habilitado es verdadero" seleccionado.]({% image_buster /assets/img/define-split-2.png %}){: style="max-width:90%;"}

{% alert note %}
Por defecto, los segmentos y filtros de un paso para la división de decisiones se comprueban justo después de recibir un paso anterior, a menos que añadas un retraso.
{% endalert %} 

## Utiliza tu división

Utilizar una división por decisión puede ayudarte a distinguir las rutas de tus usuarios en función de su segmento o sus atributos, ¡incluso si utilizan determinados canales de mensajería para recibir tus mensajes!

Supongamos que está creando un flujo de incorporación. Puede empezar con un correo electrónico de bienvenida al registrarse. Luego, dos días después, quieres enviar un mensaje push, pero solo a los usuarios habilitados para push. Después, todos los usuarios reciben otro correo electrónico tres días después de haberse inscrito. También puede utilizar su división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tienen activada la función push para animarles a activarla.

Si no hay ningún paso siguiendo uno de los caminos, los usuarios que vayan por ese camino saldrán del Canvas. 

![Un paso para la división de decisiones llamado "¿Push habilitado?" para los usuarios que no están habilitados para push y los que sí lo están. Los usuarios que no estén habilitados para push, experimentarán un retraso de 3 días y recibirán un mensaje de correo electrónico. Los usuarios habilitados para push experimentarán un retraso de 1 día, recibirán una notificación push seguida de un retraso de 2 días y, a continuación, recibirán el mismo mensaje de correo electrónico que los usuarios no habilitados para push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análisis

Consulte la tabla siguiente para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
| _El usuario ha entrado_ | El número total de veces que se ha introducido el paso. Si su Canvas tiene re-elegibilidad y un usuario introduce un paso de División de Decisión dos veces, se registrarán dos entradas. |
| _Sí_ | Número de entradas que cumplen los criterios especificados y han seguido el camino "sí". |
| _No_ | El número de entradas que no cumplieron los criterios especificados y siguieron la ruta "no". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

