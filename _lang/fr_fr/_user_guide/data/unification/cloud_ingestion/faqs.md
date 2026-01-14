---
nav_title: FAQ
article_title: "FAQ sur l'ingestion de données dans le cloud"
page_order: 100
page_type: FAQ
description: "Cette page répond aux questions fréquemment posées sur l'ingestion de données dans le cloud."
toc_headers: h2
---

# Questions fréquemment posées

> Cette page contient des réponses à certaines questions fréquemment posées concernant l'ingestion de données dans le cloud.

## Pourquoi ai-je reçu un e-mail ? "Erreur de synchronisation du CDI" ?

Ce type d'e-mail signifie généralement qu'il y a un problème dans la configuration de votre CDI. Voici quelques problèmes courants et comment les résoudre :

### CDI ne peut pas accéder à l'entrepôt de données ou à la table en utilisant vos identifiants

Cela peut signifier que les informations d'identification dans CDI sont incorrectes ou qu'elles sont mal configurées dans l'entrepôt de données. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/).

### Le tableau est introuvable

Essayez de mettre à jour votre intégration avec la configuration correcte de la base de données ou créez des ressources correspondantes sur l'entrepôt de données, comme `database/table`.

### Le catalogue est introuvable

Le catalogue configuré dans l'intégration n'existe pas dans le catalogue de Braze. Un catalogue peut être supprimé après la mise en place de l'intégration. Pour résoudre le problème, mettez à jour l'intégration pour utiliser un catalogue différent ou créez un nouveau catalogue qui correspond au nom du catalogue dans l'intégration.

## Pourquoi ai-je reçu un e-mail ? "Erreurs de rangs dans la synchronisation de votre CDI" ?

Ce type d'e-mail signifie que certaines de vos données n'ont pas pu être traitées lors de la synchronisation. Pour trouver l'erreur spécifique, vous pouvez consulter les journaux dans Braze en allant dans **CDI** > **Sync Log.**

## Comment puis-je corriger les erreurs pour Test Connection et les e-mails d'assistance ?

{% tabs %}
{% tab Snowflake %}
### Test La connexion est lente

Test Connection s'exécute sur votre entrepôt de données, l'augmentation de la capacité de l'entrepôt peut donc améliorer sa vitesse. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Erreur de connexion à l'instance de Snowflake : La requête entrante avec IP n'est pas autorisée à accéder à Snowflake

Essayez d'ajouter les IP officielles de Braze à votre liste d'autorisations d'IP. Pour plus d'informations, reportez-vous à la section [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), ou autorisez les adresses IP correspondantes :

{% multi_lang_include data_centers.md datacenters='ips' %}

### Erreur d'exécution de SQL due à la configuration du client : 002003 (42S02) : Erreur de compilation SQL : n'existe pas ou n'est pas autorisé

Si la table n'existe pas, créez-la. Si la table existe, vérifiez que l'utilisateur et le rôle ont le droit de lire la table.

### Impossible d'utiliser le schéma

Si vous recevez cette erreur, accordez l'accès à ce schéma à l'utilisateur ou au rôle spécifié.

### Impossible d'utiliser le rôle

Si vous recevez cette erreur, autorisez cet utilisateur à utiliser le rôle spécifié.

### Accès utilisateur désactivé

Si vous recevez cette erreur, autorisez cet utilisateur à accéder à votre compte Snowflake.

### Erreur de connexion à l'instance de Snowflake avec la clé actuelle et l'ancienne clé

Si vous recevez cette erreur, assurez-vous que l'utilisateur utilise la clé publique actuelle telle qu'elle s'affiche dans votre tableau de bord de Braze.
{% endtab %}

{% tab Redshift %}
### Test La connexion est lente

Test Connection s'exécute sur votre entrepôt de données, l'augmentation de la capacité de l'entrepôt peut donc améliorer sa vitesse. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### Permission refusée pour la relation {table_name}

Si vous recevez cette erreur :

  - Accordez l'autorisation `usage` sur le schéma pour cet utilisateur.
  - Accordez à cet utilisateur l'autorisation `select` sur la table.

### Erreur de création de connexion

Si vous recevez cette erreur, vérifiez que l'endpoint et le port de Redshift sont corrects.

### Erreur dans la création d'un tunnel SSH

Si vous recevez cette erreur :

  - Vérifiez que la clé publique de votre tableau de bord de Braze se trouve sur l'hôte ec2 utilisé pour le tunnel SSH.
  - Vérifiez que votre nom d'utilisateur est correct.
  - Vérifiez que le tunnel SSH est correct.
{% endtab %}

{% tab BigQuery %}
### Test La connexion est lente

Test Connection s'exécute sur votre entrepôt de données, l'augmentation de la capacité de l'entrepôt peut donc améliorer sa vitesse. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### L'utilisateur n'a pas le droit d'interroger la table

Si vous recevez cette erreur, ajoutez des autorisations d'utilisateur pour interroger la table.

### Votre utilisation a dépassé le quota personnalisé

Si vous recevez cette erreur, votre quota doit être mis à jour pour que vous puissiez continuer à synchroniser à votre rythme actuel.

