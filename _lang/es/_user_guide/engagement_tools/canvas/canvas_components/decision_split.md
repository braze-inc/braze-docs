---
nav_title: División de decisiones
article_title: División de decisiones 
alias: /decision_split/
page_order: 7
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar divisiones de decisión en el lienzo."
tool: Canvas

---

# División de decisiones 

> El componente de división de decisiones de Canvas te permite entregar experiencias personalizadas y en tiempo real a tus usuarios.

![Un paso para la división de decisiones denominado «¿Push habilitado?» para los usuarios que no tienen habilitado el push y los que sí lo tienen.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Este componente puede utilizarse para crear ramas Canvas en función de si un usuario coincide con una consulta.

## Crea una división de decisiones 

Para crear una división de decisiones en tu flujo de trabajo, añade un paso a tu lienzo de Canvas. A continuación, arrastra y solta el componente desde la barra lateral, o selecciona el botón<i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **la división de decisiones**.

### Define tu división

¿Cómo quiere dividir a sus usuarios? Puedes utilizar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) y filtros para trazar la línea. Básicamente, está creando una consulta en `true` o `false` que evaluará a sus usuarios y luego los dirigirá a un paso u otro. Debe utilizar al menos un segmento o un filtro. No es necesario utilizar a la vez un segmento y un filtro.

![Un paso para la división de decisiones con el filtro «Foreground Push Enabled is true» (Empuje en primer plano habilitado es verdadero) seleccionado.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
De forma predeterminada, los segmentos y filtros del paso para la división de decisiones se comprueban inmediatamente después de recibir un paso anterior, a menos que añadas un retraso.
{% endalert %} 

## Utiliza tu división

Utilizar una división por decisión puede ayudarte a distinguir las rutas de tus usuarios en función de su segmento o sus atributos, ¡incluso si utilizan determinados canales de mensajería para recibir tus mensajes!

Supongamos que está creando un flujo de incorporación. Puede empezar con un correo electrónico de bienvenida al registrarse. Luego, dos días después, quieres enviar un mensaje push, pero solo a los usuarios habilitados para push. Después, todos los usuarios reciben otro correo electrónico tres días después de haberse inscrito. También puede utilizar su división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tienen activada la función push para animarles a activarla.

Si no hay ningún paso siguiendo uno de los caminos, los usuarios que vayan por ese camino saldrán del Canvas. 

![Un paso para la división de decisiones denominado «¿Push habilitado?» para los usuarios que no tienen habilitado el push y los que sí lo tienen. Los usuarios que no tengan habilitada la función push experimentarán un retraso de tres días y luego recibirán un mensaje de correo electrónico. Los usuarios que tengan habilitada la función push experimentarán un retraso de un día, recibirán una notificación push seguida de un retraso de dos días y, a continuación, recibirán el mismo mensaje de correo electrónico que los usuarios que no tienen habilitada la función push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análisis

Consulte la tabla siguiente para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
| _El usuario ha entrado_ | El número total de veces que se ha introducido el paso. Si su Canvas tiene re-elegibilidad y un usuario introduce un paso de División de Decisión dos veces, se registrarán dos entradas. |
| _Sí_ | Número de entradas que cumplen los criterios especificados y han seguido el camino "sí". |
| _No_ | El número de entradas que no cumplieron los criterios especificados y siguieron la ruta "no". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

