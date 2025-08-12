---
nav_title: Voucherify y lista de códigos de promoción
article_title: Lista de códigos promocionales de Voucherify y Braze
page_order: 4
alias: /partners/voucherify/promotion/
description: "Este artículo de referencia describe cómo puedes compartir códigos de Voucherify utilizando el fragmento de código promocional Braze."
page_type: partner
search_tag: Partner
---

# Lista de códigos promocionales de Voucherify y Braze

> Además del contenido conectado y los atributos personalizados, puedes compartir códigos de Voucherify utilizando el fragmento de código promocional Braze. En primer lugar, exporte códigos desde Voucherify, importe códigos a Braze y añada un fragmento de código de correo electrónico para extraer códigos de la lista de promociones. 

_Esta integración es mantenida por Voucherify._

## Paso 1: Exportar códigos únicos desde Voucherify

En Voucherify, navegue hasta su campaña de Voucherify. A continuación, seleccione **Exportar a CSV** y edite el archivo CSV y elimine el nombre de la columna para dejar sólo la lista de códigos.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## Paso 2: Crear una lista de códigos de promoción

Vaya a **Configuración de datos** > **Códigos de promoción** y haga clic en **Crear lista de códigos de promoción**.

Puede utilizar el nombre de la campaña de Voucherify para nombrar la lista y comprobar la coherencia de los datos.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

A continuación, añada el fragmento de código que hace referencia a los códigos de la lista; se rellenará con un código único cuando se envíe el mensaje.

### Configuración adicional

También puede establecer atributos para los códigos, como la caducidad de la lista y las alertas de umbral; sin embargo, tenga en cuenta que Voucherify gestiona la lógica detrás de sus códigos independientemente de la configuración de la lista.

![Caducidad de la lista]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## Paso 3: Cargar archivo CSV

Cargue el archivo CSV con los códigos de Voucherify.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Confirme que la lista sólo contiene códigos (no encabezado de columna) y haga clic en **Iniciar carga**. Una vez finalizada la importación, haga clic en **Guardar lista** para confirmar los detalles de la lista.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## Paso 4: Utilizar fragmentos de código en campañas Braze

Para utilizar códigos de la lista en una campaña Braze, copie el fragmento y añádalo al cuerpo del correo electrónico.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Añade el fragmento de código para mostrar un código de la lista.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Una vez enviado el mensaje con el código, no se volverá a utilizar el mismo código.

