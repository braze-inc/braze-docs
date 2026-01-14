---
nav_title: Proyección de pruebas A/B
article_title: Proyección de pruebas A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artículo explica cómo funciona la proyección de pruebas A/B, cómo ejecutar una proyección y cómo utiliza Braze tus datos."
---

# Proyección de pruebas A/B

> La proyección de pruebas A/B utiliza redes neuronales para predecir qué líneas del asunto tienen mejor rendimiento. Nuestro modelo extrae características lingüísticas de las pruebas A/B ganadoras realizadas en Braze y utiliza esos patrones lingüísticos estadísticos para enseñar a nuestra IA qué hace mejores líneas del asunto.

{% alert important %}
Esta característica está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas o de éxito del cliente de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Ejecutar una proyección

En la composición de la campaña, inserta tus variantes de mensaje y sus líneas del asunto en el editor. Cuando estés listo, ve al paso **Audiencia objetivo** del flujo de creación de campañas. En el panel **Pruebas A/B**, selecciona **Ejecutar proyección**.

<img width="518" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Se abrirá un modal con las líneas del asunto de cualquier variante de mensaje que ya hayas creado. Opcionalmente, puedes insertar líneas del asunto adicionales (hasta un máximo de diez) introduciendo manualmente una en la casilla y ejecutando la proyección. Selecciona **Ejecutar proyección**.

<img width="722" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

La línea del asunto que nuestra IA prediga que es la mejor se resaltará con una etiqueta de **Ganador Proyectado**.

{% alert note %}
Para las [campañas push rápidas]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/), se admiten pruebas A/B cuando seleccionas varias plataformas.
{% endalert %}

### ¿Hasta qué punto son precisas las proyecciones?

En las pruebas, descubrimos que las proyecciones tenían un 70% de precisión al elegir entre pares de mensajes en pruebas A/B reales. Tenlo en cuenta al interpretar los mensajes que el modelo proyecta para ganar.

### ¿Cómo utilizamos tus datos?

Esta característica aprende de pruebas A/B anteriores realizadas en Braze. La copia real de tus mensajes o de los de cualquier cliente de Braze nunca se proporciona al modelo. Primero extraemos los patrones lingüísticos de alto nivel que predicen los mensajes ganadores en las pruebas A/B. A continuación, proporcionamos esos patrones a nuestra IA para enseñarle a discernir qué características lingüísticas constituyen líneas del asunto superiores.