---
nav_title: Prueba
article_title: Prueba de mensajes dentro de la aplicación
page_order: 4.5
description: "Este artículo de referencia explica el valor de probar tus mensajes dentro de la aplicación, cómo probarlos, así como una lista de cosas a tener en cuenta antes de enviarlos."
channel:
  - in-app messages
  
---

# Prueba de mensajes dentro de la aplicación

> Es extremadamente importante probar siempre tus mensajes dentro de la aplicación antes de enviar tus campañas. Nuestras capacidades de vista previa y de prueba ofrecen dos formas de echar un vistazo a tus mensajes dentro de la aplicación. Puedes previsualizar tu mensaje, para ayudarte a visualizarlo mientras lo redactas, así como enviar un mensaje de prueba a tu dispositivo o al de un usuario concreto. Te recomendamos que aproveches ambas.

## Vista previa

Puedes obtener una vista previa de tu mensaje dentro de la aplicación mientras lo redactas. Esto debería ayudarte a visualizar cómo será tu mensaje final desde la perspectiva de tu usuario.

{% alert warning %}
En la **vista previa**, la visualización de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarte de que tus medios, copia, personalización y atributos personalizados se generan correctamente.
{% endalert %}

### Vista previa de la generación de mensajes dentro de la aplicación

Obtén una vista previa del aspecto que tendrá tu mensaje para un usuario aleatorio, un usuario específico o un usuario personalizado; estos dos últimos son especialmente útiles si tu mensaje contiene personalización o varios idiomas. También puedes obtener una vista previa de los mensajes para dispositivos móviles o tabletas para hacerte una mejor idea de lo que experimentarán los usuarios.

\![Pestaña Redactar al crear un mensaje dentro de la aplicación que muestra la vista previa del aspecto que tendrá el mensaje. No se selecciona un usuario, por lo que el Liquid añadido en la sección del cuerpo se muestra como is.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze dispone de tres generaciones de mensajes dentro de la aplicación. Puedes ajustar con precisión a qué dispositivos deben enviarse tus mensajes, en función de la Generación que admitan.

Cambio entre generaciones al previsualizar un mensaje dentro de la aplicación.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Prueba

{% alert warning %}
Para enviar una prueba a [Grupos de Prueba de Contenidos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, antes de enviarla debe habilitarse la función push en tus dispositivos de prueba. <br><br>Por ejemplo, debes tener habilitada la función push en tu dispositivo iOS para poder tocar la notificación antes de que aparezca el mensaje de prueba.
{% endalert %}

### Vista previa del mensaje como usuario

También puedes obtener una vista previa de los mensajes desde la pestaña **de Prueba**, como si fueras un usuario. Puedes seleccionar un usuario concreto, un usuario aleatorio o crear un usuario personalizado.

\![Pestaña de prueba al crear un mensaje dentro de la aplicación. "Vista previa del mensaje como usuario" se establece en "Usuario personalizado", y los campos de perfil disponibles aparecen como opciones configurables.]({% image_buster /assets/img/iam-user-preview.png %})

{% alert important %}
Los envíos de prueba pueden hacer que se envíe más de un mensaje dentro de la aplicación a cada destinatario.
{% endalert %}

### Lista de control

- ¿Aparecen las imágenes y los medios y actúan como se espera de ellos?
- ¿Funciona el Liquid como se esperaba? ¿Has previsto un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) para el caso de que Liquid no devuelva información?
- ¿Es tu texto claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a dónde debe ir?

## Escáner de accesibilidad

Para respaldar las mejores prácticas de accesibilidad, Braze analiza automáticamente el contenido de los mensajes dentro de la aplicación creados con el editor HTML tradicional, comparándolo con las normas de accesibilidad. Este escáner ayuda a identificar el contenido que puede no cumplir las Normas de Accesibilidad al Contenido en la Web[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Las WCAG son un conjunto de normas técnicas reconocidas internacionalmente y desarrolladas por el Consorcio de la World Wide Web (W3C) para que los contenidos Web sean más accesibles a las personas con discapacidad.

Resultados de la exploración de accesibilidad]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
El escáner de accesibilidad de mensajes dentro de la aplicación sólo funciona con mensajes creados con HTML personalizado.
{% endalert %}

### Cómo funciona

El escáner se ejecuta automáticamente en mensajes HTML personalizados y evalúa todo tu mensaje HTML según el [conjunto](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa) completo [de reglas WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada asunto marcado, muestra:

- El elemento HTML específico implicado
- Una descripción del problema de accesibilidad
- Un enlace al contexto adicional o a las orientaciones de corrección

### Comprender las pruebas de accesibilidad automatizadas

{% multi_lang_include accessibility/automated_testing.md %}





