---
nav_title: mParticle de Rokt
article_title: mParticle de Rokt
alias: /partners/mparticle/
description: "Este artículo de referencia describe la asociación entre Braze y mParticle, una plataforma de datos de los clientes que recopila y encamina información entre fuentes de tu stack de marketing."
page_type: partner
search_tag: Partner

---

# mParticle de Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Con la plataforma de datos de los clientes de mParticle, podrás hacer mucho más con tus datos. Los especialistas en marketing más sofisticados utilizan mParticle para orquestar los datos de todo su stack de crecimiento, lo que les permite ganar en los momentos clave del recorrido del cliente.

La integración de Braze y mParticle te permite controlar fácilmente el flujo de información entre ambos sistemas:
- Sincroniza las audiencias de mParticle con Braze para la segmentación de campañas de Braze y Canvas.
- Comparte datos entre las dos plataformas. Esto puede hacerse mediante la integración del kit de mParticle y la integración de servidor a servidor.
- [Envía la interacción del usuario de Braze a mParticle a través de Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), haciéndola procesable en todo el stack de crecimiento. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de mParticle | Se necesita una [cuenta de mParticle](https://app.mparticle.com/login) para beneficiarse de esta asociación. |
| Instancia de Braze | Tu instancia de Braze se encuentra en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints) (por ejemplo, `US-01` o `US-02`). |
| Clave de identificación de la aplicación Braze | La clave de identificación de tu aplicación. <br><br>Puedes encontrarla en **Administrar configuración** > **Clave de API** en el panel de Braze. |
| Clave de API REST del espacio de trabajo | (De servidor a servidor) Una clave de API REST de Braze<br><br>Se puede crear en **Consola para desarrolladores** > **Configuración de API** > **Clave de API** en el panel de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Audiencias

Utiliza la asociación de Braze y mParticle para configurar tu integración e importar audiencias de mParticle directamente a Braze para reorientar, creando un bucle completo de datos de un sistema a otro. 

Cualquier integración que configures registrará puntos de datos. Si tienes alguna pregunta sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderte.

#### Reenviar audiencias

mParticle ofrece tres formas de establecer los atributos de pertenencia a la cohorte, controlados por el ajuste de configuración "[Enviar segmentos como](#send_settings)". Consulta las secciones siguientes para conocer el tratamiento de cada opción:

- [Atributo de cadena única](#string)
- [Atributo de matriz única](#array)
- [Un atributo por segmento](#per-segment)
- [Atributo de matriz única y atributo de cadena única](#both-1)
- [Atributo de matriz única y un atributo por segmento](#both-2)
- [Atributo de cadena única y un atributo por segmento](#both-3)
- [Atributo de matriz única, atributo de cadena única y un atributo por segmento](#multi)

##### Atributo de cadena única {#string}

mParticle creará un único atributo personalizado llamado `SegmentMembership`. El valor de este atributo es una cadena de ID de audiencia de mParticle separados por comas que coinciden con el usuario. Estos ID de audiencia se pueden encontrar en el dashboard de mParticle en **Audiencias**.

Por ejemplo, si una audiencia de mParticle "Ibiza dreamers" tiene un ID de audiencia de "11036", puedes segmentar estos usuarios con el filtro `SegmentMembership` — `matches regex` — `11036`.

Aunque esta es la opción predeterminada en mParticle, la mayoría de los usuarios de la empresa optan por utilizar [atributos de matriz única](#array) para la experiencia de filtrado al crear segmentos en Braze.

{% alert important %}
Esta solución no es recomendable si tienes más de unas pocas audiencias, porque los atributos personalizados pueden tener hasta 255 caracteres, por lo que no podrás almacenar docenas o cientos de audiencias en un perfil de usuario con este método. Si tienes un gran número de cohortes por usuario, te recomendamos encarecidamente la configuración "un atributo por segmento".
{% endalert %}

![Pertenencia al segmento de mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Atributo de matriz única {#array}

mParticle crea un único atributo de matriz personalizado en Braze para cada usuario, denominado `SegmentMembershipArray`. El valor de este atributo es una matriz de ID de audiencia de mParticle que coinciden con el usuario.

Por ejemplo, si un usuario es miembro de tres audiencias de mParticle con los ID de audiencia "13053", "13052" y "13051", puedes segmentar a los usuarios que coincidan con una de esas audiencias con el filtro `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
Los atributos de matriz de Braze tienen una longitud máxima de 25. Si alguno de tus usuarios es miembro de más de 25 audiencias, Braze truncará la información de pertenencia. Para solucionar este problema, ponte en contacto con tu representante de Braze para aumentar el umbral de longitud máxima de la matriz.
{% endalert %}

##### Un atributo por segmento {#per-segment}

mParticle creará un atributo personalizado Booleano para cada audiencia a la que pertenezca un usuario. Por ejemplo, si una audiencia de mParticle se llama "Possible Parisians", puedes segmentar a estos usuarios con el filtro `In Possible Parisians` - `equals` - `true`.

![Atributo personalizado de mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Atributo de matriz única y atributo de cadena única {#both-1}

mParticle enviará los atributos tal y como se describen tanto en el atributo de matriz única como en el atributo de cadena única.

##### Atributo de matriz única y un atributo por segmento {#both-2}

mParticle enviará los atributos tal y como se describen tanto en el atributo de matriz única como en un atributo por segmento.

##### Atributo de cadena única y un atributo por segmento {#both-3}

mParticle enviará los atributos tal y como se describen tanto en el atributo de cadena única como en un atributo por segmento.

##### Atributo de matriz única, atributo de cadena única y un atributo por segmento {#multi}

mParticle enviará los atributos tal y como se describen en el atributo de matriz única, el atributo de cadena única y un atributo por segmento.

#### Paso 1: Crear una audiencia en mParticle {#send_settings}

Para crear una audiencia en mParticle:

1. Ve a **Audiencias** > **Espacio de trabajo único** > **+ Nueva audiencia**.
2. Para conectar Braze como salida para tu audiencia, debes proporcionar los siguientes campos:

| Nombre del campo               | Descripción                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clave de API                  | Se encuentra en el panel de Braze en **Configuración** > **Claves de API**.<br><br>Si utilizas la navegación anterior, puedes encontrar las claves de API en **Consola para desarrolladores** > **Configuración de API**. |
| Sistema operativo de la clave de API | Selecciona a qué sistema operativo corresponde tu clave de API de Braze. Esta selección limitará los tipos de tokens push reenviados en una actualización de audiencia.                          |
| Enviar segmentos como         | El método de envío de audiencias a Braze. Para más detalles, consulta la sección [Reenviar audiencias](#forwarding-audiences).                                                          |
| Clave de API REST del espacio de trabajo   | Clave de API REST de Braze con permisos completos. Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**.                                                        |
| Tipo de identidad externa   | El tipo de identidad de usuario de mParticle que se reenviará como ID externo a Braze. Recomendamos dejarlo con el valor predeterminado, ID de cliente.                                          |
| Tipo de identidad del correo electrónico      | El tipo de identidad de usuario de mParticle que se reenviará como correo electrónico a Braze.                                                                                                            |
| Instancia de Braze           | Especifica a qué clúster se reenviarán tus datos de Braze.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3. Por último, **guarda** tu audiencia.

Deberías empezar a ver audiencias sincronizándose con Braze en unos minutos. La pertenencia a la audiencia solo se actualizará para los usuarios con `external_ids` (es decir, no para los usuarios anónimos). Para obtener más información sobre la creación de audiencias de Braze en mParticle, consulta la documentación de mParticle sobre [los ajustes de configuración](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Paso 2: Segmentar usuarios en Braze

En Braze, para crear un segmento de estos usuarios, ve a **Segmentos** en **Interacción** y asigna un nombre a tu segmento. A continuación se muestran dos ejemplos de segmentos en función de la opción seleccionada para **Enviar segmentos como**. Para más detalles sobre cada opción, consulta [Reenviar audiencias](#forwarding-audiences).

- **Atributo de matriz única:** Selecciona `SegmentMembershipArray` como filtro. A continuación, utiliza la opción "includes value" e introduce el ID de audiencia que desees. ![Filtro de segmento de mParticle "SegmentMembershipArray" configurado como "includes value" e ID de audiencia.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Un atributo por segmento:** Selecciona tu atributo personalizado como filtro. A continuación, utiliza la opción "equals" y elige la lógica adecuada. ![Filtro de segmento de mParticle "in possible parisians" configurado como "equals" y "true".]({% image_buster /assets/img_archive/mparticle3.png %})

Una vez guardado, puedes hacer referencia a este segmento durante la creación de Canvas o campañas en el paso de segmentación de usuarios.

#### Desactivar y eliminar conexiones

Como mParticle no mantiene directamente los segmentos en Braze, no eliminará los segmentos cuando se elimine o desactive la conexión de audiencia de mParticle correspondiente. Cuando esto sucede, mParticle no actualizará los atributos de usuario de la audiencia en Braze para eliminar la audiencia de cada usuario.

Para eliminar la audiencia de un usuario de Braze antes de borrarla, ajusta los filtros de audiencia para forzar el tamaño de la audiencia a 0 antes de eliminar una audiencia. Cuando el cálculo de la audiencia se haya completado y devuelva 0 usuarios, elimina la audiencia. Entonces, la pertenencia a la audiencia se actualizará en Braze a `false` para la opción de atributo único o se eliminará el ID de audiencia del formato de matriz.

## Mapeado de datos

Los datos pueden mapearse a Braze utilizando la [integración de kit incrustado](#embedded-kit-integration) si quieres conectar tus aplicaciones móviles y web a Braze a través de mParticle. También puedes utilizar la [integración de API de servidor a servidor](#server-api-integration) para reenviar datos del lado del servidor a Braze.

Independientemente del enfoque que elijas, debes configurar Braze como salida:

### Configura tus ajustes de salida de Braze

En mParticle, ve a **Configuración > Salidas > Añadir salidas** y selecciona **Braze** para abrir la configuración del kit de Braze. **Guárdalo** cuando lo hayas completado.

| Nombre de la configuración | Descripción |
| ------------ | ----------- |
| Clave de identificación de la aplicación Braze | La clave de identificación de tu aplicación Braze se encuentra en el panel de Braze, en **Configuración** > **Claves de API**. Ten en cuenta que las claves de API serán diferentes para cada plataforma (iOS, Android y Web). |
| Tipo de identidad externa | El tipo de identidad de usuario de mParticle que se reenviará como ID externo a Braze. Recomendamos dejarlo con el valor predeterminado, ID de cliente. |
| Tipo de identidad del correo electrónico | El tipo de identidad de usuario de mParticle que se reenviará como correo electrónico a Braze. Recomendamos dejarlo en el valor predeterminado, Correo electrónico. |
| Instancia de Braze | El clúster al que se reenviarán tus datos de Braze; debería ser el mismo clúster en el que se encuentra tu dashboard. |
| Habilitar el reenvío de flujos de eventos | (De servidor a servidor) Si se habilita, todos los eventos se reenviarán en tiempo real. Si no, todos los eventos se reenviarán en bloque. Cuando decidas habilitar el reenvío de flujos de eventos, asegúrate de que los datos que pasas a Braze respetan los [límites de velocidad]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integración de kit incrustado

Los SDK de mParticle y Braze estarán presentes en tu aplicación a través de la integración del kit incrustado. Sin embargo, a diferencia de una integración directa con Braze, mParticle se encarga de llamar a la mayoría de los métodos del SDK de Braze por ti. Los métodos de mParticle que utilices para hacer seguimiento de los datos de usuario se mapearán automáticamente con los métodos del SDK de Braze. 

Estos mapeados del SDK de mParticle para [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) y [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) son de código abierto y pueden encontrarse en [la página de GitHub de mParticle](https://github.com/mparticle-integrations). 

La integración del SDK del kit incrustado te permite aprovechar nuestra línea de productos completa de características (push, mensajes dentro de la aplicación y todo el seguimiento de análisis de mensajes pertinente).

{% alert note %}
Para las Tarjetas de contenido y las integraciones personalizadas de mensajes dentro de la aplicación, llama directamente a los métodos del SDK de Braze.
{% endalert %}

#### Paso 1: Integrar los SDK de mParticle

Integra los SDK de mParticle adecuados en tu aplicación en función de las necesidades de tu plataforma:

* [mParticle para Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle para iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle para Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Paso 2: Completar la integración del kit de eventos Braze de mParticle

Aunque no es necesario incluir directamente el SDK de Braze en tu sitio web o aplicación para esta integración de mParticle, debe instalarse el siguiente kit Appboy de mParticle para reenviar los datos de tu aplicación a Braze.

La [guía de integración del kit de eventos Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) de mParticle te guiará a través de las instrucciones de alineación personalizada de mParticle y Braze en función de tus necesidades de mensajería (push, seguimiento de ubicación, etc.).

#### Paso 3: Configuración de las conexiones para tu salida de Braze

En mParticle, ve a **Conexiones** > **Conectar** > **[Tu plataforma deseada]** > **Conectar salida** para añadir Braze como salida. A continuación, selecciona **Guardar**.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para obtener un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulta [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Integración de la API del servidor

Se trata de un complemento para enrutar tus datos de backend a Braze si utilizas los SDK del lado del servidor de mParticle (por ejemplo, Ruby, Python, etc.). Para configurar esta integración de servidor a servidor con Braze, sigue [la documentación de mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
La integración de servidor a servidor no es compatible con las características de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, las Tarjetas de contenido o las notificaciones push. También existen datos capturados automáticamente, como los campos a nivel de dispositivo, que no están disponibles a través de este método. 

Considera una integración en paralelo si deseas utilizar estas características.

Para que los datos del servidor se reenvíen a Braze, deben incluir un `external_id`; los usuarios anónimos no serán reenviados.
{% endalert %}

#### Configuración de las conexiones para tu salida de Braze

En mParticle, ve a **Conexiones > Conectar > [Tu plataforma deseada] > Conectar salida** para añadir Braze como salida. **Guárdalo** cuando lo hayas completado. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

No todos los ajustes de conexión se aplicarán a todas las plataformas y tipos de integración. Para obtener un desglose de los ajustes de conexión y las plataformas a las que se aplican, consulta [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Antes de habilitar "Atributos de usuario enriquecidos" o "Identidades de usuario enriquecidas", te recomendamos que revises los [excedentes de puntos de datos](#potential-data-point-overages) para asegurarte de que conoces cómo afectarán estas configuraciones al uso de puntos de datos.

### Detalles del mapeado de datos

#### Tipos de datos
No todos los tipos de datos son compatibles entre ambas plataformas.
- [Las propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) admiten objetos de cadena, numéricos, Booleano o de fecha. No admiten matrices ni objetos anidados.
- [Los atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) admiten objetos de cadena, numéricos, Booleano, de fecha y matrices, pero no admiten objetos ni objetos anidados. 

{% alert note %}
Braze no admite marcas de tiempo anteriores al año 0 ni posteriores al año 3000 en los atributos personalizados de tipo `Time`. Braze ingerirá estos valores cuando los envíe mParticle, pero el valor se almacenará como una cadena.
{% endalert %}

#### Mapeado de datos

| Tipo de datos de mParticle | Tipo de datos de Braze | Descripción |
| ------------------- | --------------- | ----------- |
| Atributos de usuario (reservados) | Atributo estándar | Por ejemplo, la clave de atributo de usuario reservada `$FirstName` de mParticle se mapea al campo de atributo estándar `first_name` de Braze. |
| Atributos de usuario (otros) | Atributo personalizado | Cualquier atributo de usuario pasado a mParticle que no corresponda a sus claves de atributo de usuario reservadas se registra en Braze como un atributo personalizado.<br><br>Los atributos de usuario admiten cadenas, números, booleanos, fechas y matrices, pero no objetos ni objetos anidados. |
| Evento personalizado | Evento personalizado | Los eventos personalizados de mParticle son reconocidos por Braze como eventos personalizados. Los atributos de evento se reenvían como propiedades de evento personalizadas.<br><br>Los atributos de evento pasados a Braze como propiedades de evento admiten objetos de cadena, numéricos, Booleano o de fecha, pero no admiten matrices ni objetos anidados. |
| Evento de comercio de compra | Evento de compra | Los eventos de comercio de compra se mapearán a eventos de compra de Braze. <br><br>Alterna el valor de configuración de los datos de eventos de comercio agrupados para registrar las compras a nivel de pedido o a nivel de producto. Por ejemplo, si es `false`, un único evento entrante con dos productos, promociones o impresiones únicos daría lugar al menos a dos eventos salientes de Braze. Si se establece en `true`, daría lugar a un único evento saliente con una matriz anidada de productos, promociones o impresiones, respectivamente.<br><br>Para más información sobre los campos de comercio adicionales que se registrarán, consulta [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Al establecer "bundle commerce event data" como `false`, los atributos de producto pasados a Braze como propiedades de evento de compra admiten objetos de cadena, numéricos, Booleano o de fecha, pero no admiten matrices ni objetos anidados.|
| Todos los demás eventos de comercio | Evento personalizado | Todos los demás eventos de comercio se mapearán a eventos personalizados. <br><br>Alterna el valor de configuración de los datos de eventos de comercio agrupados para registrar las compras a nivel de pedido o a nivel de producto. Por ejemplo, si es `false`, un único evento entrante con dos productos, promociones o impresiones únicos daría lugar al menos a dos eventos salientes de Braze. Si se establece en `true`, daría lugar a un único evento saliente con una matriz anidada de productos, promociones o impresiones, respectivamente.<br><br>Además de ciertos valores de comercio predeterminados, los atributos de producto se registrarán como propiedades de evento de Braze. Para más información sobre los campos de comercio adicionales que se registrarán, consulta [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Al configurar "bundle commerce event data" como `false`, los atributos de producto pasados a Braze como propiedades de evento admiten objetos de cadena, numéricos, Booleano o de fecha, pero no admiten matrices ni objetos anidados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Mapeado de identidades de usuario
Para cada salida de mParticle, puedes seleccionar el tipo de identidad externa que deseas enviar a Braze como `external_id`. Aunque el valor predeterminado es el ID de cliente, puedes elegir mapear otro ID, como `MPID`, para enviarlo a Braze como `external_id`. Ten en cuenta que elegir un identificador distinto del ID de cliente puede influir en la forma en que se envían los datos en Braze. 

Por ejemplo, mapear MPID a tu `external_id` de Braze tendrá los siguientes efectos:
- Debido a la naturaleza del momento en que se asigna el MPID, a todos los usuarios se les asignará un `external_id` al iniciar la sesión.
- La configuración de Currents puede requerir un mapeado adicional debido a los diferentes tipos de datos entre MPID y `external_id`.

### Transmisión de las solicitudes de borrado (solicitudes de los interesados)

Reenvía las solicitudes de borrado a Braze configurando una salida de solicitud del interesado a Braze. Para enviar solicitudes de borrado a Braze, sigue [la documentación de mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Posibles excedentes de puntos de datos

### Atributos de usuario enriquecidos

#### Habilitar el enriquecimiento de atributos/identidades de usuario (solo de servidor a servidor) {#enriched}

En los ajustes de conexión de mParticle, Braze recomienda desactivar **Incluir atributos de usuario enriquecidos**. Si se habilita, mParticle reenviará todos los atributos de usuario disponibles (como atributos estándar, atributos personalizados y atributos calculados) del perfil existente a Braze en cada evento registrado. Esto da lugar a un elevado consumo de puntos de datos, porque mParticle envía a Braze los mismos atributos sin cambios en cada llamada.

Por ejemplo, si un usuario añade su nombre, apellidos y número de teléfono durante su primera sesión y más tarde se registra en un boletín de noticias y añade la misma información y un correo electrónico, desencadenando un evento de registro en el boletín:
- Si está habilitado (por defecto), se incurrirá en cinco puntos de datos. (evento de registro, dirección de correo electrónico, nombre, apellidos y número de teléfono)
- Si está deshabilitado, se incurrirá en dos puntos de datos (evento de registro y dirección de correo electrónico)

{% alert note %}
Desactivar esta opción no comprobará los cambios de datos. Sin embargo, impedirá que la integración envíe todos los atributos de usuario del perfil del usuario que no se recibieron en el lote de entrada original o no se establecieron explícitamente como un atributo para el evento. Es importante seguir comprobando que solo se pasan deltas a Braze.
{% endalert %}

#### Consideraciones para desactivar los atributos de usuario enriquecidos

Hay algunas consideraciones a tener en cuenta al desactivar **Incluir atributos de usuario enriquecidos**:
1. La integración de servidor a servidor utiliza la API de eventos de mParticle para enviar eventos a Braze. Cada solicitud es desencadenada por un evento. Cuando se cambia un atributo de usuario, como la actualización de una dirección de correo electrónico, pero no está asociado a un evento específico (por ejemplo, un evento personalizado de actualización de perfil), el nuevo valor solo se pasa a una salida como Braze como un "atributo enriquecido" en la carga útil del siguiente evento desencadenado por el usuario. Cuando **Incluir atributos de usuario enriquecidos** está desactivado, este nuevo valor de atributo no asociado a un evento específico no se pasará a Braze.
  - Para solucionarlo, recomendamos crear un evento "atributo de usuario actualizado" independiente que solo envíe a Braze los atributos de usuario específicos que se han actualizado. Ten en cuenta que, con este enfoque, seguirás registrando un punto de datos adicional para el evento "atributo de usuario actualizado", pero el uso de puntos de datos será mucho menor que el envío de todos los atributos de usuario en cada llamada con la característica habilitada.
2. Los atributos calculados se transmiten a Braze como atributos de usuario enriquecidos, por lo que si se desactiva "Atributos de usuario enriquecidos" dejarán de transmitirse a Braze. Para enviar atributos calculados a Braze cuando "Atributos de usuario enriquecidos" están desactivados, una [fuente de atributos calculados](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) podría ayudar sin enviar todos los atributos. La fuente enviará una actualización a Braze cuando cambie un atributo calculado. 

## Solución de problemas

### Solución de problemas de notificaciones push en iOS con el kit de eventos Braze

Si las notificaciones push no funcionan al usar el kit de eventos Braze (integración de kit incrustado) en iOS, comprueba lo siguiente:
1. **Reenvío de tokens push:** Confirma que mParticle está reenviando tokens push a Braze. En tu dashboard de mParticle, verifica que la conexión del kit de Braze tiene push habilitado y que la credencial push de Apple correcta está configurada en el panel de Braze.
2. **Orden de inicialización del kit:** El kit de Braze debe inicializarse antes de que tu aplicación solicite permisos de push. Si los permisos de push se solicitan antes de que el kit esté activo, el token push puede no reenviarse a Braze. Comprueba que el SDK de mParticle se inicia temprano en el ciclo de vida de tu aplicación.
3. **Method swizzling:** El kit de Apple de mParticle utiliza method swizzling para reenviar automáticamente tokens push y gestionar eventos de notificaciones push. Si has deshabilitado el swizzling u otro SDK está interfiriendo, los tokens push pueden no llegar a Braze. Verifica que el swizzling está habilitado en tu configuración de mParticle.
4. **Gestión manual de tokens:** Si gestionas los tokens push manualmente (por ejemplo, implementando `application:didRegisterForRemoteNotificationsWithDeviceToken:`), asegúrate de que estás pasando el token a mParticle asignándolo a la propiedad de token de notificación push, por ejemplo: `MParticle.sharedInstance().pushNotificationToken = deviceToken`. El kit lo reenviará entonces a Braze.
5. **Discrepancia de entorno:** Confirma que el entorno de la credencial APNs (desarrollo vs. producción) coincide con la compilación de tu aplicación. Para más detalles, consulta [Solución de problemas de push en iOS]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/ios/).

### Envío de datos innecesarios o duplicados a Braze
Braze cuenta un punto de datos cada vez que se pasa un atributo a Braze, aunque el valor no cambie. Por este motivo, Braze recomienda reenviar únicamente los datos necesarios para actuar dentro de Braze y asegurarse de que solo se transmiten deltas de atributos.