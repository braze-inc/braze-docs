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

## Pourquoi ai-je reçu l'e-mail suivant : « Erreur dans la synchronisation CDI » ?

Ce type d'e-mail signifie généralement qu'il y a un problème avec votre configuration CDI. Voici quelques problèmes courants et comment les résoudre :

### CDI ne peut pas accéder à l'entrepôt de données ou à la table avec vos identifiants

Cela peut signifier que les identifiants dans CDI sont incorrects ou mal configurés dans l'entrepôt de données. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### La table est introuvable

Essayez de mettre à jour votre intégration avec la bonne configuration de base de données, ou créez les ressources correspondantes dans l'entrepôt de données, telles que `database/table`.

### Le catalogue est introuvable

Le catalogue configuré dans l'intégration n'existe pas dans le catalogue de Braze. Un catalogue peut avoir été supprimé après la mise en place de l'intégration. Pour résoudre le problème, mettez à jour l'intégration pour utiliser un autre catalogue ou créez un nouveau catalogue dont le nom correspond à celui défini dans l'intégration.

## Pourquoi ai-je reçu l'e-mail suivant : « Erreurs de ligne dans votre synchronisation CDI » ?

Ce type d'e-mail signifie que certaines de vos données n'ont pas pu être traitées lors de la synchronisation. Pour identifier l'erreur précise, consultez les journaux dans Braze en accédant à **CDI** > **Journal de synchronisation**.

## Comment corriger les erreurs liées à Test Connection et aux e-mails d'assistance ?

{% tabs %}
{% tab Snowflake %}
### Le test de connexion est lent

Le test de connexion s'exécute sur votre entrepôt de données : augmenter la capacité de l'entrepôt peut donc améliorer sa rapidité. L'utilisation d'une instance SQL serverless permet de réduire le temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Erreur de connexion à l'instance Snowflake : la requête entrante avec cette IP n'est pas autorisée à accéder à Snowflake

Essayez d'ajouter les adresses IP officielles de Braze à votre liste d'autorisation. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), ou autorisez les adresses IP correspondantes :

{% multi_lang_include data_centers.md datacenters='ips' %}

### Erreur lors de l'exécution SQL due à la configuration client : 002003 (42S02) : erreur de compilation SQL : n'existe pas ou non autorisé

Si la table n'existe pas, créez-la. Si elle existe déjà, vérifiez que l'utilisateur et le rôle disposent des autorisations de lecture sur cette table.

### Impossible d'utiliser le schéma

Si vous recevez cette erreur, accordez l'accès à ce schéma pour l'utilisateur ou le rôle spécifié.

### Impossible d'utiliser le rôle

Si vous recevez cette erreur, autorisez cet utilisateur à utiliser le rôle spécifié.

### Accès utilisateur désactivé

Si vous recevez cette erreur, autorisez cet utilisateur à accéder à votre compte Snowflake.

### Erreur de connexion à l'instance Snowflake avec la clé actuelle et l'ancienne clé

Si vous recevez cette erreur, assurez-vous que l'utilisateur utilise la clé publique actuelle telle qu'affichée dans votre tableau de bord de Braze.
{% endtab %}

{% tab Redshift %}
### Le test de connexion est lent

Le test de connexion s'exécute sur votre entrepôt de données : augmenter la capacité de l'entrepôt peut donc améliorer sa rapidité. L'utilisation d'une instance SQL serverless permet de réduire le temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Accès refusé pour la relation {table_name}

Si vous recevez cette erreur :

  - Accordez la permission `usage` sur le schéma pour cet utilisateur.
  - Accordez la permission `select` sur la table pour cet utilisateur.

### Erreur de création de connexion

Si vous recevez cette erreur, vérifiez que l'endpoint et le port Redshift sont corrects.

### Erreur de création du tunnel SSH

Si vous recevez cette erreur :

  - Vérifiez que la clé publique affichée dans votre tableau de bord de Braze est bien présente sur l'hôte EC2 utilisé pour le tunnel SSH.
  - Vérifiez que votre nom d'utilisateur est correct.
  - Vérifiez que le tunnel SSH est correct.
{% endtab %}

{% tab BigQuery %}
### Le test de connexion est lent

Le test de connexion s'exécute sur votre entrepôt de données : augmenter la capacité de l'entrepôt peut donc améliorer sa rapidité. L'utilisation d'une instance SQL serverless permet de réduire le temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### L'utilisateur n'a pas la permission d'interroger la table

Si vous recevez cette erreur, ajoutez les autorisations nécessaires pour que l'utilisateur puisse interroger la table.

### Votre utilisation a dépassé le quota personnalisé

Si vous recevez cette erreur, votre quota doit être mis à jour pour que vous puissiez continuer à synchroniser au rythme actuel.

### Table introuvable dans l'emplacement {region}

Si vous recevez cette erreur, vérifiez que votre table se trouve dans le bon projet et le bon ensemble de données.

### Signature JWT invalide

Si vous recevez cette erreur, vérifiez que le service API BigQuery est activé pour votre compte.
{% endtab %}

{% tab Databricks %}
### Le test de connexion est lent

Le test de connexion s'exécute sur votre entrepôt de données : augmenter la capacité de l'entrepôt peut donc améliorer sa rapidité. Pour Databricks, il peut y avoir deux à cinq minutes de préchauffage lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraîne des délais lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL serverless permet de réduire ce temps de préchauffage et d'améliorer le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### La commande a échoué car l'entrepôt était arrêté

