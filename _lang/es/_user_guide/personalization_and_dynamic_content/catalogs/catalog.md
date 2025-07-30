---
nav_title: Crear un catálogo
article_title: Crear un catálogo
alias: "/catalogs/"
page_order: 1
description: "En este artículo de referencia se explica cómo crear catálogos que hagan referencia a datos de no usuarios en sus campañas Braze a través de Liquid."
---

# Crear un catálogo

> La creación de un catálogo implica la importación a Braze de un archivo CSV de datos no relativos al usuario. Así podrá acceder a esa información para enriquecer sus mensajes. Puede introducir cualquier tipo de datos en un catálogo. Estos datos suelen ser algún tipo de metadatos de tu empresa, como información sobre productos para una empresa de comercio electrónico, o información sobre cursos para un proveedor de educación.<br><br>En esta página se explica cómo preparar y cargar un archivo CSV para crear un catálogo, cómo administrar catálogos y mucho más.

Los casos de uso habituales de los catálogos incluyen:

- Productos
- Servicios
- Alimentación
- Próximos eventos
- Música
- Paquetes

Una vez importada esta información, puedes empezar a acceder a ella en los mensajes de forma similar a como accedes a los atributos personalizados o a las propiedades del evento personalizado a través de Liquid.

## Preparación del archivo CSV

Antes de crear un catálogo, asegúrese de tener listo su archivo CSV si su método preferido de creación de catálogos es cargarlo.

{% alert note %}
¿Necesitas más espacio para tus archivos CSV? Ponte en contacto con tu director de cuentas Braze para obtener más información sobre la actualización de tus catálogos.
{% endalert %}

### Directrices para archivos CSV

Tenga en cuenta estas directrices a la hora de crear su archivo CSV. La primera columna del archivo CSV debe ser una cabecera de `id`, y el `id` de cada artículo debe ser único. Todos los demás nombres de columna deben ser únicos. Además, se aplican las siguientes limitaciones a los archivos CSV de catálogo:

- Máximo de 1.000 campos (columnas)
- Nombre de campo (columna) máximo de 250 caracteres
- Máximo 100 MB para todos los archivos CSV combinados de su empresa (gratis)
- Tamaño máximo de archivo CSV de 2 GB (Pro)
- Valor máximo del campo (celda) de 5.000 caracteres
- Sólo letras, números, guiones y guiones bajos para `id` y valores de cabecera.

También recomendamos formatear todo el texto de los archivos CSV en minúsculas. Asegúrese de que está codificando su archivo CSV utilizando el formato UTF-8 para cargar su archivo CSV en el siguiente paso con éxito.

## Seleccionar tu método

Para crear un catálogo, vaya a **Configuración de datos** > **Catálogos**.

Selecciona **Crear nuevo catálogo** y, a continuación, elige **Cargar CSV** o **Crear en el navegador**.

### Método 1: Cargar CSV

