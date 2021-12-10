---
nav_title: Suivi des données sociales
article_title: Suivi des données sociales pour iOS
platform: iOS
page_order: 5
description: "Cet article de référence montre comment implémenter le suivi des données sociales pour votre application iOS."
---

# Suivi des données sociales pour iOS

## Collecte des données du compte social

Le SDK iOS Braze ne collecte pas automatiquement les données utilisateur Facebook ou Twitter. Si vous voulez intégrer les données utilisateur de Facebook dans les profils d'utilisateurs de Braze, vous devez récupérer les données de l'utilisateur et les transmettre à Braze.

## Passage des données Facebook à Braze

Initialiser les objets `ABKFacebookUser` avec les données Facebook que vous avez collectées et les passer au Brésil :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKFacebookUser *facebookUser = [[ABKFacebookUser alloc] initWithFacebookUserDictionary:self.facebookUserProfile numberOfFriends:self.numberOfFacebookFriends likes:self.facebookLikes];
[Appboy sharedInstance].user.facebookUser = facebookUser;
```

{% endtab %}
{% tab SWIFT %}

```swift
let facebookUser = ABKFacebookUser(facebookUserDictionary: facebookUserDictionary, numberOfFriends: numberOfFriends, likes: likes)
Appboy.sharedInstance()?.user.facebookUser = facebookUser
```

{% endtab %}
{% endtabs %}

> Dans la méthode d'initialisation d'ABKFacebookUser `initWithFacebookUserDictionary:numberOfFriends:likes:`, tous les paramètres doivent être des dictionnaires et des tableaux retournés directement depuis Facebook:

| Paramètre                     | Définition                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| `Profil utilisateur Facebook` | Le dictionnaire a été retourné depuis le point de terminaison "/me".                          |
| `Nombre d'amis`               | La longueur du tableau des amis a été retournée depuis le point de terminaison "/me/friends". |
| `J'aime`                      | Le tableau de Facebook de l'utilisateur aime à partir du point de terminaison "/me/likes".    |
{: .reset-td-br-1 .reset-td-br-2}

> Pour plus d'informations concernant l'API graphique Facebook, veuillez vous référer à [la Documentation des Développeurs de l'API Graph Facebook][10].

De plus, vous pouvez personnaliser les données Facebook que vous envoyez à Braze, au cas où vous ne voulez pas inclure l'ensemble du profil de base. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKFacebookUser *facebookUser = [[ABKFacebookUser alloc] initWithFacebookUserDictionary:facebookUserProfile numberOfFriends:-1 likes:nil];  
```

{% endtab %}
{% tab SWIFT %}

```swift
let facebookUser = ABKFacebookUser(facebookUserDictionary: facebookUserDictionary, numberOfFriends: -1, likes:nil)
```

{% endtab %}
{% endtabs %}

Pour plus d'informations sur l'intégration du SDK Facebook, suivez les étapes dans la documentation [Facebook SDK][2].

## Passage des données Twitter à Braze

Initialisez les objets `ABKTwitterUser` , configurez les données Twitter que vous avez collectées et transmettez-les à Brasil :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKTwitterUser *twitterUser = [[ABKTwitterUser alloc] init];
twitterUser.userDescription = self.userDescription ;
twitterUser.twitterID = self.twitterID;
[Appboy sharedInstance].user.twitterUser = twitterUser;
```

{% endtab %}
{% tab SWIFT %}

```swift
let twitterUser = ABKTwitterUser()
twitterUser.userDescription = twitterDserDescription
twitterUser.twitterID = twitterID
Appboy.sharedInstance()?.user.twitterUser = twitterUser
```

{% endtab %}
{% endtabs %}

[2]: https://developers.facebook.com/docs/ios "facebook iOS sdk docs"
[10]: https://developers.facebook.com/docs/graph-api/reference/v4.0/user "facebook graph api docs"
