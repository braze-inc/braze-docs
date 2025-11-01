---
nav_title: Panel de uso de la API
article_title: Panel de uso de la API
alias: "/api_usage/"
page_order: 3.5
description: "Este artículo ofrece un resumen del panel de uso de la API."
---

# Panel de uso de la API

> El panel de uso de la API te permite controlar el tráfico entrante de la API REST en Braze para comprender las tendencias de uso de nuestras API REST y solucionar posibles problemas.

## Acerca del panel de uso de la API

Para ver tu panel de uso de la API, ve a **Configuración** > **API e identificadores** y, a continuación, selecciona **Panel**.

El panel predeterminado es una vista de todas las solicitudes de API REST entrantes para tu espacio de trabajo durante el último día (24 horas). Según tu caso de uso, puedes ajustar los controles del panel para filtrar o agrupar el tráfico y también configurar el intervalo de tiempo del panel.

\![Panel de uso de la API con 130 solicitudes totales, con una tasa de éxito del 70 por ciento y una tasa de fracaso del 30 por ciento.]({% image_buster /assets/img/api_usage_dashboard/api_usage_dashboard.png %})

## Métricas disponibles

El panel de uso de la API incluye las siguientes estadísticas:

| Métrica         | Descripción |
|----------------|-------------|
| Total solicitudes | El número total de solicitudes enviadas a Braze para tu espacio de trabajo actual, dados los filtros y controles aplicados al panel. |
| Tasa de éxito   | Porcentaje del total de solicitudes en las que Braze emitió una respuesta satisfactoria `2XX`. |
| Tasa de error     | Porcentaje del total de solicitudes en las que Braze emitió una respuesta de error `4XX` o `5XX`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Utilizar el panel de control

\![Filtros para aplicar al panel, incluyendo: Clave de API, punto final, códigos de respuesta, datos de grupo y fecha.]({% image_buster /assets/img/api_usage_dashboard/filters.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

### Filtros

Selecciona **Filtros** para aplicar filtros que reduzcan la vista del tráfico de la API REST de tu espacio de trabajo, incluidos:

- Clave de API
- Punto final
- Código de respuesta

### Datos del grupo

Puedes agrupar los datos en varias series de datos para explorar diferentes patrones en su uso, incluyendo:

- Códigos de respuesta (predeterminados)
- Punto final de la API
- Clave de API
- Sólo éxito y fracaso

### Fecha

Ajusta el filtro de fecha para mostrar un intervalo de tiempo mayor o menor según necesites. Esto incluye

- Hoy (predeterminado)
- Personalizados
- Últimas 3 horas
- Últimas 6 horas
- Últimas 12 horas
- Últimas 24 horas
- Ayer
- Últimos 7 días
- Últimos 14 días
- Últimos 30 días
- Último mes hasta la fecha

{% alert note %}
Las opciones **Últimas 3 horas** y **Últimas 6 horas** mostrarán el tráfico por minutos. Los periodos de tiempo más largos mostrarán el tráfico cada cinco minutos, hora o día.
{% endalert %}

## Consideraciones

El panel de uso de la API incluye todas las solicitudes de la API REST para las que Braze recibió y devolvió una respuesta `2XX`, `4XX` o `5XX`. Esto incluye las salidas de la Transformación de Datos y las sincronizaciones de la Ingesta de Datos en la Nube. El tráfico SDK y los pasos de Actualización de Usuario no están incluidos en este panel.

Los datos mostrados en el panel pueden tener hasta un breve retraso en mostrar el tráfico reciente. Durante los periodos de uso elevado, puedes actualizar el panel hasta 4 veces por minuto. Puede que tengas que esperar unos minutos antes de volver a actualizar el panel.
