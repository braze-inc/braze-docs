---
nav_title: Identifiant Google Advertising (facultatif)
article_title: ID optionnel Google Advertising pour Android
page_order: 9
platform:
  - Android
description: "Cet article couvre les identifiants publicitaires Google et comment transmettre ces informations publicitaires au Brésil."
---

# Identifiant Google Advertising (Android seulement) facultatif

L'identifiant Google Advertising ID est un identifiant spécifique à l'utilisateur, unique et reconfigurable pour la publicité, fourni par les services Google Play. Il donne aux utilisateurs de meilleurs contrôles et fournit aux développeurs un système simple et standard pour continuer à monétiser leurs applications. Il s'agit d'un identificateur anonyme à des fins publicitaires et permet aux utilisateurs de réinitialiser leur identificateur ou de ne plus recevoir de publicités basées sur des intérêts dans les applications Google Play. Voir [ici][2] pour plus d'informations.

## Passage de l'identifiant Google Advertising à Braze

L'identifiant Google Advertising ID n'est pas automatiquement collecté par le Braze SDK et doit être défini manuellement via la méthode [`Appboy.setGoogleAdvertisingId()`][1].

{% alert important %}
Google nécessite que l'ID de la publicité soit collecté sur un fil non UI.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient. nfo idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Brésil. etInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo. sLimitAdTrackingEnabled());
    } catch (Exception e) {
      e. rintStackTrace();
    }

}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Thread(Runnable {
  try {
    val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext())
    Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.id, idInfo.isLimitAdTrackingEnabled)
  } catch (e: Exception) {
    e.printStackTrace()
  }
}).start()
```

{% endtab %}
{% endtabs %}


[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#setGoogleAdvertisingId-java.lang.String-boolean-
[2]: https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en
