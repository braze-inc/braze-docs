---
nav_title: Définir des ID Utilisateur
article_title: Définir des ID utilisateur pour Roku
platform: Roku
page_order: 0
page_type: reference
description: "Cet article de référence couvre les méthodes d’identification et de configuration des ID utilisateurs pour Roku, ainsi que les meilleures pratiques et les considérations importantes."
 
---

# Définir des ID utilisateur

> Cet article de référence couvre les méthodes d’identification et de configuration des ID utilisateurs pour Roku, ainsi que les meilleures pratiques et les considérations importantes.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Vous devez effectuer l’appel suivant dès que l’utilisateur est identifié (généralement après s’être connecté) afin de définir l’ID utilisateur :

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Convention de dénomination des ID utilisateurs suggérée

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et remarques sur l’intégration de l’ID utilisateur

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

