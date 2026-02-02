---
nav_title: Snowplow
article_title: Snowplow
description: "Cet article de référence présente le partenariat entre Braze et Snowplow, une plateforme d'infrastructure de données, qui vous permet de transmettre les événements Snowplow à Braze en temps réel grâce à l'Event Forwarding de Snowplow."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) est une plateforme évolutive pour la collecte de données riches, de haute qualité et à faible latence. Snowplow est conçu pour collecter des données comportementales complètes et de haute qualité pour les entreprises.

_Cette intégration est maintenue par Snowplow._

## À propos de l'intégration

L'intégration entre Braze et Snowplow vous permet de transmettre en temps réel les événements de Snowplow à Braze en utilisant la solution Event Forwarding de Snowplow. Cette intégration vous permet d'envoyer des événements à Braze tout en offrant flexibilité et contrôle. Plus précisément, vous pouvez :
- Filtrez et transformez les événements avant de les envoyer à Braze.
- Mappez les données des événements de Snowplow aux attributs des utilisateurs de Braze, aux événements personnalisés et aux achats.
- Conservez toutes les données dans votre cloud privé jusqu'à ce que vous décidiez de les transmettre.
- Déployez vous-même la solution au sein de votre compte Snowplow. 

Le [transfert d'événements de](https://docs.snowplow.io/docs/destinations/forwarding-events/) Snowplow est une fonctionnalité supplémentaire payante disponible pour les clients de Snowplow. Pour transmettre des événements à Braze sans ce module complémentaire, utilisez l' [intégration](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) côte à côte serveur de Google Tag Manager de Snowplow.

Exploitez les riches données comportementales de Snowplow pour favoriser de puissantes interactions centrées sur le client dans Braze et diffuser des messages personnalisés en temps réel.

## Conditions préalables

| Condition             | Description                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pipeline Snowplow       | Vous avez besoin d'un pipeline de chasse-neige opérationnel.                                                                                                                                                                                                                                          |
| Accès à la console du chasse-neige | Vous devez avoir accès à la console Snowplow pour configurer les transferts d'événements.                                                                                                                                                                                                                                |
| Clé d'API REST Braze      | Une clé API REST de Braze avec les autorisations suivantes : `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename`, et `users.alias.update`. <br><br> Vous pouvez la créer dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST Braze     | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

### Une distribution personnalisée et axée sur l'action
Utilisez l'un des nombreux événements riches que Snowplow collecte par défaut, ou définissez des événements personnalisés pour façonner des parcours clients encore plus précis adaptés à votre entreprise. Exploitez les données comportementales de Snowplow pour concevoir des tunnels de clients et débloquer de la valeur pour vos équipes marketing et produits, en les aidant à maximiser la conversion et l'utilisation des produits par le biais de Braze.

### Segmentation dynamique
Créez des audiences dynamiques dans Braze sur la base des données comportementales de haute qualité de Snowplow : Lorsque les utilisateurs effectuent des actions dans votre produit, application ou site web, vous pouvez exploiter les données comportementales en temps réel que Snowplow collecte pour ajouter ou supprimer automatiquement des utilisateurs des segments pertinents dans Braze.

## Intégration

### Étape 1 : Configurez la destination dans la console chasse-neige

Pour créer le transitaire d'événements :

1. Dans la console chasse-neige, naviguez vers **Destinations** et sélectionnez **Créer une nouvelle destination**.
2. Lors de la configuration de la connexion, sélectionnez **Braze** pour le type de connexion.
3. Saisissez votre clé API Braze et le point d'endpoint de l'API REST.
4. Enregistrez la connexion.

### Étape 2 : Configurer le redirecteur d'événements

Lors de la configuration du transitaire, vous pouvez choisir les événements Snowplow à transférer et les mapper à des types d'objets Braze :

1. **[Attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: Mettre à jour les données du profil utilisateur et les propriétés personnalisées de l'utilisateur.
2. **[Événements personnalisés]({{site.baseurl}}/api/objects_filters/event_object)**: Envoyez les actions et les comportements des utilisateurs.
3. **[Achats]({{site.baseurl}}/api/objects_filters/purchase_object)**: Envoyez les données de la transaction avec les détails du produit.

Pour chaque type d'objet, vous pouvez configurer les mappages de champs afin de spécifier comment les données d'événement de Snowplow sont mappées aux champs de Braze. Consultez la [documentation de](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) Snowplow [sur la création de transitaires](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) pour obtenir des instructions détaillées sur la configuration et le mappage des champs.

### Étape 3 : Valider l'intégration

Confirmez que les événements atteignent Braze en consultant les pages suivantes de votre compte Braze :

1. **Générateur de requêtes**: Dans Braze, accédez à **Analyse/analytique** > **Générateur de requêtes (**si utilisé en tant qu'adjectif). Vous pouvez écrire des requêtes sur les tables suivantes pour avoir un aperçu des données transmises par Snowplow : `USER_BEHAVIORS_CUSTOMEVENT_SHARED` et `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **Tableau de bord de l'utilisation de l'API**: Dans Braze, accédez à **Paramètres** > **API et identifiants** pour voir un graphique de l'utilisation des API au fil du temps. Vous pouvez filtrer spécifiquement pour la clé API que Snowplow utilise et voir les succès et les échecs.

## Envoi de propriétés personnalisées

Vous pouvez envoyer des propriétés personnalisées en plus des champs standard. La structure dépend du type d'objet Braze que vous utilisez :

- **Attributs de l'utilisateur**: Ajouter comme champs de premier niveau (par exemple, `subscription_tier`, `loyalty_points`)
- **Propriétés d'événement**: Emboîtement sous l'objet `properties` (par exemple, `properties.plan_type`, `properties.feature_flag`)
- **Propriétés d'achat**: Emboîtement sous l'objet `properties` (par exemple, `properties.color`, `properties.size`)

Pour les noms de propriétés contenant des espaces, utilisez la notation entre crochets (par exemple, `["account type"]` ou `properties["campaign source"]`).

Consultez la [documentation sur les objets événements]({{site.baseurl}}/api/objects_filters/event_object) pour plus de détails sur les types de données pris en charge, les exigences en matière de dénomination des propriétés et les limites de taille de la charge utile.

## Restrictions

**Limites de débit :** Braze applique une limite de débit de 3 000 appels API toutes les trois secondes pour l'API de suivi des utilisateurs. Étant donné que Snowplow ne prend pas en charge la mise en lots pour les transitaires d'événements, cette limite de débit de l'API fonctionne également comme limite de débit de l'événement. Si votre débit d'entrée dépasse 3 000 événements par trois secondes, vous risquez de constater une augmentation de la latence.
