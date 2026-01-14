---
nav_title: Entrega basada en acciones
article_title: Entrega basada en acciones
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo desencadenar el envío de campañas después de que un usuario complete un determinado evento."
tool: Campaigns

---

# Entrega basada en acciones

> Las campañas de entrega basadas en acciones o las campañas desencadenadas por eventos son muy eficaces para los mensajes transaccionales o basados en logros. En lugar de enviar tu campaña en determinados días, puedes desencadenar su envío después de que un usuario complete un determinado evento. 

## Configurar una campaña desencadenada

### Paso 1: Selecciona un evento desencadenante

Selecciona un evento desencadenante. Esto puede incluir cualquiera de los siguientes elementos:
- Hacer una compra
- Iniciar una sesión
- Realización de un evento personalizado
- Realización del evento de conversión primaria de la campaña
- Añadir una dirección de correo electrónico a un perfil de usuario
- Modificar el valor de un atributo personalizado
- Actualizar el estado de una suscripción
- Actualización del estado de un grupo de suscripción
- Interactuar con otras campañas
    - Ver mensaje dentro de la aplicación
    - Haz clic en el mensaje dentro de la aplicación
    - Haz clic en los botones de mensajes dentro de la aplicación
    - Haz clic en correo electrónico
    - Haz clic en alias en el correo electrónico
    - Alias con clic en cualquier campaña o paso en Canvas
    - Abrir correo electrónico
    - Abrir correo electrónico (abre la máquina)
    - Abrir correo electrónico (otras aperturas)
    - Abrir directamente la notificación push
    - Haz clic en el botón de notificación push
    - Haz clic en la página de historias push
    - Realizar evento de conversión
    - Recibir correo electrónico
    - Recibir SMS
    - Haz clic en el enlace SMS acortado
    - Recibir notificación push
    - Recibir webhook
    - Están inscritos en el grupo de control
    - Ver tarjeta de contenido
    - Haz clic en la tarjeta de contenido
    - Descartar tarjeta de contenido
- Introducir una ubicación
- Realización del evento de excepción para otra campaña
- Interactuar con un paso en Canvas
- Desencadenar una geovalla
- Enviar un mensaje SMS entrante
- Enviar un mensaje entrante de WhatsApp

También puedes filtrar aún más los eventos desencadenantes a través de [las propiedades del evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) de Braze, permitiendo propiedades del evento personalizables para eventos personalizados y compras dentro de la aplicación. Esta característica te permite adaptar aún más qué usuarios reciben un mensaje en función de los atributos específicos del evento personalizado, lo que permite una mayor personalización de la campaña y una recopilación de datos más sofisticada. 

Por ejemplo, supongamos que tenemos una campaña con un evento personalizado de carrito abandonado al que se dirige el filtro de propiedades "valor del carrito". Esta campaña sólo llegará a los usuarios que hayan dejado en sus carritos productos por valor de entre 100 y 200 $. 

