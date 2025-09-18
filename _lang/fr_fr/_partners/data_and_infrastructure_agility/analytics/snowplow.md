---
nav_title: Snowplow
article_title: Snowplow
description: "Cet article de référence décrit le partenariat entre Braze et Snowplow, une plateforme de collecte de données open-source, qui vous permet de transmettre les événements Snowplow à Braze par l'intermédiaire du système de tags côté serveur de Google Tag Manager."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow][1] est une plateforme évolutive open-source pour la collecte de données riches, de haute qualité et à faible latence. Elle est conçue pour collecter des données comportementales complètes et de haute qualité pour les entreprises.

_Cette intégration est maintenue par Snowplow._

## À propos de l'intégration

L'intégration entre Braze et Snowplow permet aux utilisateurs de transmettre les événements de Snowplow à Braze par l'intermédiaire des tags côté serveur de Google Tag Manager. La balise Braze pour Snowplow vous permet d'envoyer des événements à Braze tout en offrant une flexibilité et un contrôle supplémentaires :
- Visibilité totale de toutes les transformations sur les données.
- Capacité d'évolution de la sophistication au fil du temps
- Toutes les données restent dans votre cloud privé jusqu'à ce que vous décidiez de les transmettre
- Facilité de configuration grâce aux riches bibliothèques d'étiquettes et à l'interface utilisateur familière de Google Tag Manager.

Exploitez les riches données comportementales de Snowplow pour favoriser de puissantes interactions centrées sur le client dans Braze et diffuser des messages personnalisés en temps réel.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Pipeline Snowplow | Un pipeline Snowplow doit être opérationnel. |
| Google Tag Manager côté serveur | GTM-SS doit être déployé et le [client Snowplow pour GTM-SS][2] doit être configuré. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][3] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

### Une distribution personnalisée et axée sur l'action
Utilisez l'un des nombreux événements riches que Snowplow collecte par défaut, ou définissez des événements personnalisés pour façonner des parcours clients encore plus précis adaptés à votre entreprise. Exploitez les données comportementales de Snowplow pour concevoir des tunnels de clients et débloquer de la valeur pour vos équipes marketing et produits, en les aidant à maximiser la conversion et l'utilisation des produits par le biais de Braze.

### Segmentation dynamique
Créez des audiences dynamiques dans Braze sur la base des données comportementales de haute qualité de Snowplow : Lorsque les utilisateurs effectuent des actions dans votre produit, application ou site web, vous pouvez exploiter les données comportementales en temps réel que Snowplow collecte pour ajouter ou supprimer automatiquement des utilisateurs des segments pertinents dans Braze.

## Intégration

### Étape 1 : Installation du modèle

#### Installation manuelle

1. Téléchargez le fichier modèle [`template.tpl`][7].
2. Créez une nouvelle balise dans la section **Modèles** d'un conteneur de serveur Google Tag Manager.
3. Cliquez sur le menu **Autres actions** dans le coin supérieur droit et sélectionnez **Importer.**
4. Importez votre fichier de modèle téléchargé et enregistrez-le.

#### Galerie du gestionnaire des étiquettes

Bientôt disponible ! Cette balise est en attente d'approbation pour être incluse dans la galerie GTM.

### Étape 2 : Configuration de l'étiquette Braze

Une fois le modèle installé, ajoutez la balise Braze à votre conteneur GTM-SS.

1. Dans l'onglet **Balise**, sélectionnez **Nouveau**, puis sélectionnez le **Balise Braze** comme configuration de balise.
2. Sélectionnez le déclencheur de votre choix pour les événements que vous souhaitez transmettre à Braze.
3. Saisissez les paramètres requis et configurez votre étiquette (vous trouverez plus de détails dans la section Personnalisation suivante).
4. Cliquez sur **Enregistrer**.

## Personnalisation

### Paramètres requis pour les balises

Le tableau suivant répertorie les paramètres requis que vous devez inclure dans la configuration de votre balise Braze.

