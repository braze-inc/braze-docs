---
nav_title: Définir des ID Utilisateur
article_title: Définir des ID utilisateur pour Windows Universal
platform: Windows Universal
page_order: 1
description: "Cet article de référence explique comment définir les ID utilisateur sur la plateforme Windows Universal."
hidden: true
---

# Définir des ID utilisateur
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après la connexion) pour définir l’ID utilisateur :

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**N’appelez pas `changeUser()` lorsqu’un utilisateur se déconnecte. `changeUser()` ne doit être appelé que lorsque l’utilisateur se connecte à l’application.** Définir `changeUser()` sur une valeur par défaut statique associera TOUTES les activités de l’utilisateur avec cet « utilisateur » par défaut jusqu’à ce qu’il se connecte à nouveau.
{% endalert %}

En outre, nous vous déconseillons de modifier l'ID de l'utilisateur lorsqu'il se déconnecte, car cela vous empêche de cibler l'utilisateur précédemment connecté avec des campagnes de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l’un d’eux lorsque votre application est à l’état déconnecté, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application.

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/developer_guide/rest_api/messaging/
[6]: http://developer.android.com/reference/java/util/Locale.html#default_locale "Documentation pour les développeurs Android - Localisation"