1. Arrastra y suelta tu archivo en la zona de carga, o selecciona **Cargar CSV** y elige tu archivo. <br>![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"} <br><br>
2. Seleccione uno de los siguientes tipos de datos para cada columna: booleano, número, cadena o tiempo.
<br> ![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"} <br><br>
3. Dale un nombre a tu catálogo. Tenga en cuenta los siguientes requisitos para un nombre de catálogo:
- Debe ser único
- 250 caracteres como máximo
- Sólo puede incluir números, letras, guiones y guiones bajos.<br><br>
4. (Opcional) Añade una descripción para el catálogo.
5. Selecciona **Procesar Catálogo** para crear el catálogo.

{% alert note %}
Este tipo de datos no se puede editar una vez configurado el catálogo. Además, un valor `NULL` no es compatible con la carga de CSV y se tratará como una cadena.
{% endalert %}

También puede utilizar plantillas en un nombre de catálogo. Por ejemplo, puede utilizar lo siguiente:
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
Tu archivo CSV puede ser rechazado si superas tu [nivel](#tiers).
{% endalert %}

También puede actualizar el archivo CSV después de seleccionar crear un catálogo en el navegador. Selecciona **Actualizar catálogo > Cargar CSV** y, a continuación, selecciona si deseas actualizar, añadir o eliminar elementos de tu catálogo.

### Método 2: Crear en el navegador

Para editar o crear catálogos en el navegador, necesitarás el permiso "Gestionar panel de catálogos".

1. Introduzca un nombre para su catálogo. Ten en cuenta los siguientes requisitos para el nombre de tu catálogo:
- Debe ser único
- Hasta 250 caracteres
- Sólo puede incluir números, letras, guiones y guiones bajos. <br> ![Un catálogo llamado "mi_catálogo".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"} <br><br>
2. (Opcional) Escribe una descripción para tu catálogo.
3. Seleccione el catálogo que acaba de crear en la página de **catálogos** de la lista para actualizar su catálogo.
4. Selecciona **Actualizar Catálogo** > **Añadir campos** para añadir tus campos. A continuación, introduzca el **Nombre del campo** y utilice el desplegable para seleccionar el tipo de datos. Repita la operación según sea necesario.<br> ![Dos campos de ejemplo "tasa" y "nombre".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}<br><br>
5. Selecciona **Actualizar catálogo** > **Añadir elementos** para añadir un elemento a tu catálogo introduciendo la información en función de los campos que hayas añadido previamente. A continuación, selecciona **Guardar elemento** o **Guardar y añadir otro** para seguir añadiendo tus elementos. <br> ![Añade un elemento del catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

También puede cargar un archivo CSV después de seleccionar crear un catálogo en el navegador.

{% alert note %}
Braze procesa los valores de tiempo basándose en la marca de tiempo del cuadro de mandos. Por ejemplo, si una columna tiene el valor "13/03/2024" y su zona horaria es la zona horaria del Pacífico, esta hora se importaría a Braze como "12/03/2024, 17:00".
{% endalert %}

#### Tutorial: Creación de un catálogo a partir de un archivo CSV

Para este tutorial, vamos a utilizar un catálogo que enumera dos juegos, su coste y un enlace de imagen.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">título</th>
    <th class="tg-0pky">precio</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Cuentos</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneración</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Crearemos el catálogo cargando un archivo CSV. Los tipos de datos de `id`, `title`, `price` y `image_link` son cadena, cadena, número y cadena, respectivamente. 

{% alert note %}
Este tipo de datos no se puede editar una vez configurado el catálogo.
{% endalert %}

![Cuatro nombres de columnas de catálogo: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

A continuación, llamaremos a este catálogo "catálogo_juegos" y seleccionaremos el botón **Procesar catálogo**. Braze comprobará si hay errores en tu catálogo antes de crearlo.

![Un catálogo llamado "catálogo_juegos".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Tenga en cuenta que no podrá editar este nombre una vez creado el catálogo. Puede eliminar un catálogo y volver a cargar una versión actualizada utilizando el mismo nombre de catálogo.

Una vez creado el catálogo, puedes empezar a hacer referencia a [este en una campaña]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/).

## Gestión de catálogos a través de API

A medida que construya más catálogos, también puede utilizar el [punto final Lista de catálogos]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) para obtener una lista de los catálogos de un espacio de trabajo.

### Gestión de los elementos del catálogo

Además de gestionar sus catálogos, también puede utilizar puntos finales asíncronos y síncronos para gestionar los elementos del catálogo. Esto incluye la posibilidad de editar y eliminar elementos del catálogo, y de listar los detalles de los elementos del catálogo. 

Por ejemplo, si quieres editar un elemento individual del catálogo, puedes utilizar el [punto final `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Niveles del catálogo {#tiers}

La versión gratuita de Catálogos admite tamaños de archivo CSV de hasta 100 MB para todos los archivos CSV combinados de tu empresa, mientras que la versión Pro de Catálogos admite tamaños de archivo CSV de hasta 2 GB para un único archivo CSV.

### Almacenamiento de catálogos

{% alert important %}
El derecho a paquete que se muestra en el panel de Braze se redondea a la unidad más próxima por motivos visuales; sin embargo, sigues teniendo derecho a la totalidad del derecho adquirido. Para solicitar una actualización para el almacenamiento de catálogos, póngase en contacto con su gestor de cuenta Braze.
{% endalert %}

#### Versión gratuita

El tamaño de almacenamiento para la versión gratuita de los catálogos es de hasta 100 MB. Puedes tener un número ilimitado de objetos, siempre que no superen los 100 MB. 

#### Catálogos Pro

A nivel de empresa, el almacenamiento máximo para Catálogos Pro se basa en el tamaño de los datos del catálogo. Las opciones de tamaño de almacenamiento son: 5 GB, 10 GB o 15 GB. Ten en cuenta que el almacenamiento de la versión gratuita (100 MB) está incluido en cada uno de estos planes.

