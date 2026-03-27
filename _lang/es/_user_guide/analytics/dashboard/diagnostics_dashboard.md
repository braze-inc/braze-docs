---
nav_title: Panel de diagnóstico de mensajería
article_title: Panel de diagnóstico de mensajería
description: "Este artículo de referencia trata sobre el panel de diagnóstico de mensajería, que te ayuda a comprender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba."
alias: /ccdd/
page_order: 4.5
toc_headers: h2
---

# Panel de diagnóstico de mensajería

> El panel **Diagnóstico de mensajería** proporciona un desglose de alto nivel de los resultados del envío de mensajes, lo que te permite detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este panel te puede ayudar a comprender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba.

{% alert important %}
El panel **Diagnóstico de mensajería** se encuentra actualmente en fase de acceso anticipado. Si te interesa participar en el acceso anticipado, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Conceptos clave

### Enviado y entregado

Es fundamental comprender que este panel informa sobre cómo Braze procesó internamente un mensaje, no sobre el estado final de entrega del mensaje.

Un mensaje marcado como "enviado" en este panel significa que Braze procesó y envió correctamente el mensaje. Para la mayoría de los canales, esto significa que Braze transfirió el mensaje al socio externo correspondiente encargado del envío. Sin embargo, no garantiza la entrega final al dispositivo del usuario. 

Cuando Braze "envía" un mensaje, la entrega final puede depender de servicios externos. Considera los siguientes ejemplos para cada canal.

| Canal | Ejemplo de entrega final |
| --- | --- |
| Tarjetas de contenido | La tarjeta se envió y es elegible para ser vista. |
| Correo electrónico | Braze entrega el mensaje a un proveedor de servicios de correo electrónico (ESP). El ESP es entonces responsable de la entrega final. Ese ESP, por ejemplo, puede informar de un "rebote" si la dirección de correo electrónico no es válida o el buzón de entrada está lleno. |
| Mensajes dentro de la aplicación | El mensaje se mostró al usuario. |
| LINE | El mensaje se entregó correctamente a un socio de envío. |
| Push | Braze envía el mensaje al servicio de notificaciones push adecuado (como Apple Push Notification service para iOS o Firebase Cloud Messaging para Android). Ese servicio es responsable de la entrega final de la notificación al dispositivo. |
| SMS/MMS/RCS | Braze envía el mensaje a una pasarela SMS (como Twilio). Esa pasarela es responsable de la entrega final al operador móvil. |
| Webhooks | La solicitud de webhook se realizó correctamente y devolvió una respuesta `2xx`. |
| WhatsApp | El mensaje se entregó correctamente a un socio de envío. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Actualización de los datos

La frecuencia con la que se actualizan los datos de este panel puede variar en función de la carga del sistema. Aunque no se garantiza la frecuencia de actualización, en la mayoría de los casos suele ser inferior a una hora.

## Configuración del panel

Puedes acceder al panel de diagnóstico yendo a **Análisis** > **Creador de paneles** y seleccionando **Diagnóstico de mensajería** en la lista de paneles creados por Braze.

Para ejecutar el panel y ver tus datos:

1. Elige entre **Campañas** o **Canvas** como fuente para los informes de tu panel. 
2. Selecciona una o varias campañas o Canvas.
3. Selecciona **Ejecutar panel** para cargar los datos de los filtros seleccionados.

