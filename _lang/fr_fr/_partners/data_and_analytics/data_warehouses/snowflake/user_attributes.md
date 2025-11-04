---
nav_title: "Attributs du profil utilisateur"
article_title: "Vues d'attributs d'utilisateurs dans Snowflake" 
page_order: 10
page_type: partner
search_tag: Partner
---

# Attributs du profil utilisateur

> Cette page sert de référence pour les vues d'attribut par défaut et personnalisé dans Snowflake. Il existe trois vues pour les attributs par défaut et trois vues pour les attributs personnalisés, chacune étant conçue pour un cas d'utilisation spécifique avec ses propres considérations en matière de performances.

{% alert important %}
Les attributs de profil utilisateur sont actuellement en version bêta pour les clients de Snowflake Data Sharing. Si vous utilisez le partage de données Snowflake et souhaitez accéder à cette version bêta, contactez votre gestionnaire de la satisfaction client ou le service d'assistance de Braze.
{% endalert %}

# Vues disponibles

<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Afficher</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Attribut par défaut</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantanés de profil utilisateur</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Profils utilisateurs en temps réel</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historique des modifications</td>
    </tr>
    <tr>
      <td rowspan="3">Attribut personnalisé</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantanés de profil utilisateur</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Profils utilisateurs en temps réel</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historique des modifications</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Instantanés de profil utilisateur

Ces vues fournissent des instantanés périodiques des attributs du profil utilisateur. Les données sont différées de 12 heures maximum, ce qui les rend utiles pour les requêtes qui ne nécessitent pas de mises à jour en temps réel. 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTES |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### Instantanés de profil utilisateur - notes d'utilisation

* Fournit un aperçu des attributs de l'utilisateur avec un **délai pouvant aller jusqu'à 12 heures**.
* Donne de bons résultats pour les requêtes qui ne nécessitent pas une précision en temps réel.
* L'exécution des requêtes est plus rapide, en particulier lors du filtrage sur des attributs autres que `USER_ID`.
* **Limitation :** Les données ne sont pas actualisées en temps réel.

## Visualisation du profil utilisateur en temps réel

Ces vues fournissent des mises à jour en temps réel sur les attributs du profil utilisateur, les données étant retardées de 10 minutes au maximum après une mise à jour dans Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`
#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJET |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### Visualisation en temps réel du profil utilisateur - notes d'utilisation

* Fournit des attributs d'utilisateur actualisés dans un délai minimal (~10 minutes).
* Utile pour les analyses en temps réel et les scénarios nécessitant des données récentes.
* **Considérations relatives à la performance :**
    * Les requêtes sur les utilisateurs individuels sont plus rapides (moins d'une minute avec un grand entrepôt).
    * Les requêtes sans filtre USER_ID nécessitent une agrégation pour tous les utilisateurs, ce qui allonge considérablement le temps d'exécution.
    * Les requêtes sur un grand ensemble de données (plus de 100 millions d'utilisateurs, par exemple) peuvent prendre plusieurs minutes.

## Historique des modifications

Ces vues stockent les journaux de modifications historiques des attributs des utilisateurs, capturant les changements avec une granularité de 12 heures.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### Schéma

| Nom de la colonne     | Type de données     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NOMBRE |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANTES |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### Historique des modifications - notes d'utilisation

* Fournit un enregistrement des modifications historiques des attributs de l'utilisateur.
* Les données sont prises en compte toutes les 12 heures, ce qui signifie que les mises à jour multiples dans cette fenêtre sont combinées en un seul enregistrement. Les modifications individuelles au cours de cette période ne sont pas conservées séparément.
* `EFF_DT` et `END_DT` marquent le début et la fin de l'état des attributs d'un utilisateur final.

# Bonnes pratiques

## Utilisation recommandée des requêtes

| Cas d’utilisation                                               | Vues recommandées                                   | Remarques                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Questions générales** ne nécessitant pas de mises à jour récentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Exécution rapide, avec des données remontant jusqu'à 12 heures.                          |
| Requêtes nécessitant les **derniers attributs de l'utilisateur**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` et `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fournit des mises à jour en temps quasi réel, mais peut être plus lent pour les grands ensembles de données. |
| **Suivi historique** des changements d'attributs           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` et `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Enregistre les changements d'attributs avec une granularité de 12 heures.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## Considérations sur les performances

* Les requêtes sur `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devraient aboutir en moins de 10 secondes pour les grands ensembles de données (~1 milliard d'utilisateurs) sur un grand entrepôt.
* Les requêtes sur `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` pour un seul utilisateur sont renvoyées en moins d'une minute, mais elles sont peu efficaces sans le filtrage de `USER_ID`.
* Les requêtes portant sur plus de 100 millions d'utilisateurs dans `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` peuvent prendre plusieurs minutes en raison de l'agrégation par utilisateur.


