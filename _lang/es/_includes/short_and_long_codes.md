# Remitentes de SMS y RCS

> Este artículo ofrece un resumen de los códigos y remitentes disponibles para enviar mensajes SMS y RCS.

## Tipos de remitentes de SMS y RCS

{% tabs %}
{% tab RCS-Verified Sender %}

#### Remitente verificado por RCS

RCS es un moderno sistema de mensajería que ofrece más características que los SMS tradicionales, introduciendo capacidades como ID de remitente con marca, medios enriquecidos y contenido interactivo, como carruseles desplazables, respuestas rápidas, botones CTA y mucho más. Está diseñado para ofrecer una experiencia de usuario más elegante y con más interacción.  

##### Detalles

| Componentes visuales | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| \- Marca comercial<br>\- logotipo<br>\- subtítulo opcional<br> \- señal verificada | 4-6 semanas para la aprobación del operador. | El rendimiento y la entrega dependen de que el destinatario disponga de una conexión de datos activa (datos móviles o Wi-Fi). RCS no depende de los límites fijos impuestos por la red como lo hace SMS; los mensajes RCS se envían a través de redes de datos en lugar de los canales de señalización celular tradicionales utilizados por SMS. | N/A | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros y contras

| Pros |
| ---- |
| **Confianza y marca verificadas**<br> A diferencia de los SMS tradicionales, en los que tu marca aparece como un código abreviado o largo de 5 dígitos, RCS permite perfiles de remitente verificados. Estos perfiles incluyen el logotipo y el nombre de tu marca, así como una marca de verificación «verificado». |
| **Características avanzadas de mensajería**<br> RCS admite carruseles, videos de alta resolución y botones de acción sugeridos (como «Reservar ahora», «Seguir paquete» o «Pagar factura»). Los usuarios pueden completar tareas complejas sin salir de su aplicación de mensajería, lo que puede generar tasas de conversión más altas que un enlace de texto sin formato. |
{: .reset-td-br-1 role="presentation"}

| Contras |
| ---- |
| **Apoyo fragmentado**<br> Aunque Google ha pushado mucho el RCS para Android y Apple ha introducido recientemente la compatibilidad con RCS para iOS, la implementación aún puede ser desigual entre los diferentes operadores y regiones. Si el teléfono o el operador del usuario no son compatibles con RCS, el mensaje se envía normalmente como un SMS normal, por lo que se pierden todas las características «avanzadas» de RCS. |
| **Incoherencias de la plataforma**<br> La experiencia del usuario de RCS varía en función del operador del destinatario, el modelo del dispositivo y la aplicación de mensajería que utilices (por ejemplo, Google Messages o iMessage). |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Short Codes %}

#### Códigos abreviados SMS

Un código abreviado es un número de 5-6 dígitos que permite enviar y recibir SMS a y desde teléfonos móviles a una tasa mayor que la de los códigos largos. Se recomienda utilizar códigos abreviados para envíos de gran volumen y urgentes.

Algunos países te permiten elegir un número específico por una tarifa adicional. Estos códigos abreviados se denominan códigos abreviados personalizados. Si estás interesado en los códigos abreviados personalizados, ponte en contacto con tu representante de cuenta de Braze para obtener más información.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | Aplicación de 4 a 12 semanas| 100 mensajes por segundo o más | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros y contras

| Pros |
| ---- |
| **Velocidad y escalabilidad**<br> Los códigos abreviados están diseñados específicamente para un tráfico de gran volumen. Pueden enviar mensajes a tasas más rápidas que los códigos largos y, dado que son previamente verificados directamente por los operadores, tienen el menor riesgo de ser marcados por los filtros automáticos de correo no deseado. |
| **Fácil de recordar para «Call to Action» (Llamada a la acción)**<br> Para las campañas de marketing (por ejemplo, «Envía WIN al 55555»), un código abreviado es mucho más fácil de recordar y escribir para los usuarios que un número de 10 dígitos. Esto convierte a los códigos abreviados en el estándar de referencia para los anuncios de radio, televisión y vallas publicitarias, donde el usuario solo tiene unos segundos para ver u oír el número. |
{: .reset-td-br-1 role="presentation"}

