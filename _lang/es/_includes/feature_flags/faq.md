# Preguntas más frecuentes

> Este artículo responde a algunas preguntas frecuentes sobre las banderas de características.

## Funcionalidad y soporte

### ¿En qué plataformas se admiten las feature flags de Braze? {#platforms}

Braze admite feature flags en plataformas iOS, Android y Web con los siguientes requisitos de versión del SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

¿Necesitas asistencia en otras plataformas? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### ¿Cuál es el nivel de esfuerzo necesario para implantar una feature flag? {#level-of-effort}

Se puede crear e integrar una bandera de características en pocos minutos. 

La mayor parte del esfuerzo tendrá que ver con tu equipo de ingeniería y la construcción de la nueva característica que piensas lanzar. Pero cuando se trata de añadir una feature flag, es tan sencillo como una declaración `IF`/`ELSE` en el código de tu aplicación o sitio web:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### ¿Cómo pueden beneficiar las feature flags a los equipos de marketing? {#marketing-teams}

Los equipos de marketing pueden utilizar banderas de características para coordinar los anuncios de productos (como los correos electrónicos de lanzamiento de productos) cuando una característica sólo está habilitada para un pequeño porcentaje de usuarios.

Por ejemplo, con las banderas de características Braze, puedes desplegar un nuevo programa de fidelización de clientes al 10% de los usuarios de tu aplicación, y enviar un correo electrónico, push u otro tipo de mensajería a ese mismo 10% de usuarios habilitados utilizando el paso en Canvas de la bandera de características. 

### ¿Cómo pueden beneficiar las feature flags a los equipos de producto? {#product-teams}

Los equipos de producto pueden utilizar indicadores de características para realizar despliegues graduales o lanzamientos suaves de nuevas características con el fin de controlar los indicadores clave de rendimiento y las opiniones de los clientes antes de ponerlas a disposición de todos los usuarios.

Los equipos de producto pueden utilizar [las propiedades de las banderas de características]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) para rellenar a distancia el contenido de una aplicación, como vínculos profundos, texto, imágenes u otros contenidos dinámicos.

Utilizando el paso en Canvas Bandera de características, los equipos de producto también pueden realizar una prueba de división A/B para medir cómo afecta una nueva característica a las tasas de conversión en comparación con los usuarios que tienen la característica desactivada. 

### ¿Cómo pueden beneficiar las banderas de características a los equipos de ingeniería? {#engineering-teams}

Los equipos de ingeniería pueden utilizar banderas de características para reducir el riesgo inherente al lanzamiento de nuevas características y evitar apresurarse a desplegar correcciones de código en mitad de la noche.

Al liberar nuevo código oculto tras una bandera de característica, tu equipo puede activar o desactivar la característica de forma remota desde el panel de Braze, evitando el retraso de enviar nuevo código o esperar la aprobación de una actualización de la tienda de aplicaciones.

## Despliegue y segmentación de características

### ¿Puede desplegarse una bandera de característica sólo a un grupo selecto de usuarios? {#target-users}

Sí, crea un segmento en Braze dirigido a usuarios específicos por dirección de correo electrónico, `user_id`, o cualquier otro atributo de tus perfiles de usuario. A continuación, despliega la bandera de características para el 100% de ese segmento.

### ¿Cómo afecta el ajuste del porcentaje de despliegue a los usuarios que antes estaban agrupados en el grupo habilitado? {#random-buckets}

Los despliegues de la bandera de características siguen siendo coherentes para los usuarios en todos los dispositivos y sesiones.

- Cuando una bandera de característica se despliega al 10% de los usuarios aleatorios, ese 10% permanecerá habilitado y persistirá durante la vida de esa bandera de característica.
- Si aumentas el despliegue del 10% al 20%, el mismo 10% seguirá habilitado, y además se añadirá un nuevo 10% adicional de usuarios al grupo habilitado.
- Si reduces el despliegue del 20 % al 10 %, solo quedará habilitado el 10 % original de los usuarios.

Esta estrategia ayuda a garantizar que los usuarios tengan una experiencia coherente en tu aplicación y no vayan y vengan de una sesión a otra. Por supuesto, desactivar una característica hasta el 0% eliminará a todos los usuarios de la bandera de características, lo que resulta útil si descubres un error o necesitas desactivar la característica por completo.

## Temas técnicos

### ¿Se pueden utilizar feature flags para controlar cuándo se inicializa el SDK de Braze? {#initialization}

No, el SDK debe inicializarse para descargar y sincronizar las feature flags del usuario actual. Esto significa que no puedes utilizar banderas de características para limitar qué usuarios se crean o se siguen en Braze.

### ¿Con qué frecuencia actualiza el SDK las feature flags? {#refresh-frequency}

Las banderas de características se actualizan al iniciar la sesión y al cambiar de usuario activo. Las feature flags también pueden actualizarse manualmente mediante el [método de actualización]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing) del SDK. La tasa de actualización de las banderas de características está limitada a una vez cada CINCO minutos (sujeto a cambios).

Ten en cuenta que las buenas prácticas de datos recomiendan no actualizar las banderas de características demasiado rápido (con una posible limitación de tasa si se hace así), por lo que es mejor actualizar sólo antes de que un usuario interactúe con nuevas características o periódicamente en la aplicación si es necesario.

### ¿Están disponibles las banderas de características mientras un usuario está desconectado? {#offline}

Sí, después de actualizar las banderas de características, se almacenan localmente en el dispositivo del usuario y se puede acceder a ellas sin conexión.

### ¿Qué ocurre si las banderas de características se actualizan a mitad de sesión? {#listen-for-updates}

Las banderas de características pueden actualizarse a mitad de sesión. Hay situaciones en las que puedes querer actualizar tu aplicación si cambian determinadas variables o tu configuración. Hay otras situaciones en las que puede que no quieras actualizar tu aplicación, para evitar un cambio impactante en la forma en que se representa tu interfaz de usuario.

Para controlar esto, [escucha las actualizaciones]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) de las banderas de características y determina si debes volver a renderizar tu aplicación en función de las banderas de características que hayan cambiado. 

### ¿Por qué los usuarios de mi grupo de control global no reciben los experimentos de las banderas de características?

No puedes habilitar los indicadores de características para los usuarios de tu [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/). Esto significa que los usuarios de tu grupo de control global tampoco pueden formar parte de los experimentos con la bandera de características.

## ¿Tienes más preguntas?

¿Tienes preguntas o comentarios? Envía un correo electrónico a nuestro equipo: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

