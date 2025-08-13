---
nav_title: Salesforce Sales Cloud
article_title: Gérer les prospects avec Salesforce Sales Cloud
page_order: 3
page_type: reference
description: "Découvrez comment utiliser les webhooks de Braze pour créer et mettre à jour des leads dans Salesforce Sales Cloud via l'endpoint Salesforce sobjects/Lead."
---

# Gérer les prospects avec Salesforce Sales Cloud

> [Salesforce](https://www.salesforce.com/) est l'une des principales plateformes de gestion de la relation client (CRM) basées sur le cloud, conçue pour aider les entreprises à gérer l'ensemble de leur processus de vente, notamment la génération de leads, le suivi des opportunités et la gestion des comptes.<br><br>Cette page montre comment utiliser les webhooks Braze pour créer et mettre à jour des leads dans Salesforce Sales Cloud via une intégration soumise par la communauté.

{% alert important %}
Il s'agit d'une intégration proposée par la communauté et qui n'est pas directement prise en charge par Braze. Seuls les modèles de webhooks officiels fournis par Braze sont pris en charge par Braze.
{% endalert %}

## Fonctionnement

L'intégration Braze et Salesforce Sales Cloud utilise les webhooks Braze pour créer et mettre à jour des leads dans Salesforce Sales Cloud via l'endpoint Salesforce [sobjects/Lead](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html).

Braze propose actuellement deux intégrations à Salesforce Sales Cloud pour les cas d'utilisation suivants :
1. [Création d'une piste dans Salesforce Sales Cloud](#creating-lead)
2. [Mise à jour d'une piste dans Salesforce Sales Cloud](#updating-lead)

{% alert note %}
Cette intégration sert uniquement à mettre à jour Salesforce depuis Braze dans le cadre de vos efforts d'acquisition et de maturation de prospects. Pour synchroniser les données de Salesforce vers Braze, consultez le [modèle de données B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) ou contactez l'un de nos [partenaires technologiques]({{site.baseurl}}/partners/home/).
{% endalert %}

## Conditions préalables

Cette intégration nécessite de créer une app connectée dans Salesforce Sales Cloud en suivant les étapes de la documentation Salesforce : [Configurez une application connectée pour le flux d'informations d'identification du client OAuth 2.0.](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5)

Lorsque vous configurez les paramètres OAuth nécessaires pour l'application connectée, conservez tous les paramètres oAuth avec leurs valeurs et sélections par défaut, à l'exception de ce qui suit :
1. Sélectionnez le flux **Activer pour l’appareil**. Vous pouvez laisser l'**URL de rappel** vide, car elle sera remplacée par défaut par un marqueur substitutif.
2. Pour les **portées OAuth** sélectionnées, ajoutez **Gérer les données des utilisateurs via les API (api)**.
3. Sélectionnez **Activer le flux d'informations d'identification du client**.

## Création d'une piste dans Salesforce Sales Cloud {#creating-lead}

En tant que plateforme d'engagement client, Braze peut générer de nouveaux prospects en fonction des flux d'utilisateurs, par exemple en remplissant un formulaire sur une page de renvoi. Lorsque cela se produit, vous pouvez utiliser un webhook Braze Salesforce Sales Cloud pour créer un lead correspondant dans Salesforce.

### Étape 1 : Rassemblez vos `client_id` et `client_secret`

1. Dans Salesforce, accédez à **Outils de plate-forme** > **Apps** > **Gestionnaire d'applications**.
2. Recherchez votre application Braze nouvellement créée et sélectionnez **View.**
3. Sous **Clé et secret du consommateur**, sélectionnez **Gérer les détails du consommateur**.
4. Sur la page qui s'affiche, notez votre **clé de consommateur** et votre **secret de consommateur**. La **clé du consommateur** est votre `client_id`, et le **secret du consommateur** est votre `client_secret`.

### Étape 2 : Configurez votre modèle de webhook

Utilisez des modèles pour réutiliser rapidement ce webhook à travers la plateforme Braze. 

1. Dans Braze, allez dans **Modèles**, sélectionnez **Modèles de webhook**, puis **\+ Créer un modèle de webhook**.
2. Donnez un nom au modèle, par exemple "Salesforce Sales Cloud > Créer une piste".
3. Dans l'onglet **Composer**, entrez les informations suivantes :

#### Composer un webhook 

| Champ | Détails |
| --- | --- |
| URL du webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| Méthode HTTP | `POST` |
| Corps de la demande | Paires clé-valeur JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valeurs clés des propriétés du corps

Sélectionnez **\+ Ajouter une nouvelle propriété du corps** pour chacune des paires clé-valeur que vous souhaitez mapper de Braze vers Salesforce. Vous pouvez mapper n'importe quel champ, le tableau suivant n'est qu'un exemple.

| Clé | Valeur |
| --- | --- |
| firstName | {% raw %}`{{${first_name}}}`{% endraw %} |
| lastName | {% raw %}`{{${last_name}}}`{% endraw %} |
| e-mail | {% raw %}`{{${email_address}}}`{% endraw %} |
| entreprise | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### En-têtes de requête

Sélectionnez **\+ Add New Header** pour chacun des en-têtes de requête suivants.

| Clé | Valeur |
| --- | --- |
| Autorisation | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Type de contenu | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. Sélectionnez **Enregistrer le modèle**.

![Un modèle de webhook rempli pour créer une piste.]({% image_buster /assets/img/b2b/create_lead_webhook.png %}){: style="max-width:70%;"}
 
## Mise à jour d'une piste dans Salesforce Sales Cloud {#updating-lead}

Pour configurer un webhook Braze Salesforce Sales Cloud qui met à jour les leads dans Salesforce, vous avez besoin d'un identifiant commun entre Salesforce Sales Cloud et Braze. L'exemple ci-dessous utilise le site `lead_id` de Salesforce comme site `external_id` de Braze, mais vous pouvez également utiliser un site `user_alias`. Pour plus de détails à ce sujet, reportez-vous à la section [Données B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models)

Cet exemple montre spécifiquement comment mettre à jour le stade d'un lead en "MQL" (Marketing Qualified Lead) après qu'il ait franchi un certain seuil de leads. Il s'agit d'un élément essentiel de notre cas d'utilisation du [workflow de scoring des prospects B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/).

### Étape 1 : Rassemblez vos `client_id` et `client_secret`

1. Dans Salesforce, accédez à **Outils de plate-forme** > **Apps** > **Gestionnaire d'applications**.
2. Recherchez votre application Braze nouvellement créée et sélectionnez **View.**
3. Sous **Clé et secret du consommateur**, sélectionnez **Gérer les détails du consommateur**.
4. Sur la page qui s'affiche, notez votre **clé de consommateur** et votre **secret de consommateur**.
    - La **clé du consommateur** est votre `client_id`, et le **secret du consommateur** est votre `client_secret`.

### Étape 2 : Configurez votre modèle de webhook

1. Dans Braze, allez dans **Modèles**, sélectionnez **Modèles de webhook**, puis **\+ Créer un modèle de webhook**.
2. Donnez un nom au modèle, par exemple "Salesforce Sales Cloud > Update Lead to MQL".
3. Dans l'onglet **Composer**, entrez les informations suivantes :

#### Composer un webhook 

| Champ | Détails |
| --- | --- |
|URL du webhook | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| Méthode HTTP | `PATCH` |
| Corps de la demande | Paires clé-valeur JSON |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### Valeurs clés des propriétés du corps

Sélectionnez **\+ Ajouter une nouvelle propriété du corps** pour la paire clé-valeur suivante. Notez que `Lead_Stage__c` est un exemple de nom. Le champ personnalisé que vous utilisez pour suivre les MQL dans Salesforce peut avoir un nom différent, assurez-vous donc qu'ils correspondent.

| Clé | Valeur |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### En-têtes de requête

Sélectionnez **\+ Add New Header** pour chacun des en-têtes de requête suivants.

| Clé | Valeur |
| --- | --- |
| Autorisation | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| Type de contenu | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. Sélectionnez **Enregistrer le modèle**.

![Un modèle de webhook rempli pour mettre à jour une piste.]({% image_buster /assets/img/b2b/update_lead_webhook.png %}){: style="max-width:70%;"}

## Utilisation de ces webhooks dans un flux de travail opérationnel

Vous pouvez rapidement ajouter vos modèles à vos flux de travail opérationnels dans Braze, par exemple :

1. Partie d'une [campagne pour les nouveaux utilisateurs](#new-lead) qui crée un lead dans Salesforce.
2. Partie d'un [Canvas de scoring des leads](#lead-scoring) qui met à jour les utilisateurs qui ont franchi votre seuil MQL à "MQL", et qui met à jour Salesforce Sales Cloud avec les mêmes informations.

### Nouvelle campagne d'information {#new-lead}

Pour créer un lead dans Salesforce lorsqu'un utilisateur fournit son adresse e-mail, vous pouvez créer une campagne qui utilise le modèle de webhook "Update Lead" et se déclenche lorsqu'un utilisateur ajoute son adresse e-mail (par exemple, lorsqu'il remplit un formulaire Web).

![Étape 2 de la création d'une campagne basée sur des actions et dont l'action déclencheur est "Ajouter une adresse e-mail".]({% image_buster /assets/img/b2b/salesforce_create_campaign.png %}){: style="max-width:70%;"}

### Canevas de notation des prospects pour le franchissement du seuil de prospects qualifiés en marketing (MQL). {#lead-scoring}

Ce webhook est abordé dans le cas d'utilisation du [lead scoring]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff), mais vous pouvez également vérifier les MQL et mettre directement à jour Salesforce dans le canevas de lead scoring (au lieu de créer une campagne de webhook distincte) : 

Ajoutez une étape ultérieure à votre mise à jour des utilisateurs pour vérifier si un utilisateur a franchi le seuil MQL que vous avez défini. S'ils se sont croisés, mettez à jour le statut de l'utilisateur en "MQL", puis mettez à jour Salesforce avec le même statut "MQL" à l'aide de ce modèle de webhook. Salesforce s'occupe du reste en acheminant ce lead vers les équipes de vente appropriées à l'aide des règles d'acheminement des leads que vous avez définies.  

#### Ajout d'une étape du canvas pour vérifier les utilisateurs qui ont passé le seuil MQL 

1. Ajoutez une étape de **parcours d'audience** avec deux groupes : "Seuil MQL" et "Tous les autres".
2. Dans le groupe "Seuil MQL", recherchez les utilisateurs dont le statut n'est pas "MQL" (par exemple, `lead_stage` est égal à "Lead"), mais dont le score est supérieur au seuil que vous avez défini (par exemple, `lead_score` supérieur à 50). Si c'est le cas, ils passent à l'étape suivante, sinon ils sortent.

![Le groupe "MQL Threshold Audience Path" avec des filtres pour un `lead_stage` égal à "Lead" et un `lead_score` supérieur à "50".]({% image_buster /assets/img/b2b/salesforce_check_mql.png %}){: style="max-width:70%;"}

{: start="3" }
3\. Ajoutez une étape de **mise à jour de l'** utilisateur qui met à jour la valeur de l'attribut `lead_stage` de l'utilisateur à "MQL".

![L'étape de mise à jour de l'utilisateur "Update to MQL" qui met à jour l'attribut `lead_stage` avec la valeur "MQL".]({% image_buster /assets/img/b2b/salesforce_update_mql.png %}){: style="max-width:70%;"}

{: start="4" }
4\. Ajoutez une étape webhook qui met à jour Salesforce avec la nouvelle étape MQL.

![L'étape du webhook "Update Salesforce" avec les détails complétés.]({% image_buster /assets/img/b2b/salesforce_webhook.png %}){: style="max-width:70%;"}

Désormais, votre flux Canvas mettra à jour les utilisateurs qui ont franchi votre seuil MQL !

![Une étape de mise à jour de l'utilisateur Canvas qui vérifie si un utilisateur franchit le seuil MQL et, si c'est le cas, met à jour Salesforce.]({% image_buster /assets/img/b2b/salesforce_canvas.png %}){: style="max-width:50%;"}

## Résolution des problèmes

Ces flux de travail ont une capacité de débogage limitée dans Salesforce, nous vous recommandons donc de vous référer au [journal d'activité des messages de]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) Braze pour savoir pourquoi un webhook a échoué et si des erreurs se sont produites.

Par exemple, une erreur causée par une URL invalide utilisée pour la récupération du jeton oAuth s'affichera sous la forme suivante : `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL`.

![Un corps de réponse d'erreur indiquant que l'URL n'est pas valide.]({% image_buster /assets/img/b2b/error_message_invalid_url.png %})

