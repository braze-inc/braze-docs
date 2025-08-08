---
nav_title: Entrega basada en acciones
article_title: Entrega basada en acciones
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo activar campañas para que se envíen después de que un usuario complete un determinado evento."
tool: Campaigns

---

# Entrega basada en la acción

> Las campañas de entrega basadas en acciones o las campañas activadas por eventos son muy eficaces para los mensajes transaccionales o basados en logros. En lugar de enviar su campaña en determinados días, puede hacer que se envíen después de que un usuario complete un determinado evento. 

## Crear una campaña activada

### Paso 1: Seleccione un evento desencadenante

Seleccione un evento desencadenante. Esto puede incluir cualquiera de los siguientes:
- Realizar una compra
- Iniciar una sesión
- Realizar un evento personalizado
- Realización del evento de conversión principal de la campaña
- Añadir una dirección de correo electrónico a un perfil de usuario
- Modificar el valor de un atributo personalizado
- Actualizar el estado de una suscripción
- Actualización del estado de un grupo de suscripción
- Interacción con otras campañas
    - Ver mensaje en la aplicación
    - Haz clic en el mensaje de la aplicación
    - Pulsa los botones de mensajes de la aplicación
    - Hacer clic en el correo electrónico
    - Hacer clic en el alias del correo electrónico
    - Alias con clic en cualquier campaña o paso de Canvas
    - Abrir correo electrónico
    - Apertura del correo electrónico (aperturas automáticas)
    - Apertura del correo electrónico (otras aperturas)
    - Abrir directamente una notificación push
    - Haga clic en el botón de notificación push
    - Hacer clic en la página de historias push
    - Realizar evento de conversión
    - Recibir correo electrónico
    - Recibir SMS
    - Haz clic en el enlace SMS acortado
    - Recibir notificaciones push
    - Recibir webhook
    - Están inscritos en el grupo de control
    - Ver tarjeta de contenido
    - Haga clic en Tarjeta de contenido
    - Descartar tarjeta de contenido
- Introducir una ubicación
- Realizar el evento de excepción para otra campaña
- Interactuar con un paso del lienzo
- Desencadenar una geovalla
- Enviar un mensaje SMS entrante
- Enviar un mensaje entrante de WhatsApp

También puedes filtrar aún más los eventos desencadenantes a través de [las propiedades del evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) de Braze, permitiendo propiedades del evento personalizables para eventos personalizados y compras dentro de la aplicación. Esta función le permite personalizar aún más qué usuarios reciben un mensaje en función de los atributos específicos del evento personalizado, lo que permite una mayor personalización de la campaña y una recopilación de datos más sofisticada. 

Por ejemplo, supongamos que tenemos una campaña con un evento personalizado de carrito abandonado que se segmenta mediante el filtro de propiedad "valor del carrito". Esta campaña sólo llegará a los usuarios que hayan dejado en sus carritos productos por valor de entre 100 y 200 dólares. 

