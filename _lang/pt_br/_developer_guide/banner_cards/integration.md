---
nav_title: Cartões de Banner
article_title: Cartões de Banner para o Braze SDK
hidden: true
description: "Este artigo de referência aborda os cartões de banner e como integrar esse recurso no Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Integração de cartões de banner

> Semelhante aos [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) de banner, os cartões de banner são incorporados diretamente no seu app ou site para que você possa engajar os usuários com uma experiência que pareça natural. Eles são uma solução rápida e perfeita para criar envios de mensagens personalizadas para seus usuários e, ao mesmo tempo, ampliar o alcance de outros canais (como e-mail ou notificações por push).

{% alert important %}
Os cartões de banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Pré-requisitos

Antes de integrar os Cartões de Banner, você precisará criar colocações de Cartões de Banner em seu app.

Além disso, estas são as versões mínimas do SDK necessárias para começar a usar os Cartões de Banner:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 reactnative:14.0.0 %}

## Integração de cartões de banner

### Etapa 1: Atualize os canais em seu app {#requestBannersRefresh}

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
{% tab SWIFT %}

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
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
This feature is not currently supported on Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Etapa 2: Ouça as atualizações {#subscribeToBannersUpdates}

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
{% tab SWIFT %}

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
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  data => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map(banner => banner.placementId),
    );
  },
);
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

### Etapa 3: Insira cartões pelo ID de colocação

{% tabs %}
{% tab JavaScript %}

Crie um elemento contêiner para o banner. Certifique-se de definir sua largura e altura.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

Em seguida, use o método para substituir o HTML interno do elemento contêiner.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
    baseUrl: "sdk-base-url",
    allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");
    if (!globalBanner) {
        return;
    }

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
{% tab SWIFT %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
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

Se você estiver usando a Nova Arquitetura do React Native, precisa registrar como um componente Fabric em seu.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```

Para obter o Banner no React Native, use:

```javascript
const banner = await Braze.getBanner("global_banner");
```

Em seu aplicativo React Native, adicione o seguinte trecho de JavaScript XML (JSX) à sua hierarquia de visualização.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
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
{% tab SWIFT %}

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

## Gerenciando envios de teste

Use envios de teste para verificar as integrações do Cartão de Banner antes de lançar uma campanha. Os cartões de banner de teste são armazenados em um cache separado na memória e não persistem entre as reinicializações do app. Embora nenhuma configuração extra seja necessária, o dispositivo deve ser capaz de receber notificações por push em primeiro plano para exibir os Cartões de Banner de teste.

{% alert important %}
Um banner de teste é tratado como qualquer outro banner, exceto que é removido na próxima sessão do app. Você deve ter a configuração de posicionamento em seu app para que o banner de teste seja exibido.
{% endalert %}

## Dimensões e tamanhos

Aqui estão algumas coisas para saber sobre as dimensões e tamanhos do Banner Card:

- Enquanto o criador permite que você veja prévias de banners em diferentes dimensões, essa informação não é salva nem enviada para o SDK.
- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.
