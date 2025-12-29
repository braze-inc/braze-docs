---
nav_title: Crear un catálogo
article_title: Crear un catálogo
alias: "/catalogs/"
page_order: 1
description: "Este artículo de referencia explica cómo crear catálogos que hagan referencia a datos de no usuarios en tus campañas Braze a través de Liquid."
---

# Crear un catálogo

> Crear un catálogo implica importar a Braze un archivo CSV de datos de no usuarios. Así podrás acceder a esa información para enriquecer tus mensajes. Puedes introducir cualquier tipo de datos en un catálogo. Estos datos suelen ser algún tipo de metadatos de tu empresa, como información sobre productos para una empresa de comercio electrónico, o información sobre cursos para un proveedor de educación.

## Casos de uso

Los casos de uso habituales de los catálogos incluyen:

- Productos
- Servicios
- Alimentación
- Próximos eventos
- Música
- Paquetes

Una vez importada esta información, puedes empezar a acceder a ella en los mensajes de forma similar a como accedes a los atributos personalizados o a las propiedades del evento personalizado a través de Liquid.

## Crear un catálogo

Para crear un catálogo, ve a **Configuración de Datos** > **Catálogos**, luego selecciona **Crear nuevo catálogo** y elige una de las siguientes opciones:

{% tabs local %}
{% tab Upload CSV %}
### Paso 1: Revisa tu archivo CSV

Antes de subir tu archivo CSV, asegúrate de que tu archivo CSV cumple los siguientes requisitos:

| Requisito CSV | Detalles |
|-----------------|---------|
| Cabeceras | La primera columna del archivo CSV debe llamarse `id`, y cada fila debe tener un valor único `id`. |
| Columnas | Un archivo CSV puede tener un máximo de 1.000 campos (columnas), y cada nombre de columna puede tener hasta 250 caracteres. |
| Tamaño del archivo | En los planes gratuitos, el tamaño total de todos los archivos CSV de una empresa está limitado a 100 MB. Para los planes Pro, el tamaño máximo de un archivo CSV es de 2 GB. |
| Valores de campo | Cada celda (valor de campo) puede contener hasta 5.000 caracteres. |
| Caracteres válidos | La columna `id` y todos los valores de cabecera sólo pueden contener letras, números, guiones y guiones bajos. |
| Tipos de datos | Los tipos de datos admitidos para subir un archivo CSV son cadena, entero, flotante, booleano o fecha-hora. |
| Formato | Formatea todo el texto en minúsculas para mantener la coherencia. |
| Codificación | Guarda y sube el archivo CSV utilizando la codificación UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
¿Necesitas más espacio para acomodar tus archivos CSV? Ponte en contacto con tu director de cuentas Braze para obtener más información sobre la actualización de tus catálogos.
{% endalert %}

### Paso 2: Cargar CSV

Arrastra y suelta tu archivo en la zona de carga, o selecciona **Cargar CSV** y elige tu archivo.

