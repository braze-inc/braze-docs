---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Définition des identifiants d'utilisateur pour le Web
platform: Web
page_order: 1
page_type: Référence
description: "Cet article décrit comment définir les identifiants d'utilisateur pour chacun de vos utilisateurs, y compris les meilleures pratiques et les points importants à prendre en considération avant d'apporter des modifications."
---

# Définition des identifiants d'utilisateur pour le web

{% include archive/setting_user_ids/setting_user_ids.md %}

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) pour définir l'identifiant de l'utilisateur :

```javascript
appboy.changeUser(VOTRE_USER_ID_STRING);
```

> __N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte.__ Le paramétrage de `changeUser()` à une valeur par défaut statique associera TOUTES les activités de l'utilisateur à cet utilisateur par défaut jusqu'à ce que l'utilisateur se connecte à nouveau. De plus, nous vous recommandons de ne pas modifier l'ID de l'utilisateur lors de la déconnexion, car cela vous rend incapable de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous prévoyez plusieurs utilisateurs sur le même appareil, mais que vous voulez seulement cibler l'un d'eux lorsque votre application est dans un état déconnecté, Nous vous recommandons de garder séparément la trace de l'identifiant de l'utilisateur que vous voulez cibler pendant la déconnexion et de revenir à cet identifiant utilisateur dans le cadre du processus de déconnexion de votre application.

Reportez-vous à la documentation [changeUser][4] pour plus d'informations.

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et notes d'intégration des identifiants utilisateur

{% include archive/setting_user_ids/best_practices.md %}

## Aliasing des utilisateurs

{% include archive/setting_user_ids/aliasing.md platform="Web" %}

[4]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.changeUser "Javadocs"
