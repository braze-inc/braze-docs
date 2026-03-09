---
nav_title: Diseño de agentes de toma de decisiones
article_title: Diseño de agentes de toma de decisiones
page_order: 4
page_type: reference
description: "Este artículo de referencia abarca conceptos clave y prácticas recomendadas para diseñar y configurar tu agente de toma de decisiones."
---

# Diseño de agentes de toma de decisiones

> Este artículo de referencia abarca conceptos clave y prácticas recomendadas para diseñar y configurar tu agente de toma de decisiones.

## Acerca de los agentes de decisión

El diseño de tu agente de toma de decisiones es el primer paso para la configuración de Decisioning Studio. Para que el agente decisorio pueda tomar decisiones, debes definir qué resultado deseas maximizar y qué acciones puede realizar el agente para lograrlo.

### Conceptos clave

Los siguientes términos se mencionan a lo largo de la guía de Decisioning Studio.

| Plazo | Definición |
| --- | --- |
| **Agente decisorio** | Un agente de decisión es una configuración personalizada para BrazeAI Decisioning Studio™ que se adapta a medida para cumplir un objetivo de negocio específico. Esto viene definido por la métrica de éxito, las dimensiones y las opciones que elijas. |
| **Métrica de éxito** | La métrica empresarial específica que deseas optimizar, como los ingresos, las conversiones o los ingresos medios por usuario (ARPU). Esta es la métrica que el agente decisorio tratará de maximizar a través de sus acciones. |
| **Dimensiones:** | Las dimensiones pueden considerarse como los *tipos de palancas* que el agente decisorio puede accionar para maximizar la métrica de éxito. Las dimensiones típicas incluyen la oferta, la línea del asunto, la creatividad, el canal o la hora de envío. |
| **Banco de Acción** | El banco de acciones define las *opciones específicas* a las que tiene acceso el agente decisorio para cada dimensión «palanca». Por ejemplo, para una dimensión de canal, definirías los canales específicos a los que tiene acceso el agente de decisión. Para una dimensión de oferta, definirías las ofertas específicas que el agente de decisión puede probar. 
| **Restricciones** | En general, el agente decisorio podría tomar cualquier combinación de acciones que tú introduzcas en el banco de acciones. Sin embargo, también puedes definir restricciones para limitar las acciones del agente de decisión con el fin de respetar las reglas empresariales críticas. Por ejemplo, esto podría consistir en impedir que una oferta específica sea seleccionada por clientes que se encuentren en una zona geográfica no elegible, o en establecer un presupuesto máximo que el agente responsable de la toma de decisiones puede gastar. 
{: .reset-td-br-1 .reset-td-br-2}

![Resumen general de alto nivel de un agente de toma de decisiones]({% image_buster /assets/img/decisioning_studio/decisioning_studio_high_level_agent.png %})

{% alert important %}
El agente de decisión solo puede realizar acciones que *tú* configures y añadas al banco de acciones. Esto significa que todas las acciones posibles se definen mediante las combinaciones de lo que pones en el banco de acciones.
{% endalert %}

## Cómo diseñar tu agente de toma de decisiones

Al configurar un agente de toma de decisiones, deberás tener en cuenta cuatro elementos de diseño principales:

### El «objetivo»: Define tus métricas de éxito.

> ¿Qué resultado quieres que el agente maximice?

Tu métrica de éxito es el resultado comercial que el agente optimizará. Esto debe estar directamente alineado con tus objetivos comerciales, no con métricas indirectas como los clics o las aperturas, sino con resultados comerciales reales como los ingresos, las conversiones, el ARPU o el valor de duración del ciclo de vida del cliente.

### El "quién": Selecciona tu audiencia

> ¿Con quién tendrá interacción el agente decisorio?

Define la audiencia que atenderá tu agente. Podrían ser todos los clientes, un segmento específico (como los miembros del programa de fidelización) o los clientes que se encuentran en una etapa concreta de su ciclo de vida (como los compradores recientes o los suscriptores en riesgo).

### El "qué": Configura tu banco de acciones

> ¿Qué opciones puede elegir el agente para influir en el resultado?

El banco de acciones define todas las palancas que el agente puede accionar: las dimensiones (como el canal, la oferta, el momento y la frecuencia) y las opciones específicas dentro de cada dimensión. El agente prueba diferentes combinaciones de estas opciones para encontrar la que mejor se adapta a cada cliente.

### El "cómo": Configura tus restricciones

> ¿Qué reglas debe seguir el agente?

Las restricciones son las reglas que debes seguir. Esto podría impedir que una oferta específica sea seleccionada para clientes en una zona geográfica no elegible, o establecer un presupuesto máximo que el agente de decisión puede gastar.

## Mejores prácticas y ejemplos

Para maximizar el impacto de tu agente de toma de decisiones, debes:

