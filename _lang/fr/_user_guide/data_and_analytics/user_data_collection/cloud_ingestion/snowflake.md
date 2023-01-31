---
nav_title: Redshift
article_title: Ingestion de données cloud dans Braze pour Redshift
description: "Cet article de référence couvre l’Ingestion de Données Cloud dans Braze et comment synchroniser les données utilisateur pertinentes avec votre intégration Redshift."
page_order: 4.1
page_type: reference
hidden: true

---

# Ingestion de données cloud pour Redshift

{% alert important %}
L’ingestion de données cloud Braze pour Redshift est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Paramétrage du produit

Les nouvelles intégrations d’ingestion de données cloud nécessitent une configuration sur Braze ainsi que dans votre instance Redshift. Suivez ces étapes pour configurer votre intégration :
1. Dans votre instance Redshift, paramétrez la ou les tables ou vues que vous voulez synchroniser avec Braze
2. Créez une nouvelle intégration dans le tableau de bord de Braze
3. Testez l’intégration et démarrez la synchronisation

### Paramétrez les tables et les vues

#### Étape 1 : Paramétrez la table 

De manière optionnelle, définissez une nouvelle base de données et un nouveau schéma pour contenir votre table source
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créer une table (ou vue) à utiliser pour votre intégration CDI
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   external_id varchar,
   payload varchar(max)
)
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et à la table, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée à la table. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour. Vous pouvez utiliser un des éléments parmi les suivants : external_id, user_alias ou braze_id.
- `PAYLOAD` - chaîne de caractères JSON des champs que vous désirez synchroniser pour l’utilisateur dans Braze.
 
#### Étape 2 : Créer un utilisateur et attribuer des autorisations 

```json
CREATE USER braze_user PASSWORD ‘{password}’;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user
```

Un nombre minimum d’autorisations est requis pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous devriez donner des autorisations pour un schéma ou les gérer en utilisant un groupe. 

#### Étape 3 : Autoriser l’accès aux IP de Braze (optional) 

Si vous avez un pare-feu ou d’autres politiques réseau actives, vous devrez donner accès au réseau de votre instance Redshift à Braze. Autorisez l’accès aux IP ci-dessous correspondant à la région de votre tableau de bord de Braze. 

| Pour les Instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` | Pour les Instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`


