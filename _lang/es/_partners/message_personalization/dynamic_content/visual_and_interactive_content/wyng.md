---
nav_title: Wyng
article_title: Wyng
description: "Este artículo de referencia describe la asociación entre Braze y Wyng, una plataforma de datos de cero partes, que facilita la recopilación, el uso y la integración de las preferencias y los atributos de los clientes a través de microexperiencias, portales de preferencias de clientes y una plataforma API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) facilita la creación de experiencias digitales interactivas (es decir, cuestionarios, centros de preferencias, promociones) que atraen a los consumidores en los momentos adecuados, recopilan preferencias y otros datos de terceros y personalizan en tiempo real.

_Esta integración está mantenida por Wyng._

## Sobre la integración

La integración de Braze y Wyng te permite aprovechar los zero-party data obtenidos a través de las experiencias Wyng para personalizar las interacciones en Braze Campaigns y Braze Canvas. Wyng también puede impulsar un centro de preferencias, para que los consumidores puedan controlar los datos y preferencias (incluidas las preferencias de comunicación) que comparten con su marca.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Wyng | Se necesita una cuenta Wyng para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conectar la integración Braze

En Wyng, vaya a [**Integraciones**](https://wyng.com/dashboard/integrations/) y seleccione la pestaña **Añadir**. A continuación, sitúate sobre **Braze** y haz clic en **Conectar** para la integración.

![La ficha del socio Braze en la plataforma Wyng.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Paso 2: Configurar el conector Braze

1. En la ventana de configuración que se abre, proporciona tu clave de API REST Braze.
![Una imagen del aspecto de la solicitud de credenciales.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. A continuación, utiliza el menú desplegable para seleccionar la campaña Wyng que te gustaría compartir con Braze.![Imagen del conector Braze que te pide que selecciones una campaña Wyng existente que te gustaría compartir con Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, debes configurar las suscripciones, los objetos atributo y evento, y los eventos personalizados.<br><br>
- **Configuración de suscripciones (obligatorio)**<br>
Para suscribir usuarios a grupos de suscripción, haga clic en **Añadir suscripción** y añada el nombre y el ID del grupo de suscripción. Para añadir varios nombres e ID de grupo, pulse de nuevo el botón **Añadir suscripción**.<br>![Una imagen que te pide el nombre y el ID de un grupo de suscripción.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Configuración del seguimiento del usuario**<br>
Haga clic en **Añadir propiedad personalizada** para añadir pares de atributos y objetos de evento para enviar al endpoint `/users/track`. Utilícelo para añadir valores de atributos codificados para cada transacción de datos enviada para la integración. Para añadir varias propiedades, haga clic de nuevo en el botón **Añadir propiedad personalizada**.<br>![Una imagen que te pide que añadas propiedades de atributo personalizadas.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Enviar evento personalizado**<br>
Opcionalmente, puede activar el **envío de eventos personalizados**. Si está activada, debe incluir el nombre del evento y el ID de la aplicación correspondiente.<br>![Una imagen que te indica que envíes eventos personalizados, si es necesario.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Por último, debe asignar los campos Wyng a los campos de la API Braze en función de su caso de uso. Haga clic en **Seleccionar un campo** para elegir los campos que desea asignar y, a continuación, **guarde** la integración. Una vez guardados, estos campos asignados se pueden encontrar en **Integraciones > Gestionar**.
![Un ejemplo de los diferentes campos Wyng que puedes mapear con determinados campos Braze.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Una lista de los campos de sincronización disponibles.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Paso 3: Pruebe su integración

En Wyng, pruebe a enviar el formulario en su campaña Wyng. También puede enviarlo en la campaña de previsualización si no desea añadir un registro a la campaña de producción principal. Debería ver una transacción correcta en el panel de **integración**.

## Mediante esta integración

Una vez establecido el conector de datos, los campos creados en Wyng y añadidos a Braze pueden utilizarse como cualquier otro campo de datos para activar campañas, segmentar audiencias o alimentar contenidos personalizados.

Las solicitudes son amplias, y las preguntas específicas pueden dirigirse a [contact@wyng.com](mailto:contact@wyng.com) o a tu director de cuentas específico.

## Solución de problemas

### Envío fallido

En el caso de un envío fallido, al enviar datos a Braze, haga clic en el enlace **Ver registro** para revisar el envío fallido y el mensaje de error asociado.

![El enlace "Ver registro" que se encuentra bajo el encabezado de acciones.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

La página de registro mostrará el envío fallido, el recuento de reintentos, los datos del envío, el error y un enlace para volver a enviar el envío.

![Un ejemplo de lo que mostrará un envío fallido.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

La sección **Ver error** mostrará el código de error y alguna información adicional sobre la causa del error. A continuación, puedes cotejar el código de error con Braze para determinar la causa.

![Un ejemplo de registro de errores mostrado en la plataforma Wyng.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Si tienes más preguntas, ponte en contacto con el servicio de asistencia de Wyng[(support@wyng.com](mailto:contact@wyng.com)).


