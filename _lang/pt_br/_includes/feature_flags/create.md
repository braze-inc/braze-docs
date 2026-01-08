# Criação de feature flags

> Os Feature Flags permitem ativar ou desativar remotamente a capacitação de uma seleção de usuários. Crie um novo feature flag no dashboard da Braze. Forneça um nome e um endereço `ID`, um público-alvo e uma porcentagem de usuários para os quais ativar esse recurso. Em seguida, usando o mesmo `ID` no código do seu app ou site, você pode executar condicionalmente determinadas partes da sua lógica de negócios. Para saber mais sobre os feature flags e como você pode usá-los no Braze, consulte [Sobre os feature flags]({{site.baseurl}}/developer_guide/feature_flags/).

## Pré-requisitos

### Versão do SDK

Para usar os Feature Flags, confira se os seus SDKs estão atualizados com pelo menos essas versões mínimas:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Permissões do Braze

Para gerenciar os Feature Flags no dashboard, você precisará ser um administrador ou ter as seguintes [permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/):

| Permissão                                                                    | O que você pode fazer                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Gerenciar Feature Flags**                                                      | Visualizar, criar e editar sinalizadores de recursos.     |
| **Campanhas de acesso, telas, cartões, Feature Flags, segmentos, biblioteca de mídia** | Veja a lista de sinalizadores de recursos disponíveis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Criação de um Feature Flag

### Etapa 1: Criar um novo Feature Flag

Acesse **Envio de mensagens** > **Feature Flags** e selecione **Criar Feature Flag**.

![Um banco de dados que mostra um sinalizador de recurso existente e como criar um novo.]({% image_buster /assets/img/feature_flags/create_ff.png %}){: style="max-width:75%"}

### Etapa 2: Preencha os detalhes

Em **Feature Flag details (Detalhes do sinalizador** de recurso), insira um nome, ID e descrição para seu sinalizador de recurso.

![Um formulário que mostra que você pode adicionar um nome, ID, descrição e propriedades a um sinalizador de recurso.]({% image_buster /assets/img/feature_flags/create_ff_properties.png %}){: style="max-width:75%"}


| Campo        | Descrição                                                                |
|--------------|----------------------------------------------------------------------------|
| Nome         | Um título legível por humanos para seus profissionais de marketing e administradores.              |
| ID           | A ID exclusiva que você usará em seu código para verificar se esse recurso está [ativado para um usuário](#enabled). Esse ID não pode ser alterado posteriormente, portanto, revise nossas [práticas recomendadas de nomeação de ID](#naming-conventions) antes de continuar. |
| Descrição  | Uma descrição opcional que fornece algum contexto sobre seu Feature Flag.   |
| Propriedades   | Propriedades opcionais que configuram remotamente seu sinalizador de recurso. Eles podem ser sobrescritos nas etapas do canva ou em experimentos do canva. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 2a: Criar propriedades personalizadas

Em **Properties (Propriedades**), você pode, opcionalmente, criar propriedades personalizadas que seu app pode acessar por meio do Braze SDK quando seu recurso estiver ativado. É possível atribuir um valor de string, booleano, imagem, carimbo de data/hora, JSON ou um número a cada variável, bem como definir um valor padrão.

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

Antes de implementar um Feature Flag, é necessário escolher um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/) de usuários para direcionamento. Selecione **Add Rule (Adicionar regra** ) no sinalizador recém-criado e, em seguida, use os menus suspensos filter group (grupo de filtros) e segment (segmento) para filtrar os usuários do seu público-alvo. Adicione vários filtros para restringir ainda mais seu público.

![Uma caixa de texto rotulada como Rollout Traffic com a capacidade de adicionar segmentos e filtros.]({% image_buster /assets/img/feature_flags/segmentation_ff.png %}){: style="max-width:75%;"}

### Etapa 5: Definir o tráfego de lançamento {#rollout}

Por padrão, os feature flags estão sempre inativos, o que permite separar a data de lançamento do seu recurso da ativação total do usuário. Para iniciar a implementação, use a seção **Rollout Traffic (Tráfego de implementação** ) para inserir uma porcentagem na caixa de texto. Isso escolherá a porcentagem de usuários aleatórios no seu segmento selecionado para receber esse novo recurso.

{% alert important %}
Não defina seu tráfego de implementação acima de 0% até que o novo recurso possa entrar em operação. Na primeira definição do seu Feature Flag no dashboard, deixe essa configuração em 0%.
{% endalert %}

{% alert important %}
Para implementar uma bandeira com apenas uma regra ou para um público Singular, adicione sua primeira regra com critérios de segmentação e porcentagens de implementação selecionadas. Por fim, confirme se a regra **Todos os outros** está desativada e salve sua bandeira.
{% endalert %}

## Rollouts de bandeiras com várias regras

Use rollouts de feature flag com várias regras para definir uma sequência de regras para avaliação de usuários, o que permite uma segmentação precisa e lançamentos controlados de recursos. Esse método é ideal para implementar o mesmo recurso para diversos públicos. 

### Ordem de avaliação

As regras do Feature Flag são avaliadas de cima para baixo, na ordem em que estão listadas. Um usuário se qualifica para a primeira regra que cumprir. Se um usuário não atender a nenhuma regra, sua elegibilidade será determinada pela regra padrão "Todos os outros".

