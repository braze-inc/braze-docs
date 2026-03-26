# Conmutadores de características

> Los conmutadores de características te permiten habilitar o deshabilitar a distancia la funcionalidad para una selección específica o aleatoria de usuarios. Y lo que es más importante, te permiten activar y desactivar una característica en producción sin necesidad de desplegar código adicional ni actualizar la tienda de aplicaciones. Esto te permite desplegar nuevas características con seguridad y confianza.

{% alert tip %}
Cuando estés listo para crear tus propios conmutadores de características, consulta [Crear conmutadores de características]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Requisitos previos

Estas son las versiones mínimas del SDK necesarias para empezar a utilizar los conmutadores de características:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Casos de uso

### Despliegues graduales

Utiliza los conmutadores de características para habilitar gradualmente características a una muestra de población. Por ejemplo, puedes hacer un lanzamiento suave de una nueva característica primero a tus usuarios VIP. Esta estrategia ayuda a mitigar los riesgos asociados con el envío de nuevas características a todo el mundo a la vez y ayuda a detectar errores con antelación.

![Imagen en movimiento del control deslizante de tráfico de despliegue pasando de 0% a 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Por ejemplo, supongamos que hemos decidido añadir un nuevo enlace de "Asistencia por chat en vivo" a nuestra aplicación para agilizar el servicio al cliente. Podríamos ofrecer esta característica a todos los clientes a la vez. Sin embargo, un lanzamiento amplio conlleva riesgos, como estos: 

* Nuestro equipo de soporte aún está en formación, y los clientes podrán iniciar tickets de soporte una vez que esté disponible. Esto no nos da margen en caso de que el equipo de soporte necesite más tiempo.
* No estamos seguros del volumen real de nuevos casos de asistencia que recibiremos, por lo que es posible que no contemos con el personal adecuado.
* Si nuestro equipo de soporte está desbordado, no tenemos ninguna estrategia para volver a desactivar rápidamente esta característica.
* Es posible que se introduzcan errores en el widget de chat, y no queremos que los clientes tengan una experiencia negativa.

Con los conmutadores de características de Braze, podemos desplegar la característica gradualmente y mitigar todos estos riesgos:

* Activaremos la característica "Asistencia por chat en vivo" cuando el equipo de soporte diga que está preparado.
* Habilitaremos esta nueva característica solo para el 10% de los usuarios para determinar si contamos con el personal adecuado.
* Si hay algún error, podemos desactivar rápidamente la característica en lugar de apresurarnos a enviar una nueva versión.

Para desplegar gradualmente esta característica, podemos [crear un conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/create/) llamado "Widget de chat en vivo".

![Detalles del conmutador de características de un ejemplo llamado Widget de chat en vivo. El ID es enable_live_chat. La descripción de este conmutador de características indica que el widget de chat en vivo se mostrará en la página de asistencia.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

En el código de nuestra aplicación, solo mostraremos el botón **Iniciar chat en vivo** cuando el conmutador de características de Braze esté habilitado:

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
{% tab Swift %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in  
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Controla a distancia las variables de la aplicación

Utiliza conmutadores de características para modificar la funcionalidad de tu aplicación en producción. Esto puede ser especialmente importante para las aplicaciones móviles, donde las aprobaciones de las tiendas de aplicaciones impiden que los cambios se apliquen rápidamente a todos los usuarios.

Por ejemplo, supongamos que nuestro equipo de marketing quiere incluir nuestras ventas y promociones actuales en la navegación de nuestra aplicación. Normalmente, nuestros ingenieros necesitan una semana de plazo para cualquier cambio y tres días para una revisión en la tienda de aplicaciones. Pero teniendo en cuenta que las fechas de Acción de Gracias, el Viernes Negro, el Ciberlunes, Hanukkah, Navidad y Año Nuevo suceden todas dentro de dos meses, no podremos cumplir estos plazos tan ajustados.

Con los conmutadores de características, podemos dejar que Braze controle el contenido del enlace de navegación de nuestra aplicación, permitiendo a nuestro administrador de marketing hacer cambios en cuestión de minutos en lugar de días.

Para configurar remotamente esta característica, crearemos un nuevo conmutador de características llamado `navigation_promo_link` y definiremos las siguientes propiedades iniciales:

![Conmutador de características con propiedades de enlace y texto que dirigen a una página de ventas genérica.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

En nuestra aplicación, utilizaremos métodos getter de Braze para recuperar las propiedades de este conmutador de características y construir los enlaces de navegación basándonos en esos valores:

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
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Ahora, el día antes de Acción de Gracias, solo tenemos que cambiar esos valores de propiedad en el dashboard de Braze.

![Conmutador de características con propiedades de enlace y texto que dirigen a una página de ventas de Acción de Gracias.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Como resultado, la próxima vez que alguien cargue la aplicación, verá las nuevas ofertas de Acción de Gracias.

### Coordinación de mensajes

Utiliza conmutadores de características para sincronizar el despliegue de una característica y la mensajería, y reforzar la colaboración entre los equipos de producto y marketing. Al coordinar los lanzamientos de características y la mensajería a través de conmutadores de características, ambos equipos pueden alinear sus estrategias y crear experiencias de usuario consistentes.

Por ejemplo, supongamos que estamos lanzando un nuevo programa de recompensas de fidelización para nuestros usuarios. Puede ser difícil para los equipos de marketing y producto coordinar perfectamente el momento de la mensajería promocional con el lanzamiento de una característica. Sin embargo, con los conmutadores de características en Canvas, nuestro equipo de producto puede aplicar una lógica sofisticada para habilitar una característica para una audiencia específica, mientras nuestro equipo de marketing controla la mensajería relacionada para esos mismos usuarios.

Para coordinar eficazmente el despliegue de características y la mensajería, crearemos un nuevo conmutador de características llamado `show_loyalty_program`. Para nuestro lanzamiento inicial por fases, dejaremos que Canvas controle cuándo y para quién se habilita el conmutador de características. Por ahora, dejaremos el porcentaje de despliegue en 0% y no seleccionaremos ningún segmento de destino.

![Un conmutador de características con el nombre Programa de recompensas de fidelización. El ID es show_loyalty_program, y la descripción indica que muestra el nuevo programa de recompensas de fidelización en la pantalla de inicio y en la página de perfil.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

A continuación, en Canvas, crearemos un [paso de conmutador de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) que habilite el conmutador de características `show_loyalty_program` para nuestro segmento "Clientes de alto valor":

![Un ejemplo de un Canvas con un paso de división de audiencia en el que el segmento de clientes de alto valor activa el conmutador de características show_loyalty_program.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Ahora, los usuarios de este segmento empezarán a ver el nuevo programa de fidelización y, una vez habilitado, se enviarán automáticamente un correo electrónico y un cuestionario para ayudar a nuestros equipos a recabar opiniones.

### Experimentación de características

Utiliza los conmutadores de características para experimentar y confirmar tus hipótesis en torno a tu nueva característica. Al dividir el tráfico en dos o más grupos, puedes comparar el impacto de un conmutador de características en todos los grupos y determinar el mejor curso de acción en función de los resultados.

Una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) es una potente herramienta que compara las respuestas de los usuarios a múltiples versiones de una variable.

En este ejemplo, nuestro equipo ha creado un nuevo proceso de pago para nuestra aplicación de comercio electrónico. Aunque estamos seguros de que mejora la experiencia del usuario, queremos hacer una prueba A/B para medir su impacto en los ingresos de nuestra aplicación.

Para empezar, crearemos un nuevo conmutador de características llamado `enable_checkout_v2`. No añadiremos un porcentaje de audiencia ni de despliegue. En su lugar, utilizaremos un experimento de conmutador de características para dividir el tráfico, habilitar la característica y medir el resultado.

En nuestra aplicación, comprobaremos si el conmutador de características está habilitado o no y cambiaremos el flujo de pago en función de la respuesta:

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
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Configuraremos nuestra prueba A/B en un [experimento de conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/experiments/).

Ahora, el 50% de los usuarios verán la experiencia antigua, mientras que el otro 50% verá la experiencia nueva. A continuación, podemos analizar las dos variantes para determinar qué proceso de pago ha dado lugar a una tasa de conversión más alta. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Un experimento de conmutador de características que divide el tráfico en dos grupos del 50%.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Una vez determinado el ganador, podemos detener esta campaña y aumentar el porcentaje de despliegue del conmutador de características al 100% para todos los usuarios, mientras nuestro equipo de ingeniería lo codifica en la próxima versión de la aplicación.

### Segmentación

Utiliza el filtro **Conmutador de características** para crear un segmento o dirigir la mensajería a los usuarios en función de si tienen habilitado un conmutador de características. Por ejemplo, supongamos que tenemos un conmutador de características que controla el contenido premium en nuestra aplicación. Podríamos crear un segmento que filtre a los usuarios que no tienen habilitado el conmutador de características, y luego enviar a ese segmento un mensaje instándoles a actualizar su cuenta para ver contenido premium.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Para más información sobre cómo filtrar por segmentos, consulta [Crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Para evitar segmentos recursivos, no es posible crear un segmento que haga referencia a otros conmutadores de características.
{% endalert %}

## Limitaciones del plan

Estas son las limitaciones de los conmutadores de características para los planes gratuitos y de pago.

| Característica                                                                                                   | Versión gratuita     | Versión de pago      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Conmutadores de características activos](#active-feature-flags)                                                                     | 10 por espacio de trabajo | 110 por espacio de trabajo |
| [Experimentos activos de campaña]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 por espacio de trabajo  | 100 por espacio de trabajo |
| [Pasos en Canvas de conmutador de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Sin límites        | Sin límites         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se considera que un conmutador de características está activo y contará para tu límite si se da alguna de las siguientes circunstancias:

- El despliegue es superior al 0%
- Se utiliza en un Canvas activo
- Se utiliza en un experimento activo

Aunque el mismo conmutador de características coincida con varios criterios, por ejemplo si se utiliza en un Canvas y el despliegue es del 50%, solo contará como 1 conmutador de características activo para tu límite.

{% alert note %}
Para adquirir la versión de pago de los conmutadores de características, ponte en contacto con tu director de cuentas de Braze o solicita una actualización en el dashboard de Braze.
{% endalert %}