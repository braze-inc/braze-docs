## Registro do local atual

Mesmo que o monitoramento contínuo esteja desativado, é possível registrar manualmente o local atual do usuário usando o método [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html) método.

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

## Monitoramento contínuo da localização

{% alert important %}
[A partir do Android Marshmallow](https://developer.android.com/training/permissions/index.html), é necessário pedir aos usuários que aceitem explicitamente o monitoramento de localização. Assim que o fizerem, o Braze poderá iniciar o monitoramento de sua localização no início da próxima sessão. Isso é diferente das versões anteriores do Android, em que era necessário apenas declarar as permissões de local em seu site `AndroidManifest.xml`.
{% endalert %}

Para rastrear continuamente a localização de um usuário, será necessário declarar a intenção do app de coletar dados de localização adicionando pelo menos uma das seguintes permissões ao arquivo `AndroidManifest.xml`.

|Permissão|Descrição|
|---|---|
| `ACCESS_COARSE_LOCATION` | Usa o provedor não-GPS mais eficiente em termos de bateria (como uma rede doméstica). Normalmente, isso é suficiente para a maioria das necessidades de dados locais. No modelo de permissões de tempo de execução, a concessão de permissão de local autoriza implicitamente a coleta de dados de localização fina. |
| `ACCESS_FINE_LOCATION`   | Inclui dados de GPS para um local mais preciso. No modelo de permissões de tempo de execução, a concessão de permissão de local também abrange o acesso fino ao local. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Seu `AndroidManifest.xml` deve ser semelhante ao seguinte:

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## Desativar o rastreamento contínuo

É possível desativar o rastreamento contínuo em tempo de compilação ou em tempo de execução.

{% tabs local %}
{% tab tempo de compilação %}

Para desativar o monitoramento contínuo de localização em tempo de compilação, defina `com_braze_enable_location_collection` como `false` em `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab tempo de execução %}

Para desativar seletivamente o monitoramento contínuo de localização em tempo de execução, use [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
