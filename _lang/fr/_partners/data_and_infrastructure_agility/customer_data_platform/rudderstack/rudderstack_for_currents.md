---
nav_title: RudderStack pour Currents
article_title: RudderStack pour Currents
description: "Cet article présente le partenariat entre Currents Braze et RudderStack, une infrastructure open source de données client qui offre une intégration transparente de Braze pour vos applications Android, iOS et Web."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# RudderStack pour Currents

> [RudderStack](https://www.rudderstack.com/) vous permet de recueillir, de transformer et d’activer vos données client sur l’ensemble de votre pile, en tirant parti de votre entrepôt de données cloud comme source centrale de vérité. Cet article donne un aperçu de la configuration d’une connexion entre Currents Braze et RudderStack.

L’intégration de Braze et RudderStack vous permet de tirer parti de Currents Braze pour exporter vos événements Braze vers RudderStack afin de générer des analyses plus approfondies.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte RudderStack | Un [compte Rudderstack](https://app.rudderstack.com/login) est requis pour profiter de ce partenariat. |
| Utiliser Braze en tant que destination | Nous vous suggérons d’avoir [installé Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) à RudderStack. |
| Currents | Pour réexporter des données dans mParticle, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une source de données pour Braze dans RudderStack

Tout d’abord, vous devez créer une source Braze sur l’application Web RudderStack. Des instructions expliquant comment créer une source de données sont disponibles sur le site Web de [RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Une fois terminé, RudderStack fournira une URL webhook, y compris la clé d’écriture, que vous devrez utiliser à l’étape suivante. Vous pouvez trouver l’URL Webhook dans l’onglet **Settings (Paramètres)** de votre source Braze.

### Étape 2 : Créer un Current

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > RudderStack Export (Exportation RudderStack)**. Indiquez un nom d’intégration, un e-mail de contact, l’URL du webhook RudderStack (qui va dans le champ de clé) et la région RudderStack. 

### Étape 3 : Exporter les événements

Ensuite, sélectionnez les événements que vous souhaitez exporter. Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

Tous les événements envoyés à RudderStack incluront l’`external_user_id` de l’utilisateur. À l’heure actuelle, Braze n’envoie pas de données d’événements à RudderStack concernant les utilisateurs qui n’ont pas d’`external_user_id` défini.

## Détails de l’intégration

Braze prend en charge l’exportation de toutes les données répertoriées dans les [glossaires d’événements Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) vers RudderStack.
