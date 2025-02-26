---
nav_title: Filtros
article_title: Filtros de Liquid
page_order: 3
description: "Esta página de referencia enumera los filtros que pueden utilizarse para reformatear contenidos estáticos o dinámicos."

---

# Filtros

> Este artículo de referencia ofrece una visión general de los filtros en Liquid y explica qué filtros son compatibles con Braze. ¿Buscas ideas para utilizar estos filtros? Consulta nuestra [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/).

Los filtros permiten modificar la salida de números, cadenas, variables y objetos en Liquid. Puede utilizar filtros para reformatear texto estático o dinámico, como cambiar una cadena de minúsculas a mayúsculas o realizar operaciones matemáticas, como sumas o divisiones.

{% alert important %}
Braze no es compatible con todos los filtros Liquid de Shopify. Esta página intenta resumir los filtros de líquido que Braze ha probado, pero puede que no sea una lista completa. Pruebe siempre su líquido antes de enviar cualquier mensaje. <br><br>Si tiene alguna pregunta sobre un filtro que no aparece aquí, póngase en contacto con su gestor de éxito de clientes.
{% endalert %}

## Sintaxis del filtro

{% raw %}

Los filtros deben colocarse dentro de una etiqueta de salida `{{ }}` y se indican mediante un carácter de tubo `|`.

{% endraw %}

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

En este ejemplo, `Big Sale` es una cadena y `upcase` es el filtro que se aplica.

### Sintaxis para filtros múltiples

Puede utilizar varios filtros en una salida. Se aplican de izquierda a derecha.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de matriz

Los filtros de matrices se utilizan para modificar la salida de las matrices.

| Filtro               | Definición                                                                                                         | Compatible |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join][1.1]          | Une los elementos de una matriz con el carácter pasado como parámetro. El resultado es una sola cadena.          | ✅ Sí   |
| [first][1.2]         | Devuelve el primer elemento de un array. En una matriz de atributos personalizada, es el valor añadido más antiguo.                | ✅ Sí   |
| [last][1.3]          | Devuelve el último elemento de un array. En una matriz de atributos personalizada, es el valor añadido más recientemente.          | ✅ Sí   |
| [compact][1.4]       | Elimina cualquier elemento `nil` de una matriz.                                                                             | ✅ Sí   |
| [concat][1.5]        | Combina una matriz con otra matriz.                                                                              | ✅ Sí   |
| [index][1.6]         | Devuelve el elemento en la posición de índice especificada en una matriz. El primer elemento de un array se referencia con `[0]`. | ✅ Sí   |
| [map][1.7]           | Acepta un atributo de elemento de matriz como parámetro y crea una matriz a partir del valor de cada elemento de matriz.        | ✅ Sí   |
| [reverse][1.8]       | Invierte el orden de los elementos de una matriz.                                                                       | ✅ Sí   |
| [size][1.9]          | Devuelve el tamaño de una cadena (el número de caracteres) o de una matriz (el número de elementos).                      | ✅ Sí   |
| [sort][1.10]         | Ordena los elementos de una matriz por un atributo dado de un elemento de la matriz.                                    | ✅ Sí   |
| [ordenar_natural][1.11] | Ordena los elementos de una matriz por orden alfabético sin distinguir mayúsculas de minúsculas.                                                | ✅ Sí   |
| [uniq][1.12]         | Elimina cualquier instancia duplicada de los elementos de una matriz.                                                           | ✅ Sí   |
| [donde][1.13]        | Filtra una matriz para incluir sólo elementos con un valor de propiedad específico.                                             | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros de color

Braze no admite [filtros de color][2.1].

## Filtros de fuentes

Braze no admite [filtros de fuentes][3.1].

## Filtros matemáticos

Los filtros matemáticos permiten realizar operaciones matemáticas. Si utilizas varios filtros en una salida, se aplicarán de izquierda a derecha.

