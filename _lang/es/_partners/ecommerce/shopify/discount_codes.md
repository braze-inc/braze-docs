---
nav_title: Códigos de descuento únicos 
article_title: Envío de códigos de descuento únicos
alias: /shopify_discount_codes/
page_order: 6
description: "Este artículo de referencia cubre un caso de uso enviado por la comunidad sobre el uso de códigos promocionales Braze con el Bot de código de descuento masivo de Shopify para enviar códigos de descuento únicos a través de tus campañas y Lienzos."
---

# Envío de códigos de descuento únicos a través de Shopify

> Este caso de uso enviado por la comunidad muestra cómo utilizar [los códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze con el Bot de código de descuento masivo de Shopify para generar códigos de descuento únicos para tus campañas y Lienzos. Los códigos de descuento únicos ayudan a evitar la explotación de códigos promocionales genéricos.

{% alert important %}
Se trata de una integración enviada por la comunidad y no está soportada directamente por Braze. El Bot de códigos de descuento a granel es compatible directamente con Shopify. Braze sólo admite códigos promocionales Braze.
{% endalert %}

## Requisitos

| Requisito | Descripción |
| --- | --- |
| Configurar una tienda Shopify | Confirma que ya has [configurado una tienda Shopify con Braze]({{site.baseurl}}/shopify_overview/). |
| Instala la aplicación Bulk Discount Code Bot | Descarga la aplicación [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) en la tienda de aplicaciones de Shopify. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Generar códigos de descuento únicos

### Paso 1: Configura tus códigos de descuento

Utiliza el Bot de códigos de descuento a granel para configurar tus códigos de descuento en función del número de códigos a generar, la longitud del código, el valor del descuento y mucho más.

![Las opciones de configuración de un conjunto de descuentos.][1]

### Paso 2: Exporta tus códigos

Busca tu conjunto de descuentos en la barra de búsqueda del Bot de códigos de descuento a granel y, a continuación, selecciona **Exportar códigos** > **Descargar códigos** para descargar un archivo CSV a tu carpeta Descargas.

![Barra de búsqueda con un desplegable que muestra el conjunto de descuentos y una fila de botones para seleccionar.][2]{: style="max-width:70%;"}

En el archivo CSV, borra la fila 1 para eliminar la cabecera de columna "Promo". Esto evitará que "Promo" se convierta en un código de descuento en Braze.

![Un diagrama de flujo que muestra la eliminación de la cabecera de fila "Promo" en un archivo CSV.][3]{: style="max-width:60%;"}

### Paso 3: Añade tus códigos de descuento a Braze

En Braze, ve a **Configuración de datos** > **Códigos promocionales** > **Crear lista de códigos promocionales** y [configura tu lista de códigos de descuento]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Asegúrate de que coincide con la fecha de caducidad configurada por el Bot de código de descuentos masivos.

A continuación, carga tu archivo CSV y selecciona **Guardar lista**.

### Paso 4: Añade tus códigos de descuento a una campaña Braze o a un paso en Canvas

Si quieres utilizar tus códigos promocionales únicos en una campaña de envío único, o no te importa que los usuarios reciban varios códigos únicos en diferentes campañas o pasos en Canvas, copia el fragmento de código Liquid de la lista de códigos promocionales que guardaste.

![Un fragmento de código Liquid con un botón para copiarlo.][4]{: style="max-width:60%;"}

Pega el fragmento de código Liquid en una campaña o paso en Canvas. 

![Un GIF que muestra cómo se añade el fragmento de código Liquid a un paso en Canvas.][5]

Si quieres que los usuarios reciban un único código de descuento, independientemente de cuántas veces se haga referencia al código de descuento en campañas o Lienzos, crea un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) directamente antes del primer paso de Mensaje que asigne el código de descuento a un atributo personalizado, como "Código promocional".

{% alert tip %}
También puedes [crear un atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) yendo a **Configuración de datos** > **Atributos** personalizados **.**
{% endalert %}

En el paso Actualizar usuario, haz lo siguiente para cada campo:
- **Nombre del atributo:** Selecciona **el código promocional**.
- **Acción:** Selecciona **Actualizar**.
- **Valor clave:** Pega el fragmento de código de Liquid.

![Un paso de Actualización de usuario que actualiza un atributo "Código promocional" con el fragmento de código Liquid.][6]

Ahora, puedes añadir el atributo personalizado {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} a cualquier mensaje, y el código de descuento aparecerá en la plantilla.

## Comportamiento del código de descuento

{% details Campaña multicanal o paso en Canvas %}

Cuando se utiliza un fragmento de código de descuento en una campaña multicanal o en un paso en Canvas, los usuarios siempre reciben un código único. Si un usuario es elegible para recibir un código a través de más de un canal, recibirá el mismo código a través de cada canal. En otras palabras, un usuario elegible sólo recibiría un código en todos los mensajes enviados por esa campaña o paso en Canvas.

{% enddetails %}

{% details Diferentes pasos en Canvas o campañas separadas %}

Cuando se hace referencia a un código de descuento mediante varios pasos en el mismo Canvas o mediante campañas separadas, un usuario elegible recibirá varios códigos promocionales únicos (un código por cada paso en Canvas o campaña).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}