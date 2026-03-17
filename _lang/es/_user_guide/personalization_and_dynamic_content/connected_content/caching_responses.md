---
nav_title: Almacenamiento en caché de respuestas
article_title: Respuestas de contenido conectado a la caché
page_order: 2.5
description: "Este artículo explica cómo almacenar en caché las respuestas de contenido conectado en diferentes campañas o mensajes del mismo espacio de trabajo para optimizar la velocidad de envío."
---

# Respuestas de contenido conectado a la caché

> Las respuestas de contenido conectado se pueden almacenar en caché en diferentes campañas o mensajes (en el mismo espacio de trabajo) para optimizar la velocidad de envío.

Braze no registra ni almacena de forma permanente **los cuerpos de respuesta** del contenido conectado. Durante la representación del mensaje, las respuestas se pueden almacenar temporalmente (por ejemplo, en la memoria y en la caché) para que Braze pueda representar Liquid y enviar el mensaje.

Para evitar el almacenamiento en caché, puedes especificar `:no_cache`, lo que puede provocar un aumento del tráfico de red. Para ayudar con la solución de problemas y la supervisión del estado del sistema, Braze registra los metadatos de las solicitudes de contenido conectado (como la URL de la solicitud completamente renderizada y el código de estado de la respuesta) para las llamadas exitosas y fallidas. Estos registros se conservan durante un máximo de 30 días.

{% details Connected Content rendering and data handling (advanced) %}
Esta sección ofrece una visión más detallada y de extremo a extremo de cómo Braze representa el contenido líquido y conectado, y dónde pueden almacenarse temporalmente los datos antes de enviar un mensaje. Esto puede ayudar con las revisiones de privacidad y manejo de datos.

#### Lo que se almacena y lo que no

- **Cuerpo de respuesta de contenido conectado:** Braze no los almacena de forma permanente. Se puede almacenar temporalmente en la memoria y, cuando la habilitación del almacenamiento en caché está activa, se puede guardar en la caché con un tiempo de vida (TTL).
- **Metadatos de solicitud de contenido conectado:** Los metadatos de las solicitudes, como la URL completa, el código de estado HTTP y la duración de la respuesta, se registran para la solución de problemas y la supervisión. Estos registros se conservan durante un máximo de 30 días. 
- **Mensaje final renderizado:** Existe en la memoria durante el renderizado. Esto también puede almacenarse en otro lugar, dependiendo de tu configuración y canal (por ejemplo, Archivo de mensajes o Tarjetas de contenido).

#### Flujo de renderizado (alto nivel)

El siguiente flujo describe cómo Braze procesa y envía mensajes para canales basados en proveedores, como correo electrónico, SMS y notificaciones push. Los canales proporcionados por SDK, como las tarjetas de contenido, utilizan la misma representación subyacente de Liquid y contenido conectado, pero difieren en el momento en que se genera el contenido y en la forma en que se entrega.

1. Un trabajador en segundo plano procesa la plantilla Liquid para un mensaje cuando este está listo para ser entregado.
2. Las etiquetas de contenido conectado se evalúan durante la representación Liquid.
3. Para cada etiqueta de contenido conectado, Braze comprueba una caché de varios niveles. Si no existe ningún valor almacenado en caché (o el almacenamiento en caché está desactivado), Braze llama a tu punto final y recibe la respuesta.
4. La respuesta se inyecta en la plantilla Liquid y el mensaje se renderiza por completo.
5. En el caso de los canales basados en proveedores, el mensaje renderizado se envía al proveedor del canal y, a continuación, al usuario. En el caso de los canales entregados por SDK, como las tarjetas de contenido, el contenido renderizado se sincroniza con el SDK de Braze y se puede generar en el momento de la primera impresión o visualización, momento en el que se muestra al usuario.

#### Dónde pueden residir temporalmente las respuestas de contenido conectado

Braze utiliza una caché de varios niveles para las respuestas de contenido conectado con TTL entre cinco minutos y cuatro horas, dependiendo de tu uso de`:cache_max_age`  y otras reglas de almacenamiento en caché:

- **Caché de memoria en proceso:** Caché transitoria dentro del proceso de trabajo. Los datos solo pueden permanecer activos durante la duración del trabajo (hasta unos 11 minutos, según el tiempo de espera del trabajador).
- **Caché de la máquina local:** Una caché por trabajador, como una instancia local de Memcached.
- **Caché para todo el clúster:** Una caché distribuida compartida entre los trabajadores, como un clúster Memcached.

Estas capas de caché son volátiles y pueden eliminar datos antes del TTL configurado.

#### ¿Qué cambia cuando usas `:no_cache`

