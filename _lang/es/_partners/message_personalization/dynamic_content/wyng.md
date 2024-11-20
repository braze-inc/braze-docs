---
nav_title: Wyng
article_title: Wyng
description: "Este artículo de referencia describe la asociación entre Braze y Wyng, una plataforma de datos de cero partes, que facilita la recopilación, el uso y la integración de las preferencias y los atributos de los clientes a través de microexperiencias, portales de preferencias de clientes y una plataforma API."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng][0] facilita la creación de experiencias digitales interactivas (es decir, cuestionarios, centros de preferencias, promociones) que atraen a los consumidores en los momentos adecuados, recopilan preferencias y otros datos de terceros y personalizan en tiempo real.

La integración de Braze y Wyng te permite aprovechar los zero-party data obtenidos a través de las experiencias Wyng para personalizar las interacciones en Braze Campaigns y Braze Canvas. Wyng también puede impulsar un centro de preferencias, para que los consumidores puedan controlar los datos y preferencias (incluidas las preferencias de comunicación) que comparten con su marca.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Wyng | Se necesita una cuenta Wyng para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conectar la integración Braze

En Wyng, vaya a [**Integraciones**][1] y seleccione la pestaña **Añadir**. A continuación, sitúate sobre **Braze** y haz clic en **Conectar** para la integración.

![La baldosa asociada Braze en la plataforma Wyng.][2]{: style="max-width:80%;"}

### Paso 2: Configurar el conector Braze

1. En la ventana de configuración que se abre, proporciona tu clave de API REST Braze.
![Una imagen del aspecto de la solicitud de credenciales.][4]{: style="max-width:80%;"}<br><br>
2. A continuación, utilice el menú desplegable para seleccionar la campaña Wyng que desea compartir con Braze.![Imagen del conector Braze que le pide que seleccione una campaña Wyng existente que desee compartir con Braze.][5]{: style="max-width:80%;"}<br><br>
3. A continuación, debes configurar las suscripciones, los objetos atributo y evento, y los eventos personalizados.<br><br>
- **Configuración de suscripciones (obligatorio)**<br>
Para suscribir usuarios a grupos de suscripción, haga clic en **Añadir suscripción** y añada el nombre y el ID del grupo de suscripción. Para añadir varios nombres e ID de grupo, pulse de nuevo el botón **Añadir suscripción**.<br>![Una imagen que te pide el nombre y el ID de un grupo de suscripción.][8]{: style="max-width:80%;"}<br><br>
- **Configuración del seguimiento del usuario**<br>
Haga clic en **Añadir propiedad personalizada** para añadir pares de atributos y objetos de evento para enviar al endpoint `/users/track`. Utilícelo para añadir valores de atributos codificados para cada transacción de datos enviada para la integración. Para añadir varias propiedades, haga clic de nuevo en el botón **Añadir propiedad personalizada**.<br>![Una imagen que le pide que añada propiedades personalizadas de atributos.][9]{: style="max-width:80%;"}<br><br>
- **Enviar evento personalizado**<br>
Opcionalmente, puede activar el **envío de eventos personalizados**. Si está activada, debe incluir el nombre del evento y el ID de la aplicación correspondiente.<br>![Una imagen que le pide que envíe eventos personalizados, si es necesario.][10]{: style="max-width:80%;"}<br><br>
4. Por último, debe asignar los campos Wyng a los campos de la API Braze en función de su caso de uso. Haga clic en **Seleccionar un campo** para elegir los campos que desea asignar y, a continuación, **guarde** la integración. Una vez guardados, estos campos asignados se pueden encontrar en **Integraciones > Gestionar**.
![Un ejemplo de los diferentes campos Wyng que puede asignar a determinados campos Braze.][11]{: style="max-width:80%;"}
![Una lista de los campos de sincronización disponibles.][12]{: style="max-width:80%;margin-top:2px"}

### Paso 3: Pruebe su integración

En Wyng, pruebe a enviar el formulario en su campaña Wyng. También puede enviarlo en la campaña de previsualización si no desea añadir un registro a la campaña de producción principal. Debería ver una transacción correcta en el panel de **integración**.

## Mediante esta integración

Una vez establecido el conector de datos, los campos creados en Wyng y añadidos a Braze pueden utilizarse como cualquier otro campo de datos para activar campañas, segmentar audiencias o alimentar contenidos personalizados.

Las solicitudes son amplias, y las preguntas específicas pueden dirigirse a [contact@wyng.com][13] o a tu director de cuentas específico.

## Solución de problemas

### Envío fallido

En el caso de un envío fallido, al enviar datos a Braze, haga clic en el enlace **Ver registro** para revisar el envío fallido y el mensaje de error asociado.

![El enlace "Ver registro" que se encuentra bajo el encabezado de acciones.][14]{: style="max-width:80%;"}

La página de registro mostrará el envío fallido, el recuento de reintentos, los datos del envío, el error y un enlace para volver a enviar el envío.

![Un ejemplo de lo que mostrará un envío fallido.][15]{: style="max-width:80%;"}

La sección **Ver error** mostrará el código de error y alguna información adicional sobre la causa del error. A continuación, puedes cotejar el código de error con Braze para determinar la causa.

![Un ejemplo de registro de errores mostrado en la plataforma Wyng.][16]{: style="max-width:80%;"}

Si tiene más preguntas, póngase en contacto con el servicio de asistencia de Wyng ([support@wyng.com][13]).

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: {{site.baseurl}}/api/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}