---
nav_title: Criação de Feature Flags
article_title: Criação de Feature Flags
page_order: 20
description: "Este artigo de referência aborda como criar sinalizadores de recursos para coordenar o lançamento de novos recursos."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Criação de feature flags

> Os Feature Flags permitem ativar ou desativar remotamente a capacitação de uma seleção de usuários. Crie um novo feature flag no dashboard da Braze. Forneça um nome e um endereço `ID`, um público-alvo e uma porcentagem de usuários para os quais ativar esse recurso. Em seguida, usando o mesmo `ID` no código do seu app ou site, você pode executar condicionalmente determinadas partes da sua lógica de negócios. Para saber mais sobre os feature flags e como você pode usá-los no Braze, consulte [Sobre os feature flags]({{site.baseurl}}/developer_guide/feature_flags/).

## Pré-requisitos

### Versão do SDK

Para usar os Feature Flags, confira se os seus SDKs estão atualizados com pelo menos essas versões mínimas:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Permissões de Braze

Para gerenciar os Feature Flags no dashboard, você precisará ser um administrador ou ter as seguintes [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/):

| Permissão                                                                    | O que você pode fazer                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Gerenciar Feature Flags**                                                      | Visualizar, criar e editar sinalizadores de recursos.     |
| **Campanhas de acesso, telas, cartões, Feature Flags, segmentos, biblioteca de mídia** | Veja a lista de sinalizadores de recursos disponíveis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Criação de um Feature Flag

### Etapa 1: Criar um novo Feature Flag

Acesse **Envio de mensagens** > **Feature Flags** e selecione **Criar Feature Flag**.

![Uma lista de feature flags criados anteriormente no dashboard do Braze]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### Etapa 2: Preencha os detalhes

Em **Details (Detalhes**), insira um nome, ID e descrição para seu Feature Flag.

| Campo        | Descrição                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome         | Um título legível por humanos para seus profissionais de marketing e administradores.                                                                                                                                                       |
| ID           | A ID exclusiva que você usará em seu código para verificar se esse recurso está [ativado para um usuário](#enabled). Esse ID não pode ser alterado posteriormente, portanto, revise nossas [práticas recomendadas de nomeação de ID](#naming-conventions) antes de continuar. |
| Descrição  | Uma descrição opcional que fornece algum contexto sobre seu Feature Flag.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 3: Criar propriedades personalizadas

Em **Propriedades**, crie propriedades personalizadas que seu app pode acessar por meio do SDK do Braze quando seu recurso estiver ativado. Você pode atribuir um valor de string, booleano, imagem, carimbo de data/hora, JSON ou um número a cada variável, bem como definir um valor padrão.

{% tabs local %}
{% tab exemplo %}
No exemplo a seguir, o feature flag mostra um banner de falta de estoque para uma loja de comércio eletrônico usando as propriedades personalizadas listadas: 

|Nome da propriedade|Tipo|Valor|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
Não há limite para o número de propriedades que você pode adicionar. No entanto, as propriedades de um sinalizador de recurso são limitadas a um total de 10 KB. Tanto os valores de propriedade quanto as chaves estão limitados a 255 caracteres de comprimento.
{% endalert %}
{% endtab %}
{% endtabs %}

### Etapa 4: Escolha os segmentos a serem direcionados

Antes de implementar um Feature Flag, é necessário escolher um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) de usuários para direcionamento. Use o menu suspenso **Add Filter (Adicionar filtro** ) para filtrar usuários fora do seu público-alvo. Adicione vários filtros para restringir ainda mais seu público.

![Dois menus suspensos. A primeira diz Target Users by Segment (Usuários-alvo por segmento). O segundo diz Filtros adicionais.]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### Etapa 5: Definir o tráfego de lançamento {#rollout}

Por padrão, os Feature Flag estão sempre desativados, o que permite separar a data de lançamento do recurso da ativação total do usuário. Para iniciar a implementação, use o controle deslizante **Rollout Traffic (Tráfego de implementação)** ou insira uma porcentagem na caixa de texto para escolher a porcentagem de usuários aleatórios no segmento selecionado para receber esse novo recurso.

