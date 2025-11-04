## Conditions préalables

Avant de commencer ce tutoriel, vérifiez que votre SDK Braze répond aux exigences minimales en matière de version :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Affichage de bannières pour le SDK Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Afficher des bannières Web" %}

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

!étape
lignes-index.js=5

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-index.js=8-23

#### 2\. S'abonner aux mises à jour de la bannière

Utilisez `subscribeToBannersUpdates()` pour enregistrer un gestionnaire qui s'exécute chaque fois qu'une bannière est mise à jour. Dans le gestionnaire, appelez `braze.getBanner("global_banner")` pour obtenir le dernier placement.

!étape
lignes-index.js=15-22

#### 3\. Insérer les groupes de contrôle de la bannière et de la poignée

Utilisez `braze.insertBanner(banner, container)` pour insérer une bannière lorsqu'elle est renvoyée. Pour que votre mise en page reste propre, masquez ou réduisez les bannières qui font partie d'un groupe de contrôle (par exemple, lorsque `isControl` est `true`).

!étape
lignes-index.js=25

#### 4\. Actualisez vos bannières

Après avoir initialisé le SDK, appelez `requestBannersRefresh(["global_banner", ...])` pour vous assurer que les bannières sont actualisées au début de chaque session.

Vous pouvez également appeler cette fonction à tout moment pour actualiser ultérieurement les placements de bannières.

!étape
lignes-main.html=3

#### 5\. Ajouter un conteneur pour votre bannière

Dans votre code HTML, ajoutez un nouvel élément `<div>` et donnez-lui un nom court, lié à la bannière `id`, tel que `global-banner-container`. Braze utilisera ce site `<div>` pour insérer votre bannière dans la page.

{% endscrolly %}
