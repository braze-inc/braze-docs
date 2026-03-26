---
nav_title: Crear geovallas
article_title: Crear geovallas
page_order: 1
page_type: reference
toc_headers: h2
description: "Aprende a configurar permisos de ubicación, crear un mensaje previo de permisos de ubicación y construir geovallas para campañas basadas en ubicación."
tool: 
  - Location
search_rank: 9
---

# Geovallas

> Una geovalla es un área geográfica virtual, representada como latitud y longitud combinadas con un radio, formando un círculo alrededor de una posición global específica. Las geovallas pueden tener desde el tamaño de un edificio hasta el de una ciudad entera. Puedes usar geovallas para desencadenar campañas en tiempo real cuando los usuarios entran y salen de sus límites, o para enviar campañas de seguimiento horas o días después.

{% alert tip %}
Para un recorrido guiado, consulta el curso de Braze Learning [Create a Geofence](https://learning.braze.com/create-a-geofence).
{% endalert %}

## Cómo funciona

Las geovallas se organizan en conjuntos de geovallas: un grupo de geovallas que puedes usar para segmentar o interactuar con los usuarios en toda la plataforma. Cada conjunto de geovallas puede contener un máximo de 10 000 geovallas. Puedes crear o cargar un número ilimitado de geovallas.

Los usuarios que entran o salen de tus geovallas añaden una nueva capa de datos de usuario que puedes usar para la segmentación y la reorientación.

Ten en cuenta los siguientes límites de dispositivo:

- Las aplicaciones de Android pueden almacenar hasta 100 geovallas localmente a la vez. Braze está configurado para almacenar solo hasta 20 geovallas localmente por aplicación.
- Los dispositivos iOS pueden monitorear hasta 20 geovallas a la vez por aplicación. Braze monitorea hasta 20 ubicaciones si hay espacio disponible.
- Si el usuario es elegible para recibir más de 20 geovallas, Braze descarga la cantidad máxima de ubicaciones en función de la proximidad al usuario en el momento del inicio de la sesión.
- Para que las geovallas funcionen correctamente, asegúrate de que tu aplicación no esté utilizando todos los puntos de geovalla disponibles.

La siguiente tabla describe los términos comunes de geovallado:

| Término | Descripción |
|---|---|
| Latitud y longitud | El centro geográfico de la geovalla. |
| Radio | El radio de la geovalla en metros, medido desde el centro geográfico. Establece un radio mínimo de 100 metros a 150 metros para todas las geovallas. |
| Tiempo de espera | Los usuarios reciben notificaciones desencadenadas por geovallas tras realizar transiciones de entrada o salida en geovallas individuales. Después de que se produzca una transición, hay un período predefinido durante el cual ese usuario no puede volver a realizar la misma transición en esa geovalla individual. Este "tiempo de espera" está predefinido por Braze y su objetivo principal es evitar solicitudes de red innecesarias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos previos

### Requisitos de SDK y plataforma

Las campañas desencadenadas por geovallas están disponibles en iOS y Android. Para admitir geovallas, se requiere lo siguiente:

* Tu integración debe soportar notificaciones push en segundo plano.
* Las geovallas de Braze o la recopilación de ubicaciones deben estar habilitadas.
* El usuario debe conceder acceso de ubicación "Permitir siempre".

{% alert important %}
La recopilación de ubicaciones de Braze está desactivada de forma predeterminada. Para verificar que está habilitada en Android, confirma que `com_braze_enable_location_collection` está configurado como `true` en tu `braze.xml`.
{% endalert %}

Para instrucciones de configuración específicas por plataforma, consulta [Geovallas]({{site.baseurl}}/developer_guide/geofences/) en la guía del desarrollador.

### Permisos de ubicación

Antes de que tus geovallas puedan funcionar, los usuarios deben conceder a tu aplicación permiso para acceder a su ubicación. Comprender los diferentes niveles de permisos y su impacto en el geovallado es fundamental para construir una estrategia efectiva basada en ubicación.

## Comprender los permisos de ubicación

Tanto iOS como Android ofrecen múltiples niveles de acceso a la ubicación. El nivel de permiso que un usuario concede afecta directamente si el geovallado funciona y qué tan precisos son los datos de ubicación.

### Niveles de permisos

{% tabs local %}
{% tab iOS %}

| Permiso | Descripción | Soporte de geovallado |
|---|---|---|
| **Permitir una vez** | Concede acceso a la ubicación para una sola sesión. El aviso reaparece la próxima vez que el usuario abre la aplicación. | No. El seguimiento en segundo plano está desactivado, por lo que el dispositivo solo recibe actualizaciones de ubicación cuando la aplicación está abierta. |
| **Permitir mientras se usa la aplicación** | Concede acceso a la ubicación siempre que la aplicación esté en primer plano. Después de conceder esto, iOS puede presentar un aviso de seguimiento preguntando al usuario si desea actualizar a "Permitir siempre". | Sí. iOS habilita el monitoreo de ubicación en segundo plano, incluidas las transiciones de geovallas, para aplicaciones con este permiso. |
| **Permitir siempre** | Concede acceso continuo a la ubicación, incluso en segundo plano y cuando la aplicación está cerrada. | Sí. Esto proporciona el monitoreo de geovallas más fiable. |
| **No permitir** | Deniega todo acceso a la ubicación. | No. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Android %}

