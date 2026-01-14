---
nav_title: Filtros
article_title: Filtros para líquidos
page_order: 3
description: "Esta página de referencia enumera los filtros que pueden utilizarse para reformatear contenido estático o dinámico."

---

# Filtros

> Este artículo de referencia ofrece un resumen de los filtros en Liquid y explica qué filtros son compatibles con Braze. ¿Buscas ideas sobre cómo puedes utilizar estos filtros? Consulta nuestra [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Con los filtros puedes modificar la salida de números, cadenas, variables y objetos en Liquid. Puedes utilizar filtros para reformatear texto estático o dinámico, como cambiar una cadena de minúsculas a mayúsculas o realizar operaciones matemáticas, como sumas o divisiones.

{% alert important %}
Braze no es compatible con todos los filtros Liquid de Shopify. Esta página intenta describir los filtros Liquid que Braze ha probado, pero puede que no sea una lista completa. Prueba siempre tu Liquid antes de enviar cualquier mensaje. <br><br>Si tienes alguna pregunta sobre un filtro que no aparece aquí, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Sintaxis del filtro

{% raw %}

Los filtros deben colocarse dentro de una etiqueta de salida `{{ }}` y se denotan mediante un carácter de tubo `|`.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

En este ejemplo, `Big Sale` es una cadena, y `upcase` es el filtro que se está aplicando.

### Sintaxis para filtros múltiples

Puedes utilizar varios filtros en una salida. Se aplican de izquierda a derecha.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de matriz

Los filtros de matrices se utilizan para modificar la salida de las matrices.

| Filtrar               | Definición                                                                                                         | Apoyado |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [únete a](https://shopify.dev/docs/api/liquid/filters/join)          | Une los elementos de una matriz con el carácter pasado como parámetro. El resultado es una sola cadena.          | ✅ Sí   |
| [primero](https://shopify.dev/docs/api/liquid/filters/first)         | Devuelve el primer elemento de una matriz. En una matriz de atributos personalizada, es el valor añadido más antiguo.                | ✅ Sí   |
| [último](https://shopify.dev/docs/api/liquid/filters/last)          | Devuelve el último elemento de una matriz. En una matriz de atributos personalizada, es el valor añadido más recientemente.          | ✅ Sí   |
| [compacto](https://shopify.dev/api/liquid/filters/compact)       | Elimina los elementos `nil` de una matriz.                                                                             | ✅ Sí   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Combina una matriz con otra matriz.                                                                              | ✅ Sí   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Devuelve el elemento en la ubicación del índice especificado en una matriz. El primer elemento de una matriz se referencia con `[0]`. | ⛔ No   |
| [mapear](https://shopify.dev/api/liquid/filters/map)           | Acepta el atributo de un elemento de la matriz como parámetro y crea una matriz con el valor de cada elemento de la matriz.        | ✅ Sí   |
| [invertir](https://shopify.dev/api/liquid/filters/reverse)       | Invierte el orden de los elementos de una matriz.                                                                       | ✅ Sí   |
| [talla](https://shopify.dev/api/liquid/filters/size)          | Devuelve el tamaño de una cadena (el número de caracteres) o de una matriz (el número de elementos).                      | ✅ Sí   |
| [ordenar](https://shopify.dev/api/liquid/filters/sort)         | Ordena los elementos de una matriz según un atributo dado de un elemento de la matriz.                                    | ✅ Sí   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Ordena los elementos de una matriz por orden alfabético sin distinguir mayúsculas de minúsculas.                                                | ✅ Sí   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Elimina las instancias duplicadas de los elementos de una matriz.                                                           | ✅ Sí   |
| [donde](https://shopify.dev/api/liquid/where)        | Filtra una matriz para que sólo incluya elementos con un valor de propiedad específico.                                             | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros de color

[Los filtros de color](https://shopify.dev/api/liquid/filters/color-filters) no son compatibles con Braze.

## Filtros de fuentes

[Los filtros de fuentes](https://shopify.dev/api/liquid/filters/font-filters) no son compatibles con Braze.

## Filtros matemáticos

Los filtros matemáticos te permiten realizar operaciones matemáticas. Si utilizas varios filtros en una salida, se aplicarán de izquierda a derecha.

| Filtrar  | Definición      | Apoyado |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Devuelve el valor absoluto de un número.     | ✅ Sí   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Limita un número a un valor máximo.   | ✅ Sí   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Limita un número a un valor mínimo.   | ✅ Sí   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Redondea una salida al entero más próximo.  | ✅ Sí   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Divide una salida por un número. La salida se redondea al número entero más próximo. Comprueba el siguiente consejo para evitar el redondeo. | ✅ Sí   |
| [suelo](https://shopify.dev/api/liquid/filters/floor)      | Redondea una salida al entero más próximo.        | ✅ Sí   |
| [menos](https://shopify.dev/api/liquid/filters/minus)      | Resta un número de una salida.          | ✅ Sí   |
| [más](https://shopify.dev/api/liquid/filters/plus)       | Añade un número a una salida.     | ✅ Sí   |
| [redonda](https://shopify.dev/api/liquid/filters/round)      | Redondea la salida al número entero más próximo o al número especificado de decimales.  | ✅ Sí   |
| [veces](https://shopify.dev/api/liquid/filters/times)     | Multiplica una salida por un número.       | ✅ Sí   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Divide una salida por un número y devuelve el resto.   | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Al dividir enteros (números enteros) entre enteros en Liquid, si la respuesta es un flotante (número con un decimal), Liquid redondeará automáticamente hacia abajo al entero más próximo. Sin embargo, dividir enteros por flotantes siempre te dará un flotante. Eso significa que puedes convertir tus enteros en un flotador (1,0, 2,0, 3,0) para devolver un flotador.
{% raw %}
<br><br>Por ejemplo,`{{15 | divided_by: 2}}` dará como resultado `7`, mientras que `{{15 | divided_by: 2.0}}` dará como resultado `7.5`.
{% endraw %}
{% endalert %}

### Operaciones matemáticas con atributos personalizados

Ten en cuenta que no puedes realizar operaciones matemáticas entre dos atributos personalizados.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Este ejemplo no funcionaría porque no puedes hacer referencia a varios atributos personalizados en una línea de Liquid. En lugar de eso, tendrías que asignar una variable al menos a uno de esos valores antes de que tengan lugar las funciones matemáticas. Añadir dos atributos personalizados juntos requeriría dos líneas de Liquid:

1. Uno para asignar el atributo personalizado a una variable,
2. Uno para realizar la adición.

#### Casos de uso: Calcular el balance de corriente

Supongamos que queremos calcular el saldo actual de un usuario sumando el saldo de su tarjeta regalo y el saldo de recompensas.

1. Utiliza la etiqueta `assign` para sustituir el atributo personalizado de `current_rewards_balance` por el término "saldo". Esto significa que ahora tienes una variable llamada `balance`, que puedes manipular.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2\. Utiliza el filtro `plus` para combinar el saldo de la tarjeta regalo de cada usuario con su saldo de recompensas, indicado por el objeto `{{balance}}`.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de dinero

Si vas a poner al día a un usuario sobre su compra, el saldo de una cuenta o cualquier otra cosa relacionada con el dinero, debes utilizar filtros de dinero. Los filtros de dinero garantizan que tus decimales estén en el lugar adecuado y que no se pierda ningún fragmento de tu actualización (como ese molesto `0` al final).

| Filtrar         | Definición          | Apoyado |
| :--------------- | :--------------- | :-------- |
| [dinero](https://shopify.dev/api/liquid/filters/money)      | Formatea los números para asegurarte de que los decimales están en el lugar correcto y de que no se han eliminado ceros al final de ningún número.   | ✅ Sí   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formatea los números con el símbolo de moneda.     | ⛔ No    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formatea los números sin el símbolo de moneda.      | ⛔ No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para formatear correctamente un número con el filtro `money`, elimina las comas del número y añade el filtro `plus: 0` antes del filtro `money`. Por ejemplo, mira el siguiente Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtrar dinero en Shopify frente a filtrar dinero en Braze

{% alert warning %}
El comportamiento del filtro `money` de Shopify difiere de cómo se utiliza en Braze. Consulta los siguientes ejemplos para obtener una descripción precisa del comportamiento esperado.
{% endalert %}

{% raw %}
En caso de que introduzcas un atributo personalizado (como `account_balance`), debes utilizar siempre el filtro `money` para colocar los decimales en el lugar adecuado y evitar que los ceros caigan al final de los números:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| CON EL FILTRO DE DINERO                       | SIN EL FILTRO DE DINERO                    |
| :------------------------------------------ | :------------------------------------------ |
| Con filtro de dinero]({% image_buster /assets/img/with_money_filter.png %})                     | \![Sin filtro de dinero]({% image_buster /assets/img/without_money_filter.png %})                  |
| Donde `account_balance` se introduce en `17.8`. | Donde `account_balance` se introduce en `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

El filtro `money` de Braze difiere del de Shopify porque no aplica automáticamente los decimales según una configuración preestablecida. Por ejemplo, tomemos el siguiente escenario en el que `rewards_redeemed` contiene un valor de `145`:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Según el filtro de [dinero](https://shopify.dev/api/liquid/filters/money) de Shopify, esto debería tener una salida de `$1.45`, sin embargo en Braze, esto tendrá una salida de `$145.00`. Como solución, podemos utilizar el filtro `divided_by` para manipular el número y convertirlo en decimal, antes de aplicar el filtro de dinero:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de cadena

Los filtros de cadenas se utilizan para manipular las salidas y variables de las cadenas. Las cadenas son una combinación de caracteres alfanuméricos y deben ir entre comillas rectas.

{% alert note %}
Las comillas rectas son diferentes de las comillas rizadas en Liquid. Ten cuidado al copiar y pegar Liquid de un editor de texto en Braze, ya que las comillas rizadas provocarán errores con tu Liquid. Si escribes tu Liquid directamente en Braze, las comillas rectas se aplicarán automáticamente.
{% endalert %}

| Filtrar          | Descripción     | Apoyado |
| :--------------- | ------------- | --------- |
| [añade](https://shopify.dev/api/liquid/filters/append)     | Añade caracteres a una cadena.           | ✅ Sí   |
| [cameliza](https://shopify.dev/docs/api/liquid/filters/camelize)     | Convierte una cadena a CamelCase.             | ⛔ No    |
| [escribe en mayúsculas](https://shopify.dev/api/liquid/filters/capitalize)     | Pone en mayúsculas la primera palabra de una cadena y en minúsculas el resto de caracteres.         | ✅ Sí   |
| [bajar el caso](https://shopify.dev/api/liquid/filters/downcase)      | Convierte una cadena a minúsculas.         | ✅ Sí   |
| [escapar](https://shopify.dev/api/liquid/filters/escape)    | Escapa de una cadena.             | ✅ Sí   |
| [Manipula](https://shopify.dev/api/liquid/filters/handleize)        | Convierte una cadena en un asa.        | ⛔ No    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Convierte una cadena en un hash MD5. Para más información, consulta [Filtros de codificación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).   | ✅ Sí   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Convierte una cadena en un hash SHA-1. Para más información, consulta [Filtros de codificación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters).  | ✅ Sí   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Convierte una cadena en un hash SHA-1 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. Para más información, consulta [Filtros de codificación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters). | ✅ Sí   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Convierte una cadena en un hash SHA-256 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro.       | ✅ Sí   |
| hmac_sha512 | Convierte una cadena en un hash SHA-512 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. | ✅ Sí  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Inserta una etiqueta HTML de salto de línea `<br>` delante de cada salto de línea de una cadena.        | ✅ Sí   |
| [pluraliza](https://shopify.dev/api/liquid/filters/pluralize)   | Muestra la versión singular o plural de una cadena inglesa en función del valor de un número.      | ⛔ No    |
| [añade](https://shopify.dev/api/liquid/filters/prepend)     | Añade caracteres a una cadena.      | ✅ Sí   |
| [elimina](https://shopify.dev/api/liquid/filters/remove)      | Elimina todas las apariciones de una subcadena de una cadena.       | ✅ Sí   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Elimina sólo la primera aparición de una subcadena de una cadena.      | ✅ Sí   |
| [sustituye](https://shopify.dev/api/liquid/filters/replace)        | Sustituye todas las apariciones de una cadena por una subcadena.   | ✅ Sí   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Sustituye la primera aparición de una cadena por una subcadena.      | ✅ Sí   |
| [cortar](https://shopify.dev/api/liquid/filters/slice)       | El filtro de trozos devuelve una subcadena que empieza en el índice especificado.       | ✅ Sí   |
| [dividir](https://shopify.dev/api/liquid/filters/split)  | El filtro dividir toma una subcadena como parámetro. La subcadena se utiliza como delimitador para dividir una cadena en una matriz.            | ✅ Sí   |
| [tira](https://shopify.dev/api/liquid/filters/strip)   | Elimina las pestañas, los espacios y las nuevas líneas (todos los espacios en blanco) de los lados izquierdo y derecho de una cadena.                                                                                                    | ✅ Sí   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Elimina las pestañas, los espacios y las nuevas líneas (todos los espacios en blanco) de la parte izquierda de una cadena.    | ⛔ No    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Elimina las pestañas, los espacios y las nuevas líneas (todos los espacios en blanco) de la parte derecha de una cadena.          | ⛔ No    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Elimina todas las etiquetas HTML de una cadena.        | ✅ Sí   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Elimina los saltos de línea/las nuevas líneas de una cadena.        | ✅ Sí   |
| [truncar](https://shopify.dev/api/liquid/filters/truncate)    | Trunca una cadena hasta el número de caracteres pasado como primer parámetro. Se añade una elipsis (...) a la cadena truncada y se incluye en el recuento de caracteres.    | ✅ Sí   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Trunca una cadena hasta el número de palabras pasado como primer parámetro. Se añade una elipsis (...) a la cadena truncada.    | ✅ Sí   |
| [subir a](https://shopify.dev/api/liquid/filters/upcase)   | Convierte una cadena a mayúsculas.      | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros adicionales

Los siguientes filtros generales sirven para muchas cosas, como formatear o convertir contenidos.

| Filtrar                | Descripción                                                                                                                      | Apoyado |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [fecha](https://shopify.dev/api/liquid/filters/date)           | Convierte una marca de tiempo en otro formato de fecha. Para más información, consulta [Filtrar por fecha](#date-filter).         | ✅ Sí   |
| [predeterminado](https://shopify.dev/api/liquid/filters/default)        | Establece un valor predeterminado para cualquier variable sin valor asignado. Puede utilizarse con cadenas, matrices y hashes.      | ✅ Sí   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formatea una dirección para imprimir los elementos de la dirección ordenados según su localización.        | ⛔ No    |
| [destaca](https://shopify.dev/api/liquid/filters/highlight)      | Envuelve las palabras dentro de los resultados de búsqueda con una etiqueta HTML `<strong>` con la clase highlight si coincide con los términos de búsqueda enviados. | ⛔ No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Puedes encontrar más filtros compatibles, como filtros de codificación y URL, en nuestra página [Filtros avanzados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtrar fecha {#date-filter}

El filtro `date` se puede utilizar para convertir una marca de tiempo en un formato de fecha diferente. Puedes pasar parámetros al filtro `date` para reformatear la marca de tiempo. Para ver ejemplos de estos parámetros, consulta [strfti.me](http://www.strfti.me/).

Por ejemplo, digamos que el valor de `date_attribute` es la marca de tiempo `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Además de las opciones de formato de `strftime`, Braze también admite convertir una marca de tiempo a hora Unix con el filtro de fecha de `%s`. Por ejemplo, para obtener el `date_attribute` en tiempo Unix:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}