| Contras |
| ---- |
| **Los códigos abreviados están disponibles en menos países**<br> Los códigos abreviados no están disponibles en todos los países. Ponte en contacto con tu equipo de cuentas de Braze para consultar los países a los que deseas enviar mensajes. |
| **Proceso de solicitud más largo**<br> A diferencia de los códigos largos y los ID de remitente alfanuméricos, que pueden proporcionarse en un plazo de 1 a 2 semanas, los códigos abreviados pueden tardar entre 4 y 12 semanas o más en proporcionarse. Todos los principales operadores deben aprobar manualmente tu solicitud específica antes de que el código se active en su red. Si tienes un lanzamiento de marketing la semana que viene, un código abreviado no es una opción. |
| **Mayor costo**<br> Los códigos abreviados suelen ser el tipo de remitente más caro debido a los gastos de configuración y las cuotas anuales de alquiler. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Long Codes %}

#### Códigos largos SMS

Un código largo es un número de teléfono estándar que se utiliza para enviar y recibir mensajes SMS. Estos números de teléfono suelen denominarse «códigos largos» (números de 10 dígitos en muchos países) en comparación con los códigos abreviados de SMS (números de 5-6 dígitos).

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos | Solicitud de 4 a 6 semanas (puede ser más corta o más larga para distintos países). | En Estados Unidos, el rendimiento de los códigos largos depende de tu puntuación de confianza 10DLC; en los mercados internacionales, el rendimiento puede variar o aumentar en algunas circunstancias, pero normalmente comienza en torno a los 10 segmentos del mensaje por segundo (MPS). | Sí | Bidireccional (dependiendo de desde dónde envíes) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros y contras

| Pros |
| ---- |
| **Familiaridad y confianza**<br> Los códigos largos se parecen a los números de teléfono personales y suelen incluir un código de área local. Para las marcas, esto representa un equilibrio entre una presencia profesional y un toque personal y accesible. |
| **Mayor disponibilidad en todo el mundo**<br>Los códigos largos están disponibles en más de 100 países importantes de todo el mundo. Ponte en contacto con tu administrador del éxito del cliente o con [el soporte de Braze]({{site.baseurl}}/braze_support/) para obtener una lista de los países disponibles.|
{: .reset-td-br-1}

| Contras |
| --- |
| **Velocidades de envío más lentas y límites diarios de mensajería**<br> Los códigos largos no están diseñados para el marketing masivo como lo están los códigos abreviados. Si intentas enviar una venta flash urgente a 100 000 personas a la vez desde un código largo, tu puede tardar horas en entregar todos los mensajes. En EE. UU., operadores como T-Mobile también pueden imponer límites diarios de envío para 10DLC en función de la puntuación de confianza de tu marca. |
| **Riesgo de filtrado más estricto**<br> Dado que los códigos largos se parecen a los números de teléfono personales, los operadores los supervisan de cerca para evitar que los números «de persona a persona» se utilicen para enviar correo no deseado. Incluso con una campaña 10DLC registrada, si el contenido de tu mensaje es demasiado «spam» o no sigue un formato estricto, corres un riesgo mucho mayor de ser bloqueado por los operadores en comparación con un código abreviado preaprobado. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### ID alfanumérico del remitente de SMS

Un ID de remitente alfanumérico (a menudo denominado «alfa») es una cadena reconocible compuesta por cualquier combinación de letras y números (a menudo el nombre de tu empresa o marca) que se muestra como ID de remitente en los mensajes de texto unidireccionales.

Pueden tener hasta 11 caracteres y contener letras mayúsculas (A-Z) y minúsculas (a-z), espacios y dígitos (0-9). **No** pueden contener solo números.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| Hasta 11 caracteres | Disponible inmediatamente si no es necesario registrarse previamente. De lo contrario, entre 1 y 4 semanas en la mayoría de los países donde se requiere registro. | Varía según el país | No | Unidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros y contras

| Pros | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul><li> Mejora del reconocimiento de marca </li><li> En muchos mercados internacionales, los operadores locales preinscriben y verifican a los remitentes alfanuméricos, por lo que es menos probable que tus mensajes sean detectados por los agresivos filtros de correo no deseado de los operadores, que de otro modo podrían bloquear códigos largos aleatorios. </li><li> Disponible en 1 semana si no es necesario registrarse previamente. </li></ul> {:/} | {::nomarkdown} <ul><li> No se admite la <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>mensajería bidireccional</a>  </li><li> No todos los países admiten esta característica. Por ejemplo, está permitido en el Reino Unido, pero bloqueado en los Estados Unidos. </li><li> Algunos países cuentan con un extenso proceso de preinscripción que requiere la presentación de documentación legal y plazos de entrega más largos. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para obtener más información sobre los ID de remitente alfanuméricos, ponte en contacto con tu administrador del éxito del cliente.
{% endtab %}
{% tab SMS toll-free numbers %}

