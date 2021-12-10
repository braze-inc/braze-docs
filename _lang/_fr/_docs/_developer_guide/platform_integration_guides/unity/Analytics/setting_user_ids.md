---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Définition des identifiants d'utilisateur pour l'unité
platform:
  - Unité
  - iOS
  - Android
page_order: 0
description: "Cet article de référence couvre la façon de définir les identifiants des utilisateurs sur la plate-forme Unity."
---

# Paramétrage des identifiants d'utilisateur

{% include archive/setting_user_ids/setting_user_ids.md %}

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) afin de définir l'identifiant de l'utilisateur :

```csharp
AppboyBinding.ChangeUser("VOTRE_USER_ID_STRING");
```

> __Ne pas appeler `ChangeUser()` lorsqu'un utilisateur se déconnecte. `ChangeUser()` ne doit être appelé que lorsque l'utilisateur se connecte dans l'application.__ Réglage `ChangeUser()` à une valeur par défaut statique associera TOUTES les activités de l'utilisateur à cet utilisateur par défaut "utilisateur" jusqu'à ce que l'utilisateur se connecte à nouveau.

De plus, nous vous recommandons de ne pas modifier l'ID de l'utilisateur lors de la déconnexion, car cela vous rend incapable de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais ne souhaite cibler l'un d'eux que lorsque votre application est en état de déconnexion, Nous vous recommandons de garder séparément la trace de l'identifiant de l'utilisateur que vous voulez cibler pendant la déconnexion et de revenir à cet identifiant utilisateur dans le cadre du processus de déconnexion de votre application.

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

## Meilleures bractices et notes d'intégration d'ID utilisateur

{% include archive/setting_user_ids/best_practices.md %}
