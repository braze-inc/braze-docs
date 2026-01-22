
{% tab android %}
Braze ofrece varios tipos predeterminados de mensajes dentro de la aplicación, cada uno personalizable con mensajes, imágenes, iconos [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), acciones de clic, análisis, esquemas de color y mucho más.

Su comportamiento y rasgos básicos están definidos por la interfaz [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) en una subclase llamada [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). `IInAppMessage` también incluye una subinterfaz, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)que te permite añadir a tu aplicación [botones de](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) cierre, clic-acción y análisis.

{% alert important %}
Ten en cuenta que los mensajes dentro de la aplicación que contengan botones incluirán el mensaje `clickAction` en la carga útil final si la acción de clic se añade antes de añadir el texto del botón.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) Los mensajes dentro de la aplicación se llaman así porque "se deslizan hacia arriba" o "se deslizan hacia abajo" desde la parte superior o inferior de la pantalla. Cubren una pequeña parte de la pantalla y proporcionan una capacidad de mensajería eficaz y no intrusiva.

El objeto de mensaje dentro de la aplicación `slideup` extiende [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Un mensaje dentro de la aplicación que se desliza desde la parte inferior de la pantalla de un teléfono y que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en la esquina inferior derecha de una página Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) Los mensajes dentro de la aplicación aparecen en el centro de la pantalla y están enmarcados por un panel translúcido. Son útiles para una mensajería más crítica y pueden equiparse con dos botones de acción de clic y habilitación de análisis.

Este tipo de mensaje es una subclase de [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)una clase abstracta que implementa `IInAppMessageImmersive`, dándote la opción de añadir funcionalidad personalizada a tus mensajes dentro de la aplicación generados localmente.

![Un mensaje modal dentro de la aplicación en el centro de una pantalla de teléfono que muestra "Los humanos somos complicados". La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en el centro de una página web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) Los mensajes dentro de la aplicación son útiles para maximizar el contenido y el impacto de tu comunicación con el usuario. La mitad superior de un mensaje dentro de la aplicación `full` contiene una imagen, y la mitad inferior muestra texto y hasta dos botones de acción de clic y habilitación de análisis.

Este tipo de mensaje amplía [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)ofreciéndote la posibilidad de añadir funciones personalizadas a tus mensajes dentro de la aplicación generados localmente.

![Un mensaje dentro de la aplicación a pantalla completa que se muestra en toda la pantalla del teléfono y que dice: "Los humanos somos complicados. La interacción personalizada no debería serlo". En el fondo se muestra el mismo mensaje dentro de la aplicación en gran parte en el centro de una página web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) Los mensajes dentro de la aplicación son útiles para crear contenido de usuario totalmente personalizado. El contenido HTML de los mensajes dentro de la aplicación, definido por el usuario, se muestra en `WebView` y puede contener opcionalmente otros contenidos enriquecidos, como imágenes y fuentes, lo que permite un control total sobre el aspecto y la funcionalidad de los mensajes.

Este tipo de mensaje implementa [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)que es una subclase de [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

Los mensajes dentro de la aplicación Android admiten una interfaz JavaScript `brazeBridge` para llamar a métodos del SDK de Android Braze desde dentro de tu HTML, consulta nuestra página de <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">puente JavaScript</a> para más detalles.

![Un mensaje HTML dentro de la aplicación con un carrusel de contenido y botones interactivos.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actualmente no admitimos la visualización de mensajes HTML personalizados dentro de la aplicación en un iFrame en las plataformas iOS y Android.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
También puedes definir vistas de mensajes dentro de la aplicación personalizadas para tu aplicación. Para un recorrido completo, consulta [Configurar fábricas personalizadas]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories).
{% endalert %}
{% endtab %}