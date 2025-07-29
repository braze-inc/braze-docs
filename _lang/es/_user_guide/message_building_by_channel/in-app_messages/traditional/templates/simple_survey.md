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



Esta plantilla de encuesta es compatible tanto con aplicaciones móviles como con navegadores web. Recuerda comprobar que tus SDK están en las [versiones de SDK mínimas](#supported-sdk-versions) requeridas para esta característica.

### Paso 1: Añade tu pregunta del cuestionario

Para empezar a construir tu cuestionario, añade tu pregunta en el campo **Encabezado** del cuestionario. Si lo desea, puede añadir un mensaje opcional **en el cuerpo** que aparecerá debajo de la pregunta de la encuesta.



{% alert tip %}
Estos campos pueden incluir tanto Liquid como emojis, ¡así que ponte elegante!
{% endalert %}

### Paso 2: 

Puede añadir hasta 12 opciones en una encuesta.

  



![Desplegable de opciones con la opción "Registrar atributos al enviar" seleccionada.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Recopilar atributos personalizados {#custom-attributes}

Seleccione **Registrar atributos al enviar** para recopilar atributos basados en el envío del usuario. Puede utilizar esta opción para crear nuevos segmentos y campañas de retargeting. 

Para añadir un atributo personalizado a cada opción, seleccione un nombre de atributo personalizado en el menú desplegable (o cree uno nuevo) y, a continuación, introduzca el valor que se establecerá cuando se envíe esta opción. 

El tipo de datos de sus atributos personalizados es importante dependiendo de cómo haya configurado su encuesta.

- **Selección múltiple:** El tipo de datos del atributo personalizado debe ser un array. Si el atributo personalizado se establece en un tipo de datos diferente, las respuestas no se registrarán.
- **Selección de opción simple:** El tipo de datos del atributo personalizado _no debe_ ser un array. Las respuestas no se registrarán si el atributo es una matriz.

{% alert important %}
Cuando la colección de atributos personalizados está activada, las opciones que comparten el mismo nombre de atributo personalizado se combinarán en una matriz.
{% endalert %}

#####  

  Si dejan la opción sin marcar, ese mismo atributo permanecerá inalterado.



#### 

También puede optar por **Registrar sólo las respuestas (sin atributos)**. Cuando se selecciona esta opción, las respuestas de la encuesta se registran como clics de botón, pero los atributos personalizados no se registran en el perfil del usuario. Esto significa que puede seguir viendo las métricas de clics para cada opción de encuesta (consulte [Análisis](#analytics)), pero esa elección no se reflejará en su perfil de usuario.

Estas métricas de clics no están disponibles para el retargeting.

### Paso 4: Elija el comportamiento de sumisión

Una vez que el usuario envía su respuesta, puede mostrar opcionalmente una página de confirmación, o simplemente cerrar el mensaje.

Una página de confirmación es un buen lugar para agradecer a los usuarios su tiempo o proporcionar información adicional. 

Edite el texto del botón y el comportamiento al hacer clic en la sección **Botón Enviar** de la parte inferior de la pestaña **Encuesta**:

![Comportamiento al hacer clic establecido en "Enviar respuestas y mostrar página de confirmación".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si decide añadir una página de confirmación, vaya a la pestaña **Página de confirmación** para personalizar su mensaje:

![Pestaña Página de confirmación del editor de encuestas simples. 

Si desea guiar a los usuarios a otra página de su aplicación o sitio web, cambie el **comportamiento Al hacer clic** del botón.

### Paso 5: Estiliza tu mensaje (opcional) {#styling}

Puede personalizar el color de la fuente y el color de acento del mensaje utilizando el selector **Tema de color**.

![Pestaña Componer del editor de encuestas simple con el selector Tema de color expandido después de que un usuario haya hecho clic en la paleta de colores.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analizar los resultados {#analytics}

Una vez lanzada la campaña, puede analizar los resultados en tiempo real para ver el desglose de cada opción seleccionada. Si ha activado [la recopilación de atributos personalizados](#custom-attributes), también podrá crear nuevos segmentos o campañas de seguimiento para los usuarios que hayan enviado la encuesta.

{% alert note %}
Las opciones de encuesta eliminadas seguirán apareciendo en los análisis, pero no se mostrarán como opción a los nuevos usuarios.
{% endalert %}

 

- 
- 
- 





### Corrientes {#currents}

 Cada elección se enviará con su identificador único universal (UUID).

## Ejemplos

### Satisfacción de los usuarios

**Objetivo:** Mida la satisfacción de los clientes y envíe campañas de recuperación a los usuarios que hayan dejado puntuaciones bajas.

 

|                                 |               |  |
|---------------------------------------|------------------------|-------|
|                   |  |      |
|                        |  |      |
|  |  |      |
|                           |  |      |
|                      |  |      |


  

### 

**Objetivo:** 

   

|              |               |   |
|--------------------|------------------------|--------|
|     | |  |
|          |      |  |
|       |   |  |
|  |         |  |
|    |            |  |


### Identificar los objetivos del cliente

**Objetivo:** Identifique las principales razones por las que los usuarios visitan su aplicación.

 

|                      |        |      |
|----------------------------|------------------|-----------|
|             |    |   |
|        |    |  |
|   |    | |
|            |    |  |
|               |    |   |


 

### Mejorar los índices de conversión

**Objetivo:** 

 

|               |         |        |
|---------------------|------------------|-------------|
|        |  |  |
|         |  |      |
|     |  |  |
|   |  | |
|         |  |      |


 

### Características favoritas

**Objetivo:** Entender qué funciones disfrutan utilizando los clientes.

 

|             |           |         |
|-------------------|--------------------|--------------|
|          | |   |
|         | |      |
|      | |     |
|   | |     |
|      | |      |
|      | |       |
|          | |   |






