---
nav_title: Suivi des données de réseaux sociaux
article_title: Suivi des données de réseaux sociaux pour iOS
platform: iOS
page_order: 5
description: "Cet article de référence montre comment implémenter le suivi des données de réseaux sociaux pour votre application iOS."

---

# Suivi des données de réseaux sociaux pour iOS

## Collecte des données de compte de réseaux sociaux

Le SDK Braze pour iOS ne recueille pas automatiquement les données utilisateur de Facebook ou Twitter. Si vous souhaitez intégrer les données utilisateur de Facebook dans les profils utilisateur Braze, vous devez récupérer les données de l’utilisateur et les transmettre à Braze.

## Transmettre les données Facebook à Braze

Initialisez les objets `ABKFacebookUser` avec les données Facebook que vous avez collectées et transmettez-les à Braze :

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

Dans la méthode d’initialisation ABKFacebookUser `initWithFacebookUserDictionary:numberOfFriends:likes:`, tous les paramètres doivent être des dictionnaires et des tableaux renvoyés directement depuis Facebook :

| Paramètre | Définition |
| --------- | ---------- |
|`facebookUserProfile`| Le dictionnaire a été renvoyé à partir de l’endpoint « /me ».|
| `numberOfFriends`| La longueur du tableau d’amis renvoyé à partir de l’endpoint « /me/friends ».|
| `likes` | Le tableau des likes Facebook de l’utilisateur à partir de l’endpoint « /me/likes ». |
{: .reset-td-br-1 .reset-td-br-2}

Reportez-vous à [l’API Facebook Graph][10] pour plus d’informations.

De plus, vous pouvez personnaliser les données Facebook que vous envoyez à Braze si vous ne souhaitez pas inclure l’intégralité du profil de base. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKFacebookUser *facebookUser = [[ABKFacebookUser alloc] initWithFacebookUserDictionary:facebookUserPublicProfile numberOfFriends:-1 likes:nil];  
```

{% endtab %}
{% tab SWIFT %}

```swift
let facebookUser = ABKFacebookUser(facebookUserDictionary: facebookUserDictionary, numberOfFriends: -1, likes:nil)
```

{% endtab %}
{% endtabs %}

Reportez-vous au [SDK Facebook][2] pour plus d’informations.

## Transmettre les données Twitter à Braze

Initialisez les objets `ABKTwitterUser` configurez les données Twitter que vous avez collectées et transmettez-les à Braze :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKTwitterUser *twitterUser = [[ABKTwitterUser alloc] init];
twitterUser.userDescription = self.userDescription;
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
