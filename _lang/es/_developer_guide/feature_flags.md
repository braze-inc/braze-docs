---
page_order: 2.5
nav_title: Conmutador de características
article_title: Banderas de características para el SDK de Braze
description: "Este artículo de referencia ofrece un resumen de los indicadores de características, incluidos los requisitos previos y los casos de uso."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
  - Unity
  - Cordova
  - React Native
  - Flutter
  - Roku

---

# Banderas de características

> Las banderas de características te permiten habilitar o deshabilitar a distancia la funcionalidad para una selección específica o aleatoria de usuarios. Y lo que es más importante, te permiten activar y desactivar una característica en producción sin necesidad de desplegar código adicional ni actualizar la tienda de aplicaciones. Esto te permite desplegar nuevas características con seguridad y confianza.

{% alert tip %}
Cuando estés listo para crear tus propias banderas de características, consulta [Crear banderas de características]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Requisitos previos

Estas son las versiones mínimas del SDK necesarias para empezar a utilizar las banderas de características:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Ejemplos

### Despliegues graduales

Utiliza los indicadores de características para habilitar gradualmente características a una muestra de población. Por ejemplo, puedes hacer un lanzamiento suave de una nueva característica primero a tus usuarios VIP. Esta estrategia ayuda a mitigar los riesgos asociados con el envío de nuevas características a todo el mundo a la vez y ayuda a detectar los errores con antelación.

