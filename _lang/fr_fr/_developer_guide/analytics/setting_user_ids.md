---
nav_title: "Définir les ID d'utilisateur"
article_title: Définir les ID d'utilisateur via le SDK Braze
page_order: 1.1
description: "Découvrez comment définir des ID d'utilisateur via le SDK de Braze."

---

# Définir les ID d'utilisateur

> Découvrez comment définir des ID d'utilisateur via le SDK de Braze. Il s'agit d'identifiants uniques qui vous permettent de suivre les utilisateurs sur différents appareils et plateformes, d'importer leurs données via l'[API de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) et d'envoyer des messages ciblés via l'[API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/). Si vous n'attribuez pas d'ID unique à un utilisateur, Braze lui attribue un ID anonyme à la place. Toutefois, vous ne pourrez pas utiliser ces fonctionnalités tant que vous ne l'aurez pas fait.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## À propos des utilisateurs anonymes

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Empêcher le suivi des utilisateurs anonymes

Si votre cas d'utilisation exige qu'aucune donnée ne soit collectée avant l'identification d'un utilisateur, vous pouvez retarder l'initialisation du SDK Braze jusqu'à ce que l'utilisateur se connecte et qu'un `external_id` soit disponible. Définissez un indicateur dans votre code qui passe à `true` lorsque l'utilisateur se connecte, et n'initialisez le SDK que lorsque cet indicateur est activé.

{% alert warning %}
Ne retardez l'initialisation que **la première fois** qu'un utilisateur télécharge votre application (avant qu'un `external_id` ne soit défini). Si vous empêchez le SDK de s'initialiser chaque fois qu'un utilisateur se déconnecte ou démarre une nouvelle session, cela interférera avec le préchargement des ressources de messages in-app et de cartes de contenu, ce qui peut entraîner des erreurs de livrabilité pour ces campagnes.
{% endalert %}

## Définition d'un ID utilisateur

Pour définir un ID utilisateur, appelez la méthode `changeUser()` après la première connexion de l'utilisateur. Les ID doivent être uniques et respecter nos [bonnes pratiques de dénomination](#naming-best-practices).

Si vous hachez un identifiant unique, veillez à normaliser l'entrée de votre fonction de hachage. Par exemple, lors du hachage d'une adresse e-mail, supprimez les espaces en début et en fin de chaîne et tenez compte de la localisation.

{% tabs local %}
{% tab WEB %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Si vous préférez utiliser Google Tag Manager, vous pouvez utiliser le type d'étiquette **Change User** pour appeler la [méthode `changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Utilisez-le chaque fois qu'un utilisateur se connecte ou est identifié d'une autre manière avec son identifiant unique `external_id`.

Veillez à saisir l'ID unique de l'utilisateur actuel dans le champ **External User ID**, généralement rempli à l'aide d'une variable de couche de données envoyée par votre site web.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d'action Braze. Les paramètres inclus sont « tag type » et « external user ID ».]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### Fonctionnement de `changeUser()`

Lorsque vous appelez `changeUser()`, les comportements suivants s'appliquent :

- Appeler `changeUser()` avec le **même** ID utilisateur que celui déjà défini n'a aucun effet sur le compteur de sessions.
- Appeler `changeUser()` avec un ID utilisateur **différent** met automatiquement fin à la session en cours et en démarre une nouvelle.
- Lorsqu'un utilisateur anonyme appelle `changeUser()` avec un **nouvel** ID utilisateur (qui n'existe pas encore dans Braze), les données du profil anonyme sont fusionnées dans le nouveau profil identifié.
- Lorsqu'un utilisateur anonyme appelle `changeUser()` avec un ID utilisateur **existant**, les données du profil anonyme ne sont pas fusionnées dans le profil identifié.

{% alert note %}
L'appel de `changeUser()` déclenche un vidage des données dans le cadre de la fermeture de la session de l'utilisateur en cours. Le SDK envoie automatiquement toutes les données en attente de l'utilisateur précédent avant de basculer vers le nouvel utilisateur. Il n'est donc pas nécessaire de demander manuellement un vidage des données avant d'appeler `changeUser()`.
{% endalert %}

{% alert warning %}
N'attribuez pas un ID utilisateur unique et partagé (par exemple, un ID externe par défaut statique) et n'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte. Cela vous empêcherait de réengager les utilisateurs précédemment connectés sur les appareils partagés, et toutes les données seraient enregistrées sous un seul ID utilisateur, ce qui peut entraîner un comportement inattendu d'autres fonctionnalités. Conservez plutôt une trace de tous les ID utilisateur séparément et assurez-vous que le processus de déconnexion de votre application permet de revenir à un utilisateur précédemment connecté. Lorsqu'une nouvelle session commence, Braze actualise automatiquement les données du profil nouvellement actif.
{% endalert %}

## Alias d'utilisateur

### Fonctionnement

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Définition d'un alias d'utilisateur

Un alias d'utilisateur se compose de deux parties : un nom et un libellé. Le nom correspond à l'identifiant lui-même, tandis que le libellé désigne le type d'identifiant auquel il appartient. Par exemple, si vous avez un utilisateur dans une plateforme d'assistance client tierce avec l'ID externe `987654`, vous pouvez lui attribuer un alias dans Braze avec le nom `987654` et le libellé `support_id`, afin de pouvoir le suivre sur l'ensemble des plateformes.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Bonnes pratiques de dénomination des ID {#naming-best-practices}

Nous vous recommandons de créer des ID utilisateur en utilisant la norme [UUID (Universally Unique Identifier)](https://en.wikipedia.org/wiki/Universally_unique_identifier), c'est-à-dire des chaînes de caractères de 128 bits, aléatoires et bien réparties.

Vous pouvez également hacher un identifiant unique existant (tel qu'un nom ou une adresse e-mail) pour générer vos ID utilisateur. Dans ce cas, veillez à mettre en œuvre l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) afin d'empêcher l'usurpation d'identité.

{% alert warning %}
N'utilisez pas une valeur facile à deviner ou un numéro incrémentiel pour votre ID utilisateur. Cela pourrait exposer votre organisation à des attaques malveillantes ou à l'exfiltration de données.

Pour une sécurité accrue, utilisez l'[authentification SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/).
{% endalert %}

Bien qu'il soit essentiel de nommer correctement vos ID utilisateur dès le départ, vous pouvez toujours les renommer ultérieurement via l'endpoint [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Types d'ID déconseillés | Exemple déconseillé |
| ------------ | ----------- |
| ID de profil visible ou nom d'utilisateur | JonDoe829525552 |
| Adresse e-mail | Anna@email.com |
| ID utilisateur à incrémentation automatique | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Évitez de divulguer des informations sur la manière dont vous créez les ID utilisateur, car cela pourrait exposer votre organisation à des attaques malveillantes ou à l'exfiltration de données.
{% endalert %}