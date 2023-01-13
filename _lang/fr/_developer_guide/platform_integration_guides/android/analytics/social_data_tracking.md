---
nav_title: Suivre les données sociales
article_title: Suivre les données sociales pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 5
description: "Cet article de référence montre comment implémenter le suivi des données sociales pour votre application Android ou FireOS."

---

# Suivre les données sociales pour Android et FireOS

Comme le SDK Braze pour iOS, le SDK Braze pour Android ne recueille pas automatiquement les données Facebook et Twitter. Il est cependant possible d’ajouter des données de réseaux sociaux à un profil utilisateur Braze depuis le SDK Android :

1. Obtenir des données sur les réseaux sociaux dans votre application via le [SDK Facebook][1] et les [API Twitter][2].
2. Initialiser les objets utilisateurs Facebook et Twitter avec les données des réseaux sociaux et les transmettre à Braze.

## Constructeurs de données de réseau social

{% tabs %}
{% tab JAVA %}

```java
FacebookUser(
  String facebookId,
  String firstName,
  String lastName,
  String email,
  String bio,
  String cityName,
  // Gender is a Braze enum.
  Gender gender,
  Integer numberOfFriends,
  // Names of pages the user likes.
  Collection<String> likes,
  // mm/dd/yyyy format.
  String birthday
)
TwitterUser(
  Integer twitterUserId,
  String twitterHandle,
  String name,
  String description,
  Integer followerCount,
  Integer followingCount,
  Integer tweetCount,
  String profileImageUrl
)
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
FacebookUser(
  facebookId: String,
  firstName: String,
  lastName: String,
  email: String,
  bio: String,
  cityName: String,
  // Gender is a Braze enum.
  gender: Gender gender,
  numberOfFriends: Integer,
  // Names of pages the user likes.
  likes: Collection<String>,
  // mm/dd/yyyy format.
  birthday: String
)
TwitterUser(
  twitterUserId: Integer,
  twitterHandle: String,
  name: String,
  description: String,
  followerCount: Integer,
  followingCount: Integer,
  tweetCount: Integer,
  profileImageUrl: String
)
```

{% endtab %}
{% endtabs %}

Pour transférer les données extraites depuis les réseaux sociaux vers Braze, vous devrez créer un nouveau `FacebookUser` ou `TwitterUser` puis les transmettre à la méthode `BrazeUser.setFacebookData()` ou `BrazeUser.setTwitterData()`. Par exemple :

{% tabs %}
{% tab JAVA %}

```java
FacebookUser facebookUser = new FacebookUser("100000", "FirstName", "LastName", "email@email.com", "bio", "City", Gender.MALE, 3, Arrays.asList(new String[]{ "like" }), "04/13/1990");
Braze.getInstance(context).getCurrentUser().setFacebookData(facebookUser);

TwitterUser twitterUser = new TwitterUser(100000, "handle", "Name", "description", 100, 50, 150, "image_url");
Braze.getInstance(context).getCurrentUser().setTwitterData(twitterUser);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val facebookUser = FacebookUser("100000", "FirstName", "LastName", "email@email.com", "bio", "City", Gender.MALE, 3, listOf("like"),"04/13/1990")
Braze.getInstance(context).currentUser?.setFacebookData(facebookUser)

val twitterUser = TwitterUser(100000, "handle", "Name", "description", 100, 50, 150, "image_url")
Braze.getInstance(context).currentUser?.setTwitterData(twitterUser)
```

{% endtab %}
{% endtabs %}

[1]: https://developers.facebook.com/docs/howtos/androidsdk/3.0/login-with-facebook/#step1
[2]: https://developer.twitter.com/en/docs
