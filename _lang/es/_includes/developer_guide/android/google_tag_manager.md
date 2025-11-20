{% multi_lang_include developer_guide/prerequisites/android.md %}

## Uso de Google Tag Manager para Android

En el siguiente ejemplo, una aplicación de streaming de música quiere registrar diferentes eventos a medida que los usuarios escuchan canciones. Mediante Google Tag Manager para Android, pueden controlar qué proveedores externos de Braze reciben este evento, y crear etiquetas específicas para Braze.

### Paso 1: Crear un desencadenante para eventos personalizados

Los eventos personalizados se registran con `actionType` configurado en `logEvent`. En este ejemplo, el proveedor de etiquetas personalizadas Braze espera que el nombre del evento personalizado se configure mediante `eventName`.

Para empezar, crea un desencadenador que busque un "Nombre de evento" que sea igual a `played song`

![Un desencadenante personalizado en Google Tag Manager configurado para desencadenar algunos eventos cuando "nombre del evento" es igual a "canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

A continuación, crea una nueva etiqueta (también conocida como "Llamada a función") e introduce la ruta de clase de tu [proveedor de etiquetas personalizado](#adding-android-google-tag-provider) que se describe más adelante en este artículo. Esta etiqueta se desencadenará cuando registres el evento `played song`.

En los parámetros personalizados de la etiqueta (también conocidos como los pares clave-valor), establece `eventName` en `played song`. Este será el nombre del evento personalizado registrado en Braze.

![Una etiqueta en Google Tag Manager con classpath y campos de par clave-valor. Esta etiqueta se configura para desencadenar con el desencadenante "canción reproducida" creado previamente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

{% alert important %}
Cuando envíes un evento personalizado, asegúrate de configurar `actionType` en `logEvent`, y establece un valor para `eventName` para que Braze reciba el nombre correcto del evento y la acción a realizar.
{% endalert %}

También puedes incluir argumentos adicionales de par clave-valor en la etiqueta, que se enviarán como propiedades del evento personalizadas a Braze. `eventName` y `actionType` no se ignorarán para las propiedades del evento personalizadas. En la siguiente etiqueta de ejemplo, `genre` se pasa y se define utilizando una variable de etiqueta en Google Tag Manager, que se obtiene del evento personalizado registrado en la aplicación.

Como Google Tag Manager para Android utiliza Firebase como capa de datos, la propiedad del evento `genre` se envía a Google Tag Manager como una variable "Firebase - Parámetro de evento".

![Una variable en Google Tag Manager donde se añade "género" como parámetro de evento para la etiqueta "Braze - Evento de canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Cuando un usuario reproduzca una canción en la aplicación, se registrará un evento a través de Firebase y Google Tag Manager utilizando el nombre del evento de análisis de Firebase que coincida con el nombre desencadenante de la etiqueta, `played song`:

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

### Paso 2: Registro de atributos personalizados

Los atributos personalizados se establecen a través de un `actionType` configurado en `customAttribute`. El proveedor de etiquetas personalizadas Braze espera que el atributo personalizado clave-valor se establezca a través de `customAttributeKey` y `customAttributeValue`:

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

### Paso 3: Llama a `changeUser()`

Las llamadas a `changeUser()` se realizan a través de un `actionType` configurado en `changeUser`. El proveedor de etiquetas personalizadas Braze espera que el ID de usuario Braze se establezca mediante un par clave-valor `externalUserId` dentro de tu etiqueta:

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

### Paso 4: Añadir un proveedor de etiquetas personalizado {#adding-android-google-tag-provider}

Con las etiquetas y desencadenadores configurados, también tendrás que implementar Google Tag Manager en tu aplicación Android, que puedes encontrar en la [documentación](https://developers.google.com/tag-manager/android/v5/) de Google.

Una vez instalado Google Tag Manager en tu aplicación, añade un proveedor de etiquetas personalizado para llamar a los métodos del SDK de Braze en función de las etiquetas que hayas configurado en Google Tag Manager.

Asegúrate de anotar la "Ruta de clase" del archivo: es lo que introducirás cuando configures una etiqueta en la consola de [Google Tag Manager](https://tagmanager.google.com/).

Este ejemplo destaca una de las muchas formas en que puedes estructurar tu proveedor de etiquetas personalizado. En concreto, muestra cómo determinar a qué método del SDK de Braze llamar en función del par clave-valor `actionType` enviado desde la etiqueta GTM.

Los `actionType` que se muestran en este ejemplo son `logEvent`, `customAttribute`, y `changeUser`, pero puede que prefieras cambiar la forma en que tu proveedor de etiquetas gestiona los datos de Google Tag Manager.

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

En tu `Application.onCreate()` asegúrate de añadir la siguiente inicialización para el fragmento de código anterior:

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
