---
nav_title: FAQ
article_title: FAQ sur le partage des données de Snowflake
page_order: 50
page_type: FAQ
description: "Cet article répond aux questions fréquemment posées sur le partage des données de Snowflake."

---

# Questions fréquemment posées

### Est-il possible d'obscurcir les données personnelles identifiables via le partage de données Snowflake ?
Non, pour l'instant, ce n'est pas possible.

### Ai-je besoin d'un partage de données pour la même région ou pour plusieurs régions ?
Utilisez le partage des données pour la même région dans les scénarios suivants :
- Votre compte Snowflake se trouve dans la région US-EAST-1 (AWS) et la région de votre tableau de bord Braze se trouve aux États-Unis.
- Votre région Snowflake se trouve dans l'UE-CENTRAL-1 et la région du tableau de bord de Braze se trouve dans l'UE.

Dans le cas contraire, utilisez le partage des données pour les régions transversales. 

### Que dois-je faire de mes données partagées lorsque je passe à un nouveau compte Snowflake ?
Vous pouvez supprimer l'ancien partage de données associé à votre ancien compte Snowflake, puis créer un nouveau partage pour le nouveau compte. Toutes les données historiques seront disponibles dans le nouveau partage. 

### Pourquoi ne vois-je pas de données dans mon partage de données ?
Vous avez peut-être utilisé le mauvais ID de compte Snowflake lors de la création de votre partage de données. L'ID du compte sur le tableau de bord de partage des données doit correspondre à la sortie de `CURRENT_ACCOUNT()` de votre compte Snowflake.

Si votre action s’étend sur plusieurs régions, il est possible que les données ne soient pas immédiatement disponibles. Selon votre volume de données, la synchronisation des données avec votre région peut prendre quelques heures.