### Le tableau n'a pas été trouvé dans l'emplacement/localisation {région} Emplacement

Si vous recevez cette erreur, vérifiez que votre table se trouve dans le bon projet et dans le bon jeu de données.

### Signature JWT invalide

Si vous recevez cette erreur, vérifiez que le service BigQuery API est activé pour votre compte.
{% endtab %}

{% tab Databricks %}
### Test La connexion est lente

Test Connection s'exécute sur votre entrepôt de données, l'augmentation de la capacité de l'entrepôt peut donc améliorer sa vitesse. Pour Databricks, il peut y avoir un temps de chauffe de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des retards lors de la configuration et des tests de connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL sans serveur minimisera le temps de chauffe et améliorera le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.

### La commande a échoué parce que l'entrepôt a été arrêté

Si vous recevez cette erreur, assurez-vous que l'entrepôt Databricks est en cours d'exécution.

### Service : Amazon S3 ; Code de statut : 403 ; Code d'erreur : 403 Interdit

Si vous recevez cette erreur, consultez [Databricks : Erreur interdite lors de l'accès aux données S3](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Comment mettre à jour mes préférences en matière d'alertes e-mail pour les intégrations CDI ?

Chaque intégration a ses propres préférences en matière de notification. Accédez à la page CDI et sélectionnez le nom de l'intégration que vous souhaitez mettre à jour. Dans la section **Préférences de notification**, vous pouvez mettre à jour la façon dont vous recevez les alertes concernant l'intégration sélectionnée.

## Que se passe-t-il si une future UPDATED_AT est synchronisée avec une intégration ?

Le CDI utilise le site `UPDATED_AT` pour déterminer quelles données sont nouvelles. Après la synchronisation d'un futur `UPDATED_AT`, toutes les données antérieures à cette date et heure futures ne seront pas traitées. Pour y remédier :

1. Correct `UPDATED_AT`.
2. Supprimez les anciennes données déjà synchronisées avec Braze.
3. Créez une nouvelle intégration pour traiter à nouveau cette table.

## Pourquoi le nombre de lignes synchronisées ne correspond-il pas à celui de mon entrepôt ?

CDI utilise `UPDATED_AT` pour décider des enregistrements à récupérer lors d'une synchronisation. Consultez [cette illustration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced) pour voir comment cela fonctionne. Au début d'un cycle de synchronisation, CDI interroge votre entrepôt pour obtenir tous les enregistrements dont l'adresse `UPDATED_AT` est égale ou postérieure à l'horodatage `UPDATED_AT` précédemment traité. Tout enregistrement récupéré au moment de l'exécution de la requête sera synchronisé dans Braze. Voici les cas les plus fréquents où un enregistrement peut ne pas être synchronisé :

- Vous ajoutez des enregistrements à la table avec une valeur `UPDATED_AT` qui a déjà été traitée.
- Vous mettez à jour les valeurs des enregistrements après qu'ils ont été traités par une synchronisation, mais vous laissez `UPDATED_AT` inchangé. 
- Vous ajoutez ou mettez à jour des enregistrements alors qu'une synchronisation est en cours. Selon le moment où la requête CDI est exécutée, il peut y avoir des conditions de concurrence qui font que les enregistrements ne sont pas pris en compte.

{% alert tip %}
Pour éviter ces comportements à l'avenir, nous vous recommandons d'utiliser des valeurs `UPDATED_AT` qui augmentent de façon monotone et de ne pas mettre à jour la table pendant l'exécution de la synchronisation planifiée.
{% endalert %}

## Lors d'une synchronisation, l'ordre est-il préservé si plusieurs enregistrements partagent le même ID ?

L'ordre de traitement n'est pas prévisible à 100 %. Par exemple, s'il y a plusieurs lignes avec le même `EXTERNAL_ID` dans la table lors d'une synchronisation, nous ne pouvons pas garantir quelle valeur se retrouvera dans le profil final. Si vous mettez à jour le même site `EXTERNAL_ID` avec différents attributs dans la colonne payload, toutes les modifications sont prises en compte lorsque la synchronisation est terminée.

## Quelles sont les mesures de sécurité du CDI ?

### Nos mesures

Braze a mis en place les mesures suivantes pour l'ICD :

- Toutes les données d'identification sont cryptées dans notre base de données, et seuls certains employés y ont un accès authentifié.
- Nous utilisons des connexions cryptées pour acheminer les données vers les entrepôts des clients.
- Nous effectuons des demandes aux endpoints de l'API Braze en utilisant les mêmes clés API et connexions TLS que celles que nous recommandons à nos clients d'utiliser.
- Nous mettons régulièrement à jour nos bibliothèques et obtenons tous les correctifs de sécurité.

### Vos mesures

Nous vous recommandons, ainsi qu'à votre équipe, de mettre en place les mesures de sécurité suivantes de votre côté : 

- Restreindre l'accès aux informations d'identification au minimum requis pour le fonctionnement du CDI. En effet, nous devons pouvoir exécuter des sélections (et des comptages) sur des tables et des vues spécifiques.
- Limitez les adresses IP pouvant accéder aux tables aux [adresses IP]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) officiellement publiées par [Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views).
