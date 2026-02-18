---
nav_title: Preparar tus orígenes de datos
article_title: Preparar tus orígenes de datos
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre los activos de datos de retroalimentación críticos necesarios para cerrar el bucle de toma de decisiones de la IA y habilitar a tu agente para que aprenda y mejore continuamente."
---

# Preparar tus orígenes de datos

> Este artículo de referencia cubre los activos de datos de retroalimentación críticos necesarios para cerrar el bucle de toma de decisiones de la IA y habilitar a tu agente para que aprenda y mejore continuamente.

## Cerrar el ciclo de toma de decisiones de la IA

Aunque todos los datos de clientes son importantes para el agente (ver [Conectar fuentes de datos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)), los activos de datos más importantes son los que le dicen al agente lo que ocurrió después de que se enviaran las decisiones de interacción con los clientes.

Estos activos crean el bucle de retroalimentación que permite al agente aprender.

{% alert note %}
Si el agente está integrado de forma nativa con la plataforma de captación de clientes (como Braze, SFMC o Klaviyo), puede que no sean necesarios pasos adicionales de configuración para los datos de respuesta, ya que éstos pueden enviarse automáticamente con los datos de los clientes.
{% endalert %}

## Activos de datos críticos de retroalimentación

Hay tres activos fundamentales para crear el bucle de retroalimentación:

1. Datos de las conversiones
2. Datos de interacción
3. Datos de activaciones

### Datos de las conversiones

El activo de conversión describe lo que le ocurrió al cliente tras la orquestación. Por ejemplo, suponiendo que un agente esté optimizando el Valor Actual Neto (VAN) de los clientes que reciben campañas optimizadas, el activo de conversión podría incluir una actualización diaria de los cambios en el VAN.

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos | Decisioning Studio debe hacer un seguimiento del recorrido del cliente, desde la recomendación hasta la conversión, pasando por la activación. |
| Cada registro tiene una marca de tiempo asociada | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es sumamente importante para la formación de los agentes y el cálculo de métricas. |
| Si se utiliza una métrica objetivo no binaria (por ejemplo, convertida frente a no convertida), el valor de la métrica objetivo se proporciona con cada evento de conversión | Decisioning Studio utiliza el valor métrico objetivo para generar experiencias de entrenamiento que recompensen/penalicen adecuadamente al agente en función de los resultados de las acciones recomendadas. |
| Si las conversiones pueden atribuirse de forma única a las comunicaciones (e.g., canje de cupones), se proporcionan los campos necesarios para hacer coincidir las conversiones con las activaciones | Si un evento de conversión puede vincularse a una comunicación concreta, esto permite una atribución limpia y precisa. La atribución directa proporciona la señal más clara al agente, pero si no es posible (como ocurre a menudo), se utilizará la atribución basada en la proximidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Datos de interacción

El activo de interacción describe las interacciones con los clientes, incluidos los clics, las aperturas y otras impresiones. Los datos de interacción pueden estar incluidos en los datos de conversión o ser independientes. Desempeña un papel similar al de los datos de las conversiones: informa al agente de lo que ha ocurrido tras la interacción con los clientes.

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos | Decisioning Studio necesita hacer un seguimiento de los eventos de interacción de cada cliente. |
| Cada registro tiene una marca de tiempo asociada | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es sumamente importante para la formación de los agentes y el cálculo de métricas. |
| Si los clics, aperturas u otros datos de interacción pueden atribuirse de forma única a las comunicaciones, se proporcionan los campos necesarios para relacionar la interacción con las activaciones. | Al igual que con los datos de conversión, si la interacción puede vincularse a una comunicación concreta, esto permite una atribución limpia y precisa. La atribución directa proporciona la señal más clara al agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Datos de activaciones

El activo activaciones indica al agente qué comunicaciones se enviaron. Esto suele ser necesario dependiendo de cómo esté configurada la orquestación. Si el agente realiza la orquestación a través de una integración directa con Braze, SFMC o Klaviyo, entonces el agente puede obtener los datos de activación directamente.

{% alert note %}
Los datos de interacción y los datos de activación suelen encontrarse en el mismo activo de datos.
{% endalert %}

| Requisito | Causa |
|-------------|------|
| Cada registro contiene un identificador único de cliente que es coherente con todos los activos de datos | Decisioning Studio debe hacer un seguimiento del recorrido del cliente, desde la recomendación hasta la conversión, pasando por la activación. |
| Cada registro tiene una marca de tiempo asociada | Comprender el tiempo que transcurre entre la comunicación y la secuencia de acciones del cliente es sumamente importante para la formación de los agentes y el cálculo de métricas. |
| Se proporcionan los campos necesarios para hacer coincidir el contenido de la comunicación con los eventos de activación (como `event_id`) | Emparejar correctamente las características de comunicación con los envíos es necesario para la atribución y la formación de los agentes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

