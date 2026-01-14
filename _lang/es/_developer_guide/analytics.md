---
nav_title: Análisis
article_title: Acerca de los análisis para el SDK de Braze
page_order: 2.6
description: "Infórmate sobre los análisis del SDK de Braze, para que puedas comprender mejor qué datos recopila Braze, la diferencia entre eventos personalizados y atributos personalizados, y las mejores prácticas para gestionar los análisis."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
---

# Análisis

> Infórmate sobre los análisis del SDK de Braze, para que puedas comprender mejor qué datos recopila Braze, la diferencia entre eventos personalizados y atributos personalizados, y las mejores prácticas para gestionar los análisis.

{% alert tip %}
Durante la implementación de Braze, asegúrate de discutir los objetivos de marketing con tu equipo, para que puedas decidir mejor los datos que quieres seguir y cómo quieres seguirlos con Braze. Para ver un ejemplo, consulta el caso de estudio de nuestra [aplicación de taxi/viaje](#example-case) compartido al final de esta guía.
{% endalert %}

## Datos recogidos automáticamente

Nuestro SDK recopila automáticamente determinados datos de usuario, por ejemplo, la primera aplicación utilizada, la última aplicación utilizada, el recuento total de sesiones, el sistema operativo del dispositivo, etc. Si sigues nuestras guías de integración para implementar nuestros SDK, podrás aprovechar esta [recopilación de datos predeterminada]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Comprobar esta lista puede ayudarte a evitar almacenar la misma información sobre los usuarios más de una vez. A excepción del inicio y fin de sesión, el resto de datos de seguimiento automático no cuentan para tu asignación de puntos de datos.

Consulta nuestro artículo [de introducción al SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) para permitir procesos de lista que bloqueen la recogida predeterminada de determinados elementos de datos.

## Eventos personalizados

Los eventos personalizados son acciones que realizan tus usuarios; son los más adecuados para hacer un seguimiento de las interacciones de alto valor de los usuarios con tu aplicación. El registro de un evento personalizado puede desencadenar cualquier número de campañas de seguimiento con retrasos configurables, y habilita los siguientes filtros de segmentación en torno a la recurrencia y frecuencia de ese evento:

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprobar si el evento personalizado se ha producido **más de X veces** | **MÁS DE** | **NÚMERO** |
| Comprobar si el evento personalizado se ha producido **menos de X veces** | **MENOS DE** | **NÚMERO** |
| Comprueba si el evento personalizado se ha producido **exactamente X número de veces** | **EXACTAMENTE** | **NÚMERO** |
| Comprueba si el evento personalizado ocurrió por última vez **después de X fecha** | **DESPUÉS DE** | **TIME** |
| Comprobar si el evento personalizado ocurrió por última vez **antes de X fecha** | **ANTES** | **TIME** |
| Compruebe si el evento personalizado se produjo por última vez **hace más de X días** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** (Positivo) Número) |
| Comprueba si el evento personalizado ocurrió por última vez **hace menos de X días** | **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** (Positivo) Número) |
| Comprueba si el evento personalizado se ha producido **más de X (Máx. = 50) veces** | **MÁS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprobar si el evento personalizado se ha producido **menos de X (Máx. = 50) veces** | **MENOS DE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
| Comprueba si el evento personalizado ocurrió **exactamente X (Máx. = 50) número de veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze anota el número de veces que se han producido estos eventos, así como la última vez que los realizó cada usuario para la segmentación. En la página de análisis de **eventos personalizados**, puedes ver de forma agregada la frecuencia con la que se produce cada evento personalizado, así como por segmentos a lo largo del tiempo para un análisis más detallado. Esto es especialmente útil para ver cómo han afectado tus campañas a la actividad de los eventos personalizados, observando las líneas grises que Braze superpone en las series temporales para indicar la última vez que se envió una campaña.

