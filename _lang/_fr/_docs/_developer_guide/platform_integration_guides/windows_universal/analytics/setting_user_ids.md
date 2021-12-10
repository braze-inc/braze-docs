---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Définition des identifiants utilisateur pour Windows Universal
platform: Univers Windows
page_order: 1
description: "Cet article de référence traite de la façon de définir les identifiants des utilisateurs sur la plate-forme Windows Universelle."
---

# Paramétrage des identifiants d'utilisateur

{% include archive/setting_user_ids/setting_user_ids.md %}

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) pour définir l'ID de l'utilisateur :

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

> __N'appelez pas `changeUser()` lorsqu'un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l'utilisateur se connecte dans l'application.__ Le paramétrage de `changeUser()` à une valeur par défaut statique associera TOUTES les activités de l'utilisateur à cet utilisateur par défaut "utilisateur" jusqu'à ce que l'utilisateur se reconnecte. De plus, nous vous recommandons de ne pas modifier l'ID de l'utilisateur lors de la déconnexion, car cela vous rend incapable de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous prévoyez plusieurs utilisateurs sur le même appareil, mais que vous voulez seulement cibler l'un d'eux lorsque votre application est dans un état déconnecté, Nous vous recommandons de garder séparément la trace de l'identifiant de l'utilisateur que vous voulez cibler pendant la déconnexion et de revenir à cet identifiant utilisateur dans le cadre du processus de déconnexion de votre application.

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et notes d'intégration des identifiants utilisateur

{% include archive/setting_user_ids/best_practices.md %}