![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
El evento desencadenante "iniciar sesión" puede ser la primera vez que el usuario abre la aplicación si el segmento de su campaña se aplica a usuarios nuevos. (por ejemplo, si el segmento está formado por usuarios sin sesión).
{% endalert %}

Tenga en cuenta que aún puede enviar una campaña activada a un segmento específico de usuarios, por lo que los usuarios que no formen parte del segmento no recibirán la campaña aunque completen el evento de activación. Si observas que los usuarios no reciben la campaña a pesar de estar cualificados para el segmento, consulta nuestra sección sobre [por qué un usuario puede no haber recibido una campaña desencadenada]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

Con respecto al evento desencadenante para cuando un usuario añade una dirección de correo electrónico a su perfil, se aplican las siguientes reglas:

- El evento desencadenante se disparará después de que se actualice el atributo del perfil del usuario. Esto significa que la evaluación de los segmentos y filtros de la campaña tendrá lugar después de cualquier actualización de atributos. Esto es beneficioso porque te permite configurar filtros como "dirección de correo electrónico coincide con gmail.com" para crear una campaña de activación que sólo se envía a los usuarios de Gmail y se dispara tan pronto como añaden su dirección de correo electrónico.
- El evento desencadenante se disparará cuando se añada una dirección de correo electrónico a un perfil de usuario. Si tiene varios perfiles de usuario creados con la misma dirección de correo electrónico, la campaña puede dispararse varias veces, una por cada perfil de usuario.

Además, los mensajes activados en la aplicación siguen cumpliendo las normas de entrega de mensajes en la aplicación y aparecen al principio de una sesión de aplicación.

![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Paso 2: Selecciona la duración del retardo

Seleccione cuánto tiempo debe esperar antes de enviar la campaña una vez que se cumplan los criterios de activación. Si la duración del retraso elegida es superior a la duración del envío del mensaje, ningún usuario recibirá la campaña. 

Además, los usuarios que completen el evento desencadenante después del lanzamiento de su campaña serán los primeros en empezar a recibir el mensaje una vez transcurrido el plazo. Los usuarios que hayan completado el evento desencadenante antes del lanzamiento de la campaña no tendrán derecho a recibir la campaña.

![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

También puede elegir enviar la campaña en un día específico de la semana (seleccionando "el siguiente" y luego seleccionando un día) o un número específico de días (seleccionando "en") en el futuro. También puede optar por enviar su mensaje utilizando la [función de sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) en lugar de seleccionar manualmente una hora de entrega.

![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Paso 3: Seleccionar eventos de excepción

Seleccione un evento de excepción que descalificará a los usuarios para recibir esta campaña. Solo puedes hacer esto si tu mensaje desencadenado se envía tras un retardo de tiempo. [Los eventos de excepción]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) pueden ser realizar una compra, iniciar una sesión, realizar uno de los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) designados de una campaña o realizar un evento personalizado. Si un usuario completa el evento de activación, pero luego completa tu evento de excepción antes de que se envíe el mensaje debido al retraso, no recibirá la campaña. Los usuarios que no reciban la campaña debido al evento de excepción serán automáticamente elegibles para recibirla en el futuro, la próxima vez que completen el evento desencadenante, incluso si no eliges que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Puedes leer más sobre cómo emplear eventos de excepción en nuestra sección sobre [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Si envía una campaña con un evento desencadenante que coincide con el evento de excepción, Braze cancelará la campaña y volverá a programar automáticamente una nueva campaña basada en la hora de entrega del mensaje del evento de excepción. Por ejemplo, si su primer evento de activación comienza a los cinco minutos y el evento de excepción comienza a los 10 minutos, se basaría en los 10 minutos del evento de excepción como tiempo de entrega del mensaje de la campaña oficial.

{% alert note %}
No puede hacer que un "inicio de sesión" sea a la vez el evento desencadenante y el evento de excepción de una campaña. Sin embargo, siempre tiene la opción de seleccionar cualquier otro evento personalizado fuera de esta opción.
{% endalert %}

### Paso 4: Asignar duración

Asigne la duración de la campaña especificando una hora de inicio y una hora de finalización opcional.

![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Si un usuario completa un evento desencadenante durante el plazo especificado, pero cumple los requisitos para recibir el mensaje fuera del plazo debido a un retraso programado, no recibirá la campaña. Por lo tanto, si establece un tiempo de retardo superior al plazo del mensaje, ningún usuario recibirá su campaña. Además, puede elegir enviar el mensaje en las [zonas horarias locales]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns) de los usuarios.

### Paso 5: Selecciona el marco temporal

Seleccione si el usuario recibirá la campaña durante una parte específica del día. Si le das al mensaje un marco temporal y el usuario completa el evento desencadenante fuera del marco temporal o el retraso del mensaje hace que pierda el marco temporal, entonces por defecto, el usuario no recibirá tu mensaje.

![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

En el caso de que un usuario complete el evento desencadenante dentro del plazo, pero el retraso del mensaje haga que el usuario se salga del plazo, puede marcar la siguiente casilla para que estos usuarios sigan recibiendo la campaña.

![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Si un usuario no recibe el mensaje porque se le ha pasado el plazo, seguirá estando cualificado para recibirlo la próxima vez que complete el evento desencadenante, aunque no haya elegido que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Si decides que los usuarios vuelvan a ser elegibles, podrán recibir la campaña cada vez que completen el evento desencadenante, siempre que cumplan los requisitos durante el plazo especificado.

Si también ha asignado a la campaña una duración determinada, entonces un usuario debe cumplir los requisitos tanto dentro de la duración como de la parte específica del día para recibir el mensaje.

### Paso 6: Determinar la readmisibilidad

Determina si los usuarios pueden convertirse en [re-elegibles]({% image_buster /assets/img_archive/ReEligible.png %}) para la campaña. Si permite que los usuarios vuelvan a ser elegibles, puede especificar un plazo de tiempo antes de que el usuario pueda volver a recibir la campaña. Esto evitará que tus campañas desencadenadas se conviertan en "correo no deseado".

![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Casos prácticos

Las campañas activadas son muy eficaces para los mensajes transaccionales o basados en logros.

Las campañas transaccionales incluyen mensajes enviados después de que el usuario complete una compra o añada un artículo a su cesta. Este último caso es un gran ejemplo de campaña que se beneficiaría de un evento de excepción. Digamos que su campaña recuerda a los usuarios los artículos de su cesta que no han comprado. El evento de excepción, en este caso, sería que el usuario comprara los productos de su carrito. Para las campañas basadas en logros, puede enviar un mensaje 5 minutos después de que el usuario complete una conversión o supere un nivel del juego.

Además, al crear campañas de bienvenida, puede activar el envío de mensajes después de que el usuario se registre o cree una cuenta. El envío escalonado de mensajes en diferentes días tras el registro le permitirá crear un proceso de incorporación exhaustivo.

## ¿Por qué un usuario no ha recibido mi campaña activada?

Cualquiera de estas cosas impedirá que un usuario que haya completado el evento desencadenante reciba la campaña:

- El usuario completó el evento de excepción antes de que el tiempo de retardo hubiera transcurrido completamente.
- Se utilizó [la lógica de Liquid `abort_message`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) y el mensaje se anuló basándose en la lógica o las reglas de `abort_message`.
- El tiempo de retraso ha hecho que el usuario esté cualificado para recibir la campaña una vez finalizada la duración de la misma.
- El retraso provocó que el usuario quedara habilitado para recibir la campaña fuera de la franja del día especificada.
- El usuario ya ha recibido la campaña, y los usuarios no vuelven a ser elegibles.
- Aunque los usuarios pueden volver a recibir la campaña, sólo pueden volver a activarla transcurrido un cierto periodo de tiempo, y ese periodo aún no ha transcurrido.

[Segmentar]({{site.baseurl}}/user_guide/engagement_tools/segments/) una campaña activada en función de los datos de usuario registrados en el momento del evento puede provocar una [condición de carrera]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions). Esto ocurre cuando el atributo del usuario sobre el que se segmenta la campaña cambia, pero el cambio no se ha procesado para el usuario cuando se envía la campaña. Dado que las campañas comprueban la pertenencia a un segmento al entrar, esto puede hacer que el usuario no reciba la campaña.

Por ejemplo, imagine que desea enviar una campaña activada por evento a usuarios masculinos que acaban de registrarse. Cuando el usuario se registra, se graba un evento personalizado `registration` y simultáneamente se establece el atributo `gender` del usuario. El evento puede activar la campaña antes de que Braze haya procesado el sexo del usuario, impidiendo que reciba la campaña.

Como práctica recomendada, asegúrese de que el atributo sobre el que se segmenta la campaña se descarga en los servidores Braze antes del evento. Si esto no es posible, la mejor forma de garantizar la entrega es utilizar [propiedades del evento personalizadas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) para adjuntar las propiedades del usuario relevantes al evento y aplicar un filtro de propiedades para la propiedad específica del evento en lugar de un filtro de segmentación. En nuestro ejemplo, añadiría una propiedad `gender` al evento personalizado `registration` para garantizar que Braze dispone de los datos que necesita cuando se activa la campaña.

Además, si una campaña se basa en una acción y tiene un retraso, puede marcar la opción **Reevaluar la pertenencia a un segmento en el momento del envío** para asegurarse de que los usuarios siguen formando parte del público objetivo cuando se envía el mensaje.

Si su campaña es activada por un evento personalizado específico y usted selecciona un segmento como audiencia, los usuarios deben realizar el mismo evento personalizado para ser incluidos en el segmento. Esto significa que los usuarios deben formar parte de la audiencia antes de que pueda activarse una campaña basada en acciones. El flujo de trabajo general de una campaña activada es el siguiente:

1. **Únete a la audiencia:** Cuando un usuario realiza el evento personalizado, se añade al público objetivo de la campaña.
2. **Desencadena el correo electrónico:** Un usuario debe realizar el evento personalizado de nuevo para activar el correo electrónico, ya que necesita formar parte de la audiencia antes de que el correo electrónico pueda ser enviado.

Recomendamos cambiar el público objetivo para incluir a todos los usuarios, o comprobar que los usuarios que se espera que realicen el evento ya forman parte del público de la campaña para que se active el mensaje.

![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Solución de problemas de eventos personalizados

Primero, confirma que el evento personalizado se está pasando a Braze. Ve a **Análisis** > **Informe de eventos personalizados** y, a continuación, selecciona el evento personalizado y el intervalo de fechas correspondientes. Si el evento no se muestra, confirma que se ha configurado correctamente y que el usuario ha realizado la acción correcta.

Si aparece el evento personalizado, soluciona el problema haciendo lo siguiente:

- Comprueba la descarga del perfil del usuario para confirmar que desencadenó el evento y cuándo lo hizo. Si se desencadenó el evento, compara la fecha y hora en que se desencadenó el evento con la hora de inicio de la campaña. El evento puede haberse desencadenado antes de que la campaña estuviera en vivo.
- Revisa los registros de cambios de la campaña y de los segmentos utilizados en la segmentación para determinar si el usuario estaba en el segmento cuando se desencadenó su evento personalizado. Si no estuvieran en el segmento, no habrían recibido la campaña.
- Comprueba si el usuario fue introducido en un grupo de control mediante segmentación y, en consecuencia, se le impidió recibir la campaña.
- Si hay un retraso programado, comprueba si el evento personalizado del usuario se desencadenó antes del retraso. Si el evento se hubiera desencadenado antes del retraso, no habrían recibido la campaña.

{% alert note %}
Los mensajes dentro de la aplicación sólo pueden ser desencadenados por eventos enviados a través del SDK, no de la API REST.
{% endalert %}

