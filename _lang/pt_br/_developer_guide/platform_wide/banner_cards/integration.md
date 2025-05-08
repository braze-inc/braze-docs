---
nav_title: Integração de cartões de banner
article_title: Integração de cartões de banner
hidden: true
description: "Este artigo de referência aborda os cartões de banner e como integrar esse recurso no Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Integração de cartões de banner

Semelhante aos [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) de banner, os cartões de banner são incorporados diretamente no seu app ou site para que você possa engajar os usuários com uma experiência que pareça natural. Eles são uma solução rápida e perfeita para criar envios de mensagens personalizadas para seus usuários e, ao mesmo tempo, ampliar o alcance de outros canais (como e-mail ou notificações por push).

{% alert important %}
Os cartões de banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

Esse recurso está disponível a partir das seguintes [versões do SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Pré-requisitos do dashboard

### Definir posicionamentos {#define-placements}

Antes de lançar uma campanha de cartão de banner em seu app, você deve configurar um posicionamento no dashboard do Braze. Os posicionamentos são locais que você define em seu app e que podem exibir cartões de banner.

#### Etapa 1: Criar um novo posicionamento

Acesse **Settings** > **Banner Cards Placements** e selecione **Create Placement**).

![Seção de posicionamentos de cartão de banner para criar IDs de posicionamento.]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### Etapa 2: Preencha os detalhes

Dê um nome à sua colocação e atribua a ela uma **ID de posicionamento**. Opcionalmente, você pode adicionar uma descrição para sua colocação.

Trabalhe com sua equipe de marketing para criar essa ID. Essa é a ID que será referenciada no código do seu aplicativo, e sua equipe de marketing usará a ID para atribuir uma campanha ao local no seu app. 

{% alert important %}
Evite editar seu ID de posicionamento após o lançamento, pois isso pode interromper a integração com seu app ou site.
{% endalert %}

![Os detalhes de posicionamento que designam um cartão de banner serão exibidos na barra lateral esquerda para campanhas de promoção de vendas na primavera.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

Para obter etapas sobre como lançar uma campanha de cartão de banner, consulte [Criação de um cartão de banner]({{site.baseurl}}/create_banner_card/).

## Atualize os canais em seu app {#requestBannersRefresh}

Os posicionamentos podem ser solicitados a cada sessão e serão armazenados em cache automaticamente quando a sessão de um usuário expirar ou quando você alterar os usuários identificados usando o método `changeUser`.

{% alert tip %}
Atualize os posicionamentos o mais rápido possível para evitar postergações no download ou na exibição de banners.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```
{% endtab %}
{% tab Java %}
```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
 Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Ouça as atualizações {#subscribeToBannersUpdates}

{% alert tip %}
Se você inserir banners usando os métodos do SDK neste guia, todos os eventos de análise de dados serão tratados automaticamente. Se você quiser renderizar manualmente o HTML, [informe-nos](mailto:banners-feedback@braze.com).
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
})

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
    for (banner in update.banners) {
      Log.d(TAG, "Received banner: " + banner.placementId)
    }
}
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Obter e inserir um cartão de bandeira por ID de colocação {#insertBanner}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");

    // choose where in the DOM you want to insert the banner HTML
    const container = document.getElementById("global-banner-container");

    // Insert the banner which replacees the innerHTML of that container
    braze.insertBanner(globalBanner, container);

    // Special handling if the user is part of a Control Variant
    if (globalBanner.isControl) {
        // hide or collapse the container
        container.style.display = 'none';
    }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])

```

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(placementId: "global_banner", braze: braze)
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(placementId: "global_banner", braze: braze)
}
```
{% endtab %}
{% tab Java %}
Para obter o banner no código Java, use:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Você pode criar cartões de banner em seu layout de visualizações do Android incluindo esse XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
Para obter o banner em Kotlin, use:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

Se estiver usando o Android Views, use este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Se estiver usando o Jetpack Compose, poderá usar isso:

```kotlin
Banner(placementId = "global_banner")
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Análise de dados

Não é necessário se preocupar com o rastreamento manual das impressões, pois o Braze cuida automaticamente de todo o registro de impressões ao usar os métodos do SDK para inserir cartões de banner.

Se precisar analisar e renderizar o HTML em uma exibição personalizada, [entre em contato conosco](mailto:banners-feedback@braze.com).

{% details Para saber mais sobre o rastreamento manual de impressões %}

{% alert important %}
É provável que a personalização de sua integração seja desnecessária, portanto, considere cuidadosamente a etapa a seguir.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
  // do something with the html
  // then log an impression when the HTML is in view
  braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
// First, get the Banner object:
var globalBanner: Braze.Banner?
brazeClient.braze()?.banners.getBanner(for: "global_banner", { banner in
  globalBanner = banner
})

// Then log the impression on the Banner.
globalBanner?.context?.logImpression()
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).logBannerImpression(banner.getPlacementId());
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).logBannerImpression(banner.placementId)
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

{% enddetails %}

## Práticas recomendadas

### Dimensões e tamanho do cartão de banner

- Nenhuma informação de dimensão é enviada pelo Braze.

{% alert note %}
O criador permite que o usuário faça uma prévia dos banners em diferentes dimensões. Essas informações não são salvas nem enviadas ao SDK.
{% endalert %}

- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Como prática recomendada, recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.