![Un gráfico de análisis de evento personalizado que muestra las estadísticas de los usuarios que añadieron una tarjeta de crédito y realizaron una búsqueda durante un periodo de treinta días.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
[El incremento de atributos personalizados]({{site.baseurl}}/api/endpoints/messaging/) puede utilizarse para mantener un contador de una acción del usuario similar a un evento personalizado. Sin embargo, no podrás ver datos de atributos personalizados en una serie temporal. Las acciones de los usuarios que no necesiten analizarse en series temporales deben registrarse mediante este método.
{% endalert %}

### Almacenamiento de eventos personalizado

Todos los datos del perfil de usuario (eventos personalizados, atributo personalizado, datos personalizados) se almacenan mientras esos perfiles estén activos.

### Propiedades del evento personalizadas

Con las propiedades del evento personalizado, Braze te permite establecer propiedades en eventos y compras personalizados. Estas propiedades pueden utilizarse para calificar aún más las condiciones desencadenantes, aumentar la personalización de la mensajería y generar análisis más sofisticados mediante la exportación de datos sin procesar. Los valores de las propiedades pueden ser cadenas, números, booleanos u objetos de tiempo. Sin embargo, los valores de propiedad no pueden ser matrices de objetos.

Por ejemplo, si una aplicación de comercio electrónico quisiera enviar un mensaje a un usuario cuando abandona su carrito, podría mejorar adicionalmente su audiencia objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento personalizada del `cart_value` de los carritos de los usuarios.

![Un ejemplo de evento personalizado que enviará una campaña a un usuario que ha abandonado su carrito y ha dejado el valor del carrito en más de 100 y menos de 200.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Las propiedades del evento personalizado también pueden utilizarse para la personalización dentro de la plantilla de mensajería. Cualquier campaña que utilice [la entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) con un evento desencadenante puede utilizar las propiedades del evento personalizado de ese evento para la personalización de la mensajería. Si una aplicación de juegos quisiera enviar un mensaje a los usuarios que hubieran completado un nivel, podría personalizar aún más el mensaje con una propiedad para el tiempo que tardaron los usuarios en completar ese nivel. En este ejemplo, el mensaje se personaliza para tres segmentos distintos utilizando [la lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/). La propiedad del evento personalizado llamada ``time_spent`` puede incluirse en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Las propiedades del evento personalizadas están diseñadas para ayudarte a personalizar tus mensajes o a crear campañas de entrega basadas en acciones granulares. Si quieres crear segmentos basados en la frecuencia y la frecuencia de las propiedades del evento, ponte en contacto con tu administrador del éxito del cliente o con nuestro equipo de soporte.

## Atributos personalizados

Los atributos personalizados son herramientas extraordinariamente flexibles que te permiten dirigirte a los usuarios con mayor especificidad que con los atributos estándar. Los atributos personalizados son estupendos para almacenar información específica de la marca sobre tus usuarios. Debes tener en cuenta que no almacenamos información de series temporales para los atributos personalizados, por lo que no vas a obtener ningún gráfico basado en ellos como en el ejemplo anterior para los eventos personalizados.

### Almacenamiento de atributos personalizado

Todos los datos del perfil de usuario (eventos personalizados, atributo personalizado, datos personalizados) se almacenan mientras esos perfiles estén activos.

### Tipos de datos de atributos personalizados

Los siguientes tipos de datos pueden almacenarse como atributos personalizados:

#### Cadenas (caracteres alfanuméricos)

Los atributos de cadena son útiles para almacenar entradas de usuario, como una marca favorita, un número de teléfono o una última cadena de búsqueda dentro de tu aplicación. Los atributos de cadena pueden tener hasta 255 caracteres.

La tabla siguiente describe las opciones de segmentación disponibles para los atributos de cadena.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el atributo de cadena **coincide exactamente con** una cadena introducida| **IGUAL A** | **CADENA** |
| Comprueba si el atributo cadena **coincide parcialmente con** una cadena introducida **O** una expresión regular | **COINCIDE CON REGEX** | **CADENA** **O** **EXPRESIÓN REGULAR** |
| Comprueba si el atributo cadena **no coincide parcialmente con** una cadena introducida **O** una expresión regular | **NO COINCIDE CON REGEX** | **CADENA** **O** **EXPRESIÓN REGULAR** |
| Comprueba si el atributo cadena **no coincide con** una cadena introducida| **NO ES IGUAL A** | **CADENA** |
| Comprueba si el atributo cadena **existe** en el perfil de un usuario | **ESTÁ EN BLANCO** | **N/A** |
| Comprueba si el atributo cadena **no existe** en el perfil de un usuario | **NO ESTÁ EN BLANCO** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Al segmentar utilizando el filtro **REGEX DOES NOT MATCH**, se requiere que ya exista un atributo personalizado con un valor asignado en ese perfil de usuario. Braze sugiere utilizar la lógica "OR" para comprobar si un atributo personalizado está en blanco con el fin de orientar correctamente a los usuarios.
{% endalert %}

{% alert tip %}
Para saber más sobre cómo utilizar nuestro filtro de expresiones regulares, consulta esta documentación sobre [expresiones regulares compatibles con Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Más recursos sobre regex:
- [Regex con Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Depurador y comprobador de expresiones regulares](https://regex101.com/)
- [Tutorial de regex](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Matrices

Los atributos de matriz son buenos para almacenar listas relacionadas de información sobre tus usuarios. Por ejemplo, almacenar en una matriz los últimos 100 contenidos que ha visto un usuario permitiría una segmentación por intereses específicos.

Las matrices de atributos personalizadas son conjuntos unidimensionales; no se admiten matrices multidimensionales. **Añadir un elemento a una matriz de atributos personalizada añade el elemento al final de la matriz, a menos que ya esté presente, en cuyo caso se mueve desde su posición actual al final de la matriz.** Por ejemplo, si se importara una matriz `['hotdog','hotdog','hotdog','pizza']`, se mostraría en el atributo de matriz como `['hotdog', 'pizza']` porque sólo se admiten valores únicos.

Si la matriz contiene su cantidad máxima de elementos, el primer elemento se descartará y el nuevo elemento se añadirá al final. A continuación se muestra un código de ejemplo que muestra el comportamiento de las matrices en el SDK Web:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

El número máximo de elementos de las matrices de atributos personalizadas está predeterminado en 25. El máximo para matrices individuales puede aumentarse hasta 100 en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Si deseas aumentar este máximo, ponte en contacto con tu administrador del servicio de atención al cliente. Las matrices que superen la cantidad máxima de elementos se truncarán para contenerla.

La tabla siguiente describe las opciones de segmentación disponibles para los atributos de la matriz.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el atributo de la matriz **incluye un valor que coincide exactamente con** un valor introducido| **INCLUYE VALOR** | **CADENA** |
| Comprueba si el atributo de la matriz **no incluye un valor que coincida exactamente con** un valor introducido| **NO INCLUYE EL VALOR** | **CADENA** |
| Comprueba si el atributo de la matriz **contiene un valor que coincide parcialmente con** un valor introducido **O** una expresión regular | **COINCIDE CON REGEX** | **CADENA** **O** **EXPRESIÓN REGULAR** |
| Comprueba si el atributo de la matriz **tiene algún valor** | **TIENE UN VALOR** | **N/A** |
| Comprueba si el atributo de la matriz **está vacío** | **ESTÁ VACÍO** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Utilizamos [expresiones regulares compatibles con Perl (PCRE)](http://www.regextester.com/pregsyntax.html).
{% endalert %}

#### Fechas

Los atributos de tiempo son útiles para almacenar la última vez que se realizó una acción específica, de modo que pueda ofrecer a sus usuarios mensajes de reenganche específicos del contenido.

{% alert note %}
La última fecha en que se produjo un evento personalizado o un evento de compra se registra automáticamente, y no debe registrarse por duplicado mediante un atributo de tiempo personalizado.
{% endalert %}

Los filtros de fecha que utilizan fechas relativas (por ejemplo, hace más de 1 día, hace menos de 2 días) miden 1 día como 24 horas. Cualquier campaña que realices utilizando estos filtros incluirá a todos los usuarios en incrementos de 24 horas. Por ejemplo, la última vez que se utilizó la aplicación hace más de 1 día captará a todos los usuarios que "utilizaron la aplicación por última vez hace más de 24 horas" desde el momento exacto en que se ejecuta la campaña. Lo mismo ocurrirá con las campañas configuradas con intervalos de fechas más largos: así, cinco días desde la activación significarán las 120 horas anteriores.

La siguiente tabla describe las opciones de segmentación disponibles para los atributos de tiempo.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el atributo de tiempo **es anterior a** una **fecha seleccionada**| **ANTES** | **SELECTOR DE FECHAS DEL CALENDARIO** |
| Comprueba si el atributo de tiempo **es posterior a** una **fecha seleccionada**| **DESPUÉS DE** | **SELECTOR DE FECHAS DEL CALENDARIO** |
| Comprueba si el atributo de tiempo es **más de X número** de **días atrás** | **MÁS DE** | **NÚMERO DE DÍAS ATRÁS** |
| Comprueba si el atributo de tiempo es **menos de X número** de **días atrás**| **MENOS DE** | **NÚMERO DE DÍAS ATRÁS** |
| Comprueba si el atributo de tiempo está **en más de X número** de **días en el futuro** | **EN MÁS DE** | **NÚMERO DE DÍAS EN EL FUTURO** |
| Comprueba si el atributo de tiempo es **menos de X número** de **días en el futuro** | **EN MENOS DE** | **NÚMERO DE DÍAS EN EL FUTURO**  |
| Comprueba si el atributo de tiempo **existe** en el perfil de un usuario | **EN BLANCO** | **N/A** |
| Comprueba si el atributo de tiempo **no existe** en el perfil de un usuario | **NO ESTÁ EN BLANCO** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Números {#integers}

Los atributos numéricos tienen una gran variedad de casos de uso. Los atributos personalizados de número creciente son útiles para almacenar el número de veces que se ha producido una determinada acción o evento. Los números estándar tienen todo tipo de usos, como registrar el número de calzado, la talla de cintura o el número de veces que un usuario ha visto una determinada característica o categoría de un producto.

{% alert note %}
El dinero gastado no debe registrarse por este método. Más bien debe registrarse a través de nuestros [métodos de compra]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking).
{% endalert %}

La tabla siguiente describe las opciones de segmentación disponibles para los atributos numéricos.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el atributo numérico **es más que** un **número**| **MÁS DE** | **NÚMERO** |
| Comprueba si el atributo numérico **es menor que** un **número**| **MENOS DE** | **NÚMERO** |
| Comprueba si el atributo numérico **es exactamente** un **número**| **EXACTAMENTE** | **NÚMERO** |
| Comprueba si el atributo numérico **no es igual a** un **número**| **NO ES IGUAL A** | **NÚMERO** |
| Comprueba si el atributo numérico **existe** en el perfil de un usuario | **EXISTE** | **N/A** |
| Comprueba si el atributo numérico **no existe** en el perfil de un usuario | **NO EXISTE** | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Booleanos (verdadero/falso)

Los atributos booleanos son útiles para almacenar estados de suscripción y otros datos binarios sencillos sobre tus usuarios. Las opciones de entrada que te proporcionamos te permiten encontrar a los usuarios a los que se les ha establecido explícitamente una variable como booleana, además de los que aún no tienen ningún registro de ese atributo.

La tabla siguiente describe las opciones de segmentación disponibles para los atributos booleanos.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el valor booleano **es** | **ES**  | **VERDADERO**, **FALSO**, **VERDADERO O NO ESTABLECIDO**, o **FALSO O NO ESTABLECIDO** |
| Comprueba si el valor booleano **existe** en el perfil de un usuario | **EXISTE**  | **N/A** |
| Comprueba si el valor booleano **no existe** en el perfil de un usuario | **NO EXISTE**  | **N/A** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Eventos de compra / seguimiento de ingresos

El uso de nuestros métodos de compra para registrar las compras dentro de la aplicación establece el Valor de Vida Útil (LTV) para cada perfil de usuario individual. Estos datos se pueden ver en nuestra página de ingresos en gráficos de series temporales.

La siguiente tabla describe las opciones de segmentación disponibles para los eventos de compra.

| Opciones de segmentación | Filtro desplegable | Opciones de entrada |
| ---------------------| --------------- | ------------- |
| Comprueba si el total de dólares gastados **es mayor que** un **número**| **MAYOR QUE** | **NÚMERO** |
| Comprueba si el número total de dólares gastados **es menor que** un **número**| **MENOS DE** | **NÚMERO** |
| Comprueba si el total de dólares gastados **es exactamente** un **número**| **EXACTAMENTE** | **NÚMERO** |
| Comprueba si la última compra se **produjo después de X fecha** | **DESPUÉS DE** | **TIME** |
| Comprueba si la última compra se produjo **antes de X fecha** | **ANTES** | **TIME** |
| Comprueba si la última compra se **produjo hace más de X días** | **MÁS DE** | **TIME** |
| Comprueba si la última compra se produjo **hace menos de X días** | **MENOS DE** | **TIME** |
| Comprueba si la compra se ha producido **más de X (Máx = 50) veces** | **MÁS DE** | en los últimos **Y Días (Y = 1,3,7,14,21,30)** |
| Comprueba si la compra se ha producido **menos de X (Máx = 50) veces** | **MENOS DE** | en los últimos **Y Días (Y = 1,3,7,14,21,30)** |
| Comprueba si la compra se ha producido **exactamente X (Máx. = 50) veces** | **EXACTAMENTE** | en los últimos **Y días (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Si desea segmentar en función del número de veces que se ha producido una compra específica, también deberá registrar dicha compra individualmente como un [atributo personalizado incremental](#integers).
{% endalert %}

## Caso de uso de aplicación de transporte compartido/taxi {#example-case}

Para este ejemplo, consideremos una aplicación de transporte compartido que quiere decidir qué datos de usuario recopilar. Las siguientes preguntas y el proceso de lluvia de ideas son un gran modelo a seguir por los equipos de marketing y desarrollo. Al final de este ejercicio, ambos equipos deberían tener una sólida comprensión de qué eventos y atributos personalizados tiene sentido recopilar para ayudar a cumplir su objetivo.

**Pregunta del caso nº 1: ¿Cuál es el objetivo?**

Su objetivo es sencillo: quieren que los usuarios llamen a taxis a través de su aplicación.

**Pregunta del caso nº 2: ¿Cuáles son los pasos intermedios en el camino hacia ese objetivo desde la instalación de la aplicación?**

1. Necesitan que los usuarios inicien el proceso de registro y rellenen sus datos personales.
2. Necesitan que los usuarios completen y verifiquen el proceso de registro introduciendo un código en la aplicación que reciben por SMS.
3. Tienen que intentar llamar un taxi.
4. Para llamar a un taxi, debe estar disponible cuando lo busquen.

Estas acciones podrían entonces etiquetarse como los siguientes eventos personalizados:

- Inicio de la inscripción
- Registro completo
- Llamadas de taxi con éxito
- Llamadas de taxi fallidas

Después de implementar los eventos, ahora puedes ejecutar las siguientes campañas:

1. Envía mensajes a los usuarios que iniciaron el registro, pero no desencadenaron el evento Registro finalizado en un plazo de tiempo determinado.
2. Envía mensajes de felicitación a los usuarios que completen el registro.
3. Envía disculpas y crédito promocional a los usuarios que hayan realizado paradas de taxi infructuosas que no hayan ido seguidas de una parada de taxi satisfactoria en un plazo de tiempo determinado.
4. Envía promociones a usuarios avanzados con muchos Taxi Llamados con éxito para agradecerles su fidelización.

¡Y muchos más!

**Pregunta del caso nº 3: ¿Qué otra información podríamos querer saber sobre nuestros usuarios que sirva de base a nuestra mensajería?**

- ¿Tienen o no créditos promocionales?
- ¿La clasificación promedio que dan a sus conductores?
- ¿Códigos promocionales únicos para el usuario?

Estas características podrían etiquetarse como los siguientes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Clasificación promedio de los conductores (tipo de número)
- Código de promoción único (Tipo de cadena)

Añadir estos atributos te permitiría enviar campañas a los usuarios, por ejemplo:

1. Recuerda a los usuarios que no se han conectado en siete días, pero que tienen un crédito promocional, que su crédito existe y que deben volver a la aplicación para utilizarlo.
2. Envía mensajes a los usuarios que dan clasificaciones bajas a los conductores para obtener opiniones directas de los clientes y saber por qué no disfrutaron de sus viajes.
3. Utiliza nuestras [características de plantilla y personalización de mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) para arrastrar el atributo de código promocional único a la mensajería dirigida a los usuarios.

## Buenas prácticas

### Buenas prácticas generales

#### Utilizar propiedades del evento

- Nombra un evento personalizado como algo que describe una acción que realiza un usuario.
- Utiliza generosamente las propiedades del evento personalizadas para representar datos importantes sobre un evento.
- Por ejemplo, en lugar de capturar un evento personalizado distinto para ver cada una de las 50 películas diferentes, sería más eficaz capturar simplemente ver una película como un evento y tener una propiedad de evento que incluya el nombre de la película.

### Mejores prácticas de desarrollo

#### Establecer ID de usuario para cada usuario

Los ID de usuario deben establecerse para cada uno de tus usuarios. Deben ser inmutables y accesibles cuando un usuario abra la aplicación. **Te recomendamos encarecidamente** que proporciones este identificador, ya que te permitirá:

- Sigue a tus usuarios a través de dispositivos y plataformas, mejorando la calidad de tus datos de comportamiento y demográficos.
- Importa datos sobre tus usuarios utilizando nuestra [API de datos de usuario]({{site.baseurl}}/api/endpoints/user_data/).
- Dirígete a usuarios específicos con nuestra [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/), tanto para mensajes generales como transaccionales.

Los ID de usuario deben tener menos de 512 caracteres y deben ser privados y no fáciles de obtener (por ejemplo, no una dirección de correo electrónico simple o un nombre de usuario). Si tal identificador no está disponible, Braze asignará un identificador único a tus usuarios, pero carecerás de las capacidades indicadas para los ID de usuario. Debes evitar configurar ID de usuario para usuarios para los que carezcas de un identificador único que esté vinculado a ellos como individuos. Pasar un identificador de dispositivo no ofrece ninguna ventaja frente al seguimiento automático de usuarios anónimos que Braze ofrece por defecto. Los siguientes son algunos ejemplos de ID de usuario adecuados e inadecuados.

Buenas opciones para los ID de usuario:

- Dirección de correo electrónico codificada o nombre de usuario único
- Identificador único de la base de datos

No deben utilizarse como ID de usuario:

- ID del dispositivo
- Número aleatorio o ID de sesión
- Cualquier ID no único
- Dirección de correo electrónico
- ID de usuario de otro proveedor externo

{% multi_lang_include sdk_auth_alert.md %}

#### Dar nombres legibles a los eventos y atributos personalizados

Imagina que eres un especialista en marketing que empieza a utilizar Braze uno o dos años después de su implantación, leer una lista desplegable llena de nombres como "usr_no_acct" sin más contexto puede resultar intimidante. Dar a tus eventos y atributos nombres identificables y legibles facilitará las cosas a todos los usuarios de tu plataforma. Considera las siguientes buenas prácticas:

- No empieces un evento personalizado con un carácter numérico. La lista desplegable está ordenada alfabéticamente y empezar con un carácter numérico hace más difícil segmentar por el filtro que elijas
- Intenta no utilizar abreviaturas oscuras o jerga técnica siempre que sea posible
  - Ejemplo: `usr_ctry` puede estar bien como nombre de variable para el país de un usuario dentro de un fragmento de código, pero el atributo personalizado debe enviarse a Braze como algo parecido a `user_country` para dar algo de claridad a un especialista en marketing que utilice el panel más adelante.

#### Registrar atributos sólo cuando cambian

Contamos cada atributo pasado a Braze como un punto de datos, aunque el atributo pasado contenga el mismo valor que el guardado anteriormente. Registrar los datos sólo cuando cambian ayuda a evitar el uso redundante de puntos de datos y favorece una experiencia más fluida al evitar llamadas innecesarias a la API.

#### Evita generar nombres de eventos mediante programación

Si estás creando constantemente nuevos nombres de eventos, va a ser imposible segmentar de forma significativa a tus usuarios. Por lo general, debes capturar eventos genéricos ("Vi un video" o "Leí un artículo") en lugar de eventos muy específicos como ("Vi el Gangnam Style" o "Leí un artículo"): Los 10 mejores sitios para comer en el centro de Manhattan"). Los datos específicos sobre el evento deben incluirse como una propiedad del evento, no como parte del nombre del evento.

### Limitaciones y restricciones técnicas

Ten en cuenta las siguientes limitaciones y restricciones al implementar eventos personalizados:

#### Restricciones de longitud

Todos los eventos personalizados, nombres de atributos personalizados (claves) y valores de cadena de eventos personalizados de 255 caracteres o más se truncarán. Lo ideal es que sean lo más cortos posible para mejorar el rendimiento de la red y de la batería en relación con tu aplicación. Si es posible, limítalos a 50 caracteres.

#### Limitaciones de contenido
El siguiente contenido se recortará programáticamente de tus atributos y eventos. Procura no utilizar lo siguiente:

- Espacio en blanco inicial y final
- Nuevas líneas
- Todos los no dígitos de los números de teléfono
  - Ejemplo: "(732) 178-1038" se condensará en "7321781038".
- Los caracteres que no sean espacios en blanco deben convertirse en espacios
- $ no debe utilizarse como prefijo de ningún evento personalizado
- Cualquier valor de codificación UTF-8 no válido
  -  "Mi Campo \\x80" se condensaría en "Mi Campo".

#### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades del evento personalizado:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Definiciones de valores

- Los valores enteros son de 64 bits
- Los decimales tienen 15 cifras decimales predeterminadas

### Análisis sintáctico de un campo de nombre genérico

Si sólo existe un único campo de nombre genérico para un usuario (por ejemplo, "JohnDoe"), puedes asignar este título completo al atributo Nombre de tu usuario. Además, puedes intentar analizar tanto el nombre como el apellido del usuario utilizando espacios, pero este último método conlleva el riesgo potencial de nombrar mal a algunos de tus usuarios.