| Paramètres | Description |
| --------- | ----------- |
| Point d'endpoint de l'API REST de Braze | Indiquez l'URL de votre [endpoint][3] REST Braze. |
| Clé API de Braze | Indiquez votre [clé API][4] Braze qui sera incluse dans chaque requête. |
| `external_id` Braze | Définissez cette clé sur la propriété d'événement du client qui correspond à l'adresse `external_id` de vos utilisateurs et qui sera utilisée comme [identifiant de l'utilisateur de Braze][5]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mappage d'événements

Le tableau suivant énumère les options de mappage d'événements concernant l'événement Snowplow tel qu'il est revendiqué par le [client Snowplow][2].

| Option de mappage | Description |
| --------- | ----------- |
| Inclure une description de l'événement | Activé par défaut. Indique si les données d'auto-description de l'événement Snowplow seront incluses dans les objets de propriétés de l'événement envoyés à Braze. |
| Règles relatives au contexte de l'événement Snowplow | Décrit comment la balise Braze utilisera les entités contextuelles attachées à un événement Snowplow. |
| Extraire une entité d'un tableau s'il n'y a qu'un seul élément | Les entités Snowplow sont toujours dans des tableaux, car plusieurs entités peuvent être attachées à un événement. Cette option sélectionne l'élément unique du tableau si celui-ci ne contient qu'un seul élément. |
| Inclure toutes les entités dans l'objet de l'événement | Activé par défaut. Inclut toutes les entités d'un événement dans l'objet des propriétés d'un événement Braze. Désactivez cette option pour sélectionner des entités individuelles à inclure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mappage d'événements avancé

#### Propriétés d'événement

Si vous souhaitez inclure d'autres propriétés de l'événement client et les mapper sur l'événement Braze, référez-vous aux règles du tableau suivant : 

| Propriétés d'événement | Description |
| --------- | ----------- |
| Inclure les propriétés d'événement communes | Activée par défaut, cette option permet d'inclure automatiquement les propriétés de l'événement de la [définition commune de l'événement][6] dans les propriétés de l'événement Braze. |
| Règles supplémentaires de mappage des propriétés utilisateur et des propriétés d'événement | Indiquez la clé de propriété de l'événement client et la clé d'objet des propriétés que vous souhaitez mapper (ou laissez la clé mappée vide pour conserver le même nom). Vous pouvez utiliser la notation du chemin d'accès (par exemple, `x-sp-tp2.p` pour une plateforme d'événements Snowplow ou `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` pour un ID de vue de page d'événements Snowplow (dans l'index de tableau 0) ou choisir des propriétés d'autres sources que Snowplow si vous utilisez un autre client.<br><br>Les règles de mappage des propriétés d'événement alimentent l'objet propriétés d'événement de Braze.|
| Inclure les propriétés communes des utilisateurs| Activée par défaut, cette option permet d'inclure ou non les propriétés `user_data` de la définition de l'événement commun dans l'objet attribut utilisateur Braze.|
| Propriété de l’heure de l'événement | Cette option vous permet de spécifier la propriété d'événement du client pour renseigner l'heure de l'événement (au format ISO-8601) ou de la laisser vide pour utiliser l'heure actuelle (comportement par défaut). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mappage des entités

À l'aide de la table de mappage des entités de Snowplow, les entités peuvent être remappées pour porter des noms différents dans Braze et être incluses dans les propriétés d'événement ou les objets d'attributs d'utilisateur. 

L'entité peut être spécifiée dans deux formats différents :
- Correspondance avec la version majeure : `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` où `com_snowplowanalytics_snowplow` est le fournisseur de l'événement, `web_page` est le nom du schéma et `1` est le numéro de la version majeure. `x-sp-` peut également être omis si vous le souhaitez.
- Correspondance complète du schéma : `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Option de mappage des entités | Description |
| --------- | ----------- |
| Inclure les entités non mappées dans l'événement | Lors du remappage ou du déplacement de certaines entités vers des attributs utilisateur avec la personnalisation précédente, cette option vous permet de vous assurer que toutes les entités non mappées (telles que toutes les entités non trouvées dans les [règles de propriété de l'](#event-property-rules)événement) seront incluses dans l'objet personnalisé de l'événement Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