#### Números gratuitos habilitados para SMS

Los números gratuitos tienen códigos de área de tres dígitos distintos (por ejemplo, 800, 888, 877 y 866), lo que permite a los usuarios comunicarse con las empresas sin que se les cobre. Ampliamente utilizados para el servicio de atención al cliente, también pueden gestionar todo tipo de mensajes A2P (de aplicación a persona), incluidos los de marketing.

##### Detalles

| Longitud | Acceso | Rendimiento | MMS habilitado | Unidireccional vs. Bidireccional |
| --- | --- | --- | --- | --- |
| 10 dígitos	 | 2-4 semanas de aplicación | Comienza en 3 MPS (segmentos por segundo) y se puede aumentar por un costo adicional. | Sí | Bidireccional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Pros y contras

| Pros |
| ---- |
| **Imagen profesional**<br> Los números gratuitos gozan de un amplio reconocimiento y confianza en Norteamérica para las comunicaciones empresariales, ya que aportan un toque profesional y de autoridad. |
| **Rendimiento flexible; sin límites de envío por parte del operador.**<br> A diferencia de los códigos largos estándar, que pueden establecer límites de rendimiento o de envío por parte del operador en función del país, los números gratuitos pueden aumentar su rendimiento para soportar volúmenes más altos y no tienen límites diarios de envío por parte del operador en EE. UU.|
{: .reset-td-br-1 role="presentation"}

| Contras |
| --- |
| **Imparcialidad impersonal y geográfica**<br> Dado que los números gratuitos carecen de código local, pueden parecer demasiado «corporativos» o anónimos. Para una empresa de servicios locales, un número gratuito puede tener un rendimiento inferior al de un número estándar de código largo, ya que carece de conexión con la comunidad y, en ocasiones, puede confundirse con una línea de telemarketing aleatoria. |
| **Capa adicional para filtrar STOP**<br> Los números gratuitos tienen una capa de gestión de exclusión voluntaria fuera de Braze que no se puede eliminar ni personalizar. Cuando un usuario envía «STOP» a tu número gratuito, se le excluirá de recibir más mensajes de tu número y recibirá una respuesta automática generada por la red. No recibirán más mensajes de tu número gratuito hasta que envíen «START» por SMS para ser eliminados de la lista de bloqueados del número gratuito. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% endtabs %}

## Configuración

Los requisitos de configuración y los plazos varían según el tipo de remitente y el país en el que se te preste el servicio.

{% tabs local %}
{% tab RCS-verified sender %}

### Remitente verificado por RCS

Los remitentes verificados por RCS se proporcionan país por país. El proceso de verificación y configuración se centra en tu agente o remitente, la persona digital que interactúa con los usuarios. Proporcionarás los activos de la marca y los datos de verificación.

#### Activos de marca

- **Nombre verificado:** El nombre que los usuarios ven en la parte superior del hilo del mensaje. Debe ser un nombre comercial reconocible, no necesariamente el nombre legal de tu empresa.
- **Logotipo:** Una imagen de alta resolución de 224 x 224 píxeles. Esto se muestra en un marco circular, así que mantén los elementos críticos centrados.
- **Banner (imagen principal):** Una imagen de fondo para tu tarjeta de perfil empresarial (similar a una foto de portada de Facebook o LinkedIn).
- **Color de la marca:** Un valor hexadecimal para los botones y los elementos de la interfaz de usuario que se adapte al estilo de tu empresa.

#### Detalles de la verificación

- **Punto de contacto (POC):** Esto es fundamental. Debes proporcionar una dirección de correo electrónico de un empleado directo de la marca (no una dirección de correo electrónico de una agencia). Google o el operador enviarán un correo electrónico a esta persona para confirmar que ha autorizado a Braze a actuar en tu nombre.
- **Sitio web y política de privacidad:** Un sitio web en vivo y una política de privacidad que explique cómo gestionas los datos de usuario y la mensajería.
- **Descripción del caso de uso:** Una explicación clara de lo que estás enviando (por ejemplo, «Actualizaciones sobre la entrega de pedidos y atención al cliente para compras en comercio minorista»).