![Ejemplo de diagnóstico de campaña y Canvas del 25 al 31 de mayo de 2025 para una campaña de serie de bienvenida.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpretación de los datos

{% alert note %}
El panel solo muestra los datos de los últimos 7 días. 
{% endalert %}

### Mosaicos de resumen

En la parte superior de la página, hay mosaicos con resúmenes clave para el periodo de tiempo seleccionado que muestran:

- **Total de cancelaciones:** El recuento total de mensajes que fueron cancelados. Esto incluye a los miembros de la audiencia de Canvas que no entraron en el Canvas o salieron del Canvas porque experimentaron un error en un paso o cumplieron con los criterios de salida mientras realizaban un evento de salida.
- **Mensajes enviados:** El recuento total de mensajes que Braze procesó y envió correctamente. 
  - **Correo electrónico, SMS/MMS/RCS, WhatsApp, LINE y push:** El mensaje se entregó correctamente a un socio de envío.  
  - **Webhooks:** La solicitud de webhook se realizó correctamente y devolvió una respuesta `2xx`.  
  - **Tarjetas de contenido:** La tarjeta se envió y es elegible para ser vista.    
  - **Mensajes dentro de la aplicación:** El mensaje se mostró al usuario.

### Resultados de los mensajes a lo largo del tiempo

Este gráfico de series temporales muestra un desglose diario de las diferentes razones por las que se canceló un mensaje o se eliminó a un usuario de Canvas. Este gráfico no muestra el número de envíos.  

{% alert note %}
Para mantener el gráfico organizado, cualquier motivo de cancelación o eliminación con cero ocurrencias en el intervalo de tiempo seleccionado no aparece en el gráfico.
{% endalert %}

### Desglose de los resultados de los mensajes

Este gráfico muestra el desglose de todos los resultados de los mensajes dentro del intervalo de tiempo seleccionado. Ofrece una visión completa de:
- El número total de envíos como proporción de todos los resultados.  
- El desglose proporcional de cada motivo de cancelación y eliminación. Esto te ayuda a identificar rápidamente las razones más comunes por las que no se envían los mensajes.

### Resultados de cancelaciones

Las siguientes definiciones explican los resultados de cancelaciones que se muestran en el panel. Los resultados se agrupan por categorías para facilitar la búsqueda del que estás investigando.

#### Contenido y renderización

| Resultado de la cancelación | Explicación |
| ---- | ---- |
| Tarjeta de contenido caducada | La tarjeta de contenido caducó antes de que el usuario la viera. |
| Tarjeta de contenido no válida | La tarjeta de contenido tenía errores y no se envió al usuario. Algunas razones comunes incluyen: {::nomarkdown}<ul><li> Se superó el tamaño máximo (2 KB) </li><li> La fecha de caducidad no es válida </li><li> El mensaje contiene caracteres no válidos </li></ul>{:/} |
| Contenido conectado fallido | Braze intentó enviar el mensaje, pero el contenido conectado falló tras alcanzar el número máximo de reintentos (el valor predeterminado es cinco). **Nota:** Este recuento representa el número de mensajes cancelados por haber alcanzado el número máximo de reintentos, no el número total de solicitudes de contenido conectado fallidas. |
| Tiempo de espera en la renderización de mensajes dentro de la aplicación | Tras múltiples intentos de reintento, no se pudo renderizar Liquid y se agotó el tiempo de espera. |
| Cancelación por Liquid | Se llamó a la etiqueta de Liquid [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages), por lo que se canceló el envío. |
| Tiempo de espera en la renderización de Liquid | La plantilla Liquid tardó demasiado en renderizarse. Es más probable que ocurra en banners, mensajes dentro de la aplicación y correos electrónicos. |
| Error de sintaxis de Liquid | La plantilla Liquid tenía un error de análisis, por lo que se canceló el mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Estado de la campaña y de Canvas

| Resultado de la cancelación | Explicación |
| ---- | ---- |
| Fallo en el paso de retraso | El [paso de retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) falló, lo que provocó que el usuario saliera del Canvas. Este fallo puede producirse cuando: {::nomarkdown}<ul><li> La variable proporcionada al paso de retraso personalizado estaba vacía o era de un tipo no válido </li><li> El retraso supera la duración máxima permitida dentro del Canvas</li></ul>{:/} |
| Evento de excepción o de salida | El usuario era anteriormente elegible para recibir el mensaje, pero: {::nomarkdown}<ul><li> realizó un <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">evento de excepción</a> para una campaña basada en acciones, por lo que el mensaje se canceló, o </li><li> cumplió los <a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">criterios de salida</a> del Canvas, por lo que fue eliminado a mitad del recorrido.</li></ul>{:/} |
| Campaña inactiva | La campaña se detuvo mientras el mensaje estaba en tránsito, por lo que se canceló. |
| Canvas inactivo | El Canvas se detuvo antes de que el usuario iniciara el recorrido. |
| Paso en Canvas inactivo | Esto puede ocurrir en Canvas si: {::nomarkdown}<ul><li> Se eliminó el paso en Canvas </li> <li>Se detuvo el Canvas, lo que provocó que todos los pasos se desactivaran </li></ul>{:/} |
| Volumen limitado | La campaña alcanzó el límite de volumen establecido, por lo que se canceló el envío. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Límite de velocidad y temporización

| Resultado de la cancelación | Explicación |
| ---- | ---- |
| Limitación de frecuencia | El usuario ya recibió el número máximo de mensajes permitido según las reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) de tu espacio de trabajo, por lo que el envío se canceló. |
| Cancelación por horas tranquilas | Se habilitaron las horas tranquilas para la campaña o el paso en Canvas con la alternativa establecida en **Cancelar mensaje**. El usuario desencadenó la campaña o entró en el paso de mensaje de Canvas durante las horas tranquilas, por lo que el mensaje se canceló. Sin embargo, esto no saca al usuario del Canvas. |
| Límite de velocidad durante más de 72 horas | El mensaje se retrasó durante más de 72 horas debido a los [límites de velocidad de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), por lo que se canceló el envío. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Elegibilidad y perfil del usuario

