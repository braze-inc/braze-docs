---
nav_title: Tealium pour Currents
article_title: Tealium pour Currents
page_order: 2.3
alias: /partners/tealium_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Tealium, une plateforme de données client qui recueille et achemine des informations entre les différentes sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Tealium pour Currents

> [Tealium](https://www.tealium.com) est une plateforme de données client qui collecte et transfère des informations issues de plusieurs sources vers divers emplacements de votre pile marketing.

L’intégration de Braze et de Tealium permet de contrôler de manière harmonieuse le flux d’informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à Tealium pour les rendre utilisables sur toute la pile d’outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Tealium EventStream et/ou Tealium AudienceStream | Un [compte Tealium](https://my.tealiumiq.com/) est nécessaire pour tirer parti de ce partenariat. |
| Currents | Pour réexporter des données dans Tealium, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| URL de Tealium | Pour obtenir cette URL, accédez à votre tableau de bord Tealium et copiez l’URL d’ingestion.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une source de données pour Braze dans Tealium

Des instructions expliquant comment créer une source de données sont disponibles sur le site Web de [Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Braze-Currents-Incoming-Webhook-Setup-Guide/ta-p/36303). Une fois terminé, Tealium fournira une URL de source de données à copier et que vous utiliserez à l’étape suivante.

### Étape 2 : Créer un Current

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Tealium Export (Exportation Tealium)**. Fournissez un nom d’intégration, une adresse e-mail de contact et votre URL Tealium. Ensuite, sélectionnez les événements que vous souhaitez suivre dans la liste des événements disponibles. Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

Tous les événements envoyés à Tealium incluront l’`external_user_id` de l’utilisateur. À l’heure actuelle, Braze n’envoie pas de données d’événements à Tealium aux utilisateurs qui n’ont pas d’`external_user_id` défini.

{% alert important %}
Il est important de tenir votre URL Tealium à jour. Si l’URL de votre connecteur est incorrecte, Braze ne pourra pas envoyer d’événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

## Détails de l’intégration

Braze prend en charge l’exportation de toutes les données répertoriées dans les [glossaires d’événements Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#nav_top_dataandanalytics_brazec urrents_eventglossary) (y compris toutes les propriétés des événements d’[engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) et de [comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/)) vers Tealium.
