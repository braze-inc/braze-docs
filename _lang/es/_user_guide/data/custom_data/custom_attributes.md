---
nav_title: Atributos personalizados
article_title: Atributos personalizados
page_order: 10
page_type: reference
description: "Esta página describe los atributos personalizados y explica los distintos tipos de datos de atributos personalizados."
search_rank: 1
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Atributos personalizados

> Esta página trata de los atributos personalizados, que son una colección de los rasgos únicos de tus usuarios. Los atributos personalizados son los mejores para almacenar atributos sobre sus usuarios, o información sobre acciones de poco valor dentro de su aplicación. 

Cuando se almacenan en Braze, los atributos personalizados pueden utilizarse para crear segmentos de audiencia y personalizar la mensajería mediante Liquid. Ten en cuenta que no almacenamos información de series temporales para los atributos personalizados, por lo que no podrás obtener ningún gráfico basado en ellos como puedes hacer con los eventos personalizados.

## Gestión de atributos personalizados

Para crear y gestionar atributos personalizados en el panel de control, vaya a **Configuración de datos** > **Atributos personalizados**. 

![Cuatro atributos personalizados que son booleanos.]({% image_buster /assets/img/export_custom_attributes.png %})

La columna **Última actualización** muestra la última vez que se editó el atributo personalizado, como la última vez que se configuró como lista de bloqueo o activo.

{% alert important %}
Para una correcta orientación del mensaje, asegúrate de que el tipo de datos de tu atributo personalizado coincide con el atributo personalizado real.
{% endalert %}

Desde esta página, puedes ver, gestionar, crear o bloquear atributos personalizados existentes. Seleccione el menú situado junto a un atributo personalizado para realizar las siguientes acciones:

### Agregando a la lista de bloqueo

Los atributos personalizados se pueden bloquear individualmente en el menú de acciones, o se pueden seleccionar hasta 100 atributos y bloquearlos en bloque. Si bloquea un atributo personalizado, no se recopilarán datos relativos a ese atributo, los datos existentes no estarán disponibles a menos que se reactiven y los atributos bloqueados no aparecerán en filtros ni gráficos. Además, si el atributo está referenciado actualmente por filtros o desencadenadores en otras áreas del panel de Braze, aparecerá un modal de advertencia explicando que todas las instancias de los filtros o desencadenadores que lo referencian serán eliminadas y archivadas.

### Marcar como información de identificación personal (PII)

Los administradores también pueden crear atributos personalizados y marcarlos como PII desde esta página. Estos atributos sólo serán visibles para los administradores y los usuarios del panel de control con el permiso "Ver atributos personalizados marcados como PII".

### Añadir descripciones

