---
nav_title: Eppo
article_title: Eppo
description: "Aprende a integrar Eppo con Braze."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) es una plataforma de experimentación de nueva generación que habilita a los equipos para realizar pruebas A/B, gestionar características a escala y aprovechar la información basada en IA para tomar decisiones basadas en datos.

*Esta integración está mantenida por Eppo.*

La integración de Braze y Eppo te permite configurar pruebas A/B en Braze y analizar los resultados en Eppo para descubrir información y vincular el rendimiento de los mensajes a métricas empresariales a largo plazo, como los ingresos o la retención.

## Requisitos previos

| Requisito                        | Descripción                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Cuenta Eppo                       | Se necesita una cuenta de Eppo para beneficiarse de esta asociación.                   |
| Compartir datos Currents o Snowflake | Para que Eppo analice los datos de los experimentos, es necesario compartir datos de Currents o Snowflake. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Configurar el uso compartido de datos Currents o Snowflake en Braze

Eppo analiza los experimentos directamente en tu almacén de datos. Para habilitar la integración, los datos de habilitación de mensajes de Braze deben estar disponibles en el almacén conectado a Eppo. Puedes exportar datos de campaña desde Braze utilizando Currents, o acceder a los datos de Braze en tu instancia de Snowflake utilizando [Compartir datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake).

### Paso 2: Configura tu experimento en una campaña Braze o Canvas

Puedes utilizar características nativas de pruebas A/B en tus campañas y Canvases. Para saber más, consulta [Multivariante y pruebas A/B](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Paso 3: Configurar Eppo para medir experimentos de Braze

Para realizar experimentos utilizando datos de Braze en Eppo, crea [tablas de asignaciones](https://docs.geteppo.com/data-management/definitions/assignment-sql/) en tu almacén basadas en los datos de eventos de mensajes a nivel de usuario exportados desde Braze. Se recomiendan tablas separadas para los experimentos en Canvas y en campañas, porque se basan en metadatos diferentes.

{% tabs local %}
{% tab experimentos en Canvas %}
Para los experimentos en Canvas, las asignaciones pueden crearse de dos formas:

- En el nivel de entrada Canvas (`users.canvas.Entry`)
- O en un paso de Experimento en Canvas (`users.canvas.experimentstep.SplitEntry`)

En estos casos, se utilizan campos como `canvas_name`, `experiment_step_id`, `canvas_variation_name`, y `experiment_split_id` para definir el nombre y la variación del experimento.

{% endtab %}

{% tab experimentos de campaña %}
Para los experimentos de campaña, utiliza eventos de envío (como push, correo electrónico, SMS) para determinar cuándo ha entrado un usuario en el experimento. `campaign_name` Para rellenar la tabla de asignaciones, se utilizan las direcciones `message_variation_name` y `time`.

{% endtab %}
{% endtabs %}

Para hacer un seguimiento de las métricas específicas de los mensajes (como clics o aperturas), incluye una **Entidad secundaria** creando un `combined_id` que una el ID de usuario con el nombre de la campaña o Canvas. Este `combined_id` también se utiliza en tus tablas de hechos para alinear las métricas con el experimento y la variación correctos.

Eppo utiliza estas asignaciones y tablas de hechos para analizar los resultados, y se recomienda establecer un **Protocolo** en Eppo para estandarizar la configuración de futuros experimentos. Para más información, consulta [la documentación de Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Soporte

Si tienes preguntas sobre cómo configurar Braze Currents, compartir datos de Snowflake o configurar campañas multivariantes, ponte en contacto con tu administrador del éxito del cliente de Braze.

Si necesitas ayuda para configurar Eppo para medir experimentos Braze, ponte en contacto con el equipo de soporte de Eppo.