Para los puntos finales que no están alojados dentro de la infraestructura de Braze, el uso de`:no_cache`  impide que el cuerpo de la respuesta de contenido conectado se almacene en Memcached. En estos casos, la respuesta solo permanece en la memoria del proceso del trabajador durante el tiempo que dura el trabajo de renderización (hasta unos 11 minutos). En el caso de los puntos finales que se resuelven en hosts internos de Braze, las respuestas pueden seguir almacenándose en caché, tal y como se describe en [Eliminación de caché](#cache-busting).

#### Dónde puede residir el resultado final renderizado

- **Archivo de mensajes:** Si el archivado de mensajes está habilitado, Braze puede escribir el mensaje final renderizado en tu contenedor de almacenamiento en la nube configurado. Si tu respuesta de contenido conectado se incluye en el mensaje renderizado, se incluirá en la copia archivada.
- **Dispositivos de usuario:** Después de la entrega, el contenido completo del mensaje puede permanecer en los dispositivos de los usuarios durante un tiempo indeterminado.
- **Tarjetas de contenido:** El contenido renderizado para las tarjetas de contenido se almacena en una base de datos de Braze hasta que la tarjeta caduca.
{% enddetails %}

## Configuración predeterminada de la caché

La duración de la caché es de hasta cinco minutos (300 segundos). Puedes actualizar esto añadiendo el`:cache_max_age`parámetro a la llamada de contenido conectado. Un ejemplo:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Las solicitudes GET se almacenan en caché. Puedes configurar esto añadiendo el:no_cacheparámetro a la llamada de contenido conectado.

Las solicitudes POST no se almacenan en caché. Esto se puede forzar añadiendo el:cache_max_ageparámetro a la llamada de contenido conectado. El tiempo mínimo de almacenamiento en caché es de 5 minutos y el máximo es de 4 horas.

{% alert note %}
La configuración de la caché no está garantizada. El almacenamiento en caché puede reducir las llamadas a tus puntos finales, por lo que recomendamos utilizar varias llamadas por punto final dentro de la duración de la caché en lugar de depender excesivamente del almacenamiento en caché.
{% endalert %}

### Límite de tamaño de la caché

El cuerpo de respuesta del contenido conectado puede tener un tamaño máximo de 1 MB. Si el cuerpo de la respuesta supera 1 MB, no se almacenará en caché.

## Tiempo de caché 

El contenido conectado almacenará en caché el valor que devuelve desde los puntos finales GET durante un mínimo de cinco minutos. Si no se especifica un tiempo de caché, el tiempo de caché predeterminado es de cinco minutos.

El tiempo de caché del contenido conectado se puede configurar para que sea más largo,:cache_max_age,tal y como se muestra en el siguiente ejemplo. El tiempo mínimo de almacenamiento en caché es de FIVE minutos y el máximo es de cuatro horas. Los datos del Contenido conectado se almacenan en caché en memoria utilizando un sistema de caché volátil, como Memcached. 

Como resultado, independientemente del tiempo de caché especificado, los datos de contenido conectado pueden ser eliminados de la caché en memoria de Braze antes de lo especificado. Esto significa que las duraciones de caché son sugerencias y pueden no representar realmente la duración que se garantiza que los datos serán almacenados en caché por Braze y es posible que vea más solicitudes de Contenido Conectado de las que podría esperar con una duración de caché determinada.

### Caché durante los segundos especificados

Este ejemplo almacenará en caché durante 900 segundos (o 15 minutos).

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Eliminación de caché

Para evitar que Connected Content almacene en caché el valor que devuelve de una solicitud GET, puede utilizar la configuración `:no_cache`. Sin embargo, las respuestas de los hosts internos de Braze seguirán almacenándose en caché.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Asegúrese de que el punto final de contenido conectado proporcionado puede gestionar grandes cantidades de tráfico antes de utilizar esta opción, o es probable que aumente la latencia de envío (mayores retrasos o intervalos de tiempo más amplios entre la solicitud y la respuesta) debido a que Braze realiza solicitudes de contenido conectado para cada mensaje.
{% endalert %}

Con un POST no es necesario eliminar la caché, ya que Braze nunca almacena en caché los resultados de las solicitudes POST.

## Lo que hay que saber

- El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas a contenido conectado. Sin embargo, no se garantiza que siempre se produzca una única llamada de contenido conectado por usuario.
- El almacenamiento en caché de contenido conectado se basa en la URL y el espacio de trabajo. Si la llamada de contenido conectado se realiza a la misma URL, se puede almacenar en caché en todas las campañas y lienzos.
- La caché se basa en una URL única, no en un ID de usuario o una campaña. Esto significa que la versión almacenada en caché de una llamada de contenido conectado podría utilizarse para varios usuarios y campañas en un espacio de trabajo si la URL es la misma.
