---
nav_title: Preparación de tus orígenes de datos
article_title: Preparación de tus orígenes de datos
page_order: 2
page_type: reference
description: "Este artículo de referencia abarca los activos de retroalimentación críticos necesarios para cerrar el ciclo de toma de decisiones de la IA y habilitar que tu agente aprenda y mejore continuamente."
---

# Preparación de tus orígenes de datos

> Este artículo de referencia abarca los activos de retroalimentación críticos necesarios para cerrar el ciclo de toma de decisiones de la IA y habilitar que tu agente aprenda y mejore continuamente.

## Cerrar el ciclo de toma de decisiones de la IA

Aunque todos los datos de los clientes son importantes para el agente (consulta [Conectar orígenes de datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), los activos más importantes son aquellos que informan al agente de lo que ha sucedido después de enviar las decisiones de interacción con los clientes.

Estos activos crean el bucle de retroalimentación que permite al agente aprender.

{% alert note %}
Si el agente está integrado de forma nativa con la plataforma de interacción con los clientes (como Braze, SFMC o Klaviyo), es posible que no sea necesario realizar pasos de configuración adicionales para los datos de retroalimentación, ya que estos pueden enviarse automáticamente con los datos de clientes.
{% endalert %}

## Activos críticos de datos sobre opiniones

Hay tres activos fundamentales para crear el ciclo de retroalimentación:

1. Datos de conversiones
2. Datos de interacción
3. Datos de activaciones

### Datos de conversiones

El activo de conversión describe lo que le sucedió al cliente después de la orquestación. Por ejemplo, supongamos que un agente está optimizando el valor actual neto (VAN) para los clientes que reciben campañas optimizadas. En ese caso, el activo de conversión podría incluir una actualización diaria de los cambios en el VAN.

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos. | Decisioning Studio necesita realizar el seguimiento del recorrido individual del cliente, desde la recomendación hasta la activación y la conversión. |
| Cada registro tiene una marca de tiempo asociada. | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es extremadamente importante para la formación de los agentes y el cálculo de métricas. |
| Si se utiliza una métrica objetivo no binaria (por ejemplo, convertida frente a no convertida), el valor de la métrica objetivo se proporciona con cada evento de conversión. | Decisioning Studio utiliza el valor métrico objetivo para generar experiencias de entrenamiento con el fin de recompensar o penalizar adecuadamente al agente en función de los resultados de las acciones recomendadas. |
| Si las conversiones pueden atribuirse de manera única a las comunicaciones (e.gpor ejemplo, canje de cupones), se proporcionan los campos necesarios para relacionar las conversiones con las activaciones. | Si un evento de conversión puede vincularse a una comunicación concreta, esto permite una atribución clara y precisa. La atribución directa proporciona la señal más clara al agente, pero si no es posible (como suele ser el caso), se utilizará la atribución basada en la proximidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Datos de interacción

El activo de interacción describe las interacciones con los clientes, incluyendo clics, aperturas y otras impresiones. Los datos de interacción pueden incluirse en los datos de conversión o pueden estar separados. Desempeña una función similar a la de los datos de conversiones: informa al agente de lo que ha sucedido después de la interacción con los clientes.

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos. | Decisioning Studio necesita realizar el seguimiento de los eventos de interacción de cada cliente individual. |
| Cada registro tiene una marca de tiempo asociada. | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es extremadamente importante para la formación de los agentes y el cálculo de métricas. |
| Si los clics, las aperturas u otros datos de interacción pueden atribuirse de forma única a las comunicaciones, se proporcionan los campos necesarios para relacionar la interacción con las activaciones. | Al igual que con los datos de conversión, si la interacción puede vincularse a una comunicación concreta, esto permite una atribución clara y precisa. La atribución directa proporciona la señal más clara al agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Datos de activaciones

El activo de activaciones indica al agente qué comunicaciones se han enviado. Esto suele ser necesario dependiendo de cómo esté configurada la orquestación. Si el agente realiza la orquestación a través de una integración directa con Braze, SFMC o Klaviyo, entonces el agente puede extraer los datos de activación directamente.

{% alert note %}
Los datos de interacción y los datos de activaciones suelen encontrarse en el mismo activo de datos.
{% endalert %}

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos. | Decisioning Studio necesita realizar el seguimiento del recorrido individual del cliente, desde la recomendación hasta la activación y la conversión. |
| Cada registro tiene una marca de tiempo asociada. | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es extremadamente importante para la formación de los agentes y el cálculo de métricas. |
| Se proporcionan los campos necesarios para hacer coincidir el contenido de la comunicación con los eventos de activación (como `event_id`) | Es necesario adaptar correctamente las características de comunicación a los envíos para la atribución y la formación de los agentes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