| Resultado de la cancelación | Explicación |
| ---- | ---- |
| Identificador de usuario duplicado | Varios usuarios con un identificador coincidente (como ID externo, dirección de correo electrónico, número de teléfono) eran elegibles para recibir este mensaje. Para evitar envíos duplicados al mismo usuario, este mensaje fue cancelado. |
| El usuario no superó la verificación previa del paso de mensaje | Esta verificación previa se ejecuta antes de las validaciones de entrega. Cuando esto ocurre, el usuario no superó la verificación previa básica para este paso de mensaje (no se encontró al usuario o no es elegible para el canal del paso de mensaje). **Nota:** En el caso de un paso de mensaje multicanal, esto significa que no se encontró al usuario; la elegibilidad del canal solo se comprueba aquí para los pasos de mensaje de un solo canal. |
| El usuario no superó la verificación previa para el mensaje desencadenado | Para un mensaje desencadenado, Braze realiza una primera serie de verificaciones básicas previas para comprobar la elegibilidad de la audiencia, la reelegibilidad y la elegibilidad del canal antes de crear un mensaje para enviar desde este desencadenador. |
| El usuario ya no es elegible | El usuario inicialmente formaba parte de la audiencia objetivo, pero ya no cumplía los criterios de audiencia antes de que Braze enviara el mensaje o introdujera al usuario en el Canvas. El tiempo transcurrido entre el momento en que el usuario cumple inicialmente los criterios de audiencia y el momento en que deja de cumplirlos puede deberse a retrasos por: {::nomarkdown}<ul><li>Intelligent Timing</li><li>Horas tranquilas</li><li>Hora local</li><li>Límites de velocidad de entrega (no aplicable a las entradas de Canvas)</li><li>Retrasos en el canal de mensajería</li></ul>{:/} |
| Usuario no elegible para el paso | El usuario salió del Canvas porque no cumplió con las [validaciones de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) establecidas para el paso de mensaje o porque formaba parte de una [lista de supresión]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists). |
| Usuario no reelegible | El usuario era elegible para recibir el mensaje o entrar en el Canvas, pero el envío se canceló debido a la configuración de reelegibilidad o reentrada. Esto puede suceder si el usuario ya recibió la campaña o entró en el Canvas hace muy poco tiempo, si ya se está realizando otro envío de la misma campaña para este usuario, o si la reelegibilidad o la reentrada están desactivadas. |
| Perfil de usuario no encontrado | El usuario nunca existió o ya no existe en Braze. Algunos casos comunes incluyen: {::nomarkdown}<ul><li> El usuario fue seleccionado mediante mensajería API, pero nunca existió en Braze. </li><li>El usuario fue eliminado antes de que se enviara el mensaje o se ejecutara el paso en Canvas. </li><li>El usuario se fusionó con otro perfil antes de enviar el mensaje.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Canal y entrega

