---
nav_title: Retraso 
article_title: Retraso 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Este artículo de referencia explica cómo añadir un retraso a tu Canvas sin necesidad de añadir un mensaje asociado."
tool: Canvas

---

# Retraso

> Los componentes de retardo te permiten añadir un retardo independiente a un Canvas. Puedes añadir un retraso a tu Canvas sin necesidad de añadir un mensaje asociado. 

Los retrasos pueden hacer que tu Canvas parezca más limpio. También puedes utilizar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día concreto o hasta un día concreto de la semana. <br> \![Un paso de Retraso con un retraso de 1 día como primer paso de un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Crear un retraso

Para crear un retraso, añade un paso a tu Canvas. Arrastra y suelta el componente Retardo desde la barra lateral, o haz clic en el botón más <i class="fas fa-plus-circle"></i> situado en la parte inferior de un paso y selecciona **Retardo**.

Hay varios detalles que debes tener en cuenta al crear un retraso en tu viaje a Canvas.

- El límite de retraso es de 30 días.
- Un componente Retardo sólo puede conectarse a un paso siguiente.

#### Retrasos prolongados

Ahora puedes prolongar los pasos de Retraso hasta dos años. Por ejemplo, si estás incorporando nuevos usuarios a tu aplicación, puedes añadir un retraso de dos meses antes de enviar un paso de Mensaje para animar a los usuarios que no han iniciado una sesión.

## Tipos de retardo

Puedes elegir el tipo de retraso antes del siguiente mensaje en tu Canvas. Puedes establecer un retraso para que tus usuarios duren hasta después de un periodo de tiempo designado, o retrasar a tus usuarios hasta una fecha y hora concretas.

{% tabs %}
{% tab Duration %}

Seleccionar **Duración** te permite retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora concreta. Por ejemplo, puedes retrasar a los usuarios cuatro horas o un día.
  
Nota la diferencia entre cómo se calculan los "días" y los "días naturales".
  
- Un "día" son 24 horas y se calcula a partir del momento en que el usuario entra en el paso Retraso. 
- Un "día del calendario" define el tiempo que hay que esperar hasta la siguiente hora especificada, que puede ser inferior a 24 horas. Puedes elegir retrasarlo a la hora de la empresa o a la hora local del usuario. Si no se especifica una hora, el usuario se retrasará hasta la medianoche del día siguiente en horario de empresa.

También puedes seleccionar **A una hora determinada** para especificar cuándo avanzarán los usuarios en el Canvas. Esta opción tiene en cuenta la hora a la que el usuario entró en el paso Retraso. Si este tiempo es superior al configurado en los ajustes, añadiremos más horas al retraso. 

Como ejemplo, digamos que hoy es 11 de diciembre, y nuestro paso Retraso está establecido en **Duración** de una semana a las 8 am UTC. Si un usuario entra en el paso Retraso el 4 de diciembre, sería liberado del paso Retraso para continuar su viaje hoy si entró originalmente en el paso Retraso a una hora anterior a las 8 de la mañana UTC. Si entraron en el paso Retraso después de esta hora, el usuario será retrasado hasta el día siguiente (la próxima vez que se produzca esta hora). 

{% endtab %}
{% tab Calendar date %}

Seleccionar **Fecha del calendario** te permite retener a los usuarios en el paso hasta una fecha y hora concretas.

#### Consideraciones

##### Los usuarios no recibirán pasos o mensajes con fecha pasada

Si la fecha y hora seleccionadas ya han pasado para cuando los usuarios pasen al paso Retraso, los usuarios saldrán del Canvas. Puede haber hasta 31 días entre el inicio del Canvas y las fechas elegidas para los pasos de "esperar hasta un día exacto".

{% alert important %}
Si participas en el [acceso anticipado del Contexto Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), puedes establecer retrasos de hasta 2 años.
{% endalert %}

Por ejemplo, los usuarios no recibirán pasos ni mensajes en estos escenarios:

- Se ha programado el envío de un mensaje para el 3 de mayo a las 21:00, pero el paso Retrasar caduca el 3 de mayo a las 9:00. 
- Un paso en Canvas se retrasa hasta una hora determinada en la zona horaria local del usuario, pero éste no tiene una zona horaria configurada en su perfil de usuario. Entonces, el retraso se predetermina a la zona horaria de la empresa para estos usuarios, que ya ha pasado la hora especificada. 
  
##### Los usuarios saldrán si un paso de Retraso posterior está dentro de la línea temporal de un paso de Retraso anterior

Si el Canvas tiene dos pasos de Retraso, pero el primer paso de Retraso es más largo que el segundo, los usuarios también saldrán del Canvas. 

Por ejemplo, supongamos que un Canvas tiene estos pasos:
- Paso 1: Paso de la mensajería
- Paso 2: Paso aplazado hasta el 13 de diciembre a las 22.00 h
- Paso 3: Paso de la mensajería
- Paso 4: Paso aplazado hasta el 13 de diciembre a las 19.00 h
- Paso 5: Paso de la mensajería
  
Los usuarios que entren en el Paso 4 saldrán del Canvas antes de recibir el Paso 5, porque el retraso del Paso 4 forma parte del plazo del Paso 2.

{% endtab %}
{% tab Day of the week %}

Seleccionar **Día de la semana** te permite retener a los usuarios en el paso hasta un día concreto de la semana, a una hora concreta. Por ejemplo, puedes retrasar a los usuarios hasta que llegue el próximo jueves a las 16 h en la zona horaria de la empresa. 

Para configurarlo correctamente, también tendrás que seleccionar qué ocurre si el usuario entra en el Canvas el día de la semana seleccionado (por ejemplo, el jueves), pero después de la hora especificada. Puedes elegir avanzar al usuario el mismo día o retenerlo hasta la semana siguiente.
{% endtab %}
{% endtabs %}

## Utilizar pasos de Retraso

Digamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entraran en el Canvas y recibieran un mensaje sobre una próxima promoción. Entonces, querrás retener a los usuarios en el Canvas hasta el 17 de junio a las 15.00, hora local. A las 15:00 hora local del 17 de junio, quieres enviar a los usuarios un mensaje recordatorio sobre la promoción.

La secuencia de pasos en Canvas podría tener el siguiente aspecto:

1. Empieza por añadir un paso en Canvas que envíe mensajes inmediatamente después de que los usuarios entren en Canvas el 11 de junio.
2. Crea un paso de Retraso que retenga a los usuarios hasta la 1 de la tarde, hora local, del 17 de junio.
3. Vincula el paso Retraso a otro paso Mensaje que envíe su mensaje inmediatamente.

### Componentes de retardo al final de un Canvas {#delay-as-last-step}

Si añades un componente de Retraso a tu Canvas y no hay pasos posteriores, cualquier usuario que llegue al último paso avanzará automáticamente fuera del Canvas. Esto es así aunque aún no se haya alcanzado el tiempo del paso Retraso. Esto significa que los usuarios que ya hayan alcanzado el paso Retraso no recibirán ningún mensaje que añadas después de este paso. Sin embargo, si un usuario no ha llegado al paso Retraso y se añade un mensaje, entonces recibiría ese mensaje.

### Retrasos personalizados

{% alert important %}
Los retrasos personalizados y los retrasos ampliados están en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

Selecciona el alternador **Personalizar retraso** para establecer un retraso personalizado para tus usuarios. Puedes utilizarlo con un [paso Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para seleccionar la variable contextual por la que retrasar. Esto anulará la hora del día establecida en el atributo o propiedad seleccionados. Esto es útil cuando aplicas un desfase en días o semanas, y quieres que los usuarios avancen en un momento concreto. La zona horaria procede del atributo o propiedad, o utiliza la alternativa si no hay ninguna disponible. 

#### Comportamiento de la zona horaria para "a una hora determinada"

Al configurar los retrasos personalizados con la opción **a una hora determinada**, el comportamiento de la zona horaria depende del tipo de datos de tu atributo o variable contextual:

- **Tipo de datos de cadena con zona horaria:** Si el atributo o la variable de contexto es un tipo de dato de cadena que incluye información sobre la zona horaria, se ajusta a la zona horaria especificada en la cadena. Por ejemplo, `2025-06-10T10:00:00-08:00` utiliza UTC-8.
- **Tipo de datos de cadena sin zona horaria:** Si el atributo o la variable de contexto es un tipo de datos de cadena sin información sobre la zona horaria, se ajusta a la zona horaria alternativa. Por ejemplo, `2025-06-10` utiliza la zona horaria alternativa.
- **Tipo de datos de tiempo:** Si el atributo o variable contextual es un tipo de dato temporal, se ajusta a UTC. Esto se debe a que el tipo de datos de hora siempre se convierte a UTC cuando se guarda en la base de datos, por lo que "a una hora determinada" siempre hará referencia a UTC cuando la variable esté configurada con el tipo de datos de hora. Por ejemplo, `2025-06-10T10:00:00-08:00` utiliza UTC+0.

{% alert note %}
Es posible que un atributo personalizado o una variable de contexto no tenga ni una hora concreta ni una zona horaria si es un tipo de datos de cadena. Si es un tipo de dato horario, tendrás que especificar la hora y la zona horaria. Sin embargo, si el atributo personalizado o la variable de contexto es una cadena "irrelevante" (como "product_name"), ), el usuario saldrá del Canvas.
{% endalert %}

#### Casos de uso

Supongamos que quieres recordar a tus clientes que compren pasta de dientes dentro de 30 días. Utilizando una combinación de un paso Contexto y un paso Retraso, puedes seleccionar esta variable de contexto para retrasarla. En este caso, tu paso Contexto tendría los siguientes campos:

- **Nombre de la variable contextual:** product_reminder_interval
- **Tipo de datos:** Tiempo
- **Valor:** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

\![El "product_reminder_interval" y su valor.]({% image_buster /assets/img/context_step1.png %})

A continuación, como quieres recordárselo a tus clientes dentro de 30 días, seleccionarás **Hasta un día concreto** como opción de retraso y seleccionarás **Personalizar retraso** para utilizar la información de tu paso Contexto. Esto significa que tus usuarios se retrasarán hasta la variable Contexto seleccionada.

## Análisis de retrasos

Los componentes de retraso tienen las siguientes métricas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| _Entró en_ | Refleja el número de veces que se ha introducido el paso. Si tu Canvas es reeleccionable y un usuario entra dos veces en un paso de Retraso, se registrarán dos entradas. |
| _Pasar al siguiente paso_ | Refleja el número de entradas que pasaron al siguiente paso en Canvas. |
| _Lienzo Exited_ | Refleja el número de entradas que salieron del Canvas y no pasaron al siguiente paso. |
| _Error de personalización_ | Refleja el número de veces que un mensaje o contenido personalizado destinado a un usuario no se pudo entregar debido a lo siguiente:<br> {::nomarkdown}<ul><li>El valor del retraso está en el pasado</li><li>El valor del retraso es de más de 2 años en el futuro</li><li><b>Cuando un</b> valor de <b>duración</b> no es un número</li><li><b>Hasta que el</b> valor de <b>un día concreto</b> no sea una fecha o una cadena con formato de fecha</li></ul>{:/} <br>Consulta [Errores de personalización fallidos](#personaliztion-failed-errors) para obtener más detalles. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las series temporales de estos análisis están disponibles en la vista ampliada de componentes.

## Solución de problemas

### Errores de personalización fallidos

Si los usuarios no están desencadenando un retraso personalizado, podría deberse a que el paso Contexto que estableciste para calificarlos para el paso Retraso no está funcionando como esperabas. Cuando una [variable de contexto no es válida]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), un usuario continuará a través de tu Canvas sin que su contexto haya sido establecido por el paso en Contexto. Esto puede hacer que no cumplan los requisitos para los pasos posteriores en tu Canvas, como los retrasos personalizados.

