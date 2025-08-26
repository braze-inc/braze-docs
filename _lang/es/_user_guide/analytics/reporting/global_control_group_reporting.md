---
nav_title: Grupo de control global 
article_title: Informes de grupos de control global
page_type: reference
description: "Esta página cubre las métricas de los informes que se encuentran en la página Informes del grupo de control global del panel."
tool: 
  - Reports

---

# Informe del Grupo de control global

> El Informe global del grupo de control le permite comparar su grupo con una muestra de tratamiento. Su muestra de tratamiento es una selección aleatoria de usuarios no control, aproximadamente el mismo número de usuarios que su control, generada mediante el método de números aleatorios de cubo.

## Ver un informe

Para ver un informe de tu [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) desde el panel, ve a **Análisis** > **Informe de grupo de control global**. 

A continuación, selecciona el parámetro con el que deseas ejecutar el informe (sesiones o un evento personalizado concreto) y selecciona **Ejecutar informe**.

![]({% image_buster /assets/img/control_group/control_group6.png %})

## Configurar tu informe

Al generar el informe, elija un evento (sesiones o cualquier evento personalizado) para comparar los grupos de tratamiento y control. A continuación, elija un periodo de tiempo para el que desee ver los datos. Tenga en cuenta que si ha guardado varios experimentos de grupos de control en distintos periodos de tiempo, debe evitar incluir datos de más de un experimento en su informe.

Tenga en cuenta que las métricas porcentuales de su informe están redondeadas. Por ejemplo, en los casos en que el número de conversiones sea un porcentaje muy bajo de tu grupo de control o de tratamiento global, la tasa de conversión puede redondearse al 0%.

Por último, al igual que otros informes de nuestra plataforma, este informe muestra un porcentaje de [confianza]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) para su métrica de cambio con respecto al control. Ten en cuenta que en los casos en que la tasa de conversión entre tu grupo de control y el de tratamiento sean idénticas, cabe esperar una confianza del 0 %; esto indica que hay un 0 % de probabilidades de que haya una diferencia de rendimiento entre los dos grupos. 

### Tamaño de los grupos

Antes de mayo de 2024, el grupo de control global fue excluido del archivado de usuarios, pero no así el grupo de muestra de tratamiento. A partir de mayo de 2024, ambos grupos quedan excluidos del archivado de usuarios. Esto podría hacer que tu grupo de muestra de tratamiento y tu grupo de control global tuvieran tamaños significativamente diferentes. La próxima vez que restablezca su Grupo de control global, esta discrepancia se resolverá y verá tamaños de grupo similares.

{% alert note %}
Cada espacio de trabajo tiene como máximo un grupo de control global y un grupo de muestra de tratamiento. El grupo de muestra de tratamiento es el mismo grupo de usuarios, independientemente de cómo configures tus informes de control global.
{% endalert %}

## Métricas de los informes

| Métrica | Definición | Cálculo |
| -- | -- | -- |
| Cambio desde el control | Calcula la diferencia entre la tasa de conversión de tus grupos de tratamiento y de control. | ((Tasa de conversión del tratamiento - tasa de conversión del control) ÷ tasa de conversión del control) * 100 |
| Uplift incremental | La diferencia de eventos totales entre los grupos de tratamiento y control. Esta métrica pretende responder a la pregunta "¿Cuántos eventos de conversión más consiguió el grupo de tratamiento?". | Total de eventos para el tratamiento - total de eventos para el control |
| Porcentaje de uplift incremental | El porcentaje del total de eventos de su tratamiento que puede atribuirse a su tratamiento (frente al comportamiento natural del usuario). Se calcula dividiendo el aumento incremental (número) por el número total de eventos de su grupo de tratamiento. | Aumento incremental (número) ÷ Total de eventos para el grupo de tratamiento |
| Tasa de conversión | El porcentaje estimado de usuarios de tu grupo de control o tratamiento que completan el evento seleccionado durante el periodo de tiempo seleccionado. Se calcula sumando el número de eventos del periodo de tiempo y dividiéndolo por la suma de usuarios del grupo cada día. Esto sólo puede ser aproximado porque el tamaño del grupo fluctúa regularmente a medida que entran nuevos usuarios en tu grupo de control global, y los eventos son totales -y no únicos-. Si el número de conversiones es muy pequeño y sus grupos de control o tratamiento son muy grandes, el índice de conversión puede redondearse al 0%. Si el número de eventos es muy elevado -por ejemplo, en los casos en que un usuario puede realizar más de un evento al día-, la tasa de conversión puede superar el 100%. | Suma del número de eventos de esos usuarios durante ese periodo de tiempo ÷ suma de usuarios del grupo cada día |
| Tamaño de grupo estimado | El número estimado de usuarios en sus grupos de control y tratamiento durante el periodo de tiempo seleccionado. | El número máximo de miembros que alcanzaron sus grupos de control y tratamiento durante el periodo de tiempo que eligió para el informe. |
| Cantidad total de eventos | El número total de veces que se ha producido el suceso seleccionado durante el periodo de tiempo elegido. Esto no es único (por ejemplo, si un usuario realiza un evento dos veces durante el periodo de tiempo, el evento se incrementa dos veces). | Suma del número de veces que se ha producido un suceso cada día durante el periodo de tiempo elegido. |
| Eventos por usuario | El número medio estimado de veces que los usuarios de cada grupo completaron sus eventos de conversión durante el periodo de tiempo seleccionado. | Total de eventos ÷ tamaño estimado del grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

