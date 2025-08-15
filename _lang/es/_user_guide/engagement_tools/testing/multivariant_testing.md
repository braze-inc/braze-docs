---
nav_title: Pruebas multivariante y A/B
article_title: Pruebas multivariante y A/B
page_order: 2
page_type: reference
description: "Este artículo de referencia explica las pruebas multivariantes y A/B y sus ventajas."
search_rank: 2
---

# Pruebas multivariantes y A/B

> Esta página explica qué son las pruebas multivariantes y las pruebas A/B y sus ventajas. Para saber cómo crear una prueba multivariante o A/B, consulta [Crear pruebas multivariantes y A/B con Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Se pueden utilizar pruebas multivariantes y A/B mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## ¿Qué son las pruebas multivariante y A/B?

### Prueba A/B

Una prueba A/B es un experimento que compara las respuestas de los usuarios a varias versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares, pero difieren en la redacción y el estilo.

El objetivo es identificar la versión de la campaña que mejor cumpla sus objetivos de marketing. En esta sección, veremos cómo comprobar la eficacia de las diferencias de contenido.

{% alert note %}
Si desea evaluar las diferencias en la programación o el calendario de los mensajes (por ejemplo, enviar un mensaje de carrito abandonado después de una hora de inactividad frente a un día de inactividad), consulte nuestra sección sobre la [creación de un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supongamos que tiene dos opciones para una notificación push:

- "¡Esta oferta expira mañana!"
- "¡Esta oferta caduca en 24 horas!"

Utilizando una prueba A/B, puedes ver qué redacción produce una mayor tasa de conversión. La próxima vez que envíe una notificación push sobre una oferta, sabrá qué tipo de redacción es más eficaz. Sin embargo, esta prueba solo examina el efecto de una variable: la copia de la notificación push.

### Prueba multivariante

Una prueba multivariante es similar a una prueba A/B, salvo que prueba los efectos de dos o más variables. Volvamos a nuestro ejemplo de las notificaciones push. Otra variable que podríamos querer probar es si se incluye un emoji al final del mensaje. Ahora estaríamos probando dos variables (o variantes, no confundir con variantes), de ahí el término "multivariante". Para ello, tendríamos que probar cuatro versiones en total del mensaje: dos opciones para la copia multiplicadas por dos opciones para el emoji (presente o no) es igual a cuatro variantes totales del mensaje.

En la documentación de Braze, "prueba multivariante" se utiliza indistintamente con "prueba A/B", ya que el proceso para configurarlos es el mismo.

## Beneficios de las pruebas multivariantes y A/B {#the-benefits-of}

Las pruebas multivariante y A/B le ofrecen una forma fácil y clara de conocer a su público. Ya no tiene que adivinar a qué responderán los usuarios: cada campaña se convierte en una oportunidad para probar distintas variantes de un mensaje y calibrar la respuesta del público.

Entre los escenarios específicos en los que las pruebas multivariantes y A/B pueden resultar útiles se incluyen:

- **Al probar un tipo de mensajería por primera vez:** ¿Te preocupa que la mensajería integrada en la aplicación salga bien a la primera? Las pruebas multivariantes le permiten experimentar y saber qué es lo que más gusta a sus usuarios.
- **Al crear campañas de incorporación y otras campañas que se envían constantemente:** Dado que la mayoría de sus usuarios se encontrarán con esta campaña, ¿por qué no asegurarse de que sea lo más eficaz posible?
- **Cuando tienes varias ideas de mensajes para enviar:** Si no está seguro de cuál elegir, haga una prueba y luego tome una decisión basada en datos.
- **Cuando investigues si tus usuarios responden a las técnicas de marketing "probadas":** Los profesionales del marketing suelen recurrir a tácticas convencionales para captar a los usuarios, pero la base de usuarios de cada producto es diferente. A veces, repetir tu llamada a la acción y utilizar la demostración social no te dará los resultados deseados. Las pruebas multivariante y A/B le permiten salirse de lo convencional y descubrir tácticas poco convencionales que funcionan para su público específico.

### Distribución de variantes

La distribución entre variantes no siempre es uniforme. Así funciona la distribución de variantes

Cada vez que se envía un mensaje en una campaña multivariante, el sistema selecciona de forma independiente una opción aleatoria en función de los porcentajes establecidos y asigna una variante en función del resultado. Es como lanzar una moneda al aire: las anomalías son posibles. Si alguna vez has tirado una moneda al aire 100 veces, sabrás que probablemente no siempre obtendrás un 50-50 exacto entre cara y cruz, aunque sólo tengas dos opciones. Podrías obtener 52 caras y 48 colas.

Si tiene varias variantes que desea dividir por igual, también debe asegurarse de que el número de variantes es múltiplo de 100. De lo contrario, algunas variantes tendrán un mayor porcentaje de usuarios distribuidos a esa variante en comparación con otras. Por ejemplo, si su campaña tiene 7 variantes, no puede haber una distribución uniforme de variantes, ya que 7 no se divide igual por 100 como número entero. En este caso, tendrías 2 variantes del 15 % y 5 variantes del 14 %.

#### Nota sobre los mensajes in-app

Al ejecutar una prueba A/B en mensajes dentro de la aplicación, puede parecer que sus análisis muestran una distribución de variantes más alta entre una variante y otra, incluso si tienen una división porcentual equitativa. Por ejemplo, considere el siguiente gráfico de *Destinatarios Únicos* para la Variante A y la Variante C.

![Gráfico de Receptores Únicos para dos variantes con una forma similar entre la Variante A y la Variante C, donde la Variante A tiene un mayor número de Receptores Únicos por día]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A tiene un mayor número de *destinatarios únicos* que la variante C. Esto no se debe a la distribución de variantes, sino a cómo se calculan *los destinatarios únicos* para los mensajes dentro de la aplicación. Para los mensajes in-app, *los Destinatarios Únicos* son en realidad *Impresiones Únicas*, que es el número total de personas que recibieron y vieron el mensaje in-app. Esto significa que si un usuario no recibe el mensaje por cualquier motivo o decide no verlo, no se incluye en el recuento de *Destinatarios Únicos*, y la distribución de variantes puede aparecer sesgada.

## Consejos para pruebas multivariantes y A/B

Las pruebas multivariantes y A/B pueden revelar información muy valiosa sobre sus usuarios. Para obtener resultados de las pruebas que reflejen realmente el comportamiento de tus usuarios, sigue estas directrices.

#### Ejecutar la prueba en un gran número de usuarios

Las muestras grandes garantizan que los resultados reflejen las preferencias del usuario medio y es menos probable que se vean influidos por valores atípicos. Las muestras de mayor tamaño también permiten identificar las Variantes Ganadoras que tienen márgenes de victoria más pequeños.

#### Clasificar aleatoriamente a los usuarios en diferentes grupos de prueba

Las pruebas multivariantes le permiten crear hasta ocho grupos de prueba seleccionados aleatoriamente. La aleatorización está diseñada para eliminar el sesgo en el conjunto de pruebas y aumentar las probabilidades de que los grupos de pruebas tengan una composición similar. De este modo se garantiza que los distintos porcentajes de respuesta se deban a diferencias en los mensajes y no en las muestras.

#### Conozca los elementos que desea probar

Las pruebas multivariantes y A/B permiten comprobar las diferencias entre varias versiones de un mensaje. En algunos casos, una prueba simple puede ser lo más eficaz, ya que aislar los cambios permite identificar qué elementos tuvieron mayor impacto en la respuesta. Otras veces, presentar más diferencias entre variantes le permitirá examinar valores atípicos y comparar distintos conjuntos de elementos. Ninguno de los dos métodos es necesariamente erróneo, siempre que tengas claro desde el principio lo que intentas comprobar.

#### Decida la duración de la prueba y no la finalice antes de tiempo.

Antes de empezar la prueba, decide cuánto tiempo va a durar y cíñete a ella. Los profesionales del marketing suelen caer en la tentación de detener las pruebas después de ver los resultados que les gustan, lo que sesga sus conclusiones. Resiste la tentación de echar un vistazo y no termines nunca el examen antes de tiempo.

#### Añade tu prueba a las campañas antes de que se lancen, no después

Si añades tu prueba a una campaña después de que se haya lanzado, la prueba no se ejecutará correctamente y puedes recibir estadísticas incorrectas o engañosas. Por ejemplo, si añades una prueba a una campaña lanzada que permite la reentrada, los usuarios que vuelvan a entrar en la campaña pasarán siempre por el mismo camino para evitar imprecisiones en los datos de la prueba. Además, si cambias alguna de las variantes mientras se está ejecutando la prueba, el cambio invalidará tu prueba y la reiniciará.

Para obtener resultados precisos:
1. Clona la campaña lanzada.
2. Detén la campaña Origin.
3. A continuación, añade la prueba a la campaña clonada. 

#### Si es posible, incluya un grupo de control

Incluir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) le permite saber si sus mensajes tienen un mayor impacto en la conversión de los usuarios que no enviar ningún mensaje.


