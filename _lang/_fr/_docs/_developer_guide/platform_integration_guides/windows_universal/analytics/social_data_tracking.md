---
nav_title: Suivi des données sociales
article_title: Suivi des données sociales pour Windows Universal
platform: Univers Windows
page_order: 5
description: "Cet article de référence traite du suivi des données sociales sur la plateforme Windows Universelle."
---

# Suivi des données sociales

Contrairement au Braze iOS SDK, le Braze Windows SDK ne collecte pas automatiquement les données Facebook et Twitter. Cependant, il est possible d'ajouter des données de réseau social au profil d'un utilisateur Braze du SDK Windows aussi:

- Obtenez des données sur les réseaux sociaux dans votre application via le SDK Facebook et les API Twitter.
    - [Documentation Facebook][1] // [Documentation Twitter][2]
- Initialiser les objets d'utilisateur Facebook et Twitter avec les données des réseaux sociaux et les transmettre au Brésil.

## Constructeurs de données du réseau social

```
FacebookUser(
  string Id,
  string FirstName,
  string LastName,
  string Email,
  // mm/dd/yyyy format.
  chaîne Birthday,
  string Bio,
  FacebookLocation LocationObject,
  // "m" ou "f".
  chaîne de genre,
  Liste<FacebookLike> J'aime,
  int NumFriends
)

FacebookLocation(
  string CityName
)

FacebookLike(
  // Le nom d'une page que l'utilisateur aime.
  string Like
)

TwitterUser(
  string Description,
  int FollowersCount,
  int FriendsCount,
  int StatusesCount,
  // Identifiant unique de Twitter pour l'utilisateur.
  int Id,
  string Name,
  string ProfileImageURL,
  // Le gestionnaire de l'utilisateur.
  string Nom d'écran
)
```

Pour passer des données récupérées à partir des réseaux sociaux au Brésil, vous allez créer un nouvel utilisateur FacebookUser ou TwitterUser et ensuite les passer à la méthode Appboy.SharedInstance.AppboyUser.SetFacebookData()/Appboy.SharedInstance.AppboyUser.SetTwitterData(). Par exemple :

### Twitter

```
var twitterUser = new TwitterUser {
  Description = "description",
  FollowersCount = 10,
  FriendsCount = 20,
  StatusesCount = 150,
  Id = 1000000,
  Nom = "Nom",
  ProfileImageURL = "https://si0. wimg.com/profile_images/00000/00000.jpeg",
  Nom d'écran = "handle"
};

Appboy.SharedInstance.AppboyUser.SetTwitterData(twitterUser);
```

### Facebook

```
// Construit une liste de pages que l'utilisateur aime.
Liste likes = new List();
var like = new FacebookLike {
  Like = "Nom de la page"
};
likes. dd(like);

// Spécifie la ville de l'utilisateur dans un objet FacebookLock.
var location = new FacebookLocation {
  CityName = "Ville"
};

// Remplir l'objet FacebookUser .
var facebookUser = new FacebookUser {
  Id = "100000",
  FirstName = "Prénom",
  Nom de famille = "Nom",
  E-mail = "email@email. om",
  Anniversaire = "04/13/1990",
  Bio = "bio",
  LocationObject = localisation,
  Sexe = "m",
  J'aime = aime,
  NumFriends = 500
};

Appboy. 
 haredInstance.AppboyUser.SetFacebookData(facebookUser);
```

[1]: https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/ "facebook"
[2]: https://developer.twitter.com/en/docs "twitter"