Los plazos de RCS varían según el país y a medida que más operadores adoptan el canal. Actualmente, puedes esperar que un remitente RCS sea aprobado por los operadores en un plazo de 3 a 6 semanas desde la solicitud de lanzamiento.

{% endtab %}
{% tab SMS short codes %}

### Códigos abreviados SMS

Los códigos abreviados se proporcionan país por país. Dependiendo del país, el proceso de solicitud de códigos abreviados es conocido por ser impredecible. Braze está aquí para ayudarte en cada paso, así que si deseas un código abreviado, ponte en contacto con tu administrador de incorporación u otro representante de Braze.

Braze te ayudará a recopilar todos los materiales y la información necesarios para enviar una solicitud y configurar un nuevo código abreviado. Los requisitos varían según el país, pero muchos exigen como mínimo lo siguiente:

| Material de solicitud    | Descripción    | Requisitos    |
|----------------------|----------------|-----------------|
| Llamada a la acción (adhesión voluntaria) | El objetivo principal de estas divulgaciones es confirmar que el usuario acepta recibir mensajes de texto y comprende la naturaleza del programa. | {::nomarkdown}<ul><li>Descripción del producto</li><li>Divulgación de la frecuencia de los mensajes</li><li>Términos y condiciones completos O enlace a los términos y condiciones completos</li><li>Política de privacidad O enlace a la política de privacidad</li><li>Palabra clave STOP</li><li>Aviso sobre posibles tasas por mensajes y datos.</li></ul>{:/} |
| Términos y condiciones | Los términos y condiciones completos pueden presentarse íntegramente debajo de la llamada a la acción o ser accesibles a través de un enlace cercano a la llamada a la acción. | {::nomarkdown}<ul><li>Nombre del programa (marca)</li><li>Divulgación de la frecuencia de los mensajes</li><li>Descripción del producto</li><li>Información de contacto del servicio de atención al cliente personalizado</li><li>Información sobre la exclusión voluntaria</li><li>Aviso sobre posibles tasas por mensajes y datos.</li></ul>{:/} |
| Flujo de mensajes | Los programas de mensajes recurrentes deben confirmar la adhesión voluntaria con un único mensaje de texto que indique explícitamente en qué programa se ha inscrito el usuario y proporcione instrucciones claras para darse de baja.<br><br> Braze procesa mensajes de adhesión voluntaria, cancelación de suscripción y ayuda, actualizando automáticamente el estado del grupo de suscripción del usuario y su número de teléfono asociado en todas las solicitudes entrantes.<br><br> Tenga en cuenta que estas palabras clave y respuestas predeterminadas también pueden personalizarse. | {::nomarkdown}<ul><li>Confirmación de adhesión voluntaria:<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Información sobre la exclusión voluntaria</li><li>Información de contacto del servicio de atención al cliente personalizado</li><li>Divulgación de la frecuencia de los mensajes</li><li>Aviso sobre posibles tasas por mensajes y datos.</li></ul></li><li>Respuesta de HELP:<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Información de contacto del servicio de atención al cliente (correo electrónico o número de teléfono de asistencia).</li></ul></li><li>Respuesta de exclusión voluntaria (STOP):<ul><li>Nombre del programa (marca) O descripción del producto</li><li>Confirmación de que no se entregarán más mensajes.</li></ul></li></ul>{:/} |
| Mensajes del programa | Los mensajes del programa se envían en el curso normal del programa de código abreviado, después de que el usuario haya recibido una confirmación de adhesión voluntaria. | {::nomarkdown}<ul><li>Las instrucciones para darse de baja deben proporcionarse a intervalos regulares y al menos una vez al mes.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cuando todos los materiales de tu solicitud estén listos, Braze enviará la solicitud a nuestros proveedores en tu nombre. A continuación, la solicitud es revisada y aprobada por los operadores locales, quienes pueden proporcionar comentarios adicionales o solicitar información adicional. Una vez que todos los operadores hayan dado su aprobación, podrás configurar inmediatamente el código abreviado para su uso en Braze.

El plazo para la revisión y aprobación de los códigos abreviados varía, pero suele tardar entre 4 y 12 semanas, dependiendo del país y la naturaleza del programa.

