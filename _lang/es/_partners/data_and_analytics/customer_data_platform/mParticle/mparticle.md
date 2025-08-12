---
nav_title: mParticle de Rokt
article_title: mParticle de Rokt
alias: /partners/mparticle/
description: "Este artículo de referencia describe la asociación entre Braze y mParticle, una plataforma de datos de clientes que recopila y encamina información entre fuentes de su pila de marketing."
page_type: partner
search_tag: Partner

---

# mParticle de Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Con la plataforma de datos de clientes de mParticle, podrás hacer mucho más con tus datos. Los especialistas en marketing más sofisticados utilizan mParticle para orquestar los datos de toda su stack de crecimiento, lo que les habilita para ganar en los momentos clave del recorrido del cliente.

La integración de Braze y mParticle permite controlar a la perfección el flujo de información entre ambos sistemas:
- Sincroniza las audiencias de mParticle con Braze para la segmentación de campañas Braze y Canvas.
- Comparte datos entre las dos plataformas. Esto puede hacerse mediante la integración del kit mParticle y la integración de servidor a servidor.
- [Envía la interacción del usuario Braze a mParticle a través de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), haciéndola procesable en todo el stack de crecimiento. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta mParticle | Se necesita una [cuenta mParticle](https://app.mparticle.com/login) para beneficiarse de esta asociación. |
| instancia de Braze | Puedes encontrar tu instancia de Braze en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints) (por ejemplo, `US-01` o `US-02`). |
| Clave de identificación de la aplicación Braze | La clave de identificación de tu aplicación. <br><br>Se encuentra en el **panel de Braze > Administrar configuración > Clave de API**. |
| Clave API REST del espacio de trabajo | (De servidor a servidor) Una clave de API REST Braze<br><br>Puede crearse en el **panel de Braze > Consola para desarrolladores > Configuración de API > Clave de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Audiencias

Utilice la asociación de Braze y mParticle para configurar su integración e importar audiencias de mParticle directamente a Braze para retargeting, creando un bucle completo de datos de un sistema a otro. Cualquier integración que establezca contará para el volumen de puntos de datos de su cuenta.

#### Reenviar audiencias

mParticle ofrece tres formas de establecer los atributos de pertenencia a la cohorte, controlados por el ajuste de configuración "[Enviar segmentos como](#send_settings)". Consulte las secciones siguientes para conocer el tratamiento de cada opción:

