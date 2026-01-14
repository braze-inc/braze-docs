---
nav_title: "Botones de acción push"
article_title: Botones de acción push
page_order: 1
page_type: reference
description: "Este artículo de referencia explica qué son los botones de acción para push y la diferencia entre las plataformas iOS y Android."
channel:
  - Push

---

# Botones de acción push

Una notificación push de iOS con dos botones de acción para push: Aceptar y Rechazar.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Los botones de acción para push te permiten configurar el contenido y las acciones de los botones al utilizar las notificaciones push de Braze para iOS y Android. Con los botones de acción, tus usuarios pueden interactuar directamente con tu aplicación desde una notificación sin necesidad de hacer clic en una experiencia de la aplicación.

## Crear botones de acción

Cada botón interactivo puede enlazar a una página Web o a un vínculo profundo o abrir la aplicación. 

- Para campañas push estándar, puedes especificar tus botones de acción para push en la sección **Comportamiento al hacer clic** del compositor de mensajes push en el panel.
- Para las [campañas push rápidas]({{site.baseurl}}/quick_push), los botones de acción se pueden configurar por separado para cada plataforma en la pestaña **Configuración**.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para utilizar botones de acción en tus mensajes push de iOS, haz lo siguiente:

1. Activa los botones de acción en la pestaña **Redactar** para una campaña estándar o en la pestaña **Configuración** para un push rápido.
2. Selecciona tu **categoría de notificación de iOS** entre las siguientes combinaciones de botones disponibles:
 - Aceptar / Rechazar
 - Sí / No
 - Confirmar / Cancelar
 - Más
 - Categoría iOS personalizada prerregistrada

Menú desplegable de la categoría de notificación de iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Debido al manejo de los botones por parte de iOS, necesitas realizar pasos de integración adicionales al configurar botones de acción para notificación push, que se describen en nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). En concreto, tienes que configurar Categorías de iOS o seleccionar entre determinadas opciones de botones predeterminados. Para las integraciones de Android, estos botones funcionarán automáticamente.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Para utilizar botones de acción en tus mensajes push de Android, haz lo siguiente:

1. Activa los botones de acción en la pestaña **Redactar** para una campaña estándar o en la pestaña **Configuración** para un push rápido.
2. Selecciona <i class="fas fa-plus-circle"></i> **Añadir botón** y especifica el texto del botón y el **Comportamiento al hacer clic**. Puedes seleccionar una de las siguientes acciones disponibles:
  - Abrir aplicación
  - Redirigir a URL Web
  - [Vínculo profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) con la aplicación

\![Seleccionar "Abrir aplicación" como comportamiento al hacer clic en un botón de notificación.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Puedes añadir hasta tres botones en tu push.

#### Límites de caracteres en Android

A diferencia de los botones de iOS, que están apilados, los botones de Android se muestran uno al lado del otro en una fila. Esto significa que cuantos más botones añadas (hasta tres), menos espacio tendrás para copiar botones. 

\![Botones de acción para notificación push de Android con texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

La siguiente tabla indica cuántos caracteres puedes añadir antes de que se trunque la copia de tu botón, dependiendo del número de botones que tengas:

| Número de botones | Máximo de caracteres por botón |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

