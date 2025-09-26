---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Este artículo de referencia describe la asociación entre Braze y Tealium, un centro de datos universal que te habilita para conectar datos móviles, Web y alternativos con otras fuentes de terceros."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) es un motor de segmentación de clientes omnicanal y de acción en tiempo real. AudienceStream toma los datos que fluyen hacia EventStream y crea perfiles de visitantes que representan los atributos más importantes de la interacción de tus clientes con tu marca. 

La integración de Braze y Tealium aprovecha los perfiles de visitantes de AudienceStream. Los comportamientos compartidos segmentan estos perfiles para crear conjuntos de visitantes con rasgos comunes, conocidos como audiencias. Estas audiencias pueden ayudar a alimentar tu stack tecnológico de marketing en tiempo real mediante conectores. 

{% alert important %}
Tealium AudienceStreams y EventStreams ofrecen acciones de conector por lotes y no por lotes. El conector no por lotes debe utilizarse cuando las solicitudes en tiempo real sean importantes para el caso de uso y no haya preocupación por superar las especificaciones del límite de velocidad de la API de Braze. Ponte en contacto con [el soporte de]({{site.baseurl}}/braze_support/) Braze o con tu administrador del éxito del cliente si tienes alguna pregunta.
{% endalert %}

## Requisitos previos

| Apellidos | Descripción |
| ---- | ----------- |
| Cuenta Tealium | Se necesita una [cuenta Tealium](https://my.tealiumiq.com/) con acceso al servidor. Recomendamos utilizar también las integraciones del lado del cliente para aprovechar esta asociación. |
| Clave de API REST | Una clave de API REST Braze con permisos `users.track`, `users.delete`, y `subscription.status.set`.<br><br>Se puede crear en **el panel de Braze > Consola para desarrolladores > Clave de API REST > Crear nueva clave de API**|
| [Punto final REST Braze]({{site.baseurl}}/api/basics/#endpoints) | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Configurar atributos y señales

#### Comprensión de los atributos

El primer paso para utilizar AudienceStream es crear atributos. Los atributos te permiten definir las características importantes que representan los hábitos, preferencias, acciones e interacción de un visitante con tu marca. 

**Atributos de la visita**: Los atributos de visita se refieren a la visita (o sesión) actual del usuario. Los datos almacenados en estos atributos persisten mientras dura la visita. Algunos ejemplos de atributos de visita son:
- Duración de la visita (número)
- Navegador actual (cadena)
- Dispositivo de corriente (cadena)
- Número de páginas vistas

**Atributos del visitante**: Los atributos de los visitantes se refieren al usuario actual. Los datos almacenados en estos atributos persisten durante toda la vida del usuario. Algunos ejemplos de atributos del visitante son: 
- Valor de duración del pedido (Número)
- Nombre (cadena)
- Fecha de nacimiento
- Compras/Marcas (Tally)

Visita [Tealium](https://docs.tealium.com/server-side/attributes/about/) para consultar la lista completa de tipos de datos disponibles.

##### Enriquecimiento de atributos

Una vez identificados los atributos deseados, puedes configurarlos con [enriquecimientos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/): reglas empresariales que determinan cuándo y cómo actualizar los valores de los atributos. Cada tipo de dato ofrece su propia selección de enriquecimientos para manipular el valor del atributo. Está asociado a la configuración "CUANDO". Las siguientes opciones están disponibles para cada atributo de visita y visitante:

- Nuevo visitante: se produce la primera vez que un visitante entra en tu sitio.
- Nueva visita: se produce en una nueva visita de un visitante.
- Cualquier suceso: se produce en cualquier suceso.
- Visita finalizada: se produce cuando termina una visita.

También puedes crear una condición personalizada, llamada regla, que determinará cuándo se producirá el enriquecimiento.

#### Señales

Las señales son atributos especiales de los visitantes que representan patrones de comportamiento valiosos. Las señales se asignan o retiran a los visitantes en función de la lógica de sus enriquecimientos. Esta lógica suele combinar varias condiciones para captar segmentos de visitantes o establece un umbral para cuando se alcanza un valor concreto.

#### Ejemplo de atributo y señal

{% tabs local %}
{% tab Atributo %}

Crea un atributo de visitante "Valor de duración del pedido" que calcule el importe acumulado gastado (`order_total`) por el cliente para todos los pedidos completados (evento de compra). Para configurar el valor de duración del pedido en tu cuenta de Tealium, sigue las siguientes instrucciones:

1. Ve a **AudienceStream > Atributos de visitantes/visitas** y haz clic en **Añadir atributo**.
2. Selecciona el ámbito como **Visitante** y haz clic en **Continuar**.
3. Selecciona el tipo de dato **Número** y haz clic en **Continuar**.
4. Introduce el nombre del atributo, "Valor de duración del pedido".
5. Haz clic en **Añadir enriquecimiento** y selecciona **Aumentar o Disminuir número**.
6. Selecciona el atributo que contiene el valor a incrementar (`order_total`).
7. Deja "CUANDO" en "Cualquier suceso" y, a continuación, haz clic en **Crear una nueva regla**.
8. Crea una regla que identifique cuándo se ha producido un evento de compra.
9. Haz clic en **Guardar** y luego en **Finalizar**.

Ahora, todos los clientes tendrán un atributo de valor de duración del pedido vinculado a ellos.

{% endtab %}
{% tab Señal %}

Puedes crear señales que te ayuden a clasificar y dirigirte a tus usuarios por determinados atributos que comparten. En el siguiente ejemplo, creamos una señal VIP para usuarios con un "Valor de pedido de por vida" superior a 500 $.

1. Ve a **AudienceStream > Atributos de visitantes/visitas** y haz clic en **Añadir atributo**.
2. Selecciona el ámbito como **Visitante** y haz clic en **Continuar**.
3. Selecciona el tipo de datos **Señal** y haz clic en **Continuar**.
4. Introduce el nombre de la señal, "VIP".
5. Haz clic en **Añadir enriquecimiento** y selecciona **Asignar señal**.
6. Deja "CUANDO" en "Cualquier evento".
7. Crea una regla para asignar señales seleccionando **Crear regla**. Asigna un título a esta regla y, utilizando el atributo creado anteriormente, establece la regla como "...tiene el atributo "Valor del pedido durante la vida útil superior a 500".
8. Haz clic en **Guardar** y luego en **Finalizar**.

{% endtab %}
{% endtabs %}

### Paso 2: Crear una audiencia

En la página de inicio de Tealium, selecciona **Audiencias** en **AudienceStream** en la barra lateral de navegación. Aquí puedes crear una audiencia de usuarios con atributos comunes. La entrada o salida de un usuario de esta audiencia será el desencadenante de la Acción desencadenante, configurada en el paso siguiente, que pasa esta información al perfil de usuario en Braze. 

En primer lugar, nombra a tu audiencia y, a continuación, considera qué atributos se aplicarían al tipo de audiencia que intentas crear. Por ejemplo, para crear una audiencia de usuarios VIP, podrías crear una audiencia de visitantes que tengan la **señal VIP**.

Asegúrate de **Guardar / Publicar** tu audiencia cuando hayas terminado.

### Paso 3: Crear un conector de eventos

Un conector es una integración entre Tealium y otro proveedor utilizada para transmitir datos. Estos conectores contienen acciones que representan las API compatibles de su socio. 

1. En la barra lateral de Tealium, en **el lado del servidor**, ve a **AudienceStream > Conectores de audiencia.**
2. Selecciona el botón azul **\+ Añadir conector** para buscar en el mercado de conectores. En el nuevo cuadro de diálogo que aparece, utiliza la búsqueda rápida para encontrar el conector **Braze**.
3. Para añadir este conector, haz clic en la ficha del conector **Braze**. Al hacer clic, puedes ver el resumen de la conexión y una lista de la información necesaria, las acciones admitidas y las instrucciones de configuración. La configuración consta de tres pasos: origen, configuración y acción.

#### Fuente

En el cuadro de diálogo **Fuente** que aparece, selecciona la audiencia que creaste en el paso anterior y un desencadenante que consideres adecuado para tu situación. También puedes alternar el límite de frecuencia para controlar la frecuencia con la que se desencadena esta acción. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuración

A continuación, aparecerá un diálogo de **Configuración**. Selecciona **Añadir conector** en la parte inferior de la página. Da un nombre a tu conector y proporciona aquí tu punto final de la API Braze y tu clave de API REST Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si ya has creado antes un conector, puedes utilizar opcionalmente uno existente de la lista de conectores disponibles y modificarlo para adaptarlo a tus necesidades con el icono del lápiz o eliminarlo con el icono de la papelera. 

Cuando hayas creado o seleccionado un conector para vincular esta audiencia, haz clic en Listo para continuar.

#### Acción

A continuación, asigna un nombre a tu acción de conector y selecciona un tipo de acción que envíe datos según el mapeado que configures. Aquí mapearás atributos Braze con nombres de atributos Tealium. Dependiendo del tipo de acción que elijas, habrá una selección variada de campos requeridos por Tealium. A continuación se dan ejemplos y explicaciones de estos campos.

{% alert important %}
No todos los campos ofrecidos son obligatorios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Usuario de seguimiento - Lote y no lote %}

Esta acción le permite realizar un seguimiento de los atributos de usuario, evento y compra en una sola acción. Aunque la acción Seguir usuario es la misma para AudienceStream y EventStream, Tealium recomienda configurar los mapeados de atributos de usuario con acciones de AudienceStream y los mapeados de eventos y compras con acciones de EventStream.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utilice este campo para asignar el campo ID de usuario Tealium a su equivalente Braze. Asigna uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID Braze, Nombre de alias y Etiqueta de alias.<br><br>\- El ID externo y el ID Braze no deben especificarse si se importan tokens push.<br>\- Si se especifica un alias de usuario, deben establecerse el nombre y la etiqueta del alias. <br><br>Para más información, consulta el [punto final de `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Atributos del usuario | Utiliza los nombres de campo de perfil de usuario Braze existentes para actualizar los valores de perfil de usuario en el panel Braze o añade tus propios datos de [atributo]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personalizado de [usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) a los perfiles de usuario.<br><br>\- Por defecto, se crearán nuevos usuarios si no existe ninguno.<br>\- Si configura **Actualizar sólo existentes** en `true`, sólo se actualizarán los usuarios existentes y no se creará ningún usuario nuevo.<br>\- Si un atributo Tealium está vacío, se convertirá en nulo y se eliminará del perfil de usuario Braze. Los enriquecimientos deben utilizarse si no deben enviarse valores nulos a Braze para eliminar un atributo de usuario. |
| Modificar los atributos del usuario | Utilice este campo para aumentar o disminuir ciertos atributos de usuario<br><br>\- Los atributos enteros pueden incrementarse con enteros positivos o negativos.<br>\- Los atributos de las matrices pueden modificarse añadiendo o eliminando valores de las matrices existentes. |
| Evento | Un evento representa una ocurrencia única de un evento personalizado por un usuario particular en una marca de tiempo. Utilice este campo para rastrear y asignar atributos de evento como los del [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) Braze. <br><br>\- El atributo de evento `Name` es necesario para cada evento asignado.<br>\- El atributo de evento `Time` se establece automáticamente en now a menos que se asigne explícitamente. <br>\- Por defecto, se crearán nuevos eventos si no existe ninguno. Estableciendo `Update Existing Only` a `true`, sólo se actualizarán los eventos existentes, y no se creará ningún evento nuevo.<br>\- Mapa de atributos de tipo array para añadir múltiples eventos. Los atributos de tipo array deben tener la misma longitud.<br>\- Se pueden utilizar atributos de valor único y aplicarlos a cada evento. |
| Plantilla de eventos | Proporcionar plantillas de eventos a las que hacer referencia en los datos del cuerpo. Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze. Consulte la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información. |
| Variable de plantilla de evento | Proporcione variables de plantilla de eventos como entrada de datos. Consulte la [Guía de Variables de Plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
| Compra | Utilice este campo para rastrear y asignar atributos de compra del usuario como los del [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) Braze.<br><br>\- Los atributos de compra `Product ID`, `Currency` y `Price` son necesarios para cada compra mapeada.<br>\- El atributo de compra `Time` se establece automáticamente en now a menos que se asigne explícitamente.<br>\- Por defecto, se crearán nuevas compras si no existe ninguna. Si configura `Update Existing Only` en `true`, sólo se actualizarán las compras existentes y no se creará ninguna compra nueva.<br>\- Asignar atributos de tipo array para añadir múltiples artículos de compra. Los atributos de tipo array deben tener la misma longitud.<br>\- Se pueden utilizar atributos de valor único y se aplicarán a cada artículo.|
| Plantilla de compra | Las plantillas pueden utilizarse para transformar los datos antes de enviarlos a Braze.<br>\- Defina una plantilla de compra si necesita compatibilidad con objetos anidados.<br>\- Cuando se define una plantilla de compra, la configuración establecida en la sección de compras de su acción será ignorada.<br>\- Consulte la [Guía de plantillas](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium para obtener más información.|
| Variable del modelo de compra | Proporcione variables de plantilla de productos como entrada de datos. Consulte la [Guía de Variables de Plantilla](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium para obtener más información. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Eliminar usuario - No lote %}

Esta acción te permite eliminar usuarios del panel de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| ID de usuario | Utiliza este campo para mapear el campo ID de usuario de Tealium a su equivalente en Braze.<br><br>\- Mapea uno o más atributos de ID de usuario. Cuando se especifican varios ID, se elige el primer valor que no está en blanco según el siguiente orden de prioridad: ID externo, ID Braze, Nombre de alias y Etiqueta de alias.<br>\- Al especificar un alias de usuario, deben establecerse tanto el Nombre de alias como la Etiqueta de alias.<br><br>Para más información, consulta el [punto final `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Actualizar estado del grupo de suscripción del usuario - No por lotes %}
Esta acción te permite añadir o eliminar usuarios de los grupos de suscripción por SMS o correo electrónico de Braze.

| Parámetros | Descripción |
| ---------- | ----------- |
| Tipo de grupo | Utiliza este campo para indicar si se trata de un grupo de suscripción por SMS o correo electrónico. |
| Tipo de actualización | Mapea esta acción a un evento de cancelar suscripción o suscripción 
| Atributos | \- ID del grupo de suscripción (obligatorio): El ID del grupo de suscripción relacionado con el tipo de grupo mapeado en el campo anterior.<br>\- ID externo: El ID externo del usuario.<br><br>Correo electrónico específico del grupo:<br>\- Correo electrónico: La dirección de correo electrónico del usuario.<br>**Si el ID externo no está definido, se requerirá el correo electrónico.**<br><br>Específico del grupo SMS:<br>\- Teléfono: El número de teléfono en formato E.164. Por ejemplo, +14155552671.<br>**Si el ID externo no está definido, se requerirá el teléfono.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecciona **Finalizar**.

#### Resumen

Visualiza el resumen del conector que has creado. Si quieres modificar las opciones elegidas, selecciona **Atrás** para editar o **Finalizar** para terminar.

Tu conector aparece ahora en la lista de conectores de tu página de inicio de Tealium.

Asegúrate de guardar o publicar tu conector cuando hayas terminado. Las acciones que configuraste se dispararán ahora cuando se cumplan las conexiones desencadenantes. 

### Paso 4: Prueba tu conector Tealium

Una vez que el conector esté en funcionamiento, debes probarlo para asegurarte de que funciona correctamente. La forma más sencilla de comprobarlo es utilizar **la Herramienta de Rastreo de** Tealium. Para empezar a utilizar Trace, asegúrate de que has añadido la extensión de navegador Herramientas de Tealium.

1. Para iniciar un nuevo rastreo, selecciona **Rastreo** en la barra lateral, en Opciones **del lado del servidor**. Haga clic en **Iniciar** y capture el ID de Traza.
2. Abre la extensión del navegador e introduce el ID de rastreo en AudienceStream Trace.
3. Examina el registro en tiempo real.
4. Compruebe la acción que desea validar haciendo clic en la entrada **Acciones desencadenadas** para expandirla.
5. Busca la acción que quieras validar y visualiza el estado del registro. 

Consulta la [documentación de Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium para obtener instrucciones más detalladas sobre la aplicación de la herramienta Trace de Tealium.

## Demostración de integración

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Posibles excesos de puntos de datos

Hay tres formas principales en las que puedes incurrir accidentalmente en excedentes de datos al integrar Braze a través de Tealium:

#### Envío de datos duplicados - envía sólo deltas Braze de atributos
Tealium no envía deltas Braze de atributos de usuario. Por ejemplo, si tienes una acción EventStream que realiza un seguimiento del nombre, correo electrónico y número de móvil de un usuario, Tealium enviará los tres atributos a Braze cada vez que se desencadene la acción. Tealium no buscará lo que ha cambiado o se ha actualizado y sólo enviará esa información.<br><br> 
**Solución**: <br>Puede comprobar su backend para evaluar si un atributo ha cambiado o no y, en caso afirmativo, llamar a los métodos pertinentes de Tealium para actualizar el perfil del usuario. **Esto es lo que suelen hacer los usuarios que integran Braze directamente.** <br>**O**<br> Si no almacenas tu propia versión de un perfil de usuario en tu backend y no puedes saber si los atributos cambian o no, puedes utilizar AudienceStream y [crear enriquecimientos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar sólo los atributos de usuario cuando los valores hayan cambiado. 

#### Enviar datos irrelevantes o sobrescribir datos innecesariamente
Si tienes varios EventStreams dirigidos a la misma fuente de eventos, **todas las acciones habilitadas para ese conector** se dispararán automáticamente cada vez que se desencadene una sola acción, **lo que también podría provocar que los datos se sobrescribieran en Braze.**<br><br>
**Solución**: <br>Configure una especificación de evento o feed independiente para realizar un seguimiento de cada acción. <br>**O**<br> Desactiva las acciones (o conectores) que no quieras que se activen utilizando los botones del panel de control de Tealium.

#### Inicializar Braze demasiado pronto
Los usuarios que se integren con Tealium utilizando la etiqueta SDK de la Web de Braze pueden ver un aumento espectacular de sus MAU. **Si Braze se inicializa al cargar la página, Braze creará un perfil anónimo cada vez que un internauta navegue por el sitio web por primera vez.** Algunos pueden querer rastrear el comportamiento del usuario sólo cuando los usuarios han completado alguna acción, como "Iniciar sesión" o "Ver vídeo", para reducir su recuento de MAU. <br><br>
**Solución**: <br>Configure [reglas de carga](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exactamente cuándo y dónde se carga una etiqueta en su sitio.

