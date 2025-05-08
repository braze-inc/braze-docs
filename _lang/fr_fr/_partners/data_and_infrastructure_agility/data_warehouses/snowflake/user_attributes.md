---
nav_title: "Attributs du profil utilisateur"
article_title: "Vues d'attributs d'utilisateurs dans Snowflake" 
page_order: 10
page_type: partner
search_tag: Partner
---

# Attributs par défaut du profil utilisateur

> Cette page sert de référence pour les vues d'attribut par défaut dans Snowflake. Il existe trois vues, chacune conçue pour un cas d'utilisation spécifique avec ses propres considérations en matière de performances.

{% alert important %}
Les attributs de profil utilisateur sont actuellement en version bêta pour les clients de Snowflake Data Sharing. Si vous utilisez le partage de données Snowflake et souhaitez accéder à cette version bêta, contactez votre gestionnaire de la satisfaction client ou le service d'assistance de Braze.
{% endalert %}

## Vues disponibles

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Cette vue fournit un aperçu périodique des attributs par défaut du profil utilisateur. Les données sont différées jusqu'à 8 heures, ce qui les rend utiles pour les requêtes qui ne nécessitent pas de mises à jour en temps réel.

#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NOMBRE        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notes d'utilisation

* Fournit un aperçu des attributs de l'utilisateur avec un **délai pouvant aller jusqu'à 8 heures.**
* Donne de bons résultats pour les requêtes qui ne nécessitent pas une précision en temps réel.
* L'exécution des requêtes est plus rapide, en particulier lors du filtrage sur des attributs autres que `USER_ID`.
* **Limitation :** Les données ne sont pas actualisées en temps réel.

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

Cette vue fournit des données en temps réel sur les attributs du profil utilisateur, les données étant retardées de 10 minutes maximum après une mise à jour dans Braze.

#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NOMBRE        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notes d'utilisation

* Fournit des attributs d'utilisateur actualisés dans un délai minimal (~10 minutes).
* Utile pour les analyses en temps réel et les scénarios nécessitant des données récentes.
* **Considérations relatives à la performance :**
    * Les requêtes sur les utilisateurs individuels sont plus rapides (moins d'une minute avec un grand entrepôt).
    * Les requêtes sans filtre USER_ID nécessitent une agrégation pour tous les utilisateurs, ce qui allonge considérablement le temps d'exécution.
    * Les requêtes sur un grand ensemble de données (plus de 100 millions d'utilisateurs, par exemple) peuvent prendre plusieurs minutes.

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

Cette vue stocke les journaux de modifications historiques des attributs des utilisateurs, capturant les modifications avec une granularité de 8 heures.

#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | NOMBRE        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### Notes d'utilisation

* Fournit un enregistrement des modifications historiques des attributs de l'utilisateur.
* Les données sont enregistrées toutes les huit heures, ce qui signifie que plusieurs mises à jour dans cette fenêtre sont combinées en un seul enregistrement. Les changements individuels au cours de cette période ne sont pas conservés séparément.
* `EFF_DT` et `END_DT` marquent le début et la fin de l'état des attributs d'un utilisateur final.

## Bonnes pratiques

### Utilisation recommandée des requêtes

| Cas d’utilisation                                               | Vue recommandée                                   | Remarques                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Questions générales** ne nécessitant pas de mises à jour récentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | Exécution rapide, avec des données remontant jusqu'à 8 heures.                          |
| Requêtes nécessitant les **derniers attributs de l'utilisateur**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | Fournit des mises à jour en temps quasi réel, mais peut être plus lent pour les grands ensembles de données. |
| **Suivi historique** des changements d'attributs           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Enregistre les changements d'attributs avec une granularité de 8 heures.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### Considérations sur les performances

* Les requêtes sur `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` devraient donner des résultats en moins de 10 secondes pour les grands ensembles de données (~1 milliard d'utilisateurs) sur un grand entrepôt.
* Les requêtes sur `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` pour un seul utilisateur donnent des résultats en moins d'une minute, mais ne sont pas très efficaces sans le filtrage de `USER_ID`.
* Les requêtes portant sur plus de 100 millions d'utilisateurs sur `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` peuvent prendre plusieurs minutes en raison de l'agrégation par utilisateur.


