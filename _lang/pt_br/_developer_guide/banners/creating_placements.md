---
nav_title: Criação de colocações
article_title: Criando posicionamentos de banner para o SDK do Braze
description: "Saiba como criar posicionamentos de banner para o SDK do Braze."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Criação de posicionamentos de banner

> Saiba como criar posicionamentos de banner para o SDK do Braze, para que possa engajar os usuários com uma experiência que pareça natural. Para saber mais sobre informações gerais, consulte [Sobre banners]({{site.baseurl}}/developer_guide/banners).

## Solicitações de colocação {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Criação de um posicionamento

### Pré-requisitos

Essas são as versões mínimas do SDK necessárias para Banners:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Etapa 2: Atualize os canais em seu app {#requestBannersRefresh}

Os posicionamentos podem ser solicitados uma vez por sessão e serão armazenados em cache automaticamente quando a sessão de um usuário expirar ou quando você alterar os usuários identificados usando o método `changeUser`. O SDK não buscará novamente os posicionamentos se você chamar o método refresh novamente durante a mesma sessão. Em vez disso, ele registrará um erro e retornará uma mensagem de erro para o chamador.

{% alert tip %}
Atualize os posicionamentos o mais rápido possível para evitar postergações no download ou na exibição de Banners.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}

{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 3: Ouça as atualizações {#subscribeToBannersUpdates}

{% alert tip %}
Se você inserir banners usando os métodos do SDK neste guia, todos os eventos de análise de dados serão tratados automaticamente.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
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
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}

{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 4: Inserir usando a ID de colocação {#insertBanner}

{% tabs %}
{% tab JavaScript %}

Crie um elemento de contêiner para o banner. Não se esqueça de definir sua largura e altura.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

Em seguida, use o método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) para substituir o HTML interno do elemento contêiner.

{% alert tip %}
Para rastrear impressões, não deixe de ligar para `insertBanner` para `isControl`. Depois disso, você pode ocultar ou recolher o contêiner.
{% endalert %}

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

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
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

Você pode criar banners em seu layout de visualizações do Android incluindo esse XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
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

Para obter o banner em Kotlin, use:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endtab %}
{% tab React Native %}

Se estiver usando [a Nova Arquitetura do React Native](https://reactnative.dev/architecture/landing-page), será necessário registrar `BrazeBannerView` como um componente Fabric em seu site `AppDelegate.mm`.

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
Para obter a integração mais simples, adicione o seguinte trecho de JavaScript XML (JSX) à hierarquia da visualização, fornecendo apenas o ID do posicionamento.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obter o modelo de dados do banner no React Native ou para verificar a presença desse posicionamento no cache do usuário, use:

```javascript
const banner = await Braze.getBanner("global_banner");
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
Para obter a integração mais simples, adicione o seguinte widget à hierarquia da visualização, fornecendo apenas o ID do posicionamento.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Você pode usar o método `getBanner` para verificar a presença desse posicionamento no cache do usuário.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}

{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 5: Enviar um banner de teste (opcional) {#handling-test-cards}

Antes de lançar uma campanha de banner, você pode [enviar um banner de teste]({{site.baseurl}}/user_guide/message_building_by_channel/banners/testing/) para verificar sua integração. Os banners de teste serão armazenados em um cache separado na memória e não persistirão durante a reinicialização do app. Embora não seja necessária nenhuma configuração extra, seu dispositivo de teste deve ser capaz de receber notificações por push em primeiro plano para que possa exibir o teste.

{% alert note %}
Os banners de teste são como qualquer outro banner, exceto pelo fato de serem removidos na próxima sessão do app.
{% endalert %}

## Registro de impressões

O Braze registra automaticamente as impressões quando você usa os métodos do SDK para inserir um banner - portanto, não há necessidade de rastrear as impressões manualmente. 

## Dimensões e dimensionamento

Veja a seguir o que você precisa saber sobre as dimensões e o tamanho do Banner:

- Embora o criador permita que você faça uma prévia dos banners em diferentes dimensões, essas informações não são salvas nem enviadas ao SDK.
- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.
