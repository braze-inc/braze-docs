---
nav_title: FAQ
article_title: "FAQ sur l'ingestion de données cloud"
page_order: 100
page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur l'ingestion de données dans le cloud."
toc_headers: h2
---

# Foire aux questions

> Cette page contient des réponses à certaines questions fréquemment posées concernant l'ingestion de données dans le cloud.

## Pourquoi ai-je reçu l’e-mail suivant : Erreur dans la synchronisation CDI

Ce type d'e-mail signifie généralement qu'il y a un problème avec votre configuration CDI. Voici quelques problèmes courants et comment les résoudre :

### CDI ne peut pas accéder à l'entrepôt de données ou à la table en utilisant vos identifiants

Cela peut signifier que les identifiants dans CDI sont incorrects ou mal configurés dans l'entrepôt de données. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### La table ne peut pas être trouvée

Essayez de mettre à jour votre intégration avec la configuration correcte de la base de données ou de créer des ressources correspondantes dans l'entrepôt de données, telles que `database/table`.

### Le catalogue ne peut pas être trouvé

Le catalogue configuré dans l'intégration n'existe pas dans le catalogue de Braze. Un catalogue peut être supprimé après la mise en place de l'intégration. Pour résoudre le problème, mettez à jour l'intégration pour utiliser un catalogue différent ou créez un nouveau catalogue qui correspond au nom du catalogue dans l'intégration.

## Pourquoi ai-je reçu l’e-mail suivant : Erreurs de ligne dans votre synchronisation CDI

Ce type d'e-mail signifie que certaines de vos données n'ont pas pu être traitées lors de la synchronisation. Pour connaître l'erreur spécifique, vous pouvez consulter les journaux dans Braze en allant à **CDI** > **Journal de synchronisation**.

## Comment puis-je corriger les erreurs pour Test Connection et les e-mails de support ?

{% tabs %}
{% tab Snowflake %}
### Le test de connexion est lent

Le test de connexion est en cours d'exécution sur votre entrepôt de données, donc l’augmentation de la capacité de l'entrepôt peut l’accélérer. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Erreur de connexion à l'instance Snowflake : La demande entrante avec l'IP n'est pas autorisée à accéder à Snowflake

Essayez d'ajouter les IP officielles de Braze à votre liste d'autorisation IP. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### Erreur lors de l'exécution de SQL en raison de la configuration du client : 002003 (42S02): Erreur de compilation SQL : n'existe pas ou n'est pas autorisé

Si la table n'existe pas, créez-la. Si la table existe, vérifiez que l'utilisateur et le rôle ont les autorisations pour lire à partir de la table.

### Impossible d'utiliser le schéma

Si vous recevez cette erreur, accordez l'accès à ce schéma pour l'utilisateur ou le rôle spécifié.

### Impossible d'utiliser le rôle

Si vous recevez cette erreur, autorisez cet utilisateur à utiliser le rôle spécifié.

### Accès utilisateur désactivé

Si vous recevez cette erreur, autorisez cet utilisateur à accéder à votre compte Snowflake.

### Erreur de connexion à l'instance Snowflake avec la clé actuelle et ancienne

Si vous recevez cette erreur, assurez-vous que l'utilisateur utilise la clé publique actuelle telle qu'elle s'affiche dans votre tableau de bord de Braze.
{% endtab %}

{% tab Redshift %}
### Le test de connexion est lent

Le test de connexion est en cours d'exécution sur votre entrepôt de données, donc l’augmentation de la capacité de l'entrepôt peut l’accélérer. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Permission refusée pour la relation {table_name}

Si vous recevez cette erreur :

  - Accorder la permission `usage` sur le schéma pour cet utilisateur.
  - Accorder la permission `select` sur la table pour cet utilisateur.

### Erreur de création de connexion

Si vous recevez cette erreur, vérifiez que l’endpoint et le port Redshift sont corrects.

### Créer une erreur de tunnel SSH

Si vous recevez cette erreur :

  - Vérifiez que la clé publique sur votre tableau de bord de Braze est sur l'hôte EC2 utilisé pour le tunnel SSH.
  - Vérifiez que votre nom d'utilisateur est correct.
  - Vérifiez que le tunnel SSH est correct.
{% endtab %}

{% tab BigQuery %}
### Le test de connexion est lent

Le test de connexion est en cours d'exécution sur votre entrepôt de données, donc l’augmentation de la capacité de l'entrepôt peut l’accélérer. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### L'utilisateur n'a pas la permission d'interroger la table

Si vous recevez cette erreur, ajoutez des autorisations d'utilisateur pour interroger la table.

### Votre utilisation a dépassé le quota personnalisé

Si vous recevez cette erreur, votre quota doit être mis à jour afin que vous puissiez continuer à synchroniser à votre rythme actuel.

### Table introuvable dans l'emplacement {region} Location