{% alert important %}
Si ya tienes tu propio código abreviado, ponte en contacto con tu administrador del éxito del cliente durante el proceso de incorporación para hablar sobre la migración o transferencia de tu código abreviado.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### Códigos largos SMS (10DLC) y números gratuitos

En muchos países, la configuración de códigos largos (también llamados «10DLC» o «códigos largos de 10 dígitos») y números gratuitos para el envío de SMS ha pasado de ser un proceso «plug and play» a un sistema de verificación regulado. Los operadores quieren saber exactamente quién eres y qué piensas decir antes de enviar el mensaje.

Durante el largo proceso de configuración del código largo, se te pedirá que compartas detalles sobre la identidad de tu marca y la intención de tu campaña.

#### Identidad de marca

- **Nombre de la entidad jurídica:** Debe coincidir exactamente con tus documentos fiscales (por ejemplo, «Acme Corp LLC» y no «Acme»).
- **Número de ID fiscal:** En EE. UU., este es tu número de identificación patronal (EIN). A nivel internacional, necesitarás un número de Impuesto sobre el Valor Añadido (IVA) o un Número de Registro Mercantil (BRN) local.
- **Presencia digital:** Un sitio web en vivo y funcional. Los operadores pueden comprobar esto para confirmar que no eres una empresa «ficticia».
- **Contacto autorizado:** Nombre, correo electrónico y número de teléfono de la persona responsable de la cuenta.

#### Intensión de la campaña

- **Casos de uso:** Indica si envías códigos 2FA, recordatorios de citas, promociones de marketing u otros.
- **Ejemplos de mensajes:** Proporciona entre 2 y 5 ejemplos de lo que enviarás.
- **Prueba de adhesión voluntaria:** Describe (y, a menudo, muestra una captura de pantalla) cómo se registra un usuario. Algunos ejemplos son un formulario Web con una casilla de verificación o la palabra clave «Text START» en un cartel.

Braze colaborará contigo para recopilar toda la información necesaria para proporcionar tu código largo o número gratuito, y luego enviará los datos a nuestro proveedor para su revisión y aprobación. Una vez que nuestro proveedor aprueba el programa, configuramos inmediatamente el código largo o el número gratuito en Braze.

El plazo de configuración depende del país de aprovisionamiento. Por lo general, los códigos largos y los números gratuitos tardan entre 1 y 4 semanas en ser aprobados.

{% alert important %}
Todos los clientes que actualmente tengan y/o utilicen códigos largos estadounidenses para enviar mensajes a clientes estadounidenses deben realizar el registro de sus códigos largos. Para obtener más información sobre los detalles del registro A2P 10DLC en EE. UU. y por qué es necesario, visita nuestro [artículo]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/) dedicado [al 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### ID alfanumérico del remitente de SMS

Los ID alfanuméricos de remitente están muy regulados porque pueden falsificarse fácilmente para realizar phishing. Mientras que algunos países permiten que cualquiera pueda crear y enviar desde un nombre, en muchos otros primero debes demostrar que eres el propietario de la marca.

Es posible que se te soliciten los siguientes datos para configurar un ID de remitente alfanumérico.

- **ID preferido:** Una cadena de hasta 11 caracteres. Debe contener al menos una letra y no puede ser una palabra genérica como «BANCO» o «INFO».
- **Prueba de propiedad de la marca:** Tu certificado de marca registrada o un documento de registro comercial (por ejemplo, un certificado de constitución emitido en los últimos 12 meses).
- **Carta de autorización:** Una carta firmada con el membrete de tu empresa en la que se autorice a Braze y a nuestro proveedor a enviar mensajes en tu nombre utilizando ese ID específico.
- **Plantillas de mensajes de ejemplo:** En varias regiones, debes realizar el registro de las «plantillas» exactas de los mensajes que pretendes enviar. Las desviaciones en los mensajes reales pueden provocar fallos en la entrega en esos países.

El plazo para configurar un ID de remitente alfanumérico depende en gran medida de si el país permite la configuración «dinámica» (inmediata, sin necesidad de registro) o si exige un «registro previo». En los países que exigen un registro previo, el plazo de configuración varía, pero suele tardar entre 1 y 4 semanas.

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

Para obtener respuestas a las preguntas frecuentes sobre los remitentes de SMS y RCS, consulta nuestra página [de preguntas frecuentes ]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions)sobre [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).