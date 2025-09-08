---
nav_title: Sendbird
article_title: Sendbird
description: "Este artículo de referencia describe la asociación entre Braze y Sendbird, una solución líder de mensajería in-app que permite a los usuarios recibir notificaciones in-app en la plataforma Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications ofrece a los responsables de marketing y de producto un nuevo y potente canal para comunicarse con sus clientes in-app con mensajes unidireccionales persistentes e interactivos. Estos mensajes pueden utilizarse para cualquier tipo de comunicación y se emplean sobre todo con fines promocionales y transaccionales.

_Esta integración está mantenida por Sendbird._

## Sobre la integración

La integración de Braze y Sendbird permite a los usuarios de Braze:
* Utiliza las funciones de segmentación y desencadenamiento de Braze para iniciar notificaciones personalizadas dentro de la aplicación.
* Cree notificaciones personalizadas dentro de la aplicación en la plataforma Sendbird Notifications, que luego se entregan dentro del entorno de la aplicación, mejorando el compromiso del usuario.

Al aprovechar las capacidades conjuntas de Braze y Sendbird Notifications, las empresas pueden elevar el compromiso de los clientes y aumentar las tasas de conversión a través de estrategias eficaces de notificación dentro de la aplicación.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Sendbird | Se requiere una cuenta Sendbird para beneficiarse de esta asociación. |
| Sendbird UIKit | Debe tener el Sendbird UIKit instalado en su aplicación [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) o [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

![]({% image_buster /assets/img/sendbird/use-cases.png %})

La integración de Braze y Sendbird Notifications ofrece una amplia gama de casos de uso para impulsar el compromiso de los clientes y ofrecer una experiencia de usuario excepcional:

- **Marketing**: Mejore las campañas dirigidas con promociones personalizadas y recomendaciones adaptadas a las preferencias de los usuarios, como descuentos exclusivos basados en el historial de navegación o en compras anteriores.
- **Transaccional**: Mejore la comunicación con el cliente mediante actualizaciones en tiempo real sobre pedidos, entregas, facturación y pagos, incluidas notificaciones sobre el estado del pedido, detalles del envío y plazos de entrega estimados.

## Integración

### Paso 1: Crear una plantilla de notificación

[Las plantillas de Sendbird](https://sendbird.com/docs/notifications/v1/templates) le permiten enviar notificaciones personalizadas dentro de la aplicación creando y utilizando varias plantillas para cada canal. Las plantillas pueden crearse y personalizarse en Sendbird Dashboard sin necesidad de escribir código.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Paso 2: Configurar la integración Braze en el panel de Sendbird

En **Sendbird Dashboard**, seleccione su aplicación, vaya a **Notificaciones > Integraciones** y haga clic en **Añadir** en la sección **Braze**. Aquí necesitarás tu clave de API REST de Braze y tu punto final REST de Braze.

Una vez que haya proporcionado todos los campos, haga clic en **Guardar** para completar la integración y acceder a los puntos finales de integración y al token de API.

### Paso 3: Instalar el Constructor de Notificaciones Sendbird

A continuación, debes instalar [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Esta extensión de Google Chrome te permite enviar notificaciones personalizadas a través de Sendbird en el Braze Dashboard.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Añadir credenciales Sendbird a la extensión

Una vez instalada la extensión, haga clic en el icono Sendbird de la barra de herramientas de su navegador y seleccione **Configuración**. Aquí, proporcione el ID de su aplicación y el token de API que se encuentra en el **Generador de notificaciones de Sendbird**.

### Paso 4: Asignar ID de usuario de Sendbird a ID de usuario de Braze

Debe añadirse un ID de usuario de Sendbird a un perfil de usuario de Braze como [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) para que pueda utilizarse la integración. Puede cargar y actualizar perfiles de usuario mediante archivos CSV desde la página de [importación de usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv). También puede utilizar el ID de usuario de Braze como ID de usuario de Sendbird.

### Paso 5: Configure su plantilla de webhook

En Braze, desde **Templates & Media**, vaya a **Webhook Templates** y elija **Sendbird Webhook Template**. Tenga en cuenta que esta plantilla sólo estará disponible si tiene instalada la extensión Sendbird Notification Builder.

{% raw %}
1. Proporcione un nombre de plantilla y añada equipos y etiquetas según sea necesario.
2. Copie un punto final en tiempo real o por lotes del panel de Sendbird en la **URL del Webhook**.
3. En el campo **Receptor**, haga clic en el icono <i class="fas fa-plus"></i> e inserte el atributo de usuario asignado al ID de usuario de Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si está utilizando un atributo personalizado `sendbird_id` como ID de usuario de Sendbird.
    - `{{ '{{' }}${user_id}}}` si utilizas el ID de usuario de Braze como ID de usuario de Sendbird.
4. En la pestaña **Configuración**, sustituya `SENDBIRD_API_TOKEN` por el token de la API de notificaciones del panel de Sendbird.
5. Guarda la plantilla.
{% endraw %}

## Mediante esta integración

### Campañas

1. En el panel Braze, en la página **Campañas**, haga clic en **Crear campaña** > **Webhook**.
2. Seleccione la plantilla de webhook que creó anteriormente. Se recomienda encarecidamente utilizar el punto final Lote para las campañas.
3. Personalice la plantilla editando sus variables en la pestaña **Componer**.

### Canvas

1. Desde un Lienzo nuevo o existente, añada un componente **Mensaje**. 
2. Abra el componente y seleccione **Webhook** en los **Canales de mensajería**.
3. Seleccione la plantilla de webhook que creó anteriormente. Se recomienda encarecidamente utilizar el punto final en tiempo real para los lienzos.
4. Personalice la plantilla editando sus variables en la pestaña **Componer**.

## Personalización

### Seguimiento de la entrega y estado abierto

Para integrar el evento de entrega y estado abierto de las notificaciones con la métrica de conversión de una campaña, añada un evento personalizado en el panel Braze.

1. En el panel de control de Braze, vaya a **Ajustes > Gestionar ajustes > Eventos personalizados** y haga clic en **\+ Añadir evento personalizado**.
2. Después de crear un evento personalizado, haga clic en **Administrar propiedades**, añada una propiedad llamada "estado" y elija "Cadena" como tipo de propiedad.
3. Cuando redacte una notificación en campañas o lienzos, introduzca el nombre del evento personalizado en el campo **Nombre del evento**.

Este evento personalizado se activará dos veces para cada notificación, cuando se envíe un mensaje y cuando un usuario abra el mensaje.
- Cuando se envía un mensaje, se activa un evento personalizado con el estado `SENT`.
- Cuando se lee un mensaje, se activa un evento personalizado con el estado `READ`.


