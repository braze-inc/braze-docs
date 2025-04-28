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

---

## Intelligent Timing

### General

#### ¿Qué predice el Intelligent Timing?

Intelligent Timing se centra en predecir cuándo es más probable que un usuario abra o haga clic en tus mensajes para garantizar que tus mensajes lleguen a los usuarios en los momentos óptimos de interacción.

#### ¿Se calcula el Intelligent Timing por separado para cada día de la semana?

No, el Intelligent Timing no está vinculado a días concretos. En su lugar, personaliza los tiempos de envío en función de los patrones de interacción únicos de cada usuario y del canal que estés utilizando, como el correo electrónico o las notificaciones push. Esto garantiza que tus mensajes lleguen a los usuarios cuando están más receptivos.

### Cálculos

#### ¿Qué datos se utilizan para calcular el tiempo óptimo para cada usuario?

Para calcular el tiempo óptimo, Intelligent Timing:

1. Analiza los datos de interacción de cada usuario registrados por el SDK de Braze. Esto incluye lo siguiente:
  - Horario de las sesiones
  - Push Direct Opens
  - Push Influenced Opens
  - Clics en el correo electrónico
  - Aperturas de correo electrónico (excluyendo aperturas de máquina)
2. Agrupa estos eventos por hora, identificando la hora de envío óptima para cada usuario.

#### ¿Se incluyen las Aperturas de Máquina al calcular el tiempo óptimo?

No, [las Aperturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens) se excluyen de los cálculos del tiempo óptimo. Esto significa que los tiempos de envío se basan únicamente en la interacción real de los usuarios, lo que proporciona una sincronización más precisa para tus campañas.

#### ¿Cómo de preciso es el momento óptimo?

Intelligent Timing programa mensajes durante la "hora de mayor interacción" de cada usuario, basándose en los eventos de inicio de sesión y apertura de mensajes. Dentro de esa hora, la hora del mensaje se redondea a los cinco minutos más próximos. Por ejemplo, si la hora óptima de un usuario se calcula a las 16:58, el mensaje se programará para las 17:00. Puede haber ligeros retrasos en la entrega debido a la actividad del sistema durante los periodos de mayor actividad.

#### ¿Cuáles son los cálculos alternativos si no hay datos suficientes?

Si hay menos de cinco eventos relevantes para un usuario, Intelligent Timing utiliza la [hora alternativa][1] de tu configuración de mensajes. 

### Administrador de campaña

#### ¿Con cuánta antelación debo lanzar una campaña de Intelligent Timing para entregarla con éxito a todos los usuarios de todas las zonas horarias?

Braze calcula la hora óptima a medianoche en la hora de Samoa, uno de los primeros husos horarios del mundo. En un solo día, abarca aproximadamente 48 horas. Por ejemplo, alguien cuya hora óptima son las 12:01 de la mañana y vive en Australia ya ha pasado su hora óptima, y es "demasiado tarde" para enviársela. Por estas razones, necesitas programar con 48 horas de antelación para entregar con éxito a todas las personas del mundo que utilicen tu aplicación.

#### ¿Por qué mi campaña de Intelligent Timing muestra pocos o ningún envío?

Braze necesita un número base de puntos de datos para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura de correo electrónico (como los nuevos usuarios), Intelligent Timing puede predeterminar la hora más popular del espacio de trabajo en ese día de la semana. Si no hay suficiente información sobre el espacio de trabajo, volvemos a la hora predeterminada de las 17 h. También puedes elegir establecer una [hora específica de alternativa]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options).

#### ¿Por qué mi campaña de Intelligent Timing se envía pasada la fecha programada?

Puede que tu campaña de Intelligent Timing esté enviando más allá de la fecha programada porque estás aprovechando las pruebas A/B. Las campañas que utilizan pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba A/B, lo que aumenta la duración del envío de la campaña. Por defecto, las campañas de Intelligent Timing se programarán para enviar la variante ganadora a los usuarios restantes para el día siguiente, pero puedes cambiar esta fecha de envío.

Te recomendamos que, si tienes campañas con Intelligent Timing, dejes más tiempo para que finalice la prueba A/B y programes el envío de la variante ganadora para dentro de dos días en lugar de uno. 

