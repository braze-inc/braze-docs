---
nav_title: Proyección de pruebas A/B
article_title: Proyección de pruebas A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artículo explica cómo funciona la proyección de pruebas A/B, cómo ejecutar una proyección y cómo utiliza Braze sus datos."
---

# Proyección de pruebas A/B

> La proyección de pruebas A/B utiliza redes neuronales para predecir qué líneas del asunto tienen mejor rendimiento. Nuestro modelo extrae las características lingüísticas de las pruebas A/B ganadoras realizadas en Braze y utiliza esos patrones lingüísticos estadísticos para enseñar a nuestra IA cuáles son las mejores líneas de asunto.

{% alert important %}
Esta función se encuentra actualmente en acceso anticipado. Póngase en contacto con su gestor de cuentas o de éxito de clientes de Braze si está interesado en participar en el acceso anticipado.
{% endalert %}

## Ejecutar una proyección

En la composición de la campaña, inserte sus variantes de mensaje y sus líneas de asunto en el editor. Cuando esté listo, vaya al paso **Público objetivo** del flujo de creación de campañas. En el panel **Pruebas A/B**, seleccione **Ejecutar proyección**.

<img width="518" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Se abrirá un modal con las líneas de asunto de cualquier variante de mensaje que ya haya creado. Opcionalmente, puede insertar líneas de asunto adicionales (hasta un máximo de diez) introduciendo manualmente una en la casilla y ejecutando la proyección. Seleccione **Ejecutar proyección**.

<img width="722" alt="imagen" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

La línea de asunto que nuestra IA prediga que es la mejor se resaltará con una etiqueta de **Ganador proyectado**.

{% alert note %}
En el caso de [las campañas push rápidas]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/), las pruebas A/B son compatibles cuando se seleccionan varias plataformas.
{% endalert %}

### ¿Hasta qué punto son exactas las proyecciones?

En las pruebas realizadas, hemos comprobado que las proyecciones tienen una precisión de aproximadamente el 70% a la hora de elegir entre pares de mensajes en pruebas A/B reales. Téngalo en cuenta a la hora de interpretar los mensajes que el modelo proyecta para ganar.

### ¿Cómo utilizamos sus datos?

Esta función aprende de las pruebas A/B realizadas anteriormente en Braze. La copia real de sus mensajes o de los de cualquier cliente de Braze nunca se facilita al modelo. Primero extraemos los patrones lingüísticos de alto nivel que predicen los mensajes ganadores en las pruebas A/B. A continuación, proporcionamos esos patrones a nuestra IA para enseñarle a discernir qué características lingüísticas constituyen líneas de asunto superiores.