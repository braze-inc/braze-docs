---
nav_title: Zeotap Symphony
description: "Este artículo de referencia describe la asociación entre Braze y Zeotap, una plataforma de datos de los clientes de nueva generación que proporciona resolución de identidades, información y enriquecimiento."
page_type: partner
search_tag: Partner
page_order: 2 
---

# Zeotap Symphony

La integración de Braze y Zeotap Symphony te permite crear orquestaciones en tiempo real y ejecutar campañas de correo electrónico y notificación push.

- Envía nombres y apellidos a través de Zeotap, a partir de los cuales los usuarios pueden enviar correos electrónicos personalizados a través de Braze.
- Enviar eventos personalizados o un evento de compra en tiempo real a través de Zeotap, a partir de los cuales los usuarios pueden crear activadores de campaña dentro de Braze para dirigirse a sus clientes.

{% alert note %}
Para crear campañas de marketing por correo electrónico, incorpore los correos electrónicos sin procesar a Zeotap asignándolos a `Email Raw` en el catálogo de Zeotap.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Nombre del cliente | Este es tu nombre de cliente para tu cuenta Braze. Puedes encontrarla navegando hasta la Consola Braze. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

Esta sección proporciona información sobre los dos métodos de integración con Braze:

### Método 1
En este método, tienes que realizar las siguientes tareas:
1. Integra el SDK de Braze en tu sitio web o aplicación.
2. Integra Braze con Zeotap a través de Symphony.

- `User traits` deben asignarse a los respectivos campos Braze en la pestaña **Datos a enviar**. Si se asignan los atributos `Event` y `Purchase`, se duplican los eventos en Braze.
- Mapea `External ID` a `User ID` configurado al configurar el SDK de Braze.

Cuando la integración se haya configurado correctamente, podrá crear campañas de correo electrónico y notificaciones push basadas en atributos personalizados enviados a Braze a través de Symphony.

### Método 2
Con este método, puedes integrar Braze con Zeotap a través de Symphony.

- Este método no es compatible con las características de la interfaz de usuario de Braze, como la mensajería dentro de la aplicación, las tarjetas de contenido o las notificaciones push.
- Zeotap recomienda mapear el `hashed email` disponible en el Catálogo Zeotap al `External ID`.

Cuando la integración se haya configurado correctamente, sólo podrá crear campañas de correo electrónico basadas en atributos personalizados enviados a Braze a través de Symphony.

## Flujo de datos a Braze e identificadores compatibles

Los datos fluirán de Zeotap a Braze utilizando el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Los siguientes puntos resumen el flujo de datos:

1. Zeotap envía atributos de perfil de usuario, atributos personalizados, eventos personalizados y campos de compra.
2. Se asignan todos los campos relevantes del Catálogo Zeotap a los campos Braze en la pestaña **Datos a enviar**.
3. A continuación, los datos se cargan en Braze.

