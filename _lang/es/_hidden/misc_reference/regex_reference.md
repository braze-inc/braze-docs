---
nav_title: Hoja de referencia regex
permalink: /regex_cheat_sheet/
hidden: true
---

# Hoja de referencia regex

Esta página sirve como guía de referencia rápida para la expresión regular, incluyendo tokens comunes, metaconsecuencias, tokens generales, constantes de grupo y mucho más.

{% tabs %}
{% tab Tokens comunes %}

| Tokens comunes |
| ------------- |
| Un solo carácter de: a, b o c | `[abc]` |
| Un carácter excepto: a, b o c | `[^abc]` |
| Un carácter del rango: a-z | `[a-z]` |
| Un carácter no comprendido en el intervalo: a-z | `[^a-z]` |
| Un carácter del rango: a-z o A-Z | `[a-zA-Z]` |
| Cualquier carácter | `.` |
| Cualquier carácter de espacio en blanco | `\s` |
| Cualquier carácter que no sea un espacio en blanco | `\S` |
| Cualquier dígito | `\d` |
| Cualquier cifra no numérica | `\D` |
| Cualquier carácter de palabra | `\w` |
| Cualquier carácter que no sea una palabra | `\W` |
| Captura cerrada | `(...)` |
| Combina a o b | `(a|b)` |
| Cero o uno de un | `a?` |
| Cero o más de un | `a*` |
| Uno o varios de | `a+` |
| Exactamente 3 de a | `a{3}` |
| Entre 3 y 6 de | `a{3,6}` |
| Inicio de cadena | `^` |
| Final de la cadena | `$` |
| Límite de palabra | `\n` |
| Límite de ninguna palabra | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Metaconsecuencia %}

| Metaconsecuencia |
| ------------- |
| Cualquier secuencia Unicode, incluidos los saltos de línea | `\X` |
| Empareja una unidad de datos | `\C` |
| Nuevas líneas Unicode | `\R` |
| Carácter de espacio en blanco vertical | `\v` |
| Negación de \\v | `\V` |
| Carácter de espacio en blanco horizontal | `\h` |
| Negación de \\h | `\H` |
| Restablecer coincidencia | `\K` |
| Coincidir con el enésimo subpatrón | `\n` |
| Propiedad Unicode X | `\pX` |
| Negación de \\pX | `\PX` |
| Propiedad Unicode o categoría de escritura | `\p{...}` |
| Negación de \\p | `\P{...}` |
| Cita; tratar como liberales | `\Q...|E` |
| Coincide con el sub-patrón 'nombre' | `\k<name>` | 
| Coincide con el sub-patrón 'nombre' | `\k'name'` | 
| Coincide con el sub-patrón 'nombre' | `\k{name}` |
| Coincidir con el enésimo subpatrón | `\gn` | 
| Coincidir con el enésimo subpatrón | `\g{n}` |
| Recurrir al enésimo grupo de captura | `\g<n>` |
| Recurrir al enésimo grupo de captura | `\g'n'` |
| Coincidir con el enésimo subpatrón anterior relativo | `\g{-n}` |
| Recurrir al enésimo subpatrón próximo relativo | `\g<+n>` |
| Emparejar enésimo pariente próximo remitente | `\g'+n'` |
| Grupo de captura de nombres recursivo | `'letter'` |
| Coincidir con el grupo de captura "letra" nombrado anteriormente | `\g{letter}` |
| Recursa nombres capturar grupo 'letra' | `\g<letter>` |
| Carácter hexadecimal YY | `\xYY` |
| Carácter hexadecimal AAAA | `\x{YYYY}` |
| Carácter octal ddd | `\ddd` |
| Carácter de control Y | `\cY` |
| Carácter de retroceso | `[\b]` |
| Hace literal cualquier carácter | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Tokens generales %}

| Tokens generales |
| -------------- |
| Nueva línea | `\n` |
| Retorno de carro | `\r` |
| Pestaña | `\t` |
| Carácter nulo | `\0` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modificadores de clase de los personajes %}

| Modificadores de clase de los personajes |
| ------------------------- |
| Un solo carácter de: a, b o c | `[abc]` |
| Un carácter excepto: a, b o c | `[^abc]` |
| Un carácter del rango: a-z | `[a-z]` |
| Un carácter no comprendido en el intervalo: a-z | `[^a-z]` |
| Un carácter del rango: a-z o A-Z | `[a-zA-Z]` |
| Letras y cifras | `[:alnum:]` |
| Cartas | `[:alpha:]` |
| Códigos ASCII 0-127 | `[:ascii:]` |
| Sólo espacio o pestaña | `[:blank:]` |
| Caracteres de control | `[:cntrl:]` |
| Dígitos | `[:digit:]` |
| Caracteres visibles (no espacio) | `[:word:]` |
| Letras minúsculas | `[:xdigit:]` |
| Letras mayúsculas | `[:<:]` |
| Caracteres de las palabras | `[:>:]` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Constantes de grupo %}

