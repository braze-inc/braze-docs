---
nav_title: Sisu Data
article_title: Sisu Data
description: "Este artículo de referencia describe la asociación entre Braze y Sisu Data, líder en inteligencia de decisiones en la nube, que permite comprender en todas las campañas o a nivel de campaña por qué están cambiando las métricas y qué impulsa los resultados más óptimos."
alias: /partners/sisu_data
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data](https://sisudata.com/) es el líder en inteligencia de decisiones en la nube que utiliza el aprendizaje automático para descomponer automáticamente el rendimiento de las métricas y ofrecer información rápida, completa y práctica.

La integración de Sisu Data y Braze le permite comprender en todas las campañas o a nivel de campaña por qué están cambiando las métricas (por ejemplo, la tasa de apertura, la tasa de clics, la tasa de conversión, etc.) y qué impulsa los resultados más óptimos. Una vez identificados estos segmentos, los usuarios de Braze pueden materializar los resultados en su almacén de datos o enviarlos directamente de Sisu a Braze para volver a dirigirse a los usuarios y captarlos.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Sisu | Se necesita una cuenta [Sisu](https://sisudata.com/) para beneficiarse de esta asociación. |
| Almacén en nube | Esta integración asume que sus datos Braze se almacenan en un almacén en la nube (por ejemplo, Snowflake, BigQuery). Para agilizar este proceso de integración, recomendamos utilizar la funcionalidad nativa de Braze a través de [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Preparar un conjunto de datos

El conjunto de datos debe indicar el KPI que desea que Sisu analice. Por ejemplo, si desea comprender mejor por qué las tasas de conversión disminuyeron de una semana a otra, el registro de alcance debe representar una conversión semanal. Las columnas del conjunto de datos deben ser posibles razones por las que la tasa de conversión podría bajar.

### Paso 2: Crear una métrica  

Una vez preparado el conjunto de datos, deberá crear una métrica que haga referencia a una columna agregada. Dado que un conjunto de datos puede alimentar varias métricas, el usuario también puede seleccionar un conjunto de dimensiones que deberían o no formar parte de todos los análisis por defecto. Tenga en cuenta que los usuarios siempre pueden seguir curando a nivel de análisis.

![]({% image_buster /assets/img/sisudata/metric_creation.png %})

### Paso 3: Crear un análisis  

Existen diferentes análisis que los usuarios pueden crear en Sisu en función del caso de uso. Uno de los análisis más habituales es el de periodo sobre periodo para comprender qué segmentos han cambiado más. Los usuarios pueden decidir si desean analizar periodos de tiempo diarios, semanales, mensuales o personalizados seleccionando los periodos de tiempo relativos.

Por ejemplo, el usuario puede crear un análisis de la tasa de conversión mes a mes para un grupo de anuncios y un canal de captación concretos, y comprender los principales factores positivos y negativos.

{% tabs %}
{% tab Principales factores positivos %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Principales factores negativos %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

A partir de aquí, puede centrarse en las cohortes en las que deseen participar o modificar las campañas. Por ejemplo, Sisu ha identificado automáticamente que las notificaciones push enviadas los martes y los correos electrónicos enviados en grandes volúmenes afectan gravemente a la tasa de conversión.

![]({% image_buster /assets/img/sisudata/segment.png %})

### Paso 4: Vuelve a escribir los resultados en el almacén de datos

Los usuarios pueden extraer los resultados de Sisu utilizando [la API de Sisu](https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults) y materializar los segmentos en un almacén de datos. Los clientes de Snowflake pueden activar estos segmentos en Braze a través de [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/).

Para otros almacenes de datos, los usuarios pueden aprovechar una solución de activación existente o ponerse en contacto con Sisu para obtener ayuda adicional.

## Soporte

Si tiene preguntas sobre esta integración, póngase en contacto con Sisu en partners@sisudata.com.

