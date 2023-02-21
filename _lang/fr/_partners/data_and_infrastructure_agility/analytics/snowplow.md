---
nav_title: Snowplow
article_title: Snowplow
page_order: 1
description: "L’intégration de Braze et Snowplow permet aux utilisateurs de transférer des événements de Snowplow vers Braze avec le marquage côté serveur de Google Tag Manager."
alias: /partners/snowplow/
page_type: partner
search_tag: Partenaire

---

# Snowplow

> [Snowplow][1] est une plateforme évolutive et open source conçue pour collecter des données enrichies de haute qualité et à faible latence. Cette plateforme collecte des données comportementales complètes et de hautes qualités pour les grandes entreprises.

L’intégration de Braze et Snowplow permet aux utilisateurs de transférer des événements de Snowplow vers Braze avec le marquage côté serveur de Google Tag Manager. La balise Snowplow Braze vous permet d’envoyer des événements à Braze tout en bénéficiant d’une flexibilité et d’un contrôle accrus :
- Visibilité totale sur toutes les modifications de données
- Capacité à évoluer et à se développer au fil du temps
- Toutes les données restent dans votre cloud privé jusqu’à ce que vous choisissiez de les envoyer
- Configuration simplifiée grâce à de vastes bibliothèques de balises et à l’interface utilisateur familière de Google Tag Manager

Tirez parti des données comportementales enrichies de Snowplow pour effectuer des interactions client efficaces dans Braze et livrer des messages personnalisés en temps réel.

## Conditions préalables

| Configuration requise | Description |
| ----------- | ----------- |
| Pipeline Snowplow | Un pipeline Snowplow doit être implémenté et opérationnel. |
| Google Tag Manager Server-Side | GTM-SS doit être déployé et le [client Snowplow pour GTM-SS][2] doit être configuré. |
| Clé API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)** .|
| Endpoint REST de Braze | [URL de votre endpoint REST][3]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

### Livraison personnalisée par événement
Utilisez l’un des nombreux événements enrichis et collectés automatiquement par défaut par Snowplow, ou définissez vos événements personnalisés pour créer des parcours clients encore plus granulaires qui ont du sens pour votre entreprise. Tirez parti des données comportementales enrichies de Snowplow pour concevoir des entonnoirs de clients et libérer de la valeur pour vos équipes marketing et produit, les aidant ainsi à maximiser le taux de conversion et l’utilisation des produits via Braze.

### Segmentation dynamique
Créez des audiences dynamiques dans Braze en vous basant sur les données comportementales de haute qualité de Snowplow : Lorsque les utilisateurs effectuent des actions dans votre produit, application ou site Web, vous pouvez tirer parti des données comportementales en temps réel collectées par Snowplow pour ajouter ou supprimer automatiquement des utilisateurs dans des segments de Braze.

## Intégration

### Étape 1 : Installation du modèle

#### Installation manuelle

1. Téléchargez le fichier modèle [`template.tpl`][7].
2. Créez une nouvelle balise dans la section **Modèles** d’un conteneur de serveur Google Tag Manager.
3. Cliquez sur le menu **Plus d’actions** dans le coin supérieur droit, puis cliquez sur **Importer**.
4. Importez le fichier modèle que vous venez de télécharger et enregistrez-le.

#### Galerie de Tag Manager

Bientôt disponible ! Cette balise sera incluse dans la galerie GTM après approbation.

### Étape 2 : Configurer la balise Braze

Une fois le modèle installé, ajoutez la balise Braze à votre conteneur GTM-SS.

1. Depuis l’onglet **Balise**, cliquez sur **Nouvelle balise**, puis **Balise Braze** comme configuration pour votre balise.
2. Sélectionnez un déclencheur pour les événements que vous souhaitez envoyer à Braze.
3. Saisissez les paramètres requis et configurez votre balise (des informations supplémentaires sont fournies dans la prochaine section : Personnalisation).
4. Cliquez sur **Enregistrer**.

## Personnalisation

### Paramètres requis pour la balise

Le tableau suivant répertorie les paramètres de balise que vous devez inclure dans votre configuration de balise Braze.

