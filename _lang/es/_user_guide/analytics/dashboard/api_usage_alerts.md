---
nav_title: Alertas de uso de API
article_title: Alertas de uso de la API
description: "Este artículo ofrece un resumen de las alertas de uso de la API, que te permiten detectar de forma proactiva el tráfico inesperado."
page_order: 3.6
---

# Alertas de uso de API

> Las alertas de uso de API proporcionan una visibilidad crítica del uso de tus API, lo que te permite detectar de forma proactiva el tráfico inesperado. Al configurar estas alertas para realizar el seguimiento de los volúmenes de solicitudes API clave, podrás recibir notificaciones en tiempo real y resolver los problemas antes de que afecten a tus campañas de marketing.

## Acerca de las alertas de uso de API

Puedes utilizar las alertas de uso de la API para supervisar los volúmenes de solicitudes de las siguientes categorías:

| Categoría API | Detalles |
|--------------|---------|
| Puntos finales de la API REST | Realiza un seguimiento del uso de todas las llamadas a la API REST realizadas al backend de Braze, como el envío de mensajes, la creación de campañas o la exportación de usuarios. |
| Solicitudes de API del SDK | Realiza un seguimiento de las solicitudes de API realizadas desde los SDK de Braze en las aplicaciones de los clientes, como la activación de mensajes dentro de la aplicación o la sincronización de datos de usuario.<br><br>_\*Solo disponible para los clientes que hayan adquirido Usuarios activos al mes – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Creación de una alerta de uso de API

Para crear una alerta de uso de la API:

1. Ve a **Configuración** > **API e identificadores** > **Alertas de uso de API** y, a continuación, crea una nueva alerta.
2. Introduce un nombre para tu alerta y selecciona los puntos finales de la API REST y las claves de API para los que deseas recibir alertas.
3. Define tus criterios de alerta seleccionando uno o varios códigos de respuesta y especificando los [umbrales de alerta](#api-usage-alert-thresholds).
4. Cuando hayas terminado, alterna **la habilitación de la opción Alerta habilitada**.
    ![Un ejemplo de alerta de uso de API que envía notificaciones cuando el punto final de seguimiento de usuarios aumenta un 100 % en una hora.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Umbrales de alerta {#api-usage-alert-thresholds}

Al definir los criterios de alerta, puedes ajustar los siguientes umbrales:

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
        Define las condiciones que conducen al volumen umbral sobre el que deseas recibir una alerta. Se admiten los siguientes:<br><br>
        <ul>
          <li><strong>Aumento</strong> o <strong>disminución de</strong>: Compara las solicitudes con el intervalo de tiempo anterior.</li>
          <li><strong>Aumento porcentual</strong> o <strong>disminución porcentual</strong>: Compara el cambio porcentual en las solicitudes con respecto al intervalo de tiempo anterior.</li>
          <li><strong>Mayor o igual</strong>, o <strong>menor o igual</strong>: Cuenta las solicitudes en un intervalo de tiempo.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volumen umbral</td>
      <td>Se utiliza junto con la condición de umbral.</td>
    </tr>
    <tr>
      <td>En</td>
      <td>El intervalo de tiempo para la evaluación de alertas.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuración de notificaciones de alerta

Puedes configurar una alerta por correo electrónico, una alerta por webhook o ambas. Las alertas de webhook pueden resultar muy útiles en casos de uso como el envío de alertas a plataformas externas, por ejemplo, a un canal de Slack. Por ejemplo, consulta nuestra [documentación](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sobre cómo realizar la integración de alertas con Slack para conocer nuestras preferencias de notificación.

![Se enviará un correo electrónico a la dirección seleccionada cuando se cumplan los criterios de la alerta.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Carga útil de muestra {#payload}

A continuación se muestra un ejemplo de carga útil para el cuerpo de un webhook de alerta de uso de API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Ejemplos de alertas

A continuación, se indican algunas formas de configurar las alertas de uso de la API para recibir notificaciones en los siguientes casos.

{% tabs local %}
{% tab api health %}
Puedes configurar alertas para supervisar el estado general de tu API. Por ejemplo, puedes configurar estas alertas cuando los errores de API aumenten drásticamente, como un 20 % con respecto a la hora anterior.

| Punto de conexión | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos de conexión | Todas las claves de API | `4XX` y `5XX` | Aumentó en un 10 %. | 10 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Recibe una alerta cuando tu espacio de trabajo alcance su límite de velocidad para`/users/track`  endpoint. También puedes aplicar esta configuración a otros puntos finales de Braze.

| Punto de conexión | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Todas las claves de API | `429` | Mayor o igual que | 100 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Esta configuración de alerta te notifica cuando se producen errores en campañas y lienzos desencadenados por API, algunos de los cuales pueden ser de alta prioridad.

| Punto de conexión | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Todas las claves de API | `4XX` y `5XX` | Mayor o igual que | 1 | 1 hora |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Utiliza la siguiente configuración de alerta para recibir una notificación cuando una integración del socio deje de enviar datos a Braze.

| Punto de conexión | Clave de API | Código de respuesta | Condición de umbral | Volumen umbral | En |
| --- | --- | --- | --- | --- | --- |
| Todos los puntos de conexión | La clave de API utilizada para la integración del socio. | Todos los códigos de respuesta | Menor o igual que | 0 | 1 día |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Consideraciones

- Cada alerta activa solo enviará una notificación por correo electrónico o webhook una vez cada 8 horas. Esto es para evitar que se envíen demasiadas notificaciones por una sola alerta. Si la alerta te avisa prematuramente, considera la posibilidad de editar los criterios de alerta para que se ajusten mejor a tu caso de uso.
- Puedes tener hasta 10 alertas por espacio de trabajo.
