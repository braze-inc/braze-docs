{% alert important %}
A partir do iOS 14, geofences não funcionam de forma confiável para usuários que optam por dar apenas permissão para sua localização aproximada.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar no Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Ative os serviços de localização do seu app

Por padrão, os serviços de localização do Braze não estão ativados. Para ativá-los no seu app, complete as seguintes etapas. Para um tutorial passo a passo, veja [Tutorial: Localizações e Geofences do Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Etapa 2.1: Adicione o módulo `BrazeLocation`

No Xcode, abra a guia **Geral**. Em **Frameworks, Bibliotecas e Conteúdo Embutido**, adicione o módulo `BrazeLocation`.

![Adicione o módulo BrazeLocation no seu projeto Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Etapa 2.2: Atualize seu `Info.plist`

No seu `info.plist`, atribua um valor `String` a uma das seguintes chaves que descrevem por que seu aplicativo precisa rastrear a localização. Essa string será exibida quando seus usuários forem solicitados a permitir serviços de localização, então certifique-se de explicar claramente o valor de ativar esse recurso para seu app.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist strings de localização no Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
A Apple descontinuou `NSLocationAlwaysUsageDescription`. Para mais informações, veja [documentação do desenvolvedor da Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Etapa 3: Ative geofences no seu código

No código do seu app, ative geofences definindo `location.geofencesEnabled` como `true` no objeto `configuration` que inicializa a instância [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Para outras opções de configuração `location`, veja [referência do SDK Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Etapa 3.1: Ativar relatórios em segundo plano (opcional)

Por padrão, eventos de geofence são monitorados apenas se seu app estiver em primeiro plano ou tiver `Always` autorização, que monitora todos os estados do aplicativo.

No entanto, você pode optar por monitorar eventos de geofence se seu app estiver em segundo plano ou tiver [`When In Use` autorização](#swift_request-authorization). 

Para monitorar esses eventos adicionais de geofence, abra seu projeto no Xcode, depois vá para **Assinatura & Capacidades**. Em **Modos em segundo plano**, marque **Atualizações de localização**.

![No Xcode, Modo em segundo plano > Atualizações de localização]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Em seguida, ative `allowBackgroundGeofenceUpdates` no código do seu app. Isso permite que a Braze estenda o status "Quando em uso" do seu app, monitorando continuamente as atualizações de localização. Essa configuração só funciona quando seu app está em segundo plano. Quando o app é reaberto, todos os processos em segundo plano existentes são pausados e os processos em primeiro plano são priorizados.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Para evitar consumo excessivo de bateria e limitação de taxa, configure `distanceFilter` para um valor que atenda às necessidades específicas do seu app. Configurar `distanceFilter` para um valor mais alto impede que seu app solicite a localizaçāo do usuário com muita frequência.
{% endalert %}

### Etapa 4: Solicitar autorização {#request-authorization}

Ao solicitar autorização de um usuário, peça autorização `When In Use` ou `Always`.

{% tabs local %}
{% tab When In Use %}
Para solicitar autorização `When In Use`, use o método `requestWhenInUseAuthorization()`:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
Por padrão, `requestAlwaysAuthorization()` só concede ao seu app `When In Use` autorização e solicitará novamente ao seu usuário para autorização `Always` após algum tempo.

No entanto, você pode optar por solicitar imediatamente ao seu usuário, chamando primeiro `requestWhenInUseAuthorization()` e depois chamando `requestAlwaysAuthorization()` após receber sua `When In Use` autorização inicial.

{% alert important %}
Você só pode solicitar `Always` autorização uma única vez imediatamente.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 5: Verificar push em segundo plano

Braze sincroniza geofences com dispositivos usando notificações por push em segundo plano. Siga estas instruções para [configurar notificações push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) para que as atualizações de geofence do servidor sejam tratadas corretamente.

{% alert note %}
Para garantir que seu aplicativo não tome ações indesejadas ao receber notificações de sincronização de geofence da Braze, siga o artigo [ignorando push silencioso]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Solicitar geofences manualmente {#manually-request-geofences}

Quando o SDK da Braze solicita geofences do backend, ele reporta a localização atual do usuário e recebe geofences que são determinadas como otimalmente relevantes com base na localização reportada.

Para controlar a localização que o SDK reporta para receber as geofences mais relevantes, você pode solicitar geofences manualmente fornecendo as coordenadas desejadas.

### Etapa 1: Defina `automaticGeofenceRequests` como `false`

Você pode desativar solicitações automáticas de geofence no seu `configuration` objeto passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Defina `automaticGeofenceRequests` como `false`.

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
{% tab OBJECTIVE-C %}

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

### Etapa 2: Chame `requestGeofences` manualment

No seu código, solicite geofences com a latitude e longitude apropriadas.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Perguntas Frequentes (FAQ) {#faq}

#### Por que não estou recebendo geofences no meu dispositivo?

Para confirmar se os geofences estão sendo recebidos no seu dispositivo, primeiro use a [ferramenta de depuração do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) para verificar os registros do SDK. Você poderá ver se os geofences estão sendo recebidos com sucesso do servidor e se há algum erro notável.

Abaixo estão outras possíveis razões pelas quais os geofences podem não ser recebidos no seu dispositivo:

##### limitações do sistema operacional iOS

O sistema operacional iOS permite armazenar até 20 geofences para um determinado app. Com as geofences ativadas, a Braze usará alguns desses 20 slots disponíveis.

Para evitar interrupções acidentais ou indesejadas em outras funcionalidades relacionadas a geofences no seu app, você deve ativar os geofences de localização para aplicativos individuais no dashboard. Para que nossos serviços de localização funcionem corretamente, verifique se seu app não está usando todos os pontos de geofence disponíveis.

##### Limite de taxa

O Braze tem um limite de 1 atualização de geofence por sessão para evitar solicitações desnecessárias.

#### Como funciona se estou usando tanto recursos de geofence do Braze quanto não-Braze?

Como mencionado acima, o iOS permite que um único app armazene um máximo de 20 geofences. Esse armazenamento é compartilhado entre geofences do Braze e não-Braze e é gerenciado pelo [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Por exemplo, se seu app contém 20 geofences não-Braze, não haverá armazenamento para rastrear geofences do Braze (ou vice-versa). Para receber novos geofences, você precisará usar [APIs de localização da Apple](https://developer.apple.com/documentation/corelocation) para parar de monitorar alguns dos geofences existentes no dispositivo.

#### A funcionalidade de Geofences pode ser usada enquanto um dispositivo está offline?

Um dispositivo precisa estar conectado à internet apenas quando uma atualização ocorre. Uma vez que ele tenha recebido com sucesso geofences do servidor, é possível registrar uma entrada ou saída de geofence mesmo que o dispositivo esteja offline. Isso ocorre porque a localização de um dispositivo opera separadamente de sua conectividade com a internet.

Por exemplo, digamos que um dispositivo recebeu e registrou com sucesso geofences no início da sessão e fica offline. Se entrar em uma dessas geofences registradas, pode disparar uma campanha do Braze.

#### Por que as geofences não são monitoradas quando meu app está em segundo plano/terminado?

Sem `Always` autorização, a Apple restringe os serviços de localização de funcionar enquanto um app não está em uso. Isso é imposto pelo sistema operacional e está fora do controle do SDK do Braze. Embora o Braze ofereça configurações separadas para executar serviços enquanto o app está em segundo plano, não há como contornar essas restrições para apps que são terminados sem receber autorização explícita do usuário.