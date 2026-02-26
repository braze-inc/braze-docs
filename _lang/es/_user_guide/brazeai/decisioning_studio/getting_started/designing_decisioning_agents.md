---
nav_title: Diseñar agentes decisores
article_title: Diseñar agentes decisores
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre los conceptos clave y las mejores prácticas para diseñar y configurar tu agente de decisión."
---

# Diseñar agentes decisores

> Este artículo de referencia cubre los conceptos clave y las mejores prácticas para diseñar y configurar tu agente de decisión.

## Acerca de los agentes decisores

Diseñar tu agente de decisión es el primer paso para configurar Decisioning Studio. Para que el agente decisor pueda tomar decisiones, tienes que definir qué resultado quieres maximizar, y qué acciones puede realizar el agente para conseguirlo.

### Conceptos clave

A lo largo de la guía de Decisioning Studio se hace referencia a los siguientes términos.

| Plazo | Definición |
| --- | --- |
| **Agente decisor** | Un agente de decisión es una configuración personalizada de BrazeAI Decisioning Studio™ hecha a medida para cumplir un objetivo de negocio específico. Esto se define por la métrica de éxito, las dimensiones y las opciones que elijas. |
| **Métrica del éxito** | La métrica empresarial específica para la que quieres optimizar, como ingresos, conversiones o ingresos medios por usuario (ARPU). Es la métrica que el agente decisor intentará maximizar con sus acciones. |
| **Dimensiones:** | Las dimensiones pueden considerarse como los *tipos de palancas* de las que puede tirar el agente decisor para maximizar la métrica del éxito. Las dimensiones típicas incluyen la oferta, la línea del asunto, la creatividad, el canal o la hora de envío. |
| **Banco de Acción** | El banco de acciones define las *opciones concretas* a las que tiene acceso el agente decisor para cada dimensión "palanca". Por ejemplo, para una dimensión de canal, definirías los canales específicos a los que tiene acceso el agente decisor. Para una dimensión de oferta, definirías las ofertas concretas que el agente decisor puede probar. 
| **Restricciones** | En general, el agente decisor podría tomar cualquier combinación de acciones que pongas en el banco de acciones. Sin embargo, también puedes definir restricciones para limitar las acciones del agente decisor para que respete las reglas críticas de la empresa. Por ejemplo, podría ser impedir que se seleccione una oferta concreta para los clientes de una zona geográfica no elegible, o establecer un presupuesto máximo para el agente decisor. 
{: .reset-td-br-1 .reset-td-br-2}

![Un resumen de alto nivel de un agente decisor]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
El agente decisor sólo puede realizar acciones que *tú* configures y añadas al banco de acciones. Esto significa que todas las acciones posibles están definidas por las combinaciones de lo que pongas en el banco de acciones.
{% endalert %}

## Cómo diseñar tu agente decisor

Cuando configures un agente decisor, tendrás que pensar en cuatro elementos principales de diseño:

### El "objetivo": Define tu métrica de éxito

> ¿Qué resultado quieres que maximice el agente?

Tu métrica de éxito es el resultado empresarial que el agente optimizará. Esto debería alinearse directamente con tus objetivos empresariales, no con métricas indirectas como clics o aperturas, sino con resultados empresariales reales como ingresos, conversiones, ARPU o valor de duración del ciclo de vida del cliente.

### El "quién": Selecciona tu audiencia

> ¿A quién va a interactuar el agente decisor?

Define la audiencia a la que servirá tu agente. Puede tratarse de todos los clientes, de un segmento específico (como los miembros de un programa de fidelización) o de clientes en una fase concreta de su ciclo de vida (como los compradores recientes o los suscriptores de riesgo).

### El "qué": Configura tu banco de acciones

> ¿Qué opciones puede elegir el agente para impulsar el resultado?

El banco de acciones define todas las palancas de las que puede tirar el agente: las dimensiones (como canal, oferta, momento y frecuencia) y las opciones específicas dentro de cada dimensión. El agente experimenta con distintas combinaciones de estas opciones para encontrar lo que mejor funciona para cada cliente.

### El "cómo": Configura tus restricciones

> ¿Qué normas debe seguir el agente?

Las restricciones son las reglas que debe seguir el agente. Esto podría consistir en impedir que se seleccione una oferta concreta para los clientes de una zona geográfica no elegible, o en establecer un presupuesto máximo para el agente decisor.

## Buenas prácticas y ejemplos

