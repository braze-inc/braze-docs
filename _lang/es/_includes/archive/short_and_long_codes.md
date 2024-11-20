
# Envío de números de teléfono

Los códigos abreviados y largos son el número de teléfono desde el que envías mensajes a tus usuarios o clientes. Pueden ser códigos abreviados de 5 ó 6 dígitos, o códigos largos de 10 dígitos. Cada tipo de código ofrece ventajas específicas y deben tenerse en cuenta todos los factores antes de elegir si quieres un código abreviado, qué tipo de código abreviado puedes querer, además del código largo que ya tendrás asignado.

## Tipos de números de envío

{% tabs %}
{% tab Códigos abreviados %}

#### Códigos abreviados

Un código abreviado es una secuencia memorable de 5-6 dígitos que permite a los remitentes enviar mensajes a tasas más altas que los códigos largos. Esto hace que los códigos abreviados sean perfectos para envíos urgentes de gran volumen.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | Aplicación de 8 a 12 semanas| 100 mensajes por segundo o más | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros y contras

| Pros |
| ---- |
| **Velocidad y escalabilidad**<br> Los códigos abreviados ofrecen velocidad y escalabilidad con tasas de envío de 100 segmentos por segundo, 6.000 segmentos por minuto, 360 mil segmentos por hora y 1 millón de segmentos cada 2 horas. Los códigos abreviados pueden alcanzar tasas tan elevadas debido a la investigación necesaria durante el proceso de solicitud del código abreviado.<br><br>**MMS habilitado para algunos códigos abreviados**<br>Algunos códigos abreviados pueden admitir MMS, también conocido como servicio de mensajes multimedia, que te permite enviar mensajes con activos multimedia (JPEG, GIF, PNG) a teléfonos móviles. Para más información sobre MMS en Braze, consulta [Acerca de MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Contras |
| ---- |
| **Los códigos abreviados están disponibles en menos países**<br> Los códigos abreviados están disponibles actualmente en algunos países, como EE. UU., Reino Unido y Canadá.<br><br>**Proceso de solicitud más largo**<br> Se requiere un proceso de solicitud complejo en el que los casos de uso deben describirse con gran detalle. Esto es necesario para apoyar la capacidad de entrega, porque después de conceder un código abreviado, los operadores auditarán los códigos abreviados, pero **no** filtrarán los mensajes, lo que permitirá tasas de envío más altas. La duración de este proceso varía según el país.<br><br>**Mayor costo**<br> Los códigos abreviados cuestan más que los códigos largos y tardan más en aprobarse. Sin embargo, después de tener un código abreviado, se te considera "preaprobado" para enviar mensajes a tasas mejores y más rápidas, y estás sujeto a menos escrutinio durante el proceso de envío, ya que habrás pasado por todas las comprobaciones durante tu solicitud del código abreviado. |
{: .reset-td-br-1}

{% endtab %}
{% tab Códigos largos %}

#### Códigos largos

Un código largo es un número de teléfono estándar que se utiliza para enviar y recibir llamadas de voz y mensajes SMS. Los números de teléfono suelen denominarse "códigos largos" (números de 10 cifras en muchos países) cuando se comparan con los códigos abreviados de los SMS (números de 5-6 cifras).

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitud de 4 a 6 semanas (puede ser más corta o más larga para distintos países). | En EE.UU., el rendimiento depende de tu puntuación de confianza 10DLC; en los mercados internacionales, el rendimiento puede variar o aumentar en algunas circunstancias. | Sí | Bidireccional (dependiendo de desde dónde envíes) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros y contras

| Pros |
| ---- |
| **Se puede utilizar inmediatamente para enviar mensajes (para determinados países)**<br>Los códigos largos proporcionan una experiencia del cliente localizada y personalizada al enviar mensajes para casos de uso de persona a persona. A diferencia de los códigos abreviados de los SMS, adquirir un código largo es un proceso bastante rápido para algunos países. (Para otros países, se necesita tanto o más tiempo que un código abreviado). Los códigos largos también pueden configurarse como número alternativo si falla un código abreviado.<br><br>**Mayor disponibilidad en todo el mundo**<br>Los códigos largos están disponibles en más de 100 países importantes de todo el mundo. Ponte en contacto con tu administrador del éxito del cliente o con [el soporte]({{site.baseurl}}/braze_support/) de Braze para obtener una lista de los países disponibles.<br><br>**MMS habilitado para determinados países**<br>Admite MMS, también conocido como Servicio de Mensajes Multimedia, que te permite enviar mensajes con activos multimedia (JPEG, GIF, PNG) a teléfonos móviles. Para más información sobre MMS en Braze, consulta nuestra documentación [aquí]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/).|
{: .reset-td-br-1}

