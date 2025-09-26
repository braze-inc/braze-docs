---
nav_title: Pruebas
article_title: Prueba de los mensajes en la aplicación
page_order: 4.5
description: "Este artículo de referencia explica el valor de probar tus mensajes in-app, cómo probarlos, así como una lista de cosas a tener en cuenta antes de enviarlos."
channel:
  - in-app messages
  
---

# Pruebas de mensajes en la aplicación

> Es muy importante probar siempre los mensajes in-app antes de enviar las campañas. Nuestras funciones de vista previa y prueba ofrecen dos maneras de echar un vistazo a tus mensajes in-app. Puedes previsualizar tu mensaje, para ayudarte a visualizarlo mientras lo redactas, así como enviar un mensaje de prueba a tu dispositivo o al de un usuario concreto. Le recomendamos que aproveche ambas.

## Vista previa

Puedes previsualizar tu mensaje en la aplicación mientras lo redactas. Esto le ayudará a visualizar el mensaje final desde la perspectiva del usuario.

{% alert warning %}
En **Vista Previa**, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarse de que los medios, la copia, la personalización y los atributos personalizados se generan correctamente.
{% endalert %}

### Vista previa de la generación de mensajes en la aplicación

Previsualice el aspecto que tendrá su mensaje para un usuario aleatorio, un usuario específico o un usuario personalizado; estos dos últimos son especialmente útiles si su mensaje contiene personalización o varios idiomas. También puedes previsualizar los mensajes para dispositivos móviles o tabletas para hacerte una mejor idea de lo que experimentarán los usuarios.

![La pestaña Redactar al crear un mensaje dentro de la aplicación muestra una vista previa del aspecto que tendrá el mensaje. No se ha seleccionado un usuario, por lo que el Liquid añadido en la sección del cuerpo se muestra tal cual.]({%image_buster /assets/img/in-app-message-preview.png %})

Braze dispone de tres generaciones de mensajes in-app. Puede ajustar con precisión a qué dispositivos deben enviarse sus mensajes, en función de la generación que admitan.

![Cambio entre generaciones al previsualizar un mensaje dentro de la aplicación.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

## Probar

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, debe activarse la función push en los dispositivos de prueba antes de enviarla. <br><br>Por ejemplo, debe tener activada la función push en su dispositivo iOS para poder tocar la notificación antes de que aparezca el mensaje de prueba.
{% endalert %}

### Vista previa del mensaje como usuario

También puedes previsualizar los mensajes desde la pestaña **Prueba**, como si fueras un usuario. Puede seleccionar un usuario específico, un usuario aleatorio o crear un usuario personalizado.

![Pestaña de prueba al crear un mensaje dentro de la aplicación. "Vista previa del mensaje como usuario" está configurado como "Usuario personalizado" y los campos de perfil disponibles aparecen como opciones configurables.]({% image_buster /assets/img/iam-user-preview.png %})

### Lista de comprobación

- ¿Aparecen las imágenes y los medios de comunicación y actúan como se esperaba?
- ¿Funciona el Líquido como se esperaba? ¿Ha previsto un [valor de atributo por defecto]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) en caso de que Liquid no devuelva ninguna información?
- ¿Es su texto claro, conciso y correcto?
- ¿Sus botones dirigen al usuario hacia dónde debe ir?

## Escáner de accesibilidad

Para respaldar las mejores prácticas de accesibilidad, Braze analiza automáticamente el contenido de los mensajes dentro de la aplicación creados con el editor HTML tradicional, comparándolo con las normas de accesibilidad. Este escáner ayuda a identificar el contenido que puede no cumplir las Normas de Accesibilidad al Contenido en la Web[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Las WCAG son un conjunto de normas técnicas reconocidas internacionalmente y desarrolladas por el Consorcio de la World Wide Web (W3C) para que los contenidos Web sean más accesibles a las personas con discapacidad.

![Resultados del escaneo de accesibilidad]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

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