| Resultado de la cancelación | Explicación |
| ---- | ---- |
| Tiempo de espera de entrega del socio | Braze intentó enviar este mensaje a tu socio de entrega durante 24 horas, pero el socio devolvió errores temporales durante todo ese periodo. |
| Credenciales push no válidas | Las [credenciales push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) para esta aplicación faltan o no son válidas, por lo que el envío se canceló. Actualiza tus credenciales en **Configuración de la aplicación**. |
| Usuario no habilitado para push de Android, aplicación o dispositivo | No se pueden enviar notificaciones push a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene la aplicación instalada.</li> <li> El usuario no tiene un token de notificaciones push válido. </li> <li>El usuario no dispone del dispositivo necesario para esta notificación push. </li> <li> El usuario ha desactivado las notificaciones de esta aplicación en la configuración de su dispositivo. </li> <li> El usuario no está suscrito ni ha realizado adhesión voluntaria para recibir notificaciones push.</li></ul>{:/} |
| Usuario no habilitado para push de iOS, aplicación o dispositivo | Igual que el resultado de cancelación "Usuario no habilitado para push de Android, aplicación o dispositivo". |
| Usuario no habilitado para push de Kindle, aplicación o dispositivo | Igual que el resultado de cancelación "Usuario no habilitado para push de Android, aplicación o dispositivo". |
| Usuario no habilitado para push web, aplicación o dispositivo | Igual que el resultado de cancelación "Usuario no habilitado para push de Android, aplicación o dispositivo". |
| Usuario no habilitado para tarjetas de contenido | El usuario no ha utilizado ninguna aplicación que incluya esta tarjeta de contenido. |
| Usuario no habilitado para correo electrónico | No se pueden enviar correos electrónicos a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene una dirección de correo electrónico en su perfil de usuario. </li><li> El estado de suscripción del usuario lo excluye de recibir este correo electrónico. </li><li> La dirección de correo electrónico del usuario ha sido marcada previamente como no válida (rebote duro). </li><li> Los mensajes enviados a esta dirección de correo electrónico se marcan sistemáticamente como correo no deseado, por lo que el envío se canceló.</li></ul>{:/} |
| Usuario no habilitado para LINE | No se pueden enviar mensajes de LINE a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a errores en la entrega. </li><li> El estado de suscripción del usuario lo excluye de recibir este mensaje. </li><li> El usuario no tiene un ID de LINE.</li></ul>{:/} |
| Usuario no habilitado para SMS/MMS/RCS | No se pueden enviar mensajes SMS a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a errores en la entrega. </li><li> El número de teléfono del usuario no tiene un formato E.164 válido y los intentos de formatearlo automáticamente fallaron. </li><li> El estado de suscripción del usuario lo excluye de recibir el mensaje SMS.</li><li>El número de teléfono del usuario se encuentra en un país bloqueado.</li></ul>{:/} |
| Usuario no habilitado para WhatsApp | No se pueden enviar mensajes de WhatsApp a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a errores en la entrega. </li><li> El estado de suscripción del usuario lo excluye de recibir este mensaje. </li><li> El usuario no tiene una cuenta de WhatsApp.</li></ul>{:/} |
| Error en el webhook | El webhook recibió un código de respuesta no exitoso (no `2xx`). Consulta el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) para obtener más detalles. Los registros con más de 60 horas de antigüedad se eliminan y ya no son accesibles; los errores de webhook se muestrean hasta un máximo de 20 registros por hora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas frecuentes

