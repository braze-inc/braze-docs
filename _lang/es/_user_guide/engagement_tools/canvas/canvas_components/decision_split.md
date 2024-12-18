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

Este componente puede utilizarse para crear ramas Canvas en función de si un usuario coincide con una consulta.

![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Crea una división de decisiones 

Para crear una división de decisiones en su flujo de trabajo, primero añada un paso a su Lienzo. Arrastre y suelte el componente desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Dividir decisión**.

### Define tu división

¿Cómo quiere dividir a sus usuarios? Puede utilizar [segmentos][5] y filtros para trazar la línea. Básicamente, está creando una consulta en `true` o `false` que evaluará a sus usuarios y luego los dirigirá a un paso u otro. Debe utilizar al menos un segmento o un filtro. No es necesario utilizar a la vez un segmento y un filtro.

![][2]{: style="max-width:90%;"}

{% alert note %}
Por defecto, los segmentos y filtros de un componente de División de decisión se comprueban justo después de recibir un paso anterior, a menos que se añada un retraso.
{% endalert %} 

## Utiliza tu división

Utilizar una división por decisión puede ayudarte a distinguir las rutas de tus usuarios en función de su segmento o sus atributos, ¡incluso si utilizan determinados canales de mensajería para recibir tus mensajes!

Supongamos que está creando un flujo de incorporación. Puede empezar con un correo electrónico de bienvenida al registrarse. Luego, dos días después, quieres enviar un mensaje push, pero solo a los usuarios habilitados para push. Después, todos los usuarios reciben otro correo electrónico tres días después de haberse inscrito. También puede utilizar su división de decisiones para enviar un mensaje dentro de la aplicación a los usuarios que no tienen activada la función push para animarles a activarla.

![][3]{: style="max-width:60%;"}

Si no hay ningún paso siguiendo uno de los caminos, los usuarios que vayan por ese camino saldrán del Canvas. 

{% alert important %}
Una decisión dividida no puede tener pasos de hermanos completos. En otras palabras, no se puede crear un paso completo que se ramifique en un paso de filtro y un paso completo. Esta restricción existe porque si hubiera una rama con un paso de filtro y un paso completo, no estaría claro por qué rama bajarían los usuarios.
<br>
Un paso de filtro sólo puede conectarse a un paso siguiente.
{% endalert %}

## Análisis

Consulte la tabla siguiente para ver las descripciones de los análisis de este paso:

| Métrica | Descripción |
|---|---|
| El usuario ha entrado | El número total de veces que se ha introducido el paso. Si su Canvas tiene re-elegibilidad y un usuario introduce un paso de División de Decisión dos veces, se registrarán dos entradas. |
| Sí | Número de entradas que cumplen los criterios especificados y han seguido el camino "sí". |
| No | El número de entradas que no cumplieron los criterios especificados y siguieron la ruta "no". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/
