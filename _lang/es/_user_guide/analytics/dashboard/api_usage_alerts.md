---
nav_title: Alertas de uso de la API
article_title: Alertas de uso de la API
description: "Este artículo ofrece un resumen de las alertas de uso de la API, que te permiten detectar de forma proactiva el tráfico inesperado."
page_order: 3.6
---

# Alertas de uso de la API

> Las alertas de uso de la API proporcionan una visibilidad crítica del uso de tu API, permitiéndote detectar proactivamente el tráfico inesperado. Al configurar estas alertas para hacer un seguimiento de los volúmenes de solicitudes de API clave, puedes recibir notificaciones en tiempo real y abordar los problemas antes de que afecten a tus campañas de marketing.

## Acerca de las alertas de uso de la API

Puedes utilizar las alertas de uso de la API para controlar los volúmenes de solicitudes de las siguientes categorías:

| Categoría API | Detalles |
|--------------|---------|
| Puntos finales de la API REST | Realiza un seguimiento del uso de todas las llamadas a la API REST realizadas al backend de Braze, como el envío de mensajes, la creación de campañas o la exportación de usuarios. |
| Solicitudes de la API del SDK | Realiza un seguimiento de las solicitudes de API realizadas desde los SDK de Braze en las aplicaciones cliente, como desencadenar mensajes dentro de la aplicación o sincronizar datos de usuario.<br><br>_\*Sólo disponible para clientes que hayan comprado Usuarios activos al mes - CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Crear una alerta de uso de la API

Para crear una alerta de uso de la API:

1. Ve a **Configuración** > **APIs e identificadores** > **Alertas de uso de la API**, y crea una nueva alerta.
2. Introduce un nombre para tu alerta y elige los puntos finales de la API REST y las claves de API de las que te gustaría recibir una alerta.
3. Define tus criterios de alerta eligiendo uno o varios códigos de respuesta y especificando los [umbrales de alerta](#api-usage-alert-thresholds).
4. Cuando hayas terminado, alterna **Alerta habilitada**.
    \![Un ejemplo de alerta de uso de la API que envía notificaciones cuando el punto final Seguimiento de usuarios aumenta un 100 por cien en el plazo de una hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Umbrales de alerta {#api-usage-alert-thresholds}

Cuando definas tus criterios de alerta, puedes ajustar los siguientes umbrales:

<table>
  <thead>
    <tr>
      <th>Campo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condición de umbral</td>
      <td>
        Define las condiciones que conducen al volumen umbral sobre el que te gustaría recibir una alerta. Se admiten los siguientes:<br><br>
        <ul>
          <li><strong>Aumentado en</strong> o <strong>Disminuido en</strong>: Compara las solicitudes con la ventana de tiempo anterior.</li>
          <li><strong>Aumentado en porcentaje</strong> o <strong>Disminuido en porcentaje</strong>: Compara el cambio porcentual de las solicitudes respecto a la ventana de tiempo anterior.</li>
          <li><strong>Mayor o igual</strong>, o <strong>menor o igual</strong>: Cuenta las solicitudes en una ventana de tiempo.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volumen umbral</td>
      <td>Se utiliza junto con la condición de umbral.</td>
    </tr>
    <tr>
      <td>En</td>
      <td>La ventana de tiempo para la evaluación de la alerta.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuración de las notificaciones de alerta

Puedes configurar una alerta por correo electrónico, una alerta webhook o ambas. Las alertas webhook pueden ser muy útiles para casos de uso como enviar una alerta a plataformas externas, como un canal de Slack. Para ver un ejemplo, consulta nuestra [documentación](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sobre la integración de alertas con Slack para conocer nuestras preferencias de notificación.

Se enviará un correo electrónico al correo electrónico seleccionado cuando se alcancen los criterios de la alerta.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Muestra de carga útil {#payload}

A continuación se muestra un ejemplo de carga útil para el cuerpo de un webhook de Alerta de uso de la API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Ejemplo de alertas

Aquí tienes algunas formas de establecer las configuraciones de tus alertas de uso de la API para recibir notificaciones en los siguientes escenarios.

{% tabs local %}
{% tab api health %}
Puedes configurar alertas para controlar el estado general de tu API. Por ejemplo, puedes configurar estas alertas cuando los errores de la API aumenten drásticamente, como un 20% respecto a la hora anterior.

| Punto final | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos finales | Todas las claves de API | `4XX` y `5XX` | Aumento del 10%. | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Recibe una alerta cuando tu espacio de trabajo alcance su límite de velocidad para el punto final `/users/track`. También puedes aplicar esta configuración a otros puntos finales Braze.

| Punto final | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas las claves de API | `429` | Mayor o igual que | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Esta configuración de alerta te notifica cuando se producen errores en las campañas desencadenadas por la API y en los Lienzos, algunos de los cuales pueden ser de alta prioridad.

| Punto final | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campañas/desencadenar/enviar</code></li><li><code>/canvas/desencadenar/enviar</code></li><li><code>/mensajes/enviar</code></li></ul>{:/} | Todas las claves de API | `4XX` y `5XX` | Mayor o igual que | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Utiliza la siguiente configuración de alerta para recibir un aviso cuando una integración del socio deje de enviar datos a Braze.

| Punto final | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos finales | La clave de API utilizada para tu integración del socio | Todos los códigos de respuesta | Inferior o igual a | 0 | 1 día |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Consideraciones

- Cada alerta activa sólo enviará una notificación por correo electrónico o webhook una vez cada 8 horas. Esto es para evitar demasiadas notificaciones de una sola alerta. Si tu alerta te notifica antes de tiempo, considera la posibilidad de editar los criterios de alerta para que se ajusten mejor a tu caso de uso.
- Puedes tener hasta 10 alertas por espacio de trabajo.