Puede añadir una descripción a un atributo personalizado después de crearlo si dispone del [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases`. Edita el atributo personalizado e introduce lo que quieras, como una nota para tu equipo.

### Añadir etiquetas

Puede añadir etiquetas a un atributo personalizado después de crearlo si dispone del [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)"Gestionar eventos, atributos, compras". Las etiquetas pueden utilizarse para filtrar la lista de atributos. 

### Eliminar atributos personalizados

Hay dos formas de eliminar los atributos personalizados de los perfiles de usuario:

* Seleccione el nombre del atributo personalizado que se eliminará en un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes).
* Establece el valor `null` en tu solicitud de API al [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Visualización de informes de uso

El informe de uso enumera todos los Canvases, campañas y segmentos que utilizan un atributo personalizado específico. Esta lista no incluye los usos de Liquid. 

Puedes ver hasta 100 informes de uso a la vez seleccionando las casillas de verificación situadas junto a los respectivos atributos personalizados y, a continuación, seleccionando **Ver informe de uso**.

### Exportar datos

Para exportar la lista de atributos personalizados como archivo CSV, seleccione **Exportar todo** en la parte superior de la página. Se generará el archivo CSV y se le enviará por correo electrónico un enlace de descarga.

## Establecer atributos personalizados

A continuación se enumeran los métodos utilizados en varias plataformas para establecer atributos personalizados.

{% details Ampliar para documentación por plataforma %}

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Almacenamiento de atributos personalizados

Todos los datos almacenados en el **perfil de usuario**, incluidos los datos de atributos personalizados, se conservan indefinidamente mientras cada perfil esté [activo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users).

## Tipos de datos de atributos personalizados

Los atributos personalizados son herramientas extraordinariamente flexibles que permiten una gran segmentación.

Los siguientes tipos de datos pueden almacenarse como atributos personalizados:

- [Booleanos](#booleans)
- [Números](#numbers)
- [Cadenas](#strings)
- [Matrices](#arrays)
- [Tiempo](#time)
- [Objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Matrices de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Booleanos (verdadero/falso) {#booleans}

Los atributos booleanos son útiles para almacenar datos binarios sencillos sobre sus usuarios, como los estados de suscripción. Puedes encontrar usuarios que explícitamente tienen una variable establecida a un valor verdadero o falso, además de aquellos que aún no tienen ningún registro de ese atributo.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprueba si el valor booleano **es** verdadero, falso, verdadero o no establecido, o falso o no establecido. | **ES**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, o **FALSE OR NOT SET** | Si este filtro especifica `coffee_drinker`, un usuario coincidirá con este filtro en las siguientes circunstancias: <br> {::nomarkdown}<ul><li>Si este filtro es <code>true</code> y el usuario tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>false</code> y el usuario no tiene el valor <code>coffee_drinker</code></li><li>Si este filtro es <code>true or not set</code> y el usuario tiene el valor <code>coffee_drinker</code> o ningún valor</li><li>Si este filtro es <code>false or not set</code> y el usuario no tiene <code>coffee_drinker</code> o cualquier valor</li></ul>{:/} |
| Comprueba si el valor booleano **existe** en el perfil de un usuario y no es nulo | **NO ESTÁ EN BLANCO**  | **N/A** | Si este filtro especifica `coffee_drinker` y un usuario tiene un valor para el atributo `coffee_drinker`, el usuario coincidirá con este filtro. | 
| Comprueba si el valor booleano **no existe** en el perfil de un usuario o es nulo | **ESTÁ EN BLANCO**  | **N/A** | Si este filtro especifica `coffee_drinker`y un usuario no tiene el atributo `coffee_drinker` o el valor de `coffee_drinker` es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Números {#numbers}

Los atributos numéricos incluyen [números enteros](https://en.wikipedia.org/wiki/Integer) y [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic), y tienen una amplia variedad de casos de uso. Los atributos personalizados de número incremental son útiles para almacenar el número de veces que se ha producido una acción o evento determinado sin que cuente para el límite de datos. Los números estándar tienen todo tipo de usos, como la grabación:

- Número de calzado
- Talla de cintura
- Número de veces que un usuario ha visto una determinada característica o categoría de producto

{% alert tip %}
El dinero gastado no debe registrarse por este método. Más bien debe registrarse a través de nuestros [métodos de compra](#purchase-revenue-tracking).
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo numérico **es exactamente** un **número**| **EXACTAMENTE** | **NÚMERO** | Si este filtro especifica `10` y un perfil de usuario tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprueba si el atributo numérico **no es igual a** un **número**| **NO ES IGUAL A** | **NÚMERO** | Si este filtro especifica `10` y un perfil de usuario no tiene el valor `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es más que** un **número**| **MÁS DE** | **NÚMERO** | Si este filtro especifica `10` y un perfil de usuario tiene un valor superior a `10`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo numérico **es menor que** un **número**| **MENOS DE** | **NÚMERO** | Si este filtro especifica `10` y un perfil de usuario tiene un valor inferior a `10`, el usuario coincidirá con este filtro. |
| Comprueba si el atributo numérico **existe** en el perfil de un usuario y no es nulo | **NO ESTÁ EN BLANCO** | **N/A** | Si un perfil de usuario contiene el atributo numérico especificado, independientemente de su valor, el usuario coincidirá con este filtro. |
| Comprueba si el atributo numérico **no existe** en el perfil de un usuario o es nulo | **ESTÁ EN BLANCO** | **N/A** | Si un perfil de usuario no contiene el atributo numérico especificado o el valor del atributo es nulo, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalles del atributo número

- Los filtros "Exactamente 0" y "Menos que" incluyen usuarios con campos NULL
  - Para excluir a los usuarios sin un valor para los atributos personalizados, debe incluir el filtro **no está en blanco**.

### Cadenas (caracteres alfanuméricos) {#strings}

Los atributos de cadena son útiles para almacenar entradas del usuario, como una marca favorita, un número de teléfono o una última cadena de búsqueda dentro de su aplicación. Los atributos de cadena pueden tener hasta 255 caracteres.

Tenga en cuenta que si introduce valores con espacios entre, antes o después de las palabras, Braze también comprobará si existen los mismos espacios.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprueba si el atributo string **coincide exactamente con** una cadena introducida| **IGUAL A** | **CADENA**<br>Distingue entre mayúsculas y minúsculas | Si este filtro especifica `book` y un perfil de usuario tiene un atributo de cadena para `last_item_purchased` que contiene `book`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de cadena **coincide parcialmente con** una cadena introducida **O** Expresión regular | **COINCIDE CON REGEX** | **STRING** **O** **EXPRESIÓN REGULAR** <br>No distingue mayúsculas de minúsculas; máximo 32.764 caracteres | 
| Comprueba si el atributo cadena **no coincide parcialmente con** una cadena introducida **O** una expresión regular | **NO COINCIDE CON LA EXPRESIÓN REGULAR** \* | **STRING** **O** **EXPRESIÓN REGULAR**<br>No distingue mayúsculas de minúsculas; máximo 32.764 caracteres |
| Comprobar si el atributo string **no coincide con** una cadena introducida| **NO ES IGUAL A** | **CADENA**<br>No se distingue entre mayúsculas y minúsculas  | Si este filtro especifica `book` y un perfil de usuario tiene un atributo de cadena para `last_item_purchased` que no contiene `book`, el usuario coincidirá con este filtro.|
| Comprueba si el atributo string **existe** en el perfil de un usuario y no es una cadena vacía | **NO ESTÁ EN BLANCO** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro independientemente del valor de su atributo. Por ejemplo, el usuario puede tener `sci-fi`, `romance`, u otro valor.|
| Comprobar si el atributo string **no existe** en el perfil de un usuario | **EN BLANCO** | **N/A** | Si este filtro especifica `favorite_genre` y un perfil de usuario no tiene el atributo `favorite_genre`, el usuario coincidirá con este filtro.|
| Comprueba si la cadena coincide exactamente con **alguna** de las cadenas introducidas | **ES CUALQUIERA DE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varias cadenas (256 como máximo) | Si este filtro especifica `book`, `bookmark`, y `reading light`, y un perfil de usuario tiene al menos una de esas cadenas, el usuario coincidirá con este filtro. |
| Comprueba si el atributo de cadena **no coincide exactamente con ninguna** de las cadenas introducidas | **NO ES NINGUNO DE** |**CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varias cadenas (256 como máximo) | Si este filtro especifica `book`, `bookmark`, y `reading light`, y un perfil de usuario no contiene ninguna de esas cadenas, el usuario coincidirá con el filtro.|
| Comprueba si el atributo string **coincide parcialmente con alguna** de las cadenas introducidas | **CONTIENE CUALQUIERA DE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varias cadenas (256 como máximo) | Si este filtro especifica `gold` y un perfil de usuario contiene `gold` en cualquier cadena, como `gold_tier` o `former_gold_tier`, el usuario coincidirá con el filtro. |
| Comprueba si el atributo string **no coincide parcialmente con ninguna** de las cadenas introducidas | **NO CONTIENE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varias cadenas (256 como máximo) | Si este filtro especifica `gold` y un perfil de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Una cadena de fecha como "12-1-2021" o "12/1/2021" se convertirá en un objeto datetime y se tratará como un [atributo de hora]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% alert important %}
Al segmentar utilizando el filtro **DOES NOT MATCH REGEX**, debe tener ya un atributo personalizado con un valor asignado en ese perfil de usuario. Braze sugiere utilizar la lógica "OR" para comprobar si un atributo personalizado está en blanco para asegurarse de que los usuarios están siendo dirigidos correctamente.
{% endalert %}