| Filtro  | Definición      | Compatible |
| :------ |:----------------| :-------- |
| [abs][4.1]        | Devuelve el valor absoluto de un número.     | ✅ Sí   |
| [at_most][4.2]    | Limita un número a un valor máximo.   | ✅ Sí   |
| [at_least][4.3]   | Limita un número a un valor mínimo.   | ✅ Sí   |
| [ceil][4.4]       | Redondea una salida al entero más próximo.  | ✅ Sí   |
| [dividido_por][4.5] | Divide una salida por un número. La salida se redondea al entero más próximo. Echa un vistazo al siguiente consejo para evitar el redondeo. | ✅ Sí   |
| [floor][4.6]      | Redondea una salida al entero más cercano.        | ✅ Sí   |
| [minus][4.7]      | Resta un número de una salida.          | ✅ Sí   |
| [plus][4.8]       | Añade un número a una salida.     | ✅ Sí   |
| [round][4.9]      | Redondea la salida al entero más próximo o al número especificado de decimales.  | ✅ Sí   |
| [veces][4.10]     | Multiplica una salida por un número.       | ✅ Sí   |
| [modulo][4.11]    | Divide una salida por un número y devuelve el resto.   | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Al dividir enteros (números enteros) entre enteros en Liquid, si la respuesta es un flotante (número con un decimal), Liquid redondeará automáticamente hacia abajo al entero más próximo. Sin embargo, al dividir enteros entre flotantes siempre se obtiene un flotante. Esto significa que puedes convertir tus enteros en un float (1.0, 2.0, 3.0) para devolver un float.
{% raw %}
<br><br>Por ejemplo,`{{15 | divided_by: 2}}` mostrará `7`, mientras que `{{15 | divided_by: 2.0}}` mostrará `7.5`.
{% endraw %}
{% endalert %}

### Operaciones matemáticas con atributos personalizados

Ten en cuenta que no puedes realizar operaciones matemáticas entre dos atributos personalizados.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Este ejemplo no funcionaría porque no se puede hacer referencia a varios atributos personalizados en una línea de Liquid. En su lugar, necesitaría asignar una variable a al menos uno de estos valores antes de que las funciones matemáticas tengan lugar. Añadir dos atributos personalizados juntos requeriría dos líneas de Liquid:

1. Uno para asignar el atributo personalizado a una variable,
2. Uno para realizar la suma.

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
{% tab Entrada %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Filtros de dinero

Si vas a poner al día a un usuario sobre su compra, el saldo de una cuenta o cualquier otra cosa relacionada con el dinero, debes utilizar filtros de dinero. Los filtros de dinero garantizan que los decimales estén en el lugar correcto y que no se pierda ningún fragmento de la actualización (como ese molesto `0` al final).

| Filtro         | Definición          | Compatible |
| :--------------- | :--------------- | :-------- |
| [money][5.1]      | Formatea los números para garantizar que los decimales están en el lugar adecuado y que no se han eliminado ceros al final de ningún número.   | ✅ Sí   |
| [dinero_con_divisa][5.2]    | Formatea los números con el símbolo de moneda.     | ⛔ No    |
| [dinero_sin_divisa][5.4]     | Formatea los números sin el símbolo de moneda.      | ⛔ No    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para formatear correctamente un número con el filtro `money`, elimine las comas del número y añada el filtro `plus: 0` antes del filtro `money`. Por ejemplo, mira el siguiente Liquid:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Filtro de dinero Shopify versus filtro de dinero Braze

{% alert warning %}
El comportamiento del filtro `money` de Shopify difiere de cómo se utiliza en Braze. Consulte los siguientes ejemplos para obtener una descripción precisa del comportamiento esperado.
{% endalert %}

{% raw %}
En caso de que introduzcas un atributo personalizado (como `account_balance`), debes utilizar siempre el filtro `money` para colocar los decimales en el lugar adecuado y evitar que los ceros caigan al final de los números:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| CON EL FILTRO DE DINERO                       | SIN EL FILTRO DE DINERO                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Con filtro de dinero][1]                     | ![Sin filtro de dinero][2]                  |
| Donde `account_balance` se introduce en `17.8`. | Donde `account_balance` se introduce en `17.8`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

