## Comprobaciones básicas

### Mi mensaje dentro de la aplicación no se mostró para un usuario.

1. ¿Estaba el usuario en el segmento al inicio de la sesión, cuando el SDK solicita nuevos mensajes dentro de la aplicación?
2. ¿El usuario era elegible o re-elegible para recibir el mensaje dentro de la aplicación según las normas de segmentación de la campaña?
3. ¿Se vio afectado el usuario por un límite de frecuencia?
4. ¿Estaba el usuario en un grupo de control? Comprueba si tu campaña está configurada para las pruebas AB.
5. ¿Se ha mostrado un mensaje dentro de la aplicación diferente y de mayor prioridad en lugar del mensaje esperado?
6. ¿Mi dispositivo estaba en la orientación correcta especificada por la campaña?
7. ¿Mi mensaje fue suprimido por el intervalo de tiempo mínimo predeterminado de 30 segundos entre desencadenamientos, impuesto por el SDK?

### Mi mensaje dentro de la aplicación no se mostró a todos los usuarios de esta plataforma.

1. ¿Tu campaña está configurada para dirigirse a aplicaciones móviles o navegadores Web, según corresponda? Por ejemplo, si tu campaña sólo se dirige a navegadores Web, no se enviará a dispositivos Android.
2. ¿Has implementado una interfaz de usuario personalizada y funciona según lo previsto? ¿Hay algún otro manejo personalizado o supresión del lado de la aplicación que pueda estar interfiriendo con la visualización? 
3. ¿Alguna vez esta plataforma y versión de aplicación en particular ha mostrado mensajes dentro de la aplicación con éxito?
4. ¿El desencadenamiento tuvo lugar localmente en el dispositivo? Ten en cuenta que no se puede utilizar una llamada REST para desencadenar un mensaje dentro de la aplicación en el SDK.

### Mi mensaje dentro de la aplicación no se mostraba a todos los usuarios.

1. ¿Se ha configurado correctamente la acción desencadenante en el panel, así como en la integración de la aplicación?
2. ¿Se ha mostrado un mensaje dentro de la aplicación diferente y de mayor prioridad en lugar del mensaje esperado?
3. ¿Tienes una versión reciente del SDK? Algunos tipos de mensajes dentro de la aplicación tienen requisitos de versión del SDK.
4. ¿Se han integrado correctamente las sesiones en tu integración? ¿Funcionan los análisis de sesión en esta aplicación?

### Mi mensaje dentro de la aplicación tardó mucho en aparecer

1. Si sirves grandes archivos de imagen o video desde tu CDN a un mensaje dentro de la aplicación basado en HTML, comprueba que tus archivos estén optimizados para ser lo más pequeños posible y que tu CDN tenga un buen rendimiento.
2. Comprueba si has configurado un `delay` para tu mensaje dentro de la aplicación en el panel.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Dependiendo de las circunstancias, los mensajes dentro de la aplicación descargarán o cargarán las imágenes relevantes del disco antes de su visualización. Si tienes una conexión de red lenta o un dispositivo de muy bajo rendimiento, este proceso puede tardar un poco. Asegúrate de que tus imágenes están optimizadas para ser lo más pequeñas posible.
{% endcase %}

Para profundizar en estas situaciones, visita <a id="troubleshooting-in-app-advanced">la sección de solución de problemas avanzados</a>.

## Problemas con los análisis de impresiones y clics

{% if include.sdk == "iOS" %}
### Las impresiones y los clics no se registran

Si has configurado un delegado de mensajes dentro de la aplicación para que gestione manualmente la visualización del mensaje o las acciones de clic, debes [registrar los clics](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) y las [impresiones](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) manualmente en el mensaje dentro de la aplicación.
{% elsif include.sdk == "Android" %}
### Las impresiones y los clics no se registran
Si has configurado un delegado de mensajes dentro de la aplicación para que gestione manualmente la visualización del mensaje o las acciones de clic, debes registrar manualmente los clics y las impresiones en el mensaje dentro de la aplicación.
{% endif %}

