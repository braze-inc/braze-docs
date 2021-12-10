---
nav_title: Paramétrage des identifiants d'utilisateur
article_title: Paramétrage des identifiants d'utilisateur pour Roku
platform: Roku
page_order: 0
page_type: Référence
description: "Cette page couvre les méthodes pour identifier les utilisateurs, ainsi que les meilleures pratiques et les considérations importantes."
---

# Paramétrage des identifiants d'utilisateur

{% include archive/setting_user_ids/setting_user_ids.md %}

Vous devriez faire l'appel suivant dès que l'utilisateur est identifié (généralement après la connexion) afin de définir l'ID de l'utilisateur :

```
m.Braze.setUserId(VOTRE_USER_ID_STRING)
```

## Convention de nommage des identifiants d'utilisateur suggérée

{% include archive/setting_user_ids/naming_convention.md %}

## Meilleures pratiques et notes d'intégration des identifiants utilisateur

{% include archive/setting_user_ids/best_practices.md %}
