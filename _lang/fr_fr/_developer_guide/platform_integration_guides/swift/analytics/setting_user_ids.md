---
nav_title: Définir des ID Utilisateur
article_title: Définir des ID Utilisateur pour iOS
platform: Swift
page_order: 1
description: "Cet article explique comment définir des ID utilisateur dans votre application iOS, propose des conventions de dénomination d’ID utilisateur et quelques bonnes pratiques."
 
---

# Définir des ID utilisateur

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Attribuer un ID utilisateur

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après la connexion) pour définir l’ID utilisateur :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**N’appelez pas `changeUser()` lorsqu’un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l’utilisateur se connecte à l’application.** Définir [`changeUser()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29) sur une valeur par défaut statique associera TOUTES les activités de l'utilisateur avec cet « utilisateur » par défaut jusqu'à ce qu’il se connecte à nouveau.
{% endalert %}

De plus, nous vous recommandons de ne pas changer l'ID utilisateur lorsqu'un utilisateur se déconnecte, car cela vous empêche de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous envisagez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez n’en cibler qu’un seul lorsque votre application est déconnectée, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler lorsqu’il est déconnecté et de revenir à cet utilisateur. ID dans le cadre du processus de déconnexion de votre application.

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias d’utilisateurs

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Swift" %}

