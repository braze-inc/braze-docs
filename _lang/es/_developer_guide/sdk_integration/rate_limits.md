---
page_order: 2.0
nav_title: Límites de tarifa
article_title: Límites de velocidad del SDK de Braze
description: "Infórmate sobre el SDK de Braze, el límite de velocidad inteligente del lado del cliente que optimiza la duración de la batería, reduce el uso del ancho de banda y garantiza una entrega de datos fiable."
---

# Límites de velocidad del SDK de Braze

> Infórmate sobre el SDK de Braze, el límite de velocidad inteligente del lado del cliente que optimiza la duración de la batería, reduce el uso del ancho de banda y garantiza una entrega de datos fiable.

## Comprender los límites de velocidad del SDK

El límite de velocidad del SDK de Braze utiliza las siguientes características para optimizar el rendimiento, minimizar el agotamiento de la batería, reducir el uso de datos y garantizar una entrega de datos fiable:

### Procesamiento asíncrono

El SDK de Braze utiliza un algoritmo de contenedor de tokens para limitar la tasa. Este enfoque permite ráfagas de actividad manteniendo el control de la tasa a largo plazo. En lugar de procesar las solicitudes en una cola estricta, el contenedor de tokens funciona de forma asíncrona:

- **Generación de token**: Los tokens se reponen a una tasa constante en el contenedor.
- **Tramitación de solicitudes**: Cualquier llamada al SDK que llegue cuando un token está disponible procede inmediatamente, independientemente de cuándo hayan llegado otras llamadas.
- **Sin orden estricto**: Las solicitudes no esperan en fila; varias llamadas pueden competir por el siguiente token disponible.
- **Manipulación de ráfagas**: Se permiten ráfagas cortas de actividad si hay suficientes tokens disponibles en el momento de las solicitudes.
- **Control de la tasa**: El rendimiento a largo plazo está limitado por la tasa constante de reposición de tokens.

Este flujo asíncrono ayuda al SDK a responder rápidamente a la capacidad disponible de la red, manteniendo al mismo tiempo unos niveles globales de tráfico predecibles.

### Limitación de velocidad adaptativa

El SDK Braze puede ajustar los límites de velocidad en tiempo real para proteger la infraestructura de red y mantener un rendimiento óptimo. Este enfoque:

- **Evita la sobrecarga**: Ajusta los límites para evitar la congestión de la red.
- **Optimiza el rendimiento**: Mantiene el buen funcionamiento del SDK en condiciones variables.
- **Responde a las condiciones**: Se adapta en función de la red actual y de los patrones de uso.

{% alert note %}
Dado que los límites se adaptan en tiempo real, no se proporcionan los tamaños exactos de los contenedores ni los valores estáticos. Pueden cambiar según las condiciones de la red y el uso.
{% endalert %}

### Optimizaciones de red

El SDK de Braze incluye varios comportamientos integrados para mejorar la eficiencia, reducir el uso de la batería y gestionar las condiciones variables de la red:

- **Dosificación automática**: Cola los eventos y envíalos en lotes eficientes.
- **Comportamiento consciente de la red**: Ajusta las tasas de descarga en función de la calidad de la conectividad.
- **Optimización de la batería**: Minimiza los despertares por radio y las llamadas de red.
- **Degradación gradual**: Mantiene la funcionalidad en condiciones de red deficientes.
- **Conciencia del fondo/del primer plano**: Optimiza el comportamiento a medida que cambia el ciclo de vida de la aplicación.

## Buenas prácticas

Sigue estas buenas prácticas para evitar problemas con el límite de velocidad:

| Haz esto | Esto no |
| --- | --- |
| Seguimiento de las acciones e hitos significativos de los usuarios | Seguimiento de cada interacción menor o evento de interfaz de usuario |
| Actualiza el contenido sólo cuando sea necesario | Actualiza el contenido en cada acción del usuario (como los eventos de desplazamiento) |
| Deja que el SDK se encargue de la dosificación automáticamente | Forzar la transmisión inmediata de datos (a menos que sea absolutamente necesario) |
| Céntrate en los eventos que añaden valor a los análisis | Llama a métodos del SDK en rápida sucesión sin tener en cuenta la frecuencia |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Conseguir ayuda

Si tienes problemas con el límite de velocidad del SDK, revisa los siguientes métodos de red:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Cuando te pongas en contacto con [support@braze.com](mailto:support@braze.com), incluye los siguientes detalles para cada uno de los métodos del SDK de red que utilices:

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:  
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
