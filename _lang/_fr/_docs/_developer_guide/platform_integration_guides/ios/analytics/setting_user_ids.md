---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Paramétrage des identifiants utilisateur pour iOS
platform: iOS
page_order: 1
description: "Cet article montre comment définir les identifiants d'utilisateur dans votre application iOS, les conventions de nommage des identifiants d'utilisateur suggérés, et les meilleures pratiques."
---

# Définition des identifiants d'utilisateur pour iOS

{% include archive/setting_user_ids/setting_user_ids.md %}

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

## Assigner un ID utilisateur

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) afin de définir l'identifiant de l'utilisateur :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] changeUser:@"VOTRE_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("VOTRE_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
Assurez-vous d'appeler cette méthode dans le fil de discussion principal de votre application. Appeler la méthode de manière asynchrone peut conduire à un comportement indéfini.
{% endalert %}

> __N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l'utilisateur se connecte dans l'application.__ Le paramétrage de `changeUser()` à une valeur par défaut statique associera TOUTES les activités de l'utilisateur à cet utilisateur par défaut "utilisateur" jusqu'à ce que l'utilisateur se reconnecte. De plus, nous vous recommandons de ne pas modifier l'ID de l'utilisateur lors de la déconnexion, car cela vous rend incapable de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous prévoyez plusieurs utilisateurs sur le même appareil, mais que vous voulez seulement cibler l'un d'eux lorsque votre application est dans un état déconnecté, Nous vous recommandons de garder séparément la trace de l'identifiant de l'utilisateur que vous voulez cibler pendant la déconnexion et de revenir à cet identifiant utilisateur dans le cadre du processus de déconnexion de votre application.

**Informations supplémentaires**

- Voir la déclaration de méthode dans le fichier [`Appboy.h`][4]. - De plus, vous pouvez vous référer à la documentation de la classe [`changeUser`][5] pour plus d'informations.

## Meilleures pratiques et notes d'intégration des identifiants utilisateur

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing des utilisateurs

{% include archive/setting_user_ids/aliasing.md platform="iOS" %}

[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69 "changeuser"
