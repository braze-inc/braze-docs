---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre inteligencia
page_order: 191
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre Canal inteligente, Selección inteligente y Temporización inteligente."
---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a las preguntas más frecuentes sobre la Intelligence Suite.

## Intelligent Selection

### ¿Por qué no se puede volver a ser elegible en menos de 24 horas cuando se combina con Intelligent Selection?

No permitimos que las campañas de Intelligent Selection vuelvan a ser elegibles en un plazo demasiado corto, porque afectaría a la integridad de la variante de control. Al crear un intervalo de 24 horas, ayudamos a garantizar que el algoritmo dispondrá de un conjunto de datos estadísticamente válido con el que trabajar.

Normalmente, las campañas con reelegibilidad harán que los usuarios vuelvan a introducir la misma variante que recibieron antes. Con Intelligent Selection, Braze no puede garantizar que un usuario reciba la misma variante de campaña, porque la distribución de variantes se habría desplazado debido al aspecto de asignación óptima de esta característica. Si se permitiera al usuario volver a entrar antes de que Intelligent Selection volviera a examinar el rendimiento de la variante, los datos podrían estar sesgados debido a los usuarios que volvieron a entrar.

Por ejemplo, si una campaña utiliza estas variantes:

- Variante A: 20%
- Variante B: 20%
- Control: 60 %

Entonces la distribución de variantes podría ser la siguiente para la segunda vuelta:

- Variante A: 15%
- Variante B: 25 %
- Control: 60 %

### ¿Por qué mis variantes de Intelligent Selection muestran envíos iguales durante las primeras fases de mi campaña?

Intelligent Selection asigna variantes de envío en función del estado actual de conversión de la campaña. Sólo determina las asignaciones finales de variantes tras un periodo de entrenamiento, en el que los envíos se reparten uniformemente entre las variantes. Si no quieres que la Intelligent Selection envíe uniformemente durante las primeras fases de tu campaña, utiliza variantes fijas para una prueba A/B tradicional.

### ¿Dejará la Intelligent Selection de optimizar sin elegir un claro ganador?

Intelligent Selection dejará de optimizar cuando tenga un 95% de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1% de su tasa actual.

### ¿Por qué no puedo habilitar Intelligent Selection en mi Canvas o campaña (aparece en gris)?

Intelligent Selection no estará disponible si:

- No has añadido eventos de conversión a tu campaña o Canvas
- Estás creando una campaña de envío único
- Tienes habilitada la reeligibilidad con una ventana inferior a 24 horas
- Tu Canvas está compuesto por una única variante sin variantes adicionales ni grupos de control añadidos
- Tu Canvas está compuesto por un único grupo de control, sin variantes añadidas

## Intelligent Timing

### ¿Predice el Intelligent Timing cuándo es más probable que un usuario convierta, o sólo cuándo es más probable que abra o haga clic?

Intelligent Timing predice cuándo es más probable que un usuario abra o haga clic.

### ¿Cómo se determina la hora de la aplicación más popular?

La hora de la aplicación más popular viene determinada por la hora media de inicio de sesión del espacio de trabajo (en hora local). Esta métrica se puede encontrar en el panel al previsualizar los tiempos de una campaña, se muestra en rojo.

### ¿Tiene en cuenta el Intelligent Timing la apertura de la máquina?

Sí, las aperturas de la máquina son filtradas por Intelligent Timing, por lo que no influyen en su rendimiento.

### ¿Cómo puedo asegurarme de que Intelligent Timing funciona lo mejor posible?

Intelligent Timing utiliza el historial individual de interacción con mensajes de cada usuario en cualquier momento en que haya recibido mensajes. Antes de utilizar Intelligent Timing, asegúrate de que has enviado mensajes a los usuarios a distintas horas del día. De ese modo, puedes "muestrear" cuándo puede ser el mejor momento para cada usuario. Un muestreo inadecuado de las distintas horas del día puede hacer que Intelligent Timing elija una hora de envío que no sea la óptima para un usuario. 

### ¿Con cuánta antelación debo lanzar una campaña de Intelligent Timing para entregarla con éxito a todos los usuarios de todas las zonas horarias?

Braze calcula la hora óptima a medianoche en la hora de Samoa, uno de los primeros husos horarios del mundo. En un solo día, abarca aproximadamente 48 horas. Por ejemplo, alguien cuya hora óptima son las 12:01 de la mañana y vive en Australia ya ha pasado su hora óptima, y es "demasiado tarde" para enviársela. Por estas razones, tienes que programarlo con 48 horas de antelación para garantizar que todas las personas del mundo que utilicen tu aplicación la reciban correctamente.

### ¿Por qué mi campaña de Intelligent Timing muestra pocos o ningún envío?

Braze necesita un número base de puntos de datos para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura de correo electrónico (como los nuevos usuarios), Intelligent Timing puede predeterminar la hora más popular del espacio de trabajo en ese día de la semana. Si no hay suficiente información sobre el espacio de trabajo, volvemos a la hora predeterminada de las 17 h. También puedes elegir establecer una [hora específica de alternativa]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options).

### ¿Por qué mi campaña de Intelligent Timing se envía pasada la fecha programada?

Puede que tu campaña de Intelligent Timing esté enviando más allá de la fecha programada porque estás aprovechando las pruebas A/B. Las campañas que utilizan pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba A/B, lo que aumenta la duración del envío de la campaña. Por defecto, las campañas de Intelligent Timing se programarán para enviar la variante ganadora a los usuarios restantes para el día siguiente, pero puedes cambiar esta fecha de envío.

Te recomendamos que, si tienes campañas con Intelligent Timing, dejes más tiempo para que finalice la prueba A/B y programes el envío de la variante ganadora para dentro de dos días en lugar de uno. 

### ¿Cuándo comprueba Braze los criterios de elegibilidad de los filtros de segmento y audiencia?

Braze realiza dos comprobaciones cuando se lanza una campaña:

1. En cuanto se identifica la primera zona horaria, se inicia el proceso de puesta en cola de usuarios, y
2. A la hora programada para ver si los usuarios siguen siendo elegibles para recibir la campaña.

Ten cuidado al crear campañas que filtren envíos de otras campañas. Por ejemplo, si enviaras dos campañas el mismo día para horas distintas, y añades un filtro que sólo permita a los usuarios recibir la segunda campaña si han recibido la primera, los usuarios no recibirán la segunda campaña. Esto se debe a que nadie era elegible cuando se creó la campaña y se formaron los segmentos.

### ¿Puedo utilizar horas tranquilas en mi campaña de Intelligent Timing?

No recomendamos utilizar tanto Intelligent Timing como horas tranquilas para tu campaña o Canvas, ya que es contraproducente. Las horas tranquilas se basan en suposiciones descendentes sobre el comportamiento de los usuarios, mientras que el Intelligent Timing se basa en la actividad de los usuarios.

### ¿Puedo utilizar Intelligent Timing y la limitación de tasas?

Braze no recomienda el uso de Intelligent Timing y la limitación de tasa porque no hay garantías sobre cuándo se entregará el mensaje.

### ¿Puedo utilizar Intelligent Timing durante el calentamiento de IP?

Braze no recomienda utilizar Intelligent Timing cuando los usuarios estén calentando de IP por primera vez, ya que algunos de sus comportamientos pueden causar dificultades para alcanzar los volúmenes diarios. Esto se debe a que Intelligent Timing evalúa dos veces los segmentos de la campaña. Una vez cuando se construye la campaña por primera vez, y una segunda vez antes de enviarla a los usuarios para verificar que deben seguir estando en ese segmento. 

Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.