- Elige una métrica de éxito que se ajuste bien a tus objetivos de negocio, como los ingresos, las conversiones o el ARPU.
- Céntrate en las dimensiones o «palancas» que vas a probar, como la oferta, la línea del asunto, la creatividad, el canal o la hora de envío, que probablemente tengan un impacto significativo en la métrica de éxito.
- Selecciona las opciones para cada dimensión, como correo electrónico frente a SMS, o frecuencia diaria frente a semanal, que probablemente tengan un impacto significativo en la métrica de éxito.

Algunos ejemplos de agentes de decisión que podrías crear son:

{% tabs %}
{% tab Repeat purchase agent %}
Podrías crear un agente de compras repetidas para aumentar las conversiones de seguimiento tras una venta inicial:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio realiza automáticamente experimentos diarios, probando diferentes combinaciones de ofertas de productos, momentos de envío de mensajes y frecuencia para cada cliente.
- Con el tiempo, BrazeAI™ aprende qué es lo que mejor funciona para cada cliente.
- Realiza la orquestación de envíos personalizados a través de Braze para maximizar las tasas de recompra.
{% endtab %}
{% tab Cross-sell or upsell agent %}
Podrías crear un agente de ventas cruzadas o ventas adicionales para maximizar los ingresos medios por usuario (ARPU) de las suscripciones a Internet:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio realiza automáticamente experimentos diarios, probando diferentes combinaciones de mensajes, horarios de envío, descuentos y ofertas de planes para cada cliente.
- BrazeAI™ aprende qué clientes son susceptibles de aceptar ofertas innovadoras y cuáles necesitan descuentos u otros incentivos para actualizar sus planes.
- Realiza la orquestación de envíos personalizados a través de Braze para maximizar el ARPU.
{% endtab %}
{% tab Renewal and retention agent %}
Podrías crear un agente de renovación y retención para garantizar las renovaciones de contratos, maximizando tanto la duración del contrato como el valor actual neto (VAN):

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio realiza automáticamente experimentos diarios, probando diferentes ofertas de renovación para cada cliente.
- BrazeAI™ identifica a los clientes que son menos sensibles al precio y necesitan descuentos menos significativos para renovar.
- Realiza la orquestación de envíos personalizados a través de Braze para maximizar las renovaciones de contratos y el valor actual neto (VAN).
{% endtab %}
{% tab Winback agent %}
Podrías crear un agente de recuperación para aumentar la reactivación animando a los antiguos suscriptores a volver a suscribirse:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando miles de variables a la vez, incluyendo creatividad, mensaje, canal y cadencia.
- BrazeAI™ descubre la mejor combinación personalizada para cada cliente.
- Realiza la orquestación de envíos personalizados a través de Braze para maximizar las tasas de reactivación.
{% endtab %}
{% tab Referral agent %}
Podrías crear un agente de referidos para maximizar la apertura de nuevas cuentas a través de referencias de tarjetas de crédito empresariales de clientes existentes:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio realiza automáticamente experimentos diarios, probando diferentes correos electrónicos, creatividades, horas de envío y ofertas de tarjetas de crédito para cada cliente.
- BrazeAI™ determina la combinación ideal para clientes personalizados.
- Realiza la orquestación de envíos personalizados a través de Braze para maximizar las conversiones por referidos.
{% endtab %}
{% tab Lead nurturing and conversion agent %}
Podrías crear un agente de conversión y captación de clientes potenciales para impulsar los ingresos incrementales y pagar la cantidad adecuada por cada cliente:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes segmentos de clientes, metodologías de puja, niveles de puja y creatividades.
- BrazeAI™ aprovecha los sólidos datos propios para optimizar el rendimiento de los anuncios pagados a medida que cambian las políticas de privacidad.
- Orquestación de envíos personalizados a través de Braze para maximizar los ingresos y optimizar el coste por cliente.
{% endtab %}
{% tab Loyalty and engagement agent %}
Podrías crear un agente de fidelización y interacción para maximizar las compras de los nuevos inscritos en un programa de fidelización de clientes:

- Define la audiencia y el mensaje en Braze.
- Decisioning Studio ejecuta automáticamente experimentos diarios, probando diferentes ofertas por correo electrónico, horarios de envío y frecuencias para cada cliente.
- BrazeAI™ aprende qué es lo que mejor funciona para cada nuevo miembro del programa de fidelización.
- Orquesta envíos personalizados a través de Braze para maximizar las tasas de compra y recompra.
{% endtab %}
{% endtabs %}

## Próximos pasos

¿Estás listo para crear tu propio agente de toma de decisiones? Sigue los siguientes pasos para tu nivel de Decisioning Studio:

- **Decisioning Studio Go**: [Configurar Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/)
- **Decisioning Studio Pro**: [Configurar Decisioning Studio Pro]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/)

Estas guías te explican cómo conectar orígenes de datos, configurar la orquestación, diseñar tu agente y ponerlo en producción.
