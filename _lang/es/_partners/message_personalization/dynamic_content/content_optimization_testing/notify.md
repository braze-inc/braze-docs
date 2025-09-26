---
nav_title: Avisa a
article_title: Avisa a
description: "Este artículo de referencia describe la asociación entre Braze y Notify, una solución de personalización omnicanal en tiempo real que ofrece personalización en todo el ciclo de vida del cliente."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Avisa a

> [Notify](https://fr.notify-group.com/) es una solución de software basada en IA que se integra fácilmente con las herramientas de administración de las relaciones con los clientes para mejorar las estrategias de marketing y facilitar la interacción a través de múltiples canales.

La integración de Braze y Notify permite a los especialistas en marketing impulsar eficazmente la interacción en varias plataformas. En lugar de depender de los métodos de marketing tradicionales, una campaña desencadenada por la API de Braze puede aprovechar las capacidades de Notify para entregar mensajes personalizados a través de múltiples canales, como correo electrónico, SMS, notificaciones push, etc.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Clave de API REST de Braze  | Una clave de API REST Braze con permisos `users.export.segment` y `campaigns.trigger.send`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Configuración CNAME | Debe crearse un subdominio para el píxel de seguimiento utilizado en el correo electrónico de Notify para realizar un seguimiento de la interacción del usuario con la mensajería, con el fin de informar mejor al modelo. Comparte la URL del subdominio con Notify después de crearlo. |
| Exportación de la adhesión voluntaria a la base de datos | Envía los datos de campaña y compra del último año (12 meses) a Notificar. ​Esta exportación se utilizará para entrenar el modelo predictivo Notify. <br><br> **Campos:** <br><br> **Correo electrónico:** Un hash SHA256 del correo electrónico, convertido a minúsculas y sin espacios iniciales ni finales.<br><br>**Segmento:** La información del segmento que define el nivel de actividad (activo o inactivo).<br><br>**Subsegmento:** Cualquier otra información de actividad relevante, como el nivel de actividad de compra.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crea tu campaña

Crea una [campaña desencadenada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery) en Braze. Después, comparte la campaña `api_identifier` con Notify.

### Paso 2: Crea tu segmento en Braze

A continuación, crea el segmento de usuarios al que te gustaría dirigirte con la campaña creada en el [paso 1](#step-1-create-your-campaign). A continuación, comparte el ID del segmento con Notify.

### Paso 3: Busca tu segmento

A continuación, Notify exportará los usuarios del segmento asociado a la campaña.

### Paso 4: Notificar desencadena la campaña

Utilizando el punto final `/campaigns/trigger/send`, la IA de Notify desencadena la campaña Braze creada en el [Paso 1](#step-1-create-your-campaign) para enviarla a los usuarios en el momento en que consideren más probable su interacción.
