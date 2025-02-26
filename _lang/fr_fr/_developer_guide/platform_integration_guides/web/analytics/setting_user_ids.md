---
nav_title: Définir des ID Utilisateur
article_title: Définir des ID utilisateur pour le Web
platform: Web
page_order: 1
page_type: reference
description: "Cet article décrit comment définir des ID utilisateur pour chacun de vos utilisateurs, y compris les meilleures pratiques et les points importants à prendre en compte avant de procéder à des modifications."
 
---

# Définir des ID utilisateur

> Cet article décrit comment définir des ID utilisateur pour chacun de vos utilisateurs, y compris les meilleures pratiques et les points importants à prendre en compte avant de procéder à des modifications.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après la connexion) pour définir l’ID utilisateur :

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte.** Définir `changeUser()` sur une valeur par défaut statique associera TOUTES les activités de l’utilisateur avec cet « utilisateur » par défaut jusqu’à ce qu’il se connecte à nouveau.
{% endalert %}

Nous vous déconseillons de modifier l'ID de l'utilisateur lorsqu'il se déconnecte, car cela vous empêche de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l’un d’eux lorsque votre application est à l’état déconnecté, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application.

Consultez la [documentation`changeUser()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "Javadocs") pour plus d'informations.

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Alias d’utilisateurs

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Web" %}