| Constantes de grupo |
| --------------- |
| Captura todo lo encerrado | `(...)` |
| Combina a o b | `(a|b)` |
| Haz coincidir todo lo adjunto | `(?:...)` |
| Agrupación atómica (no captura) | `(?>...)` |
| Número de grupo de subpatrón duplicado | `(?|...)` |
| Comentario | `(?#...)` |
| Para la insensibilidad a mayúsculas y minúsculas | `(?i)` |
| Grupo de captura con nombre | `(?'name'...)` |
| Grupo de captura con nombre | `(?<name>...)` |
| Grupo de captura con nombre | `(?P<name>...)` |
| Modificadores en línea | `(?imsxXU)` |
| Declaraciones condicionales | `(?(1)yes|no)` |
| Declaraciones condicionales recursivas | `(?(R#)yes|no)` |
| Declaración condicional | `(?(R&name)yes|no)` |
| Lookahead condicional | `(?(?=...)yes|no)` |
| Lookbehind condicional | `(?(?<=...)yes|no)` |
| Recurrir a todo el patrón | `(?R)` |
| Recurrir al primer sub-patrón | `(?1)` |
| Recurrir al primer subpatrón relativo | `(?+1)` |
| Recurrir al subpatrón 'nombre | `(?&name)` |
| Coincide con el subpatrón 'nombre' | `(?P=name)` |
| Recurrir al subpatrón 'nombre | `(?P>name)` |
| Predefine patrones antes de usarlos | `(?(DEFINE)...)` |
| Lookahead positivo | `(?=...)` |
| Lookahead negativo | `(?!...)` |
| Lookbehind positivo | `(?<=...)` |
| Lookbehind negativo | `(?<!...)` |
| Verbo de control | `(*ACCEPT)` |
| Verbo de control | `(*FAIL)` |
| Verbo de control | `(*MARK:NAME)` |
| Verbo de control | `(*COMMIT)` |
| Verbo de control | `(*PRUNE)` |
| Verbo de control | `(*SKIP)` |
| Verbo de control | `(*THEN)` |
| Modificador de patrón | `(*UTF)` |
| Modificador de patrón | `(*UTF8)` |
| Modificador de patrón | `(*UTF16)` |
| Modificador de patrón | `(*UTF32)` |
| Modificador de patrón | `(*UCP)` |
| Modificador de salto de línea | `(*CR)` |
| Modificador de salto de línea | `(*LF)` |
| Modificador de salto de línea | `(*CRLF)` |
| Modificador de salto de línea | `(*ANYCRLF)` |
| Modificador de salto de línea | `(*ANY)` |
| Modificador de salto de línea | `\R` |
| Modificador de salto de línea | `(*BSR_ANYCRLF)` |
| Modificador de salto de línea | `(*BSR_UNICODE)` |
| Modificador del motor regex | `(*LIMIT_MATCH=x)` |
| Modificador del motor regex | `(*LIMIT_RECURSION=d)` |
| Modificador del motor regex | `(*NO_AUTO_POSSESS)` |
| Modificador del motor regex | `(*NO_START_OPT)` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Cuantificadores %}

| Cuantificadores |
| ----------- |
| Cero o uno de un | `a?` |
| Cero o más de un | `a*` |
| Uno o varios de | `a+` |
| Exactamente 3 de a | `a{3}` |
| 3 o más de un | `a{3,}` |
| Entre 3 y 6 de | `a{3,6}` |
| Cuantificador codicioso | `a*` |
| Cuantificador perezoso | `a*?` |
| Cuantificador posesivo | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Anclas %}

| Anclas |
| ------- |
| Comienzo del partido | `\G` |
| Inicio de cadena | `^` |
| Final de la cadena | `$` |
| Inicio de cadena | `\A` |
| Final de la cadena | `\Z` |
| Fin absoluto de cadena | `\z` |
| Límite de palabra | `\b` |
| Límite sin palabra | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Indicadores y modificadores %}

| Indicadores y modificadores |
| ------------------- | 
| Global | `g` |
| Multilínea | `m` |
| Sensible a mayúsculas y minúsculas | `l` |
| Ignorar los espacios en blanco | `x` |
| Línea única | `s` |
| Unicode | `u` |
| Ampliado | `X` |
| Ungreedy | `U` |
| Ancla | `A` |
| Nombres de grupo duplicados | `J` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Sustitución %}

| Sustitución |
| ------------ |
| Contenido completo de la coincidencia | `\0` |
| Contenidos en el grupo de captura 1 | `\1 or $1` |
| Contenido del grupo de captura `foo` | `${foo}` |
| Valores de sustitución hexadecimales | `\x20, \x{06fa}` |
| Pestaña | `\t` |
| Retorno de carro | `\r` |
| Nueva línea | `\n` |
| Avance de página | `\f` |
| Transformación de mayúsculas | `\U` |
| Transformación en minúsculas | `\L` |
| Finaliza cualquier transformación | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

