{% alert important %}
Os geofences são suportados em **ambos iOS e Android** no SDK do React Native. O `requestLocationInitialization` método é exclusivo do Android e não é necessário para iOS. O `requestGeofences` método está disponível em ambas as plataformas. Por padrão, o SDK pode solicitar e monitorar geofences automaticamente quando a localização está disponível; você pode confiar nessa configuração automática ou chamar `requestGeofences` para solicitar manualmente.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} No Android, você precisará [configurar notificações push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) para a sincronização de geofences.

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar no Braze

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Completar a configuração nativa do Android

Como o SDK do React Native usa o SDK nativo do Braze para Android, complete a configuração nativa do geofence do Android para seu projeto. O equivalente para iOS desses passos é abordado no guia de geofences do SDK nativo Swift ([passos 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)); o passo 2.1 (Adicionar o módulo BrazeLocation) não é necessário para o React Native porque o BrazeLocation já está incluído implicitamente no SDK do Braze para React Native.

1. **Atualizar `build.gradle`:** Adicionar `android-sdk-location` e os serviços de localização do Google Play. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Atualizar o manifesto:** Adicionar permissões de localização e o receptor de inicialização do Braze. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Ativar a coleta de localização do Braze:** Atualize seu `braze.xml` arquivo. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Etapa 3: Completar a configuração nativa do iOS

Como o SDK React Native usa o SDK nativo Braze iOS, complete a configuração nativa de geofence para seu projeto seguindo as instruções do SDK nativo Swift a partir da etapa 2.2: atualize seu `Info.plist` com descrições de uso de localização (etapa 2.2) e ative geofences na sua configuração Braze, incluindo `automaticGeofenceRequests = true` (etapa 3); opcionalmente, ative o relatório em segundo plano (etapa 3.1). A Etapa 2.1 (Adicionar o módulo BrazeLocation) não é necessária—BrazeLocation já está incluído implicitamente no SDK React Native da Braze. Veja [geofences iOS, etapas 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Etapa 4: Solicitar geofences do JavaScript

**No Android:** Depois que o usuário conceder permissões de localização, chame `requestLocationInitialization()` para inicializar os recursos de localização da Braze e solicitar geofences dos servidores da Braze. Este método não é suportado no iOS e não é necessário para o iOS.

**No iOS:** O equivalente é ativar a configuração `automaticGeofenceRequests` na sua configuração nativa Swift ou Objective-C da Braze (veja a Etapa 3). Com isso ativado, o SDK solicita e monitora automaticamente geofences quando a localização está disponível; nenhuma chamada JavaScript equivalente a `requestLocationInitialization` é necessária.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Etapa 5: Solicitar geofences manualmente (opcional)

Em iOS e Android, você pode solicitar manualmente uma atualização de geofence para uma coordenada GPS específica usando `requestGeofences`. Por padrão, a Braze recupera automaticamente a localização do dispositivo e solicita geofences. Para fornecer manualmente uma coordenada em vez disso:

1. Desativar solicitações automáticas de geofence. No Android, defina `com_braze_automatic_geofence_requests_enabled` como `false` na sua `braze.xml`. No iOS, defina `automaticGeofenceRequests` como `false` na sua configuração Braze.
2. Chame `requestGeofences` com a latitude e longitude desejadas:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
As geofences só podem ser solicitadas uma vez por sessão, seja automaticamente pelo SDK ou manualmente com esse método.
{% endalert %}
