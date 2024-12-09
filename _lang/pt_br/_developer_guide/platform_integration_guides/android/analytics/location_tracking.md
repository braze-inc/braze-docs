---
nav_title: monitoramento de localização
article_title: monitoramento de localização para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 6
description: "Este artigo mostra como configurar o monitoramento de localização para seu aplicativo Android ou FireOS."
Tool:
  - Location

---

# monitoramento de localização

> Este artigo mostra como configurar o monitoramento de localização para seu aplicativo Android ou FireOS.

Adicione pelo menos uma das seguintes permissões ao seu arquivo `AndroidManifest.xml` para declarar a intenção do seu app de coletar dados de local:

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION` inclui dados de GPS ao relatar a localização do usuário, enquanto `ACCESS_COARSE_LOCATION` inclui dados do provedor não-GPS mais eficiente em termos de bateria disponível (por exemplo, a rede). A localização aproximada provavelmente será suficiente para a maioria dos casos de uso de dados de local; no entanto, sob o modelo de permissões de tempo de execução, receber permissão de local do usuário autoriza implicitamente a coleta de dados de localização precisa. Dê uma olhada em [Estratégias de localização](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html) no site Android Developers para saber mais sobre as diferenças entre essas permissões de localização e como usá-las.

{% alert important %}
Com o lançamento do Android M, o Android mudou de um modelo de permissões de tempo de instalação para um modelo de permissões de tempo de execução. Para ativar o monitoramento de localização em dispositivos com Android M ou posterior, o app deve explicitamente receber permissão para usar o local do usuário (a Braze não fará isso). Depois que as permissões de localização forem obtidas, a Braze começará a rastrear automaticamente o local no início da próxima sessão, se a coleta de dados de localização estiver ativada em `braze.xml`. Dispositivos com versões anteriores do Android só exigem que permissões de localização sejam declaradas em `AndroidManifest.xml`. Para saber mais, consulte a [documentação de permissões](https://developer.android.com/training/permissions/index.html) do Android.
{% endalert %}

## Desativação do monitoramento automático de localização

### Opção de Tempo de Compilação

Para desativar o monitoramento automático de localização em tempo de compilação, defina `com_braze_enable_location_collection` como `false` em `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### Opção do tempo de Execução

Para desativar seletivamente o monitoramento automático de localização em tempo de execução, use [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## Registro manual de local

Mesmo quando o rastreamento automático estiver desativado, é possível registrar manualmente pontos de dados únicos de localização através do método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) em `BrazeUser` assim:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

