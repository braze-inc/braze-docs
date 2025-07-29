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





El segmento base puede ser un segmento específico que usted seleccione o un segmento que contenga a todos sus usuarios. Puede comparar las siguientes estadísticas utilizando Segment Insights:

| Medición | Descripción | Fórmula |
| --------------------- | ------------- | ------------- |
|  | Número medio de sesiones diarias de usuarios del segmento | (número total de sesiones) / (número de días desde la primera sesión) |
|  |  | hoy - fecha de la primera sesión |
|  |  | hoy - fecha de la última sesión |
|  |  | gastos del ciclo de vida del usuario |
|  |  | fecha de la primera compra - fecha de la primera sesión |
|  |  | hoy - fecha de la última compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 Estas comparaciones se restablecerán cuando cambie de espacio de trabajo.



## Página de detalles del segmento

También se ha incorporado información sobre los segmentos en la vista **Detalles del segmento**. Al examinar un segmento concreto que haya configurado previamente, encontrará las mismas seis estadísticas esbozadas en el cuadro dinámico gris Estadísticas del segmento. Desde aquí, puede iniciar rápidamente la herramienta Segment Insights para comparar este segmento en particular con cualquier otro que haya configurado previamente, pero tenga en cuenta que esto sobrescribirá cualquier segmento que haya seleccionado previamente dentro de la herramienta Segment Insights.



## Ejemplos {#insights-use-cases}

### Comparación de patrones demográficos de uso y compra

Uno de los mejores usos de Segment Insights es responder a preguntas sobre el impacto de los datos demográficos de los usuarios en el uso de las aplicaciones y la eficacia de las campañas, como por ejemplo:

- ¿Hay determinados grupos demográficos de usuarios que obtienen resultados significativamente mejores o peores que la media?
- ¿Debo replantearme la localización de una campaña concreta?
- ¿Se dirige una campaña a un determinado grupo demográfico?
- ¿Qué objetivos debo fijar para una campaña dirigida a un determinado grupo demográfico?

Segment Insights puede ayudar a descubrir diferencias entre los datos demográficos de los usuarios. El siguiente ejemplo muestra una comparación de la base de usuarios de una aplicación por su idioma, ilustrando cómo los angloparlantes tienden a tener mayores niveles de LTV y actividad que los hablantes de otros idiomas.



En este ejemplo, los germanoparlantes se inscribieron hace más tiempo por término medio, lo que podría explicar por qué ya no son tan activos. Esto puede deberse a multitud de factores. Por ejemplo, si la aplicación se lanzó primero en Europa, pero ahora es más popular en Estados Unidos, donde la mayoría de la gente habla inglés o español. Para obtener resultados más sólidos, cuando se analizan los indicadores clave de rendimiento en función de la demografía, es sensato comprobar los resultados de un estudio demográfico general (por ejemplo, si el idioma influye en la LTV de todos los usuarios) analizando una población más pequeña y similar y viendo si los resultados persisten.



### Comprender los indicadores de mayores ingresos

Conseguir que los usuarios se conviertan en compradores puede ser difícil, y tratar de empujar a los usuarios nuevos, inactivos o desconectados directamente hacia la compra puede llevar al usuario a desinstalar su aplicación.  Por ejemplo, puedes trazar el impacto en las compras de diferentes comportamientos dentro de una aplicación de comercio electrónico.



  

