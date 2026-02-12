---
page_order: 2.1
nav_title: Aplicaciones ChatGPT
article_title: Integrar Braze con aplicaciones ChatGPT
description: "Aprende a integrar Braze con ChatGPT Apps para habilitar el análisis y el registro de eventos en las aplicaciones basadas en IA."
platform:
  - ChatGPT Apps
---

# Integra Braze con aplicaciones ChatGPT

> Esta guía explica cómo integrar Braze con las aplicaciones ChatGPT para habilitar el análisis y el registro de eventos en las aplicaciones basadas en IA.

![Una tarjeta de contenido integrada en la aplicación ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Resumen

Las aplicaciones ChatGPT proporcionan una potente plataforma para crear aplicaciones conversacionales de IA. Al integrar Braze con tu aplicación ChatGPT, puedes seguir manteniendo el control de los datos propios en la era de la IA, incluyendo cómo:

- Realiza un seguimiento de la interacción y el comportamiento del usuario dentro de tu aplicación ChatGPT (como identificar qué preguntas o características del chat utilizan tus clientes).
- Segmenta y reorienta las campañas Braze en función de los patrones de interacción con la IA (como el envío por correo electrónico a los usuarios que hayan utilizado el chat más de tres veces por semana).

### Beneficios clave

- **Haz tuyo el recorrido del cliente:** Mientras los usuarios interactúan con tu marca a través de ChatGPT, tú mantienes la visibilidad de su comportamiento, preferencias y patrones de interacción. Estos datos fluyen directamente a los perfiles de usuario de Braze, no sólo a los análisis de la plataforma de IA.
- **Reorientación multiplataforma:** Sigue las interacciones de los usuarios en tu aplicación ChatGPT y reoriéntalos a través de tus canales propios (correo electrónico, SMS, notificaciones push, mensajería dentro de la aplicación) con campañas personalizadas basadas en sus patrones de uso de la IA.
- **Devuelve contenido promocional 1:1 a las conversaciones ChatGPT:** Entrega [mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) Braze [dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) y mucho más directamente dentro de tu experiencia ChatGPT utilizando los componentes de interfaz de usuario conversacional personalizados que tu equipo ha creado para tu aplicación.
- **Atribución de ingresos:** Haz un seguimiento de las compras y conversiones que se originan en las interacciones con la aplicación ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Requisitos previos

Antes de integrar Braze con tu aplicación ChatGPT, debes tener lo siguiente:

- Una nueva aplicación Web y clave de API en tu espacio de trabajo Braze
- Una [aplicación ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) creada en la plataforma OpenAI[(aplicación de ejemplo OpenAI](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