| Contras |
| --- |
| **Velocidades de envío más lentas**<br>Los códigos largos no se corresponden con la velocidad y el envío de los códigos abreviados. Las tasas de envío de SMS dependen de tu puntuación de confianza 10DLC en EEUU. |
{: .reset-td-br-1}

{% endtab %}
{% tab Código abreviado de vanidad %}

#### Códigos abreviados de vanidad

Un código abreviado personalizado es un número de teléfono de 5-6 dígitos seleccionado específicamente por una marca. Los códigos abreviados de marca son más fáciles de recordar para los consumidores, aunque suelen ser más caros. Por ejemplo:
- El Departamento de Sanidad de Nueva York tiene un código abreviado de vanidad: `692-692`, que se escribe NYC-NYC en el teclado del teléfono.
- Amazon utiliza un código abreviado de `262-966` que se escribe AMA-ZON para las actualizaciones de seguimiento de los envíos.
- PayPal utiliza un código abreviado de `729-725` que se escribe PAY-PAL para los comandos de mensajes de texto.<br><br>

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | Aplicación de 8 a 12 semanas | 100 mensajes por segundo | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros y contras

| Pros |
| ---- |
| **Velocidad y escalabilidad**<br> Los códigos abreviados ofrecen velocidad y escalabilidad con tasas de envío de 100 segmentos por segundo, 6.000 segmentos por minuto, 360 mil segmentos por hora y 1 millón de segmentos cada 2 horas. Los códigos abreviados pueden alcanzar tasas tan elevadas debido a la investigación necesaria durante el proceso de solicitud del código abreviado.<br><br>**MMS habilitado**<br>Admite MMS, también conocido como Servicio de Mensajes Multimedia, que te permite enviar mensajes con activos multimedia (JPEG, GIF, PNG) a teléfonos móviles. Para más información sobre MMS en Braze, consulta [Acerca de MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/about_mms/). |
{: .reset-td-br-1}

| Contras |
| ---- |
| **Los códigos abreviados no están disponibles en todas partes**<br> Actualmente, los códigos abreviados sólo están disponibles en **EE.UU. y Canadá (CA)**.<br><br>**Proceso de solicitud más largo**<br> Se requiere un proceso de solicitud de 8 a 12 semanas en el que los casos de uso deben exponerse con gran detalle. Este proceso es necesario para apoyar la capacidad de entrega, ya que después de conceder un código abreviado, los operadores auditarán los códigos abreviados, pero **no** filtrarán los mensajes, lo que permitirá tasas de envío más altas.<br><br>**Mayor costo en EE. UU.**<br> Los códigos abreviados no tienen coste adicional en California, pero en Estados Unidos los códigos abreviados cuestan más que los códigos largos y tardan más en aprobarse. Sin embargo, después de tener un código abreviado, se te considera "preaprobado" para enviar mensajes a tasas mejores y más rápidas, y estás sujeto a menos escrutinio durante el proceso de envío, ya que habrás pasado por todas las comprobaciones durante tu solicitud del código abreviado. |
{: .reset-td-br-1}

{% endtab %}
{% tab ID alfanumérico del remitente %}

#### ID alfanumérico del remitente

Los ID de remitente son los códigos abreviados o largos que aparecen en la parte superior de un mensaje SMS y que indican quién envió el mensaje. Si un usuario no está familiarizado con un ID de remitente, puede optar por ignorar por completo estos mensajes. Mediante el uso de ID alfanuméricos de remitente, los usuarios pueden identificar rápidamente de quién están recibiendo mensajes, lo que aumenta las tasas de apertura. 

Los ID de remitente alfanuméricos te permiten establecer el nombre de tu empresa o marca (como "Kitchenerie" o "CashBlastr") como ID de remitente al enviar mensajes unidireccionales a usuarios de móvil. Pueden tener hasta 11 caracteres y acepta letras mayúsculas (A-Z) y minúsculas (a-z), espacios y dígitos (0-9). **Puede que no** haya sólo números. 

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| Hasta 11 caracteres | Disponible inmediatamente si no se requiere preinscripción | Varía según el país | No | Unidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros y contras

| Pros | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Sin coste adicional de implantación </li> <li> Mejora el conocimiento de la marca </li> <li> Aumenta las tasas de apertura de los SMS </li> <li> Coincide con la velocidad de envío de los números de teléfono dentro del grupo de suscripción </li> <li> Disponible inmediatamente si no se requiere preinscripción </li> </ul> {:/} | {::nomarkdown} <ul> <li> No se admite la <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>mensajería bidireccional</a>  </li> <li> No todos los países admiten esta característica </li> <li> Algunos países requieren un proceso de aprobación adicional </li> <li> El MMS no está habilitado </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

