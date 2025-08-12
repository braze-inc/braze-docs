---
nav_title: Localizações e Geofences
article_title: local e Geofences para iOS
platform: iOS
page_order: 6
description: "Este artigo de referência ensina a implementar locais e geofences em seu app para iOS."
Tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Locais e geocercas

Para oferecer geofences para iOS:

1. Sua integração deve suportar notificações por push em segundo plano.
2. [É preciso ativar]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/#enabling-automatic-location-tracking) as geofences da Braze pelo SDK, seja implícita (com a ativação da coleta de local) ou explicitamente (com a ativação da coleta de geofence). Eles não estão habilitados por padrão.

{% alert important %}
A partir do iOS 14, as geofences têm funcionamento instável para os usuários que optam por dar permissão de localização aproximada.
{% endalert %}

## Etapa 1: ativar push em segundo plano

Para usar completamente nossa estratégia de sincronização de geofences, você deve ter [background push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#use-silent-remote-notifications-to-trigger-background-work) ativado, além de completar a integração padrão de push.

## Etapa 2: ativar geofences

Por padrão, as geofences são ativadas se a coleta automática de localização estiver ativada. Você pode ativar geofences usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada booleana `EnableGeofences` e defina o valor como `YES`. Note que, antes do SDK da Braze para iOS v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.

Você também pode ativar geofences no momento da inicialização do app usando o método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). No dicionário `appboyOptions`, defina `ABKEnableGeofencesKey` como `YES`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Etapa 3: Verifique o push de fundo do Braze

Braze sincroniza geofences com dispositivos usando notificações por push em segundo plano. Siga o artigo de [customização do iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push/) para garantir que seu aplicativo não tome nenhuma ação indesejada ao receber notificações de sincronização de geofence do Braze.

## Etapa 4: Adicione NSLocationAlwaysUsageDescription ao seu Info.plist

Adicione a chave `NSLocationAlwaysUsageDescription` e `NSLocationAlwaysAndWhenInUseUsageDescription` ao seu `info.plist` com um valor `String` que tenha uma descrição do motivo pelo qual seu app precisa rastrear a localização. Ambas as chaves são exigidas pelo iOS 11 ou posterior.
Esta descrição será exibida quando o prompt de localização do sistema solicitar autorização e deve explicar claramente os benefícios do monitoramento de localização para seus usuários.

## Etapa 5: Solicitar autorização do usuário

O recurso de geofences só funciona enquanto a autorização de localização `Always` for concedida.

Para solicitar autorização de localização `Always`, use o seguinte código:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Etapa 6: Ativar geofences no dashboard

O iOS permite armazenar até 20 geofences para um determinado app. O uso das localizações consumirá alguns desses 20 geofences disponíveis. Para evitar interrupções acidentais ou indesejadas em outras funcionalidades relacionadas ao geofence no seu app, os geofences de local devem ser ativados para apps individuais no dashboard.

Para que as localizações funcionem corretamente, confira também se seu app não está usando todos os geofences disponíveis.

### Ativar geofences na página de locais:

![As opções de geofence na página de locais do Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Ativar geofences na página de configurações:

![A caixa de seleção de geofences localizada nas páginas de configurações da Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desativando solicitações automáticas de geofence

A partir da versão 3.21.3 do SDK do iOS, é possível desativar as geofences para que não sejam solicitadas automaticamente. Você pode fazer isso usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada booleana `DisableAutomaticGeofenceRequests` e defina o valor como `YES`.

Você também pode desativar solicitações automáticas de geofences na inicialização do app pelo método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). No dicionário `appboyOptions`, defina `ABKDisableAutomaticGeofenceRequestsKey` como `YES`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Se você optar por usar essa opção, será necessário solicitar manualmente as geofences para que o recurso funcione.

## Solicitação manual de geofences

Quando o SDK da Braze solicita geofences para monitorar do backend, ele relata a localização atual do usuário e recebe geofences que são determinados como sendo otimamente relevantes com base na localização relatada. Há um limite de frequência de uma atualização de geofence por sessão.

Para controlar o local que o SDK relata para fins de receber as geofences mais relevantes, a partir da versão 3.21.3 do SDK do iOS, é possível solicitar manualmente as geofences informando a latitude e longitude de um local. Recomenda-se desativar solicitações automáticas de geofences ao usar esse método. Para fazer isso, use o seguinte código:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}