### Consideraciones técnicas

#### ¿Cuándo comprueba Braze los criterios de elegibilidad de los filtros de segmento y audiencia?

Braze realiza dos comprobaciones cuando se lanza una campaña:

1. **Comprobación inicial:** A medianoche en la primera zona horaria del día de envío.
2. **Comprobación de la hora programada:** Justo antes de enviar a la hora Intelligent Timing seleccionada por el usuario.

Ten cuidado al filtrar en función de otros envíos de campaña para evitar dirigirte a segmentos no elegibles. Por ejemplo, si enviaras dos campañas el mismo día para horas distintas, y añades un filtro que sólo permita a los usuarios recibir la segunda campaña si han recibido la primera, los usuarios no recibirán la segunda campaña. Esto se debe a que nadie era elegible cuando se creó la campaña y se formaron los segmentos.

#### ¿Puedo utilizar horas tranquilas en mi campaña de Intelligent Timing?

Las Horas tranquilas pueden utilizarse en una campaña que utilice Intelligent Timing. El algoritmo de Intelligent Timing evitará las horas tranquilas para seguir enviando el mensaje a todos los usuarios elegibles. Dicho esto, te recomendamos que desactives las Horas tranquilas, a menos que haya implicaciones legales, de cumplimiento de normas o de otro tipo sobre cuándo se pueden enviar mensajes y cuándo no.

#### ¿Qué ocurre si la hora óptima para un usuario está dentro de las horas tranquilas? 

Si la hora óptima determinada cae dentro de las Horas Tranquilas, Braze encuentra el límite más cercano de las Horas Tranquilas y programa el mensaje para la siguiente hora permitida antes o después de las Horas Tranquilas. El mensaje se pone en cola para enviarse en el límite más cercano de las horas tranquilas en relación con la hora óptima.

#### ¿Puedo utilizar Intelligent Timing y la limitación de tasas?

El límite de velocidad puede utilizarse en una campaña que utilice Intelligent Timing. Sin embargo, la naturaleza del límite de velocidad implica que algunos usuarios pueden recibir su mensaje en un momento que no sea el óptimo, sobre todo si un gran número de usuarios en relación con el tamaño del límite de velocidad están programados en el momento alternativo debido a la insuficiencia de datos. 

Recomendamos utilizar el límite de velocidad en una campaña de Intelligent Timing sólo cuando haya requisitos técnicos que deban cumplirse utilizando el límite de tasa.

#### ¿Puedo utilizar Intelligent Timing durante el calentamiento de IP?

Braze no recomienda utilizar Intelligent Timing cuando los usuarios estén calentando de IP por primera vez, ya que algunos de sus comportamientos pueden causar dificultades para alcanzar los volúmenes diarios. Esto se debe a que Intelligent Timing evalúa dos veces los segmentos de la campaña. Una vez cuando se construye la campaña por primera vez, y una segunda vez antes de enviarla a los usuarios para verificar que deben seguir estando en ese segmento.

Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

#### ¿Cómo se determina la hora de la aplicación más popular?

La hora de la aplicación más popular viene determinada por la hora media de inicio de sesión del espacio de trabajo (en hora local). Esta métrica se puede encontrar en el panel al previsualizar los tiempos de una campaña, se muestra en rojo.

#### ¿Tiene en cuenta el Intelligent Timing la apertura de la máquina?

Sí, las aperturas de la máquina son filtradas por Intelligent Timing, por lo que no influyen en su rendimiento.

#### ¿Cómo puedo asegurarme de que Intelligent Timing funciona lo mejor posible?

Intelligent Timing utiliza el historial individual de interacción con mensajes de cada usuario en cualquier momento en que haya recibido mensajes. Antes de utilizar Intelligent Timing, asegúrate de que has enviado mensajes a los usuarios a distintas horas del día. De ese modo, puedes "muestrear" cuándo puede ser el mejor momento para cada usuario. Un muestreo inadecuado de las distintas horas del día puede hacer que Intelligent Timing elija una hora de envío que no sea la óptima para un usuario.


[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing#fallback-time
