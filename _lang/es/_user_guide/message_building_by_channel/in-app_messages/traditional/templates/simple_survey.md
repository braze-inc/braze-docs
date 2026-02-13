---
nav_title: "Encuesta simple"
article_title: Mensaje de cuestionario simple dentro de la aplicación
page_order: 1.5
page_type: reference
description: "Este artículo de referencia explica cómo recopilar atributos, información y preferencias de los usuarios para potenciar su estrategia de campaña mediante las encuestas de mensajes integradas en la aplicación."
channel:
  - in-app messages
tool:
  - Templates
---

# Encuesta simple

> Utilice la plantilla de mensajes de la aplicación **Simple Survey** para recopilar atributos, información y preferencias de los usuarios que impulsen su estrategia de campaña. 

Por ejemplo, pregunte a los usuarios cómo les gustaría utilizar su aplicación, conozca mejor sus preferencias personales o incluso pregúnteles por su satisfacción con una función concreta.

![Tres sencillos mensajes de encuesta: preferencias de notificación, preferencias dietéticas y una encuesta de satisfacción del cliente. Las opciones seleccionadas en los cuestionarios corresponden a atributos personalizados que se registrarán para ese usuario.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos del SDK {#supported-sdk-versions}

Este mensaje in-app sólo se enviará a los dispositivos compatibles con [Flex CSS](https://caniuse.com/flexbox), y deben tener al menos las siguientes [versiones del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze.
{% endalert %}

## Crear un cuestionario {#create}

Al crear un [mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), seleccione **Encuesta simple** como **Tipo de mensaje**.

Esta plantilla de encuesta es compatible tanto con aplicaciones móviles como con navegadores web. Recuerda comprobar que tus SDK están en las [versiones de SDK mínimas](#supported-sdk-versions) requeridas para esta característica.

### Paso 1: Añade tu pregunta del cuestionario

Para empezar a construir tu cuestionario, añade tu pregunta en el campo **Encabezado** del cuestionario. Si lo desea, puede añadir un mensaje opcional **en el cuerpo** que aparecerá debajo de la pregunta de la encuesta.

![Pestaña Componer del editor de cuestionarios simples, con campos para un encabezado, un cuerpo opcional y un texto de ayuda opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Estos campos pueden incluir tanto Liquid como emojis, ¡así que ponte elegante!
{% endalert %}

### Paso 2: Configurar opciones {#single-multiple-choice}

Puede añadir hasta 12 opciones en una encuesta.

Selecciona **Selección simple** o **Selección múltiple**. El **texto de ayuda** se actualizará automáticamente cuando cambies entre las dos opciones para que los usuarios sepan cuántas opciones pueden seleccionar. 

A continuación, determina si vas a [recoger atributos personalizados](#custom-attributes) o [sólo respuestas de registro](#no-attributes).

![Opciones desplegables con la opción "Registrar atributos al enviar" seleccionada.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Recopilar atributos personalizados {#custom-attributes}

Seleccione **Registrar atributos al enviar** para recopilar atributos basados en el envío del usuario. Puede utilizar esta opción para crear nuevos segmentos y campañas de retargeting. Por ejemplo, en un [cuestionario de satisfacción](#user-satisfaction), podrías enviar un correo electrónico de seguimiento a todos los usuarios que no estuvieran satisfechos.

Para añadir un atributo personalizado a cada opción, seleccione un nombre de atributo personalizado en el menú desplegable (o cree uno nuevo) y, a continuación, introduzca el valor que se establecerá cuando se envíe esta opción. También puedes crear un nuevo atributo personalizado en tu [página de configuración]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

El tipo de datos de sus atributos personalizados es importante dependiendo de cómo haya configurado su encuesta.

- **Selección múltiple:** El tipo de datos del atributo personalizado debe ser un array. Si el atributo personalizado se establece en un tipo de datos diferente, las respuestas no se registrarán.
- **Selección de opción simple:** El tipo de datos del atributo personalizado _no debe_ ser un array. Las respuestas no se registrarán si el atributo es una matriz.

{% alert important %}
Cuando la colección de atributos personalizados está activada, las opciones que comparten el mismo nombre de atributo personalizado se combinarán en una matriz.
{% endalert %}

##### Ejemplo 

Por ejemplo, en un [cuestionario de preferencias de notificación](#notification-preferences), puedes hacer que cada opción sea un atributo booleano (verdadero/falso) para que los usuarios puedan seleccionar los temas que les interesan. Si un usuario marca la opción "Promociones", se actualizará su [perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) con el atributo personalizado `Promotions Topic` establecido en `true`. Si dejan la opción sin marcar, ese mismo atributo permanecerá inalterado.

A continuación, puedes utilizar el filtro `Custom Attribute` para crear un segmento de usuarios con el atributo personalizado `Promotions Topic` `is` `true`, para asegurarte de que sólo los usuarios interesados en tus promociones recibirán las campañas pertinentes.

#### Sólo registro de respuestas {#no-attributes}

También puede optar por **Registrar sólo las respuestas (sin atributos)**. Cuando se selecciona esta opción, las respuestas de la encuesta se registran como clics de botón, pero los atributos personalizados no se registran en el perfil del usuario. Esto significa que puede seguir viendo las métricas de clics para cada opción de encuesta (consulte [Análisis](#analytics)), pero esa elección no se reflejará en su perfil de usuario.

Estas métricas de clics no están disponibles para el retargeting.

### Paso 4: Elija el comportamiento de sumisión

Una vez que el usuario envía su respuesta, puede mostrar opcionalmente una página de confirmación, o simplemente cerrar el mensaje.

Una página de confirmación es un buen lugar para agradecer a los usuarios su tiempo o proporcionar información adicional. Puedes personalizar la llamada a la acción de esta página para guiar a los usuarios a otra página de tu aplicación o sitio web.

Edite el texto del botón y el comportamiento al hacer clic en la sección **Botón Enviar** de la parte inferior de la pestaña **Encuesta**:

![Comportamiento al hacer clic establecido en "Enviar respuestas y mostrar página de confirmación".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si decide añadir una página de confirmación, vaya a la pestaña **Página de confirmación** para personalizar su mensaje:

![Pestaña Página de confirmación del editor de encuestas simples. Los campos disponibles son cabecera, cuerpo opcional, texto del botón y comportamiento del botón al hacer clic.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Si desea guiar a los usuarios a otra página de su aplicación o sitio web, cambie el **comportamiento Al hacer clic** del botón.

### Paso 5: Estiliza tu mensaje (opcional) {#styling}

Puede personalizar el color de la fuente y el color de acento del mensaje utilizando el selector **Tema de color**.

![Pestaña Componer del editor de cuestionarios simples con el selector Tema de color expandido después de que un usuario haya hecho clic en la paleta de colores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analizar los resultados {#analytics}

Una vez lanzada la campaña, puede analizar los resultados en tiempo real para ver el desglose de cada opción seleccionada. Si ha activado [la recopilación de atributos personalizados](#custom-attributes), también podrá crear nuevos segmentos o campañas de seguimiento para los usuarios que hayan enviado la encuesta.

{% alert note %}
Las opciones de encuesta eliminadas seguirán apareciendo en los análisis, pero no se mostrarán como opción a los nuevos usuarios.
{% endalert %}

Puedes encontrar las métricas de rendimiento de tu cuestionario ampliando el desplegable **Resultados** de una variante específica en la sección **Rendimiento de los mensajes dentro de la aplicación** del análisis. Aquí tienes un desglose de lo que verás:

- **La interacción con el** cuestionario muestra cómo interactuaron los usuarios con el cuestionario en general, incluyendo el total de envíos, rechazos y clics dentro del cuerpo del mensaje.
- **Los resultados del cuestionario** muestran un desglose de cuántos usuarios seleccionaron cada opción de respuesta, junto con el porcentaje de envíos totales que representa cada opción.
- **Las métricas de la página de confirmación** (si están habilitadas) incluyen cuántos usuarios vieron la pantalla de confirmación, hicieron clic en su botón o la abandonaron sin interactuar.

Para conocer las definiciones de las métricas de las encuestas, consulte el [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data/report_metrics/) y filtre por "Mensaje en la aplicación".

Consulta [los informes de mensajes en la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para obtener un desglose de las métricas de tu campaña.

### Corrientes {#currents}

Las opciones seleccionadas pasarán automáticamente a Currents, en la sección [**Eventos de clic en mensajes de la aplicación**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` en el campo Cada elección se enviará con su identificador único universal (UUID).

## Ejemplos

{% tabs %}
{% tab User satisfaction %}

### Satisfacción de los usuarios

**Objetivo:** Mida la satisfacción de los clientes y envíe campañas de recuperación a los usuarios que hayan dejado puntuaciones bajas.

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

Para configurarlo, utiliza un cuestionario de selección múltiple en el que cada opción represente un tema de notificación. En lugar de asignar el mismo atributo con distintos valores, cada elección mapea un atributo booleano distinto que refleja el interés del usuario por ese tema. Si un usuario selecciona una opción, el atributo correspondiente se establece en `true`. Si no se selecciona, el atributo no cambia.

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

**Objetivo:** Identifique las principales razones por las que los usuarios visitan su aplicación.

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

### Mejorar los índices de conversión

**Objetivo:** Comprende por qué los clientes no actualizan o no compran.

Para configurarlo, utiliza un cuestionario de selección de una sola opción, en el que cada opción represente una barrera común a la mejora. Cada elección se mapea en el atributo personalizado `upgrade_reason` con un valor correspondiente que refleja la selección del usuario.

| Elección              | Atributo        | Valor       |
|---------------------|------------------|-------------|
| Demasiado caro       | `upgrade_reason` | `expensive` |
| Sin valor        | `upgrade_reason` | `value`     |
| Difícil de usar    | `upgrade_reason` | `difficult` |
| Utilizar a un competidor  | `upgrade_reason` | `competitor`|
| Otro motivo        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando un usuario envía el cuestionario, el valor seleccionado se guarda en su perfil. A continuación, puedes dirigirte a estos usuarios con campañas adaptadas a su objeción específica, como ofertas de descuento o mejoras de usabilidad.

{% endtab %}
{% tab Favorite features %}

### Características favoritas

**Objetivo:** Entender qué funciones disfrutan utilizando los clientes.

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
