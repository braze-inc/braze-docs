---
nav_title: "Segmentos RFM"
article_title: Segmentos RFM SQL
page_order: 1
page_type: reference
alias: "/rfm_segments/"
description: "Este artículo describe cómo crear extensiones de segmento RFM, que identifican a tus mejores usuarios midiendo sus hábitos de compra."
tool: Segments
---

# Segmentos RFM SQL

> Puedes crear una Extensión de segmento RFM (recencia, frecuencia, monetario) para dirigirte a tus mejores usuarios midiendo sus hábitos de compra.

El análisis RFM es una técnica de marketing que identifica a tus mejores usuarios puntuándolos en una escala de 0 a 3 para cada categoría (recurrencia, frecuencia, monetaria), donde 3 es la mejor puntuación y 0 la peor. La recurrencia, la frecuencia y los valores monetarios se basan en los datos de un intervalo de tiempo específico que tú elijas.

## Categorías RFM

| Categoría | Definición |
| --- | --- |
| Recencia | Cómo de reciente ha sido la compra de un cliente. Una puntuación más alta significa compras más recientes. |
| Frecuencia | Frecuencia con la que un cliente realiza una compra. Una puntuación más alta significa mayor frecuencia. |
| Valor monetario | Cantidad total de dinero que gastó un cliente. Una puntuación más alta significa un gasto mayor. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Los eventos de compra deben habilitarse para utilizar segmentos SQL de RFM, porque el valor monetario de tus usuarios viene determinado por los ingresos que han generado a través de los eventos de compra de Braze.
{% endalert %}

## Crear un segmento RFM

1. Vaya a **Audiencia** > **Extensiones de segmento**.
2. Selecciona **Nueva extensión** y, a continuación, **Segmento de frecuencia, frecuencia y valor monetario (RFM)**.

![Modal con la opción de crear un segmento de catálogo para eventos, compras o segmentos RFM.]({% image_buster /assets/img/segment/select_rfm_segment.png %}){: style="max-width:80%" }

{: start="3"}
3\. En el panel **Variables**, selecciona tu **Rango temporal** para especificar el periodo de tiempo de los datos de compra a analizar. Puedes especificar hasta los últimos 60 días. El intervalo de tiempo que selecciones es el intervalo de tiempo del que se extraen los datos de comportamiento del usuario y depende de los objetivos de tu campaña.

| Campo de intervalo de tiempo | Descripción | Casos de uso |
| --- | --- | --- |
| Relativo | Especifica la actividad en los últimos X días | Analiza el comportamiento más reciente de los usuarios con una ventana móvil. | 
| Fecha de inicio | Especifica un punto de partida fijo para tu análisis | Analiza la actividad de los usuarios a partir de una fecha concreta, como después del lanzamiento de una campaña. |
| Fecha de finalización | Especifica un punto final fijo para tu análisis | Analiza la actividad de los usuarios hasta una fecha concreta, por ejemplo, antes de una actualización del producto. |
| Intervalo de fechas | Especifica una fecha de inicio y otra de fin para un periodo personalizado | Analiza el comportamiento de los usuarios durante un periodo definido, como un evento promocional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{: start="4"}
4\. Selecciona los [grupos de RFM](#rfm-groups) generados para incluirlos en tu segmento. Si seleccionas varios grupos, tu segmento incluirá a los usuarios que formen parte de cualquiera de los grupos seleccionados.

![Panel de variables con los grupos de RFM "Campeones" y "Usuarios fieles" seleccionados.]({% image_buster /assets/img/segment/rfm_groups.png %})

{: start="5"}
5\. Ejecuta una vista previa y luego guarda tu segmento

{% alert note %}
No necesitas editar el código SQL de la plantilla para crear un segmento RFM. Puedes utilizar exclusivamente el panel **Variables** para personalizar tu segmento.
{% endalert %}

### Grupos RFM

Los segmentos RFM se evalúan en un orden específico. Se asigna a los usuarios al primer segmento cuyos criterios cumplan, desde la parte superior de la lista de priorización hacia abajo. Por ejemplo, un usuario que cumple los requisitos tanto para "Campeones" como para "Usuarios fieles" se asigna al segmento "Campeones" porque tiene mayor prioridad.

| Grupo RFM          | Descripción del segmento                                                                 | Rango de recurrencia (R) | Rango de frecuencia (F) | Rango monetario (M) |
|--------------------|-------------------------------------------------------------------------------------|------------------|--------------------|-------------------|
| Campeones          | El segmento de usuarios más valioso, con las mejores puntuaciones en todas las categorías.                   | 3                | 2-3                | 2-3               |
| Usuarios fieles        | Usuarios con alta recurrencia y alta frecuencia. Puede tener un valor monetario inferior al de los Campeones. | 2-3              | 2-3                | 1-3               |
| Leales potenciales| Usuarios que compraron recientemente con una frecuencia moderada y un valor monetario moderado.   | 3                | 1-3                | 1-3               |
| Prometedor          | Usuarios que hicieron una compra inicial reciente de gran valor, pero que aún no han establecido una frecuencia de compra elevada. | 3                | 0-3                | 1-3               |
| Cliente nuevo       | Usuarios que hicieron su primera compra muy recientemente.                             | 3                | 0-3                | 0-3               |
| Necesidad de atención  | Usuarios con una recurrencia superior a la media, pero su frecuencia de compra o su valor monetario están por debajo de la media. | 2-3              | 0-3                | 0-3               |
| No puedes perderlos   | Usuarios que antes eran de alto valor, con buenas puntuaciones de frecuencia y monetarias, pero que llevan mucho tiempo sin comprar. | 0-1              | 2-3                | 2-3               |
| En peligro            | Usuarios que históricamente han tenido puntuaciones monetarias y de frecuencia moderadas, pero que no han comprado en mucho tiempo. | 0-1              | 1-3                | 1-3               |
| A punto de dormir     | Usuarios que tienen puntuaciones bajas en todas las métricas.                                       | 1                | 0-3                | 0-3               |
| Hibernando        | Usuarios que tienen una frecuencia moderada, pero que han estado inactivos durante un periodo prolongado.    | 0                | 0-2                | 0-3               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