- [Atributo de cadena única](#string)
- [Atributo de matriz única](#array)
- [Un atributo por segmento](#per-segment)
- [Atributo de matriz única y atributo de cadena única](#both-1)
- [Un único atributo de matriz y un atributo por segmento](#both-2)
- [Atributo de cadena única y un atributo por segmento](#both-3)
- [Atributo de matriz única, atributo de cadena única y un atributo por segmento](#multi)

##### Atributo de cadena única {#string}

mParticle creará un único atributo personalizado llamado `SegmentMembership`. El valor de este atributo es una cadena de identificadores de audiencia mParticle separados por comas que coinciden con el usuario. Estos ID de audiencia se pueden encontrar en el panel de control de mParticle en **Audiencias**.

Por ejemplo, si una audiencia mParticle "Ibiza dreamers" tiene un ID de audiencia de "11036", puede segmentar estos usuarios con el filtro `SegmentMembership` - `matches regex` - `11036`.

Aunque esta es la opción predeterminada en mParticle, la mayoría de los usuarios de Braze optan por utilizar [atributos de matriz única](#array) para la experiencia de filtrado al crear segmentos en Braze.

{% alert important %}
Esta solución no es recomendable si tiene más de unos pocos públicos porque los atributos personalizados pueden tener hasta 255 caracteres, por lo que no podrá almacenar docenas o cientos de públicos en un perfil de usuario utilizando este método. Si tiene un gran número de cohortes por usuario, le recomendamos encarecidamente la configuración "un atributo por segmento".
{% endalert %}

![Membresía del segmento mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Atributo de matriz única {#array}

mParticle crea un único atributo de matriz personalizado en Braze para cada usuario, denominado `SegmentMembershipArray`. El valor de este atributo es una matriz de identificadores de audiencia mParticle que coinciden con el usuario.

Por ejemplo, si un usuario es miembro de tres audiencias mParticle con los ID de audiencia "13053", "13052" y "13051", puede segmentar a los usuarios que coincidan con una de esas audiencias con el filtro `SegmentMembershipArray` - `includes value` - `13051`.

{% alert note %}
Los atributos de la matriz Braze tienen una longitud máxima de 25. Si alguno de tus usuarios es miembro de más de 25 audiencias, la información de afiliación será truncada por Braze. Para solucionar este problema, póngase en contacto con su representante de Braze para aumentar el umbral de longitud máxima de la matriz.
{% endalert %}

##### Un atributo por segmento {#per-segment}

mParticle creará un atributo booleano personalizado para cada público al que pertenezca un usuario. Por ejemplo, si una audiencia de mParticle se llama "Posibles parisinos", puedes segmentar a estos usuarios con el filtro `In Possible Parisians` - `equals` - `true`.

![mParticle atributo personalizado]({% image_buster /assets/img_archive/mparticle2.png %})

##### Atributo de matriz única y atributo de cadena única {#both-1}

mParticle enviará los atributos tal y como se describen tanto en el atributo de matriz única como en el atributo de cadena única.

##### Un único atributo de matriz y un atributo por segmento {#both-2}

mParticle enviará los atributos tal y como se describen tanto un único atributo de matriz como un atributo por segmento.

##### Atributo de cadena única y un atributo por segmento {#both-3}

mParticle enviará los atributos tal y como se describen tanto en una sola cadena de atributos como en un atributo por segmento.

##### Atributo de matriz única, atributo de cadena única y un atributo por segmento {#multi}

mParticle enviará atributos tal y como se describen en un único atributo de matriz, un único atributo de cadena y un atributo por segmento.

#### Paso 1: Crear un público en mParticle {#send_settings}

Para crear un público en mParticle:

1. Vaya a **Audiencias** > **Espacio de trabajo único** > **\+ Nueva audiencia**.
2. Para conectar Braze como una salida para su público, debe proporcionar los siguientes campos:

| Nombre del campo               | Descripción                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clave de API                  | Se encuentra en el panel de control de Braze en **Configuración** > **Claves API**.<br><br>Si utilizas la navegación anterior, puedes encontrar las claves de API en **Consola de desarrollador** > **Configuración de API**. |
| Sistema operativo de la clave de API | Selecciona a qué sistema operativo corresponde tu clave de API Braze. Esta selección limitará los tipos de tokens push reenviados en una actualización de audiencia.                          |
| Enviar segmentos como         | El método de envío de audiencias a Braze. Para más detalles, consulta la sección [Reenviar audiencias](#forwarding-audiences).                                                          |
| Clave API REST del espacio de trabajo   | Clave Braze REST API con permisos completos. Puede crearse en el panel Braze desde **Configuración** > **Claves API**.                                                        |
| Tipo de identidad externa   | El tipo de identidad de usuario mParticle a reenviar como ID externo a Braze. Recomendamos dejarlo con el valor predeterminado, ID de cliente.                                          |
| Tipo de identidad del correo electrónico      | El tipo de identidad de usuario mParticle a reenviar como correo electrónico a Braze.                                                                                                            |
| Instancia de soldadura           | Especifique a qué clúster se reenviarán sus datos Braze.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Por último, **guarda** tu audiencia.

Deberías empezar a ver audiencias sincronizándose con Braze en unos minutos. La pertenencia a la audiencia sólo se actualizará para los usuarios con `external_ids` (es decir, no para los usuarios anónimos). Para obtener más información sobre la creación de la audiencia Braze mParticle, consulta la documentación de mParticle sobre [los ajustes de configuración](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Paso 2: Segmentar usuarios en Braze

En Braze, para crear un segmento de estos usuarios, vaya a **Segmentos** en **Compromiso** y asigne un nombre a su segmento. A continuación se muestran dos ejemplos de segmentos en función de la opción seleccionada para **Enviar segmentos como**. Para más detalles sobre cada opción, consulta [Reenviar audiencias](#forwarding-audiences.)

- **Atributo de matriz única:** Seleccione `SegmentMembershipArray` como filtro. A continuación, utiliza la opción "incluye valor" e introduce el ID de audiencia que desees. ![mParticle filtro de segmento "SegmentMembershipArray" configurado como "incluye valor" e ID de audiencia.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Un atributo por segmento:** Seleccione su atributo personalizado como filtro. A continuación, utiliza la opción "igual" y elige la lógica adecuada. ![mFiltro de segmento de partículas "en posibles paris" configurado como "igual" y "verdadero".]({% image_buster /assets/img_archive/mparticle3.png %})

Una vez guardado, puede hacer referencia a este segmento durante la creación de Canvas o campañas en el paso de segmentación de usuarios.

#### Desactivar y eliminar conexiones

Dado que mParticle no mantiene directamente los segmentos en Braze, no eliminará los segmentos cuando se elimine o desactive la conexión de público de mParticle correspondiente. Cuando esto sucede, mParticle no actualizará los atributos de usuario de la audiencia en Braze para eliminar la audiencia de cada usuario.

Para eliminar la audiencia de un usuario Braze antes de borrarla, ajusta los filtros de audiencia para forzar el tamaño de la audiencia a 0 antes de borrar una audiencia. Cuando el cálculo de la audiencia se haya completado y devuelva 0 usuarios, borra la audiencia. A continuación, el número de miembros de la audiencia se actualizará en Braze a `false` para la opción de atributo único o elimina el ID de audiencia del formato de matriz.

## Mapeado de datos

Los datos pueden mapearse en Braze utilizando el [kit de integración incrustado](#embedded-kit-integration) si quieres conectar tus aplicaciones móviles y Web a Braze a través de mParticle. También puede utilizar la [integración API de servidor a servidor](#server-api-integration) para reenviar datos del lado del servidor a Braze.

Independientemente del enfoque que elija, debe configurar Braze como salida:

### Configura tus ajustes de salida Braze

En mParticle, vaya a **Configuración > Salidas > Añadir salidas** y seleccione **Braze** para abrir la configuración del kit Braze. **Guárdalo** cuando lo hayas completado.

| Nombre de la configuración | Descripción |
| ------------ | ----------- |
| Clave de identificación de la aplicación Braze | La clave de identificación de tu aplicación Braze se encuentra en el panel Braze, en **Configuración** > **Claves API**. Ten en cuenta que las claves de API serán diferentes para cada plataforma (iOS, Android y Web). |
| Tipo de identidad externa | El tipo de identidad de usuario mParticle a reenviar como ID externo a Braze. Recomendamos dejarlo con el valor predeterminado, ID de cliente |
| Tipo de identidad del correo electrónico | El tipo de identidad de usuario mParticle a reenviar como correo electrónico a Braze. Recomendamos dejarlo en el valor predeterminado, Correo electrónico, |
| Instancia de soldadura | El clúster al que se reenviarán sus datos Braze; debería ser el mismo clúster en el que se encuentra su cuadro de mandos. |
| Activar el reenvío de flujos de eventos | (Servidor a servidor) Si se activa, todos los eventos se reenviarán en tiempo real. Si no, todos los eventos se reenviarán en bloque. Cuando decida activar el reenvío de flujos de eventos, asegúrese de que los datos que pasa a Braze respetan [los límites de velocidad]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integración de kits integrados

El SDK de mParticle y Braze estará presente en tu aplicación a través de la integración del kit embebido. Sin embargo, a diferencia de una integración directa con Braze, mParticle se encarga de llamar a la mayoría de los métodos del SDK de Braze por ti. Los métodos de mParticle que utilices para hacer un seguimiento de los datos de usuario se mapearán automáticamente con los métodos del SDK de Braze. 

Estos mapeos del SDK de mParticle para [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) y [Web](https://github.com/Appboy/integration-appboy) son de código abierto y se pueden encontrar en LA [página de GitHub de mParticle](https://github.com/mparticle-integrations). 

La integración del SDK del kit incrustado le permite aprovechar nuestro conjunto completo de funciones (push, mensajes dentro de la aplicación y todo el seguimiento analítico de mensajes pertinente).

{% alert note %}
Para las tarjetas de contenido y las integraciones personalizadas de mensajes dentro de la aplicación, llame directamente a los métodos del SDK de Braze.
{% endalert %}

#### Paso 1: Integrar los SDK de mParticle

Integra los SDK de mParticle adecuados en tu aplicación en función de las necesidades de tu plataforma:

* [mParticle para Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle para iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle para Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Paso 2: Integración completa del kit de eventos Braze de mParticle

Aunque no es necesario incluir directamente el SDK de Braze en su sitio web o aplicación para esta integración de mParticle, debe instalarse el siguiente Kit Appboy de mParticle para reenviar los datos de su aplicación a Braze.

La [guía de integración del kit de eventos Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle le guiará a través de las instrucciones de alineación personalizada de mParticle y Braze en función de sus necesidades de mensajería (Push, seguimiento de ubicación, etc.).

#### Paso 3: Configuración de las conexiones para su salida Braze

En mParticle, vaya a **Conexiones > Conectar > [Su plataforma deseada] > Conectar salida** para añadir Braze como salida. **Guárdalo** cuando lo hayas completado.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para obtener un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulte [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Integración de la API del servidor

Se trata de un complemento para enrutar tus datos de backend a Braze si utilizas los SDK del lado del servidor de mParticle (por ejemplo, Ruby, Python, etc.). Para configurar esta integración de servidor a servidor con Braze, siga [la documentación de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
La integración de servidor a servidor no es compatible con las funciones de la interfaz de usuario Braze, como la mensajería dentro de la aplicación, las tarjetas de contenido o las notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles a través de este método. 

Considera una integración en paralelo si deseas utilizar estas características.

Para que los datos del servidor se reenvíen a Braze, deben incluir un `external_id`; los usuarios anónimos no serán reenviados.
{% endalert %}

#### Configuración de las conexiones para su salida Braze

En mParticle, vaya a **Conexiones > Conectar > [Su plataforma deseada] > Conectar salida** para añadir Braze como salida. **Guárdalo** cuando lo hayas completado. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para obtener un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulte [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Antes de habilitar "Atributos de usuario enriquecidos" o "Identidades de usuario enriquecidas", te recomendamos que revises los [excedentes de puntos de datos](#potential-data-point-overages) para asegurarte de que eres consciente de cómo afectarán estas configuraciones al uso de puntos de datos.

### Detalles de la asignación de datos

#### Tipos de datos
No todos los tipos de datos son compatibles entre ambas plataformas.
- [Las propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) admiten objetos de cadena, numéricos, booleanos o de fecha. No admite matrices ni objetos anidados.
- [Los atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) admiten objetos de cadena, numéricos, booleanos, de fecha y matrices, pero no admiten objetos ni objetos anidados. 

{% alert note %}
Braze no admite marcas de tiempo anteriores al año 0 ni posteriores al año 3000 en los atributos personalizados de tipo `Time`. Braze ingerirá estos valores cuando sean enviados por mParticle pero el valor será almacenado como una cadena.
{% endalert %}

#### Mapeado de datos

| Tipo de datos mParticle | Tipo de datos Braze | Descripción |
| ------------------- | --------------- | ----------- |
| Atributos de usuario (reservados) | Atributo estándar | Por ejemplo, la clave de atributo de usuario reservada `$FirstName` de mParticle se asigna al campo de atributo estándar `first_name` para Braze. |
| Atributos del usuario (otros) | Atributo personalizado | Cualquier atributo de usuario pasado a mParticle que caiga fuera de sus claves de atributo de usuario reservadas se registra en Braze como un atributo personalizado.<br><br>Los atributos de usuario admiten cadenas, números, booleanos, fechas y matrices, pero no objetos ni objetos anidados. |
| Evento personalizado | Evento personalizado | Los eventos personalizados de mParticle son reconocidos por Braze como eventos personalizados. Los atributos de evento se reenvían como propiedades de evento personalizadas.<br><br>Los atributos de evento pasados a Braze como propiedades de evento admiten objetos de cadena, numéricos, booleanos o de fecha, pero no admiten matrices ni objetos anidados. |
| Comprar evento de comercio | Evento de compra | Los eventos de comercio de compra serán mapeados a eventos de compra Braze. <br><br>Conmute el valor de configuración de los datos de eventos de comercio por lotes para registrar las compras a nivel de pedido o a nivel de producto. Por ejemplo, si `false`, un único evento entrante con dos productos, promociones o impresiones únicos daría lugar al menos a dos eventos Braze salientes. Si se establece en `true`, daría lugar a un único evento saliente con una matriz anidada de productos, promociones o impresiones, respectivamente.<br><br>Para más información sobre los campos de comercio adicionales que se registrarán, consulta [la documentación de mParticle.](https://docs.mparticle.com/integrations/braze/event/#purchase-events) <br><br>Al establecer "bundle commerce event data" como `false` atributos de producto pasados a Braze como propiedades de evento de compra, admite objetos de cadena, numéricos, booleanos o de fecha, pero no admite matrices ni objetos anidados.|
| Todos los demás eventos comerciales | Evento personalizado | Todos los demás eventos de comercio se asignarán a eventos personalizados. <br><br>Conmute el valor de configuración de los datos de eventos de comercio por lotes para registrar las compras a nivel de pedido o a nivel de producto. Por ejemplo, si `false`, un único evento entrante con dos productos, promociones o impresiones únicos daría lugar al menos a dos eventos Braze salientes. Si se establece en `true`, daría lugar a un único evento saliente con una matriz anidada de productos, promociones o impresiones, respectivamente.<br><br>Además de ciertos valores de comercio por defecto, los atributos de producto se registrarán como propiedades de evento Braze. Para más información sobre los campos de comercio adicionales que se registrarán, consulta [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Al configurar "bundle commerce event data" como `false` los atributos de producto pasados a Braze como propiedades de evento, admiten objetos de cadena, numéricos, booleanos o de fecha, pero no admiten matrices ni objetos anidados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Asignación de identidades de usuario
Para cada salida de mParticle, puede seleccionar el tipo de identidad externa que desea enviar a Braze como `external_id`. Aunque el valor predeterminado es el ID de cliente, puedes elegir mapear otro ID, como `MPID`, para enviarlo a Braze como `external_id`. Tenga en cuenta que la elección de un identificador distinto del ID de cliente puede influir en la forma en que se envían los datos en Braze. 

Por ejemplo, la asignación de MPID a su Braze `external_id` tendrá los siguientes efectos:
- Debido a la naturaleza del momento en que se asigna el MPID, a todos los usuarios se les asignará un `external_id` al iniciar la sesión.
- La configuración de Currents puede requerir un mapeado adicional debido a los diferentes tipos de datos entre MPID y `external_id`.

### Transmisión de las solicitudes de supresión (solicitudes de los interesados)

Reenvía las solicitudes de borrado a Braze configurando una salida de solicitud del interesado a Braze. Para enviar solicitudes de borrado a Braze, sigue [la documentación de mParticle.](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)

## Posibles excesos de puntos de datos

### Atributos de usuario enriquecidos

#### Activación del enriquecimiento de atributos/identidades de usuario (sólo de servidor a servidor) {#enriched}

En los ajustes de conexión de mParticle, Braze recomienda desactivar **Incluir atributos de usuario enriquecidos**. Si se activa, mParticle reenviará todos los atributos de usuario disponibles (como atributos estándar, atributos personalizados y atributos calculados) del perfil existente a Braze en cada evento registrado. Esto resultará en un alto consumo de puntos de datos ya que mParticle enviará a Braze los mismos atributos sin cambiar en cada llamada.

Por ejemplo, si un usuario añade su nombre, apellidos y número de teléfono durante su primera sesión y más tarde se suscribe a un boletín de noticias añadiendo la misma información, además del correo electrónico, se desencadena un evento de suscripción al boletín de noticias:
- Si está activada (por defecto), se incurrirá en cinco puntos de datos. (evento de registro, dirección de correo electrónico, nombre, apellidos y número de teléfono).
- Si se desactiva, se producirán dos puntos de datos (evento de registro y dirección de correo electrónico)

{% alert note %}
Si desactivas esta opción, no se comprobarán los cambios de datos. Sin embargo, impedirá que la integración envíe todos los atributos de usuario del perfil del usuario que no se recibieron en el lote de entrada original o no se establecieron explícitamente como un atributo para el evento. Es importante seguir comprobando que sólo se pasan deltas a Braze.
{% endalert %}

#### Consideraciones para desactivar los atributos de usuario enriquecidos

Hay algunas consideraciones a tener en cuenta al desactivar **Incluir atributos de usuario enriquecidos**:
1. La integración de servidor a servidor utiliza la API de eventos de mParticle para enviar eventos a Braze. Cada solicitud es desencadenada por un evento. Cuando se cambia un atributo de usuario, como la actualización de una dirección de correo electrónico, pero no está asociado a un evento específico (por ejemplo, un evento personalizado de actualización de perfil), el nuevo valor sólo se pasa a una salida como Braze como un "atributo enriquecido" en la carga útil del siguiente evento activado por el usuario. Cuando **Incluir atributos de usuario enriquecidos** está desactivado, este nuevo valor de atributo no asociado a un evento específico no se pasará a Braze.
  - Para solucionarlo, recomendamos crear un evento "atributo de usuario actualizado" independiente que sólo envíe a Braze los atributos de usuario específicos que se han actualizado. Tenga en cuenta que con este enfoque, todavía está registrando un punto de datos adicional para el evento "atributo de usuario actualizado", pero el consumo de puntos de datos será mucho menor que el envío de todos los atributos de usuario en cada llamada con la función activada.
2. Los atributos calculados se transmiten a Braze como atributos de usuario enriquecidos, por lo que si se desactiva "Atributos de usuario enriquecidos" dejarán de transmitirse a Braze. Para enviar atributos calculados a Braze cuando "Atributos de usuario enriquecidos" están desactivados, una [alimentación de atributos calculados](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) podría ayudar sin empujar todos los atributos. La fuente enviará una actualización a Braze cuando cambie un atributo calculado. 

### Envío de datos innecesarios o duplicados a Braze
Braze cuenta un punto de datos cada vez que se pasa un atributo a Braze, aunque el valor no cambie. Por este motivo, Braze recomienda reenviar únicamente los datos necesarios para actuar dentro de Braze y asegurarse de que sólo se transmiten deltas de atributos.

