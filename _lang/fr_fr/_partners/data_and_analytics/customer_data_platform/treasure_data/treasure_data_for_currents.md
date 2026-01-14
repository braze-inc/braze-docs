---
nav_title: Treasure data pour Currents
article_title: Treasure data pour Currents
description: "Cet article de référence présente le partenariat entre Braze Currents et Treasure Data, une plateforme de données client d'entreprise qui vous permet d'écrire les résultats des travaux directement dans Braze."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure data pour Currents

> [Treasure Data](https://www.treasuredata.com/) est une plateforme de données client (CDP) qui collecte et achemine des informations provenant de sources multiples vers divers autres emplacements de votre pile marketing.

L'intégration de Braze et Treasure Data vous permet de contrôler de façon fluide le flux d'informations entre les deux systèmes. Avec Currents, vous pouvez également connecter les données à Treasure Data pour les rendre exploitables dans l'ensemble des outils de croissance.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Données sur les trésors | Un [compte Treasure Data](https://console.treasuredata.com/users/sign_in) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour exporter des données dans Treasure Data, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| URL de Treasure data | Vous pouvez l'obtenir en naviguant vers votre tableau de bord Treasure Data et en copiant l'URL d'ingestion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Treasure data enregistre chaque événement par lots. Pour plus d'informations sur la manière d'interroger Treasure Data pour obtenir des comptes d'événements, reportez-vous à [Intégration de l'importation de Braze Currents](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration).
{% endalert %}

## Intégration

Il est conseillé pour se connecter à Treasure Data d’utiliser l'API Postback. Cette méthode ne nécessite pas de connecteur par défaut et les données peuvent être reçues par une approche de type "notifications push". Tous les événements envoyés dans un lot de données se trouvent à l'intérieur d'un champ d'une ligne dans un tableau JSON, qui doit être analysé pour obtenir les données requises.

{% alert important %}
L'ingestion de données par le collecteur d'événements ne se fait pas en temps réel et peut prendre jusqu'à cinq minutes.
{% endalert %}

### Étape 1 : Configuration de l'API Treasure Data Postback avec Braze

Vous trouverez des instructions pour la création d'une API Postback sur le [site web de Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). Braze enverra directement les événements mis à jour à Treasure Data en temps réel, à l'exception de l'ingestion via event-collector. Une fois l'opération terminée, Treasure data fournira une URL de source de données à copier pour l'utiliser à l'étape suivante.

### Étape 2 : Créer un flux Currents

Dans Braze, naviguez vers **Currents** > **\+ Create un flux Currents** > **Export Treasure Data**. Indiquez un nom d'intégration, un e-mail de contact et l'URL de vos données. Ensuite, sélectionnez ce que vous voulez suivre dans la liste des événements disponibles et cliquez sur **Lancer le flux Currents**.

Tous les événements envoyés à Treasure data comprendront l'adresse `external_user_id` de l'utilisateur. À l'heure actuelle, Braze n'envoie pas de données d'événement à Treasure Data pour les utilisateurs qui n'ont pas réglé leur `external_user_id`.

{% alert important %}
Maintenez l'URL de votre Treasure data à jour. Si l'URL de votre connecteur est incorrecte, Braze ne pourra pas envoyer d'événements. Si cette situation persiste pendant plus de 48 heures, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

#### Exemple de valeur de champ d'événement
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Exemple de vue ingérée

![4]{: style="max-width:70%;"}

## Détails de l'intégration

Braze prend en charge l'exportation de toutes les données répertoriées dans les [glossaires d'événements de Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) (y compris toutes les propriétés des événements d'[engagement des messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) et de [comportement des clients]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ) vers Treasure Data.

La structure des données exportées est la même que celle des connecteurs HTTP personnalisés, qui peut être consultée dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
