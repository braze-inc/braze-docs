### Mensajes de deslizamiento hacia arriba dentro de la aplicación

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} Los mensajes dentro de la aplicación se llaman así porque "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla.  Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

![Ejemplo de deslizamiento hacia arriba]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### Mensajes modales dentro de la aplicación

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Útiles para la mensajería más crítica, pueden equiparse con hasta dos botones de acción de clic y habilitación de análisis.

![Ejemplo modal]({% image_buster /assets/img_archive/In-App_Modal.png %})

### Mensajes completos dentro de la aplicación

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario.  La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen y la mitad inferior muestra texto, así como hasta dos botones de acción de clic y habilitación de análisis.

![Ejemplo completo]({% image_buster /assets/img_archive/In-App_Full.png %})

### Mensajes HTML completos dentro de la aplicación

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} Los mensajes dentro de la aplicación son útiles para crear contenidos totalmente personalizados para el usuario. El contenido HTML completo de los mensajes dentro de la aplicación, definido por el usuario, se muestra en {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes.

 {% if include.platform == "iOS" %}
El siguiente ejemplo muestra un mensaje HTML completo paginado dentro de la aplicación:

![Ejemplo HTML5]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}El siguiente ejemplo muestra un cuestionario HTML Mensaje completo dentro de la aplicación creado por SoundCloud.

![Ejemplo HTML5]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

El contenido completo de los mensajes dentro de la aplicación se muestra en un WKWebView y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes. **Ten en cuenta que actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.**

## Entrega de mensajes dentro de la aplicación

### Mensajes dentro de la aplicación (desencadenados)

La siguiente documentación se refiere al producto Braze `In-App Messaging`, también conocido como "mensajes dentro de la aplicación desencadenados", que se marcan como se resalta a continuación en el desplegable "Crear campaña":

![Creador de mensajes dentro de la aplicación]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

También puedes consultar la documentación de nuestro producto obsoleto [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages).

#### Tipos de desencadenantes

Nuestro producto de mensajes dentro de la aplicación te permite desencadenar la visualización de mensajes dentro de la aplicación como resultado de varios tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Además, los desencadenadores `Specific Purchase` y `Custom Event` pueden contener filtros de propiedades robustos.

{% alert note %}
Los mensajes desencadenados dentro de la aplicación sólo funcionan con eventos personalizados registrados a través del SDK de Braze. Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API o por eventos de la API (como eventos de compra). Si trabajas con Android, consulta cómo [registrar eventos personalizados en Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). Si trabajas con iOS, consulta cómo [registrar eventos personalizados en iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

#### Semántica de la entrega

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan al dispositivo del usuario al inicio de la sesión. Para más información sobre la semántica de inicio de sesión del SDK, consulta nuestra [documentación sobre el ciclo de vida de la sesión]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Tras la entrega, el SDK precargará los activos para que estén disponibles inmediatamente en el momento de desencadenar, minimizando la latencia de visualización.

Cuando un evento desencadenante tiene asociado más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje dentro de la aplicación con la prioridad más alta.

Para los mensajes dentro de la aplicación que se muestran inmediatamente después de entregarlos (como el inicio de sesión o el clic push), puede haber cierta latencia debido a que los activos no se precargan.

#### Intervalo de tiempo mínimo entre desencadenamientos

De forma predeterminada, limitamos la tasa de mensajes dentro de la aplicación a una vez cada 30 segundos para una experiencia de usuario de calidad.

{% if include.platform == "iOS" %}Puedes anular este valor a través de `ABKMinimumTriggerTimeIntervalKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece en `ABKMinimumTriggerTimeIntervalKey` el valor entero que desees como tiempo mínimo en segundos entre mensajes dentro de la aplicación:

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
Para anular este valor, configura `com_appboy_trigger_action_minimum_time_interval_seconds` en tu `braze.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

