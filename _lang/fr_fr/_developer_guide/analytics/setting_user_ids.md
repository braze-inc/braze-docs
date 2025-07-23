---
nav_title: Définir des ID Utilisateur
article_title: Définition des ID utilisateurs via le SDK de Braze
page_order: 1.2
description: "Découvrez comment définir des ID d'utilisateur via le SDK de Braze."

---

# Définir des ID utilisateur

> Découvrez comment définir des ID d'utilisateur via le SDK de Braze. Il s'agit d'identifiants uniques qui vous permettent de suivre les utilisateurs à travers les appareils et les plateformes, d'importer leurs données via l'[API de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) et d'envoyer des messages ciblés via l'[API de messages.]({{site.baseurl}}/api/endpoints/messaging/) Si vous n'attribuez pas d'ID unique à un utilisateur, Braze lui attribuera un ID anonyme à la place. Toutefois, vous ne pourrez pas utiliser ces fonctionnalités tant que vous ne l'aurez pas fait.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## À propos des utilisateurs anonymes

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## Définition d'un ID utilisateur

Pour définir un ID utilisateur, appelez la méthode `changeUser()` après la première connexion de l'utilisateur. Les ID doivent être uniques et respecter nos [meilleures pratiques en matière de dénomination](#naming-best-practices).

Si vous hachurez plutôt un identifiant unique, veillez à normaliser l'entrée de votre fonction de hachage. Par exemple, lors du hachage d'une adresse e-mail, supprimez les espaces de début et de fin et tenez compte de la localisation.

{% tabs local %}
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

{% tab WEB %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Si vous souhaitez utiliser Google Tag Manager à la place, vous pouvez utiliser le type d'étiquette **Change User** pour appeler la [méthode`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Utilisez-le chaque fois qu'un utilisateur se connecte ou est identifié d'une autre manière avec son identifiant unique `external_id`.

Veillez à saisir l'ID unique de l'utilisateur actuel dans le champ **ID externe**, généralement rempli à l'aide d'une variable de couche de données envoyée par votre site web.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette" et l'"ID externe".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
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

{% tab ENGINE UNREAL %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**N'attribuez pas d'ID statique par défaut ou d'appel `changeUser()` lorsqu'un utilisateur se déconnecte.** En procédant ainsi, vous ne pourrez pas réengager les utilisateurs précédemment connectés sur les appareils partagés. Au lieu de cela, gardez une trace de tous les ID d'utilisateurs séparément et assurez-vous que le processus de déconnexion de votre application permet de revenir à un utilisateur précédemment connecté. Lorsqu'une nouvelle session commence, Braze actualise automatiquement les données pour le profil nouvellement actif.
{% endalert %}

## Alias utilisateurs

### Comment ils fonctionnent

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Définition d'un alias d'utilisateur

Un alias d'utilisateur se compose de deux parties : un nom et un libellé. Le nom fait référence à l'identifiant lui-même, tandis que l'étiquette fait référence au type d'identifiant auquel il appartient. Par exemple, si vous avez un utilisateur dans une plateforme de support client tierce avec l'ID externe `987654`, vous pouvez lui attribuer un alias dans Braze avec le nom `987654` et le libellé d'alias `support_id`, afin de pouvoir le suivre à travers les plateformes.

{% tabs local %}
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

{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab API REST %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## Meilleures pratiques en matière d'ID Naming {#naming-best-practices}

Nous vous recommandons de créer des ID d'utilisateur en utilisant la norme [UUID (Universally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) ), ce qui signifie qu'il s'agit de chaînes de caractères de 128 bits qui sont aléatoires et bien réparties.

Vous pouvez également hacher un identifiant unique existant (tel qu'un nom ou une adresse e-mail) pour générer vos ID d'utilisateur. Si vous le faites, veillez à mettre en œuvre l'[authentification SDK]({{site.baseurl}}/developer_guide/authentication/), afin d'empêcher l'usurpation d'identité de l'utilisateur.

Bien qu'il soit essentiel de nommer correctement vos ID d'utilisateur dès le départ, vous pouvez toujours les renommer à l'avenir en utilisant le point de terminaison [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) endpoint.

| Recommandé | Non recommandé |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | NomSociété-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Évitez de partager des détails sur la façon dont vous créez les ID utilisateurs, car cela pourrait exposer votre organisation à des attaques malveillantes ou à la suppression de données.
{% endalert %}
