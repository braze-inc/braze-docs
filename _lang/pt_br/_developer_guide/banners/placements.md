---
nav_title: Gerenciar posicionamentos
article_title: Gerenciar as colocações de Banner para o SDK do Braze
description: "Aprenda como criar e gerenciar colocações de Banner no SDK do Braze, incluindo o acesso às suas propriedades exclusivas e o registro de impressões."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Gerenciar colocações de Banner

> Aprenda como criar e gerenciar colocações de Banner no SDK do Braze, incluindo o acesso às suas propriedades exclusivas e o registro de impressões. Para mais informações gerais, veja [Sobre Banners]({{site.baseurl}}/developer_guide/banners).

## Sobre solicitações de colocação {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Criar um posicionamento

### Pré-requisitos

Estas são as versões mínimas do SDK necessárias para criar colocações de Banner:

{% multi_lang_include sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Etapa 2: Atualize os canais em seu app {#requestBannersRefresh}

As colocações podem ser atualizadas chamando os métodos de atualização descritos abaixo. Essas colocações serão armazenadas em cache automaticamente quando a sessão de um usuário expirar ou quando você mudar usuários identificados usando o método `changeUser`.

{% alert tip %}
Atualize as colocações o mais rápido possível para evitar atrasos no download ou na exibição dos Banners.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
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
Se você inserir Banners usando os métodos do SDK neste guia, todos os eventos de análise (como impressões e cliques) serão tratados automaticamente, e as impressões só serão registradas quando o banner estiver visível.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Se você estiver usando JavaScript puro com o SDK Web do Braze, use [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) para ouvir atualizações de colocação e, em seguida, chame [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) para buscá-las.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Se você estiver usando React com o SDK Web do Braze, configure [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) dentro de um hook `useEffect` e chame [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) após registrar seu ouvinte.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
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
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endsubtab %}
{% endsubtabs %}
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

### Etapa 4: Inserir usando o ID da colocação {#insertBanner}

{% alert tip %}
Para um tutorial completo passo a passo, confira [Exibindo um Banner por ID de Colocação]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Crie um elemento contêiner para o Banner. Certifique-se de definir sua largura e altura.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Se você estiver usando JavaScript puro com o SDK Web do Braze, chame o método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) para substituir o HTML interno do elemento contêiner.

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
{% endsubtab %}

{% subtab React %}
Se você estiver usando React com o SDK Web do Braze, chame o método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) com um `ref` para substituir o HTML interno do elemento contêiner.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para rastrear impressões, certifique-se de chamar `insertBanner` para `isControl`. Você pode então ocultar ou colapsar seu contêiner depois.
{% endalert %}

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
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Para obter o banner no código Java, use:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Você pode criar Banners no layout de suas views Android incluindo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Se você estiver usando [React Native's New Architecture](https://reactnative.dev/architecture/landing-page), você precisa registrar `BrazeBannerView` como um componente Fabric em seu `AppDelegate.mm`.

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
Para a integração mais simples, adicione o seguinte trecho de JavaScript XML (JSX) na sua hierarquia de views, fornecendo apenas o ID de colocação.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obter o modelo de dados do Banner no React Native, ou para verificar a presença dessa colocação no cache do seu usuário, use:

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
Para a integração mais simples, adicione o seguinte widget na sua hierarquia de views, fornecendo apenas o ID de colocação.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Você pode usar o método `getBanner` para verificar a presença dessa colocação no cache do seu usuário.

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

### Etapa 5: Envie um Banner de teste (opcional) {#handling-test-cards}

Antes de lançar uma campanha de Banner, você pode [enviar um Banner de teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) para verificar sua integração. Banners de teste serão armazenados em um cache separado na memória e não persistirão entre reinicializações do app. Embora nenhuma configuração extra seja necessária, seu dispositivo de teste deve ser capaz de receber notificações por push em primeiro plano para que possa exibir o teste.

{% alert note %}
Banners de teste são como qualquer outro banner, exceto que são removidos na próxima sessão do app.
{% endalert %}

## Registrar impressões

A Braze registra automaticamente impressões para Banners que estão visíveis quando você usa métodos do SDK para inserir um Banner—portanto, não há necessidade de rastrear impressões manualmente.

## Registrando cliques

O método usado para registrar cliques em Banners depende de como seu Banner é renderizado e onde seu manipulador de cliques está localizado.

### Conteúdo padrão do Banner (automático)

Se você estiver usando métodos do SDK padrão, prontos para uso, para inserir Banners, e seu Banner usar componentes de editor padrão (imagens, botões, texto), os cliques são rastreados automaticamente. O SDK anexa ouvintes de cliques a esses elementos, e nenhum código adicional é necessário.

### Blocos de Código Personalizados

Se seu Banner usar o bloco de editor **Custom Code** no dashboard da Braze, você deve usar `brazeBridge.logClick()` para registrar cliques a partir desse HTML personalizado. Isso se aplica mesmo ao usar métodos SDK para renderizar o Banner, porque o SDK não pode anexar ouvintes automaticamente a elementos dentro do seu código personalizado.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para a referência completa, veja [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge). O `brazeBridge` fornece uma camada de comunicação entre o HTML interno do Banner e o SDK Braze pai.

### Implementações de UI personalizadas (sem cabeça)

Se você estiver construindo uma UI totalmente personalizada usando as [propriedades personalizadas](#custom-properties) do Banner em vez de renderizar o HTML do Banner, você deve registrar manualmente cliques (e impressões) a partir do seu código de aplicativo. Como o SDK não está renderizando o Banner, ele não tem como rastrear automaticamente as interações com seus elementos de UI personalizados.

Use o método `logClick()` no objeto Banner.

## Dimensões e tamanhos

Aqui está o que você precisa saber sobre dimensões e tamanhos do Banner:

- Embora o criador permita que você visualize Banners em diferentes dimensões, essa informação não é salva ou enviada para o SDK.
- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.

## Propriedades personalizadas {#custom-properties}

Você pode usar propriedades personalizadas da sua campanha de Banner para recuperar dados chave-valor através do SDK e modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Enviar metadados para suas análises de terceiros ou integrações.
- Usar metadados como um `timestamp` ou objeto JSON para disparar lógica condicional.
- Controlar o comportamento de um banner com base em metadados incluídos como `ratio` ou `format`.

### Pré-requisitos

Você precisará [adicionar propriedades personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties) à sua campanha de Banner. Além disso, estas são as versões mínimas do SDK necessárias para acessar propriedades personalizadas:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Acessar propriedades personalizadas

Para acessar as propriedades personalizadas de um banner, use um dos seguintes métodos com base no tipo da propriedade definido no dashboard. Se a chave não corresponder a uma propriedade desse tipo ou não existir, o método retorna `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object propertyßß
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}