Encontrará información detallada sobre los distintos atributos en la sección [Datos a enviar](#data-to-send-tab).

## Configuración del destino

Después de aplicar filtros o añadir una condición para sus usuarios en Symphony, puede activarlos en Braze en **Enviar a destinos**. Se abrirá una nueva ventana en la que podrá configurar su destino. Puede utilizar un destino existente de la lista de **Destinos disponibles** o crear uno nuevo.

#### Añadir nuevo destino
Realice los siguientes pasos para añadir un nuevo destino:
1. Selecciona **Añadir nuevo destino**.
2. Busca **Braze**.
3. Añada el **Nombre del Cliente**, la **Clave API** y la **Instancia** y guarde el destino.

El destino se crea y se pone a disposición en **Destinos disponibles**.

#### Añadir entradas a nivel de flujo de trabajo
Después de crear un destino, lo siguiente es añadir entradas a nivel de flujo de trabajo, como se menciona a continuación.
1. Elija el destino en la lista de destinos disponibles utilizando la función de búsqueda.
2. Los campos **Nombre de cliente**, **Clave API** e **Instancia** se rellenan automáticamente en función del valor introducido al crear el destino.
3. Introduzca el **Nombre de Audiencia** que desea crear para este nodo de flujo de trabajo. Se envía como **atributo personalizado** a Braze.
4. Complete la asignación de Catálogo a Destino en la pestaña **Datos a Enviar**. A continuación encontrará información detallada sobre cómo realizar la asignación.

#### Ficha Datos a enviar
La pestaña **Datos a enviar** permite asignar los campos del Catálogo Zeotap a los campos Braze que pueden enviarse a Braze. La asignación puede realizarse de una de las siguientes maneras:
- **Asignación estática** \- Hay determinados campos que Zeotap asigna automáticamente a los campos Braze correspondientes, como correo electrónico, teléfono, nombre, apellidos, etc.<br>
- **Selección desplegable** \- Asigne los campos relevantes ingestados en Zeotap a los campos Braze proporcionados en el menú desplegable.<br>![Varios rasgos del usuario configurados en Zeotap, como idioma, ciudad, cumpleaños, etc.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Entrada de datos personalizados** \- Añada datos personalizados asignados al campo Zeotap correspondiente y envíelos a Braze.<br>![Seleccionando "loyalty_points" como rasgo de usuario en Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Atributos admitidos
En esta sección encontrará información detallada sobre todos los campos Braze.

| Campo de Braze | Tipo de mapeado | Descripción |
| --- | --- | --- |
| ID externo | Selección desplegable | Este es el `User ID` persistente definido por Braze para rastrear a los usuarios a través de dispositivos y plataformas. Le recomendamos que asigne `User ID` a `External ID`; de lo contrario, Zeotap puede enviar correo electrónico como alias de usuario.<br><br>Zeotap te recomienda que mapees el `hashed email` disponible en el Catálogo Zeotap en el `External ID`.|
| Correo electrónico | Cartografía estática | Está mapeado en `Email Raw` en el Catálogo Zeotap. |
| Teléfono | Cartografía estática | Está mapeado en `Mobile Raw` en el Catálogo Zeotap.<br><br>\- Braze acepta números de teléfono en formato `E.164`. Zeotap no realiza ninguna transformación. Por lo tanto, debe introducir los números de teléfono en el formato prescrito. Para más información, consulta [Números de teléfono de usuario]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| Nombre | Cartografía estática | Está mapeado en `First Name` en el Catálogo Zeotap. |
| Apellido | Cartografía estática | Está mapeado en `Last Name` en el Catálogo Zeotap. |
| Género | Cartografía estática | Está mapeado en `Gender` en el Catálogo Zeotap. |
| Nombre de evento personalizado | Cartografía estática | Está mapeado en `Event Name` en el Catálogo Zeotap.<br><br>Tanto el Nombre del evento personalizado como la Hora del evento personalizado deben estar mapeados para capturar eventos personalizados en Braze. El evento personalizado no se puede procesar si no se asigna ninguno de los dos. Para más información, consulta el [objeto evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Sello de tiempo de evento personalizado | Cartografía estática | Está mapeado en la dirección `Event Timestamp` del Catálogo Zeotap.<br><br>Tanto el Nombre del evento personalizado como la Hora del evento personalizado deben estar mapeados para capturar eventos personalizados en Braze. El evento personalizado no se puede procesar si no se asigna ninguno de los dos. Para más información, consulta el [objeto evento]({{site.baseurl}}/api/objects_filters/event_object#what-is-the-event-object). |
| Suscripción por correo electrónico | Selección desplegable | Incorpora un campo `Email Marketing Preference` y mapea en él.<br><br>Zeotap envía los tres valores siguientes:<br>- `opted_in` - Indica que el usuario se ha registrado explícitamente para la preferencia de marketing por correo electrónico.<br>- `unsubscribed` - Indica que el usuario ha optado explícitamente por no recibir mensajes de correo electrónico.<br>- `subscribed` - Indica que el usuario no se ha adherido ni se ha excluido voluntariamente. |
| Push Suscriptor | Selección desplegable | Incorpora un campo `Push Marketing Preference` y mapea en él.<br><br>Zeotap envía los tres valores siguientes:<br>- `opted_in` - Indica que el usuario se ha registrado explícitamente para la preferencia de push marketing<br>- `unsubscribed` - Indica que el usuario ha optado explícitamente por no recibir mensajes push.<br>- `subscribed` - Indica que el usuario no ha optado ni por la adhesión ni por la exclusión voluntaria. |
| Habilitar el seguimiento de aperturas de correo electrónico | Selección desplegable | Asigne el campo `Marketing Preference` correspondiente.<br><br>Cuando se establece en true, permite añadir un píxel de seguimiento de apertura a todos los futuros correos electrónicos enviados a este usuario. |
| Habilitar seguimiento de clics por correo electrónico | Selección desplegable | Asigne el campo `Marketing Preference` correspondiente.<br><br>Cuando se establece en true, habilita el seguimiento de clics para todos los enlaces dentro de todos los futuros correos electrónicos enviados a este usuario. |
| Identificación del producto | Selección desplegable | \- Identificador de una acción de compra `(Product Name/Product Category)`. Para más detalles, consulta el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/).<br>\- Incorpora el atributo correspondiente al Catálogo Zeotap y mapea con él.<br><br>`Product ID`, `Currency`, y `Price` deben ser mapeados obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. Para más información, consulta el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-object). |
| Divisa | Selección desplegable | \- Atributo de moneda para la acción de compra.<br>\- El formato compatible es `ISO 4217 Alphabetic Currency Code`.<br>\- Incorpora al Catálogo Zeotap los Datos de Divisa correctamente formateados y mapeados.<br><br>`Product ID`, `Currency`, y `Price` deben ser mapeados obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. |
| Precio | Selección desplegable | \- Atributo de precio para la acción de compra.<br>\- Incorpora el atributo correspondiente al Catálogo Zeotap y mapea con él.<br><br>`Product ID`, `Currency`, y `Price` deben ser mapeados obligatoriamente para capturar eventos de compra en Braze. El evento de compra no puede llevarse a cabo si falta alguno de los tres. |
| Cantidad | Selección desplegable | \- Atributo de cantidad para la acción de compra.<br>\- Incorpora el atributo correspondiente al Catálogo Zeotap y mapea con él. |
| País | Selección desplegable | Mapea al campo del Catálogo `Country` que estás incorporando. |
| Localidad | Selección desplegable | Mapea al campo del Catálogo `City` que estás incorporando. |
| Idioma | Selección desplegable | \- El formato aceptado es `ISO-639-1` estándar (por ejemplo, en).<br>\- Incorpora la lengua correctamente formateada y mapeada. |
| Fecha de nacimiento | Selección desplegable | Mapea el campo `Date of Birth` que estás incorporando. |
| Atributo personalizado | Introducción de datos personalizados | Asigne cualquier atributo de usuario a una entrada de datos personalizada, que luego se envía a Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Visualización de datos en la consola Braze

Una vez asignados los atributos relevantes que se enviarán y publicarán en el flujo de trabajo, los eventos empezarán a fluir a Braze en función de los criterios definidos. Puede buscar por ID de correo electrónico o ID externo en la consola Braze.

![]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Varios atributos se encuentran en diferentes secciones del panel de control del usuario en Braze.
- La pestaña **Perfil** contiene los atributos del usuario.
- La pestaña **Atributos personalizados** contiene los atributos personalizados definidos por el usuario.
- La pestaña **Eventos personalizados** contiene el evento personalizado definido por el usuario.
- La pestaña **Compras** contiene las compras realizadas durante un periodo de tiempo por el usuario.

## Creación de campañas

Los usuarios pueden crear campañas dentro de Braze y activar usuarios en tiempo real o en función de la hora programada. Las campañas pueden activarse en función de las acciones realizadas por el usuario (evento personalizado, compra) o de los atributos del usuario.

