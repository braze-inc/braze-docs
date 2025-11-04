---
nav_title: Integración
article_title: Resumen de la integración de la incorporación
page_order: 8
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben dar tus ingenieros o desarrolladores."

---

# Integración

> La integración con Braze es un proceso que merece la pena. Pero eres inteligente. Estás **aquí**. Está claro que ya lo sabes. Pero lo que probablemente no sepas es que tú y tus desarrolladores estáis a punto de emprender juntos un viaje que requiere conocimientos técnicos, planificación estratégica y una comunicación coherente que os ayude a coordinaros.

{% alert note %}
Ten en cuenta que el contenido de este artículo no se aplica al correo electrónico. Compruébalo en la sección [Configuración del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/).
{% endalert %}

## El aspecto técnico del proceso de integración

Puede que pienses: "¡Mis desarrolladores son mágicos! Pueden hacer cualquier cosa, ¡así que suelo dejarles hacer!". ¡Y probablemente lo son y probablemente pueden! Pero no hay razón para que no sepas lo que hacen entre bastidores. De hecho, ayudaría a todo el proceso si supieras cuándo intervenir con información y qué buscar cuando te digan: "¿Puedes enviarme la clave de API y el punto final de API?".

Entonces, ¿qué hacen cuando integran Braze con tu aplicación o sitio web? Me alegro de que preguntes.

### Paso 1: Implementan el SDK Braze

El SDK (kit de desarrollo de software) de Braze es la forma en que enviamos y recibimos información hacia y desde tu aplicación o sitio web. Tus ingenieros son, esencialmente, los que unen nuestras aplicaciones. Para ello, necesitan algunos datos clave:

* Tus [claves de API]({{site.baseurl}}/api/api_key/)
* Tu [punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze ya no proporciona puntos finales personalizados, así que utiliza los puntos finales SDK predefinidos. Si te han dado un punto final personalizado preexistente, aquí puedes encontrar los pasos de configuración necesarios para la integración [con Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) y [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Puedes darles esta información directamente, o puedes darles acceso a Braze creándoles una cuenta. 

{% alert warning %}
Asegúrate de que tú y tus desarrolladores no cambiáis sin saberlo o sin querer las credenciales de la empresa en Braze, ya que esto podría causar problemas durante el proceso de implementación o bloquear a uno o más de vosotros vuestras cuentas.
{% endalert %}

### Paso 2: Implementan los canales de mensajería que desees

Braze tiene muchas opciones para ponerte en contacto con tus usuarios, y cada una requiere su propia configuración o ajuste para que funcione como tú quieres. Aquí es donde la comunicación con tus ingenieros se vuelve crítica.

Asegúrate de indicar a tus desarrolladores qué canales quieres utilizar para garantizar que la implementación se realiza de forma eficiente y en el orden adecuado.

| Canal | Detalles |
|---|---|
| Mensajes dentro de la aplicación | Requiere la implementación del SDK, así como estos pasos específicos del canal. |
| Push | Requiere la implementación del SDK para proporcionar una gestión adecuada de las credenciales de mensajería y los tokens de notificaciones push. |
| Correo electrónico | Se trata de un proceso totalmente distinto. Consulta la sección [Configuración del correo]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) electrónico para obtener más detalles sobre la integración. |
| Tarjetas de contenido | Para empezar con [las tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), ponte en contacto con tu administrador del éxito del cliente Braze. |
| SMS & MMS | Consulta la sección [Configuración de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/) para obtener más detalles sobre la integración. |
| Webhooks | Requiere la implementación del SDK, así como pasos específicos del canal. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Puedes utilizar Braze para crear campañas de mensajería accesibles en cada canal. Trabaja con tus desarrolladores para asegurarte de que cumples las normas de accesibilidad en tu implementación.
{% endalert %}

### Paso 3: Configuran tus datos

Braze no es un pony de un solo truco. No se trata sólo de enviar correos electrónicos o enviar push. Se trata de crear recorridos del cliente personalizados que sean únicos para cada usuario y cliente. Los recorridos del cliente se basan en sus acciones dentro de tu aplicación o sitio web, ¡y tú defines cuáles son! La siguiente tarea de tus desarrolladores es asegurarse de que las acciones realizadas dentro de tu aplicación o sitio web sean recogidas por Braze.

Entonces, ¿qué tienes que hacer para darles esta información?

1. Trabaja con tu equipo de marketing para definir las campañas, los objetivos, los atributos y los eventos que necesitas seguir. Define esos casos de uso y compártelos con tus equipos.
2. Define tus requisitos de datos personalizados[(atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), etc.).
3. A partir de ahí, discute cómo deberían seguirse esos datos (desencadenados a través del SDK, etc.).
4. Define cuántos [espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) necesitas. Tus ingenieros necesitarán saber cómo [probar y configurar]({{site.baseurl}}/user_guide/getting_started/workspaces/) estos espacios de trabajo.

Una vez que descubras toda esta información, compártela con tu ingeniero. Tomarán esa información e implementarán tus [datos personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/). Puede que incluso necesites [importar algunos usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/). También debes conocer [las convenciones de denominación de los eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

### Paso 4: Personalizan en función de lo que quieras

Si quieres cosas como el lanzamiento desencadenado por API y el contenido conectado, discútelo tanto con tu contacto Braze como con tus desarrolladores para asegurarte de que podrás obtener datos que viven fuera de tu aplicación y de Braze en tus mensajes.

### Paso 5: Ambos realizáis el control de calidad de vuestra aplicación

Colabora con tu ingeniero para asegurarte de que todo funciona. Envía [mensajes de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), utiliza nuestras [aplicaciones de prueba para Android]({{site.baseurl}}/developer_guide/references/?tab=android) y [aplicaciones de prueba para iOS]({{site.baseurl}}/developer_guide/references/?tab=swift), ¡comprueba todas las casillas antes de empezar a enviar!

Incluso tenemos instrucciones específicas para [probar tu integración con Android o FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) y probar [el push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Tras la aplicación

Ten en cuenta que la línea de meta de la implementación no es también la luz verde para enviar un millón de mensajes a la vez. Enviar un millón de push podría romper tu aplicación si todos los clientes hacen clic simultáneamente en el mismo enlace. Te recomendamos que analices cuál es la capacidad de tu configuración interna para gestionar solicitudes de Braze antes de hacer clic en el botón **Enviar**. Luego, puedes establecer tu [límite de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) en función de eso.

\![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Cuando te sientas cómodo utilizando Braze, ¡considera la posibilidad de convertirte en un Braze Firebrand! Con Braze Firebrands, nuestra comunidad de interacción con los clientes, estamos construyendo una comunidad de personas influyentes que utilizan Braze para modernizar su experiencia del cliente y su marketing. ¿Quieres saber más? [Únete ahora](https://brazefirebrands.splashthat.com/).
