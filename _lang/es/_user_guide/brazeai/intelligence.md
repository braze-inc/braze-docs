---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "La línea de productos Braze Intelligence Suite te ayuda a automatizar la toma de decisiones con información basada en datos. Desde el plazo de entrega hasta las pruebas multivariantes, las marcas pueden utilizar estas herramientas y características para crear experiencias dinámicas y a través de canales que se optimicen a escala. <br> <br> La Intelligence Suite consta de tres características principales: Intelligent Timing, Canal inteligente e Intelligent Selection."
description: "La línea de productos Braze Intelligence Suite te ayuda a automatizar la toma de decisiones con información basada en datos. Desde el plazo de entrega hasta las pruebas multivariantes, las marcas pueden utilizar estas herramientas y características para crear experiencias dinámicas y a través de canales que se optimicen a escala."

Tool:
  - Dashboard

guide_featured_title: "Herramientas y características"
guide_featured_list:
- name: Intelligent Timing
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: Canal inteligente
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: Intelligent Selection
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: Preguntas frecuentes sobre inteligencia
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## Casos prácticos

La Intelligence Suite proporciona potentes características para analizar el historial de usuarios y el rendimiento de campañas y Canvas, y luego hacer ajustes automáticos para aumentar la interacción, la audiencia y las conversiones. Para ver algunos ejemplos de cómo estas características pueden beneficiar a distintos sectores, consulta los siguientes casos de uso.

### Comercio electrónico

- **Ventas flash:** Utiliza el [filtro del canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) para estudiar el historial del usuario e identificar a los usuarios que son más receptivos a las notificaciones push frente a los correos electrónicos, y luego envía notificaciones push y correos electrónicos a los usuarios respectivos. Opcionalmente, selecciona un canal específico para los usuarios que no dispongan de datos suficientes para determinar su canal preferido.
- **Banners promocionales:** Utiliza [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para analizar el rendimiento de diferentes banners promocionales en una campaña recurrente y, a continuación, selecciona y envía automáticamente el banner que genere las tasas de click-through más altas.

### Viaja a

- **Ofertas de paquetes:** Utiliza Intelligent Selection para probar diferentes ofertas de paquetes de viaje en un Canvas recurrente y cambia gradualmente el tráfico del Canvas a la variante con mejor rendimiento para conseguir tasas de reserva más altas.
- **Ofertas de viajes:** Utiliza el filtro de canal inteligente para enviar ofertas de viajes personalizadas a través del canal más activo de un usuario, como el correo electrónico o los SMS, maximizando la probabilidad de que interactúen con tu mensaje.

### entretenimiento

- **Promoción de nuevos contenidos:** Utiliza [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para enviar notificaciones sobre nuevas películas, programas, música y otros tipos de contenido cuando sea más probable que los usuarios abran tu mensajería.
- **Compras en el juego:** Utiliza Intelligent Selection para probar diferentes mensajes promocionales para compras dentro del juego y selecciona automáticamente el que genere las tasas de conversión más altas.

### Restaurante de servicio rápido

Imaginemos que trabajamos en SandwichEmperor, un restaurante de comida rápida que tiene un nuevo artículo de menú por tiempo limitado: el Asado Real. Utilizaremos dos características de Intelligence Suite para enviar promociones personalizadas en un Canvas.

#### Utiliza Intelligent Timing para saber cuándo enviar las notificaciones

Utilizaremos Intelligent Timing para analizar las interacciones pasadas de nuestros usuarios con nuestra aplicación y cada canal de mensajería, y luego seleccionaremos automáticamente el mejor momento para promocionar el Asado Real a cada usuario. Algunos usuarios pueden recibir la promoción por la tarde, mientras que otros pueden recibirla por la noche. 

Proporcionaremos una hora alternativa para los usuarios que no tengan suficientes interacciones pasadas para analizar: la hora más popular de uso de la aplicación entre todos los usuarios.

![Configuración de entrega de Intelligent Timing para un paso de Mensaje.][1]

#### Utiliza la Selección Inteligente para seleccionar la promoción

Para los mensajes promocionales propiamente dichos, utilizaremos Intelligent Selection para probar tres mensajes diferentes (notificación push, correo electrónico y SMS) para el Asado Real. Intelligent Selection analizará el rendimiento de todos nuestros mensajes promocionales dos veces al día y, a continuación, enviará gradualmente más mensajes de los que obtengan mejores resultados y menos de los demás.

Después de que Intelligent Selection reúna suficientes datos para determinar el mensaje con mejor rendimiento, utilizará ese mensaje en el 100% de los envíos futuros.

![Sección de pruebas A/B de un Canvas con Intelligent Selection habilitada.][3]

#### Iniciar el Canvas

Tanto con Intelligent Timing como con Intelligent Selection, hemos configurado nuestras promociones de Royal Roast para optimizar el tiempo y la mensajería. Podemos lanzar nuestro Canvas y ver cómo nuestros envíos cambian para adaptarse a las preferencias de los usuarios.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
