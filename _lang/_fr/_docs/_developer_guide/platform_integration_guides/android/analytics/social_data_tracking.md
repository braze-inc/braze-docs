---
nav_title: Suivi des données sociales
article_title: Suivi des données sociales pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 5
description: "Cet article de référence montre comment implémenter le suivi des données sociales pour votre application Android."
---

# Suivi des données sociales pour Android/FireOS

Similaire à Braze iOS SDK, le Braze Android SDK ne collecte pas automatiquement les données Facebook et Twitter. Cependant, il est possible d'ajouter des données de réseau social au profil d'un utilisateur Braze depuis le SDK Android aussi:

- Obtenez des données sur les réseaux sociaux dans votre application via le SDK Facebook et les API Twitter.
  - [Documentation Facebook][1]
  - [Documentation Twitter][2]
- Initialiser les objets d'utilisateur Facebook et Twitter avec les données des réseaux sociaux et les transmettre au Brésil.

## Constructeurs de données du réseau social

{% tabs %}
{% tab JAVA %}

```java
FacebookUser(
  String facebookId,
  String firstName,
  String lastName,
  Email de chaîne,
  bio de chaînes,
  cityName,
  // Gender est un enum de Braze.
  Sexe genre,
  Integer numberOfFriends,
  // Noms des pages que l'utilisateur aime.
  Collection<String> J'aime,
  // format mm/jj/aaaa.
  Anniversaire de la chaîne
)
TwitterUser(
  Integer twitterUserId,
  String twitterHandle,
  String name,
  String description,
  Nombre d'entiers suiveurs,
  Nombre entier suivant,
  Nombre entier tweetCount,
  ProfileImageUrl chaîne de caractères
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
  // Le genre est un enum de Braze.
  gender: gender,
  numberOfFriends: Integer,
  // Noms des pages que l'utilisateur aime.
  likes: Collection<String>,
  // format mm/jj/aaaa.
  anniversaire: String
)
TwitterUser(
  twitterUserId: Integer,
  twitterHandle: String,
  name : String,
  description : String,
  followerCount: Integer,
  followingCount: Integer,
  tweetCount: Integer,
  profileImageUrl : String
)
```

{% endtab %}
{% endtabs %}

Pour transmettre les données récupérées des réseaux sociaux à Braze, vous allez créer un nouvel utilisateur Facebook ou TwitterUser et ensuite les passer à la méthode `BrazeUser. etFacebookData()`/`BrazeUser.setTwitterData()`. Par exemple :

{% tabs %}
{% tab JAVA %}

```java
FacebookUser facebookUser = new FacebookUser("100000", "Prénom", "Nom", "email@email.com", "bio", "City", Gender.MALE, 3, Arrays.asList(new String[]{ "like" }), "04/13/1990");
Braze.getInstance(context).getCurrentUser(). etFacebookData(facebookUser);

TwitterUser twitterUser = new TwitterUser(100000, "handle", "Name", "description", 100, 50, 150, "image_url");
Braze.getInstance(context).getCurrentUser().setTwitterData(twitterUser);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val facebookUser = FacebookUser("100000", "Prénom", "Nom", "email@email.com", "bio", "Ville", Gender.MALE, 3, listOf("like"),"04/13/1990")
Braze.getInstance(context).currentUser?. etFacebookData(facebookUser)

val twitterUser = TwitterUser(100000, "handle", "Name", "description", 100, 50, 150, "image_url")
Braze.getInstance(context).currentUser?.setTwitterData(twitterUser)
```

{% endtab %}
{% endtabs %}

[1]: https://developers.facebook.com/docs/howtos/androidsdk/3.0/login-with-facebook/#step1
[2]: https://developer.twitter.com/en/docs
