---
nav_title: Dashboard de uso de API
article_title: Dashboard de uso de API
permalink: "/api_usage/"
hidden: true
description: "Este artículo ofrece un resumen del panel de uso de la API."
---

# Panel de uso de la API

> El panel de uso de la API te permite controlar el tráfico entrante de la API REST en Braze para comprender las tendencias de uso de nuestras API REST y solucionar posibles problemas.

El panel predeterminado es una vista de todas las solicitudes de API REST entrantes para tu espacio de trabajo durante el último día (24 horas). Según tu caso de uso, puedes ajustar los controles del panel para filtrar o agrupar el tráfico y también configurar el intervalo de tiempo del panel.

![]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Resumen estadístico

- **Total de solicitudes:** El número total de solicitudes enviadas a Braze para tu espacio de trabajo actual, dados los filtros y controles aplicados al panel.
- **Tasa de éxito:** Porcentaje del total de solicitudes en las que Braze emitió una respuesta satisfactoria `2XX`.
- **Tasa de error:** Porcentaje del total de solicitudes en las que Braze emitió una respuesta de error `4XX` o `5XX`.

## Controles del panel de instrumentos

![]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros

Aplica filtros para limitar la vista del tráfico de la API REST de tu espacio de trabajo. Los filtros disponibles son:

- Punto de conexión de API
- Clave de API
- Código de respuesta

### Agrupar datos

Agrupa los datos en varias series de datos para explorar distintos patrones en su uso. Las opciones de agrupación disponibles son:

- Códigos de respuesta (predeterminados)
- Punto de conexión de API
- Clave de API
- Solo éxito y fallo

### Fecha

Ajusta el filtro de fecha para mostrar un intervalo de tiempo mayor o menor según necesites. Las opciones de fecha disponibles son:

- Hoy (predeterminado)
- Personalizado
- Últimas 3 horas
- Últimas 6 horas
- Últimas 12 horas
- Últimas 24 horas
- Ayer
- 7 últimos días
- Últimos 14 días
- 30 últimos días
- Último mes hasta la fecha

{% alert note %}
Las opciones **Últimas 3 horas** y **Últimas 6 horas** mostrarán el tráfico por minutos. Los periodos de tiempo más largos mostrarán el tráfico por horas o días.
{% endalert %}

## Consideraciones

El panel de uso de la API incluye todas las solicitudes de la API REST para las que Braze recibió y devolvió una respuesta `2XX`, `4XX` o `5XX`. Esto incluye las salidas de la Transformación de datos y las sincronizaciones de la Ingesta de datos en la nube. El tráfico SDK y los pasos de Actualización de Usuario no están incluidos en este panel.

Los datos mostrados en el panel pueden tener un retraso de hasta 15 minutos en mostrar el tráfico reciente. Durante los períodos de uso elevado, puedes actualizar el panel hasta 4 veces por minuto. Puede que tengas que esperar unos minutos antes de volver a actualizar el panel.
