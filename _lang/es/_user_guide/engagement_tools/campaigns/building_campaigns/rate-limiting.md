---
nav_title: Limitación de velocidad y limitación de frecuencia
article_title: Limitación de tasa y limitación de frecuencia
page_order: 6
tool: Campaigns
page_type: reference
description: "Este artículo de referencia analiza el concepto de limitación de tasa y limitación de frecuencia en las campañas, y cómo puedes gestionar la presión del marketing para mejorar la experiencia del usuario."

---

# Limitación de velocidad y limitación de frecuencia

> La limitación de tasa y la limitación de frecuencia pueden utilizarse conjuntamente para asegurarte de que tus usuarios reciben los mensajes que necesitan y ninguno de los que no.

## Sobre el límite de velocidad

Braze te permite controlar la presión del marketing limitando la tasa de tus campañas, regulando la cantidad de tráfico saliente de tu plataforma. Puedes implementar dos tipos diferentes de límite de velocidad para tus campañas: 

1. [**Limitación de velocidad centrada en el usuario:**](#user-centric-rate-limiting) Se centra en proporcionar la mejor experiencia al usuario.
2. [**Limitación de la tasa de velocidad de entrega:**](#delivery-speed-rate-limiting) Tiene en cuenta el ancho de banda de tus servidores.

Braze intentará distribuir uniformemente los envíos de mensajes a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una campaña con un límite de velocidad de 5.000 mensajes por minuto, intentaremos distribuir las 5.000 solicitudes uniformemente a lo largo del minuto (unos 84 mensajes por segundo), pero puede haber alguna variación en la tasa por segundo.

### Limitación de velocidad centrada en el usuario

A medida que crees más segmentos, habrá casos en los que los miembros de esos segmentos se solapen. Si envías campañas a esos segmentos, debes asegurarte de que no estás enviando mensajes a tus usuarios con demasiada frecuencia. Si un usuario recibe demasiados mensajes en poco tiempo, se sentirá agobiado y desactivará las notificaciones push o desinstalará tu aplicación.

#### Filtros de segmentos relevantes

Braze proporciona los siguientes filtros para ayudarte a limitar la tasa a la que tus usuarios reciben mensajes:

- Última interacción con un mensaje
- Último mensaje recibido
- Última campaña push recibida
- Última campaña de correo electrónico recibida
- Último SMS recibido

#### Aplicar filtros

Digamos que hemos creado un segmento llamado "Escaparate de filtrado de reorientación" con un filtro "La última vez que usé estas aplicaciones fue hace más de 7 días" para orientar a los usuarios. Sería un segmento estándar de reactivación de la interacción.

Si tienes otros segmentos más específicos que han recibido notificaciones recientemente, puede que no quieras que tus usuarios reciban campañas más genéricas dirigidas a este segmento. Aplicando el filtro "Última campaña push recibida" a este segmento, el usuario se ha asegurado de que si ha recibido otra notificación en las últimas 24 horas, se deslizará fuera de este segmento durante las próximas 24 horas. Si 24 horas después siguen cumpliendo los demás criterios del segmento y no han recibido más notificaciones, volverán al segmento.

\![Sección Detalles del segmento con el filtro del segmento "Último mensaje recibido" resaltado.]({% image_buster /assets/img_archive/rate_limit_daily.png %})

Si aplicas este filtro a todos los segmentos a los que se dirigen las campañas, tus usuarios recibirán como máximo un push cada 24 horas. Así podrías priorizar tu mensajería asegurándote de que tus mensajes más importantes se entregan antes que los mensajes menos importantes.

#### Configuración de un límite máximo de usuarios

En el paso **Audiencias objetivo** del compositor de tu campaña, también puedes limitar el número total de usuarios que recibirán tu mensaje. Esto sirve como control independiente de los filtros de tu campaña, permitiéndote segmentar libremente a los usuarios sin preocuparte por el exceso de spam.

Resumen de audiencia con una casilla de verificación seleccionada para limitar el número de personas que reciben la campaña.]({% image_buster /assets/img_archive/total_limit.png %})

Seleccionando el límite máximo de usuarios, puedes limitar la tasa a la que tus usuarios reciben notificaciones por canal o globalmente en todos los tipos de mensajes.

##### Máxima capacidad de usuarios con optimizaciones

Si utilizas una optimización como Variante ganadora o Variante personalizada, la campaña constará de dos envíos: el experimento inicial y el envío final. 

Para configurar un límite máximo de usuarios en este escenario, selecciona **Limitar el número de personas que recibirán esta campaña**, luego selecciona **En total esta campaña debería**, e introduce un límite de audiencia. El límite de tu audiencia se dividirá según los porcentajes mostrados en el panel de **Pruebas A/B**. 

Si seleccionas **Cada vez que se programe la campaña**, esas dos fases se limitarán por separado al número establecido. Esto no suele ser deseable.

#### Establecer un tope máximo de impresiones

Para los mensajes dentro de la aplicación y las tarjetas de contenido, puedes controlar la presión del marketing estableciendo un número máximo de impresiones que se mostrarán a tu base de usuarios, después del cual Braze no enviará más mensajes a tus usuarios. Sin embargo, es importante notar que este tope no es exacto. 

Las nuevas tarjetas de contenido y reglas de mensajería dentro de la aplicación se envían a una aplicación al iniciar la sesión, lo que significa que Braze puede enviar un mensaje al usuario antes de que se alcance el límite, pero cuando el usuario desencadena el mensaje, ya se ha alcanzado el límite. En esta situación, el dispositivo seguirá mostrando el mensaje.

Por ejemplo, supongamos que tienes un juego con un mensaje dentro de la aplicación que se desencadena cuando un usuario supera un nivel, y lo limitas a 100 impresiones. Hasta ahora ha habido 99 impresiones. Alice y Bob abren el juego y Braze indica a sus dispositivos que son elegibles para recibir el mensaje cuando superen un nivel. Alice supera primero un nivel y recibe el mensaje. Bob supera el nivel a continuación, pero como su dispositivo no se ha comunicado con los servidores Braze desde que comenzó su sesión, su dispositivo no es consciente de que el mensaje ha alcanzado su tope y él también recibirá el mensaje. Sin embargo, cuando se ha alcanzado un tope de impresiones, la próxima vez que cualquier dispositivo solicite la lista de mensajes dentro de la aplicación elegibles, ese mensaje no se enviará y se eliminará de ese dispositivo.

### Limitación de tasa y pruebas A/B

Cuando se utiliza el límite de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma forma que al grupo de prueba, lo que es una fuente potencial de sesgo temporal. Para evitar este sesgo, utiliza ventanas de conversión adecuadas.

### Limitación de la tasa de velocidad de entrega

Si prevés que las grandes campañas provoquen un aumento de la actividad de los usuarios y sobrecarguen tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes, lo que significa que Braze no enviará más de lo que hayas configurado como límite de velocidad en un minuto.

Al dirigirte a los usuarios durante la creación de la campaña, puedes navegar a **Audiencias objetivo** (para campañas) o a **Configuración de envío** (para Canvas) para seleccionar un límite de velocidad (en varios incrementos, desde tan bajo como 10 hasta tan alto como 500.000 mensajes por minuto).

Ten en cuenta que las campañas sin tasa limitada pueden superar estos límites de entrega. Sin embargo, ten en cuenta que los mensajes se cancelarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. Si el límite de velocidad es demasiado bajo, el creador de la campaña recibirá alertas en el panel y por correo electrónico.

\![Resumen de audiencia con una casilla seleccionada para limitar la tasa a la que finalizará la campaña, y una tasa de 500.000 por minuto.]({% image_buster /assets/img_archive/per_minute_rate_limit.png %})

#### Ejemplo

Si intentas enviar 75.000 mensajes con un límite de velocidad de 10.000 por minuto, la entrega se repartirá en ocho minutos. Tu campaña no entregará más de 10.000 mensajes durante cada uno de los primeros siete minutos, y 5.000 durante el último minuto.

#### Número de envíos

Ten en cuenta que los mensajes con tasa limitada pueden no enviarse uniformemente a lo largo de cada minuto. Utilizando el ejemplo de un límite de tasa de 10.000 por minuto, esto significa que Braze se asegura de que no se envían más de 10.000 mensajes por minuto. Esto podría significar que un mayor porcentaje de los 10.000 mensajes se envían en el primer medio minuto frente al último medio minuto.

El límite de velocidad se aplica al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad en algunos minutos. Con el tiempo, el número de envíos por minuto no superará el límite de velocidad.

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

Para las campañas push que se entregan en varias plataformas, el límite de velocidad seleccionado se distribuirá equitativamente entre las plataformas. Una campaña de mensajería push que aproveche Android e iOS con un límite de tasa de 10.000 por minuto distribuirá equitativamente los 10.000 mensajes entre las dos plataformas.

#### Limitación de la tasa de velocidad de entrega de Canvas {#canvas-delivery-speed}

Al enviar un Canvas con un límite de velocidad, el límite de tasa se comparte entre canales. Esto significa que el número total de mensajes enviados por minuto desde el Canvas no superará el límite de velocidad. Por ejemplo, si tu Canvas tiene un límite de velocidad de 10.000 por minuto y utiliza correo electrónico y SMS, Braze enviará un total de 10.000 mensajes por minuto por correo electrónico y SMS.

#### Limitación de tasa y reintentos de contenido conectado

Cuando el [reintento de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) está activado, Braze reintentará los fallos de llamada respetando el límite de velocidad que establezcas para cada reenvío. Consideremos el caso de enviar 75.000 mensajes con un límite de velocidad de 10.000 por minuto. Imagina que en el primer minuto, la llamada falla o es lenta y sólo envía 4.000 mensajes.

En lugar de intentar compensar el retraso y enviar los 6.000 mensajes restantes en el segundo minuto o añadirlos a los 10.000 que ya están configurados para enviar, Braze moverá esos 6.000 mensajes al "final de la cola" y añadirá un minuto, si es necesario, al total de minutos que tardaría en enviar tu mensaje.

| Minuto | Sin fallo | 6.000 Fallo en el minuto 1 |
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

A medida que tu base de usuarios sigue creciendo y tu mensajería se amplía para incluir campañas de ciclo de vida, desencadenadas, transaccionales y de conversión, es importante evitar que tus notificaciones parezcan "spam" o perturbadoras. Al proporcionar un mayor control sobre la experiencia de tus usuarios, la limitación de frecuencia te habilita para crear las campañas que desees sin abrumar a tu audiencia.

### Resumen de características {#freq-cap-feat-over}

La limitación de frecuencia se aplica en el nivel de envío de la campaña o del componente Canvas y puede configurarse para cada espacio de trabajo desde **Configuración** > **Reglas de limitación de frecuencia**.

Por predeterminado, la limitación de frecuencia se alterna cuando se crean nuevas campañas. Desde aquí, puedes elegir lo siguiente:

- Qué canal de mensajería te gustaría capar: push, correo electrónico, SMS, webhook, WhatsApp o cualquiera de esos cinco.
- Cuántas veces debe recibir cada usuario el envío de una campaña o componente Canvas de un canal dentro de un plazo determinado.
- Cuántas veces debe recibir cada usuario una campaña o componente Canvas enviado por [etiqueta](#frequency-capping-by-tag) dentro de un plazo determinado.

Este plazo puede medirse en minutos, días o semanas (siete días), con una duración máxima de 30 días.

Cada línea de limitación de frecuencia se conectará mediante el operador `AND`, y puedes añadir hasta 10 reglas por espacio de trabajo. Además, puedes incluir varias tapas para los mismos tipos de mensajes. Por instancia, puedes limitar a los usuarios a no más de un push al día y no más de tres push a la semana.

\![Sección de limitación de frecuencia con listas de campañas y Lienzos a los que se aplicarán las normas y a los que no.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %})

#### Comportamiento cuando los usuarios tienen limitación de frecuencia en un paso en Canvas

Si un usuario de Canvas tiene limitación de frecuencia debido a la configuración global de limitación de frecuencia, el usuario avanzará inmediatamente al siguiente paso en Canvas. El usuario no saldrá del Canvas debido al límite de frecuencia.

### Normas de entrega

Puede haber algunas campañas, como los mensajes transaccionales, que quieras que lleguen siempre al usuario, aunque ya haya alcanzado su límite de frecuencia. Por ejemplo, una aplicación de entrega puede querer enviar un correo electrónico o un push cuando se entrega un artículo, independientemente de cuántas campañas haya recibido el usuario.

Si quieres que una campaña concreta anule las normas de limitación de frecuencia, puedes configurarlo en el panel de Braze al programar la entrega de esa campaña, alternando la opción **Limitación de frecuencia** en **OFF**. 

Después de esto, se te preguntará si todavía quieres que esta campaña cuente para tu límite de frecuencia. Los mensajes que cuentan para la limitación de frecuencia se incluyen en los cálculos del filtro del canal inteligente. Al enviar [campañas API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), que suelen ser transaccionales, tendrás la posibilidad de especificar que una campaña ignore las normas de limitación de frecuencia [dentro de la solicitud API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns) configurando `override_messaging_limits` en `true`.

Por defecto, las nuevas campañas y los Lienzos que no respeten los límites de frecuencia tampoco contarán. Esto es configurable para cada campaña y Canvas.

{% alert note %}
Este comportamiento cambia el predeterminado cuando desactivas la limitación de frecuencia para una campaña o Canvas. Los cambios son compatibles con versiones anteriores y no afectan a los mensajes que están actualmente en vivo.
{% endalert %}

\![Sección Controles de entrega con la limitación de frecuencia activada.]({% image_buster /assets/img_archive/frequencycappingupdate.png %})

Los distintos canales de una campaña multicanal contabilizarán individualmente el límite de frecuencia. Por ejemplo, si creas una campaña multicanal con push y correo electrónico y has configurado la limitación de frecuencia para ambos canales, entonces el push contará para una campaña push y el mensaje de correo electrónico contará para una campaña de mensajes de correo electrónico. La campaña también contará para una "campaña de cualquier tipo". Si los usuarios están limitados a una campaña push y a una campaña de correo electrónico al día y un usuario recibe esta campaña multicanal, dejará de ser elegible para campañas push o de correo electrónico durante el resto del día (a menos que una campaña ignore las normas de limitación de frecuencia).

Los mensajes dentro de la aplicación y las tarjetas de contenido no se tienen en cuenta para los límites de las campañas ni para los componentes de Canvas de ningún tipo.

{% alert important %}
La limitación de frecuencia global se programa en función de la zona horaria del usuario y se calcula por días naturales, no por periodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de envío de no más de una campaña al día, un usuario puede recibir un mensaje a las 11 de la noche en su zona horaria local y sería elegible para recibir otro mensaje una hora más tarde.
{% endalert %}

#### Casos de uso

{% tabs %}
{% tab Use case 1 %}

Digamos que estableces una regla de limitación de frecuencia que pide que tu usuario no reciba más de tres campañas de notificación push o componentes de Canvas a la semana de todas las campañas o componentes de Canvas.

Si tu usuario está programado para recibir tres notificaciones push, dos mensajes dentro de la aplicación y una tarjeta de contenido esta semana, recibirá todos esos mensajes.

{% endtab %}
{% tab Use case 2 %}

Este escenario utiliza las siguientes reglas de limitación de frecuencia:

**Cuando se produce el siguiente escenario:**

- Un usuario desencadena la misma campaña, `Campaign ABC` tres veces a lo largo de una semana.
- Este usuario desencadena `Campaign ABC` una vez el lunes, una vez el miércoles y una vez el jueves.

\![Sección de limitación de frecuencia con la norma de no enviar más de 2 campañas de notificación push/Pasos en Canvas de todas las campañas/Pasos en Canvas a un usuario cada 1 semana.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Entonces, el comportamiento esperado es ése:**

- Este usuario recibirá los envíos de campaña que se desencadenaron el lunes y el miércoles.
- Este usuario no recibirá el tercer envío de campaña el jueves porque ya ha recibido dos envíos de campaña push esa semana.

{% endtab %}
{% endtabs %}

### Limitación de frecuencia por etiqueta

[Las reglas de limitación de frecuencia](#delivery-rules) pueden aplicarse a los espacios de trabajo utilizando etiquetas específicas que hayas aplicado a tus campañas y Lienzos, permitiéndote basar esencialmente tu limitación de frecuencia en grupos con nombres personalizados.

Con la limitación de frecuencia por etiqueta, se pueden establecer reglas en las etiquetas principales y anidadas, para que Braze tenga en cuenta todas las etiquetas. Por ejemplo, si has seleccionado utilizar la etiqueta principal A para limitar la frecuencia, también incluiremos la información de todas las etiquetas anidadas (por ejemplo, las etiquetas B y C) al determinar el límite.

También puedes combinar la limitación de frecuencia normal con la limitación de frecuencia por etiquetas. Considera las siguientes reglas:

1. No más de tres campañas de notificación push o componentes de Canvas por semana de todos los pasos en Canvas y campañas. <br>**Y**
2. No más de dos campañas de notificación push o componentes de Canvas por semana con la etiqueta `promotional`.

\![Sección de limitación de frecuencia con dos reglas que limitan cuántas campañas de notificación push/Canvases se pueden enviar a un usuario cada 1 semana.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Como resultado, tus usuarios no recibirán más de tres envíos de campaña por semana en todas las campañas y pasos en Canvas y no más de dos campañas de notificación push o componentes de Canvas con la etiqueta `promotional`.

{% alert important %}
Los lienzos se etiquetan a nivel de Canvas, en lugar de etiquetarlos por componentes. Así, cada componente Canvas heredará todas las etiquetas de nivel Canvas.
{% endalert %}

#### Normas contradictorias

Cuando las normas entren en conflicto, se aplicará a tus usuarios la norma de limitación de frecuencia aplicable más restrictiva. Por ejemplo, supongamos que tienes las siguientes reglas:

1. No más de una campaña de notificación push o componente Canvas por semana de todos los componentes de campaña y Canvas. <br>**Y**
2. No más de tres campañas de notificación push o componentes de Canvas por semana con la etiqueta `promotional`.

\![Sección de limitación de frecuencia con normas conflictivas para limitar cuántas campañas de notificación push/pasos en Canvas se envían a un usuario cada 1 semana.]({% image_buster /assets/img/global_rules.png %} "global rules")

En este ejemplo, tu usuario no recibirá más de una campaña de notificación push o componentes Canvas con la etiqueta "promocional" en una semana determinada, porque has especificado que los usuarios no deben recibir más de una campaña de notificación push o componente Canvas de todas las campañas y componentes Canvas. En otras palabras, la norma de frecuencia aplicable más restrictiva es la que se aplicará a un usuario determinado.

#### Recuento de etiquetas

La limitación de frecuencia por reglas de etiqueta se computa en el momento en que se envía un mensaje. Esto significa que la limitación de frecuencia por etiqueta sólo cuenta las etiquetas que están actualmente en las campañas o Lienzos que un usuario recibió en el pasado. No cuenta las etiquetas que estaban en las campañas o Lienzos durante el tiempo en que se enviaron, pero que se han eliminado desde entonces. Contará si posteriormente se añade una etiqueta a un mensaje que un usuario recibió en el pasado, pero antes de que se envíe el mensaje etiquetado más reciente.

##### Casos de uso

Considera las siguientes campañas y la limitación de frecuencia por regla de etiqueta:

**Campañas**:

- **La campaña A** es una campaña push etiquetada como `promotional`. Está previsto que se envíe el lunes a las 9 de la mañana.
- **La campaña B** es una campaña push etiquetada como `promotional`. Está previsto que se envíe a las 9 de la mañana del miércoles.

**Limitación de frecuencia por regla de etiqueta:**

- Tu usuario no debe recibir más de una campaña de notificación push a la semana con la etiqueta `promotional`.<br><br>

| Acción | Resultado |
|---|---|
| La etiqueta `promotional` se elimina de **la campaña A** después de que tu usuario haya recibido el mensaje, pero antes de que **se haya enviado la campaña B.** | Tu usuario recibirá **la campaña B**.|
| La etiqueta `promotional` se ha eliminado por error de **la campaña A** después de que tu usuario recibiera el mensaje. <br> La etiqueta se vuelve a añadir a **la campaña A** el martes, antes de enviar **la campaña B**. | Tu usuario no recibirá **la campaña B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envío a gran escala {#sending-at-large-scales}

La limitación de frecuencia mediante reglas de etiquetas podría no aplicarse correctamente a grandes escalas, como 100 mensajes por canal de campañas o componentes de Canvas.

Por ejemplo, si tu regla de limitación de frecuencia por etiqueta es:

> No más de dos campañas de correo electrónico o componentes de Canvas con la etiqueta `Promotional` a un usuario cada semana.

Si envías al usuario más de 100 correos electrónicos de campañas y pasos en Canvas con la limitación de frecuencia activada en el transcurso de una semana, es posible que se le envíen más de dos correos electrónicos.

Dado que 100 mensajes por canal son más mensajes de los que la mayoría de las marcas envían a sus usuarios, es poco probable que te veas afectado por esta limitación. Para evitar esta limitación, puedes establecer un tope para el número máximo de correos electrónicos que deseas que reciban tus usuarios en el transcurso de una semana.

Por ejemplo, puedes establecer la siguiente regla:

> No más de tres campañas por correo electrónico o componentes de Canvas por semana de todos los pasos en Canvas y campañas.

Esta regla garantizará que ningún usuario reciba más de 100 correos electrónicos a la semana porque, como máximo, los usuarios recibirán tres correos electrónicos a la semana de campañas o componentes de Canvas con la limitación de frecuencia activada.

