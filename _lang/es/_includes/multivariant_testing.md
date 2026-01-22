{% if include.section == "Variant distribution" %}

La distribución entre variantes no siempre es uniforme. Así funciona la distribución de variantes

Cada vez que se envía un mensaje en una campaña multivariante, el sistema selecciona de forma independiente una opción aleatoria según los porcentajes que establezcas y asigna una variante en función del resultado. Es como lanzar una moneda al aire: las anomalías son posibles. Si alguna vez has tirado una moneda al aire 100 veces, sabrás que probablemente no siempre obtendrás un 50-50 exacto entre cara y cruz, aunque sólo tengas dos opciones. Podrías obtener 52 caras y 48 colas.

Si tiene varias variantes que desea dividir por igual, también debe asegurarse de que el número de variantes es múltiplo de 100. De lo contrario, algunas variantes tendrán un mayor porcentaje de usuarios distribuidos a esa variante en comparación con otras. Por ejemplo, si su campaña tiene 7 variantes, no puede haber una distribución uniforme de variantes, ya que 7 no se divide igual por 100 como número entero. En este caso, tendrías 2 variantes del 15 % y 5 variantes del 14 %.

#### Nota sobre los mensajes in-app

Al ejecutar una prueba A/B en mensajes dentro de la aplicación, puede parecer que tus análisis muestran una distribución de variantes mayor entre una variante y otra, aunque tengan una división porcentual uniforme. Por ejemplo, considere el siguiente gráfico de *Destinatarios Únicos* para la Variante A y la Variante C.

![Gráfico de Receptores Únicos para dos variantes con una forma similar entre la Variante A y la Variante C, donde la Variante A tiene un mayor número de Receptores Únicos por día]({% image_buster /assets/img/variant_distribution_iam.png %})

La variante A tiene un mayor número de *destinatarios únicos* que la variante C. Esto no se debe a la distribución de variantes, sino a cómo se calculan *los destinatarios únicos* para los mensajes dentro de la aplicación. Para los mensajes in-app, *los Destinatarios Únicos* son en realidad *Impresiones Únicas*, que es el número total de personas que recibieron y vieron el mensaje in-app. Esto significa que si un usuario no recibe el mensaje por cualquier motivo o decide no verlo, no se incluye en el recuento de *Destinatarios Únicos*, y la distribución de variantes puede aparecer sesgada.

{% endif %}