| Permiso | Descripción | Soporte de geovallado |
|---|---|---|
| **Mientras se usa la aplicación** | Concede acceso a la ubicación mientras la aplicación está en primer plano. | No. En Android, se requiere acceso a la ubicación en segundo plano para el monitoreo de geovallas. |
| **Permitir siempre** | Concede acceso continuo a la ubicación, incluso en segundo plano. En Android 10 y versiones posteriores, esto requiere un aviso separado después de que se conceda el permiso inicial "Mientras se usa la aplicación". | Sí. Esto es obligatorio para el geovallado en Android. |
| **No permitir** | Deniega todo acceso a la ubicación. En Android 13 y versiones posteriores, si un usuario deniega el aviso de ubicación dos veces, el sistema operativo bloquea los avisos posteriores dentro de la aplicación. | No. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### Ubicación precisa frente a aproximada

En iOS 14+ y Android 12+, los usuarios pueden elegir entre ubicación precisa y aproximada.

| Configuración | Precisión | Impacto en el geovallado |
|---|---|---|
| **Ubicación precisa (activada)** | Precisión en el rango de 5 metros a 50 metros, usando GPS, Wi-Fi y triangulación celular. | Las geovallas funcionan como se espera. Recomendado para todos los casos de uso basados en geovallas. |
| **Ubicación aproximada (desactivada)** | Precisión de aproximadamente 3 kilómetros cuadrados (aproximadamente 1 milla cuadrada). El dispositivo devuelve un área general en lugar de coordenadas exactas. | Las geovallas no se desencadenan de forma fiable. El dispositivo no puede determinar con precisión si un usuario está dentro o fuera del límite de una geovalla. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para que el geovallado funcione de forma fiable, los usuarios deben habilitar la ubicación precisa. Incluye esta orientación en tu mensaje previo de permisos de ubicación para que los usuarios comprendan por qué la ubicación precisa es importante.
{% endalert %}

## Configurar un mensaje previo de permisos de ubicación

Un mensaje previo de permisos de ubicación es un mensaje dentro de la aplicación que explica el valor de compartir datos de ubicación antes de que el usuario vea el aviso nativo de permisos del sistema operativo. Dado que el aviso nativo de ubicación solo se puede mostrar una vez (en iOS) o un número limitado de veces (en Android), preparar a los usuarios con anticipación aumenta las tasas de adhesión voluntaria.

### Paso 1: Trabaja con tu equipo de desarrollo

Dado que los mensajes dentro de la aplicación de Braze no incluyen una acción de botón integrada para invocar el aviso nativo de permisos de ubicación, tu equipo de desarrollo necesita gestionar los permisos de ubicación en el lado del dispositivo. Antes de crear el mensaje dentro de la aplicación en Braze, coordínate con tu equipo de desarrollo para configurar vínculos profundos que tu mensaje dentro de la aplicación pueda llamar. La implementación específica depende de la arquitectura de tu aplicación, pero los enfoques comunes incluyen:

