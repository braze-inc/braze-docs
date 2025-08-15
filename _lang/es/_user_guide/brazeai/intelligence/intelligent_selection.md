---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1.0
description: "Este artículo trata sobre Intelligent Selection, una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection es una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje. 

## Acerca de Intelligent Selection

Una variante que parezca rendir más que las demás se enviará a más usuarios, mientras que las variantes de bajo rendimiento se dirigirán a menos usuarios. Cada ajuste se realiza mediante un [algoritmo estadístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garantiza que Braze se ajusta a las diferencias de rendimiento reales y no al azar.

![Sección de pruebas A/B de una campaña con Intelligent Selection habilitada.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligent Selection lo hará:
- Observa repetidamente los datos de rendimiento y desplaza gradualmente el tráfico de la campaña hacia las variantes ganadoras.
- Comprueba que más usuarios reciben tu variante de mejor rendimiento sin sacrificar la confianza estadística.
- Descarta las variantes de bajo rendimiento e identifica las de alto rendimiento más rápidamente que con una [prueba A/B tradicional]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Haz pruebas con más frecuencia y con mayor seguridad de que tus usuarios verán tu mejor mensaje. 

Intelligent Selection funciona mejor en campañas que se envían más de una vez. Necesita datos de rendimiento tempranos para empezar a optimizar, por lo que las campañas de un solo envío no se beneficiarán. Para esas campañas, recomendamos utilizar en su lugar una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) tradicional.

## Requisitos previos

{% tabs %}
{% tab Campaña %}
Antes de añadir Intelligent Selection a tu campaña, asegúrate de que has configurado todo correctamente:

- Tu campaña se envía de forma periódica. No se admiten campañas de envío único.
- Has añadido al menos dos variantes de mensaje.
- Has definido un evento de conversión para medir el rendimiento entre variantes.
- El plazo para volver a ser elegible es de 24 horas o más. No se admiten ventanas más cortas, ya que afectarían a la integridad de la variante de control. Para saber más, consulta [las FAQ sobre Inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Para utilizar Intelligent Selection en un Canvas, confirma lo siguiente:
- Tu Canvas incluye al menos dos variantes de mensaje en un paso en Mensajería.
- Has añadido al menos un evento de conversión.
{% endtab %}
{% endtabs %}

## Añadir Intelligent Selection

Puedes añadir Intelligent Selection a tus campañas y Lienzos.

{% tabs %}
{% tab Campaña %}
Intelligent Selection puede añadirse a cualquier campaña multienvío en el paso **Audiencias objetivo** del compositor de campañas Braze. Las campañas que sólo se envían una vez no pueden aprovechar esta característica.

{% alert note %}
La Intelligent Selection no puede utilizarse en campañas con un periodo de reelección inferior a 24 horas, porque afectaría a la integridad de la variante de control. Para saber más, consulta [las FAQ sobre Inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Añade al menos un evento de conversión y dos variantes a tu Canvas. A continuación, selecciona uno de los porcentajes de variantes en el paso Construir. 

![Un Canvas con dos variantes, cada una ajustada al 50% de distribución de variantes, que permite habilitar la Intelligent Selection.]({% image_buster /assets/img/intelligent_selection.png %})

Esto te permite editar la distribución de variantes y activar la Intelligent Selection. 

![Opción Intelligent Selection activada para un Canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection no estará disponible si aún no has añadido eventos de conversión a tu Canvas o si tu campaña se compone de una sola variante.
{% endtab %}
{% endtabs %}

## Tiempo de ejecución

Para las campañas y los lienzos, Intelligent Selection funcionará hasta que reúna suficientes pruebas sobre las tasas de conversión "verdaderas" de las variantes. "Suficiente" viene determinado por una métrica especial llamada "arrepentimiento". Puedes pensar que es similar a la confianza, en el sentido de que la Intelligent Selection se desactivará cuando haya suficientes datos para saber qué variante es la mejor. 

En la mayoría de los casos, Intelligent Selection elegirá una de las variantes como Variante Ganadora. Esta variante se dará al 100% de la audiencia para futuros envíos.

{% alert note %}
Es posible que la Intelligent Selection deje de optimizar sin elegir un único ganador claro. Intelligent Selection deja de optimizar cuando tiene un 95% de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1% de su tasa actual.
{% endalert %}

## Preguntas más frecuentes (FAQ) {#faq}

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