Si vous recevez cette erreur, assurez-vous que l'entrepôt Databricks est en cours d'exécution.

### Service : Amazon S3 ; Code d'état : 403 ; Code d'erreur : 403 Forbidden

Si vous recevez cette erreur, consultez [Databricks : Erreur Forbidden lors de l'accès aux données S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Comment mettre à jour mes préférences d'alerte par e-mail pour les intégrations CDI ?

Chaque intégration dispose de ses propres préférences de notification. Accédez à la page CDI et sélectionnez le nom de l'intégration que vous souhaitez mettre à jour. Dans la section **Préférences de notification**, vous pouvez modifier la façon dont vous recevez les alertes pour l'intégration sélectionnée.

## Que se passe-t-il si un UPDATED_AT futur est synchronisé avec une intégration ?

CDI utilise `UPDATED_AT` pour déterminer quelles données sont nouvelles. Une fois qu'un `UPDATED_AT` situé dans le futur a été synchronisé, toutes les données antérieures à cette date et heure ne seront pas traitées. Pour corriger cela :

1. Corrigez `UPDATED_AT`.
2. Supprimez toutes les anciennes données déjà synchronisées avec Braze.
3. Créez une nouvelle intégration pour traiter à nouveau cette table.

## Pourquoi le nombre de « lignes synchronisées » ne correspond-il pas à celui de mon entrepôt ?

CDI utilise `UPDATED_AT` pour décider quels enregistrements récupérer lors d'une synchronisation. Consultez [cette illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) pour comprendre le fonctionnement. Au début d'une synchronisation, CDI interroge votre entrepôt de données pour obtenir tous les enregistrements dont la valeur `UPDATED_AT` est postérieure à la dernière valeur `UPDATED_AT` traitée. Les enregistrements situés exactement à l'horodatage limite peuvent également être re-synchronisés si de nouvelles lignes partagent cet horodatage. Tout enregistrement récupéré au moment de l'exécution de la requête est synchronisé dans Braze. Voici les cas courants où un enregistrement pourrait ne pas être synchronisé :

- Vous ajoutez des enregistrements à la table avec une valeur `UPDATED_AT` qui a déjà été traitée.
- Vous mettez à jour les valeurs des enregistrements après leur traitement par une synchronisation, mais vous laissez `UPDATED_AT` inchangé. 
- Vous ajoutez ou mettez à jour des enregistrements pendant qu'une synchronisation est en cours. Selon le moment où la requête CDI s'exécute, des conditions de concurrence peuvent empêcher la prise en compte de certains enregistrements.

{% alert tip %}
Pour éviter ces comportements à l'avenir, nous recommandons d'utiliser des valeurs `UPDATED_AT` croissantes de manière monotone et de ne pas mettre à jour la table pendant l'exécution de votre synchronisation planifiée.
{% endalert %}

## Lors d'une synchronisation, l'ordre est-il préservé si plusieurs enregistrements partagent le même ID ?

L'ordre de traitement n'est pas prévisible à 100 %. Par exemple, s'il y a plusieurs lignes avec le même `EXTERNAL_ID` dans la table lors d'une synchronisation, nous ne pouvons pas garantir quelle valeur se retrouvera dans le profil final. Si vous mettez à jour le même `EXTERNAL_ID` avec différents attributs dans la colonne payload, toutes les modifications sont prises en compte une fois la synchronisation terminée.

## Pourquoi les nouveaux utilisateurs ne sont-ils pas créés à partir de ma synchronisation CDI ?

Si l'option **Mettre à jour uniquement les utilisateurs existants** est activée dans votre intégration CDI, seuls les utilisateurs déjà présents dans Braze sont mis à jour, et aucun nouvel utilisateur n'est créé. Cela signifie que si une ligne de votre table de synchronisation fait référence à un `EXTERNAL_ID` qui ne correspond à aucun utilisateur Braze existant, cette ligne est ignorée.

Pour créer de nouveaux utilisateurs via CDI, désactivez l'option **Mettre à jour uniquement les utilisateurs existants** dans les paramètres de votre intégration. Rendez-vous dans **Paramètres des données** > **Ingestion de données dans le cloud** et sélectionnez une intégration.

## Quelles sont les mesures de sécurité pour CDI ?

### Nos mesures

Braze dispose des mesures suivantes pour CDI :

- Toutes les informations d'identification sont chiffrées dans notre base de données, et seuls certains employés y ont accès après authentification.
- Nous utilisons des connexions chiffrées pour récupérer les données depuis les entrepôts des clients.
- Nous effectuons des requêtes vers les endpoints de l'API Braze en utilisant les mêmes clés API et connexions TLS (sécurité de la couche de transport) que nous recommandons à nos clients d'utiliser.
- Nous mettons régulièrement à jour nos bibliothèques et appliquons tous les correctifs de sécurité.

### Vos mesures

Nous vous recommandons, à vous et à votre équipe, de mettre en place les mesures de sécurité suivantes de votre côté : 

- Restreindre l'accès des identifiants au minimum requis pour le fonctionnement de CDI. En effet, nous devons être en mesure d'exécuter des requêtes select (et count) sur les tables et vues spécifiques.
- Restreindre les adresses IP pouvant accéder aux tables aux [IP Braze publiées officiellement]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).