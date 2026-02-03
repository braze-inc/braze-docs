---
nav_title: Almacenamiento en caché de las respuestas
article_title: Caché de respuestas de contenido conectado
page_order: 2.5
description: "Este artículo explica cómo almacenar en caché las respuestas del Contenido conectado en diferentes campañas o mensajes en el mismo espacio de trabajo para optimizar la velocidad de envío."
---

# Caché de respuestas de contenido conectado

> Las respuestas del contenido conectado pueden almacenarse en caché en diferentes campañas o mensajes (en el mismo espacio de trabajo) para optimizar la velocidad de envío.

Braze no registra ni almacena permanentemente **los cuerpos de respuesta** del Contenido conectado. Durante la renderización del mensaje, las respuestas pueden retenerse temporalmente (por ejemplo, en memoria y en caché) para que Braze pueda renderizar Liquid y enviar el mensaje.

Para evitar el almacenamiento en caché, puedes especificar `:no_cache`, lo que puede provocar un aumento del tráfico de red. Para ayudar a solucionar problemas y supervisar el estado del sistema, Braze registra los metadatos de solicitud de contenido conectado (como la URL de solicitud completamente renderizada y el código de estado de la respuesta) para las llamadas realizadas con éxito y las fallidas. Estos registros se conservan hasta 30 días.

{% details Connected Content rendering and data handling (advanced) %}
Esta sección proporciona una visión más detallada, de extremo a extremo, de cómo Braze representa el Contenido Líquido y Conectado y dónde pueden existir datos temporalmente antes de enviar un mensaje. Esto puede ayudar en las revisiones sobre privacidad y tratamiento de datos.

#### Qué se almacena y qué no

- **Cuerpo de la respuesta Contenido conectado:** No almacenados permanentemente por Braze. Puede mantenerse temporalmente en memoria y, cuando se habilita la caché, almacenarse en caché con un tiempo de vida (TTL).
- **Metadatos de solicitud de contenido conectado:** Los metadatos de la solicitud, como la URL completa, el código de estado HTTP y la duración de la respuesta, se registran para la solución de problemas y la supervisión. Estos registros se conservan hasta 30 días. 
- **Mensaje final renderizado:** Existe en memoria durante la renderización. También puede almacenarse en otro lugar, dependiendo de tu configuración y canal (por ejemplo, Archivo de mensajes o Tarjetas de contenido).

#### Flujo de renderizado (alto nivel)

El siguiente flujo describe cómo Braze renderiza y envía mensajes para canales basados en proveedores, como correo electrónico, SMS y push. Los canales entregados mediante SDK, como las tarjetas de contenido, utilizan la misma renderización subyacente de Liquid y Contenido conectado, pero difieren en el momento en que se genera el contenido y en la forma de entregarlo.

1. Un trabajador en segundo plano renderiza la plantilla Liquid de un mensaje cuando éste se prepara para ser entregado.
2. Las etiquetas de Contenido conectado se evalúan durante la representación de Liquid.
3. Para cada etiqueta de Contenido conectado, Braze comprueba una caché de varios niveles. Si no existe ningún valor almacenado en caché (o el almacenamiento en caché está desactivado), Braze llama a tu punto final y recibe la respuesta.
4. La respuesta se inyecta en la plantilla Liquid y el mensaje se renderiza por completo.
5. En los canales basados en proveedores, el mensaje renderizado se envía al proveedor del canal y después al usuario. Para los canales entregados mediante SDK, como las tarjetas de contenido, el contenido renderizado se sincroniza con el SDK de Braze y puede generarse en el momento de la primera impresión o visualización, momento en el que se muestra al usuario.

#### Donde las respuestas de contenido conectado pueden vivir temporalmente

Braze utiliza una caché multinivel para las respuestas de Contenido conectado con TTL de entre cinco minutos y cuatro horas, dependiendo de tu uso de `:cache_max_age` y de otras reglas de caché:

- **Caché de memoria en proceso:** Caché transitorio dentro del proceso trabajador. Los datos sólo pueden estar en vivo mientras dure el trabajo (hasta ~11 minutos según el tiempo de espera del trabajador).
- **Caché local de la máquina:** Una caché por trabajador, como una instancia local de Memcached.
- **Caché de todo el clúster:** Una caché distribuida compartida entre trabajadores, como un clúster Memcached.

