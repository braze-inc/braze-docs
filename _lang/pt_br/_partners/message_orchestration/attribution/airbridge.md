---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Este artigo de referência descreve a parceria entre a Braze e a Airbridge, que oferece atribuição baseada em pessoas e medição incremental para medir a verdadeira eficácia do marketing em dispositivos, identidades e plataformas."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) é uma plataforma unificada de medição móvel que ajuda você a descobrir as verdadeiras fontes de crescimento por meio de atribuição móvel, medição incrementalista e modelagem de mix de marketing.

_Esta integração é mantida pelo Airbridge._

## Sobre a integração

A integração do Braze e Airbridge permite que você passe todos os dados de atribuição da instalação não orgânica do Airbridge para o Braze para criar campanhas de marketing personalizadas.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Airbridge | Uma conta Airbridge é necessária para usar a parceria. |
| App para iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários em sua aplicação. |
| Airbridge SDK | Além do SDK obrigatório da Braze, você deve instalar o SDK da Airbridge para [Android](https://help.airbridge.io/en/developers/android-sdk) ou [iOS](https://help.airbridge.io/en/developers/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: mapeie o ID do dispositivo

A integração de servidor para servidor pode ser habilitada incluindo os seguintes trechos de código em seus aplicativos.

#### Android

Se você tiver um app para Android, precisará passar um ID de dispositivo da Braze exclusivo para a Airbridge.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Se você tiver um app para iOS, será possível coletar o IDFV definindo o campo useUUIDAsDeviceId como falso. Se não for definido, a atribuição do iOS provavelmente não será mapeada com precisão da Airbridge para a Braze. Para saber mais, consulte "Coleta de IFDV".

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Etapa 2: Obter a chave de importação de dados do Braze

No Braze, navegue para **Integrações de Parceiros** > **Parceiros de Tecnologia** e selecione **Airbridge**.

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard do Airbridge.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### Etapa 3: Configure Braze no dashboard do Airbridge

1. Na Airbridge, navegue até **Integrations > Third-party Integrations** (Integrações > Integrações de terceiros) na barra lateral esquerda e selecione **Braze**.
2. Forneça a chave de importação de dados e o endpoint REST que você encontrou no dashboard da Braze.
3. Selecione o tipo de evento (evento de instalação ou evento de instalação e abertura de deeplink) e salve.

{% alert note %}
Os dados de atribuição para campanhas que levaram a eventos de abertura de deeplink são atualizados no nível do dispositivo. Por exemplo, se dois usuários usam um único dispositivo e um usuário realiza um evento de abertura de deeplink, os dados de atribuição deste evento também são refletidos nos dados do outro usuário.
{% endalert %}

Para obter instruções mais detalhadas, visite [Airbridge](https://help.airbridge.io/en/guides/braze).

### Etapa 4: Confirmar a integração

Depois que a Braze receber os dados de atribuição da Airbridge, o indicador de status da conexão na página de parceiros de tecnologia da Airbridge na Braze mudará de "Não conectado" para "Conectado". Um carimbo de data/hora da última solicitação bem-sucedida também será incluído.

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da Airbridge, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

## Campos de dados disponíveis

Airbridge pode enviar quatro tipos de dados de atribuição para a Braze listados no seguinte gráfico de campo de dados. Esses dados podem ser visualizados no dashboard do Airbridge e são usados para atribuição da instalação e filtragem de usuários.

Supondo que você configure sua integração conforme sugerido, a Braze mapeará os dados de instalação para filtros de segmento.

| Campo de dados do Airbridge | Filtro de segmento Braze | Descrição |
| -------------------- | ---------------------| ---- |
| `Channel` | Instalação por origem | O canal ao qual as instalações ou aberturas de deeplink são atribuídas |
| `Campaign` | Instalação por campanha | A campanha em que as instalações ou aberturas de deeplink são atribuídas |
| `Ad Group` | Instalação por grupo de anúncio | O grupo de anúncios ao qual as instalações ou aberturas de deeplink são atribuídas |
| `Ad Creative` | Instalação por anúncio | O criativo do anúncio ao qual as instalações ou aberturas de deeplink são atribuídas |

Sua base de usuários pode ser segmentada por dados de atribuição no dashboard da Braze usando os filtros de atribuição da instalação.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Dados de atribuição do Meta Business

Os dados de atribuição para campanhas do Meta Business não estão disponíveis através de nossos parceiros. Esta fonte de mídia não permite que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de clique da Airbridge na Braze (opcional)

Usar links de rastreamento de cliques em suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de app e reengajamento. Como resultado, você será capaz de medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo ROI.

Para começar com os links de rastreamento de cliques do Airbridge, visite [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Depois que a configuração estiver concluída, você pode inserir diretamente os links de rastreamento de cliques do Airbridge em suas campanhas do Braze. Airbridge usará então suas [metodologias de atribuição probabilística](https://help.airbridge.io/en/guides/identity-matching) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento do Airbridge com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas do Braze. Isso atribuirá deterministicamente o usuário que clicou no link.

{% tabs %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração SDK da Airbridge. Você pode incluir o GAID nos seus links de rastreamento de cliques da Airbridge utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Airbridge coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. Você pode incluir o IDFV nos seus links de rastreamento de cliques da Airbridge utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendação é puramente opcional**<br>
Se você não usa identificadores de dispositivo, como o IDFV ou GAID, nos seus links de rastreamento de cliques nem planeja adotá-los, a Airbridge ainda será capaz de atribuir esses cliques através de um modelo probabilístico.
{% endalert %}


