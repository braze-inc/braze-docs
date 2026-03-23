---
page_order: 2.0
nav_title: Límites de velocidad
article_title: Límites de velocidad del SDK de Braze
description: "Descubre el límite de velocidad inteligente del SDK de Braze en el lado del cliente, que optimiza la duración de la batería, reduce el uso de ancho de banda y garantiza una entrega de datos fiable."
---

# Límites de velocidad del SDK de Braze

> Descubre el límite de velocidad inteligente del SDK de Braze en el lado del cliente, que optimiza la duración de la batería, reduce el uso de ancho de banda y garantiza una entrega de datos fiable.

## Comprender los límites de velocidad del SDK

El límite de velocidad del SDK de Braze utiliza las siguientes características para optimizar el rendimiento, minimizar el consumo de batería, reducir el uso de datos y garantizar una entrega de datos fiable:

### Procesamiento asíncrono

El SDK de Braze utiliza un algoritmo de contenedor de tokens para establecer el límite de velocidad. Este enfoque permite ráfagas de actividad mientras se mantiene el control de la tasa a largo plazo. En lugar de procesar las solicitudes en una cola estricta, el contenedor de tokens funciona de forma asíncrona:

- **Generación de tokens**: Los tokens se reponen a una tasa constante en el contenedor.
- **Gestión de solicitudes**: Cualquier llamada al SDK que llegue cuando haya un token disponible se procesa inmediatamente, independientemente de cuándo hayan llegado otras llamadas.
- **Sin orden estricto**: Las solicitudes no esperan en fila; varias llamadas pueden competir por el siguiente token disponible.
- **Gestión de ráfagas**: Se permiten breves ráfagas de actividad si hay suficientes tokens disponibles en el momento de las solicitudes.
- **Control de velocidad**: El rendimiento a largo plazo está limitado por la tasa de reposición constante de tokens.

Este flujo asíncrono ayuda al SDK a responder rápidamente a la capacidad de red disponible, al tiempo que mantiene unos niveles de tráfico generales predecibles.

### Limitación de velocidad adaptativa

El SDK de Braze puede ajustar los límites de velocidad en tiempo real para proteger la infraestructura de red y mantener un rendimiento óptimo. Este enfoque:

- **Evita la sobrecarga**: Ajusta los límites para evitar la congestión de la red.
- **Optimiza el rendimiento**: Mantiene el buen funcionamiento del SDK en condiciones variables.
- **Responde a las condiciones**: Se adapta en función de la red actual y los patrones de uso.

{% alert note %}
Dado que los límites se adaptan en tiempo real, no se proporcionan los tamaños exactos de los contenedores ni los valores estáticos. Pueden variar en función de las condiciones de la red y del uso.
{% endalert %}

### Optimizaciones de red

El SDK de Braze incluye varios comportamientos integrados para mejorar la eficiencia, reducir el consumo de batería y gestionar las diferentes condiciones de la red:

- **Procesamiento automático por lotes**: Pone en cola los eventos y los envía en lotes eficientes.
- **Comportamiento consciente de la red**: Ajusta las tasas de envío en función de la calidad de la conexión.
- **Optimización de la batería**: Minimiza las activaciones de radio y las llamadas de red.
- **Degradación gradual**: Mantiene la funcionalidad en condiciones de red deficientes.
- **Conciencia de segundo plano/primer plano**: Optimiza el comportamiento a medida que cambia el ciclo de vida de la aplicación.

## Buenas prácticas

Sigue estas prácticas recomendadas para evitar problemas relacionados con los límites de velocidad:

| Haz esto | No esto |
| --- | --- |
| Realiza un seguimiento de las acciones y los hitos significativos de los usuarios | Realizar un seguimiento de cada interacción menor o evento de la interfaz de usuario |
| Actualiza el contenido solo cuando sea necesario | Actualizar el contenido con cada acción del usuario (como los eventos de desplazamiento) |
| Deja que el SDK se encargue automáticamente del procesamiento por lotes | Forzar la transmisión inmediata de datos (a menos que sea absolutamente necesario) |
| Céntrate en los eventos que aportan valor al análisis | Llamar a los métodos del SDK en rápida sucesión sin tener en cuenta la frecuencia |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Obtener ayuda

Si tienes problemas con el límite de velocidad del SDK, revisa los siguientes métodos de red:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Cuando te pongas en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support), incluye los siguientes detalles para cada uno de los métodos de red del SDK que utilices:

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
