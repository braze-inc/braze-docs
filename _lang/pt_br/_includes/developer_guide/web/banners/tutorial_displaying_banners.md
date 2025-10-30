## Pré-requisitos

Antes de iniciar este tutorial, verifique se o SDK do Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibição de banners para o Web SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Exibindo banners na Web" %}

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

!!! etapa
linhas-index.js=5

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
linhas-index.js=8-23

#### 2\. Assine as atualizações do Banner

Use `subscribeToBannersUpdates()` para registrar um manipulador que é executado sempre que um banner é atualizado. Dentro do manipulador, chame `braze.getBanner("global_banner")` para obter o posicionamento mais recente.

!!! etapa
Linhas -index.js=15-22

#### 3\. Insira o Banner e manipule os grupos de controle

Use `braze.insertBanner(banner, container)` para inserir um banner quando ele for retornado. Para garantir a limpeza do layout, oculte ou recolha os Banners que fazem parte de um grupo de controle (por exemplo, quando `isControl` for `true`).

!!! etapa
linhas-index.js=25

#### 4\. Atualize seus Banners

Depois de inicializar o SDK, chame `requestBannersRefresh(["global_banner", ...])` para garantir que os Banners sejam atualizados no início de cada sessão.

Você também pode chamar essa função a qualquer momento para atualizar os posicionamentos do Banner posteriormente.

!!! etapa
linhas-main.html=3

#### 5\. Adicione um contêiner para seu banner

Em seu HTML, adicione um novo elemento `<div>` e dê a ele um nome curto, relacionado ao banner `id`, como `global-banner-container`. O Braze usará o endereço `<div>` para inserir seu banner na página.

{% endscrolly %}
