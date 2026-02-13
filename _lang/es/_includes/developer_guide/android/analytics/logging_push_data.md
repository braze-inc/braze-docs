## Registrar datos con la API de Braze (recomendado)

Puedes registrar análisis en tiempo real haciendo llamadas al [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para registrar los análisis, envía el valor `braze_id` desde el panel de Braze para identificar qué perfil de usuario hay que actualizar.

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Registrar datos manualmente

Dependiendo de los detalles de tu carga útil, puedes registrar los análisis manualmente en tu implementación de `FirebaseMessagingService.onMessageReceived` o en tu actividad de inicio. Ten en cuenta que tu subclase `FirebaseMessagingService` debe finalizar la ejecución en un plazo de 9 segundos desde la invocación para evitar ser [marcada o terminada](https://firebase.google.com/docs/cloud-messaging/android/receive) por el sistema Android.