- Un vínculo profundo que desencadena el aviso nativo de permisos de ubicación desde dentro de tu aplicación.
- Un vínculo profundo que abre la página de configuración de ubicación de la aplicación en los ajustes del sistema operativo del dispositivo, lo cual es útil para volver a solicitar permisos a usuarios que previamente los denegaron o limitaron.

Para más información sobre vínculos profundos, consulta [Vinculación en profundidad a contenido dentro de la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/). Para orientación específica por plataforma sobre la integración de ubicación y geovallas, consulta [Geovallas]({{site.baseurl}}/developer_guide/geofences/) en la guía del desarrollador.

### Paso 2: Crea el mensaje previo de ubicación dentro de la aplicación

Crea una campaña de mensaje dentro de la aplicación que explique el valor del acceso a la ubicación. Todos los tipos de mensajes dentro de la aplicación admiten esta adhesión voluntaria, incluido el de arrastrar y soltar.

1. Ve a **Mensajería** > **Campañas**, luego selecciona **Crear campaña** > **Mensaje dentro de la aplicación**.
2. Elige un tipo de mensaje y diseño. Un diseño **Modal** o **Completo** te da más espacio para articular los beneficios.
3. Escribe un mensaje que explique claramente por qué el acceso a la ubicación beneficia al usuario. Por ejemplo:
    - "Habilita la ubicación para recibir notificaciones sobre ofertas cerca de ti."
    - "Activa la ubicación para que podamos avisarte cuando tu pedido esté listo para recoger en tu tienda más cercana."
4. Añade un botón principal de llamada a la acción (como **Activar ubicación**) y configura su comportamiento al hacer clic como **Vínculo profundo a la aplicación**, usando el vínculo profundo que tu equipo de desarrollo creó para desencadenar el aviso nativo de ubicación.
5. Añade un botón secundario (como **Ahora no**) que cierre el mensaje.

### Paso 3: Dirige a la audiencia adecuada

Para obtener los mejores resultados, muestra el mensaje previo de ubicación cuando los usuarios estén interactuando y sea probable que vean valor en compartir su ubicación.

- **Dirige a usuarios que aún no han concedido acceso a la ubicación.** Trabaja con tu equipo de desarrollo para determinar la mejor manera de rastrear y segmentar usuarios según su estado de permisos de ubicación.
- **Programa el mensaje previo después de una acción de alto valor,** como completar una compra, guardar una tienda como favorita o explorar eventos cercanos. Los usuarios tienen más probabilidades de aceptar cuando comprenden el beneficio.
- **Evita mostrar el mensaje previo en el primer inicio.** Espera hasta que los usuarios hayan experimentado suficiente valor de la aplicación como para querer una experiencia más personalizada.

### Paso 4: Fomenta el nivel de permiso recomendado

Tu mensaje previo debe animar a los usuarios a conceder el nivel de permiso que habilita el geovallado:

- **En iOS,** anima a los usuarios a seleccionar **Permitir mientras se usa la aplicación** como mínimo. iOS puede solicitar posteriormente al usuario que actualice a **Permitir siempre** por su cuenta. También puedes hacer un seguimiento con una campaña separada para explicar por qué "Permitir siempre" proporciona la mejor experiencia.
- **En Android,** anima a los usuarios a conceder **Permitir siempre**. En Android 10 y versiones posteriores, el usuario primero debe conceder "Mientras se usa la aplicación" y luego conceder "Permitir siempre" en un aviso de seguimiento separado. Guíalos a través de ambos pasos.

En ambos casos, recuerda a los usuarios que mantengan la **Ubicación precisa** activada para la mejor experiencia.

## Redirigir a los usuarios a los ajustes del sistema operativo

Si un usuario previamente denegó el acceso a la ubicación o seleccionó un permiso limitado, no puedes desencadenar el aviso nativo de nuevo desde dentro de la aplicación en la mayoría de las versiones del sistema operativo. En su lugar, dirígelos a actualizar sus permisos en los ajustes del dispositivo.

Usa un vínculo profundo dentro de un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) personalizado para llevar al usuario a la página de configuración de ubicación de la aplicación en el sistema operativo. Tu equipo de desarrollo puede configurar un vínculo profundo para esto como parte de la gestión de permisos de ubicación de tu aplicación (consulta el [Paso 1](#step-1-work-with-your-development-team)).

Al crear este mensaje dentro de la aplicación, ten en cuenta lo siguiente:

- **Cuándo mostrarlo:** Dirige a usuarios que tienen el permiso "Mientras se usa la aplicación" cuando necesitas "Permitir siempre", o a usuarios que previamente denegaron el acceso a la ubicación.
- **Ejemplo de mensaje:** "Para aprovechar al máximo las características basadas en ubicación, actualiza tu configuración de ubicación a 'Permitir siempre'. Toca abajo para ir a Ajustes."

{% alert tip %}
Puedes desencadenar este mensaje dentro de la aplicación en cualquier punto del recorrido del usuario: después de una compra, al explorar contenido cercano o como parte de un flujo de Canvas. Sé selectivo al volver a solicitar: limita estas campañas a usuarios leales o muy comprometidos para evitar la fatiga de adhesión voluntaria.
{% endalert %}

## Ejemplos de estrategias de preparación de ubicación

### Mensaje previo "Mientras se usa la aplicación"

Una aplicación de comercio minorista muestra un mensaje modal dentro de la aplicación después de que un usuario guarda una tienda como favorita:

- **Encabezado:** "Recibe notificaciones sobre ofertas en tienda"
- **Cuerpo:** "Activa la ubicación para que podamos enviarte ofertas exclusivas cuando estés cerca de tus tiendas favoritas. Tu ubicación solo se consulta mientras usas la aplicación."
- **CTA:** **Activar ubicación** vincula en profundidad al aviso nativo de permisos de ubicación
- **Descartar:** **Quizás después** cierra el mensaje

Este enfoque es efectivo porque el usuario ya ha expresado interés en una tienda específica, creando un contexto natural para la solicitud de permisos de ubicación.

### Seguimiento de "Permitir siempre"

Después de que un usuario concede el permiso "Mientras se usa la aplicación", muestra un mensaje de seguimiento dentro de la aplicación durante la siguiente sesión:

- **Encabezado:** "No te pierdas ninguna oferta cercana"
- **Cuerpo:** "Actualiza tu configuración de ubicación a 'Siempre' para que podamos notificarte sobre ofertas incluso cuando no estés navegando en la aplicación. Solo enviaremos alertas relevantes cuando estés cerca de ubicaciones participantes."
- **CTA:** **Actualizar ajustes** vincula en profundidad a la página de configuración de ubicación de la aplicación en el sistema operativo
- **Descartar:** **Mantener configuración actual** cierra el mensaje

Este seguimiento le da al usuario contexto sobre por qué actualizar a "Permitir siempre" proporciona valor adicional más allá del nivel de permiso inicial.

## Crear geovallas manualmente

### Paso 1: Crear un conjunto de geovallas

Para crear una geovalla, primero debes crear un conjunto de geovallas.

1. Ve a **Audiencia** > **Ubicaciones** en el panel de Braze.
2. Selecciona **Crear conjunto de geovallas**.
3. En **Nombre del conjunto**, introduce un nombre para tu conjunto de geovallas.
4. (Opcional) Añade etiquetas para filtrar tu conjunto.

### Paso 2: Añadir las geovallas

A continuación, añade geovallas a tu conjunto de geovallas.

1. Selecciona **Dibujar geovalla** para hacer clic y arrastrar el círculo sobre el mapa. Repite el proceso para añadir más geovallas a tu conjunto según sea necesario.
2. (Opcional) Selecciona **Editar** y sustituye la descripción de la geovalla por un nombre.
3. Selecciona **Guardar conjunto de geovallas** para guardar.

{% alert tip %}
Crea geovallas con un radio de al menos 200 metros para una funcionalidad óptima. Para más información, consulta [Mejores prácticas de geovallas](#geofence-best-practices).
{% endalert %}

![Un conjunto de geovallas con dos geovallas "EastCoastGreaterNY" y "WesternRegion" con dos círculos en el mapa.]({% image_buster /assets/img/geofence_example.png %})

## Carga masiva de geovallas {#creating-geofence-sets-via-bulk-upload}

Puedes cargar geovallas de forma masiva como un objeto GeoJSON de tipo `FeatureCollection`. Cada geovalla es un tipo de geometría `Point` en la colección de características. Las propiedades de cada característica requieren una clave `radius` y una clave opcional `name` para cada geovalla.

Para cargar tu archivo JSON, selecciona **Más** > **Cargar JSON**.

Al crear tus geovallas, ten en cuenta los siguientes detalles:

- El valor `coordinates` en GeoJSON tiene el formato `[Longitude, Latitude]`.
- El radio máximo de la geovalla que se puede cargar es de 10 000 metros (unos 10 kilómetros o 6,2 millas).

### Ejemplo

El siguiente ejemplo muestra el formato GeoJSON correcto para especificar dos geovallas: una para la sede central de Braze en Nueva York y otra para la Estatua de la Libertad, al sur de Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Usar eventos de geovallas

Una vez configuradas las geovallas, puedes usarlas para mejorar y enriquecer la forma en que te comunicas con tus usuarios.

### Desencadenar campañas y Canvas

Para usar datos de geovallas como parte de los desencadenantes de campañas y Canvas, elige **Entrega basada en acciones** como método de entrega. A continuación, añade una acción desencadenante de `Trigger a Geofence`. Por último, elige el conjunto de geovallas y los tipos de eventos de transición de geovalla para tu mensaje. También puedes hacer avanzar a los usuarios a través de un Canvas mediante eventos de geovalla.

![Una campaña basada en acciones con una geovalla que se desencadenará cuando un usuario entre en los aeropuertos alemanes.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizar mensajes

Para usar datos de geovallas para personalizar un mensaje, puedes utilizar la siguiente sintaxis de personalización de Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Actualizar los conjuntos de geovallas

El SDK de Braze solicita geovallas solo una vez al día al iniciar la sesión. Si realizas cambios en los conjuntos de geovallas después del inicio de la sesión, necesitas esperar 24 horas desde el momento en que los conjuntos se descargaron por primera vez para recibir el conjunto actualizado.

Si el usuario tiene push en segundo plano habilitado, Braze envía un push silencioso cada 24 horas cuando se actualizan los conjuntos de geovallas para descargar las ubicaciones más recientes al dispositivo.

{% alert note %}
Si las geovallas no se cargan en el dispositivo localmente, el usuario no puede desencadenar la geovalla aunque entre en el área.
{% endalert %}

## Mejores prácticas de geovallas

### Configuración de geovallas

- Usa un radio de 200 metros o más para un desencadenamiento fiable.
- Evita configurar geovallas que se superpongan o estén anidadas unas dentro de otras, ya que esto puede causar problemas con el desencadenamiento.
- Una geovalla puede desencadenar un evento de entrada solo una vez cada seis horas. Este período de espera se aplica localmente. Si un usuario desinstala la aplicación o borra los datos de la aplicación, todos los tiempos de espera se reinician.
- No se pueden almacenar más de 20 geovallas en total en un dispositivo. Si el usuario es elegible para más de 20, Braze descarga las ubicaciones más cercanas en función de la proximidad al iniciar la sesión o durante la actualización por push silencioso.
- Braze solo envía geovallas dentro de un radio de 2000 kilómetros del usuario al dispositivo.

### Requisitos del dispositivo

- Los permisos de push y los permisos de ubicación deben estar habilitados para la aplicación.
- Se requiere un token de push en primer plano válido.

{% alert note %}
La integración básica del SDK solo habilita el seguimiento de ubicación. El geovallado requiere pasos de configuración adicionales tanto para iOS como para Android. Para más detalles, consulta [Geovallas]({{site.baseurl}}/developer_guide/geofences/) en la guía del desarrollador.
{% endalert %}

También puedes usar geovallas con socios tecnológicos de Braze, como [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) y [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/).

## Preguntas frecuentes

### ¿Cuál es la diferencia entre geovallas y seguimiento de ubicación?

En Braze, una geovalla es un concepto diferente del seguimiento de ubicación. Las geovallas se usan como desencadenantes de determinadas acciones: cuando un usuario entra o sale de un límite virtual establecido alrededor de una ubicación geográfica, puede desencadenar una acción específica, como el envío de un mensaje.

El seguimiento de ubicación recopila y almacena los datos de ubicación más recientes de un usuario. Estos datos pueden usarse para segmentar usuarios en función del filtro `Most Recent Location`. Por ejemplo, podrías usar el filtro `Most Recent Location` para dirigirte a usuarios ubicados en Nueva York.

Para más información, consulta [Seguimiento de ubicación]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### ¿Qué grado de precisión tienen las geovallas de Braze?

Las geovallas de Braze utilizan una combinación de todos los proveedores de ubicación disponibles en un dispositivo para triangular la ubicación del usuario, incluyendo Wi-Fi, GPS y torres de telefonía móvil.

La precisión típica está en el rango de 20 metros a 50 metros, y la mejor precisión está en el rango de 5 metros a 10 metros. En zonas rurales, la precisión puede degradarse significativamente, pudiendo llegar a varios kilómetros. Crea geovallas con radios mayores en ubicaciones rurales.

La precisión también depende de si el usuario tiene la ubicación precisa habilitada. Con solo la ubicación aproximada, la precisión baja a aproximadamente 3 kilómetros cuadrados, lo que hace que las geovallas no sean fiables. Para más información, consulta [Ubicación precisa frente a aproximada](#precise-versus-approximate-location).

### ¿Cómo afectan las geovallas a la duración de la batería?

El geovallado de Braze utiliza el servicio nativo de geovallado del sistema en iOS y Android. Está optimizado para equilibrar de forma inteligente la precisión y el consumo energético, ahorrando batería y mejorando el rendimiento a medida que mejora el servicio subyacente.

### ¿Cuándo están activas las geovallas?

Las geovallas de Braze funcionan a cualquier hora del día, incluso cuando tu aplicación está cerrada. Se activan en cuanto se definen y se cargan en el panel de Braze. Sin embargo, las geovallas no pueden funcionar si un usuario ha desactivado el seguimiento de ubicación.

Para que las geovallas funcionen, los usuarios deben tener los servicios de ubicación habilitados en su dispositivo y deben haber concedido a tu aplicación el nivel de permiso de ubicación requerido. Para más información, consulta [Comprender los permisos de ubicación](#understanding-location-permissions).

### ¿Se almacenan los datos de la geovalla en los perfiles de usuario?

No, Braze no almacena datos de geovallas en los perfiles de usuario. Las geovallas son monitoreadas por los servicios de ubicación de Apple y Google, y Braze solo recibe una notificación cuando un usuario desencadena una geovalla. En ese momento, Braze procesa cualquier campaña desencadenante asociada.

### ¿Puedo configurar una geovalla dentro de una geovalla?

Como práctica recomendada, evita configurar geovallas que se superpongan entre sí, ya que esto puede causar problemas con el desencadenamiento de notificaciones.

### ¿Qué pasa si un usuario deniega el acceso a la ubicación?

Tu equipo de desarrollo puede configurar un vínculo profundo que abra la página de configuración de ubicación de la aplicación en el sistema operativo, donde los usuarios pueden actualizar sus permisos. Puedes usar este vínculo profundo dentro de un mensaje personalizado dentro de la aplicación en cualquier punto del recorrido del usuario. Sé selectivo sobre cuándo muestras este mensaje: dirige a usuarios que estén comprometidos o que hayan realizado una acción de alto valor para aumentar la probabilidad de adhesión voluntaria. Para más información, consulta [Redirigir a los usuarios a los ajustes del sistema operativo](#redirecting-users-to-os-settings).