### Las impresiones son inferiores a lo esperado

1. Los desencadenantes tardan en sincronizarse con el dispositivo al iniciar la sesión, por lo que puede darse una condición de carrera si los usuarios registran un evento o una compra justo después de iniciar la sesión. Una posible solución podría ser cambiar la campaña para que se desencadene al inicio de la sesión, y luego segmentar en función del evento o la compra previstos. Ten en cuenta que esto entregaría el mensaje dentro de la aplicación en el siguiente inicio de sesión tras producirse el evento.

2. Si la campaña se desencadena por el inicio de una sesión o un evento personalizado, debes asegurarte de que este evento o sesión se produce con la frecuencia suficiente para desencadenar el mensaje. Comprueba estos datos en las páginas [Resumen]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (para datos de sesión) o [Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![Página de eventos personalizados que muestra un gráfico del número de veces que se ha producido el evento personalizado Añadido a Favoritos durante un periodo de un mes]({% image_buster /assets/img_archive/trouble5.png %})

### Las impresiones son más bajas que antes

1. Asegúrate de que nadie haya alterado involuntariamente el segmento o la campaña desde su lanzamiento. Nuestros registros de cambios de segmento y de campaña te darán información sobre los cambios que se han hecho, quién los hizo y cuándo ocurrieron.

![Enlace para ver el registro de cambios en la página Detalles de la campaña con siete cambios desde la última vez que el usuario vio la campaña]({% image_buster /assets/img_archive/trouble4.png %})

2. Asegúrate de que no has reutilizado el evento desencadenante en una campaña de mensajes dentro de la aplicación con una prioridad más alta.

## Solución de problemas avanzada {#troubleshooting-in-app-advanced}

La mayoría de los problemas de mensajes dentro de la aplicación pueden dividirse en dos categorías principales: entrega y visualización. Para solucionar los problemas por los que un mensaje dentro de la aplicación no se ha mostrado en tu dispositivo, confirma que el <a id="troubleshooting-in-app-message-delivery">mensaje dentro de la aplicación se ha entregado al dispositivo</a> y, a continuación, <a id="troubleshooting-in-app-message-display">soluciona el problema de la visualización del mensaje</a>.

### Solución de problemas de entrega {#troubleshooting-in-app-message-delivery}

El SDK solicita mensajes dentro de la aplicación a los servidores Braze al iniciar la sesión. Para comprobar si los mensajes dentro de la aplicación se entregan a tu dispositivo, tendrás que asegurarte de que los mensajes dentro de la aplicación son solicitados por el SDK y devueltos por los servidores Braze.

#### Comprueba si se solicitan y devuelven mensajes

1. Añádase como [usuario de prueba]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) en el panel.
2. Configura una campaña de mensajes dentro de la aplicación dirigida a tu usuario.
3. Asegúrate de que se produce una nueva sesión en tu aplicación.
4. Utiliza el [registro de usuarios del evento]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar que tu dispositivo solicita mensajes dentro de la aplicación al iniciar la sesión. Busca la solicitud SDK asociada al evento de inicio de sesión de tu usuario de prueba.
  - Si tu aplicación debía solicitar mensajes dentro de la aplicación desencadenados, deberías ver `trigger` en el campo **Respuestas solicitadas**, en **Datos de respuesta**.
  - Si tu aplicación debía solicitar mensajes originales dentro de la aplicación, deberías ver `in_app` en el campo **Respuestas solicitadas**, en **Datos de respuesta**.
5. Utiliza los [registros de usuarios del evento]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para comprobar si se devuelven los mensajes dentro de la aplicación correctos en los datos de respuesta.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Solución de problemas de mensajes no solicitados

Si tus mensajes dentro de la aplicación no se solicitan, es posible que tu aplicación no esté haciendo un seguimiento correcto de las sesiones, ya que los mensajes dentro de la aplicación se actualizan al iniciar la sesión. Además, asegúrate de que tu aplicación está iniciando realmente una sesión según la semántica de tiempo de espera de sesión de tu aplicación:

