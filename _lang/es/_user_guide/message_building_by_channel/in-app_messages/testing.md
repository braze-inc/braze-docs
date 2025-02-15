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

![La pestaña Redactar al crear un mensaje dentro de la aplicación muestra una vista previa del aspecto que tendrá el mensaje. No se selecciona un usuario, por lo que el Líquido añadido en la sección del cuerpo se muestra tal cual.][1]

Braze dispone de tres generaciones de mensajes in-app. Puede ajustar con precisión a qué dispositivos deben enviarse sus mensajes, en función de la generación que admitan.

![Cambio entre generaciones al previsualizar un mensaje in-app.][2]{: height="50%" width="50%"}

## Probar

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, debe activarse la función push en los dispositivos de prueba antes de enviarla. <br><br>Por ejemplo, debe tener activada la función push en su dispositivo iOS para poder tocar la notificación antes de que aparezca el mensaje de prueba.
{% endalert %}

### Vista previa del mensaje como usuario

También puedes previsualizar los mensajes desde la pestaña **Prueba**, como si fueras un usuario. Puede seleccionar un usuario específico, un usuario aleatorio o crear un usuario personalizado.

![Pestaña de prueba al crear un mensaje dentro de la aplicación. "Previsualizar mensaje como usuario" se establece en "Usuario personalizado" y los campos de perfil disponibles aparecen como opciones configurables.][3]

### Lista de comprobación

- ¿Aparecen las imágenes y los medios de comunicación y actúan como se esperaba?
- ¿Funciona el Líquido como se esperaba? ¿Ha previsto un [valor de atributo por defecto]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) en caso de que Liquid no devuelva ninguna información?
- ¿Es su texto claro, conciso y correcto?
- ¿Sus botones dirigen al usuario hacia dónde debe ir?

[1]: {%image_buster /assets/img/in-app-message-preview.png %}
[2]: {% image_buster /assets/img/iam-generations.gif %}
[3]: {% image_buster /assets/img/iam-user-preview.png %}
