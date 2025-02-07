---
nav_title: Dashboard de uso de API
article_title: Dashboard de uso de API
alias: "/api_usage/"
page_order: 3.5
description: "Este artículo ofrece un resumen del panel de uso de la API."
---

# Panel de uso de la API

> El panel de uso de la API te permite controlar el tráfico entrante de la API REST en Braze para comprender las tendencias de uso de nuestras API REST y solucionar posibles problemas.

Para ver tu panel de uso de la API, ve a **Configuración** > **API e identificadores** y selecciona **Panel**. El panel predeterminado es una vista de todas las solicitudes de API REST entrantes para tu espacio de trabajo durante el último día (24 horas). Según tu caso de uso, puedes ajustar los controles del panel para filtrar o agrupar el tráfico y también configurar el intervalo de tiempo del panel.

![Panel de uso de la API con 130 peticiones totales, con una tasa de éxito del 70 por ciento y una tasa de fracaso del 30 por ciento.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Detalles del resumen

El panel de uso de la API incluye las siguientes estadísticas:

- **Total de solicitudes:** El número total de solicitudes enviadas a Braze para tu espacio de trabajo actual, dados los filtros y controles aplicados al panel.
- **Tasa de éxito:** Porcentaje del total de solicitudes en las que Braze emitió una respuesta satisfactoria `2XX`.
- **Tasa de error:** Porcentaje del total de solicitudes en las que Braze emitió una respuesta de error `4XX` o `5XX`.

## Controles del panel de instrumentos

![Filtros para aplicar al panel, incluyendo: Clave de API, punto final, códigos de respuesta, datos del grupo y fecha.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros

Selecciona **Filtros** para aplicar filtros que reduzcan la vista del tráfico de la API REST de tu espacio de trabajo, incluidos:

- Clave de API
- Punto de conexión
- Código de respuesta

### Agrupar datos

Puedes agrupar los datos en varias series de datos para explorar diferentes patrones en su uso, incluyendo:

- Códigos de respuesta (predeterminados)
- Punto de conexión de API
- Clave de API
- Solo éxito y fallo

### Fecha

Ajusta el filtro de fecha para mostrar un intervalo de tiempo mayor o menor según necesites. Esto incluye lo siguiente:

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
Las opciones **Últimas 3 horas** y **Últimas 6 horas** mostrarán el tráfico por minutos. Los periodos de tiempo más largos mostrarán el tráfico cada cinco minutos, hora o día.
{% endalert %}

## Consideraciones

El panel de uso de la API incluye todas las solicitudes de la API REST para las que Braze recibió y devolvió una respuesta `2XX`, `4XX` o `5XX`. Esto incluye las salidas de la Transformación de datos y las sincronizaciones de la Ingesta de datos en la nube. El tráfico SDK y los pasos de Actualización de Usuario no están incluidos en este panel.

Los datos mostrados en el panel pueden tener hasta un breve retraso en mostrar el tráfico reciente. Durante los períodos de uso elevado, puedes actualizar el panel hasta 4 veces por minuto. Puede que tengas que esperar unos minutos antes de volver a actualizar el panel.