El filtro `money` de Braze difiere del de Shopify porque no aplica automáticamente los decimales según una configuración preestablecida. Por ejemplo, tomemos el siguiente escenario en el que `rewards_redeemed` contiene un valor de `145`:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Según el filtro de [dinero][5.1] de Shopify, esto debería tener una salida de `$1.45`, sin embargo en Braze, esto tendrá una salida de `$145.00`. Como solución, podemos utilizar el filtro `divided_by` para manipular el número y convertirlo en decimal, antes de aplicar el filtro de dinero:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
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
Las comillas rectas son diferentes de las rizadas en Liquid. Tenga cuidado al copiar y pegar Liquid desde un editor de texto en Braze, ya que las comillas rizadas provocarán errores con su Liquid. Si escribes tu Liquid directamente en Braze, las comillas rectas se aplicarán automáticamente.
{% endalert %}

| Filtro          | Descripción     | Compatible |
| :--------------- | ------------- | --------- |
| [append][6.1]     | Añade caracteres a una cadena.           | ✅ Sí   |
| [camelcase][6.2]     | Convierte una cadena a CamelCase.             | ⛔ No    |
| [capitalize][6.3]     | Escribe en mayúsculas la primera palabra de una cadena y en minúsculas el resto de caracteres.         | ✅ Sí   |
| [downcase][6.4]      | Convierte una cadena a minúsculas.         | ✅ Sí   |
| [escape][6.5]    | Escapa de una cadena.             | ✅ Sí   |
| [handle/handleize][6.6]        | Formatea una cadena en un asa.        | ⛔ No    |
| [md5][6.7]    | Convierte una cadena en un hash MD5. Consulte [Filtros de codificación][3] para obtener más información.   | ✅ Sí   |
| [sha1][6.8]    | Convierte una cadena en un hash SHA-1. Consulte [Filtros de codificación][3] para obtener más información.  | ✅ Sí   |
| hmac_sha1_hex<br>(anteriormente [hmac_sha_1][6.10]) | Convierte una cadena en un hash SHA-1 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. Consulte [Filtros de codificación][3] para obtener más información. | ✅ Sí   |
| [hmac_sha256][6.11]    | Convierte una cadena en un hash SHA-256 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro.       | ✅ Sí   |
| hmac_sha512 | Convierte una cadena en un hash SHA-512 utilizando un código de autenticación de mensajes hash (HMAC). Pasa la clave secreta del mensaje como parámetro al filtro. | ✅ Sí  |
| [newline_to_br][6.12]     | Inserta una etiqueta HTML de salto de línea `<br>` delante de cada salto de línea de una cadena.        | ✅ Sí   |
| [pluralize][6.13]   | Imprime la versión singular o plural de una cadena inglesa en función del valor de un número.      | ⛔ No    |
| [prepend][6.14]     | Antepone caracteres a una cadena.      | ✅ Sí   |
| [remove][6.15]      | Elimina todas las apariciones de una subcadena de una cadena.       | ✅ Sí   |
| [remove_first][6.16]    | Elimina sólo la primera aparición de una subcadena de una cadena.      | ✅ Sí   |
| [replace][6.17]        | Sustituye todas las apariciones de una cadena por una subcadena.   | ✅ Sí   |
| [replace_first][6.18]        | Sustituye la primera aparición de una cadena por una subcadena.      | ✅ Sí   |
| [slice][6.19]       | El filtro slice devuelve una subcadena, comenzando en el índice especificado.       | ✅ Sí   |
| [split][6.20]  | El filtro de división toma una subcadena como parámetro. La subcadena se utiliza como delimitador para dividir una cadena en una matriz.            | ✅ Sí   |
| [strip][6.21]   | Elimina tabuladores, espacios y nuevas líneas (todos los espacios en blanco) de los lados izquierdo y derecho de una cadena.                                                                                                    | ✅ Sí   |
| [lstrip][6.22]     | Elimina tabuladores, espacios y nuevas líneas (todos los espacios en blanco) de la parte izquierda de una cadena.    | ⛔ No    |
| [rstrip][6.23]             | Elimina tabuladores, espacios y nuevas líneas (todos los espacios en blanco) de la parte derecha de una cadena.          | ⛔ No    |
| [strip_html][6.24]         | Elimina todas las etiquetas HTML de una cadena.        | ✅ Sí   |
| [strip_newlines][6.25]  | Elimina los saltos de línea y las nuevas líneas de una cadena.        | ✅ Sí   |
| [truncate][6.26]    | Trunca una cadena hasta el número de caracteres pasado como primer parámetro. Se añade una elipsis (...) a la cadena truncada y se incluye en el recuento de caracteres.    | ✅ Sí   |
| [truncatewords][6.27]   | Trunca una cadena hasta el número de palabras pasado como primer parámetro. Se añade una elipsis (...) a la cadena truncada.    | ✅ Sí   |
| [upcase][6.28]   | Convierte una cadena a mayúsculas.      | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Filtros adicionales

