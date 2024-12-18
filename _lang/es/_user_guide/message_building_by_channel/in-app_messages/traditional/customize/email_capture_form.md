---
nav_title: Formulario de captura de correo electrónico
article_title: Formulario de captura de correo electrónico
page_order: 3
page_type: reference
description: "Este artículo ofrece una visión general del tipo de mensaje in-app de captura de correo electrónico."
channel:
  - in-app messages
---

# Formulario de captura de correo electrónico {#email-capture-form}

> Los mensajes de captura de correo electrónico le permiten solicitar fácilmente a los usuarios de su sitio que envíen su dirección de correo electrónico, tras lo cual estará disponible en su perfil de usuario para utilizarla en todas sus campañas de mensajería.

Cuando un usuario final introduce su dirección de correo electrónico en este formulario, la dirección de correo electrónico se añadirá a su perfil de usuario.

- En el caso de [los usuarios]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) anónimos que aún no tengan una cuenta, la dirección de correo electrónico aparecerá en el perfil de usuario anónimo vinculado al dispositivo del usuario.
- Si ya existe una dirección de correo electrónico en el perfil del usuario, la dirección de correo electrónico existente se sobrescribirá con la nueva dirección de correo electrónico introducida.
- Si el usuario conocido tiene una dirección de correo electrónico marcada como [rebotada]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces), comprobaremos si la dirección de correo electrónico recién introducida difiere de la que figura en su perfil de Braze. Si la dirección de correo electrónico proporcionada es diferente, se actualizará la dirección de correo electrónico y se eliminará el estado de rebote duro. 
- Si un usuario introduce una dirección de correo electrónico no válida, verá un mensaje de error: "Por favor, introduzca un correo electrónico válido".
    - Direcciones de correo electrónico no válidas: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - Direcciones de correo electrónico válidas: 
        - `example@gmail.com`
        - `example@gnail.com` (con una errata)
    - Para obtener más información sobre la validación de correo electrónico en Braze, consulte [Directrices y notas técnicas sobre correo electrónico]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation/).

{% details Más sobre usuarios identificados frente a anónimos %}

En general, la lógica del formulario de captura de correo electrónico es sencilla. Establecerá la dirección de correo electrónico en el perfil de usuario en Braze para el usuario que está activo actualmente. Sin embargo, eso significa que el comportamiento difiere en función de si el usuario está identificado (conectado, llamada a `changeUser` ) o no.

Si un usuario anónimo introduce su correo electrónico en el formulario y lo envía, Braze añade la dirección de correo electrónico a su perfil. Si se llama a `changeUser` más adelante en su recorrido por la web y se asigna un nuevo `external_id` (como cuando un nuevo usuario se registra en el servicio), se fusionan todos los datos del perfil del usuario anónimo, incluida la dirección de correo electrónico.

Si se llama a `changeUser` con un `external_id` existente, el perfil de usuario anónimo queda huérfano y se fusionan [los campos de datos específicos del perfil de usuario]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior) que no existan ya en el usuario identificado, pero se pierden los campos que ya existan, incluida la dirección de correo electrónico.

Para más información, consulte el [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## Paso 1: Crear una campaña de mensajes in-app

Para acceder a esta opción, debe crear una campaña de mensajería in-app. A partir de ahí, en función de su caso de uso, establezca **Enviar a** en **Navegadores web**, **Aplicaciones móviles** o **Aplicaciones móviles y Navegadores web**, y seleccione **Formulario de captura de correo electrónico** como **Tipo de mensaje**.

![][4]

{% alert note %}
Para habilitar los mensajes HTML dentro de la aplicación a través del SDK Web, debes proporcionar la opción de inicialización `allowUserSuppliedJavascript` a Braze, por ejemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Esto es por razones de seguridad, ya que los mensajes dentro de la aplicación en HTML pueden ejecutar JavaScript, por lo que requerimos que un mantenedor del sitio los habilite.
{% endalert %}

## Paso 2: Personalizar el formulario {#customizable-features}

A continuación, personalice el formulario según sea necesario. Puede personalizar las siguientes características para su formulario de captura de correo electrónico:

- Encabezado, cuerpo y texto del botón de envío
- Una imagen opcional
- Un enlace opcional a las "Condiciones del servicio
- Diferentes colores para el encabezado y el cuerpo del texto, los botones y el fondo
- Pares clave-valor
- Estilo para el texto del encabezado y del cuerpo, los botones, el color del borde de los botones, el fondo y la superposición.

![Compositor para formulario de captura de correo electrónico.][5]

Si necesita una mayor personalización, elija **Código personalizado** para su **Tipo de mensaje**. Puede utilizar esta [plantilla modal de captura de correo electrónico](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal) del repositorio [Braze Templates](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub como código de inicio.

## Paso 3: Configura tu audiencia de entrada

Si sólo desea enviar este formulario a usuarios sin dirección de correo electrónico, utilice el filtro `Email Available is false`.

![Filtrar por correo electrónico disponible es falso][10]{: style="max-width:50%"}

Si sólo desea enviar este formulario a usuarios sin ID externo (usuarios anónimos), utilice el filtro `External User ID is blank`.

![El filtro por ID de usuario externo está en blanco][11]{: style="max-width:50%"}

Si lo deseas, también puedes combinar los dos filtros utilizando la lógica `AND`.

## Paso 4: Usuarios objetivo que rellenaron el formulario (opcional)

Una vez que haya lanzado el formulario de captura de correo electrónico y recopilado las direcciones de correo electrónico de sus usuarios, puede dirigirse a esos usuarios con el filtro `Clicked/Opened Campaign`. 

Configure el filtro en `Has clicked in-app message button 1` para la campaña `<CAMPAIGN_NAME>`. Sustituya `<CAMPAIGN_NAME>` por el nombre de su campaña de formulario de captura de correo electrónico.

![Filtro de ha hecho clic en el botón de mensaje in-app 1 para su campaña de formulario de captura de correo electrónico web][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}
