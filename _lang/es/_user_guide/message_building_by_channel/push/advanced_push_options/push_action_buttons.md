---
nav_title: "Botones de acción para notificación push"
article_title: Botones de acción para notificación push
page_order: 1
page_type: reference
description: "Este artículo de referencia explica qué son los botones de acción para push y la diferencia entre las plataformas iOS y Android."
channel:
  - Push

---

# Botones de acción para notificación push

![Una notificación push de iOS con dos botones de acción para push: Aceptar y Rechazar.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Los botones de acción push permiten configurar el contenido y las acciones de los botones cuando se utilizan las notificaciones push Braze de iOS y Android. Con los botones de acción, sus usuarios pueden interactuar directamente con su aplicación desde una notificación sin necesidad de hacer clic en una experiencia de aplicación.

## Crear botones de acción

Cada botón interactivo puede enlazar a una página web o a un enlace profundo o abrir la aplicación. 

- Para campañas push estándar, puedes especificar tus botones de acción para push en la sección **Comportamiento al hacer clic** del compositor de mensajes push en el panel.
- Para las [campañas push rápidas]({{site.baseurl}}/quick_push), los botones de acción se pueden configurar por separado para cada plataforma en la pestaña **Configuración**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para utilizar botones de acción en tus mensajes push de iOS, haz lo siguiente:

1. Activa los botones de acción en la pestaña **Redactar** para una campaña estándar o en la pestaña **Configuración** para un push rápido.
2. Seleccione su **categoría de notificación de iOS** entre las siguientes combinaciones de botones disponibles:
 - Aceptar / Rechazar
 - Sí / No
 - Confirmar / Cancelar
 - Más
 - Categoría iOS personalizada prerregistrada

![Menú desplegable de categorías de notificaciones de iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Debido a la forma en que iOS gestiona los botones, es necesario realizar pasos de integración adicionales al configurar botones de acción push, que se describen en nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). En concreto, es necesario configurar las categorías de iOS o seleccionar entre determinadas opciones de botones predeterminados. Para las integraciones de Android, estos botones funcionarán automáticamente.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Para utilizar botones de acción en sus mensajes push de Android, haga lo siguiente:

1. Activa los botones de acción en la pestaña **Redactar** para una campaña estándar o en la pestaña **Configuración** para un push rápido.
2. Selecciona <i class="fas fa-plus-circle"></i> **Añadir botón** y especifica el texto del botón y el **Comportamiento al hacer clic**. Puede seleccionar una de las siguientes acciones disponibles:
  - Abrir aplicación
  - Redirigir a URL de página web
  - [Vínculo profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) a la aplicación

![Seleccionar "Abrir aplicación" como comportamiento al hacer clic en un botón de notificación.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Puedes añadir hasta tres botones en tu push.

#### Límites de caracteres en Android

A diferencia de los botones de iOS, que están apilados, los de Android se muestran uno al lado del otro en una fila. Esto significa que cuantos más botones añadas (hasta tres), menos espacio tendrás para copiar botones. 

![Botones de acción para notificación push de Android con texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

En la tabla siguiente se indica cuántos caracteres puede añadir antes de que se trunque la copia del botón, en función del número de botones que tenga:

| Número de botones | Caracteres máximos por botón |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