![Um controle deslizante rotulado como Rollout Traffic (Tráfego de lançamento), variando entre 0 e 100.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
Não defina seu tráfego de implementação acima de 0% até que o novo recurso possa entrar em operação. Na primeira definição do seu Feature Flag no dashboard, deixe essa configuração em 0%.
{% endalert %}

## Usando o campo "enabled" para seus Feature Flags {#enabled}

Depois de definir seu Feature Flag, configure seu app ou site para verificar se ele está ou não ativado para um determinado usuário. Quando a capacitação estiver ativada, você definirá alguma ação ou fará referência às propriedades variáveis do sinalizador de recurso com base no seu caso de uso. O SDK da Braze fornece métodos getter para obter o status do Feature Flag e suas propriedades em seu app. 

Os Feature Flag são atualizados automaticamente no início da sessão para que você possa exibir a versão mais atualizada do seu recurso no lançamento. O SDK armazena esses valores em cache para que possam ser usados off-line. 

{% alert note %}
Certifique-se de registrar [as impressões das bandeiras de recursos](#impressions).
{% endalert %}

Digamos que você esteja implementando um novo tipo de perfil de usuário para o seu app. Você pode definir o endereço `ID` como `expanded_user_profile`. Em seguida, o app verificaria se deve exibir esse novo perfil de usuário para um usuário específico. Por exemplo:

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### Registro da impressão de um feature flag {#impressions}

Rastreie a impressão de um Feature Flag sempre que um usuário tiver a oportunidade de interagir com seu novo recurso ou quando ele __poderia__ ter interagido se o recurso estivesse desativado (no caso de um grupo de controle em um teste A/B). As impressões do Feature Flag são registradas apenas uma vez por sessão. 

Normalmente, você pode colocar essa linha de código diretamente abaixo de onde faz referência ao sinalizador de recurso em seu app:

{% tabs %}
{% tab JavaScript %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### Acesso a propriedades {#accessing-properties}

Para acessar as propriedades de um Feature Flag, use um dos seguintes métodos, dependendo do tipo que você definiu no dashboard.

Se uma propriedade que você referenciou não existir, esses métodos retornarão `null`.

{% tabs %}
{% tab JavaScript %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the String property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### Obter uma lista de todos os Feature Flags {#get-list-of-flags}

{% tabs %}
{% tab JavaScript %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### Atualizar os Feature Flag {#refreshing}

É possível atualizar os sinalizadores de recursos do usuário atual no meio da sessão para obter os valores mais recentes do Braze.

{% alert tip %}
A atualização ocorre automaticamente no início da sessão. A atualização só é necessária antes de ações importantes do usuário, como antes de carregar uma página de checkout, ou se você souber que um sinalizador de recurso será referenciado.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Java %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### Ouvindo as mudanças {#updates}

Você pode configurar o SDK da Braze para ouvir e atualizar seu app quando o SDK atualizar qualquer Feature Flag.

Isso é útil se você quiser atualizar seu app se um usuário não for mais elegível para um recurso. Por exemplo, definir algum estado em seu app com base no fato de um recurso estar ou não ativado ou em um de seus valores de propriedade.

{% tabs %}
{% tab JavaScript %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

Para ouvir as alterações, defina os valores de **Game Object Name** e **Callback Method Name** em **Braze Configuration** > **Feature Flags** para os valores correspondentes em seu aplicativo.

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

No código Dart em seu app, use o seguinte código de exemplo:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

Em seguida, faça essas alterações também na camada nativa do iOS. Note que não são necessárias etapas adicionais na camada Android.

1. Implemente o site `featureFlags.subscribeToUpdates` para assinar atualizações de Feature Flags, conforme descrito na documentação [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)).

2. Sua implementação de retorno de chamada `featureFlags.subscribeToUpdates` deve fazer uma chamada para `BrazePlugin.processFeatureFlags(featureFlags)`.

Para obter um exemplo, consulte [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) em nosso app de amostra.

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## Exibir o changelog

Para visualizar o changelog de um sinalizador de recurso, abra um sinalizador de recurso e selecione **Changelog**.

![A página "Edit" (Editar) de um sinalizador de recurso, com o botão "Changelog" destacado.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

Aqui, você pode verificar quando uma alteração ocorreu, quem fez a alteração, a qual categoria ela pertence e muito mais.

![O changelog do sinalizador de recurso selecionado.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## Segmentação com feature flags {#segmentation}

O Braze mantém automaticamente o rastreamento de quais usuários estão atualmente habilitados para uma bandeira de recurso. Você pode criar um segmento ou envio de mensagens de destino usando o [filtro**Feature Flag**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags). Para saber mais sobre filtragem em segmentos, consulte [Criação de um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

![A seção "Filtros" com "Feature Flag" digitado na barra de pesquisa do filtro.]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
Para evitar segmentos recursivos, não é possível criar um segmento que faça referência a outros feature flags.
{% endalert %}

## Práticas recomendadas

### Não combine lançamentos com telas ou experimentos

Para evitar que os usuários sejam ativados e desativados por diferentes pontos de entrada, defina o controle deslizante de rollouts como um valor maior que zero OU ative o sinalizador de recurso em um Canvas ou experimento. Como prática recomendada, se você planeja usar um sinalizador de recurso em um Canva ou experimento, mantenha a porcentagem de implementação em zero.

### Convenções de nomenclatura

Para manter seu código claro e consistente, considere usar o seguinte formato ao nomear o ID do Feature Flag:

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

Substitua o seguinte:

| Espaço reservado | Descrição                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | O comportamento do recurso. Em seu código, certifique-se de que o comportamento esteja desativado por padrão e evite usar frases como `disabled` no nome do Feature Flag. |
| `PRODUCT`   | O produto ao qual o recurso pertence.                                                                                       |
| `FEATURE`    | O nome do recurso.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Veja um exemplo de Feature Flag em que `show` é o comportamento, `animation_profile` é o produto e `driver` é o recurso:

```plaintext
show_animation_profile_driver
```

### Planejamento antecipado

Sempre jogue pelo seguro. Ao considerar novos recursos que podem exigir um botão de desativação, é melhor lançar um novo código com um sinalizador de recurso e não precisar dele do que perceber que é necessária uma nova atualização do app.

### Seja descritivo

Adicione uma descrição ao seu Feature Flag. Embora esse seja um campo opcional no Braze, ele pode ajudar a responder a perguntas que outras pessoas possam ter ao pesquisar os sinalizadores de recursos disponíveis.

- Detalhes de contato de quem é responsável pela capacitação e pelo comportamento dessa bandeira
- Quando esse sinalizador deve ser desativado
- Links para documentação ou notas sobre o novo recurso que esse flag controla
- Quaisquer dependências ou notas sobre como usar o recurso

### Limpeza de antigos Feature Flags

É muito comum deixarmos recursos 100% implementados por mais tempo do que o necessário.

Para ajudar a manter seu código (e o dashboard do Braze) limpo, remova os sinalizadores de recursos permanentes de sua base de código depois que todos os usuários tiverem feito upgrade e você não precisar mais da opção de desativar o recurso. Isso ajuda a reduzir a complexidade de seu ambiente de desenvolvimento, mas também mantém sua lista de Feature Flags organizada.

