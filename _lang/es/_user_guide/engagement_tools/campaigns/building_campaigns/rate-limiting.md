---
nav_title: Limitación de velocidad y frecuencia
article_title: Limitación de velocidad y frecuencia
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artículo de referencia analiza el concepto de limitación de velocidad y frecuencia en las campañas, y cómo puede gestionar la presión del marketing para mejorar la experiencia del usuario."

---

# Limitación de velocidad y limitación de frecuencia

> La limitación de velocidad y la limitación de frecuencia pueden utilizarse conjuntamente para asegurarse de que sus usuarios reciben los mensajes que necesitan y ninguno de los que no.

## Sobre el límite de velocidad

Braze le permite controlar la presión del marketing limitando la tasa de sus campañas, regulando la cantidad de tráfico saliente de su plataforma. Puedes implementar dos tipos diferentes de límite de velocidad para tus campañas: 

1. [**Limitación de velocidad centrada en el usuario:**](#user-centric-rate-limiting) Se centra en proporcionar la mejor experiencia al usuario.
2. [**Limitación de la tasa de velocidad de entrega:**](#delivery-speed-rate-limiting) Tiene en cuenta el ancho de banda de tus servidores.

Braze intentará distribuir uniformemente los envíos de mensajes a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una campaña con un límite de velocidad de 5.000 mensajes por minuto, intentaremos distribuir las 5.000 solicitudes uniformemente a lo largo del minuto (unos 84 mensajes por segundo), pero puede haber alguna variación en la tasa por segundo.

### Limitación de tarifas centrada en el usuario

A medida que cree más segmentos, habrá casos en los que los miembros de esos segmentos se solapen. Si envías campañas a esos segmentos, debes asegurarte de no enviar mensajes a tus usuarios con demasiada frecuencia. Si un usuario recibe demasiados mensajes en poco tiempo, se sentirá agobiado y desactivará las notificaciones push o desinstalará la aplicación.

#### Filtros de segmentos relevantes

Braze proporciona los siguientes filtros para ayudarle a limitar la velocidad a la que sus usuarios reciben mensajes:

- Última interacción con un mensaje
- Último mensaje recibido
- Última campaña push recibida
- Última campaña de correo electrónico recibida
- Último SMS recibido

#### Aplicación de filtros

Supongamos que hemos creado un segmento denominado "Escaparate de filtros de reorientación" con un filtro "La última vez que utilizó estas aplicaciones fue hace más de 7 días" para dirigirnos a los usuarios. Sería un segmento estándar de reactivación de la interacción.

Si tiene otros segmentos más específicos que reciben notificaciones recientemente, es posible que no desee que sus usuarios reciban campañas más genéricas dirigidas a este segmento. Aplicando el filtro "Última campaña push recibida" a este segmento, el usuario se ha asegurado de que si ha recibido otra notificación en las últimas 24 horas, se deslizará fuera de este segmento durante las próximas 24 horas. Si siguen cumpliendo los demás criterios del segmento 24 horas después y no han recibido más notificaciones, volverán a entrar en el segmento.

![Sección Detalles del segmento con el filtro del segmento "Último mensaje recibido" resaltado.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Si se aplica este filtro a todos los segmentos a los que se dirigen las campañas, los usuarios recibirán como máximo una notificación cada 24 horas. Así podrá priorizar sus mensajes, asegurándose de que los más importantes se envían antes que los menos importantes.

#### Establecer un límite máximo de usuarios

En el paso **Audiencias objetivo** del compositor de tu campaña, también puedes limitar el número total de usuarios que recibirán tu mensaje. Esto sirve como control independiente de los filtros de tu campaña, permitiéndote segmentar libremente a los usuarios sin preocuparte por el exceso de spam.

![Resumen de audiencia con una casilla seleccionada para limitar el número de personas que reciben la campaña.]({% image_buster /assets/img_archive/total_limit.png %})

Al seleccionar el límite máximo de usuarios, puede limitar la velocidad a la que sus usuarios reciben notificaciones por canal o globalmente en todos los tipos de mensajes.

##### Máxima capacidad de usuarios con optimizaciones

Si utilizas una optimización como Variante ganadora o Variante personalizada, la campaña constará de dos envíos: el experimento inicial y el envío final. 

Para establecer un límite máximo de usuarios en este escenario, seleccione **Limitar el número de personas que recibirán esta campaña**, luego seleccione **En total esta campaña debería**, e introduzca un límite de audiencia. El límite de tu audiencia se dividirá según los porcentajes mostrados en el panel de **Pruebas A/B**. 

Si selecciona **Cada vez que se programe la campaña**, esas dos fases se limitarán por separado al número establecido. Esto no suele ser deseable.

#### Fijar un tope máximo de impresiones

Para los mensajes dentro de la aplicación y las Tarjetas de contenido, puede controlar la presión de marketing estableciendo un número máximo de impresiones que se mostrarán a su base de usuarios, después del cual Braze no enviará más mensajes a sus usuarios. Sin embargo, es importante señalar que este tope no es exacto. 

Las nuevas tarjetas de contenido y las reglas de mensajes dentro de la aplicación se envían a una aplicación al inicio de la sesión, lo que significa que Braze puede enviar un mensaje al usuario antes de que se alcance el límite, pero cuando el usuario activa el mensaje, ya se ha alcanzado el límite. En esta situación, el dispositivo seguirá mostrando el mensaje.

Por ejemplo, supongamos que tiene un juego con un mensaje dentro de la aplicación que se activa cuando un usuario supera un nivel, y lo limita a 100 impresiones. Hasta ahora ha habido 99 impresiones. Alice y Bob abren el juego y Braze indica a sus dispositivos que pueden recibir el mensaje cuando superan un nivel. Alice supera primero un nivel y recibe el mensaje. Bob supera el nivel a continuación, pero como su dispositivo no se ha comunicado con los servidores Braze desde que comenzó su sesión, su dispositivo no es consciente de que el mensaje ha alcanzado su tope y él también recibirá el mensaje. Sin embargo, cuando se ha alcanzado un tope de impresiones, la próxima vez que cualquier dispositivo solicite la lista de mensajes in-app elegibles, ese mensaje no se enviará hacia abajo y se eliminará de ese dispositivo.

### Limitación de tarifas y pruebas A/B

Cuando se utiliza la limitación de la tasa con una prueba A/B, el límite de la tasa no se aplica al grupo de control de la misma manera que al grupo de prueba, lo que es una fuente potencial de sesgo temporal. Para evitar este sesgo, utiliza ventanas de conversión adecuadas.

### Limitación de la tasa de velocidad de entrega

Si prevés que las grandes campañas provoquen un aumento de la actividad de los usuarios y sobrecarguen tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no enviará más de lo que hayas configurado como límite de velocidad en un minuto.

Al dirigirte a los usuarios durante la creación de la campaña, puedes navegar a **Audiencias objetivo** (para campañas) o a **Configuración de envío** (para Canvas) para seleccionar un límite de velocidad (en varios incrementos, desde tan bajo como 10 hasta tan alto como 500.000 mensajes por minuto).

Tenga en cuenta que las campañas no limitadas por tarifa pueden superar estos límites de entrega. Sin embargo, ten en cuenta que los mensajes se cancelarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. Si el límite de velocidad es demasiado bajo, el creador de la campaña recibirá alertas en el panel y por correo electrónico.

![Resumen de audiencia con una casilla seleccionada para limitar la tasa a la que finalizará la campaña, y una tasa de 500.000 por minuto.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

Otro ejemplo: si intentas enviar 75.000 mensajes con un límite de tasa de 10.000 por minuto, la entrega se repartirá en 8 minutos. Tu campaña no entregará más de 10.000 mensajes durante cada uno de los primeros siete minutos, y 5.000 durante el último minuto.

Ten en cuenta que los mensajes con tasa limitada pueden no enviarse uniformemente a lo largo de cada minuto. Utilizando el ejemplo de un límite de tasa de 10.000 por minuto, esto significa que Braze se asegura de que no se envían más de 10.000 mensajes por minuto. Esto podría significar que un mayor porcentaje de los 10.000 mensajes se envían en el primer medio minuto frente al último medio minuto. 

Además, ten en cuenta que el límite de velocidad se aplica al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad en algunos minutos. Con el tiempo, el número de envíos por minuto no superará el límite de velocidad.

{% alert important %}
Ten cuidado con retrasar los mensajes sensibles al tiempo con esta forma de limitar la tasa en relación con el número total de usuarios de un segmento. Por ejemplo, si el segmento contiene 30 millones de usuarios, pero fijamos el límite de velocidad en 10.000 por minuto, una gran parte de tu base de usuarios no recibirá el mensaje hasta el día siguiente.
{% endalert %}

#### Campañas monocanal

Al enviar una campaña monocanal con un límite de velocidad, el límite de velocidad se aplica a todos los mensajes juntos.

#### Campañas multicanal

Al enviar una campaña multicanal con un límite de velocidad, cada canal se envía independientemente de los demás. Como consecuencia, puede ocurrir lo siguiente

- El número total de mensajes enviados por minuto podría ser superior al límite de velocidad. 
    - Por ejemplo, si tu campaña tiene un límite de velocidad de 10.000 por minuto y utiliza correo electrónico y SMS, Braze puede enviar un máximo de 20.000 mensajes en total cada minuto (10.000 por correo electrónico y 10.000 por SMS).
- Los usuarios podrían recibir los distintos canales en momentos diferentes, y no es predecible qué canal recibirán primero. 
    - Por ejemplo, si envías una campaña que contiene un correo electrónico y un SMS, puedes tener 10.000 usuarios con números de teléfono válidos y 50.000 usuarios con direcciones de correo electrónico válidas. Si configuras la campaña para enviar 100 mensajes por minuto (un límite de tasa lento para el tamaño de la campaña), un usuario podría recibir el SMS en el primer lote de envíos y el correo electrónico en el último lote de envíos, casi nueve horas después.

#### Campañas push multiplataforma

Para las campañas push que se entregan en varias plataformas, el límite de velocidad seleccionado se distribuirá equitativamente entre las plataformas. Una campaña push en Android e iOS con un límite de 10.000 mensajes por minuto distribuirá por igual los 10.000 mensajes entre las dos plataformas.

#### Limitación de la tasa de velocidad de entrega de Canvas {#canvas-delivery-speed}

Al enviar un Canvas con un límite de velocidad, el límite de tasa se comparte entre canales. Esto significa que el número total de mensajes enviados por minuto desde el Canvas no superará el límite de velocidad. Por ejemplo, si tu Canvas tiene un límite de velocidad de 10.000 por minuto y utiliza correo electrónico y SMS, Braze enviará un total de 10.000 mensajes por minuto por correo electrónico y SMS.

#### Limitación de velocidad y reintentos de contenido conectado

Cuando el [reintento de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) está activado, Braze reintentará los fallos de llamada respetando el límite de velocidad que establezcas para cada reenvío. Consideremos el caso de enviar 75.000 mensajes con un límite de velocidad de 10.000 por minuto. Imagina que en el primer minuto, la llamada falla o es lenta y sólo envía 4.000 mensajes.

En lugar de intentar compensar el retraso y enviar los 6.000 mensajes restantes en el segundo minuto o añadirlos a los 10.000 que ya están configurados para enviar, Braze moverá esos 6.000 mensajes al "final de la cola" y añadirá un minuto, si es necesario, al total de minutos que tardaría en enviar tu mensaje.

| Minuto | Ningún fallo | 6.000 Fallos en el minuto 1 |
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

Las solicitudes de contenido conectado no están limitadas por la tasa de forma independiente y seguirán el límite de velocidad del webhook. Esto significa que si hay una llamada de Contenido conectado a un punto final único por webhook, esperarías 5.000 webhooks y también 5.000 llamadas de Contenido conectado por minuto. Ten en cuenta que el almacenamiento en caché puede afectar a esto y reducir el número de llamadas a Contenido conectado. Además, los reintentos pueden aumentar las llamadas de Contenido Conectado, por lo que recomendamos comprobar que el punto final de Contenido Conectado puede soportar cierta fluctuación aquí.

## Sobre la limitación de frecuencia

A medida que su base de usuarios crece y su mensajería se amplía para incluir campañas de ciclo de vida, activadas, transaccionales y de conversión, es importante evitar que sus notificaciones parezcan "spam" o molestas. Al proporcionar un mayor control sobre la experiencia de sus usuarios, la limitación de la frecuencia le permite crear las campañas que desea sin abrumar a su audiencia.

### Resumen de características {#freq-cap-feat-over}

La limitación de frecuencia se aplica a nivel de campaña o de envío de componentes de Canvas y puede configurarse para cada área de trabajo desde **Configuración** > **Reglas de limitación de frecuencia**.

Por defecto, el límite de frecuencia se activa cuando se crean nuevas campañas. Desde aquí, puedes elegir lo siguiente:

- Qué canal de mensajería te gustaría limitar: push, correo electrónico, SMS, webhook, WhatsApp o cualquiera de esos cinco.
- Cuántas veces debe recibir cada usuario los envíos de una campaña o componente Canvas desde un canal en un periodo de tiempo determinado.
- Cuántas veces debe recibir cada usuario una campaña o componente Canvas enviado por [etiqueta](#frequency-capping-by-tag) dentro de un plazo determinado.

Este plazo puede medirse en minutos, días o semanas (siete días), con una duración máxima de 30 días.

Cada línea de tapas de frecuencia se conectará utilizando el operador `AND`, y puede añadir hasta 10 reglas por espacio de trabajo. Además, puedes incluir varios límites para los mismos tipos de mensajes. Por ejemplo, puedes limitar a los usuarios a no más de un push al día y no más de tres push a la semana.

![Sección de limitación de frecuencia con listas de campañas y Lienzos a los que se aplicarán las reglas y a los que no.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportamiento cuando los usuarios tienen limitación de frecuencia en un paso en Canvas

Si un usuario de Canvas tiene limitación de frecuencia debido a la configuración global de limitación de frecuencia, el usuario avanzará inmediatamente al siguiente paso en Canvas. El usuario no saldrá del Canvas debido al límite de frecuencia.

### Normas de entrega

Puede haber algunas campañas, como los mensajes transaccionales, que desee que lleguen siempre al usuario, incluso si ya han alcanzado su límite de frecuencia. Por ejemplo, una aplicación de entrega puede querer enviar un correo electrónico o un push cuando se entrega un artículo, independientemente de cuántas campañas haya recibido el usuario.

Si desea que una campaña en particular anule las reglas de limitación de frecuencia, puede configurarlo en el panel de control de Braze al programar la entrega de esa campaña configurarlo la **limitación de frecuencia** en **OFF**. 

A continuación, se le preguntará si desea que esta campaña siga contando para su límite de frecuencia. Los mensajes que cuentan para la limitación de frecuencias se incluyen en los cálculos del filtro Canal Inteligente. Cuando envíes [campañas API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que suelen ser transaccionales, tendrás la posibilidad de especificar que una campaña ignore las normas de limitación de frecuencia [dentro de la solicitud API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) configurando `override_messaging_limits` en `true`.

Por defecto, las nuevas campañas y los lienzos que no respeten los límites de frecuencia tampoco contarán. Esto es configurable para cada campaña y Canvas.

{% alert note %}
Este comportamiento cambia el comportamiento por defecto cuando se desactiva la limitación de frecuencia para una campaña o Canvas. Los cambios son compatibles con las versiones anteriores y no afectan a los mensajes que están actualmente activos.
{% endalert %}

![Sección de controles de entrega con la limitación de frecuencia activada.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Los distintos canales de una campaña multicanal contabilizarán individualmente el límite de frecuencia. Por ejemplo, si crea una campaña multicanal con push y correo electrónico y ha configurado un límite de frecuencia para ambos canales, el push contará para una campaña push y el mensaje de correo electrónico contará para una campaña de mensaje de correo electrónico. La campaña también contará como una "campaña de cualquier tipo". Si los usuarios están limitados a una campaña push y una campaña de correo electrónico al día y un usuario recibe esta campaña multicanal, ya no podrá recibir campañas push o de correo electrónico durante el resto del día (a menos que una campaña ignore las reglas de limitación de frecuencia).

Los mensajes dentro de la aplicación y las tarjetas de contenido no se tienen en cuenta para los límites de las campañas o los componentes de Canvas de cualquier tipo.

{% alert important %}
La limitación global de frecuencias se programa en función de la zona horaria del usuario y se calcula por días naturales, no por periodos de 24 horas. Por ejemplo, si establece una regla de limitación de frecuencia de envío de no más de una campaña al día, un usuario puede recibir un mensaje a las 11 de la noche en su zona horaria local y podría recibir otro mensaje una hora más tarde.
{% endalert %}

#### Ejemplos

{% tabs %}
{% tab Caso de uso 1 %}

Supongamos que establece una regla de limitación de frecuencia que pide que su usuario no reciba más de tres campañas de notificaciones push o componentes de Canvas por semana de todas las campañas o componentes de Canvas.

Si su usuario está programado para recibir tres notificaciones push, dos mensajes in-app y una Content Card esta semana, recibirá todos esos mensajes.

{% endtab %}
{% tab Caso de uso 2 %}

Este escenario utiliza las siguientes reglas de limitación de frecuencia:

**Cuando se produce el siguiente escenario:**

- Un usuario activa la misma campaña, `Campaign ABC` tres veces en el transcurso de una semana.
- Este usuario activa `Campaign ABC` una vez el lunes, una vez el miércoles y una vez el jueves.

![Sección de limitación de frecuencia con la regla de no enviar más de 2 campañas de notificación push/Pasos en Canvas de todas las campañas/Pasos en Canvas a un usuario cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Entonces, el comportamiento esperado es ese:**

- Este usuario recibirá los envíos de campaña que se activaron el lunes y el miércoles.
- Este usuario no recibirá el tercer envío de campaña el jueves porque ya ha recibido dos envíos de campaña push esa semana.

{% endtab %}
{% endtabs %}

### Limitación de frecuencia por etiqueta

[Las reglas de limitación de frecuencia](#delivery-rules) pueden aplicarse a los espacios de trabajo utilizando etiquetas específicas que haya aplicado a sus campañas y lienzos, lo que le permite básicamente basar su limitación de frecuencia en grupos con nombres personalizados.

Con la limitación de frecuencia por etiqueta, se pueden establecer reglas en las etiquetas principales y anidadas, de modo que Braze tendrá en cuenta todas las etiquetas. Por ejemplo, si ha seleccionado utilizar la etiqueta principal A para el límite de frecuencia, también incluiremos la información de todas las etiquetas anidadas (por ejemplo, las etiquetas B y C) a la hora de determinar el límite.

También puede combinar la limitación de frecuencia normal con la limitación de frecuencia por etiquetas. Considera las siguientes reglas:

1. No más de tres campañas de notificaciones push o componentes Canvas por semana de todos los pasos de campaña y Canvas. <br>**Y**
2. No más de dos componentes de campaña de notificaciones push o Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con dos reglas que limitan cuántas campañas de notificación push/Canvases se pueden enviar a un usuario cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, sus usuarios no recibirán más de tres envíos de campaña por semana en todas las campañas y pasos de Canvas y no más de dos campañas de notificaciones push o componentes de Canvas con la etiqueta `promotional`.

{% alert important %}
Los lienzos se etiquetan a nivel de lienzo, en lugar de por componente. Así, cada componente Canvas heredará todas las etiquetas de nivel Canvas.
{% endalert %}

#### Normas contradictorias

Cuando las reglas entren en conflicto, se aplicará a sus usuarios la regla de limitación de frecuencia aplicable más restrictiva. Por ejemplo, supongamos que tiene las siguientes normas:

1. No más de una campaña de notificación push o componente Canvas por semana de todos los componentes de campaña y Canvas. <br>**Y**
2. No más de tres campañas de notificaciones push o componentes Canvas por semana con la etiqueta `promotional`.

![Sección de limitación de frecuencia con reglas conflictivas para limitar cuántas campañas de notificación push/pasos en Canvas se envían a un usuario cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "reglas globales")

En este ejemplo, su usuario no recibirá más de una campaña de notificación push o componentes de Canvas con la etiqueta "promocional" en una semana determinada, porque ha especificado que los usuarios no deben recibir más de una campaña de notificación push o componente de Canvas de todas las campañas y componentes de Canvas. En otras palabras, la norma de frecuencia aplicable más restrictiva es la que se aplicará a un usuario determinado.

#### Recuento de etiquetas

La limitación de frecuencia por reglas de etiquetas se computa en el momento en que se envía un mensaje. Esto significa que la limitación de frecuencia por etiqueta sólo cuenta las etiquetas que están actualmente en las campañas o los lienzos que un usuario recibió en el pasado. No se tienen en cuenta las etiquetas que estaban en las campañas o los lienzos durante el tiempo en que se enviaron pero que se han eliminado desde entonces. Contará si más tarde se añade una etiqueta a un mensaje que un usuario recibió en el pasado, pero antes de que se envíe el mensaje etiquetado más reciente.

##### Caso de uso

Considere las siguientes campañas y la limitación de frecuencia por regla de etiqueta:

**Campañas**:

- **La campaña A** es una campaña push etiquetada como `promotional`. Está previsto que se envíe el lunes a las 9 de la mañana.
- **La campaña B** es una campaña push etiquetada como `promotional`. Está previsto que se envíe a las 9 de la mañana del miércoles.

**Limitación de frecuencia por regla de etiqueta:**

- Su usuario no debe recibir más de una campaña de notificaciones push por semana con la etiqueta `promotional`.<br><br>

| Acción | Resultado |
|---|---|
| La etiqueta `promotional` se elimina de **la Campaña A** después de que su usuario haya recibido el mensaje, pero antes de **que se haya enviado la Campaña B.** | Su usuario recibirá **la Campaña B**.|
| La etiqueta `promotional` se ha eliminado por error de **la campaña A** después de que su usuario recibiera el mensaje. <br> La etiqueta se vuelve a añadir a **la campaña A** el martes, antes de que se envíe **la campaña B**. | Tu usuario no recibirá **la Campaña B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envío a gran escala {#sending-at-large-scales}

Es posible que la limitación de frecuencia mediante reglas de etiquetas no se aplique correctamente a grandes escalas, como 100 mensajes por canal de campañas o componentes de Canvas.

Por ejemplo, si su regla de limitación de frecuencia por etiqueta es:

> No más de dos campañas de correo electrónico o componentes de Canvas con la etiqueta `Promotional` a un usuario cada semana.

Y envías al usuario más de 100 correos electrónicos de campañas y pasos de Canvas con el límite de frecuencia activado en el transcurso de una semana, es posible que se envíen más de dos correos electrónicos al usuario.

Dado que 100 mensajes por canal son más mensajes de los que la mayoría de las marcas envían a sus usuarios, es poco probable que te veas afectado por esta limitación. Para evitar esta limitación, puede establecer un límite para el número máximo de correos electrónicos que desea que sus usuarios reciban en el transcurso de una semana.

Por ejemplo, puede establecer la siguiente regla:

> No más de tres campañas de correo electrónico o componentes de Canvas por semana de todos los pasos de campaña y Canvas.

Esta regla garantizará que ningún usuario reciba más de 100 correos electrónicos por semana, ya que, como máximo, los usuarios recibirán tres correos electrónicos por semana de campañas o componentes de Canvas con la limitación de frecuencia activada.

