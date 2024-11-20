---
nav_title: Resumen
article_title: Resumen de mensajes dentro de la aplicación para Roku
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "Este artículo cubre un resumen de la mensajería dentro de la aplicación de Roku, incluyendo las mejores prácticas y casos de uso."

---

# Resumen de mensajes dentro de la aplicación

> [Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) te ayudan a hacer llegar contenido a tu usuario sin interrumpir su día con una notificación push. Los mensajes dentro de la aplicación, personalizados y adaptados, mejoran la experiencia del usuario y ayudan a tu audiencia a obtener el máximo valor de tu aplicación. Con una gran variedad de diseños y herramientas de personalización para elegir, los mensajes dentro de la aplicación atraen a tus usuarios más que nunca.

Consulta nuestros [casos de estudio](https://www.braze.com/customers) para ver ejemplos de mensajes dentro de la aplicación.

![Tres imágenes de posibles mensajes dentro de la aplicación de Roku que podría crear un usuario. Estos ejemplos incluyen "toma de pantalla completa", "banner de página de inicio" y "notificador de esquina".]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## Tipos de mensajes dentro de la aplicación

Crea un mensaje dentro de la aplicación para Roku seleccionando **Dispositivos Roku** como plataforma de mensajes dentro de la aplicación.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## Documentación técnica

Visita nuestra [guía de integración]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration) para obtener instrucciones sobre cómo mostrar mensajes dentro de la aplicación y registrar impresiones y análisis de clics.

![Un ejemplo de "banner de página de inicio" que muestra los distintos componentes necesarios para construir el banner personalizado. Los componentes enumerados incluyen el componente de composición del mensaje (que muestra el cuerpo, el texto del botón, la imagen, el comportamiento asignado al botón (enlace profundo) y los pares clave-valor), los detalles del backend (audiencia enumerada como "usuarios que vieron la temporada 1", interacciones previstas (botón de enlace profundo a la aplicación, cierre del mensaje que descarta el mensaje y descarte automático tras 10 segundos), el desencadenante (inicio de sesión) y el par clave-valor (plantilla = homepage_banner)).]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})

## Pruebas y control de calidad

La característica de envío de prueba no es compatible con los mensajes dentro de la aplicación de Roku. Para probar un mensaje, lanza la campaña filtrada sólo a tu ID de usuario.

