---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Este artículo de referencia describe la asociación entre Braze y Bluedot, una plataforma de ubicación, que proporciona una plataforma de geovallado precisa y directa para tus aplicaciones."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) es una plataforma de ubicación que proporciona una plataforma de geovallado precisa y sencilla para tus aplicaciones. Utilice el SDK de Bluedot para enviar mensajes de forma más inteligente, automatizar el registro de pedidos móviles, optimizar los flujos de trabajo y crear experiencias sin fricciones. 

_Esta integración está mantenida por Bluedot._

## Sobre la integración

La integración de Braze y Bluedot le permite utilizar los servicios de localización de geofence de Bluedot para crear eventos de usuario que se pueden utilizar para crear recorridos, campañas y analizar los comportamientos e intereses de los clientes. Los eventos (entrada/salida) generados por el usuario en su dispositivo se envían inmediatamente a Braze con toda la información relevante. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Bluedot | Se requiere una cuenta Bluedot para aprovechar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

La información personalizada sobre la ubicación del evento proporcionada por Bluedot puede utilizarse en sus campañas para lograr casos de uso comunes como:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Restaurante de servicio rápido)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## Integración

### Paso 1: Crear un proyecto Bluedot
Configura tu cuenta de Bluedot e inicia sesión en tu [panel de Bluedot Canvas](https://docs.bluedot.io/canvas/). Visita la [documentación de Bluedot](https://docs.bluedot.io/canvas/creating-a-new-project/) para saber cómo crear un nuevo proyecto.

### Paso 2: Integrar los SDK
Integra el SDK de Bluedot Point y el SDK de Braze en tu aplicación siguiendo los pasos indicados en la documentación de [integración Bluedot-Braze](https://docs.bluedot.io/integrations/braze-integration/).

### Paso 3: Autenticar el SDK de Bluedot
Utiliza el `projectId` creado en el paso 1 para autenticar el SDK de Bluedot Point.

### Paso 4: Utilizar eventos Bluedot en Braze

#### Activación de mensajes

Puedes configurar una campaña push o Canvas que actúe a partir de eventos de ubicación generados por el SDK de Bluedot. Esta ruta de integración es ideal para la mensajería en tiempo real justo cuando los usuarios entran en un local o lugar de interés, o para la comunicación de seguimiento diferido después de que se hayan marchado.

Configure una campaña basada en acciones dentro de Braze que enviará mensajes basados en una ubicación establecida. Para su activador, utilice un evento personalizado de `bluedot_entry` o `bluedot_exit` como se muestra en la siguiente captura de pantalla:

![Una campaña basada en la acción en la fase de entrega. Aquí tiene dos opciones de programación que enviarán la campaña si un usuario realiza un evento personalizado `bluedot_entry` o `bluedot_exit`.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Dirigirse a los usuarios

Asegúrese de seleccionar **Todos los usuarios** para su área de trabajo.
![Una campaña basada en acciones con el paso de usuarios objetivo que le anima a seleccionar "Todos los usuarios" como segmento deseado.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}

