---
nav_title: Zeotap pour Currents
article_title: Zeotap pour Currents
description: "Cet article de référence présente le partenariat entre Braze Currents et Zeotap, une plateforme de données client de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile en fournissant une résolution d'identité, des informations et un enrichissement des données."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap pour Currents

> [Zeotap](https://zeotap.com/) est une plateforme de données clients de nouvelle génération qui vous aide à découvrir et à comprendre votre audience mobile grâce à des outils de résolution d'identité, des informations exploitables et des données enrichies.

L'intégration entre Braze et Zeotap vous permet d'étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap avec les profils d'utilisateurs de Braze. Avec [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), vous pouvez également connecter les données à Zeotap pour les rendre exploitables dans l'ensemble des outils de croissance.

{% alert important %}
Le connecteur HTTP personnalisé est actuellement en version bêta. Si vous souhaitez gérer cette intégration, contactez votre gestionnaire de satisfaction client.
{% endalert %}

## Conditions préalables

| Condition | Descriptif |
| --- | --- |
|Compte Zeotap | Un [compte Zeotap](https://zeotap.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour exporter des données dans Zeotap, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Mise en œuvre

### Étape 1 : Créer une source de courants

1. Dans Zeotap, allez dans **Sources** sous **Intégrer**.
2. Sélectionnez **Créer une source**.
3. Sélectionnez les **canaux d'engagement client** comme catégorie.<br><br>![Une fenêtre "Créer une source" répertoriant différentes catégories, dont "Canaux d'engagement client".][1]{: style="max-width:70%;"}<br><br>
4. Sélectionnez **Braze** comme source de données.
5. Saisissez un nom de source.
6. Sélectionnez votre région.<br><br>![Fenêtre avec options de sélection de votre région et de l'entité de données.][6]{: style="max-width:70%;"}<br><br>
7. Sélectionnez **Créer une source**.
8. Accédez à l'onglet **Détails de la mise en œuvre** et notez l'**URL de l'API** et la **clé d'écriture**.<br><br>![Détails de la mise en œuvre pour Braze Currents qui contient l'URL de l'API et la clé d'écriture.][2]

### Étape 2 : Configurer le flux de données en continu dans Currents

1. Dans Braze, allez dans **Intégrations partenaires** > **Exportation de données**.
2. Sélectionnez **Créer un nouveau courant** et **Exporter des courants personnalisés**.<br><br>![Le bouton "Créer un nouveau courant" avec un menu déroulant qui contient "Exportation de courants personnalisés".][3]{: style="max-width:60%;"}<br><br>
3. Saisissez un nom d'intégration et un e-mail pour être contacté en cas d'erreurs avec l'intégration.
4. Sous **Credentials**, entrez les informations suivantes que vous avez notées à l'[étape 1 :](#step-1-create-a-currents-source)
- L'URL de l'API comme **endpoint**
- La clé d'écriture comme **jeton porteur**<br><br>![Sections permettant de saisir les détails de l'intégration et les informations d'identification.][4]<br><br>
5. Sélectionnez les événements engagement lié aux messages que vous souhaitez envoyer à Zeotap.<br><br>![L'onglet "Paramètres généraux" comporte une section permettant de sélectionner les événements d'engagement aux messages.][5]
6. Sélectionnez **Lancer le courant** pour enregistrer les modifications et commencer à envoyer des événements à Zeotap.

{% alert important %}
Le connecteur Currents ne prend pas en charge les utilisateurs anonymes (utilisateurs sans `external_id`).
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}