## Pré-requisitos

Antes de começar este tutorial, verifique se o seu SDK Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibindo banners para o SDK da Web

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

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

!!etapa
linhas-index.js=5

#### 1\. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!etapa
linhas-index.js=8-23

#### 2\. Inscreva-se para atualizações de Banner

Use `subscribeToBannersUpdates()` para registrar um manipulador que é executado sempre que um Banner é atualizado. Dentro do manipulador, chame `braze.getBanner("global_banner")` para obter a colocação mais recente.

!!etapa
linhas-index.js=15-22

#### 3\. Insira o Banner e gerencie grupos de controle

Use `braze.insertBanner(banner, container)` para inserir um Banner quando ele for retornado. Para garantir que seu layout permaneça limpo, oculte ou colapse Banners que fazem parte de um grupo de controle (por exemplo, quando `isControl` é `true`).

!!etapa
linhas-index.js=25

#### 4\. Atualize seus Banners

Após inicializar o SDK, chame `requestBannersRefresh(["global_banner", ...])` para garantir que os Banners sejam atualizados no início de cada sessão.

Você também pode chamar esta função a qualquer momento para atualizar as colocações de Banner mais tarde.

!!etapa
linhas-main.html=3

#### 5\. Adicione um contêiner para o seu Banner

No seu HTML, adicione um novo `<div>` elemento e dê a ele um `id` curto relacionado ao Banner, como `global-banner-container`. Braze usará este `<div>` para inserir seu Banner na página.

{% endscrolly %}
