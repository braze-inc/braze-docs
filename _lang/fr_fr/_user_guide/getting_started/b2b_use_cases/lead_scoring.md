---
nav_title: Notation des prospects
article_title: "Création d'un flux de travail pour l'évaluation des prospects"
page_order: 1
page_type: reference
description: "Apprenez à utiliser Braze pour réaliser des évaluations simples de prospects, des évaluations externes de prospects et des transferts de prospects."
---

# Création d'un flux de travail pour l'évaluation des prospects

> Ce cas d'utilisation montre comment vous pouvez utiliser Braze pour mettre à jour les scores des leads des utilisateurs en temps réel et transmettre automatiquement les leads à vos équipes de vente.

La création d'un flux de travail de notation des prospects dans Braze se fait en deux étapes clés :

1. Créez un canvas de notation des prospects dans Braze ou intégrez un outil externe de notation des prospects :
- [Un système simple d'évaluation des prospects](#simple-lead-scoring)
- [Evaluation externe des prospects](#external-lead-scoring)

2. Créez une campagne webhook pour envoyer des prospects qualifiés à votre équipe de vente :
- [Transfert de prospects : des prospects qualifiés en marketing (MQL) aux ventes](#lead-handoff)

## Un système simple d'évaluation des prospects

### Étape 1 : Créer un Canvas

1. Allez dans **Messagerie** > **Canvas** et sélectionnez **Créer un Canvas**, puis remplissez les bases de votre Canvas.

2. Donnez à votre canvas un nom pertinent, tel que « Canvas de notation des prospects » et, pour le retrouver facilement, apposez-lui une étiquette mentionnant par exemple « Gestion des prospects ».<br><br>![Première étape de la création d'un canvas nommé "Lead Scoring Canvas" et portant l'étiquette "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Étape 2 : Définissez vos critères d'entrée

1. Passez à l'étape **Planification d’entrée** et sélectionnez une planification d’entrée **par événement**. Cela permettra aux utilisateurs d'entrer dans le Canvas lorsqu'ils effectueront des actions spécifiques.

2. Dans **Options basées sur l'action**, ajoutez ces deux actions :
    - **Remplacez la valeur de l'attribut personnalisé** par le nom de votre attribut d'évaluation des prospects (par exemple `lead score`). Si vous n'avez pas encore créé d'attribut de lead scoring, suivez les étapes de la section [Attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). Ceci permet aux utilisateurs d'entrer dans le canvas chaque fois que leur notation de prospect change.
    - **Ajouter une adresse e-mail**

![Deuxième étape de la création d'un canvas avec la planification d'entrée "Basé sur l'action" et les options basées sur l'action de modification d'un attribut personnalisé "lead score" et d'ajout d'une adresse e-mail.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Étape 3 : Identifiez votre audience cible

#### Étape 3a : Sélectionner des segments

Tous les utilisateurs sont éligibles pour le lead scoring, vous pouvez donc ajouter des règles spécifiques à l'entreprise concernant les personnes à scorer en sélectionnant les [segments d']({{site.baseurl}}/user_guide/engagement_tools/segments/) utilisateurs à cibler et en appliquant des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) supplémentaires. Par exemple, vous pouvez exclure les employés, les utilisateurs qui sont déjà clients, etc. 

![Troisième étape de la création d'un canvas avec des options de sélection de segments et de filtres pour restreindre l'audience d'entrée.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Étape 3b : Rééligibilité des toiles de canevas

Un utilisateur passera par ce Canvas de nombreuses fois au cours de son cycle de vie avec vous, assurez-vous donc qu'il puisse y revenir aussi rapidement qu'il en est sorti la fois précédente. Ceci peut se faire par le biais de paramètres de rééligibilité. 

Dans les **contrôles d'entrée**, procédez comme suit :
- Sélectionnez **Autoriser les utilisateurs à saisir à nouveau cette toile.**
- Sélectionnez **Fenêtre spécifiée**.
- Définissez la rééligibilité sur 0 **seconde**.

![La section "Contrôles d'entrée" comporte des sélections pour "Autoriser les utilisateurs à entrer à nouveau dans ce canvas" dans une "fenêtre spécifiée" de 0 seconde.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Étape 3c : Mettez à jour les paramètres d'envoi

Étant donné la nature opérationnelle de ce Canvas et le fait qu'aucun message ne sera envoyé à ces utilisateurs, vous n'avez pas besoin de respecter les statuts d'abonnement.

Sous **Paramètres d'abonnement**, pour **Envoyer à ces utilisateurs :** sélectionnez **tous les utilisateurs, y compris les utilisateurs désabonnés**. 

![Étape 4 de la création d'un Canvas pour la définition des options d'envoi des messages.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Étape 4 : Créer votre Canvas

#### Étape 4a : Ajouter un parcours d'action

Sous votre variante, cliquez sur l'icône plus, puis sélectionnez **Parcours d'action**.

![Canvas avec "parcours d'action" s'affichant dans le menu ouvert par l'icône plus.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Étape 4b : Créer des groupes d'action

Chaque groupe d'action représentera toutes les actions qui conduisent à l'incrémentation ou à la décrémentation du même point. Vous pouvez définir jusqu'à huit groupes d'action. Dans ce scénario, nous allons créer quatre groupes.

Ajoutez les groupes suivants à votre parcours d'action :

- **Groupe 1 :** Tous les événements qui comptent pour un incrément de 1 point.
- **Groupe 2 :** Tous les événements qui comptent pour un incrément de 5 points.
- **Groupe 3 :** Tous les événements qui comptent pour un décrément de 1 point.
- **Tous les autres :** Les parcours d'action vous permettent de définir la fenêtre d'attente pour voir si un utilisateur entreprend une action, avant de le placer dans un groupe "tous les autres". Pour la notation des prospects, c'est l'occasion d’abaisser le score pour « inactivité ».

![Parcours d'action contenant des groupes d'action pour ajouter un point, cinq points et dix points ; soustraire un point et dix points ; et "Tous les autres".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %})

#### Étape 4c : Configurez chaque groupe pour y inclure les événements pertinents

Dans chaque groupe d'action, sélectionnez **Sélectionner un déclencheur** et choisissez l'événement qui ajoutera le nombre de points pour ce groupe d'action particulier. Ajoutez d'autres déclencheurs pour inclure tous les événements qui incrémenteront le score du lead d'une unité. Par exemple, un utilisateur pourrait incrémenter son score d'une unité lorsqu'il démarre une session dans n'importe quelle app ou effectue un événement personnalisé (comme s'inscrire ou rejoindre un webinaire). 

![Groupe d'applications pour l'ajout d'un point avec les déclencheurs "Démarrer une session dans n'importe quelle application" et "Effectuer un événement personnalisé".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Étape 4d : Ajoutez des étapes Mise à jour utilisateur

Ajoutez une étape de mise à jour de l'utilisateur à chaque parcours canvas créé sous votre chemin d'action. 

![Canevas affichant le parcours d'action avec des chemins de mise à jour de l'utilisateur ramifiés pour chaque groupe d'action.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
Dans l'onglet **Composer de** chaque étape de mise à jour de l'utilisateur, procédez comme suit pour les champs respectifs :

| Champ | Action |
| --- | --- |
| **Nom de l’attribut** | Sélectionnez l'attribut de notation des prospects que vous avez sélectionné à l'étape 2 (`lead score`).|
| **Action** | Changez l'action en **Incrémenter par** si le parcours augmente le score ou **Décrémenter par** si le parcours diminue le score. |
| **Incrémenter par** ou **décrémenter par** | Saisissez le nombre de points qui seront augmentés ou diminués par rapport à la note de référence.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 5 : Lancez votre Canvas

C'est tout ! Votre canevas d'évaluation des prospects est prêt à être lancé.

## Evaluation externe des prospects

Que vous utilisiez l'un de nos [partenaires technologiques]({{site.baseurl}}/partners/home/), votre propre modèle interne de scoring des leads, l'apprentissage automatique ou un autre outil de scoring des leads, nous avons de multiples options pour vous.

### Partenaires externes

Consultez la rubrique [Partenaires technologiques]({{site.baseurl}}/partners/home) pour en savoir plus sur nos partenaires B2B qui proposent des fonctionnalités de notation des prospects. Votre outil n'y figure pas ? Vous pouvez l'intégrer en appelant notre endpoint d’API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users). 

### Modèles de données internes pour l'évaluation des prospects

Vous pouvez intégrer Braze à vos modèles de données internes, y compris les modèles de notation des prospects, de différentes manières. Vous trouverez ci-dessous quelques exemples personnalisés d'intégration de Braze par nos clients.

#### Entrepôt de données en nuage intégré

{% tabs %}
{% tab Braze comme source de données %}

En tant qu'outil marketing, Braze contient des données extrêmement pertinentes qui pourraient compléter le modèle interne de score des prospects de votre équipe. 

Par exemple, les données d'engagement des messages (telles que les ouvertures et les clics d'e-mail, l'engagement des pages de renvoi et autres) peuvent déterminer le niveau d'engagement d'un lead. Vous pouvez retransmettre ces données à votre entrepôt de données en nuage et les mettre à disposition en tant que données d'entrée pour vos modèles d'évaluation des prospects en utilisant les solutions de flux de données en continu de Braze :

- [Currents Braze]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Partage sécurisé des données avec Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze en tant que destination %}

Une fois que vos équipes internes ont créé et exécuté votre modèle d'évaluation des prospects, vous pouvez récupérer ces données dans Braze afin de mieux segmenter et cibler les prospects pour leur envoyer des messages pertinents. Vous pouvez le faire avec [Cloud Data Ingestion de Braze]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

Avec Cloud Data Ingestion, vos équipes internes créeront un nouveau tableau ou une nouvelle vue avec vos identifiants d'utilisateur, les derniers scores des prospects et les horodatages de mise à jour des scores. Braze reprendra le tableau ou la vue et ajoutera les scores des prospects aux profils utilisateurs.

{% endtab %}
{% endtabs %}

## Transfert de prospects : des prospects qualifiés en marketing (MQL) aux ventes {#lead-handoff}

L'approche que nous recommandons pour les transferts de prospects consiste à associer un prospect ou un contact à chaque utilisateur dans Braze. Ces prospects entrent alors dans la file d'attente de vos équipes de vente lorsque leur statut passe à l'étape MQL. Salesforce lance alors un workflow d'acheminement ou d'affectation des prospects. 

Pour mettre à jour l'enregistrement du prospect dans Salesforce avec le statut du prospect provenant de Braze, nous vous recommandons d'utiliser un modèle de webhook déclenché.

### Étape 1 : Créez une campagne webhook

### Étape 2 : Configurez votre webhook

#### Étape 2a : Composer un webhook

1. Donnez un nom à votre campagne webhook, par exemple « Salesforce > Mise à jour de prospect en MQL ».

2. Saisissez l'URL de votre webhook au format {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. L'ID utilisateur de Braze ( {% raw %}`{{$user_id}}}`{% endraw %} ) doit correspondre à votre ID de contact Salesforce. Si ce n'est pas le cas, utilisez un alias au lieu de {% raw %}`{{$user_id}}}`{% endraw %}.

3. Mettez à jour la **méthode HTTP** en la remplaçant par **PATCH**.

4. Configurez votre charge utile pour qu'elle mette à jour l'enregistrement du prospect dans Salesforce uniquement si le score de ce prospect dépasse le seuil prédéfini. Voir l'exemple de corps de demande ci-dessous pour un score de prospect supérieur à 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Incluez les en-têtes suivants :

| En-tête | Contenu |
| --- | --- |
| Autorisation | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Pour récupérer un jeton, [configurez une appli connectée](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) pour le flux d’identifiants du client OAuth 2.0, puis utilisez le contenu connecté pour récupérer le porteur dans Salesforce : <br><br>{% raw %}<code>{% connected_content <mem_3a6f2257-5115-4593-80a1-14f17e6384a5/>[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]_mem_amp_client_secret=[client_secret]_mem_amp_grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Type_de_contenu | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Webhook composé d'une URL de webhook Salesforce, d'une méthode HTTP PATCH, d'un corps de requête en texte brut et d'en-têtes de requête.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Étape 2b : Planification des envois de webhooks

La campagne doit se déclencher à chaque fois que le score de l'utilisateur change. Cette campagne se déclenchera pour tout utilisateur dont le score change, mais elle n'affectera que les utilisateurs qui ne sont pas actuellement un MQL et qui ont franchi le seuil que vous avez défini à l'étape précédente.

Dans l'étape **Planifier la réception/distribution**, sélectionnez les éléments suivants :
- Un type de **réception/distribution basé sur l'action** 
- Une action de déclenchement de **Changer la valeur de l'attribut personnalisé** avec le nom de votre attribut de lead scoring et une action de **toute nouvelle valeur.**

#### Étape 2c : Identifiez l'audience cible

Dans l'étape **Audiences cibles**, incluez un filtre qui exclut les utilisateurs dont le statut de prospect est déjà au niveau MQL ou au-delà, par exemple « `lead_status` `is none of` `MQL` ».

![Les options de ciblage du webhook avec le filtre "lead_status" n'est pas "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Étape 3 : Lancez la campagne

Sélectionnez **Lancer** et observez l'évolution du statut de votre lead dans Salesforce à mesure que vos clients franchissent le seuil du score de lead MQL.

