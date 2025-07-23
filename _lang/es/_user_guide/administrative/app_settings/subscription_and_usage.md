---
nav_title: Facturación
article_title: Facturación
alias: /subscription_and_usage/
page_order: 25
page_type: reference
description: "Este artículo de referencia cubre la página de Facturación, donde puedes monitorizar y comprobar tu consumo de datos."
tool: Dashboard
search_rank: 5
---

# Facturación

> Aprende a utilizar la página de **Facturación** para supervisar y comprobar tu consumo de datos en todos los espacios de trabajo, aplicaciones y fuentes de eventos. Este artículo cubre las diferentes secciones de la página y la información que pueden proporcionarte.

Para navegar a la página de **Facturación**, vaya a **Configuración** > **Facturación**.

La página **Facturación** incluye las siguientes pestañas:

- [Suscripciones y uso](#subscriptions-and-usage)
- [Eventos y atributos más utilizados por aplicación](#most-used-events-and-attributes-by-app)
- [Total de uso de puntos de datos](#total-data-points-dashboard)

## Suscripciones y uso

La pestaña **Suscripciones y uso** incluye gráficos de uso y los detalles de tu contrato.

### Gráficos de uso

Aquí encontrarás gráficos de uso que se aplican a tus espacios de trabajo. Puede que su propio panel muestre diferentes métricas de uso en función de los productos que haya adquirido. 

![Gráfico de uso que muestra los visitantes únicos mensuales][3]{: style="max-width:90%;"}

Estos gráficos pueden mostrar los usuarios activos mensuales, los visitantes únicos mensuales y los envíos de correo electrónico. Este tipo de gráficos son especialmente útiles para presupuestar el uso y comprender mejor qué espacios de trabajo contribuyen al uso general.

### Detalles del contrato

Los detalles del contrato indican la fecha de inicio y fin de su contrato actual con Braze.

## Eventos y atributos más utilizados por aplicación

En **Eventos y atributos más utilizados por aplicación**, puedes comprobar los impulsores de tu consumo de puntos de datos de atributos y eventos personalizados. 

![Eventos y atributos más utilizados por aplicación][4]

Para cada aplicación, puedes seleccionar **Ver desglose** para ver un recuento estimado de cada atributo personalizado específico, atributo de perfil y evento personalizado para el periodo de tiempo seleccionado, así como el porcentaje de las actualizaciones de atributos y eventos de esa aplicación que fueron impulsadas por ese atributo o evento. 

![Pestaña Desglose de eventos y atributos más utilizados por aplicación][1]

Los desgloses de datos de este tipo pueden ayudarle a comprender qué puntos de datos específicos están ocupando grandes porcentajes de su asignación. Le recomendamos que controle esta información de vez en cuando para asegurarse de que no está gastando puntos de datos de forma accidental e innecesaria. Su gestor de éxito de clientes puede orientarle para sacar el máximo partido a su plan actual o proporcionarle opciones para una mayor flexibilidad. 

## Panel de puntos de datos totales

La pestaña **Uso total de puntos de datos** ofrece una visión detallada de su consumo de puntos de datos. Puede ver todos los datos de esta sección agregados por semanas o meses.

![Filtrar el uso de puntos de datos por semanas][2]

### Detalles del contrato

Aquí encontrarás información sobre cuándo empieza y termina tu contrato Braze actual, así como los puntos de datos asignados y una suma de todos los puntos de datos que se han utilizado hasta ahora en tu contrato actual.

Los campos de esta sección se definen del siguiente modo:

- **Tipo de contrato:** Estructura de plazos de facturación, anual o plurianual.
- **Fecha de inicio y fin del contrato:** Fecha de inicio y fin de todo el contrato.
- **Puntos de datos asignados:** La cantidad de puntos de datos asignados en el contrato por periodo de facturación.
- **Uso de punto de datos del contrato:** Es el total acumulado de todos los puntos de datos consumidos durante la vigencia del contrato, y no se reinicia en el siguiente periodo de facturación.

![Sección Detalles del contrato de la pestaña Utilización total de puntos de datos][5]

### Datos de facturación de la empresa

#### Uso total de punto de datos a nivel de aplicación

Este gráfico muestra el uso de punto de datos en todas las aplicaciones.

![El uso total de puntos de datos a nivel de aplicación muestra los puntos de datos utilizados por cada aplicación.][14]

Selecciona uno de los totales para ver la tabla **Uso de punto de datos en el tiempo**, que muestra tus totales semanales de puntos de datos para cada espacio de trabajo.  Las filas que tienen la columna **Nombre de la aplicación** en blanco representan puntos de datos que no están asociados a ninguna aplicación (como puntos de datos utilizados en solicitudes que no especifican una `app_id`).

![Uso de puntos de datos a lo largo del tiempo mostrando el total de puntos de datos semanales de dos espacios de trabajo.][15]

#### Uso de punto de datos en el espacio de trabajo

Este gráfico permite evaluar el uso total de puntos de datos de una empresa por espacio de trabajo. Este gráfico le permite evaluar cómo contribuye cada espacio de trabajo al uso de puntos de datos de la empresa.

![Gráfico de utilización de puntos de datos de dos espacios de trabajo][7]{: style="max-width:90%;"}

#### Uso de punto de datos del ciclo de facturación por origen de evento

Este gráfico te permite ver cómo se reparte el uso de punto de datos entre diferentes orígenes de eventos, como diferentes atributos de API, eventos personalizados y sesiones.

![Uso de punto de datos del ciclo de facturación por origen de sucesos que muestra la asignación de punto de datos entre diferentes orígenes de sucesos.][13]

#### Utilización de puntos de datos a lo largo del tiempo

Este gráfico le permite ver rápidamente el uso total de puntos de datos en comparación con la cantidad de puntos de datos asignados.

![Uso de puntos de datos a lo largo del tiempo contrastando los puntos de datos asignados al ciclo de facturación actual con el total en curso.][8]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img/most_used_events_attributes_2.png %}
[2]: {% image_buster /assets/img/subscription_and_billing2.png %}
[3]: {% image_buster /assets/img/subscription_and_billing4.png %}
[4]: {% image_buster /assets/img/most_used_events_attributes_time.png %}
[5]: {% image_buster /assets/img/contract_details.png %}
[6]: {% image_buster /assets/img/current_billing_cycle.png %}
[7]: {% image_buster /assets/img/appgroup_datapoint_usage.png %}
[8]: {% image_buster /assets/img/company_data_point_usage_time.png %}
[9]: {% image_buster /assets/img/appgroup_drilldown.png %}
[10]: {% image_buster /assets/img/appgroup_level_datapoint_usage_bycategory.png %}
[11]: {% image_buster /assets/img/appgroup_level_usage_time.png %}
[12]: {% image_buster /assets/img/app_level_stats.png %}
[13]: {% image_buster /assets/img/event_source_stats.png %}
[14]: {% image_buster /assets/img/app_level_total.png %}
[15]: {% image_buster /assets/img/data_point_usage_time.png %}