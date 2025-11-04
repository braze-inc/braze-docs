---
nav_title: "Cuestionario sencillo"
article_title: Mensaje dentro de la aplicación del cuestionario simple
page_order: 1.5
page_type: reference
description: "Este artículo de referencia explica cómo recopilar atributos, información y preferencias de los usuarios para potenciar tu estrategia de campaña utilizando los cuestionarios de mensajes dentro de la aplicación."
channel:
  - in-app messages
tool:
  - Templates
---

# Cuestionario sencillo

> Utiliza la plantilla de mensajes dentro de la aplicación **Encuesta simple** para recopilar atributos, información y preferencias de los usuarios que impulsen tu estrategia de campaña. 

Por ejemplo, pregunta a los usuarios cómo les gustaría utilizar tu aplicación, aprende más sobre sus preferencias personales, o incluso pregúntales sobre su satisfacción con una característica concreta.

Tres sencillos mensajes de mensajería: preferencias de notificación, preferencias dietéticas y un cuestionario de satisfacción del cliente. Las opciones seleccionadas en los cuestionarios corresponden a atributos personalizados que se registrarán para ese usuario.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos del SDK {#supported-sdk-versions}

Este mensaje dentro de la aplicación sólo se entregará a dispositivos que admitan [Flex CSS](https://caniuse.com/flexbox), y deben tener al menos las siguientes [versiones del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze.
{% endalert %}

## Crear un cuestionario {#create}

Cuando crees un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), selecciona **Encuesta simple** como **Tipo de mensaje**.

Esta plantilla de cuestionario es compatible tanto con aplicaciones móviles como con navegadores web. Recuerda comprobar que tus SDK están en las [versiones de SDK mínimas](#supported-sdk-versions) requeridas para esta característica.

### Paso 1: Añade tu pregunta del cuestionario

Para empezar a construir tu cuestionario, añade tu pregunta al campo **Encabezado** del cuestionario. Si lo deseas, puedes añadir un mensaje opcional **en el cuerpo** que aparecerá debajo de la pregunta de tu cuestionario.

\![Pestaña Componer del editor de cuestionarios simples, con campos para un encabezado, un cuerpo opcional y un texto de ayuda opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Estos campos pueden incluir tanto Liquid como emojis, ¡así que ponte elegante!
{% endalert %}

### Paso 2: Configurar opciones {#single-multiple-choice}

Puedes añadir hasta 12 opciones en un cuestionario.

Elige entre **Selección simple** o **Selección múltiple**. El **texto de ayuda** se actualizará automáticamente cuando cambies entre las dos opciones para que los usuarios sepan cuántas opciones pueden seleccionar. 

A continuación, determina si vas a [recoger atributos personalizados](#custom-attributes) o [sólo respuestas de registro](#no-attributes).

\![Lista desplegable de opciones con la opción "Registrar atributos al enviar" seleccionada.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Recoger atributos personalizados {#custom-attributes}

Selecciona **Registrar atributos en el envío** para recopilar atributos basados en el envío del usuario. Puedes utilizar esta opción para crear nuevos segmentos y campañas de reorientación. Por ejemplo, en un [cuestionario de satisfacción](#user-satisfaction), podrías enviar un correo electrónico de seguimiento a todos los usuarios que no estuvieran contentos.

Para añadir un atributo personalizado a cada elección, selecciona un nombre de atributo personalizado en el menú desplegable (o crea uno nuevo) y, a continuación, introduce el valor que se establecerá cuando se envíe esta elección. También puedes crear un nuevo atributo personalizado en tu [página de configuración]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

El tipo de datos de tus atributos personalizados importa en función de cómo hayas configurado tu cuestionario.

- **Selección múltiple:** El tipo de datos del atributo personalizado debe ser una matriz. Si el atributo personalizado se establece en un tipo de datos diferente, las respuestas no se registrarán.
- **Selección de una sola opción:** El tipo de datos del atributo personalizado _no debe_ ser una matriz. Las respuestas no se registrarán si el atributo es una matriz.

{% alert important %}
Cuando se habilita la recopilación de atributos personalizados, las elecciones que compartan el mismo nombre de atributo personalizado se combinarán en una matriz.
{% endalert %}

##### Ejemplo 

Por ejemplo, en un [cuestionario de preferencias de notificación](#notification-preferences), puedes hacer que cada opción sea un atributo booleano (verdadero/falso) para que los usuarios puedan seleccionar los temas que les interesan. Si un usuario marca la opción "Promociones", se actualizará su [perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) con el atributo personalizado `Promotions Topic` establecido en `true`. Si dejan la opción sin marcar, ese mismo atributo permanecerá inalterado.

A continuación, puedes utilizar el filtro `Custom Attribute` para crear un segmento de usuarios con el atributo personalizado `Promotions Topic` `is` `true`, para asegurarte de que sólo los usuarios interesados en tus promociones recibirán las campañas pertinentes.

#### Sólo registro de respuestas {#no-attributes}

También puedes elegir **Registrar sólo las respuestas (sin atributos)**. Cuando se selecciona esta opción, las respuestas a los cuestionarios se registran como clics en los botones, pero los atributos personalizados no se registran en el perfil del usuario. Esto significa que puedes seguir viendo las métricas de clics de cada opción del cuestionario (ver [Análisis](#analytics)), pero esa elección no se reflejará en su perfil de usuario.

Estas métricas de clics no están disponibles para reorientar.

### Paso 4: Elige el comportamiento de sumisión

Una vez que el usuario envía su respuesta, puedes mostrar opcionalmente una página de confirmación, o simplemente cerrar el mensaje.

Una página de confirmación es un buen lugar para agradecer a los usuarios su tiempo o proporcionar información adicional. Puedes personalizar la llamada a la acción de esta página para guiar a los usuarios a otra página de tu aplicación o sitio web.

Edita el texto del botón y el comportamiento al hacer clic en la sección **Botón de envío**, en la parte inferior de la pestaña **Encuesta**:

\![Comportamiento al hacer clic establecido en "Enviar respuestas y mostrar página de confirmación".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si decides añadir una página **de** confirmación, pasa a la pestaña **Página de confirmación** para personalizar tu mensaje:

\![Pestaña Página de confirmación del editor de cuestionarios simples. Los campos disponibles son cabecera, cuerpo opcional, texto del botón y comportamiento del botón al hacer clic.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Si quieres guiar a los usuarios a otra página de tu aplicación o sitio web, cambia el **comportamiento Al hacer clic** del botón.

### Paso 5: Estiliza tu mensaje (opcional) {#styling}

Puedes personalizar el color de la fuente y el color de acento del mensaje utilizando el selector **Tema de color**.

\![Pestaña Componer del editor de cuestionarios simples con el selector Tema de color expandido después de que un usuario haya hecho clic en la paleta de colores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analiza los resultados {#analytics}

Una vez lanzada tu campaña, puedes analizar los resultados en tiempo real para ver el desglose de cada elección seleccionada. Si has habilitado [la recogida de atributos personalizada](#custom-attributes), también podrás crear nuevos segmentos o campañas de seguimiento para los usuarios que hayan enviado el cuestionario.

{% alert note %}
Las opciones de cuestionario eliminadas seguirán apareciendo en los análisis, pero no se mostrarán como opción a los nuevos usuarios.
{% endalert %}

Puedes encontrar las métricas de rendimiento de tu cuestionario ampliando el desplegable **Resultados** de una variante específica en la sección **Rendimiento de los mensajes dentro de la aplicación** del análisis. Aquí tienes un desglose de lo que verás:

- **La interacción con el** cuestionario muestra cómo interactuaron los usuarios con el cuestionario en general, incluyendo el total de envíos, rechazos y clics dentro del cuerpo del mensaje.
- **Los resultados del cuestionario** muestran un desglose de cuántos usuarios seleccionaron cada opción de respuesta, junto con el porcentaje de envíos totales que representa cada opción.
- **Las métricas de la página de confirmación** (si están habilitadas) incluyen cuántos usuarios vieron la pantalla de confirmación, hicieron clic en su botón o la abandonaron sin interactuar.

Para las definiciones de las métricas de los cuestionarios, consulta el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtra por "Mensaje dentro de la aplicación".

Consulta [los informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para obtener un desglose de las métricas de tu campaña.

### Currents {#currents}

Las opciones seleccionadas pasarán automáticamente a Currents, en la sección [**Eventos de clic en mensajes dentro de la aplicación**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` . Cada elección se enviará con su identificador único universal (UUID).

## Casos de uso

{% tabs %}
{% tab User satisfaction %}

### Satisfacción del usuario

**Objetivo:** Mide la satisfacción del cliente y envía campañas de recuperación a los usuarios que dejaron puntuaciones bajas.

Para configurarlo, utiliza un cuestionario de selección de una sola opción con cinco opciones que vayan de "😡 Muy insatisfecho" a "😍 Muy satisfecho". Cada elección está mapeada en el atributo personalizado `customer_satisfaction`, con un valor numérico de 1 a 5 -donde 1 indica el menos satisfecho y 5 el más satisfecho-.

| Elección                                | Atributo              | Valor |
|---------------------------------------|------------------------|-------|
| 😡 Muy insatisfecho                  | `customer_satisfaction` | 1     |
| 😟 Insatisfecho                       | `customer_satisfaction` | 2     |
| 🙂 Ni satisfecho ni insatisfecho | `customer_satisfaction` | 3     |
| 😊 Satisfecho                          | `customer_satisfaction` | 4     |
| 😍 Muy satisfecho                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario envía el cuestionario, su valor seleccionado se registra como un atributo personalizado. A continuación, puedes crear campañas de seguimiento utilizando filtros de audiencia. Por ejemplo, dirige mensajes de recuperación a usuarios cuyo atributo `customer_satisfaction` sea 1 ó 2.

{% endtab %}
{% tab Notification preferences %}

### Preferencias de notificación

**Objetivo:** Deja que los usuarios opten por tipos específicos de notificaciones.

Para configurarlo, utiliza un cuestionario de selección múltiple en el que cada opción represente un tema de notificación. En lugar de asignar el mismo atributo con valores distintos, cada elección mapea un atributo booleano distinto que refleja el interés del usuario por ese tema. Si un usuario selecciona una opción, el atributo correspondiente se establece en `true`. Si no se selecciona, el atributo no se modifica.

| Elección             | Atributo              | Valor  |
|--------------------|------------------------|--------|
| Actualizaciones de productos    | `wants_product_updates`| `true` |
| Promociones         | `wants_promotions`     | `true` |
| Invitaciones a eventos      | `wants_event_invites`  | `true` |
| Cuestionarios & Opiniones | `wants_surveys`        | `true` |
| Consejos & Tutoriales   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Identificar los objetivos del cliente

**Objetivo:** Identifica las principales razones por las que los usuarios visitan tu aplicación.

Para configurarlo, utiliza un cuestionario de selección de una sola opción, en el que cada opción represente un objetivo o intención común. Cada elección se mapea en el atributo personalizado `product_goal` con un valor correspondiente a la intención del usuario seleccionado.

| Elección                     | Atributo       | Valor     |
|----------------------------|------------------|-----------|
| Comprobación del estado            | `product_goal`   | `status`  |
| Actualizar mi cuenta       | `product_goal`   | `upgrade` |
| Programar una cita  | `product_goal`   | `schedule`|
| Atención al cliente           | `product_goal`   | `support` |
| Navegando              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario envía el cuestionario, el valor seleccionado se registra como un atributo personalizado en su perfil. A continuación, puedes utilizar estos datos para personalizar futuras experiencias o segmentar a los usuarios en función de su objetivo principal.

{% endtab %}
{% tab Improve conversion rates %}

### Mejorar las tasas de conversión

**Objetivo:** Comprende por qué los clientes no actualizan o no compran.

Para configurarlo, utiliza un cuestionario de selección de una sola opción, en el que cada opción represente una barrera común a la mejora. Cada elección se mapea en el atributo personalizado `upgrade_reason` con un valor correspondiente que refleja la selección del usuario.

| Elección              | Atributo        | Valor       |
|---------------------|------------------|-------------|
| Demasiado caro       | `upgrade_reason` | `expensive` |
| Sin valor        | `upgrade_reason` | `value`     |
| Difícil de usar    | `upgrade_reason` | `difficult` |
| Utilizar un competidor  | `upgrade_reason` | `competitor`|
| Otro motivo        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario envía el cuestionario, el valor seleccionado se guarda en su perfil. A continuación, puedes dirigirte a estos usuarios con campañas adaptadas a su objeción específica, como ofertas de descuento o mejoras de usabilidad.

{% endtab %}
{% tab Favorite features %}

### Características favoritas

**Objetivo:** Comprende qué características disfrutan utilizando los clientes.

Para configurarlo, utiliza un cuestionario de selección múltiple en el que cada opción represente una característica de tu aplicación. Cada elección se mapea en el atributo personalizado `favorite_features`, y cuando el usuario envía el cuestionario, el atributo se establece en una matriz de los valores seleccionados.

| Elección            | Atributo          | Valor        |
|-------------------|--------------------|--------------|
| Marcadores         | `favorite_features`| `bookmarks`  |
| Aplicación móvil        | `favorite_features`| `mobile`     |
| Compartir publicaciones     | `favorite_features`| `sharing`    |
| Atención al cliente  | `favorite_features`| `support`    |
| Personalización     | `favorite_features`| `custom`     |
| Precio / Valor     | `favorite_features`| `value`      |
| Comunidad         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Como este cuestionario utiliza la selección múltiple, el perfil del usuario se actualizará con una lista de todos los valores de características seleccionados.

{% endtab %}
{% endtabs %}
