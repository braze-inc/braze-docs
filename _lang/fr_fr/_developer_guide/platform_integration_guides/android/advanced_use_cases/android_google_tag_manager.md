---
nav_title: Google Tag Manager pour Android
article_title: Google Tag Manager pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "Cet article de référence explique comment initialiser, configurer et mettre en œuvre Google Tag Manager dans votre application Android ou FireOS."

---

# Google Tag Manager pour Android

> Cet article de référence explique comment initialiser, configurer et mettre en œuvre Google Tag Manager dans votre application Android ou FireOS.

## Initialisation du SDK {#initializing-android-google-tag-provider}

Le SDK Android de Braze peut être initialisé et contrôlé par des tags configurés dans [Google Tag Manager.](https://tagmanager.google.com/)

Comme condition préalable à cette mise en œuvre, votre [intégration SDK Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration) doit être complète.

## Configuration de votre Google Tag Manager {#configuring-android-google-tag-manager}

Dans cet exemple, nous allons prétendre que nous sommes une application de streaming de musique qui veut enregistrer différents événements pendant que les utilisateurs écoutent des chansons. Grâce à Google Tag Manager pour Android, nous pouvons contrôler lequel de nos fournisseurs tiers reçoit cet événement et créer des balises spécifiques à Braze.

### Événements personnalisés

Les événements personnalisés sont enregistrés avec `actionType` réglé sur `logEvent`. Le fournisseur de balises personnalisées de Braze, dans notre exemple, attend que le nom de l’événement personnalisé soit défini à l’aide de `eventName`.

Pour commencer, créez un déclencheur qui recherche un « nom de l’événement » qui équivaut à `played song`

![Un événement personnalisé dans Google Tag Manager qui se déclenche pour certains événements lorsque "nom de l'événement" est égal à "chanson jouée".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Ensuite, créez une nouvelle balise (« Appel de fonction ») et saisissez le chemin de classe de votre [fournisseur de balises personnalisées](#adding-android-google-tag-provider), décrit plus loin dans cet article.

Cette balise sera déclenchée lorsque vous enregistrez l’événement `played song` que nous venons de créer.

Dans les paramètres personnalisés de notre balise (paires clé-valeur), nous avons défini `eventName` vers `played song` qui sera le nom de l’événement personnalisé enregistré sur Braze.

{% alert important %}
Lorsque vous envoyez un événement personnalisé, assurez-vous de définir `actionType` vers `logEvent` et de définir une valeur pour `eventName` comme illustré dans la capture d’écran suivante.

Le fournisseur de balises personnalisées dans notre exemple utilisera ces clés pour déterminer les mesures à prendre et le nom de l’événement à envoyer à Braze lorsqu’il reçoit des données de Google Tag Manager.
{% endalert %}

![Une balise dans Google Tag Manager avec des champs de chemin de classe et de paires clé-valeur. Cette étiquette est définie pour se déclencher avec le déclencheur "chanson jouée" créé précédemment.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Vous pouvez également inclure des arguments de paires clé-valeur supplémentaires à la balise, qui seront envoyés en tant que propriétés d’événement personnalisé à Braze. `eventName` et `actionType` ne seront pas ignorés pour les propriétés d’événement personnalisé. Dans l’exemple de balise suivant, nous allons transmettre `genre` qui a été défini à l’aide d’une variable de balise dans Google Tag Manager issue de l’événement personnalisé que nous avons enregistré dans notre application.

La propriété de l’événement `genre` est envoyée à Google Tag Manager en tant que variable « Firebase - paramètre de l’événement » étant donné que Google Tag Manager pour Android utilise Firebase comme couche de données.

![Une variable du Google Tag Manager où « genre » est ajouté en tant que paramètre de l’événement pour la bibliothèque « Braze - événement de musique jouée ».]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Enfin, lorsqu’un utilisateur joue une chanson dans notre application, nous allons enregistrer un événement via Firebase et Google Tag Manager en utilisant le nom d’événement d’analytique Firebase qui correspond au nom de déclencheur de notre balise, `played song` :

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

### Enregistrer des attributs personnalisés

Les attributs personnalisés sont définis via un `actionType` réglé sur `customAttribute`. Le fournisseur de balises personnalisées Braze attend de la clé-valeur d’attribut personnalisée qu’elle soit définie via `customAttributeKey` et `customAttributeValue` :

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

### Appeler changeUser

Les appels vers `changeUser()` sont réalisés via un `actionType` réglé sur `changeUser`. Le fournisseur de balises personnalisées Braze attend que l’ID utilisateur Braze soit réglé via une paire clé-valeur `externalUserId` dans votre balise :

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

## Fournisseur de balises personnalisées du Braze SDK {#adding-android-google-tag-provider}

Une fois les tags et les déclencheurs gérés, vous devrez également implémenter Google Tag Manager dans votre application Android, ce que vous trouverez dans la [documentation de](https://developers.google.com/tag-manager/android/v5/) Google.

Une fois que l'outil Google Tag Manager est installé dans votre application, ajoutez un fournisseur de balises personnalisées pour appeler les méthodes du SDK Braze en fonction des balises que vous avez configurées dans Google Tag Manager.

Veillez à noter le "chemin de classe" du fichier - c'est ce que vous indiquerez lorsque vous configurerez une étiquette dans la console du [gestionnaire Google.](https://tagmanager.google.com/) 

Cet exemple montre l’une des nombreuses façons de structurer votre fournisseur de balises personnalisées dans laquelle nous déterminons quelle méthode du SDK Braze doit être appelée en fonction de la paire clé-valeur `actionType` envoyée à partir de la balise GTM.

Les `actionType` que nous avons pris en charge dans notre exemple sont `logEvent`, `customAttribute` et `changeUser`, mais vous pouvez modifier la manière dont votre fournisseur de balises gère les données de Google Tag Manager.

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

Dans votre `Application.onCreate()` assurez-vous d’ajouter l’initialisation suivante pour l’extrait de code précédent :

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

