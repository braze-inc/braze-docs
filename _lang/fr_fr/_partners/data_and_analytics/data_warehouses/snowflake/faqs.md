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
- Votre région Snowflake se trouve en AP-Southeast-2 (AWS) et votre région tableau de bord Braze se trouve en Australie.
- Votre région Snowflake se trouve en AP-Southeast-3 (AWS) et votre région tableau de bord de Braze se trouve en Indonésie.

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

### Combien de fois dois-je exécuter `CREATE DATABASE` lorsque plusieurs espaces de travail partagent des données avec le même compte Snowflake ?

Vous ne devez exécuter `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` qu'une seule fois. Lorsque plusieurs partages de données provenant de différents espaces de travail Braze sont partagés sur le même compte Snowflake, ils sont automatiquement combinés en un seul et même partage. Une fois que vous avez créé la base de données initiale, les données des espaces de travail supplémentaires sont automatiquement ajoutées à la base de données existante sans nécessiter de demandes de partage supplémentaires ou d'étapes de création de base de données.

Par exemple, si vous créez un partage de données vers le compte 123 de Snowflake à partir de l'espace de travail A, vous acceptez la demande de partage et créez une base de données. Lorsque vous créez ultérieurement un partage de données vers le même compte Snowflake 123 à partir de l'espace de travail B, aucune nouvelle demande de partage n'est envoyée : les données sont immédiatement ajoutées au partage existant et deviennent disponibles dans la base de données précédemment créée.

### Si j'ai plusieurs espaces de travail, une seule base de données contient-elle les données de tous ces espaces ?

Oui. Lorsque vous partagez des données provenant de plusieurs espaces de travail Braze vers le même compte Snowflake, toutes les données sont combinées en un seul partage et disponibles dans la même base de données. Vous pouvez filtrer les données par `app_group_id` pour distinguer les espaces de travail.

En guise de bonne pratique, filtrez toujours par `app_group_id` dans vos requêtes afin de les protéger contre les évolutions futures. Ainsi, vos tableaux de bord et rapports restent exacts si vous ajoutez des espaces de travail supplémentaires à l'avenir. Sans ce filtre, vos indicateurs peuvent inclure de manière inattendue des données provenant d'espaces de travail nouvellement ajoutés.

### Quelle est l'approche recommandée pour gérer les données provenant de plusieurs espaces de travail dans Snowflake ?

Envoyez toutes les données de Braze dans la même base de données et filtrez par `app_group_id` pour distinguer les espaces de travail. Cette approche simplifie la gestion des données et garantit l'établissement de rapports cohérents dans l'ensemble de votre organisation.

### De combien de connecteurs de partage de données Snowflake ai-je besoin pour plusieurs espaces de travail ?

Le nombre de connecteurs dont vous avez besoin dépend de votre configuration spécifique et de vos droits. Contactez votre équipe de compte Braze pour en savoir plus sur les droits adaptés à votre cas d'utilisation.


