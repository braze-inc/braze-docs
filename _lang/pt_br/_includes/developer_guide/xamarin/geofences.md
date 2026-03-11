{% multi_lang_include developer_guide/prerequisites/xamarin.md %} Além disso, você precisará [configurar notificações por push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Pré-requisitos

Estas são as versões mínimas do SDK necessárias para começar a usar geofences:

{% sdk_min_versions xamarin:9.0.0 %}

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar no Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Em seguida, siga as instruções específicas da plataforma abaixo para Android ou iOS:

{% tabs %}
{% tab Android %}

### Etapa 2: Adicionar dependências

Adicione a seguinte referência de pacote NuGet ao seu projeto:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Etapa 3: Atualize seu AndroidManifest.xml

Adicione as seguintes permissões ao seu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
A permissão de acesso à localização em segundo plano é necessária para que os geofences funcionem enquanto o app está em segundo plano em dispositivos Android 10 ou superiores.
{% endalert %}

### Etapa 4: Configurar a coleta de localização do Braze

Certifique-se de que a coleta de localização esteja ativada na sua configuração do Braze. Se você quiser ativar geofences sem a coleta automática de localização, defina o seguinte em seu `Braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Etapa 5: Solicitar permissões de localização em tempo de execução

Você deve solicitar permissões de localização do usuário antes de registrar geofences. No seu código C#, use o seguinte padrão:

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

Após as permissões serem concedidas, inicialize a coleta de localização do Braze:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Etapa 6: Solicitar manualmente atualizações de geofence (opcional)

Para solicitar geofences manualmente para uma localização específica:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
As geofences só podem ser solicitadas uma vez por sessão, seja automaticamente pelo SDK ou manualmente com esse método.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Etapa 2: Adicionar dependências

Adicione a seguinte referência de pacote NuGet ao seu projeto:

- `Braze.iOS.BrazeLocation`

### Etapa 3: Configurar o uso de localização em Info.plist

Adicione uma descrição de uso para os serviços de localização em seu `Info.plist`:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
A Apple descontinuou `NSLocationAlwaysUsageDescription`. Use as chaves acima para iOS 14+.
{% endalert %}

### Etapa 4: Ative geofences na sua configuração do Braze

No seu código de inicialização do app (e.g., `App.xaml.cs`), configure o Braze com geofences ativados:

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### Etapa 5: Ative atualizações de localização em segundo plano (opcional)

Para monitorar geofences em segundo plano, ative o modo de fundo **Atualizações de localização** adicionando a seguinte configuração ao seu `Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Então, na sua configuração do Braze, defina:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Defina `DistanceFilter` para um valor que atenda às necessidades do seu app para evitar consumo excessivo de bateria.
{% endalert %}

### Etapa 6: Solicite autorização de localização

Solicite autorização `When In Use` ou `Always` do usuário:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Sem autorização `Always`, o iOS restringe os serviços de localização enquanto o app não está em uso. Isso é imposto pelo sistema operacional e não pode ser contornado pelo SDK do Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