![Imagen en movimiento del control deslizante de tráfico del rollout pasando del 0% al 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Por ejemplo, digamos que hemos decidido añadir un nuevo enlace de "Asistencia por chat en vivo" a nuestra aplicación para agilizar el servicio al cliente. Podríamos ofrecer esta característica a todos los clientes a la vez. Sin embargo, un lanzamiento amplio conlleva riesgos, como estos: 

* Nuestro equipo de soporte aún está en formación, y los clientes podrán iniciar los tickets de soporte una vez que esté disponible. Esto no nos da margen en caso de que el equipo de soporte necesite más tiempo.
* No estamos seguros del volumen real de nuevos casos de asistencia que recibiremos, por lo que es posible que no contemos con el personal adecuado.
* Si nuestro equipo de soporte está desbordado, no tenemos ninguna estrategia para volver a desactivar rápidamente esta característica.
* Es posible que se introduzcan errores en el widget de chat, y no queremos que los clientes tengan una experiencia negativa.

Con las feature flags de Braze, podemos desplegar la característica gradualmente y mitigar todos estos riesgos:

* Activaremos la característica "Asistencia por chat en vivo" cuando el equipo de soporte diga que está preparado.
* Habilitaremos esta nueva característica sólo para el 10% de los usuarios para determinar si contamos con el personal adecuado.
* Si hay algún error, podemos desactivar rápidamente la característica en lugar de apresurarnos a enviar una nueva versión.

Para desplegar gradualmente esta característica, podemos [crear una bandera de característica]({{site.baseurl}}/developer_guide/feature_flags/create/) llamada "Widget de chat en vivo".

![Detalles de la feature flag de un ejemplo llamado Widget de Chat en vivo. El ID es enable_live_chat. La descripción de esta bandera de característica dice que el widget de chat en vivo se mostrará en la página de soporte.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

En el código de nuestra aplicación, sólo mostraremos el botón **Iniciar chat en vivo** cuando esté habilitada la bandera de la característica Braze:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% endtabs %}

### Controla a distancia las variables de la aplicación

Utiliza banderas de características para modificar la funcionalidad de tu aplicación en producción. Esto puede ser especialmente importante para las aplicaciones móviles, donde las aprobaciones de las tiendas de aplicaciones impiden que los cambios se apliquen rápidamente a todos los usuarios.

Por ejemplo, supongamos que nuestro equipo de marketing quiere incluir nuestras ventas y promociones actuales en la navegación de nuestra aplicación. Normalmente, nuestros ingenieros necesitan una semana de plazo para cualquier cambio y tres días para una revisión en la tienda de aplicaciones. Pero teniendo en cuenta que las fechas de Acción de Gracias, el Viernes Negro, el Ciberlunes, Hanukkah, Navidad y Año Nuevo suceden todas dentro de dos meses, no podremos cumplir estos plazos tan ajustados.

Con las banderas de características, podemos dejar que Braze controle el contenido del enlace de navegación de nuestra aplicación, permitiendo a nuestro administrador de marketing hacer cambios en cuestión de minutos en lugar de días.

Para configurar remotamente esta característica, crearemos una nueva bandera de característica llamada `navigation_promo_link` y definiremos las siguientes propiedades iniciales:

![Bandera de característica con propiedades de enlace y texto que dirigen a una página de ventas genérica.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

En nuestra aplicación, utilizaremos métodos getter de Braze para recuperar las propiedades de esta bandera de característica y construir los enlaces de navegación basándonos en esos valores:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% endtabs %}

Ahora, el día antes de Acción de Gracias, sólo tenemos que cambiar esos valores de propiedad en el panel de Braze.

![Bandera de características con propiedades de enlace y texto que dirigen a una página de ventas de Acción de Gracias.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Como resultado, la próxima vez que alguien cargue la aplicación, verá las nuevas ofertas de Acción de Gracias.

### Coordinación de mensajes

Utiliza banderas de características para sincronizar el despliegue y la mensajería de una característica. Esto te permitirá utilizar Braze como fuente de verdad tanto para tu experiencia de usuario como para su mensajería relevante. Para conseguirlo, dirige la nueva característica a un segmento concreto o a una parte filtrada de tu audiencia. Después, crea una campaña o Canvas que solo se dirija a ese segmento. 

Supongamos que lanzamos un nuevo programa de recompensas de fidelización para nuestros usuarios. Puede ser difícil para los equipos de marketing y producto coordinar perfectamente el momento de la mensajería promocional con el lanzamiento de una característica. Los indicadores de características en Canvas te permiten aplicar una lógica sofisticada a la hora de habilitar una característica para una audiencia seleccionada y controlar la mensajería relacionada para esos mismos usuarios.

Para coordinar eficazmente el despliegue de características y la mensajería, crearemos una nueva feature flag llamada `show_loyalty_program`. Para nuestro lanzamiento inicial por fases, dejaremos que Canvas controle cuándo y para quién se habilita la bandera de la característica. Por ahora, dejaremos el porcentaje de despliegue en 0% y no seleccionaremos ningún segmento de destino.

![Una feature flag con el nombre Programa de recompensas por fidelización. El ID es show_loyalty_program, y la descripción que esto muestra el nuevo programa de recompensas de fidelización en la pantalla de inicio y en la página de perfil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

A continuación, en el Flujo de Canvas, crearemos un [paso de Feature flag]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) que habilite la feature flag `show_loyalty_program` para nuestro segmento "Clientes de alto valor":

![Un ejemplo de Canvas con un paso en Canvas de segmentación de audiencia en el que el segmento de clientes de alto valor activa la bandera de la característica show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Ahora, los usuarios de este segmento empezarán a ver el nuevo programa de fidelización y, una vez habilitado, se enviarán automáticamente un correo electrónico y un cuestionario para ayudar a nuestro equipo a recabar opiniones.

### Experimentación de características

Utiliza las banderas de características para experimentar y confirmar tus hipótesis en torno a tu nueva característica. Al dividir el tráfico en dos o más grupos, puedes comparar el impacto de una bandera de característica en todos los grupos, y determinar el mejor curso de acción en función de los resultados.

Una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) es una potente herramienta que compara las respuestas de los usuarios a múltiples versiones de una variable.

En este ejemplo, nuestro equipo ha creado un nuevo flujo de pago para nuestra aplicación de comercio electrónico. Aunque estamos seguros de que mejora la experiencia del usuario, queremos hacer una prueba A/B para medir su impacto en los ingresos de nuestra aplicación.

Para empezar, crearemos una nueva feature flag llamada `enable_checkout_v2`. No añadiremos un porcentaje de audiencia o de lanzamiento. En su lugar, utilizaremos un experimento de señalización de características para dividir el tráfico, habilitar la característica y medir el resultado.

En nuestra aplicación, comprobaremos si la bandera de característica está habilitada o no y cambiaremos el flujo de pago en función de la respuesta:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Configuraremos nuestra prueba A/B en un [Experimento de bandera de características]({{site.baseurl}}/developer_guide/feature_flags/experiments/).

Ahora, el 50% de los usuarios verán la experiencia antigua, mientras que el otro 50% verá la experiencia nueva. A continuación, podemos analizar las dos variantes para determinar qué flujo de pago dio lugar a una mayor tasa de conversión. {% multi_lang_include metrics.md metric='Conversion Rate' %}

![Un experimento de bandera de características que divide el tráfico en dos grupos del 50%.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Una vez determinado el ganador, podemos detener esta campaña y aumentar el porcentaje de despliegue de la característica al 100% para todos los usuarios, mientras nuestro equipo de ingeniería la codifica en la próxima versión de la aplicación.

### Segmentación

Utiliza el filtro Bandera de **características** para crear un segmento o dirigir la mensajería a los usuarios en función de si tienen habilitada una bandera de características. Por ejemplo, supongamos que tenemos una bandera de característica que controla el contenido premium en nuestra aplicación. Podríamos crear un segmento que filtrara a los usuarios que no tienen habilitada la bandera de característica, y luego enviar a ese segmento un mensaje instándoles a actualizar su cuenta para ver contenido premium.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Para más información sobre cómo filtrar por segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Para evitar segmentos recursivos, no es posible crear un segmento que haga referencia a otras banderas de características.
{% endalert %}

## Limitaciones del plan

Estas son las limitaciones de la bandera de características para los planes gratuitos y de pago.

| Característica                                                                                                   | Versión gratuita     | Versión de pago      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Banderas de características activas](#active-feature-flags)                                                                     | 10 por espacio de trabajo | 110 por espacio de trabajo |
| [Experimentos activos de campaña]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 por espacio de trabajo  | 100 por espacio de trabajo |
| [Pasos en Canvas de feature flag]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Sin límites        | Sin límites         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se considera que una bandera de característica está activa y contará para tu límite si se da alguna de las siguientes circunstancias:

- La difusión es superior al 0%.
- Utilizado en un Canvas activo
- Utilizado en un experimento activo

Aunque la misma bandera de característica coincida con varios criterios, por ejemplo si se utiliza en un Canvas y el despliegue es del 50%, sólo contará como 1 bandera de característica activa para tu límite.

{% alert note %}
Para adquirir la versión de pago de las banderas de características, ponte en contacto con tu administrador de cuentas Braze o solicita una actualización en el panel Braze.
{% endalert %}
