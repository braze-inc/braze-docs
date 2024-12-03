---
nav_title: "Cuestionario simple"
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

![Tres sencillos mensajes de encuesta: preferencias de notificación, preferencias dietéticas y una encuesta de satisfacción del cliente. Las opciones seleccionadas en las encuestas corresponden a atributos personalizados que se registrarán para ese usuario.]({% image_buster /assets/img/iam/iam-survey.png %})

## Requisitos del SDK {#supported-sdk-versions}

Este mensaje in-app sólo se enviará a los dispositivos compatibles con [Flex CSS](https://caniuse.com/flexbox), y deben tener al menos las siguientes [versiones del SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze.
{% endalert %}

## Crear un cuestionario {#create}

Al crear un [mensaje dentro de la aplicación][1], seleccione **Encuesta simple** como **Tipo de mensaje**.

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

Esta plantilla de encuesta es compatible tanto con aplicaciones móviles como con navegadores web. Recuerda comprobar que tus SDK están en las [versiones de SDK mínimas](#supported-sdk-versions) requeridas para esta característica.

### Paso 1: Añade tu pregunta del cuestionario

Para empezar a construir tu cuestionario, añade tu pregunta en el campo **Encabezado** del cuestionario. Si lo desea, puede añadir un mensaje opcional **en el cuerpo** que aparecerá debajo de la pregunta de la encuesta.

![Pestaña de composición del editor de cuestionarios simples, con campos para un encabezado, un cuerpo opcional y un texto de ayuda opcional.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
Estos campos pueden incluir tanto Liquid como emojis, ¡así que ponte elegante!
{% endalert %}

### Paso 2: Elige entre opción única o múltiple {#single-multiple-choice}

Utilice **Selección de una opción** o **Selección de varias opciones** para controlar si un usuario puede seleccionar sólo una opción o varias opciones. Puede añadir hasta 12 opciones en una encuesta.

![Desplegable de opciones con la opción "Selección múltiple" seleccionada.]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
Su **texto de ayuda** se actualizará automáticamente cuando cambie entre **Selección de opción única** y **Selección de opción múltiple** para que los usuarios sepan cuántas opciones pueden seleccionar.
{% endalert %}

### Paso 3: Recopilar atributos personalizados {#custom-attributes}

Seleccione **Registrar atributos al enviar** para recopilar atributos basados en el envío del usuario. Puede utilizar esta opción para crear nuevos segmentos y campañas de retargeting. Por ejemplo, en una encuesta de satisfacción, podría enviar un correo electrónico de seguimiento a todos los usuarios que no estuvieran satisfechos.

![Desplegable de opciones con la opción "Registrar atributos al enviar" seleccionada.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

Para añadir un atributo personalizado a cada opción, seleccione un nombre de atributo personalizado en el menú desplegable (o cree uno nuevo) y, a continuación, introduzca el valor que se establecerá cuando se envíe esta opción. Puede crear un nuevo atributo personalizado en su [Página de Configuración][5].

Por ejemplo, en una encuesta sobre preferencias de notificaciones, puede hacer que cada opción sea un atributo booleano (verdadero/falso) para permitir a los usuarios seleccionar los temas que les interesan. Si un usuario marca la opción "Promociones", se actualizará su [perfil de usuario][3] con el atributo personalizado `Promotions Topic` establecido en `true`. Si dejan la opción sin marcar, ese mismo atributo permanecerá inalterado.

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

A continuación, puede crear un segmento para los usuarios con `Promotions Topic = true` para asegurarse de que sólo los usuarios interesados en sus promociones recibirán las campañas pertinentes.

{% alert important %}
Cuando la colección de atributos personalizados está activada, las opciones que comparten el mismo nombre de atributo personalizado se combinarán en una matriz.
{% endalert %}

#### Tipos de datos de atributos personalizados

El tipo de datos de sus atributos personalizados es importante dependiendo de cómo haya configurado su encuesta.

- **Selección múltiple:** El tipo de datos del atributo personalizado debe ser un array. Si el atributo personalizado se establece en un tipo de datos diferente, las respuestas no se registrarán.
- **Selección de opción simple:** El tipo de datos del atributo personalizado _no debe_ ser un array. Las respuestas no se registrarán si el atributo es una matriz.

#### Sólo registro de respuestas

También puede optar por **Registrar sólo las respuestas (sin atributos)**. Cuando se selecciona esta opción, las respuestas de la encuesta se registran como clics de botón, pero los atributos personalizados no se registran en el perfil del usuario. Esto significa que puede seguir viendo las métricas de clics para cada opción de encuesta (consulte [Análisis](#analytics)), pero esa elección no se reflejará en su perfil de usuario.

Estas métricas de clics no están disponibles para el retargeting.

### Paso 4: Elija el comportamiento de sumisión

Una vez que el usuario envía su respuesta, puede mostrar opcionalmente una página de confirmación, o simplemente cerrar el mensaje.

Una página de confirmación es un buen lugar para agradecer a los usuarios su tiempo o proporcionar información adicional. Puede personalizar la llamada a la acción de esta página para guiar a los usuarios a otra página de su aplicación o sitio web.

Edite el texto del botón y el comportamiento al hacer clic en la sección **Botón Enviar** de la parte inferior de la pestaña **Encuesta**:

![Comportamiento al hacer clic establecido en "Enviar respuestas y mostrar página de confirmación".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si decide añadir una página de confirmación, vaya a la pestaña **Página de confirmación** para personalizar su mensaje:

![Pestaña Página de confirmación del editor de encuestas simples. Los campos disponibles son cabecera, cuerpo opcional, texto del botón y comportamiento del botón al hacer clic.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

Si desea guiar a los usuarios a otra página de su aplicación o sitio web, cambie el **comportamiento Al hacer clic** del botón.

### Paso 5: Estiliza tu mensaje (opcional) {#styling}

Puede personalizar el color de la fuente y el color de acento del mensaje utilizando el selector **Tema de color**.

![Pestaña Componer del editor de encuestas simple con el selector Tema de color expandido después de que un usuario haya hecho clic en la paleta de colores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analizar los resultados {#analytics}

Una vez lanzada la campaña, puede analizar los resultados en tiempo real para ver el desglose de cada opción seleccionada. Si ha activado [la recopilación de atributos personalizados](#custom-attributes), también podrá crear nuevos segmentos o campañas de seguimiento para los usuarios que hayan enviado la encuesta.

{% alert note %}
Las opciones de encuesta eliminadas seguirán apareciendo en los análisis, pero no se mostrarán como opción a los nuevos usuarios.
{% endalert %}

Para conocer las definiciones de las métricas de las encuestas, consulte el [Glosario de métricas de los informes][11] y filtre por "Mensaje en la aplicación".

![Panel de rendimiento de mensajes in-app con análisis de clics para cada opción y botón de la encuesta.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

Consulta [los informes de mensajes en la aplicación][4] para obtener un desglose de las métricas de tu campaña.

### Corrientes {#currents}

Las opciones seleccionadas pasarán automáticamente a Currents, en la sección [**Eventos de clic en mensajes de la aplicación**][6] `button_id` en el campo Cada elección se enviará con su identificador único universal (UUID).

## Ejemplos

### Satisfacción de los usuarios

**Objetivo:** Mida la satisfacción de los clientes y envíe campañas de recuperación a los usuarios que hayan dejado puntuaciones bajas.

Para este caso de uso, utilice la selección de una sola opción, con opciones que vayan de "Muy insatisfecho" a "Muy satisfecho". Cada opción tiene el atributo personalizado `customer_satisfaction` establecido en un número del 1 al 5, siendo 1 el menos satisfecho y 5 el más satisfecho.

Una vez lanzada la encuesta, puede dirigir las campañas de recuperación a los usuarios que se declararon "Muy insatisfechos" o "Insatisfechos", es decir, los usuarios con `customer_satisfaction` en 1 ó 2.

![][7]

### Identificar los objetivos del cliente

**Objetivo:** Identifique las principales razones por las que los usuarios visitan su aplicación.

Para este caso de uso, utilice la selección de una sola opción, siendo cada opción una razón común por la que un usuario podría estar visitando su aplicación. Cada opción tiene el atributo personalizado `product_goal` establecido en el tema del caso de uso. 

Por ejemplo, si el usuario selecciona "Actualizar mi cuenta", se configurará `product_goal = upgrade` en el perfil del usuario.

![][8]

### Mejorar los índices de conversión

**Objetivo:** Comprende por qué los clientes no actualizan o no compran.

Para este caso de uso, utilice la selección de una sola opción, siendo cada opción una razón común por la que un usuario podría no pasar a una cuenta Premium. Cada opción tiene el atributo personalizado `upgrade_reason` establecido en la selección del usuario. 

Por ejemplo, si el usuario selecciona "Demasiado caro", aparecerá `upgrade_reason = expensive` en su perfil. Puede dirigirse a estos usuarios para campañas promocionales como descuentos o pruebas gratuitas.

![][9]

### Características favoritas

**Objetivo:** Entender qué funciones disfrutan utilizando los clientes.

Para este caso de uso, utilice una selección múltiple en la que cada opción sea una función de la aplicación. Cada opción tiene el atributo personalizado `favorite_features` establecido en la selección del usuario. Dado que este caso de uso implica opciones múltiples, después de que el usuario haya completado la encuesta, su perfil se actualizará con el atributo `favorite_features` establecido en una matriz de todas las opciones seleccionadas.

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