### Matrices {#arrays}

Los atributos de matriz son buenos para almacenar listas relacionadas de información sobre sus usuarios. Por ejemplo, almacenar en una matriz los últimos 100 contenidos vistos por un usuario permitiría segmentar por intereses específicos.

Por defecto, la longitud de una matriz para un atributo es de hasta 500 elementos. Por ejemplo, si envías un atributo como "Películas vistas" y está establecido en 500, cuando un usuario vea la película 501, se eliminará la primera película de la matriz y se añadirá la película más reciente.

Ten en cuenta que si introduces algún valor con espacios entre, antes o después de las palabras, Braze también comprobará si existen los mismos espacios.

{% alert note %}
La opción de aumentar la longitud máxima no estará disponible si el atributo está configurado para detectar automáticamente el tipo de datos; el tipo de datos debe estar configurado como array.
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprueba si el atributo array **incluye un valor que coincide exactamente con** un valor introducido| **INCLUYE VALOR** | **CADENA** | Si este filtro especifica `sci-fi` y un perfil de usuario tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprueba si el atributo de la matriz **no incluye un valor que coincida exactamente con** un valor introducido| **NO INCLUYE EL VALOR** | **CADENA** | Si este filtro especifica `sci-fi` y un perfil de usuario no tiene el valor `sci-fi`, el usuario coincidirá con este filtro.|
| Comprueba si el atributo array **contiene un valor que coincide parcialmente con** un valor introducido **O** Expresión Regular | **COINCIDE CON REGEX** | **STRING** **O** **EXPRESIÓN REGULAR**<br>Máximo de 32.764 caracteres | |
| Comprueba si el atributo array **tiene algún valor** o no está vacío | **TIENE UN VALOR** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario contiene `favorite_genres` con cualquier valor, el usuario coincidirá con este filtro. |
| Comprobar si el atributo array **está vacío** o no existe | **ESTÁ VACÍO** | **N/A** | Si este filtro especifica `favorite_genres` y un perfil de usuario no contiene `favorite_genres` o contiene `favorite_genres` pero no tiene valores, el usuario coincidirá con este filtro.|
| Comprueba si el atributo del array **incluye un valor que coincide exactamente con cualquiera** de los valores introducidos | **INCLUYE CUALQUIERA DE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene cualquier combinación de `sci-fi`, `fantasy`, o `romance`, incluyendo sólo una de ellas (como sólo `sci-fi`). Un usuario puede tener `horror` u otro valor en su cadena si también tiene alguno de `sci-fi`, `fantasy`, y `romance`.|
| Comprobar si el atributo de la matriz **no incluye un valor que coincida exactamente con cualquiera** de los valores introducidos. | **NO INCLUYE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene ninguna combinación de `sci-fi`, `fantasy`, o `romance`, el usuario coincidirá con este filtro. El usuario puede tener `horror` u otro valor si no tiene ninguno de `sci-fi`, `fantasy`, o `romance`.|
| Comprueba si el atributo del array **contiene un valor que coincide parcialmente con alguno** de los valores introducidos | **CONTIENEN CUALQUIERA DE LOS VALORES** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo) | Si este filtro especifica `gold` y una matriz de perfiles de usuario contiene `gold` en al menos una cadena, el usuario coincidirá con este filtro. Esto incluye valores de cadena como `gold_tier`, `former_gold_tier` y otros.|
| Comprobar si el atributo de la matriz **no incluye un valor que coincida parcialmente con alguno** de los valores introducidos. | **NO CONTIENEN NINGUNO DE LOS VALORES** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo) | Si este filtro especifica `gold` y una matriz de perfiles de usuario no contiene `gold` en ninguna cadena, el usuario coincidirá con este filtro. Esto significa que los usuarios con valores de cadena como `gold_tier` y `former_gold_tier` no coincidirán con este filtro.|
| Comprueba si el atributo array **incluye todos** los valores introducidos | **ES TODO DE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo) | Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario tiene todos esos valores, el usuario coincidirá con este filtro. El usuario también puede tener `horror` u otros valores y coincidir con este filtro.|
| Comprueba si el atributo array **no incluye todos** los valores introducidos | **NO ES TODO DE** | **CADENA**<br>Distingue entre mayúsculas y minúsculas; admite varios valores (256 como máximo)|  Si este filtro especifica `sci-fi, fantasy, romance` y un perfil de usuario no tiene todos esos valores, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Para saber más sobre cómo utilizar expresiones regulares (regex), consulta estos recursos:
- [Expresiones regulares compatibles con Perl (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex con Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador y comprobador de regex](https://www.regex101.com/)
- [Tutorial regex](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Tiempo {#time}

Los atributos de tiempo son útiles para almacenar la última vez que se realizó una acción específica, de modo que pueda ofrecer a sus usuarios mensajes de reenganche específicos del contenido.

Los filtros temporales que utilizan fechas relativas (por ejemplo, hace más de 1 día, hace menos de 2 días) miden 1 día como 24 horas. Cualquier campaña que ejecute utilizando estos filtros incluirá a todos los usuarios en incrementos de 24 horas. Por ejemplo, `last used app more than 1 day ago` captará a todos los usuarios que "hayan utilizado la aplicación por última vez más de 24 horas" desde el momento exacto en que se ejecute la campaña. Lo mismo ocurrirá con las campañas establecidas con intervalos de fechas más largos: cinco días desde la activación significarán las 120 horas anteriores.

Por ejemplo, para crear un segmento dirigido a usuarios con un atributo de tiempo entre 24 y 48 horas en el futuro, aplique los filtros `in more than 1 day in the future` y `in less than 2 days in the future`.

{% alert warning %}
La última fecha en la que se produjo un evento personalizado o un evento de compra se registra automáticamente y no debería volver a registrarse a través de un atributo de tiempo personalizado.
{% endalert %}

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprobar si el atributo de tiempo **es anterior a** una **fecha seleccionada**| **ANTES** | **SELECTOR DE FECHAS DEL CALENDARIO** | Si este filtro especifica `2024-01-31` y el perfil de un usuario tiene una fecha anterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprobar si el atributo de tiempo **es posterior a** una **fecha seleccionada**| **DESPUÉS DE** | **SELECTOR DE FECHAS DEL CALENDARIO** | Si este filtro especifica `2024-01-31` y el perfil de un usuario tiene una fecha posterior a `2024-1-31`, el usuario coincidirá con este filtro. |
| Comprueba si el atributo de tiempo es **más de X número** de **días atrás** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** | Si este filtro especifica `7` y el perfil de un usuario tiene una fecha de hace más de siete días, el usuario coincidirá con este filtro. |
| Comprueba si el atributo de tiempo es **menos de X número** de **días atrás**| **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** | Si este filtro especifica `7` y el perfil de un usuario tiene una fecha de hace menos de siete días, el usuario coincidirá con este filtro.|
| Compruebe si el atributo de tiempo está **en más de X número** de **días en el futuro** | **EN MÁS DE** | **NÚMERO DE DÍAS EN EL FUTURO** | Si este filtro especifica `7` y el perfil de un usuario tiene una fecha de más de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprueba si el atributo de tiempo es **menos de X número** de **días en el futuro** | **EN MENOS DE** | **NÚMERO DE DÍAS EN EL FUTURO**  | Si este filtro especifica `7` y el perfil de un usuario tiene una fecha de menos de siete días en el futuro, el usuario coincidirá con este filtro.|
| Comprueba si el atributo de tiempo **existe** en el perfil de un usuario y no es nulo | **NO ESTÁ EN BLANCO** | **N/A** | Si este filtro especifica un atributo de tiempo que está en un perfil de usuario, el usuario coincidirá con este filtro.|
| Comprueba si el atributo de tiempo **no existe** en el perfil de un usuario o es nulo | **ESTÁ EN BLANCO** | **N/A** | Si este filtro especifica un atributo de tiempo que no está en un perfil de usuario, el usuario coincidirá con este filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Detalles de los atributos de tiempo

- Día del evento recurrente
  - Cuando utilice el filtro "Día del evento recurrente" y se le pida que seleccione el "Día del calendario del evento recurrente", si selecciona `IS LESS THAN` o `IS MORE THAN`, se contará la fecha actual para ese filtro de segmentación.
  - Por ejemplo, si el 10 de marzo de 2020 ha seleccionado la fecha del atributo `LESS THAN ... March 10, 2020`, se tendrán en cuenta los atributos de los días hasta el 10 de marzo de 2020 inclusive. 
- Hace menos de X días: El filtro "Hace menos de X días" incluye las fechas comprendidas entre hace X días y la fecha/hora actual.
- Menos de X días en el futuro: Incluye fechas entre la fecha/hora actual y X días en el futuro.

### Objetos

Puede utilizar atributos personalizados anidados para enviar objetos como tipo de datos para atributos personalizados. Para más información, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Matrices de objetos

Utilice una matriz de objetos para agrupar atributos relacionados. Para más detalles, consulte nuestro artículo sobre [Array de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Operadores consolidados

Hemos consolidado la lista de operadores disponibles para usar en filtros de atributos, filtros de atributos personalizados y filtros de atributos personalizados anidados. Si dispone de filtros que utilicen estos operadores, se actualizarán automáticamente para utilizar los nuevos operadores.

| Tipo de datos | Operador antiguo | Operador nuevo | Valor |
| --- | --- | --- | --- |
| Cadena | equivale a | es uno de | Al menos un valor |
| Cadena | no equivale a | no es ninguno de | Al menos un valor |
| Matriz | incluye el valor | incluye uno de | Al menos un valor |
| Matriz | no incluye el valor | no incluye ninguno de | Al menos un valor |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Seguimiento de compras e ingresos {#purchase-revenue-tracking}

El uso de nuestros métodos de compra para registrar las compras dentro de la aplicación establece el valor de por vida (LTV) para cada perfil de usuario individual. Estos datos pueden consultarse en nuestra página de ingresos en series temporales.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada | Ejemplos |
| ---------------------| --------------- | ------------- | -------- |
| Comprueba si el total de dólares gastados **es mayor que** un **número**| **MAYOR QUE** | **NÚMERO** | Si este filtro especifica `500` y un perfil de usuario tiene un valor superior a `500`, el usuario coincidirá con este filtro. |
| Comprueba si el número total de dólares gastados **es menor que** un **número**| **MENOS DE** | **NÚMERO** | Si este filtro especifica `500` y un perfil de usuario tiene un valor inferior a `500`, el usuario coincidirá con este filtro.|
| Comprueba si el total de dólares gastados **es exactamente** un **número**| **EXACTAMENTE** | **NÚMERO** | Si este filtro especifica `500` y un perfil de usuario tiene el valor `500`, el usuario coincidirá con este filtro. |
| Compruebe si la última compra se **produjo después de X fecha** | **DESPUÉS DE** | **TIME** | Si este filtro especifica `2024/31/1` y la última compra de un usuario fue posterior a `2024/31/1`, el usuario coincidirá con este filtro.|
| Compruebe si la última compra se produjo **antes de X fecha** | **ANTES** | **TIME** | Si este filtro especifica `2024/31/1` y la última compra de un usuario fue antes de `2024/31/1`, el usuario coincidirá con este filtro.|
| Compruebe si la última compra se **produjo hace más de X días** | **MÁS DE** | **TIME** | Si este filtro especifica `7` y la última compra de un usuario fue hace más de siete días a partir de hoy, el usuario coincidirá con este filtro.|
| Compruebe si la última compra se produjo **hace menos de X días** | **MENOS DE** | **TIME** |  Si este filtro especifica `7` y la última compra de un usuario fue hace menos de siete días a partir de hoy, el usuario coincidirá con este filtro.|
| Compruebe si la compra se ha producido **más de X (máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |  Si este filtro especifica `7` veces y `21` días, y un usuario realizó más de siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
| Compruebe si la compra se ha producido **menos de X (máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** | Si este filtro especifica `7` veces y `21` días, y un usuario realizó menos de siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
| Compruebe si la compra se ha producido **exactamente X (máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** | Si este filtro especifica `7` veces y `21` días, y un usuario realizó siete compras en los últimos 21 días, el usuario coincidirá con este filtro.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Si desea segmentar en función del número de veces que se ha producido una compra específica, también deberá registrar dicha compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes).
{% endalert %}

Puede cambiar el tipo de datos de su atributo personalizado, pero debe ser consciente de las repercusiones de [cambiar los tipos de datos]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/).

