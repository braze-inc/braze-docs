---
nav_title: Límites de velocidad de mensajería del espacio de trabajo
article_title: Límites de velocidad de mensajería del espacio de trabajo
alias: /workspace_messaging_rate_limits/
page_type: reference
description: "Este artículo de referencia describe los límites de velocidad de mensajería del espacio de trabajo y cómo funcionan con tus mensajes."
page_order: 10
---

# Límites de velocidad de mensajería del espacio de trabajo

> Usa los límites de velocidad de mensajería del espacio de trabajo para regular la tasa de entrega de tus mensajes salientes desde tu plataforma y asegurarte de que tus usuarios reciban los mensajes que necesitan.

{% alert important %}
Los límites de velocidad de mensajería del espacio de trabajo se están implementando gradualmente. Es posible que aún no veas esta configuración en tu dashboard.
{% endalert %}

## Cómo funciona

Los límites de velocidad de mensajería del espacio de trabajo se aplican al total de mensajes enviados en tu espacio de trabajo. Al establecer y optimizar un límite de velocidad a nivel de espacio de trabajo, puedes controlar mejor el tráfico saliente de tus mensajes de Braze, evitando posibles picos de demanda que podrían afectar el rendimiento del servidor.
{% alert note %}
Ten en cuenta que los mensajes enviados mediante puntos de conexión de mensajería de API como `/messages/send` y `/messages/schedule/create` también se contabilizan y se ven afectados por los límites de velocidad de mensajería del espacio de trabajo.
{% endalert %}
El recuento total de mensajes enviados por minuto no excede los límites de velocidad configurados del espacio de trabajo. No hay un orden particular en cuanto a qué campañas se despachan en los primeros minutos en comparación con los minutos posteriores.

Por ejemplo, supongamos que tienes un límite de velocidad de mensajería del espacio de trabajo de 100.000 mensajes por minuto, y los siguientes mensajes se están procesando a las 12 pm:

| Campaña    | Número de mensajes | Hora de envío |
|------------|--------------------|---------------|
| Campaña 1  | 100.000            | 12 pm         |
| Campaña 2  | 100.000            | 12 pm         |
| Campaña 3  | 100.000            | 12 pm         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Los mensajes se despachan en un intervalo de 3 minutos.

Los mensajes se procesan en paralelo. Cuando se procesan, los mensajes se programan respetando el límite de velocidad de mensajería del espacio de trabajo por orden de llegada. Esto significa que, en el ejemplo anterior, los mensajes enviados cada minuto son una mezcla variable de las campañas 1, 2 y 3 que suman 100.000.

![Ejemplo de cómo se despachan los mensajes para las tres campañas.]({% image_buster /assets/img/workspace_messaging_rate_limits2.png %})

Considera el siguiente ejemplo con un límite de velocidad de mensajería del espacio de trabajo de 100.000 mensajes por minuto, con los siguientes mensajes configurados:

| Campaña    | Número de mensajes | Hora de envío |
|------------|--------------------|---------------|
| Campaña 1  | 1.000.000          | 9 am          |
| Campaña 2  | 1.000.000          | 9:05 am       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A continuación se muestra la planificación de despacho esperada y los mensajes enviados por minuto:

- La campaña 1 se programaría de 9 am a 9:10 am, con 100.000 mensajes enviados por minuto.
- La campaña 2 se programaría para despacharse 5 minutos después de su hora de despacho original, de 9:10 am a 9:20 am, con 100.000 mensajes enviados por minuto.

![Ejemplo de cómo se despachan los mensajes por minuto para las dos campañas.]({% image_buster /assets/img/workspace_messaging_rate_limits1.png %})

{% alert note %}
Después de establecer el límite de velocidad de mensajería del espacio de trabajo, puedes aumentarlo. Sin embargo, cada mensaje ya procesado antes del aumento utiliza el límite establecido previamente.
{% endalert %}

## Configurar el límite de velocidad de mensajería de tu espacio de trabajo

1. En el panel de Braze, ve a **Configuración** > **Configuración del espacio de trabajo** > **Límites de velocidad de mensajería del espacio de trabajo**.
2. Selecciona **+ Añadir límite de velocidad** y luego selecciona un canal de mensajería.
3. En **Mensajes por minuto**, introduce el límite de velocidad.
4. Selecciona **Guardar**.

## Cosas que debes saber

El límite de velocidad se aplica al despacho, es decir, al inicio del intento de envío del mensaje. Cuando hay fluctuaciones en el tiempo que tarda en completarse el envío, el número de envíos completados puede superar ligeramente el límite de velocidad en algunos minutos. Con el tiempo, el número de envíos por minuto se promedia a no más del límite de velocidad.

Cuando una campaña o Canvas tiene su propio límite de velocidad establecido y también se aplica un límite de velocidad a nivel de espacio de trabajo, ambos se aplican. Por ejemplo, si una campaña tiene un límite de velocidad de 500.000 pero, debido a los límites de velocidad del espacio de trabajo, solo puede enviar 100.000 mensajes por minuto en ese momento, entonces el límite de velocidad del espacio de trabajo tiene efecto.

Braze intenta distribuir uniformemente los despachos de mensajes a lo largo del minuto, pero no puede garantizarlo. Por ejemplo, si tienes una campaña con un límite de velocidad de 500.000 mensajes por minuto, intentaremos distribuir los 500.000 mensajes de manera uniforme durante el minuto (aproximadamente 8.400 mensajes por segundo), pero puede haber cierta variación en la tasa por segundo.

Ten en cuenta que aún puedes establecer límites de velocidad individuales en tus campañas y Canvas. Estos se aplican de forma independiente de los límites de velocidad de mensajería del espacio de trabajo.

### Mensajes no incluidos en los límites de velocidad de mensajería del espacio de trabajo

- Los mensajes enviados mediante [campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) no están incluidos en los límites de velocidad de mensajería del espacio de trabajo. Esto significa que tienen su propio límite de velocidad y no se contabilizan en los límites de velocidad de mensajería del espacio de trabajo establecidos.
- Los mensajes a [grupos semilla]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab#seed-groups) y [envíos de prueba]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages) no están incluidos en los límites de velocidad de mensajería del espacio de trabajo. Esto significa que no tienen límite de velocidad y no se contabilizan en los límites de velocidad de mensajería del espacio de trabajo establecidos.
- Las respuestas automáticas de SMS no están incluidas en los límites de velocidad de mensajería del espacio de trabajo. Esto significa que no tienen límite de velocidad y no se contabilizan en los límites de velocidad de mensajería del espacio de trabajo establecidos.