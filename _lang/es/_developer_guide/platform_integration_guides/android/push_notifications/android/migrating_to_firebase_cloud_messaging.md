---
nav_title: Migración a la mensajería en la nube de Firebase
article_title: Migración a la API de mensajería en la nube de Firebase
platform: Android
page_order: 29
description: "En este artículo se explica cómo migrar de la obsoleta API de mensajería en la nube de Google a Firebase Cloud Messaging (FCM)."
channel:
  - push
search_rank: 3
---

# Migración a la API de mensajería en la nube de Firebase

> Aprende a migrar de la API de mensajería en la nube obsoleta de Google a su API Firebase Cloud Messaging (FCM) totalmente compatible. Para más información, consulta las [Preguntas frecuentes sobre Firebase de Google - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
Si es la primera vez que configuras la integración push para Android, consulta en su lugar [Integración push estándar de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration).
{% endalert %}

## Límite de velocidad

La API de Firebase Cloud Messaging (FCM) tiene un límite de velocidad predeterminado de 600 000 solicitudes por minuto. Si alcanzas este límite, Braze lo volverá a intentar automáticamente en unos minutos. Para solicitar un aumento, ponte en contacto con [el servicio de asistencia de Firebase](https://firebase.google.com/support).

## Migración a FCM

### Paso 1: Verifica tu ID de Proyecto

Primero, abre Google Cloud. En la página de inicio de tu proyecto, comprueba el número del campo **ID del proyecto**: a continuación lo compararás con el de tu proyecto Firebase.

![La página de inicio del proyecto de Google Cloud con el "ID del proyecto" resaltado.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

A continuación, abre la Consola Firebase y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**.

![El proyecto Firebase con el menú "Configuración" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

En la pestaña **General**, comprueba que el **ID del proyecto** coincide con el que aparece en tu proyecto de Google Cloud.

![La página de "Configuración" del proyecto Firebase con el "ID del proyecto" resaltado.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### Paso 2: Verifica tu ID de remitente

Primero, abre Braze y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > Configuración de la aplicación **.**

![El menú "Configuración" se abre en Braze con la opción "Configuración de la aplicación" resaltada.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

En la **Configuración de notificaciones push** de tu aplicación Android, comprueba el número del campo **ID del remitente de la mensajería en la nube de Firebase**; a continuación, lo compararás con el de tu proyecto Firebase.

![El formulario de "Configuración de notificaciones push".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

A continuación, abre la Consola Firebase y selecciona <i class="fa-solid fa-gear"></i> **Configuración** > **Configuración del proyecto**.

![El proyecto Firebase con el menú "Configuración" abierto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecciona **Mensajería en la nube**. En **API de mensajería en la nube (heredada)**, comprueba que el **ID del remitente** coincide con el que aparece en tu panel Braze.

![La página "Cloud Messaging" del proyecto Firebase con el "Sender ID" resaltado.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### Paso 3: Habilitar la API de mensajería en la nube de Firebase

En Google Cloud, selecciona el proyecto que utiliza tu aplicación Android y, a continuación, habilita la [API de mensajería de Firebase Cloud](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![Habilitada la API Firebase Cloud Messaging (FCM)]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Paso 4: Crear una cuenta de servicio

A continuación, crea una nueva cuenta de servicio, para que Braze pueda realizar llamadas autorizadas a la API al registrar tokens de FCM. En Google Cloud, ve a **Service Accounts (Cuentas de servicio)** y elige tu proyecto. En la página **Cuentas de servicio**, selecciona **Crear cuenta de servicio**.

![Página de inicio de la cuenta de servicio de un proyecto con la opción "Crear cuenta de servicio" resaltada.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Introduce un nombre de cuenta de servicio, un ID y una descripción, luego selecciona **Crear y continuar**.

![El formulario para "Detalles de la cuenta de servicio".]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

En el campo **Rol**, busca y selecciona **Administrador de la API de mensajería en la nube de Firebase** en la lista de roles. Para un acceso más restrictivo, crea un [rol personalizado](https://cloud.google.com/iam/docs/creating-custom-roles) con el permiso `cloudmessaging.messages.create` y, en su lugar, elígelo de la lista. Cuando hayas terminado, selecciona **Hecho**.

{% alert warning %}
Asegúrate de seleccionar _Firebase Cloud Messaging **API** Admin_, no _Firebase Cloud Messaging Admin_.
{% endalert %}

![El formulario para "Conceder a esta cuenta de servicio acceso al proyecto" con "Firebase Cloud Messaging API Admin" seleccionado como rol.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Paso 5: Verificar permisos (opcional)

Para verificar qué permisos tiene tu cuenta de servicio, abre Google Cloud, luego ve a tu proyecto y selecciona **IAM**. En **Ver por directores**, selecciona **Exceso de permisos**.

![La pestaña "Ver por principios" con el número de permisos excedentes listados para cada principal.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

Ahora puedes revisar los permisos actuales asignados a tu rol seleccionado.

![La lista de permisos actuales asignados al rol seleccionado.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### Paso 6: Generar credenciales JSON

A continuación, genera las credenciales JSON de tu cuenta del servicio FCM. En Google Cloud IAM & Admin, ve a **Service Accounts (Cuentas de servicio)** y elige tu proyecto. Localiza la cuenta de servicio FCM [que creaste anteriormente](#step-4-create-a-service-account) y, a continuación, selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > **Gestionar claves**.

![La página de inicio de la cuenta de servicio del proyecto con el menú "Acciones" abierto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Selecciona **Añadir clave** > **Crear nueva clave**.

{% alert note %}
La creación de una nueva clave no eliminará las anteriores. Si borras accidentalmente tu nueva clave seleccionando **Revertir credenciales**, Braze utilizará tus claves heredadas como copia de seguridad.
{% endalert %}

![La cuenta de servicio seleccionada con el menú "Añadir clave" abierto.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Elige **JSON** y selecciona **Crear**. Si creaste tu cuenta de servicio utilizando un ID de proyecto de Google Cloud distinto del ID de tu proyecto de FCM, tendrás que actualizar manualmente el valor asignado a `project_id` en tu archivo JSON.

Asegúrate de recordar dónde descargaste la clave: la necesitarás en el siguiente paso.

![El formulario para crear una clave privada con "JSON" seleccionado.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Las claves privadas pueden suponer un riesgo para la seguridad si se ponen en peligro. Guarda tus credenciales JSON en una ubicación segura por ahora: eliminarás tu clave después de subirla a Braze.
{% endalert %}

### Paso 7: Sube tus credenciales JSON a Braze

En Braze, selecciona <i class="fa-solid fa-gear"></i> **Configuración** > Configuración de la aplicación **.**

![El menú "Configuración" se abre en Braze con la opción "Configuración de la aplicación" resaltada.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

En **Configuración de notificaciones push**, selecciona **Cargar archivo JSON** y, a continuación, elige el archivo [que generaste anteriormente](#step-6-generate-json-credentials). Cuando hayas terminado, selecciona **Guardar**.

![El formulario de "Configuración de la notificación push" con la clave privada actualizada en el campo "Clave del servidor de mensajería en la nube de Firebase".]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Las claves privadas pueden suponer un riesgo para la seguridad si se ponen en peligro. Ahora que tu clave está cargada en Braze, borra de tu computadora el archivo [que generaste anteriormente](#step-6-generate-json-credentials).
{% endalert %}

### Paso 8: Prueba tus nuevas credenciales (opcional)

En cuanto cargues tus credenciales en Braze, podrás empezar a enviar notificaciones push utilizando tus nuevas credenciales. Para probar tus nuevas credenciales, envía una notificación push real o de prueba a tu aplicación utilizando FCM o Braze. Si la notificación push pasa, todo funciona. Si no lo hace

- [Verifica tu ID de remitente](#step-2-verify-your-sender-id)
- [Verifica tus permisos](#step-5-verify-permissions-optional)
- Revisa los errores de notificación push en tu [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

Si sigues teniendo problemas, consulta [Revertir tus credenciales](#reverting-your-credentials).

## Revertir tus credenciales

Puedes borrar tus nuevas credenciales y restaurar tus credenciales heredadas en cualquier momento. En cuanto se restablezcan tus credenciales, podrás empezar a enviar notificaciones push utilizando tus credenciales heredadas.

En Braze, selecciona <i class="fa-solid fa-gear"></i> **Configuración** > Configuración de la aplicación **.** En **Configuración de notificaciones push**, selecciona **Revertir credenciales**.

{% alert warning %}
Si borras tus nuevas credenciales, no podrás restaurarlas más tarde. Tendrás que [generar nuevas credenciales](#step-6-generate-json-credentials) y volver a [subirlas a Braze](#step-7-upload-your-json-credentials-to-braze).
{% endalert %}

![El formulario de "Configuración de notificaciones push" con el botón "Revertir credenciales" resaltado.]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## Preguntas más frecuentes (FAQ) {#faq}

### ¿Cómo sé que mis nuevas credenciales funcionan?

Tus nuevas credenciales empezarán a funcionar en cuanto las subas a Braze. Para probarlas, selecciona **Probar credenciales**. Si obtienes un error, siempre puedes [revertir tus credenciales](#reverting-your-credentials).

### ¿Necesito migrar a FCM para mis aplicaciones no utilizadas o mis aplicaciones desarrolladoras?

No. Sin embargo, tus aplicaciones no utilizadas y tus aplicaciones de desarrollador seguirán mostrando un mensaje de advertencia pidiéndote que migres. Para eliminar este mensaje, puedes cargar nuevas credenciales o eliminar estas aplicaciones de tu espacio de trabajo. Si decides eliminar estas aplicaciones, asegúrate de consultarlo antes con tu equipo por si alguien las está utilizando.

### ¿Dónde puedo consultar los mensajes de error?

Puedes revisar los errores de las notificaciones push en tu [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

### Antes de migrar, ¿necesito actualizar mi aplicación o SDK?

No. Sólo tienes que cargar tus nuevas credenciales en Braze.

### ¿Tengo que borrar primero mis antiguas credenciales heredadas?

No. Si alguna vez necesitas eliminar tus nuevas credenciales, [podrás utilizar en su lugar tus credenciales heredadas](#reverting-your-credentials).

### Después de la migración, ¿por qué sigue apareciendo un mensaje de advertencia en Braze?

Seguirás viendo este mensaje de advertencia si hay al menos una aplicación Android en tu espacio de trabajo que todavía necesitas migrar. Asegúrate de migrar todas tus aplicaciones Android a la API FCM de Google, que es totalmente compatible.

### Después de la migración, ¿cuánto tiempo tengo que esperar para volver a enviar notificaciones push?

Tras la migración, puedes empezar a enviar notificaciones push utilizando tus nuevas credenciales inmediatamente.

### ¿Qué pasa si he creado mi cuenta de servicio utilizando un proyecto diferente al de mi proyecto FCM?

Si creaste tu cuenta de servicio utilizando un ID de proyecto de Google Cloud distinto del ID de tu proyecto de FCM, tendrás que actualizar manualmente el valor asignado a `project_id` en tu archivo JSON después de [crear uno nuevo](#step-6-generate-json-credentials).
