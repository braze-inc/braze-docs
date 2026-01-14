---
nav_title: Pruebas multivariantes y A/B
article_title: Pruebas multivariantes y A/B
page_order: 2
page_type: reference
description: "Este artículo de referencia explica las pruebas multivariantes y A/B y sus ventajas."
search_rank: 2
---

# Pruebas multivariantes y A/B

> Esta página explica qué son las pruebas multivariantes y las pruebas A/B y sus ventajas. Para saber cómo crear una prueba multivariante o A/B, consulta [Crear pruebas multivariantes y A/B con Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Se pueden utilizar pruebas multivariantes y A/B mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## ¿Qué son las pruebas multivariantes y las pruebas A/B?

### Pruebas A/B

Una prueba A/B es un experimento que compara las respuestas de los usuarios a varias versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares, pero difieren en la redacción y el estilo.

El objetivo es identificar la versión de la campaña que mejor cumpla tus objetivos de marketing. En esta sección, veremos cómo comprobar la eficacia de las diferencias de contenido.

{% alert note %}
Si quieres evaluar las diferencias en la programación de los mensajes o en el tiempo (por ejemplo, enviar un mensaje de carrito abandonado tras una hora de inactividad frente a un día de inactividad), consulta nuestra sección sobre la [configuración de un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Supón que tienes dos opciones para una notificación push:

- "¡Esta oferta caduca mañana!"
- "¡Esta oferta caduca en 24 horas!"

Utilizando una prueba A/B, puedes ver qué redacción produce una mayor tasa de conversión. La próxima vez que envíes una notificación push sobre una oferta, sabrás qué tipo de redacción es más eficaz. Sin embargo, esta prueba sólo examina el efecto de una variable: la copia de la notificación push.

### Prueba multivariante

Una prueba multivariante es similar a una prueba A/B, salvo que prueba los efectos de dos o más variables. Volvamos a nuestro ejemplo de notificación push. Otra variable que podríamos querer probar es si se incluye un emoji al final del mensaje. Ahora estaríamos probando dos variables (o variantes, no confundir con variantes), de ahí el término "multivariante". Para ello, tendríamos que probar cuatro versiones totales del mensaje: dos opciones para la copia multiplicadas por dos opciones para el emoji (presente o no) es igual a cuatro variantes totales del mensaje.

En la documentación de Braze, "prueba multivariante" se utiliza indistintamente con "prueba A/B", ya que el proceso para configurarlas es el mismo.

## Ventajas de las pruebas multivariantes y A/B {#the-benefits-of}

Las pruebas multivariantes y A/B te ofrecen una forma fácil y clara de conocer a tu audiencia. Ya no tienes que adivinar a qué responderán los usuarios: cada campaña se convierte en una oportunidad para probar distintas variantes de un mensaje y medir la respuesta de la audiencia.

Entre los escenarios específicos en los que las pruebas multivariantes y A/B pueden resultar útiles se incluyen:

- **Al probar un tipo de mensajería por primera vez:** ¿Te preocupa acertar a la primera con los mensajes dentro de la aplicación? Las pruebas multivariantes te permiten experimentar y aprender qué resuena entre tus usuarios.
- **Al crear campañas de incorporación y otras campañas que se envían constantemente:** Puesto que la mayoría de tus usuarios se encontrarán con esta campaña, ¿por qué no asegurarse de que sea lo más eficaz posible?
- **Cuando tengas varias ideas de mensajes para enviar:** Si no estás seguro de cuál elegir, haz una prueba y luego toma una decisión basada en datos.
- **Cuando investigues si tus usuarios responden a las técnicas de marketing "probadas":** Los especialistas en marketing suelen ceñirse a las tácticas convencionales para interactuar con los usuarios, pero la base de usuarios de cada producto es diferente. A veces, repetir tu llamada a la acción y utilizar la demostración social no te dará los resultados deseados. Las pruebas multivariantes y A/B te permiten salir de lo convencional y descubrir tácticas poco convencionales que funcionan para tu audiencia específica.

### Distribución de variantes

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Consejos para pruebas multivariantes y A/B

Las pruebas multivariantes y A/B pueden desvelar información muy valiosa sobre tus usuarios. Para obtener resultados de las pruebas que reflejen realmente el comportamiento de tus usuarios, sigue estas directrices.

#### Ejecuta la prueba en un gran número de usuarios

Las muestras grandes garantizan que tus resultados reflejen las preferencias de tu usuario medio y es menos probable que se vean influidos por valores atípicos. Las muestras de mayor tamaño también te permiten identificar las variantes ganadoras que tienen menores márgenes de victoria.

#### Ordena aleatoriamente a los usuarios en diferentes grupos de prueba

Las pruebas multivariantes te permiten crear hasta ocho grupos de pruebas seleccionados al azar. La aleatorización está diseñada para eliminar el sesgo en el conjunto de pruebas y aumentar las probabilidades de que los grupos de prueba tengan una composición similar. Esto garantiza que las diferentes tasas de respuesta se deban a diferencias en tus mensajes y no en tus muestras.

#### Saber qué elementos quieres probar

Las pruebas multivariantes y A/B te permiten comprobar las diferencias entre varias versiones de un mensaje. En algunos casos, una simple prueba puede ser lo más eficaz, ya que aislar los cambios te permite identificar qué elementos tuvieron mayor impacto en la respuesta. Otras veces, presentar más diferencias entre variantes te permitirá examinar valores atípicos y comparar distintos conjuntos de elementos. Ninguno de los dos métodos es necesariamente erróneo, siempre que tengas claro desde el principio lo que intentas comprobar.

#### Decide cuánto tiempo durará tu prueba y no la finalices antes de tiempo

Antes de empezar la prueba, decide el tiempo que durará y cíñete a él. Los especialistas en marketing suelen caer en la tentación de detener las pruebas después de ver los resultados que les gustan, sesgando sus conclusiones. Resiste la tentación de echar un vistazo y ¡nunca termines tu prueba antes de tiempo!

#### Añade tu prueba a las campañas antes de que se lancen, no después

Si añades tu prueba a una campaña después de que se haya lanzado, la prueba no se ejecutará correctamente y puedes recibir estadísticas incorrectas o engañosas. Por ejemplo, si añades una prueba a una campaña lanzada que permite la reentrada, los usuarios que vuelvan a entrar en la campaña pasarán siempre por el mismo camino para evitar imprecisiones en los datos de la prueba. Además, si cambias alguna de las variantes mientras se está ejecutando la prueba, el cambio invalidará tu prueba y la reiniciará.

Para obtener resultados precisos:
1. Clona la campaña lanzada.
2. Detén la campaña Origin.
3. A continuación, añade la prueba a la campaña clonada. 

#### Si es posible, incluye un grupo de control

Incluir un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) te permite saber si tus mensajes tienen un mayor impacto en la conversión de los usuarios que no enviar ningún mensaje.


