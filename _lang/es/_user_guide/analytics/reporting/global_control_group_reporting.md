---
nav_title: Grupo de control global
article_title: Informes del grupo de control global
page_type: reference
description: "Esta página cubre las métricas de los informes que se encuentran en la página Informes del grupo de control global del panel."
tool: 
  - Reports

---

# Informe del grupo de control global

> El Informe del grupo de control global te permite comparar tu grupo con una muestra de tratamiento. Tu muestra de tratamiento es una selección aleatoria de usuarios no control, aproximadamente el mismo número de usuarios que tu control, generada mediante el método del Número de contenedor aleatorio.

## Ver un informe

Para ver un informe de tu [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) desde el panel, ve a **Análisis** > **Informe de grupo de control global**. 

A continuación, selecciona el parámetro con el que deseas ejecutar el informe (sesiones o un evento personalizado concreto) y selecciona **Ejecutar informe**.

\![]({% image_buster /assets/img/control_group/control_group6.png %})

## Configurar tu informe

Cuando generes tu informe, elige un evento -ya sean sesiones o cualquier evento personalizado- para comparar los grupos de tratamiento y de control. A continuación, elige un periodo de tiempo para el que quieras ver los datos. Ten en cuenta que si has guardado varios experimentos de grupo de control en distintos periodos de tiempo, debes evitar incluir datos de más de un experimento en tu informe.

Ten en cuenta que las métricas porcentuales de tu informe están redondeadas. Por ejemplo, en los casos en que el número de conversiones sea un porcentaje muy bajo de tu grupo de control o de tratamiento global, la tasa de conversión puede redondearse al 0%.

Por último, como ocurre con otros informes de nuestra plataforma, este informe muestra un porcentaje de [confianza]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) para tu cambio respecto a la métrica de control. Ten en cuenta que en los casos en que la tasa de conversión entre tu grupo de control y el de tratamiento sean idénticas, cabe esperar una confianza del 0%; esto indica que hay un 0% de probabilidades de que haya una diferencia de rendimiento entre los dos grupos. 

### Tamaño de los grupos

Antes de mayo de 2024, el grupo de control global fue excluido del archivado de usuarios, pero no así el grupo de muestra de tratamiento. A partir de mayo de 2024, ambos grupos quedan excluidos del archivado de usuarios. Esto podría hacer que tu grupo de muestra de tratamiento y tu grupo de control global tuvieran tamaños significativamente diferentes. La próxima vez que restablezcas tu Grupo de control global, esta discrepancia se resolverá y verás tamaños de grupo similares.

{% alert note %}
Cada espacio de trabajo tiene como máximo un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios, independientemente de cómo configures tus informes de control global.
{% endalert %}

## Métrica del informe

| Métrica | Definición | Cálculo |
| -- | -- | -- |
| Cambio de Control | Calcula la diferencia entre la tasa de conversión de tus grupos de tratamiento y de control. | ((Tasa de conversión del tratamiento - tasa de conversión del control) ÷ tasa de conversión del control) * 100 |
| Elevación incremental | La diferencia de acontecimientos totales entre tus grupos de tratamiento y de control. Esta métrica pretende responder a la pregunta "¿Cuántos eventos de conversión más consiguió el grupo de tratamiento?". | Total de acontecimientos para el tratamiento - total de acontecimientos para el control |
| Porcentaje de elevación incremental | El porcentaje del total de eventos de tu tratamiento que puede atribuirse a tu tratamiento (frente al comportamiento natural del usuario). Se calcula dividiendo el aumento incremental (número) por el número total de acontecimientos de tu grupo de tratamiento. | Aumento incremental (número) ÷ Total de acontecimientos del grupo de tratamiento |
| Tasa de conversión | El porcentaje estimado de usuarios de tu grupo de control o tratamiento que completan el evento seleccionado durante el periodo de tiempo seleccionado. Se calcula sumando el número de eventos del periodo de tiempo y dividiéndolo por la suma de usuarios del grupo cada día. Esto sólo puede ser aproximado porque el tamaño del grupo fluctúa regularmente a medida que entran nuevos usuarios en tu grupo de control global, y los eventos son totales -y no únicos-. Si el número de conversiones es muy pequeño y tus grupos de control o tratamiento son muy grandes, la tasa de conversión puede redondearse al 0%. Si el número de eventos es muy elevado -por ejemplo, en los casos en que un usuario puede realizar más de un evento al día-, la tasa de conversión puede superar el 100%. | Suma del número de eventos de esos usuarios durante ese periodo de tiempo ÷ suma de usuarios del grupo cada día |
| Tamaño estimado del grupo | El número estimado de usuarios en tus grupos de control y tratamiento durante el periodo de tiempo seleccionado. | El tamaño máximo de miembros que alcanzaron tus grupos de control y tratamiento durante el periodo de tiempo que elegiste para el informe. |
| Número total de eventos | El número total de veces que ocurrió el suceso seleccionado durante el periodo de tiempo elegido. No es único (por ejemplo, si un usuario realiza un evento dos veces durante el periodo de tiempo, el evento se incrementa dos veces). | Suma del número de veces que se produjo un suceso cada día durante el periodo de tiempo elegido. |
| Eventos por usuario | El número medio estimado de veces que los usuarios de cada grupo completaron tus eventos de conversión durante el periodo de tiempo seleccionado. | Total de actos ÷ tamaño estimado del grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

