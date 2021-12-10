---
nav_title: Google Tag Manager pour Android
article_title: Google Tag Manager pour Android pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 8
description: "Cet article couvre la façon d'initialiser, de configurer et d'implémenter le gestionnaire de Google Tag dans votre application Android."
---

# Google Tag Manager pour Android

## Initialisation du SDK {#initializing-android-google-tag-provider}

Le SDK Android de Braze peut être initialisé et contrôlé par des balises configurées dans [Google Tag Manager][5].

Mais d'abord - avant d'utiliser Google Tag Manager - assurez-vous d'abord de suivre notre [Configuration initiale du SDK][1].

## Configuration de votre Google Tag Manager {#configuring-android-google-tag-manager}

Dans notre exemple, nous allons prétendre que nous sommes une application de streaming de musique qui veut enregistrer différents événements lorsque les utilisateurs écoutent des chansons. En utilisant Google Tag Manager pour Android, nous pouvons contrôler lequel de nos fournisseurs tiers reçoivent cet événement, et créer des tags spécifiques au Brésil.

### Événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur de balises personnalisées Braze dans notre exemple attend que le nom de l'événement personnalisé soit défini en utilisant `eventName`.

Pour commencer, créez un trigger qui recherche un "Nom de l'événement" qui équivaut à `la musique jouée`

!\[Déclenchement du nom de l'événement pour les événements\]\[3\]

Ensuite, créez un nouveau tag ("Appel de fonction") et entrez le chemin de classe de votre [fournisseur de tags personnalisés](#adding-android-google-tag-provider) décrit plus loin dans cet article.

Ce tag sera déclenché lorsque vous enregistrez l'événement `de la chanson jouée` que nous venons de créer.

Dans notre exemple de paramètres personnalisés (paires clé-valeur), nous avons mis `eventName` à `joué la musique` - qui sera le nom de l'événement personnalisé enregistré sur Braze.

{% alert important %}
Lors de l'envoi d'un événement personnalisé, assurez-vous de définir `actionType` à `logEvent`, et définissez une valeur pour `eventName` comme indiqué dans la capture d'écran ci-dessous.

Le fournisseur de tags personnalisés dans notre exemple utilisera ces clés pour déterminer les actions à entreprendre, et quel nom d'événement envoyer à Braze quand il reçoit des données de Google Tag Manager.
{% endalert %}

!\[Tag d'appel de la fonction\]\[4\]

Vous pouvez également inclure des arguments de paire de clés supplémentaires à la balise, qui seront envoyés en tant que propriétés d'événement personnalisées à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d'événement personnalisées. Dans notre exemple de balise ci-dessous, nous passerons en `genre` qui a été défini en utilisant une balise Variable dans Google Tag Manager - provenant de l'événement personnalisé que nous avons connecté dans notre application.

La propriété événement `genre` est envoyée à Google Tag Manager une variable "Firebase - Event Parameter" depuis que Google Tag Manager pour Android utilise Firebase comme couche de données.

!\[Tag Variable Event Name\]\[6\]

Enfin, lorsqu'un utilisateur joue une chanson dans notre application, nous allons enregistrer un événement via Firebase/Google Tag Manager en utilisant le nom de l'événement Firebase Analytics qui correspond au nom de trigger de notre tag, `a joué la chanson`.

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
params.putInt("nombre de fois écouté", 42);
mFirebaseAnalytics!!logEvent("chanson jouée", params)
```

{% endtab %}
{% endtabs %}

### Logging des attributs personnalisés

Les attributs personnalisés sont définis via un `actionType` défini à `customAttribute`. Le fournisseur de balises personnalisées Braze attend la valeur de clé d'attribut personnalisé à être définie via `customAttributeKey` et `customAttributeValue`.

{% tabs %}
{% tab JAVA %}

```java
Paramètres du bundle = new Bundle();
params.putString("customAttributeKey", "chanson préférée");
params.putString("customAttributeValue", "Private Eyes");
mFirebaseAnalytics.logEvent("customAttribute", params);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val params = Bundle()
params.putString("customAttributeKey", "chanson préférée")
params.putString("customAttributeValue", "Private Eyes")
mFirebaseAnalytics!!.logEvent("customAttribute", params)
```

{% endtab %}
{% endtabs %}

### Calling changeUser

Les appels à `changeUser()` sont faits via une `actionType` définie à `changeUser`. Le fournisseur de balises personnalisées Braze attend que l'ID de l'utilisateur Braze soit défini via une paire clé-valeur `externalUserId` dans votre tag.

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
mFirebaseAnalytics!!.logEvent("changeUser", params)
```

{% endtab %}
{% endtabs %}

## Fournisseur de tags personnalisés Braze SDK {#adding-android-google-tag-provider}

Avec les tags et les déclencheurs configurés, vous devrez également implémenter Google Tag Manager dans votre application Android que vous trouverez dans la documentation [de Google][2]

Once Google Tag Manager is installed in your app, add a custom tag provider to call Braze SDK methods based on the tags you've configured within Google Tag Manager.

Be sure to note the "Class Path" to the file which - this is what you'll enter when setting up a Tag in the [Google Tag Manager][5] console.

This example shows one of many ways to structure your custom tag provider, where we determine which Braze SDK method to call based on the `actionType` key-value pair sent down from the GTM Tag.

The `actionType` we've supported in our example are `logEvent`, `customAttribute`, and `changeUser`, but you may prefer to change how your tag provider handles data from Google Tag Manager.

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
   * Must be set before calling any of the below methods to
   * ensure that the proper application context is available when needed.
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

    BrazeUser brazeUser = Braze.getInstance(sApplicationContext).getCurrentUser();
    if (brazeUser == null) {
      BrazeLogger.w(TAG, "BrazeUser was null. Returning.");
      return;
    }

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

    val brazeUser = Braze.getInstance(sApplicationContext).currentUser
    if (brazeUser == null) {
      BrazeLogger.w(TAG, "BrazeUser was null. Returning.")
      return
    }

    when (value) {
      is Boolean -> brazeUser.setCustomUserAttribute(key, (value as Boolean?)!!)
      is Int -> brazeUser.setCustomUserAttribute(key, (value as Int?)!!)
      is Long -> brazeUser.setCustomUserAttribute(key, (value as Long?)!!)
      is String -> brazeUser.setCustomUserAttribute(key, value as String?)
      is Double -> brazeUser.setCustomUserAttribute(key, (value as Double?)!!)
      is Float -> brazeUser.setCustomUserAttribute(key, (value as Float?)!!)
      else -> BrazeLogger.w(TAG, "Failed to parse value into a custom "
          + "attribute accepted type. Key: '" + key + "' Value: '" + value + "'")
    }
  }

  private fun changeUser(tagParameterMap: Map<String, Any>) {
    val userId = tagParameterMap[CHANGE_USER_ID_VARIABLE].toString()
    Braze.getInstance(sApplicationContext).changeUser(userId)
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(BrazeGtmTagProvider::class.java!!)
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
     * Must be set before calling any of the below methods to
     * ensure that the proper application context is available when needed.
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

Dans votre `Application.onCreate()` assurez-vous d'ajouter l'initialisation suivante pour le snippet précédent :

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
[3]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %} [4]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %} [6]: {% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration
[2]: https://developers.google.com/tag-manager/android/v5/
[5]: https://tagmanager.google.com/
