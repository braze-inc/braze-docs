---
nav_title: Définir des ID Utilisateur
article_title: Définir des ID Utilisateur pour iOS
platform: iOS
page_order: 1
description: "Cet article explique comment définir des ID utilisateur dans votre application iOS, propose des conventions de dénomination d’ID utilisateur et quelques bonnes pratiques."
 
---

{% multi_lang_include deprecations/objective-c.md %}

# Définir des ID Utilisateur pour iOS

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Attribuer un ID utilisateur

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après la connexion) pour définir l’ID utilisateur :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("YOUR_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**N’appelez pas `changeUser()` lorsqu’un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l’utilisateur se connecte à l’application.** Définir [`changeUser()`][5] sur une valeur par défaut statique associera TOUTES les activités de l’utilisateur avec cet « utilisateur » par défaut jusqu’à ce qu’il se connecte à nouveau.
{% endalert %}

N’oubliez pas d’employer cette méthode dans le fil principal de votre application. L’utilisation asynchrone de la méthode peut entraîner un comportement non défini.

Nous recommandons également de ne pas modifier l’ID utilisateur lorsqu’un utilisateur se déconnecte, car cela vous empêcherait de cibler l’utilisateur précédemment connecté avec des campagnes de réengagement. Si vous envisagez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez n’en cibler qu’un seul lorsque votre application est déconnectée, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler lorsqu’il est déconnecté et de revenir à cet utilisateur. ID dans le cadre du processus de déconnexion de votre application.

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias d’utilisateurs

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="iOS" %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69 "changeuser"
