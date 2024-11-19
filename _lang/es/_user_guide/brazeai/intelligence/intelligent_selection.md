---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1
description: "Este artículo trata sobre Intelligent Selection, una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje."
search_rank: 10
---

# Intelligent Selection {#intelligent-selection}

> Intelligent Selection es una característica que analiza el rendimiento de una campaña recurrente o Canvas dos veces al día y ajusta automáticamente el porcentaje de usuarios que reciben cada variante de mensaje. 

Una variante que parezca rendir más que las demás se enviará a más usuarios, mientras que las variantes de bajo rendimiento se dirigirán a menos usuarios. Cada ajuste se realiza utilizando un [algoritmo estadístico][227] que garantiza que estamos ajustando las diferencias reales de rendimiento y no sólo el azar.

![Sección de pruebas A/B de una campaña con Intelligent Selection habilitada.][3]

Intelligent Selection lo hará:
- Observa repetidamente los datos de rendimiento y desplaza gradualmente el tráfico de la campaña hacia las variantes ganadoras.
- Comprueba que más usuarios reciben tu variante de mejor rendimiento sin sacrificar la confianza estadística.
- Descarta las variantes de bajo rendimiento e identifica las de alto rendimiento más rápidamente que con una [prueba A/B tradicional][1].
- Haz pruebas con más frecuencia y con mayor seguridad de que tus usuarios verán tu mejor mensaje. 

Intelligent Selection es ideal para campañas programadas para enviarse varias veces. Los resultados iniciales son necesarios para empezar a ajustar tu campaña; por tanto, una campaña que sólo se envíe una vez no será beneficiosa. Para esas campañas, una [prueba A/B][1] sería más eficaz.

## ¿Cómo añado Intelligent Selection a mis campañas?

### Campaña Intelligent Selection
Intelligent Selection puede añadirse a cualquier campaña multienvío en el paso **Audiencias objetivo** del compositor de campañas Braze. Las campañas que sólo se envían una vez no pueden aprovechar esta característica.

### Canvas Selección Inteligente
Cuando añadas variantes a tu Canvas, haz clic en uno de los porcentajes de variantes. Esto te permite editar la distribución de variantes y activar la Intelligent Selection.

![Un Canvas con dos variantes, cada una ajustada al 50% de distribución de variantes, que permite habilitar la Intelligent Selection.][2]

Intelligent Selection no estará disponible si aún no has añadido eventos de conversión a tu Canvas o si tu campaña se compone de una sola variante.

{% alert note %}
No permitimos el uso de Intelligent Selection con campañas con habilitación de reeleccionabilidad en menos de 24 horas porque afectaría a la integridad de la variante de control. Consulta [las FAQ sobre Inteligencia]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection) para saber más.
{% endalert %}

## ¿Durante cuánto tiempo funcionará?

Para las campañas y los lienzos, Intelligent Selection funcionará hasta que reúna suficientes pruebas sobre las tasas de conversión "verdaderas" de las variantes. "Suficiente" viene determinado por una métrica especial llamada "arrepentimiento". Puedes pensar que es similar a la confianza, en el sentido de que la Intelligent Selection se desactivará cuando haya suficientes datos para saber qué variante es la mejor. 

En la mayoría de los casos, Intelligent Selection elegirá una de las variantes como Variante Ganadora. Esta variante se dará al 100% de la audiencia para futuros envíos.

{% alert note %}
Es posible que la Intelligent Selection deje de optimizar sin elegir un único ganador claro. Intelligent Selection deja de optimizar cuando tiene un 95% de confianza en que continuar el experimento no mejorará la tasa de conversión en más de un 1% de su tasa actual.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[2]: {% image_buster /assets/img/intelligent_selection.png %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit

