---
nav_title: Survicate
article_title: Survicate
description: "Este artículo de referencia describe la asociación entre Braze y Survicate, una plataforma de opiniones de clientes que te ayuda a recopilar, analizar y actuar sobre la información de los clientes en múltiples canales y a lo largo del recorrido del usuario."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) es una plataforma de opiniones de clientes que recopila, analiza y actúa sobre la información de los clientes a través de múltiples canales y durante todo el recorrido del usuario. [Ver una demostración rápida](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Esta integración está mantenida por Survicate._

## Sobre la integración

Utiliza la integración nativa de Survicate y Braze para sincronizar las respuestas de las encuestas por correo electrónico, aplicación, móvil o Web con los perfiles de cliente de Braze. Las respuestas a los cuestionarios se sincronizan automáticamente con los perfiles de usuario Braze como atributos o eventos personalizados. La información sobre las opiniones en tiempo real facilita el seguimiento y el análisis de las opiniones junto con los datos de clientes y la creación de seguimientos de objetivos y segmentos hiperpersonalizados. 

## Ejemplos

Braze y Survicate trabajan juntos para cubrir una amplia gama de casos de uso, ayudándote a recopilar información accionable de los usuarios y a mejorar la experiencia del cliente:

- Mejora las tasas de respuesta de los cuestionarios con encuestas incrustadas que puedan responderse desde un buzón de entrada de correo electrónico. 
- Obtén información en las fases críticas del recorrido del cliente a través del mensaje dentro de la aplicación Braze. 
- Utiliza la información almacenada en Survicate para crear segmentos más inteligentes en Braze. 
- Automatiza campañas de seguimiento basadas en las opiniones de los clientes. 
- Utiliza la información de los clientes para desencadenar flujos de trabajo personalizados. 
- Llega a una audiencia más amplia con cuestionarios traducidos automáticamente.
- Envía eventos a los perfiles de contacto de Braze cuando alguien responda a tu cuestionario

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Survicate | Necesitas una cuenta de Survicate para activar esta integración. |
| Clave de API REST de Braze | Una clave de API REST de Braze con el permiso `users.track`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **API e identificadores**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Características principales de la integración

La integración de Survicate y Braze ofrece sincronización de datos en tiempo real, por lo que la información más actualizada de los cuestionarios de Survicate está disponible inmediatamente en Braze. Basándote en las respuestas a los cuestionarios, puedes utilizar estos datos para emprender acciones oportunas y personalizadas.

- **Envía las respuestas de los cuestionarios a Braze como atributos personalizados de usuario**: Enriquece los perfiles de usuario de Braze con datos procedentes de respuestas a cuestionarios.
- **Desencadena eventos personalizados en Braze**: Utiliza eventos basados en respuestas a cuestionarios para dirigirte a grupos específicos o iniciar campañas de seguimiento.
- **Construye segmentos detallados**: Crea segmentos Braze utilizando los datos de los cuestionarios Survicate para personalizar aún más tu alcance.

## Integración

### Crea tus cuestionarios en Survicate

#### Incrusta tu cuestionario en un correo electrónico o crea una encuesta con un enlace que se pueda compartir 

1.  En Survicate, haz clic en **\+ Crear nueva encuesta**, selecciona cualquier método de creación (una plantilla, utilizar la creación de encuestas mediante IA o añadir tus propias preguntas) y el tipo de encuesta Correo electrónico o Enlace compartible:
![Se selecciona Braze en el creador de cuestionarios.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\. En la pestaña Configurar del cuestionario, selecciona **Braze** como herramienta para identificar a los encuestados:
![Se selecciona Braze en la pestaña Configurar del cuestionario.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\. Después de configurar tu cuestionario, ve a la pestaña Compartir y decide cómo enviar tu cuestionario por correo electrónico. Hay dos opciones: puedes enviar tu **encuesta como un enlace** o **incrustar la primera pregunta en el correo electrónico** para que los encuestados empiecen a responder a la encuesta directamente desde el correo electrónico.

{% details Survey link option %}

1. Obtén un enlace a tu cuestionario desde el botón Copiar enlace de cuestionario:

![Obtén un enlace a tu cuestionario desde el botón Copiar enlace de cuestionario.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\. Oculta el enlace del cuestionario detrás de un botón CTA o hipervínculo en tu correo electrónico Braze.

![Oculta el enlace del cuestionario detrás de un botón CTA o hipervínculo en tu correo electrónico Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Muestra la primera pregunta directamente en el cuerpo del correo electrónico para iniciar el cuestionario desde el correo electrónico. A continuación, se redirige a los encuestados a una página de destino para que realicen el resto del cuestionario.

1. Haz clic en **Obtener código de correo electrónico** y, a continuación, **Copia el código HTML**:

![Obtener código de correo electrónico]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\. Ve a la campaña Braze que quieras utilizar para el cuestionario, haz clic en **Editar cuerpo del correo electrónico** y añade un bloque HTML a tu plantilla:

![Obtener código HTML de bloque]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\. Sustituye el código por el que copiaste de tu cuestionario Survicate. A continuación, verás la primera pregunta del cuestionario en la plantilla:

![Sustituye el código por el que has copiado de tu cuestionario Survicate]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4\. Programa el correo electrónico, elige tu Grupo objetivo y tu campaña estará lista para enviar.

{% enddetails %}

### Cuestionario sobre mensajes dentro de la aplicación Braze

1. Haz clic en **\+ Crear nueva encuesta**, selecciona cualquier método de creación (una plantilla, utilizar la creación de encuestas mediante IA o añadir tus propias preguntas) y, a continuación, elige Encuestas dentro de la aplicación y el tipo de encuesta Mensaje dentro de la aplicación de Braze:

![Haz clic en + Crear nuevo cuestionario, selecciona cualquier método de creación]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\. Inicia tu cuestionario de mensajes **dentro de la** aplicación Braze accediendo a tu cuenta Braze y, a continuación, a **Mensajería > Campañas > Crear campaña > Mensaje dentro de la aplicación:**
![Inicia tu cuestionario de mensajes dentro de la aplicación Braze]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Lanza tu cuestionario Braze In-App Messenger a través del editor tradicional

1. Si utilizas el editor tradicional, en Tipo de mensaje, elige **Código personalizado**:

![elegir Código personalizado]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\. A continuación, pega el código de la pestaña Inicio de tu cuestionario en el campo HTML:

![pega el código de la pestaña Inicio de tu cuestionario en el campo HTML]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze muestra mensajes dentro de la aplicación en un iframe predeterminado mientras el fondo de la aplicación está bloqueado. Para permitir la interacción con tu aplicación, mientras aparecen los cuestionarios de Survicate, debes:<br><br>

- Añade `opts.useBrazeIframeClipper = true` a tu fragmento de código Survicate-Braze.
- Instala el [paquete](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` en el archivo donde inicialices Braze y utilices la función `initBrazeBridge`.

Puedes encontrar un fragmento de código de muestra y una implementación de React [en el sitio de desarrolladores de Survicate.](https://developers.survicate.com/javascript/installation/#braze)
{% endalert %}

{: start="3"}
3\. En tu campaña Braze, configura los pasos Objetivo y Asignar. Una vez completado, tu campaña estará lista para lanzarse. En el paso Revisar, puedes ver el aspecto de la campaña. El cuestionario aparece en tu sitio web en el lugar especificado en el panel Survicate, como se ha descrito anteriormente.

### Habilitación de la integración Braze

1. Para habilitar la integración Braze, ve a **Integraciones**, busca y selecciona "Braze".

![Selecciona Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\. Haz clic en **Conectar** para configurar la autorización.

3. Introduce la clave de API del espacio de trabajo de tu cuenta Braze y la URL de la instancia de Braze:

![Introduce la clave de API del espacio de trabajo de tu cuenta Braze y la URL de la instancia de Braze]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Para conectar Survicate a Braze, la clave de API de Braze debe tener permisos `users.track`.
{% endalert %}

### Conectar tus cuestionarios a Braze

Ahora que la integración Braze está conectada, puedes establecer configuraciones individuales para cada cuestionario. Ve a tu cuestionario, selecciona la pestaña **Conectar** y elige **Braze** de la lista de integraciones disponibles.

![Ve a tu cuestionario, selecciona la pestaña Conectar y elige Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envío de respuestas a Braze como atributos personalizados

Configura las respuestas de los cuestionarios para que fluyan hacia Braze como atributos personalizados, lo que enriquece tus perfiles de usuario Braze con los datos recopilados.

1. En la pestaña Configuración de la integración Braze, multa la sección **Actualizar campos**.

![Selecciona la sección Actualizar campos]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\. Selecciona la pregunta de la que quieres actualizar los campos. Para evitar inundar de datos tus perfiles de usuario de Braze, puedes enviar respuestas sólo a las preguntas elegidas.

![Selecciona la pregunta de la que quieres actualizar los campos]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Las preguntas de Clasificación y Matriz no son compatibles con esta integración Braze.
{% endalert %}

{: start="3"}
3\. Añade el nombre del atributo personalizado que quieres actualizar en el campo **Usuario**:

![Añade el nombre del atributo personalizado que quieres actualizar en el campo Usuario]({% image_buster /assets/img/survicate/survicate_17.png %})

Por defecto, Survicate envía el contenido de una respuesta a un cuestionario como un valor de atributo. Puedes cambiar la etiqueta para hacerla más corta o ajustarla a tu estructura de datos haciendo clic en **Editar mapeado** para modificar estos valores:

![La respuesta al cuestionario como valor de atributo]({% image_buster /assets/img/survicate/survicate_18.png %})

![Haz clic en editar mapeado para modificar estos valores]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Para NPS, Survicate envía valores mapeados basados en el grupo de respuesta de la pregunta NPS®. Sin embargo, si quieres recibir valores numéricos, puedes activar Enviar respuestas como valores 0-10.
{% endalert %}

![Survicate envía valores mapeados en función del grupo de respuesta]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4\. Conecta más preguntas a tu integración haciendo clic en **\+ Añadir nuevo** y aplicando los mismos pasos.

![Conecta más preguntas a tu integración]({% image_buster /assets/img/survicate/survicate_21.png %})

### Enviar eventos a los perfiles de los contactos Braze

Aparte de la configuración anterior, cada vez que un encuestado responde a una pregunta del cuestionario, Survicate puede enviar un evento personalizado en Braze denominado `survicate-question-answered`.
En el panel Supervivencia, en Enviar respuestas como atributos personalizados, puedes elegir si quieres enviar el evento para todas las preguntas, las preguntas elegidas en la pestaña Actualizar campos, o para ninguna:

![puedes elegir si quieres enviar el evento para todas las preguntas]({% image_buster /assets/img/survicate/survicate_22.png %})

Si decides enviar los eventos, podrás ver en los perfiles de los usuarios cuántas veces han respondido a los cuestionarios de Survicate y cuándo lo hicieron por última vez:

![Respuestas ]({% image_buster /assets/img/survicate/survicate_23.png %})

El evento contiene propiedades del evento con la respuesta a la pregunta e información sobre el cuestionario, la pregunta y el encuestado. Puedes utilizar este evento para crear segmentos. Por ejemplo, crea un segmento de usuarios que hayan respondido a un cuestionario después de una fecha concreta o un número determinado de veces:

![El evento contiene propiedades del evento con la respuesta]({% image_buster /assets/img/survicate/survicate_24.png %})

También puedes utilizar estos datos al crear una campaña en Braze.

![También puedes utilizar estos datos al crear una campaña en Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Prueba la integración

Cuando tengas tu cuestionario listo y la integración configurada, puedes probarla sin salir de Survicate haciendo clic en el botón Probar integración junto a cualquier atributo, etiqueta o nueva configuración de contacto que hayas creado. Survicate crea un contacto de prueba (`braze-test@survicate.com`) en tu cuenta de Braze. El perfil del contacto incluye campos actualizados según la configuración.

![Haz clic en el botón Probar integración]({% image_buster /assets/img/survicate/survicate_26.png %})

En Braze, puedes ver datos de muestra de los campos mapeados en el Contacto ficticio Survicate:

![Datos de muestra de los campos mapeados en el contacto ficticio Survicate]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analizar los resultados de tu cuestionario

Después de recopilar respuestas a través de tu cuestionario Braze, es hora de analizar los comentarios y la información que han compartido tus encuestados. Survicate te permite revisar fácilmente los resultados, las estadísticas y las tendencias para tomar nuevas medidas.

### Retroalimentación en Survicate

Cuando tu cuestionario empiece a recoger respuestas, las verás inmediatamente en la pestaña Analizar del cuestionario.

![Respuestas en la pestaña Analizar]({% image_buster /assets/img/survicate/survicate_28.png %})

La pestaña Analizar te muestra los resultados globales con estadísticas y datos a lo largo del tiempo, así como respuestas individuales para examinar en detalle cada envío de cuestionario.

### Feedback en Braze

Si actualizas los campos de usuario con las respuestas del cuestionario o envías las respuestas como eventos personalizados, podrás ver los datos del cuestionario sincronizados en tiempo real. En Braze, ve a un contacto concreto que haya respondido a tu cuestionario. Verás tanto los datos basados en la respuesta como los eventos en la vista principal del contacto.

![datos del cuestionario sincronizados en tiempo real]({% image_buster /assets/img/survicate/survicate_29.png %}) 