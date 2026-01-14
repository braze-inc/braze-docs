---
nav_title: Análisis
article_title: "Análisis de recomendación de artículos"
description: "Infórmate sobre los análisis de recomendación de artículos y cómo verlos en Braze."
page_order: 1.3
---

# Análisis de recomendación de artículos

> Infórmate sobre los análisis de recomendación de artículos y cómo verlos en Braze.

## Ver análisis

Puedes consultar los análisis de tu recomendación para ver qué artículos se recomendaron a los usuarios y la precisión del modelo de recomendación.

1. Ve a **Análisis** > **Recomendación de artículos**.
2. Selecciona tu recomendación de la lista.

## Métricas disponibles

### Audiencia

Son métricas relacionadas con tu audiencia de recomendación, que incluyen precisión, cobertura y tipo de recomendación.

Las métricas de audiencia de las recomendaciones muestran precisión (25,3%), cobertura (54,3%) y tipos de recomendación divididos entre artículos personalizados y más populares.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Consulta la tabla siguiente para obtener más información:

| Métrica              | Descripción |
| ------------------- | ---------- |
| **Precisión**           | El porcentaje de veces que el modelo adivinó correctamente el siguiente artículo que compró un usuario. La precisión depende en gran medida del tamaño y la mezcla específicos de tu catálogo, y debe utilizarse como guía para comprender con qué frecuencia el modelo es correcto.<br><br>En pruebas anteriores, hemos visto que los modelos rinden bien con cifras de precisión que oscilan entre el 6 y el 20%. Esta métrica se actualiza cuando el modelo vuelve a entrenarse.  |
| **Cobertura**            | Qué porcentaje de artículos disponibles en el catálogo se recomiendan al menos a un usuario. Puedes esperar ver una mayor cobertura de artículos con recomendaciones de artículos personalizados sobre los más populares. |
| **Tipo de recomendación** | El porcentaje de usuarios que recibirán recomendaciones personalizadas o más recientes frente a la alternativa de los artículos más populares. La alternativa se envía a los usuarios que no tienen datos suficientes para generar una recomendación personalizada o más reciente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Artículos

Esta tabla incluye métricas sobre los artículos personalizados, más recientes y más populares de tu catálogo.

\![Tablas contiguas que enumeran los elementos asignados a los usuarios, separados por recomendaciones personalizadas y recomendaciones más populares.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Consulta la tabla siguiente para obtener más información:

| Métrica              | Descripción |
| ------------------- | ---------- |
| **Artículos personalizados**<br><br>**Artículos más recientes** | Esta columna enumera cada artículo del catálogo en orden descendente de los más recomendados a los usuarios. Esta columna también muestra a cuántos usuarios asignó el modelo cada elemento.<br><br>Según el [tipo de recomendación]({{site.baseurl}}/user_guide/brazeai/recommendations/), se mostrarán los artículos **personalizados** o los **más recientes**. |
| **Artículos más populares** | Esta columna enumera cada artículo del catálogo en orden descendente de popularidad. La popularidad aquí se refiere a los elementos del catálogo con los que los usuarios interactúan más a menudo en todo el espacio de trabajo. El más popular se utiliza como alternativa cuando no se puede calcular el personalizado o el más reciente para un usuario individual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resumen

Se trata de un resumen de la configuración de recomendación elegida, que incluye cuándo se actualizó la recomendación por última vez.

\![Tabla resumen de recomendaciones que muestra el tipo, el catálogo, el tipo de evento, el nombre del evento personalizado, el nombre de la propiedad y la última fecha de actualización.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }
