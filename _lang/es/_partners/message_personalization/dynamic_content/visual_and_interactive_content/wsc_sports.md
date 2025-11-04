---
nav_title: WSC Sports
article_title: WSC Sports
description: "Este artículo de referencia describe la asociación entre Braze y WSC Sports, una plataforma de vídeo deportivo que te permite incluir medios deportivos ricos y sólidos en tus notificaciones push de Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> La plataforma [WSC Sports](https://wsc-sports.com/) genera vídeos deportivos personalizados para cada plataforma digital y cada aficionado al deporte, de forma automática y en tiempo real. 

_Esta integración es mantenida por WSC Sports._

## Sobre la integración

La integración de Braze y WSC Sports te permite incluir medios deportivos ricos y sólidos en tus notificaciones push de Braze. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta CSM | Se necesita una cuenta WSC para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos para **Mensajes**, **Segmentos**, **Campañas** y **Canvas**. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La aplicación WSC Sports gestiona el proceso de principio a fin, desde la selección del vídeo hasta la llegada de la notificación push al dispositivo del usuario final. 

### Paso 1: Selecciona la configuración de envío

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "soldadura_integracion.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Antes de iniciar la integración, asegúrate de que tienes tus segmentos de campaña y de usuarios deseados creados en Braze. Una vez completado, en la plataforma WSC Sports, selecciona el video que desees, y en la configuración de envío, selecciona el segmento de usuarios Braze y el ID de campaña que quieras utilizar. Por último, elige la hora a la que quieres que se envíe tu mensaje push. 

#### Llamada API

Una vez enviada, WSC Sports entregará la notificación push a los segmentos de usuarios elegidos, utilizando los siguientes endpoints Braze, en función de las opciones seleccionadas:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

El cuerpo resultante del mensaje es el siguiente: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Paso 2: Prueba de envío

En este punto, tu campaña debería estar lista para probarla y enviarla. Comprueba los registros de mensajes de error de Braze si te encuentras con errores. 


