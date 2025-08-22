---
nav_title: Información del segmento
article_title: Información del segmento
page_order: 8
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "Este artículo te explicará cómo utilizar, interpretar y compartir la información del segmento."
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Información del segmento

> Aprende a utilizar, interpretar y compartir la información del segmento. 

Segment Insights le muestra el rendimiento de un segmento en comparación con otro a través de un conjunto de KPI preseleccionados.

## Ver información por segmentos

Ve a la página **Información del segmento** de tu panel, en **Análisis**, y para ver hasta 10 segmentos diferentes comparados con una línea de base.

![Panel de información del segmento que compara tres segmentos, "Usuarios del Reino Unido", "Usuarios de Francia" y "Usuarios de California", con un segmento de referencia, "Todos los usuarios".]({% image_buster /assets/img_archive/segment_insights.png %})

El segmento base puede ser un segmento específico que usted seleccione o un segmento que contenga a todos sus usuarios. Puede comparar las siguientes estadísticas utilizando Segment Insights:

| Medición | Descripción | Fórmula |
| --------------------- | ------------- | ------------- |
| Sesiones por día | Número medio de sesiones diarias de usuarios del segmento | (número total de sesiones) / (número de días desde la primera sesión) |
| Días desde la primera sesión | Número medio de días entre la primera sesión de los usuarios del segmento y ahora | hoy - fecha de la primera sesión |
| Días desde la última sesión | Número medio de días entre la última sesión de los usuarios del segmento y ahora | hoy - fecha de la última sesión |
| Ingresos vitalicios en dólares | Ingresos medios durante la vida útil en dólares de los usuarios del segmento | gastos del ciclo de vida del usuario |
| Días desde la primera compra | Media de días entre la primera sesión de los usuarios del segmento y la primera compra | fecha de la primera compra - fecha de la primera sesión |
| Días desde la última compra | Media de días entre la última compra de los usuarios del segmento y ahora | hoy - fecha de la última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Puedes compartir fácilmente comparaciones específicas con tus compañeros de equipo utilizando la URL única de la página, y también puedes seleccionar el icono del ojo junto a cada segmento para revelar más información sobre ese segmento. Estas comparaciones se restablecerán cuando cambie de espacio de trabajo.

![Detalles del segmento "Usuarios Premium (iOS VideoApp)" con un gráfico que muestra el historial de miembros y un cuadro que desglosa el tamaño estimado para varios canales de mensajería.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## Página de detalles del segmento

También se ha incorporado información sobre los segmentos en la vista **Detalles del segmento**. Al examinar un segmento concreto que haya configurado previamente, encontrará las mismas seis estadísticas esbozadas en el cuadro dinámico gris Estadísticas del segmento. Desde aquí, puede iniciar rápidamente la herramienta Segment Insights para comparar este segmento en particular con cualquier otro que haya configurado previamente, pero tenga en cuenta que esto sobrescribirá cualquier segmento que haya seleccionado previamente dentro de la herramienta Segment Insights.

![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## Ejemplos {#insights-use-cases}

### Comparación de patrones demográficos de uso y compra

Uno de los mejores usos de Segment Insights es responder a preguntas sobre el impacto de los datos demográficos de los usuarios en el uso de las aplicaciones y la eficacia de las campañas, como por ejemplo:

- ¿Hay determinados grupos demográficos de usuarios que obtienen resultados significativamente mejores o peores que la media?
- ¿Debo replantearme la localización de una campaña concreta?
- ¿Se dirige una campaña a un determinado grupo demográfico?
- ¿Qué objetivos debo fijar para una campaña dirigida a un determinado grupo demográfico?

Segment Insights puede ayudar a descubrir diferencias entre los datos demográficos de los usuarios. El siguiente ejemplo muestra una comparación de la base de usuarios de una aplicación por su idioma, ilustrando cómo los angloparlantes tienden a tener mayores niveles de LTV y actividad que los hablantes de otros idiomas.

![Desglose de la información del segmento en inglés, alemán, francés y español.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

En este ejemplo, los germanoparlantes se inscribieron hace más tiempo por término medio, lo que podría explicar por qué ya no son tan activos. Esto puede deberse a multitud de factores. Por ejemplo, si la aplicación se lanzó primero en Europa, pero ahora es más popular en Estados Unidos, donde la mayoría de la gente habla inglés o español. Para obtener resultados más sólidos, cuando se analizan los indicadores clave de rendimiento en función de la demografía, es sensato comprobar los resultados de un estudio demográfico general (por ejemplo, si el idioma influye en la LTV de todos los usuarios) analizando una población más pequeña y similar y viendo si los resultados persisten.

Para mejorar las conversiones entre hablantes de idiomas distintos del inglés, un buen primer paso sería [localizar las campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) al idioma del dispositivo del usuario y asegurarse de que el texto de esos mensajes atrae a los usuarios, utilizando una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) para probar distintas versiones del texto en el idioma extranjero.

### Comprender los indicadores de mayores ingresos

Conseguir que los usuarios se conviertan en compradores puede ser difícil, y tratar de empujar a los usuarios nuevos, inactivos o desconectados directamente hacia la compra puede llevar al usuario a desinstalar su aplicación. La información del segmento puede ayudarte a descubrir acciones que lleven a los usuarios más abajo en el embudo de compra sin que tengan que comprar todavía, por ejemplo, suscribirse a tu boletín de noticias, compartir en redes sociales o registrarse para recibir mensajes promocionales. Por ejemplo, puedes trazar el impacto en las compras de diferentes comportamientos dentro de una aplicación de comercio electrónico.

![Desglose de la información del segmento para los usuarios que compartieron en redes sociales, se registraron para promociones y se suscribieron al boletín de noticias.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

En este caso, son relativamente pocos los usuarios que se han registrado para recibir mensajes promocionales y no son tan activos, pero estos usuarios generan mayores ingresos de por vida. Para aumentar los ingresos, puede ser una buena idea incluir una invitación a registrarse para recibir mensajes promocionales en las campañas de incorporación. Para reactivar la interacción de los usuarios que han abandonado, un buen plan sería enviar una [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) típica [para usuarios que han abandonado]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) y dirigirse a [los usuarios que se han convertido]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) con una campaña posterior para que se registren para recibir mensajes promocionales.