\![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Selecciona un tipo de datos para cada columna.

{% alert note %}
Este tipo de datos no se puede editar después de configurar tu catálogo. Además, un valor `NULL` no es compatible con la carga de CSV y se tratará como una cadena.
{% endalert %}

\![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Introduce un nombre y una descripción opcional para tu catálogo. Ten en cuenta los siguientes requisitos a la hora de nombrar tu catálogo:

  - Debe ser único
  - Máximo de 250 caracteres
  - Sólo puede incluir números, letras, guiones y guiones bajos

{% alert tip %}
También puedes [utilizar plantillas en el nombre de un](#template-catalog-names) catálogo, lo que te permite generar dinámicamente nombres de catálogo en función de variables como el idioma o la campaña.
{% endalert %}

\![Un catálogo llamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Selecciona **Procesar Catálogo** para crear el catálogo.

{% alert important %}
Tu archivo CSV puede ser rechazado si superas tu [nivel](#tiers).
{% endalert %}

### Tutorial: Crear un catálogo a partir de un archivo CSV

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

Crearemos el catálogo subiendo un archivo CSV. Los tipos de datos de `id`, `title`, `price` y `image_link` son cadena, cadena, número y cadena, respectivamente. 

{% alert note %}
Este tipo de datos no se puede editar después de configurar tu catálogo.
{% endalert %}

\![Cuatro nombres de columnas de catálogo: "id", "título", "precio", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

A continuación, llamaremos a este catálogo "games_catalog" y seleccionaremos el botón **Procesar catálogo**. A continuación, Braze comprobará si hay errores en el catálogo antes de crearlo.

\![Un catálogo llamado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Ten en cuenta que no podrás modificar este nombre una vez creado el catálogo. Puedes borrar un catálogo y volver a subir una versión actualizada utilizando el mismo nombre de catálogo.

Después de crear el catálogo, puedes empezar a hacer referencia al [catálogo en una campaña]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Requisitos previos

Para poder editar o crear catálogos en el navegador, necesitarás el permiso **Gestionar panel de catálogos**.

### Paso 1: Introduce los datos del catálogo

Introduce un nombre y una descripción opcional para tu catálogo. Ten en cuenta los siguientes requisitos a la hora de nombrar tu catálogo:

- Debe ser único
- Máximo de 250 caracteres
- Sólo puede incluir números, letras, guiones y guiones bajos

{% alert tip %}
También puedes [utilizar plantillas en el nombre de un](#template-catalog-names) catálogo, lo que te permite generar dinámicamente nombres de catálogo en función de variables como el idioma o la campaña.
{% endalert %}

\![Un catálogo llamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Paso 2: Crea tu catálogo

Selecciona tu catálogo de la lista y, a continuación, selecciona **Actualizar catálogo** > **Añadir campos**. Introduce el **Nombre del campo** y utiliza el desplegable para seleccionar el tipo de datos. Repítelo según sea necesario.

\![Dos campos de ejemplo "tasa" y "nombre".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Selecciona **Actualizar catálogo** > **Añadir artículos** para añadir un artículo a tu catálogo introduciendo la información en función de los campos que hayas añadido previamente. A continuación, selecciona **Guardar elemento** o **Guardar y añadir otro** para seguir añadiendo tus elementos.

Añade un elemento del catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze procesa los valores de tiempo basándose en la marca de tiempo del panel. Por ejemplo, si una columna tiene el valor "13/03/2024" y tu zona horaria es la del Pacífico, esta hora se importaría a Braze como "12/03/2024, 17:00".
{% endalert %}
{% endtab %}
{% endtabs %}

## Utilizar plantillas en los nombres de catálogo {#template-catalog-names}

Al dar nombre a tu catálogo, también puedes utilizar plantillas en el nombre del catálogo. Esto te permite generar dinámicamente nombres de catálogo en función de variables como el idioma o la campaña. Por ejemplo, puedes utilizar lo siguiente:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Administrador de catálogos

### En el panel de control

Para actualizar tu catálogo después de cargar un CSV o de crear un catálogo en el navegador, selecciona **Actualizar catálogo > Cargar CSV** y, a continuación, selecciona si deseas actualizar, añadir o eliminar elementos de tu catálogo.

### Utilizar la API REST

A medida que construyas más catálogos, también puedes utilizar el [punto final Listar catálogos]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) para obtener una lista de los catálogos de un espacio de trabajo.

Los tipos de datos admitidos para utilizar la API son: cadena, entero, flotante, booleano o fecha-hora. También puedes cargar matrices y objetos cuando gestiones tus catálogos con la API.

## Administrar elementos del catálogo

Además de gestionar tus catálogos, también puedes utilizar puntos finales asíncronos y síncronos para gestionar los elementos del catálogo. Esto incluye la posibilidad de editar y eliminar elementos del catálogo, y de listar los detalles de los elementos del catálogo. 

Por ejemplo, si quieres editar un elemento individual del catálogo, puedes utilizar el [punto final`/catalogs/catalog_name/items/item_id` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Almacenamiento de catálogos {#tiers}

La versión gratuita de Catálogos admite tamaños de archivo CSV de hasta 100 MB para todos los archivos CSV combinados de tu empresa, mientras que la versión Pro de Catálogos admite tamaños de archivo CSV de hasta 2 GB para un único archivo CSV.

{% alert important %}
El derecho a paquete que aparece en el panel de Braze se redondea a la unidad más próxima por motivos visuales; sin embargo, sigues teniendo derecho al derecho completo adquirido. Para solicitar una actualización del almacenamiento de catálogos, ponte en contacto con tu director de cuentas Braze.
{% endalert %}

#### Versión gratuita

El tamaño de almacenamiento para la versión gratuita de los catálogos es de hasta 100 MB. Puedes tener un número ilimitado de artículos siempre que no superen los 100 MB. 

#### Catálogos Pro

A nivel de empresa, el almacenamiento máximo para Catálogos Pro se basa en el tamaño de los datos del catálogo. Las opciones de tamaño de almacenamiento son: 5 GB, 10 GB o 15 GB. Ten en cuenta que el almacenamiento de la versión gratuita (100 MB) está incluido en cada uno de estos planes.