Para más información sobre el ID alfanumérico de remitente, ponte en contacto con tu administrador del éxito del cliente.
{% endtab %}
{% tab Número de teléfono gratuito %}

#### Número gratuito habilitado para SMS

Un número de teléfono gratuito, o un número de teléfono gratuito, es un número de teléfono al que se facturan todas las llamadas entrantes en lugar de incurrir en gastos en el abonado telefónico de origen. Los números gratuitos de EE.UU. y Canadá están habilitados para SMS, en los que se cobra a los suscriptores por los mensajes entrantes y salientes.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos	 | 2-4 semanas de aplicación | Depende de tu aprobación y se puede aumentar pagando más | No | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Pros y contras

| Pros | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Debes registrarte antes de enviar. </li> </ul> {:/} | {::nomarkdown} <ul> <li> Los números gratuitos son sólo los de EE.UU. y Canadá </li><li> El MMS no está habilitado </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2} 

{% endtab %}
{% endtabs %}

{% alert important %}
Si se supera el rendimiento, algunos mensajes pueden fallar.
{% endalert %}

Además de estas diferencias, debes saber que una marca suele tener un código abreviado, pero varios códigos largos de reserva, en función del número de destinatarios a los que tenga previsto enviar SMS.

{% alert important %}
¿Te preguntas en qué consisten los códigos abreviados compartidos? Para saber más sobre por qué recomendamos alejarse de los códigos abreviados compartidos, visita el tema en nuestras [Preguntas frecuentes sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/).
{% endalert %}

## ¿Cómo consigo un código abreviado?

El proceso de solicitud del código abreviado puede ser largo. Sin embargo, ¡puede merecer la pena! Si quieres un código abreviado, ponte en contacto con tu administrador de incorporación u otro representante de Braze y díselo. Después de hacerlo, lo solicitarán por ti: te pedirán algunos datos básicos que te ayudarán a reunir los requisitos. Entonces, ¡sólo queda esperar!

### Solicitud de código abreviado

Aunque Braze se encarga de solicitar el código abreviado, necesitamos que nos facilites cierta información. Te recomendamos que revises estas preguntas antes de ponerte en contacto con Braze. 

La normativa exige que haya respuestas a todas las respuestas de adhesión voluntaria, exclusión voluntaria y palabras clave de ayuda/información. Tendrás que indicarnos los flujos de mensajes específicos (las respuestas que quieres enviar a los usuarios después de que envíen una [palabra clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)) que deseas para las siguientes situaciones.

| Flujo necesario | Tipo | Ejemplo |
| ----------- | ---- | ------- |
| Adhesión voluntaria <br><br>Doble adhesión voluntaria| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Adhesión voluntaria | Sitio web | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Cancelación | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Ayuda | N/A | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Dependiendo de tu situación, puede que necesites proporcionar más o menos flujos como los enumerados en la tabla anterior. También tendrás que indicarnos **tres ejemplos generales** de mensajes que piensas enviar por SMS; no dudes en pedir orientación a tu representante de Braze.

También debes informarnos, independientemente del número que utilices, de cuántos mensajes al mes piensas enviar.

{% alert important %}
Si tienes tu propio código abreviado, ponte en contacto con tu administrador del éxito del cliente durante el proceso de incorporación para hablar de la migración o transferencia de tu código abreviado. Los códigos abreviados deben ser configurados por tu administrador del éxito del cliente.
{% endalert %}

## Aplicación-a-Persona Códigos largos de 10 dígitos (A2P 10DLC)

A2P 10DLC hace referencia a un sistema de Estados Unidos que permite a las empresas enviar mensajería del tipo Aplicación a Persona (A2P) a través de un número de teléfono estándar de código largo de 10 dígitos (10DLC). Los códigos largos de 10 dígitos se han diseñado tradicionalmente para el tráfico de Persona a Persona (P2P), por lo que las empresas se ven constreñidas por un rendimiento limitado y un mayor filtrado. Este servicio ayuda a aliviar esos problemas, mejorando la capacidad de entrega de mensajes en general, permitiendo a las marcas enviar mensajes a escala que incluyan enlaces y llamadas a la acción, y ayudando a proteger aún más a los consumidores de mensajes no deseados. 

Todos los clientes que actualmente tengan y/o utilicen códigos largos de EE. UU. para enviar a clientes de dicho país deben registrar sus códigos largos para 10DLC. Este proceso de solicitud tarda entre 4 y 6 semanas. Para saber más sobre los detalles del 10DLC y por qué es necesario, visita nuestro [artículo dedicado al 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/