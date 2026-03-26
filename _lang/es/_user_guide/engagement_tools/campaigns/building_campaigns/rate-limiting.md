---
nav_title: Limitación de velocidad y limitación de frecuencia
article_title: Limitación de velocidad y frecuencia
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artículo de referencia analiza el concepto de limitación de velocidad y frecuencia en las campañas, y cómo puedes gestionar la presión del marketing para mejorar la experiencia del usuario."

---

# Limitación de velocidad y limitación de frecuencia

> La limitación de velocidad y la limitación de frecuencia se pueden utilizar conjuntamente para garantizar que los usuarios reciban los mensajes que necesitan.

## Sobre el límite de velocidad

Braze te permite controlar la presión del marketing limitando la velocidad de tus campañas, regulando la cantidad de tráfico saliente de tu plataforma. Puedes implementar dos tipos diferentes de límite de velocidad para tus campañas: 

1. [Limitación de velocidad centrada en el usuario:](#user-centric-rate-limiting) Se centra en proporcionar la mejor experiencia al usuario.
2. [Limitación de la velocidad de entrega:](#delivery-speed-rate-limiting) Tiene en cuenta el ancho de banda de tus servidores.

Braze intentará distribuir de manera uniforme los mensajes enviados a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una campaña con un límite de velocidad de 5000 mensajes por minuto, intentaremos distribuir las 5000 solicitudes de manera uniforme a lo largo del minuto (aproximadamente 84 mensajes por segundo), pero puede haber algunas variaciones en la tasa por segundo.

### Limitación de velocidad centrada en el usuario

A medida que crees más segmentos, habrá casos en los que los miembros de esos segmentos se solapen. Si envías campañas a esos segmentos, debes asegurarte de no enviar mensajes a tus usuarios con demasiada frecuencia. Si un usuario recibe demasiados mensajes en poco tiempo, se sentirá agobiado y desactivará las notificaciones push o desinstalará tu aplicación.

#### Filtros de segmentos relevantes

Braze ofrece los siguientes filtros para ayudarte a limitar la frecuencia con la que tus usuarios reciben mensajes:

- Última interacción con un mensaje
- Último mensaje recibido
- Última notificación push recibida
- Último correo electrónico recibido
- Último SMS recibido

#### Aplicación de filtros

Supongamos que hemos creado un segmento denominado "Retargeting Filter Showcase" con un filtro "Última aplicación utilizada hace más de 7 días" para dirigirnos a los usuarios. Sería un segmento estándar de reactivación de la interacción.

Si tienes otros segmentos más específicos que han recibido notificaciones recientemente, es posible que no desees que tus usuarios sean objeto de campañas más genéricas dirigidas a este segmento. Al añadir el filtro "Última notificación push recibida" a este segmento, el usuario se ha asegurado de que, si ha recibido otra notificación en las últimas 24 horas, saldrá de este segmento durante las próximas 24 horas. Si 24 horas después siguen cumpliendo los demás criterios del segmento y no han recibido más notificaciones, volverán a entrar en el segmento.

![Un segmento denominado "Retargeting Filter Showcase" con el grupo de filtros "Última aplicación utilizada hace más de 7 días".]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

Si se aplica este filtro a todos los segmentos a los que se dirigen las campañas, los usuarios recibirán como máximo una notificación push cada 24 horas. Así podrás priorizar tus mensajes, asegurándote de que los más importantes se envían antes que los menos importantes.

#### Establecer un límite máximo de usuarios

En el paso **Audiencia objetivo** del compositor de campañas, también puedes limitar el número total de usuarios que recibirán tu mensaje. Esto sirve como una comprobación independiente de los filtros de tu campaña.

![Resumen de la audiencia con una casilla seleccionada para limitar el número de personas que reciben la campaña.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

Al seleccionar el límite máximo de usuarios, puedes limitar el volumen de mensajes enviados por canal o de forma global para todos los tipos de mensajes.

{% alert note %}
El límite máximo de usuarios restringe el número de usuarios enviados, no el número de mensajes enviados correctamente. Dado que los mensajes abortados cuentan para este límite, el número real de mensajes enviados puede ser inferior al límite configurado. Por ejemplo, si estableces un límite de 10 000 y se abortan 2000 mensajes debido a la lógica de Liquid u otras condiciones, solo se enviarán 8000 mensajes.
{% endalert %}

##### Límite máximo de usuarios con optimizaciones

Si utilizas una optimización como Variante ganadora o Variante personalizada, la campaña constará de dos envíos: el experimento inicial y el envío final. 

Para establecer un límite máximo de usuarios en este escenario, selecciona **Limitar el número de personas que recibirán esta campaña**, luego selecciona **En total esta campaña debería** e introduce un límite de audiencia. El límite de tu audiencia se dividirá según los porcentajes mostrados en el panel de **pruebas A/B**. 

Si seleccionas **Cada vez que se programe la campaña**, esas dos fases se limitarán por separado al número establecido. Esto no suele ser deseable.

#### Establecer un límite máximo de impresiones en las campañas

En el caso de los mensajes dentro de la aplicación, puedes controlar la presión comercial estableciendo un número máximo de impresiones que se mostrarán a tu base de usuarios, tras lo cual Braze no enviará más mensajes a tus usuarios. Sin embargo, es importante señalar que este límite no es exacto. 

Las reglas de mensajes dentro de la aplicación se envían a una aplicación al inicio de la sesión, lo que significa que Braze puede enviar un mensaje al usuario antes de que se alcance el límite, pero en el momento en que el usuario desencadena el mensaje, ya se ha alcanzado el límite. En esta situación, el dispositivo seguirá mostrando el mensaje.

Por ejemplo, supongamos que tienes un juego con un mensaje dentro de la aplicación que se activa cuando un usuario supera un nivel, y lo limitas a 100 impresiones. Hasta ahora ha habido 99 impresiones. Alice y Bob abren el juego, y Braze les indica a sus dispositivos que son elegibles para recibir el mensaje cuando superen un nivel. Alice supera primero un nivel y recibe el mensaje. Bob supera el siguiente nivel, pero como su dispositivo no se ha comunicado con los servidores de Braze desde que comenzó la sesión, su dispositivo no sabe que el mensaje ha alcanzado su límite y también recibe el mensaje. Sin embargo, cuando se alcanza un límite de impresiones, la próxima vez que un dispositivo solicite la lista de mensajes elegibles dentro de la aplicación, el sistema no envía ese mensaje y lo elimina de ese dispositivo.

### Limitación de velocidad y pruebas A/B

Cuando se utiliza la limitación de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma manera que al grupo de prueba, lo que es una fuente potencial de sesgo temporal. Para evitar este sesgo, utiliza ventanas de conversión adecuadas.

### Limitación de la velocidad de entrega

Si prevés que las grandes campañas provocarán un aumento en la actividad de los usuarios y sobrecargarán tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no enviará más mensajes de los que establezcas en tu configuración de límite de velocidad por minuto.

Al dirigirte a los usuarios durante la creación de la campaña, puedes navegar a **Audiencia objetivo** (para campañas) o a **Configuración de envío** (para Canvas) para seleccionar un límite de velocidad (en varios incrementos, desde tan bajo como 10 hasta tan alto como 500 000 mensajes por minuto).

Ten en cuenta que las campañas no limitadas por velocidad pueden superar estos límites de entrega. Sin embargo, ten en cuenta que los mensajes se cancelarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. Si el límite de velocidad es demasiado bajo, el creador de la campaña recibirá alertas en el dashboard y por correo electrónico.

#### Ejemplo

Si intentas enviar 75 000 mensajes con un límite de velocidad de 10 000 mensajes por minuto, la entrega se distribuirá a lo largo de ocho minutos. Tu campaña no entregará más de 10 000 mensajes durante cada uno de los primeros siete minutos, y 5000 durante el último minuto.

#### Número de envíos

Ten en cuenta que los mensajes con límite de velocidad pueden no enviarse uniformemente a lo largo de cada minuto. Utilizando el ejemplo de un límite de velocidad de 10 000 por minuto, esto significa que Braze se asegura de que no se envían más de 10 000 mensajes por minuto. Esto podría significar que un mayor porcentaje de los 10 000 mensajes se envían en el primer medio minuto frente al último medio minuto.

El límite de velocidad se aplica al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad durante unos minutos. Con el tiempo, el número de envíos por minuto no superará de media el límite de velocidad.

{% alert important %}
Ten cuidado con retrasar los mensajes urgentes con esta forma de límite de velocidad en relación con el número total de usuarios de un segmento. Por ejemplo, si el segmento contiene 30 millones de usuarios, pero establecemos el límite de velocidad en 10 000 por minuto, una gran parte de tu base de usuarios no recibirá el mensaje hasta el día siguiente.
{% endalert %}

#### Campañas multicanal y Canvas

Al establecer un límite de velocidad de entrega para una campaña multicanal o Canvas, puedes elegir entre establecer un límite compartido o un límite basado en el canal.

Cuando una campaña multicanal o Canvas utiliza un límite de velocidad compartido, esto significa que el número total de mensajes enviados por minuto desde la campaña o Canvas no supera el límite de velocidad. Por ejemplo, si tu Canvas tiene un límite de velocidad de 500 000 por minuto y contiene pasos de correo electrónico y mensajes SMS, Braze envía un total de 500 000 mensajes por minuto entre correo electrónico y SMS.

![La opción de limitar la velocidad de envío de la campaña, seleccionada con 500 000 mensajes por minuto.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Cuando una campaña multicanal o Canvas utiliza la limitación de velocidad basada en canales, el límite de velocidad se aplicará a cada uno de los canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para enviar un máximo de 5000 webhooks y 2500 mensajes SMS por minuto en toda la campaña o Canvas.

![Límites de velocidad separados para dos canales, webhook y SMS/MMS/RCS, con 5000 y 2500 mensajes por minuto, respectivamente.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notificaciones push

Para campañas o Canvas con plataformas push (como Android, iOS, notificación push web o Kindle), puedes seleccionar **Notificaciones push** para aplicar un límite de velocidad que se comparta entre todas las plataformas push de tu campaña o Canvas.

![El menú desplegable del canal con opciones para plataformas push y notificaciones push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

Si seleccionas un límite para las notificaciones push, no podrás establecer límites de velocidad para cada canal push individualmente. Del mismo modo, si seleccionas límites para canales push individuales, no podrás establecer límites compartidos para las notificaciones push.

{% alert important %}
**Actualizaciones de la interfaz de límite de velocidad**<br>
Braze ha actualizado la interfaz de límite de velocidad para ofrecer más transparencia y control sobre cómo se aplican los límites de velocidad a las campañas multicanal y Canvas.<br><br>

- **Campañas y Canvas existentes:** Todas las campañas y Canvas existentes se han migrado a esta interfaz. Su comportamiento de entrega sigue siendo el mismo. El dashboard muestra si la campaña utiliza lógica compartida o por canal.<br>
- **Nuevas campañas y Canvas:** Para todas las campañas y Canvas nuevos, hay un interruptor manual para elegir la lógica del límite de velocidad que prefieras. Asegúrate de seleccionar el comportamiento de limitación de velocidad que se ajuste al comportamiento deseado al configurar o actualizar una campaña o un límite de velocidad de Canvas.
{% endalert %}

##### Consideraciones sobre el límite de velocidad

Algunas notas que debes tener en cuenta al configurar los límites de velocidad y qué comportamiento debes esperar:

- El envío de SMS está sujeto a un límite de velocidad de 50 000 mensajes por grupo de suscripción. Algunos proveedores de SMS pueden aplicar otros límites.
- Los siguientes mensajes no se verán afectados por el límite de velocidad ni se tendrán en cuenta para el mismo:
    - Envíos de prueba
    - Grupos semilla
    - Tarjetas de contenido configuradas para crear "a primera impresión" (esto se controlará mediante la tasa de impresiones de la aplicación). Consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) para obtener más información sobre las diferencias entre las opciones de creación de tarjetas.
- Los límites de velocidad de entrega no son compatibles con lo siguiente:
    - Respuestas automáticas por SMS
    - Mensajes respaldados por SLA (como [el correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - Mensajes dentro de la aplicación
    - Conmutadores de características
    - Banners

#### Limitación de velocidad y reintentos de contenido conectado

Cuando el [reintento de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) está activado, Braze volverá a intentar las llamadas fallidas respetando el límite de velocidad que hayas establecido para cada reenvío. Consideremos el caso de enviar 75 000 mensajes con un límite de velocidad de 10 000 mensajes por minuto. Imagina que, en el primer minuto, la llamada falla o es lenta y solo envía 4000 mensajes.

En lugar de intentar compensar el retraso y enviar los 6000 mensajes restantes en el segundo minuto o añadirlos a los 10 000 que ya están programados para enviarse, Braze moverá esos 6000 mensajes al "final de la cola" y añadirá un minuto, si es necesario, al total de minutos que tardaría en enviarse tu mensaje.

| Minuto | Sin fallos | 6000 fallos en el minuto 1 |
|--------|------------|---------------------------|
| 1      | 10,000     | 4,000                     |
| 2      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| 4      | 10,000     | 10,000                    |
| 5      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| 7      | 10,000     | 10,000                    |
| 8      | 5,000      | 10,000                    |
| 9      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Las solicitudes de contenido conectado no tienen un límite de velocidad independiente y seguirán el límite de velocidad de los webhooks. Esto significa que, si hay una llamada de contenido conectado a un punto de conexión único por cada webhook, se esperarían 5000 webhooks y también 5000 llamadas de contenido conectado por minuto. Ten en cuenta que el almacenamiento en caché puede afectar a esto y reducir el número de llamadas de contenido conectado. Además, los reintentos pueden aumentar las llamadas de contenido conectado, por lo que recomendamos comprobar que el punto de conexión de contenido conectado pueda manejar algunas fluctuaciones en este sentido.

{% alert note %}
**Los límites de velocidad son restricciones y no definen una velocidad de envío exacta.** Por lo general, los mensajes se distribuyen de manera uniforme a lo largo de cada minuto y, en la gran mayoría de los casos, se envían al ritmo del límite configurado o muy cerca de él. No siempre es así, por ejemplo, cuando los mensajes son muy grandes (como correos electrónicos con muchos bloques de contenido, etiquetas de contenido conectado o etiquetas de elementos de catálogo), o cuando hay muchos abortos de Liquid (los mensajes abortados siguen consumiendo una ranura y pueden reducir las tasas de envío efectivas).<br><br>
En la práctica, la tasa de envío sostenida (mensajes completados por minuto) puede ser inferior al límite de velocidad configurado debido a reintentos, variabilidad de la red, latencia del punto de conexión descendente y suavizado por minuto. Si observas constantemente un rendimiento significativamente inferior al esperado, comprueba los tiempos de respuesta del contenido conectado, las tasas de error (como `429`) y el comportamiento de reintento.
{% endalert %}

## Sobre la limitación de frecuencia

A medida que tu base de usuarios crece y tu mensajería se amplía para incluir campañas de ciclo de vida, desencadenadas, transaccionales y de conversión, es importante evitar que tus notificaciones parezcan correo no deseado o resulten molestas. Al proporcionar un mayor control sobre la experiencia de tus usuarios, la limitación de frecuencia te permite crear las campañas que deseas sin abrumar a tu audiencia.

### Resumen de características {#freq-cap-feat-over}

La limitación de frecuencia se aplica a nivel de campaña o de envío de componentes de Canvas y puede configurarse para cada espacio de trabajo desde **Configuración** > **Reglas de limitación de frecuencia**.

Por defecto, la limitación de frecuencia se activa cuando se crean nuevas campañas. Desde aquí, puedes elegir lo siguiente:

- El canal de mensajería que deseas limitar: push, correo electrónico, SMS, webhook, WhatsApp, LINE o cualquiera de esos canales.
- Cuántas veces cada usuario debe recibir una campaña o un componente de Canvas enviado desde un canal dentro de un determinado periodo de tiempo.
- Cuántas veces cada usuario debe recibir una campaña o un componente de Canvas enviado por [etiqueta](#frequency-capping-by-tag) en un determinado periodo de tiempo.

Este plazo puede medirse en minutos, días o semanas (siete días), con una duración máxima de 30 días.

Cada línea de limitación de frecuencia se conecta mediante el operador `AND`, y puedes añadir hasta 10 reglas por espacio de trabajo. Puedes incluir varios límites para los mismos tipos de mensajes. Por ejemplo, puedes limitar a los usuarios a no más de un push al día y no más de tres pushes a la semana. Ten en cuenta que los mensajes abortados no cuentan para la limitación de frecuencia.

![Sección de limitación de frecuencia con listas de campañas y Canvas a los que se aplicarán o no las reglas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Comportamiento cuando se aplica la limitación de frecuencia a los usuarios en un paso en Canvas

Si un usuario de Canvas tiene un límite de frecuencia debido a la configuración global de limitación de frecuencia, el usuario avanzará inmediatamente al siguiente paso en Canvas. El usuario no saldrá del Canvas debido a la limitación de frecuencia.

### Reglas de entrega

Puede haber algunas campañas, como los mensajes transaccionales, que desees que lleguen siempre al usuario, incluso si ya han alcanzado su límite de frecuencia. Por ejemplo, una aplicación de entrega puede querer enviar un correo electrónico o una notificación push cuando se entrega un artículo, independientemente del número de campañas que haya recibido el usuario.

Si deseas que una campaña en particular anule las reglas de limitación de frecuencia, puedes configurarlo en el dashboard de Braze al programar la entrega de esa campaña alternando la **Limitación de frecuencia** a **OFF**. 

A continuación, se te preguntará si deseas que esta campaña siga contando para tu límite de frecuencia. Los mensajes que cuentan para la limitación de frecuencia se incluyen en los cálculos del filtro de canal inteligente. 

Al enviar [campañas API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que suelen ser transaccionales, tendrás la posibilidad de especificar que una campaña ignore las reglas de limitación de frecuencia estableciendo `override_frequency_capping` en `true` en la solicitud API.

Por defecto, las nuevas campañas y Canvas que no respeten los límites de frecuencia tampoco contarán para ellos. Esto es configurable para cada campaña y Canvas.

{% alert note %}
Este comportamiento cambia el comportamiento por defecto cuando desactivas la limitación de frecuencia para una campaña o Canvas. Los cambios son compatibles con las versiones anteriores y no afectan a los mensajes que están actualmente activos.
{% endalert %}

![Sección de controles de entrega con la limitación de frecuencia activada.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Los diferentes canales de una campaña multicanal cuentan individualmente para la limitación de frecuencia. Por ejemplo, si creas una campaña multicanal con notificaciones push y correo electrónico y configuras una limitación de frecuencia para ambos canales, las notificaciones push se contabilizarán como una campaña de notificaciones push y los mensajes de correo electrónico se contabilizarán como una campaña de correo electrónico. La campaña también cuenta como una "campaña de cualquier tipo". Si los usuarios tienen un límite de una campaña push y una campaña de correo electrónico al día, y un usuario recibe esta campaña multicanal, ya no serán elegibles para recibir campañas push ni de correo electrónico durante el resto del día (a menos que la campaña ignore las reglas de limitación de frecuencia).

Los mensajes dentro de la aplicación y las tarjetas de contenido no se tienen en cuenta para los límites de las campañas o los componentes de Canvas de cualquier tipo.

{% alert important %}
La limitación global de frecuencia se programa en función de la zona horaria del usuario y se calcula por días naturales, no por periodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de envío de no más de una campaña al día, un usuario puede recibir un mensaje a las 11 de la noche en su zona horaria local, y sería elegible para recibir otro mensaje una hora más tarde.
{% endalert %}

#### Casos de uso

{% tabs %}
{% tab Caso de uso 1 %}

Supongamos que estableces una regla de limitación de frecuencia para que tus usuarios no reciban más de tres campañas de notificaciones push o pasos en Canvas por semana de todas las campañas o pasos en Canvas.

Si tu usuario está programado para recibir tres notificaciones push, dos mensajes dentro de la aplicación y una tarjeta de contenido esta semana, recibirá todos esos mensajes.

{% endtab %}
{% tab Caso de uso 2 %}

Este escenario utiliza una regla de limitación de frecuencia para que los usuarios no reciban más de dos campañas de notificaciones push o pasos en Canvas por semana de todas las campañas o pasos en Canvas.

**Cuando se da la siguiente situación:**

- Un usuario desencadena la misma campaña `Campaign ABC` tres veces a lo largo de una semana.
- Este usuario desencadena `Campaign ABC` una vez el lunes, una vez el miércoles y una vez el jueves.

![Sección de limitación de frecuencia con la regla de no enviar más de 2 campañas de notificaciones push/pasos en Canvas de todas las campañas/pasos en Canvas a un usuario cada semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Entonces, el comportamiento esperado es que:**

- Este usuario recibirá los envíos de campaña que se desencadenaron el lunes y el miércoles.
- Este usuario no recibirá el tercer envío de campaña el jueves porque ya ha recibido dos envíos de campaña push esa semana.

{% endtab %}
{% endtabs %}

### Limitación de frecuencia por etiqueta

[Las reglas de limitación de frecuencia](#delivery-rules) pueden aplicarse a los espacios de trabajo utilizando etiquetas específicas que hayas aplicado a tus campañas y Canvas, lo que te permite básicamente basar tu limitación de frecuencia en grupos con nombres personalizados.

Con la limitación de frecuencia por etiqueta, se pueden establecer reglas en las etiquetas principales y anidadas, de modo que Braze tendrá en cuenta todas las etiquetas. Por ejemplo, si has seleccionado utilizar la etiqueta principal A como límite de frecuencia, también incluiremos información de todas las etiquetas anidadas (por ejemplo, las etiquetas B y C) a la hora de determinar el límite.

También puedes combinar la limitación de frecuencia normal con la limitación de frecuencia por etiquetas. Considera las siguientes reglas:

1. No más de tres campañas de notificaciones push o componentes de Canvas por semana de todas las campañas y pasos en Canvas. <br>**Y**
2. No más de dos campañas de notificaciones push o componentes de Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con dos reglas que limitan cuántas campañas de notificaciones push/Canvas se pueden enviar a un usuario cada semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, tus usuarios no recibirán más de tres envíos de campaña por semana en todas las campañas y pasos en Canvas y no más de dos campañas de notificaciones push o componentes de Canvas con la etiqueta `promotional`.

{% alert important %}
Los Canvas se etiquetan a nivel de Canvas, en lugar de por componente. Por lo tanto, cada componente de Canvas heredará todas las etiquetas de nivel de Canvas.
{% endalert %}

#### Reglas contradictorias

Cuando las reglas entran en conflicto, se aplica a tus usuarios la regla de limitación de frecuencia más restrictiva y aplicable. Por ejemplo, supongamos que tienes las siguientes reglas:

1. No más de una campaña de notificaciones push o componente de Canvas por semana de todas las campañas y componentes de Canvas. <br>**Y**
2. No más de tres campañas de notificaciones push o componentes de Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con reglas contradictorias para limitar cuántas campañas de notificaciones push/pasos en Canvas se envían a un usuario cada semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

En este ejemplo, tu usuario no recibirá más de una campaña de notificaciones push o componentes de Canvas con la etiqueta "promotional" en una semana determinada, porque has especificado que los usuarios no deben recibir más de una campaña de notificaciones push o componente de Canvas de todas las campañas y componentes de Canvas. En otras palabras, la regla de frecuencia aplicable más restrictiva es la que se aplicará a un usuario determinado.

#### Recuento de etiquetas

La limitación de frecuencia por reglas de etiquetas se calcula en el momento en que se envía un mensaje. Esto significa que la limitación de frecuencia por etiqueta solo cuenta las etiquetas que están actualmente en las campañas o Canvas que un usuario recibió en el pasado. No cuenta las etiquetas que estaban en las campañas o Canvas durante el tiempo en que se enviaron, pero que desde entonces han sido eliminadas. Se tiene en cuenta si posteriormente se añade una etiqueta a un mensaje que un usuario recibió en el pasado, pero antes de que se envíe el mensaje etiquetado más reciente.

##### Caso de uso

Considera las siguientes campañas y la limitación de frecuencia por regla de etiqueta:

**Campañas**:

- **La campaña A** es una campaña push etiquetada como `promotional`. Está previsto que se envíe a las 9 de la mañana del lunes.
- **La campaña B** es una campaña push etiquetada como `promotional`. Está previsto que se envíe a las 9 de la mañana del miércoles.

**Limitación de frecuencia por regla de etiqueta:**

- Tu usuario no debe recibir más de una campaña de notificaciones push por semana con la etiqueta `promotional`.<br><br>

| Acción | Resultado |
|---|---|
| La etiqueta `promotional` se elimina de **la campaña A** después de que tu usuario haya recibido el mensaje, pero antes de que **se haya enviado la campaña B.** | Tu usuario recibe **la campaña B**.|
| La etiqueta `promotional` se ha eliminado por error de **la campaña A** después de que tu usuario recibiera el mensaje. <br> La etiqueta se vuelve a añadir a **la campaña A** el martes, antes de que se envíe **la campaña B**. | Tu usuario no recibe **la campaña B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envío a gran escala {#sending-at-large-scales}

Es posible que la limitación de frecuencia mediante reglas de etiquetas no se aplique correctamente a grandes escalas, como 100 mensajes por canal de campañas o componentes de Canvas.

Por ejemplo, si tu regla de limitación de frecuencia por etiqueta es:

> No más de dos campañas de correo electrónico o componentes de Canvas con la etiqueta `Promotional` a un usuario cada semana.

Y envías al usuario más de 100 correos electrónicos de campañas y pasos en Canvas con la limitación de frecuencia activada en el transcurso de una semana, es posible que se envíen más de dos correos electrónicos al usuario.

Dado que 100 mensajes por canal son más mensajes de los que la mayoría de las marcas envían a sus usuarios, es poco probable que te veas afectado por esta limitación. Para evitarla, puedes establecer un límite para el número máximo de correos electrónicos que deseas que tus usuarios reciban en el transcurso de una semana.

Por ejemplo, puedes establecer la siguiente regla:

> No más de tres campañas de correo electrónico o componentes de Canvas por semana de todas las campañas y pasos en Canvas.

Esta regla determina que ningún usuario reciba más de 100 correos electrónicos por semana, ya que, como máximo, los usuarios reciben tres correos electrónicos por semana de campañas o componentes de Canvas con la limitación de frecuencia activada.

## Preguntas frecuentes

### Si cambio un límite de envío en un Canvas activo, ¿afecta esto a los usuarios que ya están en el Canvas?

Sí, cuando aumentas o reduces un límite de velocidad de Canvas, el límite actualizado entrará en vigor para los nuevos mensajes en aproximadamente 30 segundos tras el cambio debido al almacenamiento en caché.

### ¿La limitación de frecuencia hace que los usuarios salgan de Canvas?

No. Si un usuario de Canvas tiene un límite de frecuencia debido a la configuración global de limitación de frecuencia, pasará inmediatamente al siguiente paso en Canvas. El usuario **no** saldrá del Canvas debido a la limitación de frecuencia.

### ¿Cómo puedo identificar a los usuarios a los que se les ha aplicado una limitación de frecuencia en Canvas?

Los usuarios con limitación de frecuencia no generan un evento de envío para ese paso. Para identificar a estos usuarios, puedes utilizar [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) para realizar el seguimiento de los eventos con limitación de frecuencia de mensajes. Como alternativa, puedes crear una [extensión de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) para analizar a los usuarios que ingresaron al Canvas pero no recibieron el mensaje esperado.