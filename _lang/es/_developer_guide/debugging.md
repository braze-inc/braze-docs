---
nav_title: Depuración SDK
article_title: Depuración del SDK de Braze 
description: "Aprende a utilizar el depurador del SDK de Braze, para que puedas solucionar los problemas de tus canales con SDK, sin habilitar manualmente el registro detallado en tu aplicación."
page_order: 13
---

# Depuración del SDK de Braze

> Aprende a utilizar el depurador integrado del SDK de Braze, para que puedas solucionar problemas de tus canales con SDK, sin necesidad de habilitar el registro detallado en tu aplicación.

{% alert important %}
Actualmente, esta característica sólo está disponible para aplicaciones nativas de iOS y Android. Para habilitar la depuración para el SDK de la Web de Braze, puedes [utilizar un parámetro URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging) en su lugar.
{% endalert %}

## Requisitos previos

Para utilizar el depurador Braze SDK, asegúrate de que tus SDK están actualizados al menos con estas versiones mínimas:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Depuración del SDK de Braze

### Paso 1: Cierra tu aplicación

Antes de iniciar la sesión de depuración, cierra la aplicación que esté experimentando problemas. Puedes relanzar la aplicación al inicio de tu sesión.

### Paso 2: Crear una sesión de depuración

En Braze, ve a **Configuración** y, en **Configuración y pruebas**, selecciona **Depurador SDK**.

![La sección "Configuración y pruebas" con "Depurador SDK" resaltado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecciona **Crear sesión de depuración**.

![La página "Depurador SDK".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Paso 3: Selecciona un usuario

Busca a un usuario utilizando su dirección de correo electrónico, `external_id`, alias de usuario o token de notificaciones push. Cuando estés listo para iniciar la sesión, selecciona **Seleccionar usuario**.

![La página de depuración del usuario seleccionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Paso 4: Volver a lanzar la aplicación

Primero, inicia la aplicación y confirma que tu dispositivo está emparejado. Si el emparejamiento se realiza correctamente, relanza tu aplicación; así te asegurarás de que los registros de inicialización de la aplicación se capturan por completo.

### Paso 5: Completa los pasos de reproducción

Tras relanzar tu aplicación, sigue los pasos para reproducir el error.

{% alert tip %}
Cuando reproduzcas el error, asegúrate de seguir los pasos de reproducción lo más fielmente posible, para que puedas crear [registros de calidad](#step-6-export-your-session-logs-optional).
{% endalert %}

### Paso 6: Finaliza tu sesión

Cuando hayas terminado con los pasos de reproducción, selecciona **Finalizar sesión** > **Cerrar**.

![La sesión de depuración muestra el botón "Finalizar sesión".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Puede tardar unos minutos en generar tus registros, dependiendo de la duración de la sesión y de la conectividad de la red.
{% endalert %}

### Paso 7: Comparte o exporta tu sesión (opcional)

Después de la sesión, puedes exportar tus registros de sesión como archivo CSV. Además, otras personas pueden utilizar tu **ID de sesión** para buscar tu sesión de depuración, por lo que no necesitas enviarles tus registros directamente.

![La página de depuración con "Exportar registros" y "Copiar ID de sesión" que se muestra después de la sesión.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})
