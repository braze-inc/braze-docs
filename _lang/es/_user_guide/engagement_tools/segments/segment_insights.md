---
nav_title: Información del segmento
article_title: Información del segmento
page_order: 4
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

Vaya a la página **Segment Insights** de su panel de control, en **Analytics**, y haga clic en <i class="fas fa-plus"></i> **Add Segment** para ver hasta cuatro segmentos diferentes comparados con una línea de base.

{% alert note %}
Si está utilizando la [navegación anterior]({{site.baseurl}}/navigation), puede encontrar esta página en **Participación** > **Segmentos** > **Información de segmentos**.
{% endalert %}

![Panel de información del segmento.][1]

El segmento base puede ser un segmento específico que usted seleccione o un segmento que contenga a todos sus usuarios. Puede comparar las siguientes estadísticas utilizando Segment Insights:

| Medición | Descripción | Fórmula |
| --------------------- | ------------- | ------------- |
| Frecuencia de sesiones | Número medio de sesiones diarias de usuarios del segmento | (número total de sesiones) / (número de días desde la primera sesión) |
| Tiempo transcurrido desde la primera sesión | Tiempo promedio entre la primera sesión de los usuarios de segmentos y ahora | hoy - fecha de la primera sesión |
| Tiempo transcurrido desde la última sesión | Tiempo promedio entre la última sesión de los usuarios de segmentos y ahora | hoy - fecha de la última sesión |
| Ingresos del ciclo de vida | Ingresos promedio del ciclo de vida para los usuarios del segmento | gastos del ciclo de vida del usuario |
| Tiempo hasta la primera compra | Tiempo promedio entre la primera sesión de los usuarios de segmentos y su primera compra | fecha de la primera compra - fecha de la primera sesión |
| Tiempo transcurrido desde la última compra | Tiempo promedio entre la última compra de los usuarios de segmentos y ahora | hoy - fecha de la última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Puede compartir fácilmente comparaciones específicas con sus compañeros de equipo utilizando la URL única de la página, y también puede hacer clic debajo de cada segmento para revelar más información sobre el mismo. Estas comparaciones se restablecerán cuando cambie de espacio de trabajo.

![][2]

## Página de detalles del segmento

También se ha incorporado información sobre los segmentos en la vista **Detalles del segmento**. Al examinar un segmento concreto que haya configurado previamente, encontrará las mismas seis estadísticas esbozadas en el cuadro dinámico gris Estadísticas del segmento. Desde aquí, puede iniciar rápidamente la herramienta Segment Insights para comparar este segmento en particular con cualquier otro que haya configurado previamente, pero tenga en cuenta que esto sobrescribirá cualquier segmento que haya seleccionado previamente dentro de la herramienta Segment Insights.

![][3]

## Ejemplos {#insights-use-cases}

### Comparación de patrones demográficos de uso y compra

Uno de los mejores usos de Segment Insights es responder a preguntas sobre el impacto de los datos demográficos de los usuarios en el uso de las aplicaciones y la eficacia de las campañas, como por ejemplo:

- ¿Hay determinados grupos demográficos de usuarios que obtienen resultados significativamente mejores o peores que la media?
- ¿Debo replantearme la localización de una campaña concreta?
- ¿Se dirige una campaña a un determinado grupo demográfico?
- ¿Qué objetivos debo fijar para una campaña dirigida a un determinado grupo demográfico?

Segment Insights puede ayudar a descubrir diferencias entre los datos demográficos de los usuarios. El siguiente ejemplo muestra una comparación de la base de usuarios de una aplicación por su idioma, ilustrando cómo los angloparlantes tienden a tener mayores niveles de LTV y actividad que los hablantes de otros idiomas.

![][5]

En este ejemplo, los germanoparlantes se inscribieron hace más tiempo por término medio, lo que podría explicar por qué ya no son tan activos. Esto puede deberse a multitud de factores. Por ejemplo, si la aplicación se lanzó primero en Europa, pero ahora es más popular en Estados Unidos, donde la mayoría de la gente habla inglés o español. Para obtener resultados más sólidos, cuando se analizan los indicadores clave de rendimiento en función de la demografía, es sensato comprobar los resultados de un estudio demográfico general (por ejemplo, si el idioma influye en la LTV de todos los usuarios) analizando una población más pequeña y similar y viendo si los resultados persisten.

Para mejorar las conversiones entre hablantes de idiomas distintos del inglés, un buen primer paso sería [localizar las campañas][10] al idioma del dispositivo del usuario y asegurarse de que el texto de esos mensajes atrae a los usuarios utilizando una [campaña multivariante][11] para probar distintas versiones del texto en el idioma extranjero.

### Comprender los indicadores de mayores ingresos

Conseguir que los usuarios se conviertan en compradores puede ser difícil, y tratar de empujar a los usuarios nuevos, inactivos o desconectados directamente hacia la compra puede llevar al usuario a desinstalar su aplicación. Segment Insights puede ayudarle a descubrir acciones que lleven a los usuarios más lejos en el embudo de compra sin que tengan que comprar todavía, por ejemplo, añadir artículos a su lista de deseos, compartir en las redes sociales o dar un favorito a un contenido. Por ejemplo, puedes trazar el impacto en las compras de diferentes comportamientos dentro de una aplicación de comercio electrónico.

![][7]

En este caso, son relativamente pocos los usuarios suscritos al boletín, pero suelen ser los más activos. Para mantener el interés de los nuevos usuarios, sería una buena idea incluir una invitación para solicitar el boletín en las campañas de incorporación. Para volver a captar a los usuarios antiguos, un buen plan sería enviar una campaña típica de [usuario antiguo][9] y dirigirse a [usuarios que se convirtieron][12] con una campaña posterior para que se suscriban al boletín de noticias.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