Si vous recevez cette erreur, vérifiez que votre table se trouve dans le projet et l'ensemble de données corrects.

### Signature JWT invalide

Si vous recevez cette erreur, vérifiez que le service API BigQuery est activé pour votre compte.
{% endtab %}

{% tab Databricks %}
### Le test de connexion est lent

Le test de connexion est en cours d'exécution sur votre entrepôt de données, donc l’augmentation de la capacité de l'entrepôt peut l’accélérer. Pour Databricks, il peut y avoir deux à cinq minutes de temps de préchauffage lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations programmées. L'utilisation d'une instance SQL sans serveur permet de réduire ce temps de préchauffage et d’améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### La commande a échoué car l'entrepôt a été arrêté

Si vous recevez cette erreur, assurez-vous que l'entrepôt Databricks est en cours d'exécution.

### Service: Amazon S3 ; Code d'état : 403 ; Code d'erreur : 403 Interdit

Si vous recevez cette erreur, consultez [Databricks: Erreur interdite lors de l'accès aux données S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Comment puis-je mettre à jour mes préférences d'alerte par e-mail pour les intégrations CDI ?

Chaque intégration a sa propre préférence de notification. Accédez à la page CDI et sélectionnez le nom de l'intégration que vous souhaitez mettre à jour. Dans la section **Préférences de notification**, vous pouvez mettre à jour la façon dont vous recevez les alertes concernant l'intégration sélectionnée.

## Que se passe-t-il si un futur UPDATED_AT est synchronisé avec une intégration ?

CDI utilise `UPDATED_AT` pour décider quelles données sont nouvelles. Après qu'un futur `UPDATED_AT` est synchronisé, toutes les données antérieures à cette date et heure futures ne seront pas traitées. Pour corriger cela :

1. Correct `UPDATED_AT`.
2. Supprimez toutes les anciennes données déjà synchronisées avec Braze
3. Créer une nouvelle intégration pour traiter à nouveau cette table.

## Pourquoi le nombre de « lignes synchronisées » ne correspond-il pas à celui de mon entrepôt ?

CDI utilise `UPDATED_AT` pour décider quels enregistrements récupérer lors d'une synchronisation. Regardez [cette illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) pour voir comment cela fonctionne. Au début d'une exécution de synchronisation, CDI interroge votre entrepôt pour obtenir tous les enregistrements avec `UPDATED_AT` plus tard que la valeur précédemment traitée. Tout enregistrement récupéré au moment de l'exécution de la requête sera synchronisé dans Braze. Voici les cas courants où un enregistrement pourrait ne pas être synchronisé :

- Vous ajoutez des enregistrements au tableau avec une valeur `UPDATED_AT` qui a déjà été traitée.
- Vous mettez à jour les valeurs des enregistrements après qu'elles ont été traitées par une synchronisation, mais vous laissez `UPDATED_AT` inchangé. 
- Vous ajoutez ou mettez à jour des enregistrements pendant qu'une synchronisation est en cours. Selon le moment où la requête CDI s'exécute, il pourrait y avoir des conditions de concurrence qui entraînent la non prise en compte de certains enregistrements.

{% alert tip %}
Pour éviter ces comportements à l'avenir, nous recommandons d'utiliser des valeurs `UPDATED_AT` croissantes de manière monotone et de ne pas mettre à jour la table pendant votre exécution de synchronisation planifiée.
{% endalert %}

## Lors d'une synchronisation, l'ordre est-il préservé si plusieurs enregistrements partagent le même identifiant ?

L'ordre de traitement n'est pas prévisible à 100%. Par exemple, s'il y a plusieurs lignes avec le même `EXTERNAL_ID` dans le tableau lors d'une synchronisation, nous ne pouvons pas garantir quelle valeur se retrouvera dans le profil final. 

## Quelles sont les mesures de sécurité pour CDI ?

### Les mesures de Braze

Braze dispose des mesures suivantes pour CDI :

- Toutes les informations d'identification sont cryptées dans notre base de données, et seuls certains employés y ont accès après authentification.
- Nous utilisons des connexions chiffrées pour acheminer les données vers les entrepôts des clients.
- Nous faisons des demandes aux points de terminaison de l'API Braze en utilisant les mêmes clés API et connexions TLS que nous recommandons à nos clients d'utiliser.
- Nous mettons régulièrement à jour nos bibliothèques et obtenons tous les correctifs de sécurité.

### Vos mesures

Nous vous recommandons, à vous et à votre équipe, de mettre en place les mesures de sécurité suivantes de votre côté : 

- Restreindre l'accès des identifiants au minimum requis pour que CDI puisse fonctionner. C'est parce que nous devons être capables d'exécuter des sélections (et des comptages) sur les tables et vues spécifiques.
- Restreindre les IPs qui peuvent accéder aux tables aux [IPs Braze publiées officiellement]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).
