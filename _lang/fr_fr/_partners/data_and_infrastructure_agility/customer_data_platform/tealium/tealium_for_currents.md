---
nav_title: Tealium pour Currents
article_title: Tealium pour Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et Tealium, une plateforme de données client qui collecte et achemine les données entre les sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium pour Currents

> [Tealium](https://www.tealium.com) est une plateforme de données clients qui collecte et achemine des données provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et Tealium vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à Tealium afin de les exploiter dans la suite des outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Tealium Eventstream ou Tealium Audiencestream | Un [compte Tealium](https://my.tealiumiq.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données vers Tealium, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| URL de Tealium | Vous pouvez les obtenir en vous rendant sur votre tableau de bord Tealium et en copiant l'URL d'ingestion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créez une source de données pour Braze dans Tealium

Les instructions pour créer une source de données sont disponibles sur le site de [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/). Une fois terminé, Tealium vous fournira une URL de source de données à copier, que vous utiliserez à l'étape suivante.

### Étape 2 : Créer un flux Currents

Dans Braze, naviguez vers **Currents > + Créer un flux Currents > Export Tealium**. Indiquez un nom d'intégration, un e-mail de contact et l'URL de Tealium. Sélectionnez ensuite l'événement que vous souhaitez suivre dans la liste des événements disponibles. Enfin, cliquez sur **Lancer le flux Currents**

Tous les événements envoyés à Tealium comprendront l'adresse `external_user_id` de l'utilisateur. Pour l'instant, Braze n'envoie pas de données d'événement à Tealium pour les utilisateurs qui n'ont pas défini leur `external_user_id`.

{% alert important %}
Il est important de maintenir votre URL Tealium à jour. Si l'URL de votre connecteur est incorrecte, Braze ne pourra pas envoyer d'événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Détails de l'intégration

Braze prend en charge l'exportation vers Tealium de toutes les données répertoriées dans les [glossaires d'événements de Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (y compris toutes les propriétés des événements d'[engagement d'un message]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) et de [comportement des clients]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ).

La structure des données exportées est la même que celle des connecteurs HTTP personnalisés, qui peut être consultée dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).