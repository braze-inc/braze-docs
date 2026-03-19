---
nav_title: Demora 
article_title: Demora 
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Este artículo de referencia cubre cómo añadir un retraso a tu Canvas sin necesidad de añadir un mensaje asociado."
tool: Canvas

---

# Demora

> Los componentes de retardo permiten añadir un retardo independiente a un lienzo. Puede añadir un retraso a su lienzo sin necesidad de añadir un mensaje asociado. 

Los retrasos pueden hacer que su lienzo parezca más limpio. También puede utilizar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día específico o hasta un día específico de la semana. <br> ![Un paso de retraso con un retraso de 1 día como primer paso de un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Crear un retraso

Para crear un retraso, añade un paso a tu Canvas. Arrastre y suelte el componente Retardo desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Retardo**.

Hay varios detalles que debes tener en cuenta al crear un retraso en tu recorrido de Canvas.

- El límite de retraso es de 30 días.
- Un componente de retardo sólo puede conectarse a un paso siguiente.

#### Retrasos prolongados

Ahora puedes prolongar los pasos de Retraso hasta dos años. Por ejemplo, si estás incorporando nuevos usuarios a tu aplicación, puedes añadir un retraso de dos meses antes de enviar un paso de Mensaje para animar a los usuarios que no han iniciado una sesión.

## Tipos de retardo de tiempo

Puedes elegir el tipo de retraso antes del siguiente mensaje en tu Canvas. Puedes establecer un retraso para que tus usuarios duren hasta después de un periodo de tiempo designado, o retrasar a tus usuarios hasta una fecha y hora específicas.

{% tabs %}
{% tab Duration %}

Al seleccionar **Duración,** puedes retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora específica. Por ejemplo, puedes retrasar a los usuarios cuatro horas o un día.
  
Tenga en cuenta la diferencia entre cómo se calculan los "días" y los "días naturales".
  
- Un «día» es de 24 horas y se calcula desde el momento en que el usuario entra en la etapa de retraso. 
- Un «día del calendario» define el tiempo que hay que esperar hasta la siguiente hora especificada, que puede ser inferior a 24 horas. Puedes optar por retrasar la hora de la empresa o la hora local del usuario. Si no se especifica una hora, el usuario se retrasará hasta la medianoche del día siguiente en la hora de la empresa.

También puedes seleccionar **A una hora determinada** para especificar cuándo avanzarán los usuarios en el Canvas. Esta opción tiene en cuenta la hora a la que el usuario entró en el paso Retraso. Si este tiempo es superior al configurado en los ajustes, añadiremos más horas al retraso. 

Por ejemplo, supongamos que hoy es 11 de diciembre y que nuestro paso de retraso está configurado con **una duración** de una semana a las 8:00 a. m. UTC. Si un usuario entra en el paso Retraso el 4 de diciembre, sería liberado del paso Retraso para continuar su viaje hoy si entró originalmente en el paso Retraso a una hora anterior a las 8 de la mañana UTC. Si entraron en el paso Retraso después de esta hora, el usuario será retrasado hasta el día siguiente (la próxima vez que se produzca esta hora). 

{% endtab %}
{% tab Calendar date %}

Al seleccionar **la fecha del calendario**, puedes retener a los usuarios en el paso hasta una fecha y hora específicas.

#### Consideraciones

##### Los usuarios no recibirán pasos o mensajes con fecha pasada.

Si la fecha y hora seleccionadas ya han pasado para cuando los usuarios procedan al paso Retrasar, los usuarios saldrán del Lienzo. Pueden transcurrir hasta 31 días entre el inicio del Canvas y las fechas elegidas para los pasos «esperar hasta un día exacto».

{% alert important %}
Si participas en el [acceso anticipado a Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), puedes establecer retrasos de hasta 2 años.
{% endalert %}

Por ejemplo, no recibiréis pasos ni mensajes en estos casos:

- Se ha programado el envío de un mensaje para el 3 de mayo a las 9 p. m., pero el paso Retraso expira el 3 de mayo a las 9 a. m. 
- Un paso en Canvas se retrasa hasta una hora específica en la zona horaria local del usuario, pero los usuarios no tienen una zona horaria configurada en su perfil de usuario. El retraso se establece entonces de forma predeterminada en la zona horaria de la empresa para estos usuarios, que ya ha superado la hora especificada. 
  
##### Los usuarios saldrán si un paso de retraso posterior se encuentra dentro de la línea de tiempo de un paso de retraso anterior.

Si el Canvas tiene dos pasos de retraso, pero el primero es más largo que el segundo, los usuarios también saldrán del Canvas. 

Por ejemplo, supongamos que un Canvas tiene estos pasos:
- Paso 1: Paso de mensaje
- Paso 2: Aplaza el paso hasta el 13 de diciembre a las 10 de la noche.
- Paso 3: Paso de mensaje
- Paso 4: Aplaza el paso hasta el 13 de diciembre a las 7 p. m.
- Paso 5: Paso de mensaje
  
Los usuarios que entran en el paso 4 saldrán del lienzo antes de recibir el paso 5, ya que el retraso del paso 4 forma parte del plazo del paso 2.

{% endtab %}
{% tab Day of the week %}

Al seleccionar **Día de la semana,** puedes retener a los usuarios en el paso hasta un día específico de la semana, a una hora específica. Por ejemplo, puedes retrasar a los usuarios hasta que llegue el próximo jueves a las 16:00 en la zona horaria de la empresa. 

Para configurarlo correctamente, también tendrá que seleccionar qué ocurre si el usuario entra en el lienzo el día de la semana seleccionado (por ejemplo, el jueves), pero después de la hora especificada. Puede optar por adelantar al usuario el mismo día o retenerlo hasta la semana siguiente.
{% endtab %}
{% endtabs %}

## Utilizar pasos de Retraso

Digamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entraran en el Canvas y recibieran un mensaje sobre una próxima promoción. Entonces, querrás retener a los usuarios en el Canvas hasta el 17 de junio a las 15:00, hora local. A las 15:00 hora local del 17 de junio, quieres enviar a los usuarios un mensaje recordatorio sobre la promoción.

La secuencia de pasos en Canvas podría ser la siguiente:

1. Empieza por añadir un paso en Canvas que envíe mensajes inmediatamente después de que los usuarios entren en Canvas el 11 de junio.
2. Crea un paso de Retraso que retenga a los usuarios hasta la 1 de la tarde, hora local, del 17 de junio.
3. Vincula el paso Retraso a otro paso Mensaje que envíe su mensaje inmediatamente.

### Componentes de retardo al final de un lienzo {#delay-as-last-step}

Si añades un componente de retraso al Canvas y no hay pasos posteriores, cualquier usuario que llegue al último paso realizará automáticamente el avance al exterior del Canvas. Esto es así aunque aún no se haya alcanzado el tiempo del paso Retraso. Esto significa que los usuarios que ya hayan llegado al paso Retraso no recibirán ningún mensaje que añadas después de este paso. Sin embargo, si un usuario no ha llegado al paso Retraso y se añade un mensaje, entonces recibiría ese mensaje.

### Retrasos personalizados

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecciona el alternador **Personalizar retraso** para establecer un retraso personalizado para tus usuarios. Puedes utilizarlo con un [paso Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para seleccionar la variable contextual por la que retrasar. Esto anulará la hora del día establecida en el atributo o propiedad seleccionados. Esto resulta útil cuando se aplica un desfase en días o semanas y se desea que los usuarios avancen en un momento específico. La zona horaria proviene del atributo o propiedad, o utiliza la alternativa si no hay ninguno disponible. 

#### Comportamiento de la zona horaria para «a una hora específica»

Al configurar retrasos personalizados con la opción **«a una hora específica**», el comportamiento de la zona horaria depende del tipo de datos de tu atributo o variable de contexto:

- **Tipo de datos de cadena con zona horaria:** Si el atributo o la variable de contexto es un tipo de datos de cadena que incluye información sobre la zona horaria, se ajusta a la zona horaria especificada en la cadena. Por ejemplo,`2025-06-10T10:00:00-08:00`utiliza UTC-8.
- **Tipo de datos de cadena sin zona horaria:** Si el atributo o la variable de contexto es un tipo de datos de cadena sin información de zona horaria, se ajusta a la zona horaria alternativa. Por ejemplo,`2025-06-10`utiliza la zona horaria alternativa.
- **Tipo de datos de tiempo:** Si el atributo o la variable de contexto es un tipo de datos de tiempo, se ajusta al UTC. Esto se debe a que el tipo de datos de tiempo siempre se convierte a UTC cuando se guarda en la base de datos, por lo que «en un momento específico» siempre hará referencia a UTC cuando la variable se establezca en el tipo de datos de tiempo. Por ejemplo,`2025-06-10T10:00:00-08:00`utiliza UTC+0.

{% alert note %}
Es posible que un atributo personalizado o una variable de contexto no tengan ni una hora específica ni una zona horaria si son de tipo de datos de cadena. Si se trata de un tipo de datos de tiempo, deberás especificar la hora y la zona horaria. Sin embargo, si el atributo personalizado o la variable de contexto es una cadena «irrelevante» (como"product_name"),  el usuario saldrá del Canvas.
{% endalert %}

#### Casos de uso

Supongamos que quieres recordar a tus clientes que compren pasta de dientes dentro de 30 días. Mediante una combinación de un paso de contexto y un paso de retraso, puedes seleccionar esta variable de contexto para retrasar. En este caso, tu paso Contexto tendría los siguientes campos:

- **Nombre de la variable de contexto:** product_reminder_interval
- **Tipo de datos:** Tiempo
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![El"product_reminder_interval"  y su valor.]({% image_buster /assets/img/context_step1.png %})

A continuación, como quieres recordarles a tus clientes dentro de 30 días, seleccionarás **Hasta un día específico** como opción de retraso y seleccionarás **Personalizar retraso** para utilizar la información de tu paso Contexto. Esto significa que tus usuarios se retrasarán hasta la variable de contexto seleccionada.

## Análisis de retrasos

Los componentes de retraso tienen las siguientes métricas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| _El usuario ha entrado_ | Refleja el número de veces que se ha introducido el paso. Si tu Canvas es reeleccionable y un usuario entra dos veces en un paso de Retraso, se registrarán dos entradas. |
| _Continúa con el paso siguiente_ | Refleja el número de entradas que pasaron al siguiente paso en el Canvas. |
| _Has salido de Canvas_ | Refleja el número de entradas que salieron del Canvas y no pasaron al siguiente paso. |
| _Error de personalización_ | Refleja el número de veces que un mensaje personalizado o contenido destinado a un usuario no se ha podido entregar debido a lo siguiente:<br> {::nomarkdown}<ul><li>El valor del retraso está en el pasado.</li><li>El valor del retraso es de más de dos años en el futuro.</li><li><b>Después de una duración,</b> el valor no es un número.</li><li><b>Hasta que un</b> valor <b>de día específico</b> no sea una fecha o una cadena con formato de fecha.</li></ul>{:/} <br>Consulta [Errores de personalización fallida](#personaliztion-failed-errors) para obtener más detalles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las series temporales de estos análisis están disponibles en la vista ampliada de componentes.

## Solución de problemas

### Errores de personalización fallida

Si los usuarios no desencadenan un retraso personalizado, podría deberse a que el paso Contexto que has configurado para que se califiquen para el paso Retraso no funciona como esperabas. Cuando una [variable de contexto no es válida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), el usuario continuará por tu Canvas sin que el paso Contexto establezca su contexto. Esto puede hacer que no reúnas los requisitos para pasos posteriores en Canvas, como los retrasos de personalización.