Los siguientes filtros generales sirven para muchas cosas, como formatear o convertir contenidos.

| Filtro                | Descripción                                                                                                                      | Compatible |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date][7.1]           | Convierte una marca de tiempo en otro formato de fecha. Más información en [Filtro de fechas](#date-filter).         | ✅ Sí   |
| [default][7.2]        | Establece un valor por defecto para cualquier variable sin valor asignado. Puede utilizarse con cadenas, matrices y hashes.      | ✅ Sí   |
| [format_address][7.3] | Formatea una dirección para imprimir los elementos de la dirección en orden según su localización.        | ⛔ No    |
| [highlight][7.4]      | Envuelve las palabras dentro de los resultados de búsqueda con una etiqueta HTML `<strong>` con la clase highlight si coincide con los términos de búsqueda enviados. | ⛔ No    |
| `time_zone`             | Consulta [Filtrar zona horaria](#time-zone-filter).     | ✅ Sí   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Encontrará más filtros compatibles, como los de codificación y URL, en nuestra página [Filtros avanzados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/).

### Filtro de fechas {#date-filter}

El filtro `date` puede utilizarse para convertir una marca de tiempo en un formato de fecha diferente. Puede pasar parámetros al filtro `date` para reformatear la marca de tiempo. Para ver ejemplos de estos parámetros, consulte [strfti.me](http://www.strfti.me/).

Por ejemplo, supongamos que el valor de `date_attribute` es la marca de tiempo `2021-06-03 17:13:41 UTC`.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Además de las opciones de formato de `strftime`, Braze también admite la conversión de una marca de tiempo a hora Unix con el filtro de fecha `%s`. Por ejemplo, para obtener el `date_attribute` en tiempo Unix:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Filtro de zona horaria {#time-zone-filter}

{% raw %}
Además de los filtros que encontrarás listados en la documentación de Shopify, Braze también soporta el filtro `time_zone`.

El filtro `time_zone` toma una hora, una zona horaria y un formato de fecha y devuelve la hora de esa zona horaria en el formato de fecha especificado. Por ejemplo, supongamos que el valor de `{{custom_attribute.$date_attribute}}}` es `2021-08-04 9:00:00 UTC`:
{% endraw %}

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | time_zone: 'America/Los_Angeles' | date: '%a %b %e %T' }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
Wed August 4 2:00:00
```
{% endraw %}
{% endtab %}
{% endtabs %}

También puede utilizar la variable reservada `now` para acceder a la fecha y hora actuales para su manipulación.

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ 'now' | date: '%Y-%m-%d %H:%M:%S' }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
2021-08-04 18:13:13
```
{% endraw %}
{% endtab %}
{% endtabs %}


[1.1]: https://shopify.dev/api/liquid/filters/array-filters#join
[1.2]: https://shopify.dev/api/liquid/filters/array-filters#first
[1.3]: https://shopify.dev/api/liquid/filters/array-filters#last
[1.4]: https://shopify.dev/api/liquid/filters#compact
[1.5]: https://shopify.dev/api/liquid/filters/array-filters#concat
[1.6]: https://shopify.dev/api/liquid/filters/array-filters#index
[1.7]: https://shopify.dev/api/liquid/filters/array-filters#map
[1.8]: https://shopify.dev/api/liquid/filters/array-filters#reverse
[1.9]: https://shopify.dev/api/liquid/filters/array-filters#size
[1.10]: https://shopify.dev/api/liquid/filters/array-filters#sort
[1.11]: https://shopify.dev/api/liquid/filters#sort_natural
[1.12]: https://shopify.dev/api/liquid/filters/array-filters#uniq
[1.13]: https://shopify.dev/api/liquid/filters#where

[2.1]: https://shopify.dev/api/liquid/filters/color-filters
[3.1]: https://shopify.dev/api/liquid/filters/font-filters

[4.1]: https://shopify.dev/api/liquid/filters/math-filters#abs
[4.2]: https://shopify.dev/api/liquid/filters/math-filters#at_most
[4.3]: https://shopify.dev/api/liquid/filters/math-filters#at_least
[4.4]: https://shopify.dev/api/liquid/filters/math-filters#ceil
[4.5]: https://shopify.dev/api/liquid/filters/math-filters#divided_by
[4.6]: https://shopify.dev/api/liquid/filters/math-filters#floor
[4.7]: https://shopify.dev/api/liquid/filters/math-filters#minus
[4.8]: https://shopify.dev/api/liquid/filters/math-filters#plus
[4.9]: https://shopify.dev/api/liquid/filters/math-filters#round
[4.10]: https://shopify.dev/api/liquid/filters/math-filters#times
[4.11]: https://shopify.dev/api/liquid/filters/math-filters#modulo

[5.1]: https://shopify.dev/api/liquid/filters/money-filters#money
[5.2]: https://shopify.dev/api/liquid/filters/money-filters#money_with_currency
[5.3]: https://shopify.dev/api/liquid/filters/money-filters#money_without_trailing_zeros
[5.4]: https://shopify.dev/api/liquid/filters/money-filters#money_without_currency

[6.1]: https://shopify.dev/api/liquid/filters/string-filters#append
[6.2]: https://shopify.dev/api/liquid/filters/string-filters#camelcase
[6.3]: https://shopify.dev/api/liquid/filters/string-filters#capitalize
[6.4]: https://shopify.dev/api/liquid/filters/string-filters#downcase
[6.5]: https://shopify.dev/api/liquid/filters/string-filters#escape
[6.6]: https://shopify.dev/api/liquid/filters/string-filters#handle-handleize
[6.7]: https://shopify.dev/api/liquid/filters/string-filters#md5
[6.8]: https://shopify.dev/api/liquid/filters/string-filters#sha1
[6.10]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1
[6.11]: https://shopify.dev/api/liquid/filters/string-filters#hmac_sha256
[6.12]: https://shopify.dev/api/liquid/filters/string-filters#newline_to_br
[6.13]: https://shopify.dev/api/liquid/filters/string-filters#pluralize
[6.14]: https://shopify.dev/api/liquid/filters/string-filters#prepend
[6.15]: https://shopify.dev/api/liquid/filters/string-filters#remove
[6.16]: https://shopify.dev/api/liquid/filters/string-filters#remove_first
[6.17]: https://shopify.dev/api/liquid/filters/string-filters#replace
[6.18]: https://shopify.dev/api/liquid/filters/string-filters#replace_first
[6.19]: https://shopify.dev/api/liquid/filters/string-filters#slice
[6.20]: https://shopify.dev/api/liquid/filters/string-filters#split
[6.21]: https://shopify.dev/api/liquid/filters/string-filters#strip
[6.22]: https://shopify.dev/api/liquid/filters/string-filters#lstrip
[6.23]: https://shopify.dev/api/liquid/filters/string-filters#rstrip
[6.24]: https://shopify.dev/api/liquid/filters/string-filters#strip_html
[6.25]: https://shopify.dev/api/liquid/filters/string-filters#strip_newlines
[6.26]: https://shopify.dev/api/liquid/filters/string-filters#truncate
[6.27]: https://shopify.dev/api/liquid/filters/string-filters#truncatewords
[6.28]: https://shopify.dev/api/liquid/filters/string-filters#upcase

[7.1]: https://shopify.dev/api/liquid/filters/additional-filters#date
[7.2]: https://shopify.dev/api/liquid/filters/additional-filters#default
[7.3]: https://shopify.dev/api/liquid/filters/additional-filters#format_address
[7.4]: https://shopify.dev/api/liquid/filters/additional-filters#highlight


[1]: {% image_buster /assets/img/with_money_filter.png %}
[2]: {% image_buster /assets/img/without_money_filter.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/#encoding-filters
