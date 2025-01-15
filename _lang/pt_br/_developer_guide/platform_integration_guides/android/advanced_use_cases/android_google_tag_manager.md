---
nav_title: Google Tag Manager para Android
article_title: Google Tag Manager para Android para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Este artigo de referência aborda como inicializar, configurar e implementar o Google Tag Manager em seu app para Android ou FireOS."

---

# Google Tag Manager para Android

> Este artigo de referência aborda como inicializar, configurar e implementar o Google Tag Manager em seu app para Android ou FireOS.

## Inicialização do SDK {#initializing-android-google-tag-provider}

O SDK Braze Android pode ser inicializado e controlado por tags configuradas dentro do [Google Tag Manager](https://tagmanager.google.com/).

Como pré-requisito para essa implementação, sua [integração do SDK do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration) deve estar completa.

## Configuração do Google Tag Manager {#configuring-android-google-tag-manager}

Neste exemplo, vamos fingir que somos um app de streaming de música que deseja fazer o registro de diferentes eventos à medida que os usuários ouvem as músicas. Usando o Google Tag Manager para Android, podemos controlar quais de nossos fornecedores terceirizados recebem esse evento e criar tags específicas para o Braze.

### Eventos personalizados

Os eventos personalizados são registrados com `actionType` definido como `logEvent`. O provedor de tag personalizada do Braze em nosso exemplo está esperando que o nome do evento personalizado seja definido usando `eventName`.

Para começar, crie um disparador que procure um "Nome do evento" igual a `played song`

![Um gatilho personalizado no Google Tag Manager configurado para disparar para alguns eventos quando "nome do evento" é igual a "música tocada".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Em seguida, crie uma nova tag ("Function Call") e insira a jornada da classe de seu [provedor de tag personalizado](#adding-android-google-tag-provider) descrito mais adiante neste artigo.

Essa tag será disparada quando for registrado o evento `played song` que acabamos de criar.

Nos parâmetros personalizados da nossa tag (pares de valores-chave), definimos `eventName` como `played song` \- que será o nome do evento personalizado registrado no Braze.

{% alert important %}
Ao enviar um evento personalizado, certifique-se de definir `actionType` como `logEvent` e de definir um valor para `eventName`, conforme mostrado na captura de tela a seguir.

O provedor de tag personalizado em nosso exemplo usará essa chave para determinar qual ação realizar e qual nome de evento enviar à Braze quando receber dados do Google Tag Manager.
{% endalert %}

![Uma tag no Google Tag Manager com classpath e campos de par de valores chave. Esta tag está configurada para disparar com o gatilho "música tocada" criado anteriormente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Você também pode incluir argumentos adicionais de pares de valores-chave na tag, que serão enviados como propriedades de eventos personalizados para o Braze. `eventName` e `actionType` não serão ignorados nas propriedades de eventos personalizados. No exemplo de tag a seguir, passaremos `genre`, que foi definido usando uma variável de tag no Google Tag Manager, proveniente do evento personalizado que registramos em nosso app.

A propriedade do evento `genre` é enviada ao Google Tag Manager como uma variável "Firebase - Event Parameter", pois o Google Tag Manager para Android usa o Firebase como camada de dados.

![Uma variável no Google Tag Manager onde "genre" é adicionado como um parâmetro de evento para a tag "Braze - Evento de Música Tocada".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Por fim, quando um usuário reproduzir uma música em nosso app, registraremos um evento por meio do Firebase e do Google Tag Manager usando o nome do evento de análise de dados do Firebase que corresponde ao nome do disparo da nossa tag, `played song`:

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("genre", "pop");
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("genre", "pop")
params.putInt("number of times listened", 42);
mFirebaseAnalytics.logEvent("played song", params)
```

{% endtab %}
{% endtabs %}

### Registro de atributos personalizados

Os atributos personalizados são definidos por meio de um `actionType` definido como `customAttribute`. O provedor de tag personalizada da Braze está esperando que o atributo personalizado chave-valor seja definido por meio de `customAttributeKey` e `customAttributeValue`:

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("customAttributeKey", "favorite song");
params.putString("customAttributeValue", "Private Eyes");
mFirebaseAnalytics.logEvent("customAttribute", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("customAttributeKey", "favorite song")
params.putString("customAttributeValue", "Private Eyes")
mFirebaseAnalytics.logEvent("customAttribute", params)
```

{% endtab %}
{% endtabs %}

### Chamada de changeUser

As chamadas para `changeUser()` são feitas por meio de um `actionType` definido como `changeUser`. O provedor de tags personalizadas do Braze espera que o ID de usuário do Braze seja definido por meio de um par de valores-chave `externalUserId` dentro da sua tag:

{% tabs %}
{% tab JAVA %}

```java
Bundle params = new Bundle();
params.putString("externalUserId", userId);
mFirebaseAnalytics.logEvent("changeUser", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("externalUserId", userId)
mFirebaseAnalytics.logEvent("changeUser", params)
```

{% endtab %}
{% endtabs %}

## Provedor de tags personalizadas do Braze SDK {#adding-android-google-tag-provider}

Com as tags e os disparadores configurados, você também precisará implementar o Google Tag Manager em seu app para Android, o que pode ser encontrado na [documentação](https://developers.google.com/tag-manager/android/v5/) do Google.

Depois que o Google Tag Manager estiver instalado em seu app, adicione um provedor de tag personalizado para chamar os métodos do Braze SDK com base nas tags que você configurou no Google Tag Manager.

Certifique-se de anotar o "Caminho da Classe" para o arquivo - é isso que você irá inserir ao configurar uma tag no console do [Google Tag Manager](https://tagmanager.google.com/).

Este exemplo mostra uma das muitas maneiras de estruturar seu provedor de tag personalizado, em que determinamos qual método do Braze SDK deve ser chamado com base no par de valores-chave `actionType` enviado pela tag GTM.

Os `actionType` suportados em nosso exemplo são `logEvent`, `customAttribute` e `changeUser`, mas você pode preferir alterar a forma como seu provedor de tag trata os dados do Google Tag Manager.

{% tabs %}
{% tab JAVA %}

```java
public class BrazeGtmTagProvider implements CustomTagProvider {
  private static final String TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider.class);
  private static final String ACTION_TYPE_KEY = "actionType";

  // Custom Events
  private static final String LOG_EVENT_ACTION_TYPE = "logEvent";
  private static final String EVENT_NAME_VARIABLE = "eventName";

  // Custom Attributes
  private static final String CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute";
  private static final String CUSTOM_ATTRIBUTE_KEY = "customAttributeKey";
  private static final String CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue";

  // Change User
  private static final String CHANGE_USER_ACTION_TYPE = "changeUser";
  private static final String CHANGE_USER_ID_VARIABLE = "externalUserId";

  private static Context sApplicationContext;

  /**
   * Must be set before calling any of the following methods
   * so that the proper application context is available when needed.
   *
   * Recommended to be called in your {@link Application#onCreate()}.
   */
  public static void setApplicationContext(Context applicationContext) {
    if (applicationContext != null) {
      sApplicationContext = applicationContext.getApplicationContext();
    }
  }

  @Override
  public void execute(Map<String, Object> map) {
    BrazeLogger.i(TAG, "Got google tag manager parameters map: " + map);

    if (sApplicationContext == null) {
      BrazeLogger.w(TAG, "No application context provided to this tag provider.");
      return;
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      BrazeLogger.w(TAG, "Map does not contain the Braze action type key: " + ACTION_TYPE_KEY);
      return;
    }
    String actionType = String.valueOf(map.remove(ACTION_TYPE_KEY));

    switch (actionType) {
      case LOG_EVENT_ACTION_TYPE:
        logEvent(map);
        break;
      case CUSTOM_ATTRIBUTE_ACTION_TYPE:
        setCustomAttribute(map);
        break;
      case CHANGE_USER_ACTION_TYPE:
        changeUser(map);
        break;
      default:
        BrazeLogger.w(TAG, "Got unknown action type: " + actionType);
        break;
    }
  }

  private void logEvent(Map<String, Object> tagParameterMap) {
    String eventName = String.valueOf(tagParameterMap.remove(EVENT_NAME_VARIABLE));
    Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap));
  }

  private BrazeProperties parseMapIntoProperties(Map<String, Object> map) {
    BrazeProperties brazeProperties = new BrazeProperties();
    for (Map.Entry<String, Object> entry : map.entrySet()) {
      final Object value = entry.getValue();
      final String key = entry.getKey();
      if (value instanceof Boolean) {
        brazeProperties.addProperty(key, (Boolean) value);
      } else if (value instanceof Integer) {
        brazeProperties.addProperty(key, (Integer) value);
      } else if (value instanceof Date) {
        brazeProperties.addProperty(key, (Date) value);
      } else if (value instanceof Long) {
        brazeProperties.addProperty(key, (Long) value);
      } else if (value instanceof String) {
        brazeProperties.addProperty(key, (String) value);
      } else if (value instanceof Double) {
        brazeProperties.addProperty(key, (Double) value);
      } else {
        BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'");
      }
    }

    return brazeProperties;
  }

  private void setCustomAttribute(Map<String, Object> tagParameterMap) {
    String key = String.valueOf(tagParameterMap.get(CUSTOM_ATTRIBUTE_KEY));
    Object value = tagParameterMap.get(CUSTOM_ATTRIBUTE_VALUE_KEY);

    Braze.getInstance(sApplicationContext).getCurrentUser(new IValueCallback<BrazeUser>() {
      @Override
      public void onSuccess(BrazeUser brazeUser) {
        if (value instanceof Boolean) {
          brazeUser.setCustomUserAttribute(key, (Boolean) value);
        } else if (value instanceof Integer) {
          brazeUser.setCustomUserAttribute(key, (Integer) value);
        } else if (value instanceof Long) {
          brazeUser.setCustomUserAttribute(key, (Long) value);
        } else if (value instanceof String) {
          brazeUser.setCustomUserAttribute(key, (String) value);
        } else if (value instanceof Double) {
          brazeUser.setCustomUserAttribute(key, (Double) value);
        } else if (value instanceof Float) {
          brazeUser.setCustomUserAttribute(key, (Float) value);
        } else {
          BrazeLogger.w(TAG, "Failed to parse value into a custom "
              + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'");
        }
      }
    });
  }

  private void changeUser(Map<String, Object> tagParameterMap) {
    String userId = String.valueOf(tagParameterMap.get(CHANGE_USER_ID_VARIABLE));
    Braze.getInstance(sApplicationContext).changeUser(userId);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class BrazeGtmTagProvider : CustomTagProvider {

  override fun execute(map: MutableMap<String, Any>) {
    BrazeLogger.i(TAG, "Got google tag manager parameters map: $map")

    if (sApplicationContext == null) {
      BrazeLogger.w(TAG, "No application context provided to this tag provider.")
      return
    }

    if (!map.containsKey(ACTION_TYPE_KEY)) {
      BrazeLogger.w(TAG, "Map does not contain the Braze action type key: $ACTION_TYPE_KEY")
      return
    }
    val actionType = map.remove(ACTION_TYPE_KEY).toString()

    when (actionType) {
      LOG_EVENT_ACTION_TYPE -> logEvent(map)
      CUSTOM_ATTRIBUTE_ACTION_TYPE -> setCustomAttribute(map)
      CHANGE_USER_ACTION_TYPE -> changeUser(map)
      else -> BrazeLogger.w(TAG, "Got unknown action type: $actionType")
    }
  }

  private fun logEvent(tagParameterMap: MutableMap<String, Any>) {
    val eventName = tagParameterMap.remove(EVENT_NAME_VARIABLE).toString()
    Braze.getInstance(sApplicationContext).logCustomEvent(eventName, parseMapIntoProperties(tagParameterMap))
  }

  private fun parseMapIntoProperties(map: Map<String, Any>): BrazeProperties {
    val brazeProperties = BrazeProperties()
    map.forEach { param ->
      val key = param.key
      val value = param.value
      when (value) {
        is Boolean -> brazeProperties.addProperty(key, value)
        is Int -> brazeProperties.addProperty(key, value)
        is Date -> brazeProperties.addProperty(key, value)
        is Long -> brazeProperties.addProperty(key, value)
        is String -> brazeProperties.addProperty(key, value)
        is Double -> brazeProperties.addProperty(key, value)
        else -> BrazeLogger.w(TAG, "Failed to parse value into an BrazeProperties "
            + "accepted type. Key: '" + key + "' Value: '" + value + "'")
      }
    }

    return brazeProperties
  }

  private fun setCustomAttribute(tagParameterMap: Map<String, Any>) {
    val key = tagParameterMap[CUSTOM_ATTRIBUTE_KEY].toString()
    val value = tagParameterMap[CUSTOM_ATTRIBUTE_VALUE_KEY]

    Braze.getInstance(sApplicationContext).getCurrentUser { brazeUser ->
      when (value) {
        is Boolean -> brazeUser.setCustomUserAttribute(key, value)
        is Int -> brazeUser.setCustomUserAttribute(key, value)
        is Long -> brazeUser.setCustomUserAttribute(key, value)
        is String -> brazeUser.setCustomUserAttribute(key, value)
        is Double -> brazeUser.setCustomUserAttribute(key, value)
        is Float -> brazeUser.setCustomUserAttribute(key, value)
        else -> BrazeLogger.w(
          TAG, "Failed to parse value into a custom "
            + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'"
        )
      }
    }
  }

  private fun changeUser(tagParameterMap: Map<String, Any>) {
    val userId = tagParameterMap[CHANGE_USER_ID_VARIABLE].toString()
    Braze.getInstance(sApplicationContext).changeUser(userId)
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider::class.java)
    private val ACTION_TYPE_KEY = "actionType"

    // Custom Events
    private val LOG_EVENT_ACTION_TYPE = "logEvent"
    private val EVENT_NAME_VARIABLE = "eventName"

    // Custom Attributes
    private val CUSTOM_ATTRIBUTE_ACTION_TYPE = "customAttribute"
    private val CUSTOM_ATTRIBUTE_KEY = "customAttributeKey"
    private val CUSTOM_ATTRIBUTE_VALUE_KEY = "customAttributeValue"

    // Change User
    private val CHANGE_USER_ACTION_TYPE = "changeUser"
    private val CHANGE_USER_ID_VARIABLE = "externalUserId"

    private var sApplicationContext: Context? = null

    /**
     * Must be set before calling any of the following methods so
     * that the proper application context is available when needed.
     *
     * Recommended to be called in your [Application.onCreate].
     */
    fun setApplicationContext(applicationContext: Context?) {
      if (applicationContext != null) {
        sApplicationContext = applicationContext.applicationContext
      }
    }
  }
}
```

{% endtab %}
{% endtabs %}

Em seu site `Application.onCreate()`, não se esqueça de adicionar a seguinte inicialização para o snippet anterior:

{% tabs %}
{% tab JAVA %}

```java
BrazeGtmTagProvider.setApplicationContext(this.getApplicationContext());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeGtmTagProvider.setApplicationContext(this.applicationContext)
```

{% endtab %}
{% endtabs %}

