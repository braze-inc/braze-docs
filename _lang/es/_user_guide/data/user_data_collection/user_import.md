---
nav_title: Importación de usuarios
article_title: Importación de usuarios
page_order: 4
description: "Infórmate sobre las distintas opciones de importación de usuarios de Braze, como la importación en CSV, la API REST, la ingesta de datos en la nube y mucho más."

---
# Importación de usuarios

> Infórmate sobre las distintas opciones de importación de usuarios de Braze, como la importación en CSV, la API REST, la ingesta de datos en la nube y mucho más.

## Acerca de la validación HTML

Ten en cuenta que Braze no sanea, valida ni reformatea los datos HTML durante la importación, lo que significa que las etiquetas de script deben eliminarse de todos los datos de importación que utilices para la personalización Web.

Al importar datos a Braze destinados específicamente al uso de personalización en un navegador web, asegúrese de que estén desprovistos de HTML, JavaScript o cualquier otra etiqueta de secuencia de comandos que pueda ser aprovechada de forma malintencionada al visualizarse en un navegador web.

Alternativamente, para HTML, puedes utilizar los filtros Braze Liquid (`strip_html`) para escapar caracteres HTML del texto representado. Por ejemplo:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Opciones de importación

### Importación CSV de Braze

Puedes utilizar la importación en CSV para registrar y actualizar los siguientes atributos de usuario y eventos personalizados. Para empezar, consulta [Importación de CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Tipo|Definición|Ejemplo|Tamaño máximo del archivo|
|---|---|---|---|
|Atributos predeterminados|Atributos de usuario reservados reconocidos por Braze.|`first_name`, `email`|500 MB|
|Atributos personalizados|Atributos de usuario únicos para tu empresa.|`last_destination_searched`|500 MB|
|Eventos personalizados|Eventos únicos de tu empresa que representan acciones de los usuarios.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Importación de usuarios Lambda en CSV

Puedes utilizar nuestro script de importación CSV de S3 Lambda sin servidor para cargar atributos de usuario en Braze. Esta solución funciona como un cargador de CSV en el que depositas tus CSV en un bucket de S3 y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un archivo con 1.000.000 de filas deberían rondar los cinco minutos. Consulte [Importación de atributos de usuario CSV a Braze](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) para obtener más información.

### API REST

Utiliza el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para registrar eventos personalizados, atributos de usuario y compras de usuarios.

### Ingesta de datos de Cloud

Utiliza [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/) Braze para importar y mantener los atributos de los usuarios.

## Correos electrónicos transaccionales legalmente requeridos

{% multi_lang_include email-via-sms-warning.md %}