Para maximizar el impacto de tu agente decisor, debes

- Elige una métrica de éxito que esté estrechamente alineada con tus objetivos de negocio, como ingresos, conversiones o ARPU.
- Céntrate en las dimensiones o "palancas" a probar, como la oferta, la línea del asunto, la creatividad, el canal o la hora de envío, que tienen más probabilidades de influir significativamente en la métrica de éxito.
- Selecciona las opciones para cada dimensión, como correo electrónico frente a SMS, o frecuencia diaria frente a semanal, que tengan más probabilidades de tener un impacto significativo en la métrica de éxito.

Algunos ejemplos de agentes de decisión que podrías construir son:

{% tabs %}
{% tab Repeat purchase agent %}
Podrías crear un agente de compra repetida para aumentar las conversiones de seguimiento tras una venta inicial:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes combinaciones de ofertas de productos, tiempo de envío de mensajes y frecuencia para cada cliente.
- Con el tiempo, BrazeAI™ aprende lo que funciona mejor para cada cliente
- Orquestación de envíos personalizados a través de Braze para maximizar las tasas de recompra.
{% endtab %}
{% tab Cross-sell or upsell agent %}
Podrías crear un agente de venta cruzada o de venta ascendente para maximizar los ingresos medios por usuario (ARPU) de las suscripciones a Internet:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando distintas combinaciones de mensajes, tiempos de envío, descuentos y ofertas de planes para cada cliente
- BrazeAI™ aprende qué clientes son susceptibles de recibir ofertas de salto y cuáles necesitan descuentos u otros incentivos para subir de categoría
- Orquestación de envíos personalizados a través de Braze para maximizar el ARPU
{% endtab %}
{% tab Renewal and retention agent %}
Podrías crear un agente de renovación y retención para asegurar la renovación de los contratos, maximizando tanto su duración como su valor actual neto (VAN):

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes ofertas de renovación para cada cliente
- BrazeAI™ identifica a los clientes menos sensibles a los precios y que necesitan descuentos menos importantes para renovar
- Orquestación de envíos personalizados a través de Braze para maximizar las renovaciones de contratos y el VAN.
{% endtab %}
{% tab Winback agent %}
Podrías crear un agente de recuperación para aumentar la reactivación animando a los antiguos suscriptores a volver a suscribirse:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando miles de variables a la vez, como la creatividad, el mensaje, el canal y la cadencia.
- BrazeAI™ descubre la mejor combinación para cada cliente individual
- Orquestación de envíos personalizados a través de Braze para maximizar las tasas de reactivación.
{% endtab %}
{% tab Referral agent %}
Podrías crear un agente de referidos para maximizar las nuevas cuentas abiertas a través de referidos de tarjetas de crédito de empresas de clientes existentes:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes correos electrónicos, creatividades, tiempos de envío y ofertas de tarjetas de crédito para cada cliente.
- BrazeAI™ determina la combinación ideal para clientes específicos
- Orquestación de envíos personalizados a través de Braze para maximizar las conversiones de referidos.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Podrías crear un agente de conversión y nutrición de clientes potenciales para aumentar los ingresos y pagar la cantidad adecuada a cada cliente:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes segmentos de clientes, metodología de pujas, niveles de puja y creatividades.
- BrazeAI™ aprovecha datos propios sólidos para optimizar el rendimiento de los anuncios de pago a medida que cambian las políticas de privacidad
- Orquesta envíos personalizados a través de Braze para maximizar los ingresos y optimizar el coste por cliente.
{% endtab %}
{% tab Loyalty and engagement agent %}
Podrías crear un agente de fidelización e interacción para maximizar las compras de los nuevos inscritos en un programa de fidelización de clientes:

- Define la audiencia y el mensaje en Braze
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes ofertas de correo electrónico, tiempos de envío y frecuencias para cada cliente.
- BrazeAI™ aprende qué funciona mejor para cada nuevo inscrito en el programa de fidelización
- Orquestación de envíos personalizados a través de Braze para maximizar las tasas de compra y recompra.
{% endtab %}
{% endtabs %}

## Próximos pasos

¿Listo para crear tu propio agente decisor? Sigue los siguientes pasos para tu nivel de Decisioning Studio:

- **Estudio de decisión Go**: [Configurar Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Configurar Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Estas guías te guiarán a través de la conexión de orígenes de datos, la configuración de la orquestación, el diseño de tu agente y el lanzamiento a producción.
