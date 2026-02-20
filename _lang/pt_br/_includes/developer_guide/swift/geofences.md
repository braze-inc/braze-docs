{% alert important %}
A partir do iOS 14, as geofences não funcionam de forma confiável para usuários que optam por dar permissão apenas para o local aproximado.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuração de geofences {#setting-up-geofences}

### Etapa 1: Capacitação em Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Ative os serviços de local do seu app

Por padrão, os serviços de local do Braze não estão ativados. Para ativá-las em seu app, conclua as etapas a seguir. Para obter um tutorial passo a passo, consulte [Tutorial: Locais do Braze e geofences](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Etapa 2.1: Adicione o módulo `BrazeLocation` 

No Xcode, abra a guia **General**. Em **Frameworks, Libraries, and Embedded Content**, adicione o módulo `BrazeLocation`.

![Adicione o módulo BrazeLocation em seu projeto Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Etapa 2.2: Atualize seu `Info.plist`

Em seu `info.plist`, atribua um valor `String` a uma das seguintes chaves que descreva por que seu aplicativo precisa rastrear o local. Essa string será exibida quando os usuários forem solicitados a usar os serviços locais, portanto, certifique-se de explicar claramente o valor de ativar esse recurso para o seu app.

- `NSLocationAlwaysAndWhenInUseUsageDescription` 
- `NSLocationWhenInUseUsageDescription`

![Info.plist strings de local no Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
A Apple descontinuou o site `NSLocationAlwaysUsageDescription`. Para saber mais, consulte [a documentação do desenvolvedor da Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Etapa 3: Ative as geofences em seu código

No código de seu app, ative as geofences definindo `location.geofencesEnabled` como `true` no objeto `configuration` que inicializa a [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/) instância. Para obter outras opções de configuração do site `location`, consulte [a referência do Braze Swift SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

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

Por padrão, os eventos de geofence só são monitorados se o app estiver em primeiro plano ou se tiver a autorização `Always`, que monitora todos os estados do aplicativo.

No entanto, você pode optar por monitorar também os eventos de geofence se o seu app estiver em segundo plano ou tiver [autorização`When In Use` ](#swift_request-authorization). 

Para monitorar esses eventos adicionais de geofence, abra seu projeto Xcode e acesse **Acessar & Capabilities**. Em **Modos de segundo plano**, verifique **Atualizações de local**.

![No Xcode, Modo de segundo plano > Atualizações de local]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Em seguida, ative o `allowBackgroundGeofenceUpdates` no código do seu app. Isso permite que o Braze estenda o status "Quando em uso" do seu app, monitorando continuamente as atualizações do local. Essa configuração só funciona quando o app está em segundo plano. Quando o app é reaberto, todos os processos em segundo plano existentes são pausados e os processos em primeiro plano são priorizados.

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
Para evitar o esgotamento da bateria e o limite de frequência, configure `distanceFilter` em um valor que atenda às necessidades específicas do seu app. Configurar `distanceFilter` para um valor mais alto impede que seu app solicite a localizaçāo do usuário com muita frequência.
{% endalert %}

### Etapa 4: Solicitar autorização {#request-authorization}

Ao solicitar a autorização de um usuário, solicite a autorização `When In Use` ou `Always`.

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

No entanto, você pode optar por avisar imediatamente o usuário ligando primeiro para `requestWhenInUseAuthorization()` e depois para `requestAlwaysAuthorization()` após receber a autorização inicial de `When In Use`.

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

### Etapa 5: Verificar o push em segundo plano

Braze sincroniza geofences com dispositivos usando notificações por push em segundo plano. Siga estas instruções para [configurar notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) para que as atualizações de geofence do servidor sejam tratadas adequadamente.

{% alert note %}
Para garantir que seu aplicativo não execute nenhuma ação indesejada ao receber notificações de sincronização de geofence do Braze, siga o artigo [Ignorando o push silencioso]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).
{% endalert %}

## Solicitar geofences manualmente {#manually-request-geofences}

Quando o SDK do Braze solicita geofences do backend, ele informa o local atual do usuário e recebe geofences que são determinadas como relevantes de forma ideal com base no local informado.

Para controlar o local que o SDK informa para receber os geofences mais relevantes, você pode solicitar geofences manualmente fornecendo as coordenadas desejadas.

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

### Etapa 2: Ligue para `requestGeofences` manualmente

Em seu código, solicite geofences com a latitude e a longitude apropriadas.

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

#### Por que não estou recebendo geofences em meu dispositivo?

Para confirmar se as geofences estão ou não sendo recebidas no seu dispositivo, primeiro use a [ferramenta SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) para verificar os registros do SDK. Poderá então ver se as geofences estão sendo recebidas com sucesso do servidor e se há algum erro notável.

Abaixo estão outros possíveis motivos pelos quais as geofences podem não ser recebidas em seu dispositivo:

##### Limitações do sistema operacional iOS

O sistema operacional iOS só permite o armazenamento de até 20 geofences para um determinado app. Com as geofences ativadas, a Braze usará alguns desses 20 slots disponíveis.

Para evitar a interrupção acidental ou indesejada de outras funcionalidades relacionadas a geofences em seu aplicativo, é necessário ativar geofences locais para aplicativos individuais no dashboard. Para que nossos serviços de localização funcionem corretamente, verifique se seu app não está usando todos os pontos de geofence disponíveis.

##### Limite de taxa

O Braze tem um limite de 1 atualização de geofence por sessão para evitar solicitações desnecessárias.

#### Como isso funciona se eu estiver usando os recursos de geofence Braze e não Braze?

Como mencionado acima, o iOS permite que um único app armazene um máximo de 20 geofences. Esse armazenamento é compartilhado por geofences Braze e não-Braze e é gerenciado pelo [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Por instância do app, se o seu aplicativo contiver 20 geofences não Braze, não haverá armazenamento para rastreamento de geofences Braze (ou vice-versa). Para receber novas geofences, será necessário usar [as APIs de local da Apple](https://developer.apple.com/documentation/corelocation) para interromper o monitoramento de algumas das geofences existentes no dispositivo.

#### O recurso Geofences pode ser usado quando um dispositivo está off-line?

Um dispositivo precisa estar conectado à Internet somente quando ocorrer uma atualização. Depois de receber geofences com sucesso do servidor, é possível registrar uma entrada ou saída de geofence mesmo que o dispositivo esteja offline. Isso ocorre porque o local de um dispositivo opera separadamente de sua conectividade com a Internet.

Por exemplo, digamos que um dispositivo tenha recebido e registrado geofences com sucesso no início da sessão e fique off-line. Se ele entrar em uma dessas geofences registradas, poderá disparar uma campanha do Braze.

#### Por que as geofences não são monitoradas quando meu app está em segundo plano/terminado?

Sem a autorização do `Always`, a Apple impede que os serviços locais sejam executados enquanto um app não estiver em uso. Isso é imposto pelo sistema operacional e está fora do controle do SDK do Braze. Embora o Braze ofereça configurações separadas para executar serviços enquanto o aplicativo está em segundo plano, não há como contornar essas restrições para aplicativos que são encerrados sem receber autorização explícita do usuário.