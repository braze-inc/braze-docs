---
nav_title: Suivre des données sociales
article_title: Suivre des données sociales pour Windows Universal
platform: Windows Universal
page_order: 5
description: "Cet article de référence explique comment gérer le suivi des données sociales sur la plateforme Windows Universal."

---

# Suivre des données sociales
{% include archive/windows_deprecation.md %}

Contrairement au SDK Braze pour iOS, le SDK Braze pour Windows ne recueille pas automatiquement les données Facebook et Twitter. Il est cependant possible d’ajouter des données de réseaux sociaux à un profil utilisateur Braze depuis le SDK Windows :

- Obtenir des données sur les réseaux sociaux dans votre application via le [SDK Facebook][1] et les [API Twitter][2].
- Initialiser les objets utilisateurs Facebook et Twitter avec les données des réseaux sociaux et les transmettre à Braze.

## Constructeurs de données de réseau social

```
FacebookUser(
  string Id,
  string FirstName,
  string LastName,
  string Email,
  // mm/dd/yyyy format.
  string Birthday,
  string Bio,
  FacebookLocation LocationObject,
  // "m" or "f".
  string Gender,
  List<FacebookLike> Likes,
  int NumFriends
)

FacebookLocation(
  string CityName
)

FacebookLike(
  // The name of a page the user likes.
  string Like
)

TwitterUser(
  string Description,
  int FollowersCount,
  int FriendsCount,
  int StatusesCount,
  // Twitter's unique id for the user.
  int Id,
  string Name,
  string ProfileImageURL,
  // The user's handle.
  string ScreenName
)
```

Pour transférer les données extraites depuis les réseaux sociaux vers Braze, vous devrez créer un nouveau FacebookUser ou TwitterUser puis les transmettre à la méthode `Appboy.SharedInstance.AppboyUser.SetFacebookData()` ou `Appboy.SharedInstance.AppboyUser.SetTwitterData()`. Par exemple :

### Twitter

```
var twitterUser = new TwitterUser {
  Description = "description",
  FollowersCount = 10,
  FriendsCount = 20,
  StatusesCount = 150,
  Id = 1000000,
  Name = "Name",
  ProfileImageURL = "https://si0.twimg.com/profile_images/00000/00000.jpeg",
  ScreenName = "handle"
};

Appboy.SharedInstance.AppboyUser.SetTwitterData(twitterUser);
```

### Facebook

```
// Build a list of pages the user likes.
List likes = new List();
var like = new FacebookLike {
  Like = "Page Name"
};
likes.Add(like);

// Specify the user's city in a FacebookLocation object.
var location = new FacebookLocation {
  CityName = "City"
};

// Populate the FacebookUser object.
var facebookUser = new FacebookUser {
  Id = "100000",
  FirstName = "FirstName",
  LastName = "LastName",
  Email = "email@email.com",
  Birthday = "04/13/1990",
  Bio = "bio",
  LocationObject = location,
  Gender = "m",
  Likes = likes,
  NumFriends = 500
};

Appboy.SharedInstance.AppboyUser.SetFacebookData(facebookUser);
```

[1]: https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/ "facebook"
[2]: https://developer.twitter.com/en/docs "twitter"
