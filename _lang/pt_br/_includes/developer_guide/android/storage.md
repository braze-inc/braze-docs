# Armazenamento

> Este artigo descreve as diferentes propriedades no nível de dispositivo capturadas ao usar o Braze Android SDK.

## Propriedades do dispositivo

Por padrão, o Braze coletará as seguintes [propriedades no nível do dispositivo](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html) para permitir a personalização de mensagens com base no dispositivo, no idioma e no fuso horário:

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` e `TIMEZONE` não são coletados se forem `null` ou estiverem em branco. `GOOGLE_ADVERTISING_ID` não é coletado automaticamente pelo SDK e deve ser passado via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}

Você pode desativar ou especificar as propriedades que deseja coletar, definindo-as usando [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) e [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html).

O exemplo a seguir mostra a lista de permissões do objeto de dispositivo para incluir somente a versão do sistema operacional Android e a localização do dispositivo no objeto de dispositivo:
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Por padrão, todos os campos estão ativados. Observe que, sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, a entrega no horário local não funcionará sem o fuso horário.

Visite nosso artigo sobre [a coleta de dados do SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) para saber mais sobre as propriedades do dispositivo coletadas automaticamente.