### ¿Qué significa un fallo en la "verificación previa"?

Una "verificación previa" se refiere a una comprobación de validación agrupada y de alta velocidad que se ejecuta al comienzo de una etapa del proceso (como el desencadenamiento de un mensaje o el envío de un paso de mensaje en Canvas). Piensa en ello como una salida anticipada diseñada para alcanzar la máxima velocidad. En lugar de realizar muchas comprobaciones independientes que consumen muchos recursos (como validar cada detalle del perfil de usuario), Braze agrupa varias validaciones básicas en una "primera pasada".

Si un usuario no supera esta única comprobación agrupada, se lo excluye inmediatamente. Este enfoque combinado permite a Braze procesar grandes volúmenes de mensajes a gran velocidad y puede contribuir a un rendimiento más rápido y estable de tus campañas y Canvas, al reducir la latencia de procesamiento de cada mensaje.

### ¿Qué significa un resultado de cancelación "otro"?

Son cancelaciones que no encajaron en ninguna de las categorías preexistentes de Braze. Si notas una gran proporción de cancelaciones con este resultado, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support) para obtener más ayuda.

### ¿Por qué la suma del _total de cancelaciones_ y _mensajes enviados_ es inferior al tamaño de audiencia esperado?

Esto puede ocurrir por varias razones:

- **Criterios de audiencia:** Es posible que menos usuarios de los esperados cumplieran los criterios de audiencia (por ejemplo, no pertenecían al segmento o no tenían los atributos necesarios) cuando se lanzó la campaña o el Canvas.
- **Procesamiento en curso:** Es posible que los mensajes aún se estén procesando activamente. Los usuarios pueden encontrarse aún en pasos anteriores del Canvas y no haber llegado a ningún paso de mensaje.
- **Actualización de los datos:** Los datos del panel se actualizan aproximadamente cada 15 minutos, pero esto no es una garantía. Es posible que los datos más recientes de esta campaña o Canvas aún no hayan llegado al panel.
- **Casos extremos:** Existe una pequeña posibilidad de que te encuentres con un caso extremo que no se refleja en este panel en este momento. Si sospechas que este es el caso, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### ¿Por qué la suma del _total de cancelaciones_ y _mensajes enviados_ es mayor que la audiencia de una campaña o Canvas?

Esto puede ocurrir por las siguientes razones:

- **Mensajes multicanal:** La campaña o el paso en Canvas se configuró para enviar mensajes a través de múltiples canales (como SMS y correo electrónico). Un solo usuario puede recibir un resultado "enviado" para un canal (como correo electrónico) y un resultado "cancelado" para otro (como "Usuario no habilitado para SMS/MMS/RCS"). En este caso, ese usuario se contabilizaría dos veces en el gráfico: una como "enviado" y otra como "cancelado".
  - **Ejemplo:** Envías una campaña push a 100 usuarios, dirigida tanto a iOS como a Android. Si un usuario solo tiene un dispositivo iOS, recibirá la notificación push de iOS ("enviada"), pero también se desencadenará una cancelación para la notificación push de Android ("Usuario no habilitado para push de Android, aplicación o dispositivo").
- **Varios pasos de mensaje (solo Canvas):** Tu Canvas puede tener más de un paso de mensaje en una ruta determinada. Este panel agrega todos los resultados, por lo que un mismo usuario podría contabilizarse varias veces si pasa por varios pasos de mensaje dentro del intervalo de tiempo seleccionado.
- **Mensajes de prueba:** El envío de pruebas (que se contabiliza en el panel) hace que el recuento total sea superior al tamaño de la audiencia.