\![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
El evento desencadenante "iniciar sesión" puede ser la primera apertura de la aplicación por parte del usuario, si el segmento de tu campaña se aplica a usuarios nuevos. (por ejemplo, si tu segmento está formado por los que no tienen sesión).
{% endalert %}

Ten en cuenta que aún puedes enviar una campaña desencadenada a un segmento específico de usuarios, por lo que los usuarios que no formen parte del segmento no recibirán la campaña aunque completen el evento desencadenante. Si observas que los usuarios no reciben la campaña a pesar de estar cualificados para el segmento, consulta nuestra sección sobre [por qué un usuario puede no haber recibido una campaña desencadenada]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

Con respecto al evento desencadenante para cuando un usuario añade una dirección de correo electrónico a su perfil, se aplican las siguientes reglas:

- El evento desencadenante se disparará después de que se actualice el atributo del perfil de usuario. Esto significa que la evaluación de los segmentos y filtros de la campaña se producirá después de cualquier actualización de atributos. Esto es beneficioso porque te habilita para configurar filtros como "la dirección de correo electrónico coincide con gmail.com" para crear una campaña desencadenante que sólo se envíe a usuarios de Gmail y se dispare en cuanto añadan su dirección de correo electrónico.
- El evento desencadenante se disparará cuando se añada una dirección de correo electrónico a un perfil de usuario. Si tienes varios perfiles de usuario que creas con la misma dirección de correo electrónico, la campaña puede dispararse varias veces, una por cada perfil de usuario.

Además, los mensajes desencadenados dentro de la aplicación siguen cumpliendo las normas de entrega de mensajes dentro de la aplicación y aparecen al principio de una sesión de aplicación.

\![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Paso 2: Selecciona la duración del retardo

Selecciona cuánto tiempo se debe esperar antes de enviar la campaña una vez que se cumplan los criterios desencadenantes. Si la duración del retraso elegida es superior a la duración del mensaje para su envío, ningún usuario recibirá la campaña. 

Además, los usuarios que completen el evento desencadenante después del lanzamiento de tu campaña serán los primeros en empezar a recibir el mensaje una vez transcurrido el retraso. Los usuarios que hayan completado el evento desencadenante antes del lanzamiento de la campaña no podrán recibir la campaña.

\![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

También puedes elegir enviar la campaña en un día concreto de la semana (eligiendo "el siguiente" y luego seleccionando un día) o en un número concreto de días (seleccionando "en") en el futuro. Alternativamente, puedes elegir enviar tu mensaje utilizando la característica [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) en lugar de seleccionar manualmente una hora de entrega.

\![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
\![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Paso 3: Seleccionar eventos de excepción

Selecciona un evento de excepción que descalificará a los usuarios para recibir esta campaña. Sólo puedes hacer esto si tu mensaje desencadenado se envía tras un retardo de tiempo. [Los eventos de excepción]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) pueden ser realizar una compra, iniciar una sesión, realizar uno de los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) designados de una campaña o realizar un evento personalizado. Si un usuario completa el evento de excepción, pero luego lo completa antes de que se envíe el mensaje debido al retraso, no recibirá la campaña. Los usuarios que no reciban la campaña debido al evento de excepción serán automáticamente elegibles para recibirla en el futuro, la próxima vez que completen el evento desencadenante, aunque no elijas que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

\![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Puedes leer más sobre cómo emplear eventos de excepción en nuestra sección sobre [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Si envías una campaña con un evento de excepción que coincide con el evento de excepción, Braze cancelará la campaña y volverá a programar automáticamente una nueva campaña basada en la hora de entrega del mensaje del evento de excepción. Por ejemplo, si tu primer evento de excepción empieza a los cinco minutos y el evento de excepción empieza a los 10 minutos, te basarías en los 10 minutos del evento de excepción como tiempo de entrega del mensaje de la campaña oficial.

{% alert note %}
No puedes hacer que un "inicio de sesión" sea a la vez el evento de desencadenamiento y el evento de excepción de una campaña. Sin embargo, siempre tienes la opción de seleccionar cualquier otro evento personalizado fuera de esta opción.
{% endalert %}

### Paso 4: Asignar duración

Asigna la duración de la campaña especificando una hora de inicio y una hora de finalización opcional.

\![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un usuario completa un evento desencadenante durante el plazo especificado, pero cumple los requisitos para recibir el mensaje fuera del plazo debido a un retraso programado, no recibirá la campaña. Por lo tanto, si estableces un tiempo de retardo superior al plazo del mensaje, ningún usuario recibirá tu campaña. Además, puedes elegir enviar el mensaje en las [zonas horarias locales]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns) de los usuarios.

### Paso 5: Selecciona el marco temporal

Selecciona si el usuario recibirá la campaña durante una parte específica del día. Si das al mensaje un marco temporal y el usuario completa el evento desencadenante fuera del marco temporal o el retraso del mensaje hace que se salte el marco temporal, entonces, por predeterminado, el usuario no recibirá tu mensaje.

\![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

En el caso de que un usuario complete el evento desencadenante dentro del plazo, pero el retraso del mensaje haga que el usuario quede fuera del plazo, puedes marcar la casilla siguiente para que estos usuarios sigan recibiendo la campaña.

\![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un usuario no recibe el mensaje porque se salta el plazo, seguirá estando cualificado para recibirlo la próxima vez que complete el evento desencadenante, aunque no hayas elegido que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Si decides que los usuarios vuelvan a ser elegibles, podrán recibir la campaña cada vez que completen el evento desencadenante, siempre que cumplan los requisitos durante el plazo especificado.

Si también has asignado a la campaña una duración determinada, entonces un usuario debe cumplir los requisitos tanto dentro de la duración como de la parte específica del día para recibir el mensaje.

### Paso 6: Determinar la readmisibilidad

Determina si los usuarios pueden convertirse en [re-elegibles]({% image_buster /assets/img_archive/ReEligible.png %}) para la campaña. Si permites que los usuarios vuelvan a ser elegibles, puedes especificar un plazo de tiempo antes de que el usuario pueda volver a recibir la campaña. Esto evitará que tus campañas desencadenadas se conviertan en "spam".

\![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos de uso

Las campañas desencadenadas son muy eficaces para mensajes transaccionales o basados en logros.

Las campañas de mensajería transaccional incluyen mensajes enviados después de que el usuario complete una compra o añada un artículo a su cesta. Este último caso es un gran ejemplo de campaña que se beneficiaría de un evento de excepción. Digamos que tu campaña recuerda a los usuarios los artículos de su cesta que no han comprado. El evento de excepción, en este caso, sería que el usuario comprara los productos de su cesta. Para las campañas basadas en logros, puedes enviar un mensaje 5 minutos después de que el usuario complete una conversión o supere un nivel del juego.

Además, al crear campañas de bienvenida, puedes desencadenar el envío de mensajes después de que el usuario se registre o cree una cuenta. Escalonar los mensajes para que se envíen en días diferentes tras el registro te permitirá crear un proceso de incorporación exhaustivo.

## ¿Por qué un usuario no ha recibido mi campaña desencadenada?

Cualquiera de estas cosas impedirá que un usuario que haya completado el evento desencadenante reciba la campaña:

- El usuario completó el evento de excepción antes de que transcurriera completamente el tiempo de espera.
- Se utilizó [la lógica de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) Liquid [`abort_message` y el mensaje se abortó basándose en la lógica o las reglas de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) `abort_message`.
- El tiempo de retraso hizo que el usuario estuviera cualificado para recibir la campaña una vez finalizada la duración de la misma.
- El retraso hizo que el usuario quedara habilitado para recibir la campaña fuera de la parte del día especificada.
- El usuario ya ha recibido la campaña, y los usuarios no vuelven a ser elegibles.
- Aunque los usuarios son elegibles de nuevo para recibir la campaña, sólo pueden volver a desencadenarla tras un cierto periodo de tiempo, y ese periodo de tiempo aún no ha transcurrido.

[Segmentar]({{site.baseurl}}/user_guide/engagement_tools/segments/) una campaña desencadenada en función de los datos de usuario registrados en el momento del suceso puede provocar una [condición de carrera]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Esto ocurre cuando cambia el atributo del usuario sobre el que se segmenta la campaña, pero el cambio no se ha procesado para el usuario cuando se envía la campaña. Como las campañas comprueban la pertenencia a un segmento en la entrada, esto puede hacer que el usuario no reciba la campaña.

Por ejemplo, imagina que quieres enviar una campaña desencadenada por un evento a usuarios masculinos que se acaban de registrar. Cuando el usuario se registra, grabas un evento personalizado `registration` y estableces simultáneamente el atributo `gender` del usuario. El evento puede desencadenar la campaña antes de que Braze haya procesado el sexo del usuario, impidiendo que reciba la campaña.

Como práctica recomendada, asegúrate de que el atributo sobre el que se segmenta la campaña se descarga en los servidores Braze antes del evento. Si esto no es posible, la mejor forma de garantizar la entrega es utilizar [propiedades del evento personalizadas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) para adjuntar las propiedades del usuario relevantes al evento y aplicar un filtro de propiedades para la propiedad específica del evento en lugar de un filtro de segmentación. En nuestro ejemplo, añadirías una propiedad `gender` al evento personalizado `registration` para que Braze tenga la garantía de disponer de los datos que necesitas cuando se desencadene tu campaña.

Además, si una campaña está basada en acciones y tiene un retraso, puedes marcar la opción **Volver a evaluar la pertenencia a un segmento en el momento del envío** para asegurarte de que los usuarios siguen formando parte de la audiencia objetivo cuando se envíe el mensaje.

Si tu campaña se desencadena por un evento personalizado específico y seleccionas un segmento como audiencia, los usuarios deben realizar el mismo evento personalizado para ser incluidos en el segmento. Esto significa que los usuarios deben formar parte de la audiencia antes de desencadenar una campaña basada en la acción. El flujo de trabajo general de una campaña desencadenada es el siguiente:

1. **Únete a la audiencia:** Cuando un usuario realiza el evento personalizado, se añade a la audiencia objetivo de la campaña.
2. **Desencadena el correo electrónico:** Un usuario debe volver a realizar el evento personalizado para desencadenar el correo electrónico, ya que necesita formar parte de la audiencia antes de que se pueda enviar el correo electrónico.

Recomendamos cambiar la audiencia objetivo para incluir a todos los usuarios, o comprobar que los usuarios que se espera que realicen el evento ya forman parte de la audiencia de la campaña para que se desencadene el mensaje.

\![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Solución de problemas de eventos personalizados

Primero, confirma que el evento personalizado se está pasando a Braze. Ve a **Análisis** > **Informe de eventos personalizados** y, a continuación, selecciona el evento personalizado y el intervalo de fechas correspondientes. Si el evento no se muestra, confirma que se ha configurado correctamente y que el usuario ha realizado la acción correcta.

Si aparece el evento personalizado, soluciona el problema haciendo lo siguiente:

- Comprueba la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si se desencadenó el evento, compara la fecha y hora en que se desencadenó el evento con la hora en que la campaña se puso en marcha. El evento puede haberse desencadenado antes de que la campaña estuviera en vivo.
- Revisa los registros de cambios de la campaña y de los segmentos utilizados en la segmentación para determinar si el usuario estaba en el segmento cuando se desencadenó su evento personalizado. Si no estuvieran en el segmento, no habrían recibido la campaña.
- Comprueba si el usuario fue introducido en un grupo de control mediante segmentación y, en consecuencia, se le impidió recibir la campaña.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se hubiera desencadenado antes del retraso, no habrían recibido la campaña.

{% alert note %}
Los mensajes dentro de la aplicación sólo pueden ser desencadenados por eventos enviados a través del SDK, no de la API REST.
{% endalert %}