Estas capas de caché son volátiles y pueden desalojar datos antes del TTL configurado.

#### Qué cambia cuando utilizas `:no_cache`

Para los puntos finales que no están alojados dentro de la infraestructura Braze, el uso de `:no_cache` impide que el cuerpo de respuesta del Contenido conectado se almacene en Memcached. En estos casos, la respuesta sólo permanece en vivo en la memoria del proceso del trabajador mientras dura el trabajo de renderizado (hasta ~11 minutos). Para los puntos finales que se resuelven a hosts internos de Braze, las respuestas pueden seguir almacenándose en caché, tal como se describe en [Reventar caché](#cache-busting).

#### Donde puede vivir el resultado final renderizado

- **Archivo de mensajes:** Si está habilitado el Archivado de mensajes, Braze puede escribir el mensaje final renderizado en el contenedor de almacenamiento en la nube que hayas configurado. Si tu respuesta de Contenido conectado se incluye en el mensaje renderizado, se incluirá en la copia archivada.
- **Dispositivos de usuario:** Tras la entrega, el contenido del mensaje totalmente renderizado puede persistir en los dispositivos de los usuarios durante un tiempo desconocido.
- **Tarjetas de contenido:** El contenido renderizado de las tarjetas de contenido se almacena en una base de datos Braze hasta que la tarjeta caduca.
{% enddetails %}

## Configuración predeterminada de la caché

La antigüedad de la caché es de hasta cinco minutos (300 segundos). Puedes actualizarlo añadiendo el parámetro `:cache_max_age` a la llamada al Contenido conectado. Un ejemplo:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

Las peticiones GET se almacenan en caché. Puedes configurarlo añadiendo el parámetro :no_cache a la llamada Contenido conectado.

Las peticiones POST no se almacenan en caché. Esto puede forzarse añadiendo el parámetro :cache_max_age a la llamada Contenido conectado. El tiempo mínimo de caché es de 5 minutos, y el tiempo máximo de caché es de 4 horas.

{% alert note %}
La configuración de la caché no está garantizada. El almacenamiento en caché puede reducir las llamadas a tus puntos finales, por lo que recomendamos utilizar varias llamadas por punto final dentro de la duración del almacenamiento en caché, en lugar de depender excesivamente de éste.
{% endalert %}

### Límite de tamaño de la caché

El cuerpo de respuesta del Contenido conectado puede ser de hasta 1 MB. Si el cuerpo de la respuesta supera 1 MB, no se almacenará en caché.

## Tiempo de caché 

El Contenido Conectado guardará en caché el valor que devuelva de los puntos finales GET durante un mínimo de cinco minutos. Si no se especifica un tiempo de caché, el tiempo de caché predeterminado es de cinco minutos.

El tiempo de caché del Contenido conectado puede configurarse para que sea más largo con :cache_max_age,, como se muestra en el siguiente ejemplo. El tiempo mínimo de caché es de cinco minutos y el máximo de cuatro horas. Los datos del Contenido conectado se almacenan en caché en memoria utilizando un sistema de caché volátil, como Memcached. 

Como resultado, independientemente del tiempo de caché especificado, los datos de Contenido Conectado pueden ser desalojados de la caché en memoria de Braze antes de lo especificado. Esto significa que las duraciones de caché son sugerencias y pueden no representar realmente la duración que se garantiza que los datos serán almacenados en caché por Braze y es posible que vea más solicitudes de Contenido Conectado de las que podría esperar con una duración de caché determinada.

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

Con un POST no necesitas almacenar en caché el busto, ya que Braze nunca almacena en caché los resultados de las peticiones POST.

## Lo que hay que saber

- El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de Contenido conectado. Sin embargo, no está garantizado que siempre resulte en una única llamada de Contenido conectado por usuario.
- El almacenamiento en caché del Contenido conectado se basa en la URL y el espacio de trabajo. Si la llamada al contenido conectado es a la misma URL, puede almacenarse en caché en todas las campañas y lienzos.
- La caché se basa en una URL única, no en un ID de usuario o campaña. Esto significa que la versión en caché de una llamada a Contenido conectado podría utilizarse en varios usuarios y campañas de un espacio de trabajo si la URL es la misma.
