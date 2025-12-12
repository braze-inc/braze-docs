## Requisitos previos

Antes de empezar este tutorial, comprueba que tu SDK de Braze cumple los requisitos mínimos de la versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Mostrar banners para el SDK Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Visualización de banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

Paso
líneas-index.js=5

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-index.js=8-23

#### 2\. Suscribirse a las actualizaciones del Banner

Utiliza `subscribeToBannersUpdates()` para registrar un controlador que se ejecute cada vez que se actualice un Banner. Dentro del controlador, llama a `braze.getBanner("global_banner")` para obtener la última colocación.

Paso
líneas-index.js=15-22

#### 3\. Inserta el Banner y maneja los grupos de control

Utiliza `braze.insertBanner(banner, container)` para insertar un Banner cuando se devuelva. Para mantener limpio tu diseño, oculta o contrae los banners que formen parte de un grupo de control (por ejemplo, cuando `isControl` es `true`).

Paso
líneas-index.js=25

#### 4\. Actualiza tus Banners

Tras inicializar el SDK, llama a `requestBannersRefresh(["global_banner", ...])` para asegurarte de que los Banners se actualizan al inicio de cada sesión.

También puedes llamar a esta función en cualquier momento para refrescar las colocaciones del Banner más adelante.

Paso
líneas-main.html=3

#### 5\. Añade un contenedor para tu Banner

En tu HTML, añade un nuevo elemento `<div>` y dale un nombre corto, relacionado con el Banner `id`, como `global-banner-container`. Braze utilizará este `<div>` para insertar tu Banner en la página.

{% endscrolly %}
