---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes de las Actividades en vivo
page_order: 20
description: "Esta página proporciona respuestas a las preguntas más frecuentes sobre las actividades en vivo para el SDK de Swift."
tool: Live Activities
platform:
  - iOS
---

# Preguntas más frecuentes

> Este artículo responde a algunas preguntas frecuentes sobre las Actividades en vivo.

## Funcionalidad y soporte

### ¿Qué plataformas admiten Actividades en vivo?

Las Actividades en vivo son actualmente una característica específica de iOS. El artículo Actividades en vivo cubre los [requisitos previos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites) para gestionar Actividades en vivo a través del SDK Swift de Braze.

### ¿Son compatibles las aplicaciones React Native con las actividades en vivo?

Sí, a partir de la versión 3.0.0+ del SDK React Native se admiten Actividades en vivo a través del SDK Swift de Braze. Es decir, tienes que escribir código React Native de iOS directamente sobre el SDK Swift de Braze. 

No existe una API de conveniencia JavaScript específica de React Native para las Actividades en vivo porque las características de las Actividades en vivo proporcionadas por Apple utilizan lenguajes intraducibles en JavaScript (por ejemplo, concurrencia Swift, genéricos, SwiftUI).

### ¿Admite Braze Actividades en vivo como campaña o paso en Canvas?

No, actualmente no es posible.

## Notificaciones push y actividades en vivo

### ¿Qué ocurre si se envía una notificación push mientras está activa una Actividad en vivo? 

![Una pantalla de teléfono con un partido deportivo de los Bulls contra los Bears en vivo hacia el centro de la pantalla y texto de notificación push lorem ipsum en la parte inferior de la pantalla.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Las Actividades en vivo y las notificaciones push ocupan un espacio de pantalla diferente y no entrarán en conflicto en la pantalla de un usuario.

### Si las Actividades en vivo aprovechan la funcionalidad de los mensajes push, ¿es necesario habilitar las notificaciones push para recibir Actividades en vivo?

Aunque las Actividades en vivo se basan en notificaciones push para las actualizaciones, están controladas por diferentes configuraciones de usuario. Un usuario puede optar por las Actividades en vivo pero no por las notificaciones push, y al revés.

Los tokens de actualización de Actividad en vivo caducan a las ocho horas.

### ¿Las actividades en vivo requieren push primers?

[Los cebadores push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) son una buena práctica para pedir a tus usuarios que acepten las notificaciones push de tu aplicación. Sin embargo, no hay ninguna indicación del sistema para participar en las Actividades en vivo. Por defecto, los usuarios son incluidos en las Actividades en vivo para una aplicación individual cuando el usuario instala esa aplicación en iOS 16.1 o posterior. Este permiso puede habilitarse o deshabilitarse en la configuración del dispositivo para cada aplicación.

## Temas técnicos y solución de problemas

### ¿Cómo sé si las Actividades en vivo tienen errores?

Cualquier error de Actividad en vivo se registrará en el panel de Braze, en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), donde puedes filtrar por "Errores de Actividad en vivo".

### Después de enviar una notificación push, ¿por qué no he recibido mi Actividad en vivo?

En primer lugar, comprueba que tu carga útil incluye todos los campos obligatorios descritos en el punto final [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) punto final. Los campos `activity_attributes` y `content_state` deben coincidir con las propiedades definidas en el código de tu proyecto. Si estás seguro de que la carga útil es correcta, es posible que tengas una tasa limitada por APN. Este límite lo impone Apple y no Braze.

Para verificar que tu notificación push ha llegado correctamente al dispositivo pero no se ha mostrado debido a los límites de tasa, puedes depurar tu proyecto utilizando la aplicación Consola de tu Mac. Adjunta el proceso de grabación del dispositivo que desees y, a continuación, filtra los registros por `process:liveactivitiesd` en la barra de búsqueda.

### Recibo una respuesta de acceso denegado cuando intento utilizar el punto final `live_activity/update`. ¿Por qué?

Las claves de API que utilices deben tener los permisos correctos para acceder a los distintos puntos finales de la API Braze. Si estás utilizando una clave de API que creaste anteriormente, es posible que hayas olvidado actualizar sus permisos. Lee nuestro [resumen de seguridad de la clave de API]({{site.baseurl}}/api/basics/#rest-api-key-security) para refrescarte la memoria.

### ¿Comparte el punto final `messages/send` límites de velocidad con el punto final `messages/live_activity/update`? 

De manera predeterminada, el límite de velocidad para el punto final `messages/live_activity/update` es de 250 000 solicitudes por hora, por espacio de trabajo y a través de múltiples puntos finales. Para más información, consulta los [límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

### ¿Por qué no se generan mis tokens de notificaciones push?

Apple ha limitado sus API `pushToStartToken` y `pushToStartTokenUpdates`, que se introdujeron en iOS 17.2. En la práctica, los tokens de push-to-start sólo se generan durante el primer lanzamiento de la aplicación en `application(_:didFinishLaunchingWithOptions:)` después de la primera instalación. Si es necesario repetir este paso, los tokens sólo pueden generarse de nuevo creando manualmente una nueva instancia de esa Actividad en vivo, o tras reiniciar y volver a instalar la aplicación.

### ¿Cuántas Actividades en vivo puedo iniciar para mi aplicación?

Los límites los define Apple y pueden variar en función de varios factores. También pueden estar sujetos a cambios en el futuro. En la práctica, hay un límite de cinco instancias de actividad simultáneas que pueden lanzarse por aplicación en un momento dado. Cualquier intento posterior de lanzar una nueva instancia más allá de ese límite será ignorado por el sistema.

### ¿Qué otras cosas debo tener en cuenta durante la solución de problemas?

- Asegúrate de que estás utilizando una clave `.p8` para la autenticación en lugar de un archivo `.p12` o `.pem`.
- Comprueba que tu perfil de aprovisionamiento push coincide con el entorno que estás probando. Los certificados universales pueden configurarse en el panel de Braze para enviarlos al entorno de desarrollo o de producción del servicio de notificaciones push de Apple (APN). Utilizar un certificado de desarrollador para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.


