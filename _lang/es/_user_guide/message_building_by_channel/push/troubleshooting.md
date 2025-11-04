---
nav_title: Solución de problemas
article_title: Solución de problemas Push
page_order: 23
page_type: reference
description: "Esta página contiene pasos para la solución de problemas relacionados con el canal de mensajería push."
channel: push
---

# Solución de problemas Push

> Esta página te ayuda a solucionar varios problemas que puedas experimentar con el canal de mensajería Push.

## Faltan notificaciones push

¿Tienes problemas de entrega con las notificaciones push? Hay una serie de pasos que puedes dar para solucionar este problema, comprobando el:

- [Estado de la suscripción push](#push-subscription-status)
- [Segmento](#segment)
- [Tapas de notificación push](#push-notification-caps)
- [Límites de velocidad](#rate-limits)
- [Estado del grupo de control](#control-group-status)
- [Token de notificaciones push válido](#valid-push-token)
- [Tipo de notificación push](#push-notification-type)
- [Aplicación Currents](#current-app)

#### Estado de la suscripción push

Los push sólo pueden enviarse a usuarios suscritos o con adhesión voluntaria. Comprueba tu perfil de usuario en la pestaña [Interacción]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) de la sección **Perfil de usuario** para confirmar si estás registrado activamente para push en el espacio de trabajo que estás probando. Si estás registrado para varias aplicaciones, las encontrarás listadas en el campo **Push registrado para**:

\![Push Registrado para]({% image_buster /assets/img_archive/trouble1.png %})

También puedes exportar los perfiles de usuario utilizando los puntos finales de exportación Braze:
- [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Cualquiera de los dos puntos finales devolverá un objeto token de notificaciones push que incluye información de habilitación push por dispositivo.

#### Segmento

Asegúrate de que entras en el segmento al que te diriges (si se trata de una campaña en vivo y no de una prueba). En el **perfil de usuario**, verás una lista de los segmentos en los que se encuentra actualmente el usuario. Recuerda que se trata de una variable en constante cambio, ya que la segmentación se actualiza en tiempo real.

\![Lista de segmentos]({% image_buster /assets/img_archive/trouble2.png %})

También puedes confirmar que el usuario forma parte del segmento utilizando **la Búsqueda de usuarios** al crear un segmento.

Sección de búsqueda de usuarios con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Tapas de notificación push

Comprueba los límites globales de frecuencia. Es posible que no recibieras la notificación push porque tu espacio de trabajo tiene establecida una limitación de frecuencia global y ya has alcanzado el límite de notificaciones push para el periodo de tiempo especificado.

Puedes hacerlo activando la [limitación de frecuencia global]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) en el panel. Si la campaña está configurada para cumplir las normas de limitación de frecuencia, habrá una serie de usuarios afectados por esta configuración

Detalles de la campaña]({% image_buster /assets/img_archive/trouble3.png %})

#### Límites de velocidad

Si tienes configurado un límite de velocidad para tu campaña o Canvas, es posible que dejes de recibir mensajería por superar este límite. Para más información, consulta [Limitación de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Estado del grupo de control

Si se trata de una campaña de un solo canal o de un Canvas con un grupo de control, es posible que estés cayendo en el grupo de control.

  1. Comprueba la [distribución de variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) para ver si hay un grupo de control.
  2. Si es así, crea un segmento filtrando por [en grupo de control de campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), luego [exporta el segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) y comprueba si tu ID de usuario está en esta lista.

#### Token de notificaciones push válido
Un token de notificaciones push es un identificador que los remitentes utilizan para dirigirse a dispositivos específicos con una notificación push. Por tanto, si el dispositivo no tiene un token de notificaciones push válido, no hay forma de enviarle una notificación push. 

#### Tipo de notificación push

Comprueba que estás utilizando el tipo correcto de notificación push. Por ejemplo, si quieres dirigirte a un FireTV, entonces utilizarías una notificación push de Kindle, no una campaña push de Android. Del mismo modo, si quieres dirigirte a un Android, utiliza una notificación push de Android y no una campaña push de iOS. Consulta los siguientes artículos para obtener más información sobre el flujo de trabajo de Braze:
- [Notificación push de Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Mensajería en la nube Firebase]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aplicación Currents

Cuando pruebes envíos push con usuarios internos, asegúrate de que el usuario que quieres que reciba la notificación push ha iniciado sesión en la aplicación correspondiente. Esto puede hacer que el usuario no reciba un push o reciba un push para el que crees que no está segmentado.

## Los clics push se abren inesperadamente en la aplicación

Si tienes problemas con los enlaces de las notificaciones push que se abren inesperadamente en tu aplicación en lugar de en tu navegador Web, puede que haya un problema con la configuración de tu campaña o con la implementación del SDK. Consulta estos pasos para obtener ayuda.

### Verificar el comportamiento al hacer clic

En tu campaña o paso en Canvas, comprueba que la opción **Abrir URL Web dentro de la aplicación móvil** no está seleccionada. Si es así, borra la selección y relánzala. 

\!["Comportamiento al hacer clic" campo de configuración de un push establecido en "Abrir URL web" con "Abrir URL web dentro de la aplicación móvil" sin marcar.]({% image_buster /assets/img/push_on_click.png %})

La interacción predeterminada para el comportamiento al hacer clic "Abrir URL Web" difiere según la versión del SDK. Para las versiones del SDK iOS 2.29.0 y Android 2.0.0 y superiores, esta opción está seleccionada por defecto y las URL web se abrirán en una vista web dentro de la aplicación. Antes de estas versiones, esta opción estaba desactivada por defecto y las URL web se abrían en el navegador web predeterminado del dispositivo.

Si este no es el problema, puede que haya un problema con tu implementación de push. 

### Doble comprobación de la integración push

Si los enlaces de tus notificaciones push se abren en la aplicación de forma inesperada, puede deberse a problemas con la integración de tus notificaciones push o con tu configuración personalizada. Sigue estos pasos para solucionar problemas:

1. **Revisa la implementación del delegado push:** Asegúrate de que el delegado push de Braze se implementa correctamente. Para obtener instrucciones detalladas, consulta la guía de integración de notificaciones push de tu [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecciona el manejo personalizado de los enlaces:** Comprueba si la aplicación incluye un tratamiento personalizado para todos los enlaces `https://`. Las configuraciones personalizadas pueden anular los comportamientos predeterminados. Colabora con tu equipo de desarrolladores para revisar y ajustar estas configuraciones si es necesario.
3. **Verifica el registro push de iOS:** Para iOS, revisa el paso 1 de la guía de integración push sobre el [registro de notificaciones push con APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Asegúrate de que tu objeto delegado se asigna de forma sincrónica antes de que la aplicación termine de ejecutarse. Este paso debe completarse en el método `application:didFinishLaunchingWithOptions:`.
4. **Prueba tu integración:** Tras realizar los ajustes, prueba el comportamiento de las notificaciones push tanto en dispositivos iOS como Android para confirmar que el problema se ha resuelto.

## Las notificaciones push web no se comportan como se esperaba

Si tienes problemas con las notificaciones push en tu navegador, es posible que tengas que restablecer los permisos de notificación de tu sitio y borrar el almacenamiento del mismo. Consulta estos pasos para obtener ayuda.

{% tabs %}
{% tab Chrome %}

### Restablecer Chrome en el escritorio

1. Junto a tu URL en el navegador Chrome, selecciona el icono deslizante **Ver información del sitio**.
2. En **Notificaciones**, selecciona **Restablecer permiso**.
3. Abre Chrome DevTools. A continuación se indican los atajos relevantes por sistema operativo.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Atajos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. En DevTools, ve a la pestaña **Aplicación**.
5\. En la barra lateral, selecciona **Almacenamiento**.
6\. Selecciona **Borrar datos del sitio**.
7\. Chrome te pedirá que vuelvas a cargar la página para aplicar la configuración actualizada. Selecciona **Recargar**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

### Reiniciar Chrome en Android

Si tienes una notificación de tu sitio visible en el cajón de notificaciones de tu Android:

1. Desde la notificación push, pulsa <i class="fas fa-cog" title="Configuración"></i> y selecciona **Configuración del sitio**.
2. En **Configuración del sitio**, pulsa **Borrar & Restablecer**.

Si no tienes una notificación de tu sitio abierta:

1. Abre Chrome en Android.
2. Pulsa en el menú <i class="fas fa-ellipsis-vertical"></i>.
3. Ve a **Configuración** > **Configuración del sitio** > Notificaciones.
4. Comprueba que las notificaciones están configuradas en **Preguntar antes de enviar (recomendado)**.
5. Encuentra tu sitio en la lista.
6. Selecciona la entrada y pulsa **Borrar y Restablecer**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

{% endtab %}
{% tab Firefox %}

### Reiniciar Firefox en el escritorio

1. Junto a la URL de tu sitio, selecciona <i class="fa-solid fa-circle-info" alt="info icon"></i> o <i class="fas fa-lock" alt="lock icon"></i>.
2. En **Permisos**, junto a **Recibir notificaciones**, selecciona <i class="fa-solid fa-circle-xmark" title="Borrar este permiso y volver a preguntar"></i> para borrar los permisos de notificación.
3. En el mismo menú, selecciona **Borrar cookies y datos del sitio**.
4. En el cuadro de diálogo para confirmar tu elección, selecciona **Aceptar**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

### Reiniciar Firefox en Android

Para restablecer los permisos push en Android, consulta este [artículo de soporte de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Reiniciar Safari en macOS

{% alert note %}
Estos pasos son sólo para macOS, ya que Apple no admite Web Push para Safari en Windows.
{% endalert %}

1. Abre Safari.
2. [En la barra de menús del Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), ve a **Safari** > **Configuración** > **Sitios web** > Notificaciones.
3. Selecciona tu centro de la lista.
4. Selecciona **Eliminar** para suprimir los permisos de notificación del sitio.
5. A continuación, ve a **Privacidad** > **Gestionar datos del sitio web**.
6. Selecciona tu centro de la lista.
7. Selecciona **Eliminar**, o para eliminar todos los datos del sitio, selecciona **Eliminar todo**.
8. Selecciona **Hecho**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

{% endtab %}
{% endtabs %}

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