![La solicitud SDK encontrada en los registros de usuarios del evento que muestra un evento de inicio de sesión con éxito.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Solución de problemas de mensajes no devueltos

Si tus mensajes dentro de la aplicación no se devuelven, es probable que estés experimentando un problema de orientación de la campaña:

1. Tu segmento no contiene a tu usuario.
  - Comprueba la pestaña [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) de tu usuario para ver si aparece el segmento correcto en **Segmentos**.
2. Tu usuario ha recibido previamente el mensaje dentro de la aplicación y no era elegible para volver a recibirlo.
  - Comprueba la [configuración de elegibilidad de la campaña]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) en el paso **Entrega** del **Compositor de campañas** y asegúrate de que la configuración de elegibilidad se ajusta a tu configuración de pruebas.
3. Tu usuario alcanzó el límite de frecuencia de la campaña.
  - Comprueba la configuración de la campaña [límite de frecuencia]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) y asegúrate de que coincide con la configuración de tus pruebas.
4. Si había un grupo de control en la campaña, tu usuario puede haber caído en el grupo de control.
  - Puedes comprobar si esto ha ocurrido creando un segmento con un filtro de variante de campaña recibida, en el que la variante de campaña esté configurada como **Control**, y comprobando si tu usuario cayó en ese segmento.
  - Cuando crees campañas para realizar pruebas de integración, asegúrate de no añadir un grupo de control.


### Pantalla de solución de problemas {#troubleshooting-in-app-message-display}

Si tu aplicación solicita y recibe correctamente mensajes dentro de la aplicación, pero no se muestran, es posible que la lógica del dispositivo esté impidiendo la visualización:

1. ¿Se desencadena el evento como se espera? Para comprobarlo, intenta configurar el mensaje para que se desencadene mediante una acción diferente (como el inicio de sesión) y comprueba si se muestra.
{% if include.sdk == "iOS" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), predeterminado en 30 segundos.
{% elsif include.sdk == "Android" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), predeterminado en 30 segundos.
{% elsif include.sdk == "Web" %}
2. Los mensajes desencadenados dentro de la aplicación tienen una tasa limitada en función del [intervalo de tiempo mínimo entre desencadenamientos]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), predeterminado en 30 segundos.
{% endif %}
3. Las descargas de imágenes fallidas impedirán que se muestren los mensajes dentro de la aplicación con imágenes. Comprueba los registros de tu dispositivo para asegurarte de que las descargas de imágenes no fallan. Prueba a eliminar temporalmente la imagen de tu mensaje para ver si así se muestra.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Si has configurado un delegado para personalizar la gestión de mensajes dentro de la aplicación, comprueba tu delegado para asegurarte de que no está afectando a la visualización de mensajes dentro de la aplicación.
  {% when "Web" %}
5. Si tienes una gestión personalizada de mensajes dentro de la aplicación a través de `braze.subscribeToInAppMessage` o `appboy.subscribeToNewInAppMessages`, comprueba esa suscripción para asegurarte de que no está afectando a la visualización de mensajes dentro de la aplicación.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Si la orientación del dispositivo no coincide con la orientación especificada por el mensaje dentro de la aplicación, el mensaje dentro de la aplicación no se mostrará. Asegúrate de que tu dispositivo está en la orientación correcta.
{% endcase %}
7. Si tu mensaje dentro de la aplicación se desencadena al iniciar la sesión y has configurado un tiempo de espera de sesión ampliado, esto afectará a la rapidez con la que puedes mostrar mensajes. Por ejemplo, si el tiempo de espera de tu sesión está configurado en 300 segundos, cerrar y volver a abrir la aplicación en menos de ese tiempo no actualizará la sesión, por lo que un mensaje dentro de la aplicación desencadenado por el inicio de una sesión no se mostrará.

