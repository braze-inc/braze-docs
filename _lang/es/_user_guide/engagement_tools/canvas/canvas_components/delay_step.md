---
nav_title: Demora 
article_title: Demora 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre cómo añadir un retraso a tu Canvas sin necesidad de añadir un mensaje asociado."
tool: Canvas

---

# Demora

> Los componentes de retardo permiten añadir un retardo independiente a un lienzo. Puede añadir un retraso a su lienzo sin necesidad de añadir un mensaje asociado. 

Los retrasos pueden hacer que su lienzo parezca más limpio. Si antes tenía que crear dos pasos completos, ahora puede crear un paso de retardo y un único paso completo. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

También puede utilizar este componente para retrasar un paso diferente hasta una fecha exacta, hasta un día específico o hasta un día específico de la semana.

## Crear un retraso

Para crear un retraso, primero añada un paso a su Lienzo. Arrastre y suelte el componente Retardo desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Retardo**.

Hay varios detalles que debes tener en cuenta al crear un retraso en tu recorrido de Canvas.
- El límite de retraso es de 30 días.
- Un componente de retardo sólo puede conectarse a un paso siguiente.

### Opciones de temporización

Puedes elegir el tipo de retraso antes del siguiente mensaje en tu Canvas. Puedes establecer un retraso para que tus usuarios duren hasta después de un periodo de tiempo designado, o retrasar a tus usuarios hasta una fecha y hora específicas.

{% tabs %}
  {% tab Después de una duración %}

  La opción **Después de una duración** permite retrasar a los usuarios durante un número determinado de segundos, minutos, horas, días o semanas, y a una hora concreta. Por ejemplo, puedes retrasar a los usuarios cuatro horas o un día. 
  
  Tenga en cuenta la diferencia entre cómo se calculan los "días" y los "días naturales". 
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  {% endtab %}
  {% tab Hasta una fecha determinada %}

  La opción **Hasta una fecha determinada** permite retener a los usuarios en el paso hasta una fecha y hora determinadas.

  {% alert important %}
  Si la fecha y hora seleccionadas ya han pasado para cuando los usuarios procedan al paso Retrasar, los usuarios saldrán del Lienzo. Puede haber un máximo de 31 días entre el inicio del Lienzo y las fechas elegidas para los pasos "Esperar hasta la fecha exacta".
  {% endalert %}
  {% endtab %}
  {% tab Hasta un día concreto de la semana %}

  La opción **Hasta un día concreto de la semana** permite retener a los usuarios en el paso hasta un día concreto de la semana, a una hora concreta. Por ejemplo, puedes retrasar a los usuarios hasta que llegue el próximo jueves a las 16:00 en la zona horaria de la empresa. 

  Para configurarlo correctamente, también tendrá que seleccionar qué ocurre si el usuario entra en el lienzo el día de la semana seleccionado (por ejemplo, el jueves), pero después de la hora especificada. Puede optar por adelantar al usuario el mismo día o retenerlo hasta la semana siguiente.
  {% endtab %}
{% endtabs %}

## Utilizar pasos de retraso

Digamos que es 10 de junio. El 11 de junio, te gustaría que los usuarios entraran en el Canvas y recibieran un mensaje sobre una próxima promoción. Entonces, querrás retener a los usuarios en el Canvas hasta el 17 de junio a las 15:00, hora local. A las 15:00 hora local del 17 de junio, quieres enviar a los usuarios un mensaje recordatorio sobre la promoción.

Empezaría por añadir un paso completo que se envíe inmediatamente después de que los usuarios entren en el lienzo el 11 de junio. Entonces, crearías un paso de retraso que retuviera a los usuarios en el paso hasta las 15:00, hora local, del 17 de junio. Después, enlazarías el paso de retraso con un paso completo que envíe su mensaje inmediatamente.

### Componentes de retardo al final de un lienzo {#delay-as-last-step}

Si añades un componente de Retraso a tu Canvas, pero no hay más pasos después del componente de retraso, cualquier usuario que llegue al último paso avanzará automáticamente fuera del Canvas. Esto es así aunque aún no se haya alcanzado el tiempo del paso Retraso. Esto significa que, para los usuarios que ya han alcanzado el paso de Retraso, no recibirán ningún mensaje que añadas después del paso de Retraso. Sin embargo, si un usuario no ha llegado al paso Retraso y se añade un mensaje, entonces recibiría ese mensaje.

## Análisis de retrasos

Los retrasos tienen tres estadísticas disponibles en la vista de análisis de un Canvas activo o previamente activo.

| Métrica | Descripción |
|---|---|
| `Entered` | Refleja el número de veces que se ha introducido el paso. Si su Lienzo tiene reelegibilidad y un usuario introduce un paso de retraso dos veces, se registrarán dos entradas. |
| `Proceeded to Next Step` | Refleja el número de entradas que pasaron al siguiente paso en el Canvas. |
| `Exited Canvas` | Refleja el número de entradas que salieron del Canvas y no pasaron al siguiente paso. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las series temporales de estos análisis están disponibles en la vista ampliada de componentes.

[1]: {% image_buster /assets/img/canvas_delay.png %}
