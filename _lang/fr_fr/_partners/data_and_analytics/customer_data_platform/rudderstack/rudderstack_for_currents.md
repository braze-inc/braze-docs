---
nav_title: Rudderstack pour Currents
article_title: Rudderstack pour Currents
description: "Cet article présente le partenariat entre Braze Currents et RudderStack, une infrastructure de données client open-source qui offre une intégration fluide de Braze pour vos applications Android, iOS et web."
page_type: partner
tool: Currents
search_tag: Partner

---

# Rudderstack pour Currents

> [RudderStack](https://www.rudderstack.com/) vous permet de collecter, de transformer et d'activer les données de vos clients dans l'ensemble de votre pile, en exploitant votre entrepôt de données dans le cloud comme source centrale de vérité. Cet article explique comment connecter Braze Currents et Rudderstack.

L'intégration Braze et RudderStack vous permet de tirer parti de Braze Currents pour exporter vos événements Braze vers RudderStack afin de réaliser des analyses plus approfondies.

## Prérequis

| Condition | Description |
| --- | --- |
| Compte Rudderstack | Un [compte Rudderstack](https://app.rudderstack.com/login) est nécessaire pour bénéficier de ce partenariat. |
| Destination Braze | Nous vous suggérons de [configurer Braze comme destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) dans Rudderstack. |
| Currents | Pour exporter des données dans Rudderstack, vous devez configurer [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer une source de données pour Braze dans Rudderstack

Tout d'abord, vous devez créer une source Braze dans l'application web Rudderstack. Les instructions relatives à la création d'une source de données sont disponibles sur le site de [Rudderstack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Une fois terminé, Rudderstack fournira une URL de webhook, y compris la clé d'écriture, que vous devrez utiliser à l'étape suivante. Vous trouverez l'URL du webhook dans l'onglet **Paramètres** de votre source Braze.

### Étape 2 : Créer un flux Current

Dans Braze, naviguez vers **Currents > + Créer un flux Current > Export RudderStack**. Indiquez le nom de l'intégration, l'e-mail du contact, l'URL du webhook de Rudderstack (qui va dans le champ de la clé) et la région de RuddStack. 

### Étape 3 : Exporter des événements

Sélectionnez ensuite les événements que vous souhaitez exporter. Enfin, cliquez sur **Lancer le flux Current**

Tous les événements envoyés à Rudderstack comprendront l'adresse `external_user_id` de l'utilisateur. À l'heure actuelle, Braze n'envoie pas de données d'événement à Rudderstack pour les utilisateurs dont le `external_user_id` n'est pas configuré.

## Détails de l'intégration

Braze permet d'exporter vers Rudderstack toutes les données figurant dans les [glossaires des événements de Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/).

La structure des données exportées est la même que celle des connecteurs HTTP personnalisés, qui peut être consultée dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).