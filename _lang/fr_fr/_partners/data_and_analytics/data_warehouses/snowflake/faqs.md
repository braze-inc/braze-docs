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

### Pourquoi est-ce que je reçois une erreur de conformité HIPAA lors de la création d'un partage de données ?

Le compte spécifié n'est pas conforme à la norme HIPAA ou se trouve sur des [éditions de Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inférieures à Business Critical. Votre compte Snowflake doit être modifié pour passer à l'édition Business Critical afin d'être conforme à l'HIPAA pour le partage des données. Contactez le service d'assistance de Snowflake pour obtenir de l'aide sur la mise à niveau de votre compte.

### Pourquoi ne puis-je pas recréer un partage de données après en avoir supprimé un ?

Il se peut que le système soit encore en train de traiter la suppression de votre précédent partage de données. Attendez quelques minutes que le processus de déprovisionnement se termine, puis essayez à nouveau de créer le nouveau partage de données.