### Qualificação do usuário

- Se um usuário atender aos critérios da primeira regra, ele será imediatamente elegível para receber o Feature Flag.
- Se um usuário não se qualificar para a primeira regra, ele será avaliado em relação à segunda regra, e assim por diante.

A avaliação sequencial continua até que um usuário se qualifique para uma regra ou chegue à regra "Todos os outros" na parte inferior da lista.

### Regra "Todos os demais"

A regra "Todos os outros" funciona como padrão. Se um usuário não se qualificar para nenhuma das regras anteriores, sua elegibilidade para o sinalizador de recurso será determinada pela configuração de alternância da regra "Everyone Else" (Todos os outros). Por exemplo, se a regra "Everyone Else" (Todos os outros) estiver desativada, no estado padrão, um usuário que não atender aos critérios de nenhuma outra regra não receberá o sinalizador de recurso no início da sessão.

### Regras de reordenação

Por padrão, as regras são ordenadas na sequência em que são criadas, mas você pode reordená-las arrastando-as e soltando-as no dashboard.

![Uma imagem mostrando que um usuário pode adicionar uma regra a um sinalizador de recurso.]({% image_buster /assets/img/feature_flags/add_rule.png %}){: style="max-width:80%;"}

![Uma imagem mostrando um resumo de um sinalizador de recurso com várias regras adicionadas e uma regra para todos os outros.]({% image_buster /assets/img/feature_flags/mr_rules_overview.png %}){: style="max-width:80%;"}

### Casos de uso do Feature Flag com várias regras

#### Liberar gradualmente uma página de checkout

Digamos que você trabalhe para uma marca de comércio eletrônico e tenha uma nova página de checkout que deseja implementar em diferentes regiões geográficas para garantir a estabilidade. Usando os sinalizadores de recursos de várias regras, você pode definir o seguinte:

- **Regra 1:** Seu segmento dos EUA está definido como 100%.
- **Regra 2:** Seu segmento está definido como 50% dos usuários brasileiros, portanto, nem todos eles recebem o fluxo de uma só vez. 
- **Regra 3 (Todos os demais):** Para todos os outros usuários, ative a regra "Everyone Else" e defina-a como 15%, para que uma parte de todos os usuários possa fazer o check-out com o novo fluxo.

#### Alcançar primeiro os testadores internos

Digamos que você seja um gerente de produto que queira mesmo garantir que seus testadores internos sempre recebam o sinalizador de recurso quando você lançar um novo produto. Você pode adicionar o segmento de testadores internos à sua primeira regra e defini-la como 100%, para que os testadores internos sejam elegíveis durante cada lançamento de recurso.

## Usando o campo "enabled" para seus Feature Flags {#enabled}

Depois de definir seu Feature Flag, configure seu app ou site para verificar se ele está ou não ativado para um determinado usuário. Quando a capacitação estiver ativada, você definirá alguma ação ou fará referência às propriedades variáveis do sinalizador de recurso com base no seu caso de uso. O SDK da Braze fornece métodos getter para obter o status do Feature Flag e suas propriedades em seu app. 

Os Feature Flag são atualizados automaticamente no início da sessão para que você possa exibir a versão mais atualizada do seu recurso no lançamento. O SDK armazena esses valores em cache para que possam ser usados off-line. 

{% alert note %}
Certifique-se de registrar [as impressões das bandeiras de recursos](#impressions).
{% endalert %}

Digamos que você esteja implementando um novo tipo de perfil de usuário para o seu app. Você pode definir o endereço `ID` como `expanded_user_profile`. Em seguida, o app verificaria se deve exibir esse novo perfil de usuário para um usuário específico. Por exemplo:

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab SWIFT %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endsubtab %}
{% endsubtabs %}
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
{% tab Web %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab SWIFT %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endsubtab %}
{% endsubtabs %}
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

Se não houver nenhuma propriedade do tipo correspondente para a chave que você forneceu, esses métodos retornarão `null`.

{% tabs %}
{% tab Web %}

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
{% tab SWIFT %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the string property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty: Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty: String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty: [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

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

{% endsubtab %}
{% subtab Kotlin %}

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

{% endsubtab %}
{% endsubtabs %}
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
{% tab Web %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab SWIFT %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endsubtab %}
{% endsubtabs %}
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
{% tab Web %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab SWIFT %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.refreshFeatureFlags();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endsubtab %}
{% endsubtabs %}
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
{% tab Web %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab SWIFT %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endsubtab %}
{% endsubtabs %}
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

## Verificação da elegibilidade do usuário

Para verificar a quais sinalizadores de recursos um usuário é elegível no Braze, vá para **Público** > **Pesquisar usuários** e, em seguida, pesquise e selecione um usuário.

Na guia **Feature Flags Eligibility (Elegibilidade de sinalizadores** de recursos), você pode filtrar a lista de sinalizadores de recursos elegíveis por plataforma, aplicativo ou dispositivo. Também é possível fazer uma prévia da carga útil que será retornada ao usuário selecionando <i class="fa-solid fa-eye"></i> ao lado de um sinalizador de recurso.

![Uma imagem que mostra a tabela de Feature Flags a que um usuário é elegível.]({% image_buster /assets/img/feature_flags/eligibility.png %}){: style="max-width:85%;"}

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

