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

> Los componentes de demora te permiten añadir un retraso independiente a un Canvas. Puedes añadir un retraso a tu Canvas sin necesidad de añadir un mensaje asociado. 

Los retrasos pueden hacer que tu Canvas se vea más limpio. También puedes usar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día específico o hasta un día específico de la semana. Un componente de demora puede conectarse a un solo paso posterior como máximo. <br> ![Un paso de retraso con un retraso de 1 día como primer paso de un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Crear un retraso

Para crear un retraso, añade un paso a tu Canvas. Arrastra y suelta el componente Demora desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y luego elige **Demora**.

#### Retrasos prolongados

Ahora puedes prolongar los pasos de demora hasta dos años. Por ejemplo, si estás incorporando nuevos usuarios a tu aplicación, puedes añadir un retraso prolongado de dos meses antes de enviar un paso de mensaje para animar a los usuarios que no han iniciado una sesión.

## Tipos de retardo de tiempo

Puedes elegir el tipo de retraso antes del siguiente mensaje en tu Canvas. Puedes establecer un retraso para que tus usuarios esperen hasta después de un periodo de tiempo designado, o retrasar a tus usuarios hasta una fecha y hora específicas.

{% tabs %}
{% tab Duration %}

Al seleccionar **Duración**, puedes retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora específica. Por ejemplo, puedes retrasar a los usuarios cuatro horas o un día.
  
Ten en cuenta la diferencia entre cómo se calculan los "días" y los "días naturales".
  
- Un "día" es de 24 horas y se calcula desde el momento en que el usuario entra en el paso de demora. 
- Un "día natural" define el tiempo que hay que esperar hasta la siguiente hora especificada, que puede ser inferior a 24 horas. Puedes optar por retrasar en la hora de la empresa o en la hora local del usuario. Si no se especifica una hora, el usuario se retrasará hasta la medianoche del día siguiente en la hora de la empresa.

También puedes seleccionar **A una hora específica** para especificar cuándo avanzarán los usuarios en el Canvas. Esta opción tiene en cuenta la hora a la que el usuario entró en el paso de demora. Si este tiempo es superior al configurado en la configuración, se añadirán más horas al retraso. 

Por ejemplo, supongamos que hoy es 11 de diciembre y nuestro paso de demora está configurado con una **Duración** de una semana a las 8:00 a. m. UTC. Si un usuario entra en el paso de demora el 4 de diciembre, sería liberado del paso de demora para continuar su recorrido hoy si entró originalmente en el paso de demora a una hora anterior a las 8 de la mañana UTC. Si entraron en el paso de demora después de esta hora, el usuario será retrasado hasta el día siguiente (la próxima ocurrencia de esta hora). 

{% endtab %}
{% tab Calendar date %}

Al seleccionar **Fecha del calendario**, puedes retener a los usuarios en el paso hasta una fecha y hora específicas.

#### Consideraciones

##### Los usuarios no recibirán pasos o mensajes con fecha pasada

Si la fecha y hora seleccionadas ya han pasado para cuando los usuarios procedan al paso de demora, los usuarios saldrán del Canvas. Pueden transcurrir hasta 31 días entre el inicio del Canvas y las fechas elegidas para los pasos "esperar hasta un día exacto".

{% alert important %}
Si participas en el [acceso anticipado a Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), puedes establecer retrasos de hasta 2 años.
{% endalert %}

Por ejemplo, los usuarios no recibirán pasos ni mensajes en estos escenarios:

- Se ha programado el envío de un mensaje para el 3 de mayo a las 9 p. m., pero el paso de demora expira el 3 de mayo a las 9 a. m. 
- Un paso en Canvas se retrasa hasta una hora específica en la zona horaria local del usuario, pero los usuarios no tienen una zona horaria configurada en su perfil de usuario. El retraso se establece entonces de forma predeterminada en la zona horaria de la empresa para estos usuarios, que ya ha superado la hora especificada. 
  
##### Los usuarios saldrán si un paso de demora posterior se encuentra dentro de la línea de tiempo de un paso de demora anterior

Si el Canvas tiene dos pasos de demora, pero el primero es más largo que el segundo, los usuarios también saldrán del Canvas. 

Por ejemplo, supongamos que un Canvas tiene estos pasos:
- Paso 1: Paso de mensaje
- Paso 2: Paso de demora hasta el 13 de diciembre a las 10 p. m.
- Paso 3: Paso de mensaje
- Paso 4: Paso de demora hasta el 13 de diciembre a las 7 p. m.
- Paso 5: Paso de mensaje
  
Los usuarios que entran en el paso 4 saldrán del Canvas antes de recibir el paso 5, ya que el retraso del paso 4 forma parte del plazo del paso 2.

{% endtab %}
{% tab Day of the week %}

Al seleccionar **Día de la semana**, puedes retener a los usuarios en el paso hasta un día específico de la semana, a una hora específica. Por ejemplo, puedes retrasar a los usuarios hasta que llegue el próximo jueves a las 4 p. m. en la zona horaria de la empresa. 

Para configurarlo correctamente, también tendrás que seleccionar qué ocurre si el usuario entra en el Canvas el día de la semana seleccionado (por ejemplo, el jueves), pero después de la hora especificada. Puedes optar por avanzar al usuario el mismo día o retenerlo hasta la semana siguiente.
{% endtab %}
{% endtabs %}

## Usar pasos de demora

Digamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entraran en el Canvas y recibieran un mensaje sobre una próxima promoción. Luego, quieres retener a los usuarios en el Canvas hasta el 17 de junio a las 3 p. m. hora local. A las 3 p. m. hora local del 17 de junio, quieres enviar a los usuarios un mensaje recordatorio sobre la promoción.

La secuencia de pasos en Canvas podría ser la siguiente:

1. Empieza añadiendo un paso de mensaje que se envíe inmediatamente después de que los usuarios entren en el Canvas el 11 de junio.
2. Crea un paso de demora que retenga a los usuarios hasta la 1 p. m. hora local del 17 de junio.
3. Vincula el paso de demora a otro paso de mensaje que envíe su mensaje inmediatamente.

### Componentes de demora al final de un Canvas {#delay-as-last-step}

Si añades un componente de demora a tu Canvas y no hay pasos posteriores, cualquier usuario que llegue al último paso avanzará automáticamente fuera del Canvas. Esto es así aunque aún no se haya alcanzado el tiempo del paso de demora. Esto significa que los usuarios que ya hayan llegado al paso de demora no recibirán ningún mensaje que añadas después de este paso. Sin embargo, si un usuario no ha llegado al paso de demora y se añade un mensaje, entonces recibiría ese mensaje.

### Retrasos personalizados

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Selecciona el alternador **Personalizar retraso** para establecer un retraso personalizado para tus usuarios. Puedes usarlo con un [paso Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para seleccionar la variable de contexto por la que retrasar. Esto anulará la hora del día establecida en el atributo o la propiedad seleccionados. Esto resulta útil cuando aplicas un desfase en días o semanas y quieres que los usuarios avancen en un momento específico. La zona horaria proviene del atributo o la propiedad, o usa la alternativa si no hay ninguna disponible. 

#### Comportamiento de la zona horaria para "a una hora específica"

Al configurar retrasos personalizados con la opción **a una hora específica**, el comportamiento de la zona horaria depende del tipo de datos de tu atributo o variable de contexto:

- **Tipo de datos de cadena con zona horaria:** Si el atributo o la variable de contexto es un tipo de datos de cadena que incluye información sobre la zona horaria, se ajusta a la zona horaria especificada en la cadena. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC-8.
- **Tipo de datos de cadena sin zona horaria:** Si el atributo o la variable de contexto es un tipo de datos de cadena sin información de zona horaria, se ajusta a la zona horaria alternativa. Por ejemplo, `2025-06-10` usa la zona horaria alternativa.
- **Tipo de datos de tiempo:** Si el atributo o la variable de contexto es un tipo de datos de tiempo, se ajusta a UTC. Esto se debe a que el tipo de datos de tiempo siempre se convierte a UTC cuando se guarda en la base de datos, por lo que "a una hora específica" siempre hará referencia a UTC cuando la variable se establezca en el tipo de datos de tiempo. Por ejemplo, `2025-06-10T10:00:00-08:00` usa UTC+0.

{% alert note %}
Es posible que un atributo personalizado o una variable de contexto no tengan ni una hora específica ni una zona horaria si son de tipo de datos de cadena. Si se trata de un tipo de datos de tiempo, deberás especificar la hora y la zona horaria. Sin embargo, si el atributo personalizado o la variable de contexto es una cadena "irrelevante" (como "product_name"), el usuario saldrá del Canvas.
{% endalert %}

#### Caso de uso

Supongamos que quieres recordar a tus clientes que compren pasta de dientes dentro de 30 días. Mediante una combinación de un paso Context y un paso de demora, puedes seleccionar esta variable de contexto para retrasar. En este caso, tu paso Context tendría los siguientes campos:

- **Nombre de la variable de contexto:** product_reminder_interval
- **Tipo de datos:** Tiempo
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![El "product_reminder_interval" y su valor.]({% image_buster /assets/img/context_step1.png %})

A continuación, como quieres recordarles a tus clientes dentro de 30 días, seleccionarás **Hasta un día específico** como opción de retraso y seleccionarás **Personalizar retraso** para usar la información de tu paso Context. Esto significa que tus usuarios se retrasarán hasta la variable de contexto seleccionada.

## Análisis de demoras

Los componentes de demora tienen las siguientes métricas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| _Entró_ | Refleja el número de veces que se ha entrado en el paso. Si tu Canvas tiene reelegibilidad y un usuario entra dos veces en un paso de demora, se registrarán dos entradas. |
| _Avanzó al paso siguiente_ | Refleja el número de entradas que avanzaron al siguiente paso en el Canvas. |
| _Salió del Canvas_ | Refleja el número de entradas que salieron del Canvas y no avanzaron al siguiente paso. |
| _Error de personalización_ | Refleja el número de veces que un mensaje personalizado o contenido destinado a un usuario no se pudo entregar debido a lo siguiente:<br> {::nomarkdown}<ul><li>El valor del retraso está en el pasado</li><li>El valor del retraso es de más de 2 años en el futuro</li><li>El valor de <b>Después de una duración</b> no es un número</li><li>El valor de <b>Hasta un día específico</b> no es una fecha o una cadena con formato de fecha</li></ul>{:/} <br>Consulta [Errores de personalización fallida](#personaliztion-failed-errors) para obtener más detalles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las series temporales de estos análisis están disponibles en la vista ampliada de componentes.

## Solución de problemas

### Errores de personalización fallida

Si los usuarios no desencadenan un retraso personalizado, podría deberse a que el paso Context que configuraste para calificarlos para el paso de demora no funciona como esperabas. Cuando una [variable de contexto no es válida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), el usuario continuará por tu Canvas sin que el paso Context establezca su contexto. Esto puede hacer que no cumplan los requisitos para pasos posteriores en tu Canvas, como los retrasos personalizados.