| Paramètre | Description |
| --------- | ----------- |
| Endpoint d’API REST Braze | Renseignez l’URL de votre [endpoint][3] REST Braze. |
| Clé API Braze | Renseignez votre [clé API][4] Braze qui sera incluse dans chaque requête. |
| `external_id`  Braze| Définissez cette clé sur la propriété d’événement client qui correspond à l’`external_id` de vos utilisateurs et qui sera utilisée comme [Identifiant utilisateur Braze][5]. |
{: .reset-td-br-1 .reset-td-br-2}

### Mappage d’événements

Le tableau suivant répertorie les options de mappage d’événements pour les événements Snowplow, comme revendiqué par le [client Snowplow][2].

| Option de mappage | Description |
| --------- | ----------- |
| Inclure un événement auto-descriptif | Cette option activée par défaut indique si les données d’événement auto-descriptif de Snowplow seront incluses dans les objets des propriétés de l’événement envoyés à Braze. |
| Règles contextuelles des événements Snowflow | Cette option décrit comment la balise Braze utilisera les entités contextuelles associées à un événement Snowplow. |
| Extraire l’entité de la matrice si elle contient un seul élément | Les entités Snowplow sont toujours organisées en matrice, car plusieurs entités peuvent être jointes à un événement. Cette option permet de sélectionner l’élément de la matrice si la matrice ne contient qu’un seul élément. |
| Inclure toutes les entités dans l’objet événement | Cette option activée par défaut garantit que toutes les entités d’un événement seront incluses dans l’objet des propriétés de l’événement Braze. Désactivez cette option pour sélectionner et inclure des entités individuelles. |
{: .reset-td-br-1 .reset-td-br-2}

### Mappage avancé des événements

#### Règles des propriétés de l’événement

Si vous souhaitez inclure d’autres propriétés de l’événement client et les mapper sur l’événement Braze, veuillez consulter les règles énoncées dans le tableau ci-dessous : 

| Règles des propriétés de l’événement | Description |
| --------- | ----------- |
| Inclure les propriétés d’événement courantes | Cette option activée par défaut détermine si vous souhaitez inclure automatiquement les propriétés d’événement de la [définition des événements communs][6] dans les propriétés de l’événement Braze. |
| Règles supplémentaires pour le mappage des propriétés de l’utilisateur et de l’événement | Spécifiez la clé de propriété de l’événement client et la clé d’objet des propriétés que vous souhaitez mapper (ou laissez la clé mappée vide pour conserver le même nom). Vous pouvez utiliser le chemin d’accès à la clé ici (par ex., `x-sp-tp2.p` pour une plateforme d’événements Snowplow ou `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` pour un identifiant de page d’événements Snowplow [dans l’index de la matrice 0]) ou choisir des propriétés non associées à Snowplow si vous utilisez un autre client.<br><br>Les règles de mappage des propriétés de l’événement remplissent l’objet des propriétés de l’événement Braze.|
| Inclure les propriétés utilisateur courantes| Cette option activée par défaut détermine si vous souhaitez inclure les propriétés `user_data` de la définition d’événement courant dans l’objet des attributs utilisateur de Braze.|
| Propriété de l’heure de l’événement | Cette option vous permet de spécifier la propriété de l’événement client pour renseigner l’heure de l’événement (au format ISO-8601) ou la laisser vide pour utiliser l’heure actuelle (comportement par défaut). |
{: .reset-td-br-1 .reset-td-br-2}

### Mappage d’entité

À l’aide du tableau de mappage d’entité de Snowplow, les entités peuvent être mappées à nouveau pour avoir des noms différents dans Braze et que ceux-ci soient inclus dans les propriétés de l’événement ou dans les objets des attributs utilisateur. 

L’entité peut être spécifiée sous deux formats différents :
- Correspondance de version majeure : `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` où `com_snowplowanalytics_snowplow` est le fournisseur d’événements, `web_page` est le nom du schéma et `1` est le numéro de version majeure. `x-sp-` peut également être omis si vous le souhaitez.
- Correspondance complète du schéma : `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Option de mappage d’entité | Description |
| --------- | ----------- |
| Inclure des entités non mappées dans l’événement | Lorsque vous remappez ou déplacez des entités dans des attributs utilisateur avec la personnalisation précédente, cette option vous permet de garantir que toutes les entités non mappées (c.-à-d., toute entité qui ne fait pas partie des [règles de propriété de l’événement](#event-property-rules)) seront incluses dans l’objet des propriétés de l’événement Braze. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
