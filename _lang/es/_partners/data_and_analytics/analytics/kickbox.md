---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "Este artículo de referencia describe la asociación entre Braze y Kickbox, una plataforma de verificación de correo electrónico utilizada para validar listas de correo electrónico o integrar la verificación en tu aplicación."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) es una plataforma de verificación de correo electrónico todo en uno, repleta de las características, integraciones y seguridad que necesitas para mantener tus datos de correo electrónico limpios y entregables. La integración de Kickbox mejora la capacidad de entrega de tus campañas Braze utilizando la verificación de correo electrónico de Kickbox para identificar las direcciones de correo electrónico no entregables y de baja calidad antes de pulsar enviar.

Kickbox te permite validar la calidad de las direcciones de correo electrónico de tus usuarios en el momento en que se actualiza un perfil de usuario en Braze. Esto se consigue mediante un flujo de trabajo Canvas o de campaña específico, que se desencadena al poblar el campo `email` de un perfil.

El Canvas o la campaña enviará un webhook a Kickbox, compartiendo la dirección de correo electrónico del usuario. Kickbox validará la dirección de correo electrónico y utilizará el punto final de la API REST de Braze para actualizar el perfil de usuario con un atributo personalizado que detalle su calidad.

## Requisitos previos

| Requisito                           | Descripción                                                                   |
| --------------------------------------|-------------------------------------------------------------------------------|
| Cuenta Kickbox                       | Se requiere una cuenta activa de Kickbox para utilizar esta integración.                |
| Clave de API REST Braze   | Una clave de API REST de Braze con permisos `users.track`. <br><br>Se puede crear en el panel de Braze yendo a **Configuración** > **API e identificadores** > **Claves de API**|
| Solicita acceso a la integración.     | Pide al equipo de soporte de Kickbox que te conceda acceso a la integración Braze.        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

Para la integración con Kickbox, sigue los pasos de [Integración con Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Ejemplos

### Verificación masiva

También puedes optar por verificar toda tu lista cada pocos meses o trimestralmente, para protegerte de los correos electrónicos que abandonan o de las listas que se degradan con el tiempo y hacen caer lentamente tu capacidad de entrega.

Para ello, tendrás que cambiar la configuración **de entrada** del flujo de trabajo, tal y como indica Kickbox. En lugar de seleccionar **Entrega basada en acciones**, selecciona **Programada**. A continuación, elige una hora programada para que tu lista se verifique toda a la vez.

### Crear segmentos verificados

Los atributos personalizados de Kickbox tienen un esquema coherente, que coincide con los siguientes ejemplos.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

Esto significa que puedes crear segmentos de audiencia de usuarios con direcciones de correo electrónico verificadas para que tus campañas y Canvases tengan una mayor tasa de éxito en la entrega, protegiendo tu reputación con los ESP.

Para ello, sigue estos pasos:

1. En Braze, ve a **Audiencia** > **Segmentos** > Crear segmento **.**
2. En la sección **Grupo de filtrado**, añade el filtro **Atributo personalizado** y selecciona "resultado" en el desplegable. 

Dependiendo de tu caso de uso, puede ser apropiado crear un segmento en el que el atributo personalizado "resultado" de Kickbox exista en un perfil de usuario, o en el que su valor sea igual a "entregable". Este filtro puede utilizarse por sí solo para crear un segmento, o puede formar parte de todos los segmentos futuros para validar a todos los usuarios que haya dentro. 