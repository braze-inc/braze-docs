---
nav_title: Locais e geofences
article_title: Local e Geofences para iOS
platform: Swift
page_order: 4
description: "Este artigo de referência ensina a implementar locais e geofences em seu app para Swift SDK."
Tool:
  - Location

---

# Locais e geocercas

> Este artigo aborda a configuração de geofences para sua integração de iOS SDK. Geofences estão disponíveis apenas em pacotes selecionados da Braze. Informe-se com seu gerente de sucesso do cliente da Braze.

No centro da oferta de localização em tempo real da Braze, está o conceito de uma [geofence]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences). Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo ao redor de uma posição global específica.

{% alert important %}
A partir do iOS 14, as geofences têm funcionamento instável para os usuários que optam por dar permissão de localização aproximada.
{% endalert %}

## Etapa 1: ativar push em segundo plano

Para utilizar totalmente nossa estratégia de sincronização de geofences, você deve ter [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) ativadas, além de concluir a integração padrão de push.

## Etapa 2: ativar serviços de localização do Braze
Os serviços de localização do Braze [devem ser ativados](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) através do SDK. Eles não estão habilitados por padrão.

## Etapa 3: Ativar geofences

Ative as geofences definindo `location.geofencesEnabled` como `true` no objeto `configuration` que inicializa a instância [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Outras `location` opções de configuração podem ser encontradas [aqui](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).
{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Configurations for background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Configurando geofences para relatórios em segundo plano

Por padrão, as geofences são monitoradas apenas se o seu app estiver em primeiro plano ou se tiver a autorização `Always` (que monitora todos os estados do aplicativo).

No entanto, você pode optar por monitorar eventos de geofence quando seu app estiver em segundo plano ou quando tiver `When In Use` autorização adicionando a capacidade `Background Mode -> Location updates` ao seu projeto Xcode e ativando `allowBackgroundGeofenceUpdates`. Isso permite que a Braze estenda o status "em uso" do seu app monitorando continuamente as atualizações de local.

`allowBackgroundGeofenceUpdates` só funciona quando seu app está em segundo plano. Quando reabre, seus processos em segundo plano existentes são pausados, para que os processos em primeiro plano possam ser priorizados.

{% alert important %}
Para evitar o consumo excessivo de bateria e a limitação de taxa, certifique-se de configurar `distanceFilter` para um valor que atenda às necessidades específicas do seu app. Configurar `distanceFilter` para um valor mais alto impede que seu app solicite a localizaçāo do usuário com muita frequência.
{% endalert %}

## Etapa 4: Verifique o push de fundo do Braze

Braze sincroniza geofences com dispositivos usando notificações por push em segundo plano. Siga o artigo [ignorando push silencioso]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) para garantir que seu aplicativo não tome nenhuma ação indesejada ao receber notificações de sincronização de geofence do Braze.

## Etapa 5: Adicione strings de descrição de uso de local ao seu Info.plist

Adicione a chave `NSLocationAlwaysUsageDescription`, `NSLocationAlwaysAndWhenInUseUsageDescription` ou `NSLocationWhenInUseUsageDescription` ao `info.plist` com um valor `String` que tenha uma descrição de por que seu aplicativo precisa rastrear local.

Esta descrição será exibida quando o prompt de localização do sistema solicitar autorização e deve explicar claramente os benefícios do monitoramento de localização para seus usuários.

## Etapa 6: Solicitar autorização do usuário

Ao solicitar autorização de um usuário, você pode solicitar [`When In Use`](#when-in-use) ou [`Always`](#always) autorização.

### Quando em uso

Para solicitar autorização `When In Use`, use o método `requestWhenInUseAuthorization()`:

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endtab %}

{% tab OBJECTIVE C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endtab %}
{% endtabs %}

### Sempre

Por padrão, `requestAlwaysAuthorization()` só concede ao seu app `When In Use` autorização e solicitará novamente ao seu usuário para autorização `Always` após algum tempo. No entanto, você pode optar por solicitar imediatamente ao seu usuário chamando `requestWhenInUseAuthorization()`, depois chamando `requestAlwaysAuthorization()` após receber sua autorização inicial `When In Use`.

{% alert important %}
Você só pode solicitar `Always` autorização uma única vez imediatamente.
{% endalert %}

{% tabs %}
{% tab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endtab %}

{% tab OBJECTIVE C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endtab %}
{% endtabs %}

## Etapa 7: Ativar geofences no dashboard

O iOS permite armazenar até 20 geofences para um determinado app. Com as geofences ativadas, a Braze usará alguns desses 20 slots disponíveis. Para evitar interrupções acidentais ou indesejadas em outras funcionalidades relacionadas ao geofence no seu app, geofences de local devem ser ativados para apps individuais no dashboard. Para que nossos serviços de localização funcionem corretamente, verifique se seu app não está usando todos os pontos de geofence disponíveis.

Existem duas maneiras de ativar geofences para um app específico: na página **Locais** ou na página **Gerenciar Configurações**.

### Ativar geofences na página de Localizações

Ativar geofences na página **Locais** do dashboard.

1. Acessar **público** > **Locais**.
{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Locais** em **engajamento**.
{% endalert %}

{:start="2"}
2\. O número de aplicativos no seu espaço de trabalho que atualmente têm geofences habilitados é exibido abaixo do mapa, por exemplo: **0 de 1 apps com geofences ativados**. Clique neste texto.
3\. Selecione o app para ativar geofences. Clique **Concluído.**
![As opções de geofence na página de locais da Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Ativar geofences na página de Gerenciar configurações

Ativar geofences nas configurações do seu app.

1. Acessar **Configurações** > **Configurações do app**.
{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar geofences em **Gerenciar Configurações** > **Configurações**.
{% endalert %}

{:start="2"}
2\. Selecione o app para o qual você deseja ativar geofences.
3\. Selecione a caixa de seleção **Geofences Enabled**. Clique **Salvar.**

![A caixa de seleção de geofences localizada nas páginas de configurações da Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desativando solicitações automáticas de geofence

Você pode desativar solicitações automáticas de geofence no seu `configuration` objeto passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Defina `automaticGeofenceRequests` como `false`. Por exemplo:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Se você optar por usar essa opção, será necessário solicitar manualmente as geofences para que o recurso funcione.

## Solicitação manual de geofences

Quando o SDK da Braze solicita geofences para monitorar do backend, ele relata a localização atual do usuário e recebe geofences que são determinados como sendo otimamente relevantes com base na localização relatada. Há um limite de frequência de uma atualização de geofence por sessão.

Para controlar o local que o SDK relata para fins de recebimento das geofences mais relevantes, você pode solicitar manualmente as geofences fornecendo a latitude e longitude de um local. Recomenda-se desativar solicitações automáticas de geofence ao usar este método. Para fazer isso, use o seguinte código:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

