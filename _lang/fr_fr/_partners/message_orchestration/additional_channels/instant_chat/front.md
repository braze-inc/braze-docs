---
nav_title: Front
article_title: Front
description: "Découvrez comment intégrer Front à Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> L'intégration de Front vous permet de tirer parti de la transformation des données de Braze et des webhooks de chaque plateforme pour mettre en place un pipeline SMS conversationnel bidirectionnel.

Le webhook entrant provenant de Front contiendra une charge utile comprenant le message envoyé par l'agent. La demande devra être reformatée avant d'être acceptée par les endpoints de Braze. Le modèle de transformation des données frontales reformatera la charge utile et écrira un événement personnalisé dans le profil utilisateur intitulé **SMS sortant envoyé,** le corps du message étant transmis en tant que propriété de l'événement.

Avant de configurer une nouvelle transformation dans Braze, nous vous recommandons de consulter la matrice de prise en charge de chaque niveau dans notre documentation sur la [transformation des données]({{site.baseurl}}/user_guide/data/data_transformation/overview/). Nos niveaux Free et Pro offrent un nombre différent de transformations actives et de requêtes entrantes par mois. Confirmez que le plan actuel que vous avez souscrit peut prendre en charge votre cas d'utilisation.

## Prérequis

Avant de commencer, vous avez besoin des éléments suivants :

| Prérequis             | Descriptif                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Front            | Un compte Front est nécessaire pour tirer parti de ce partenariat.|
| URL du webhook Braze pour la transformation des données | La [transformation des données de Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/) sera utilisée pour reformater le webhook entrant de Front afin qu'il puisse être accepté par l'endpoint Braze /users/track.|
| Une clé API REST Front         | Une clé API REST de Front sera utilisée pour effectuer une requête webhook sortante de Braze à Front. |

## Cas d'utilisation

- Rationalisez votre processus de production de prospects en utilisant les messages SMS automatisés de Braze pour identifier les préférences des utilisateurs et permettre aux agents commerciaux en ligne/instantanés d'assurer le suivi et de conclure les ventes.
- Réengagez les clients qui ont abandonné leur panier en stimulant les conversions de ventes grâce aux réponses automatisées par SMS et à l'assistance directe par chat.

## Intégration de Front

### Étape 1 : Créer une transformation de données

Tout d'abord, vous allez créer une nouvelle transformation de données dans Braze. Les étapes suivantes sont simplifiées ; pour une description complète, voir [Création d'une transformation]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

1. Dans Braze, accédez à **Paramètres des données** > **Transformations de données**, puis sélectionnez **Créer une transformation**.
2. Sous **Modifier l'expérience**, sélectionnez **Recommencer à zéro**.
3. Sous **Sélectionner une destination**, sélectionnez **POST : Suivre les utilisateurs**.
4. Copiez et collez le modèle de transformation suivant, puis enregistrez et activez l'endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Votre transformation devrait ressembler à ce qui suit :

    ![Exemple de transformation de données.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
Vous pouvez modifier ce modèle pour répondre à vos besoins spécifiques. Par exemple, vous pouvez personnaliser le nom de l'événement personnalisé prédéfini. Pour plus d'informations, voir l'[aperçu de la transformation des données]({{site.baseurl}}/user_guide/data/data_transformation/overview/).
{% endalert %}

### Étape 2 : Créer une campagne de SMS sortants

Ensuite, vous créerez une campagne SMS qui écoutera les webhooks de Front et enverra une réponse SMS personnalisée à vos clients.

#### Étape 2.1 : Composez votre message

Dans la zone de texte **Message**, ajoutez le code Liquid suivant, ainsi que tout texte de désabonnement ou autre contenu statique.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Votre message devrait ressembler à ce qui suit :

![Un exemple de message utilisant le code Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Planification de la distribution

Pour le type de distribution, sélectionnez **Livraison par événement**. Pour le déclencheur d'événement personnalisé, sélectionnez **Envoi de SMS sortants**.

![La page "Planifier la distribution".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Cet événement personnalisé est la transformation de données qui écrit dans le profil de l'utilisateur. Les messages de l'agent seront enregistrés en tant que propriété de cet événement.
{% endalert %}

Enfin, sous **Contrôle de la distribution**, activez la rééligibilité.

![Rééligibilité activée sous "Contrôles de la distribution".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Étape 3 : Créer un canal personnalisé

Dans le tableau de bord de Braze, allez dans **Paramètres** > **Canaux** > **Ajouter des canaux**, puis sélectionnez **Canal personnalisé** et saisissez un nom pour votre nouveau canal Braze.

![Un canal personnalisé pour Braze dans le tableau de bord Front.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Étape 4 : Configurez les paramètres

Dans le champ de l'endpoint API sortant, entrez l'URL du webhook de transformation des données [que vous avez créé précédemment](#step-1-set-up-a-data-transformation-in-braze). Tous les messages sortants des agents en ligne/en production/instantanée sur votre nouveau canal Braze seront envoyés ici. Ce canal fournit également une URL d'endpoint vers laquelle Braze doit transférer les messages SMS dans le champ **URL entrant.**

Notez bien cette URL, vous en aurez besoin plus tard.

![Les paramètres du canal Braze nouvellement créé dans Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Étape 5 : Mise en place d'une redirection des SMS entrants

Ensuite, vous allez créer deux nouvelles campagnes webhook à Braze afin de pouvoir transférer les SMS entrants des clients vers la boîte de réception du Front.

|Nombre|Objectif|
|---|---|
|Campagne webhook 1|Signale à Front qu'une conversation en direct est demandée.|
|Campagne webhook 2|Transfère toutes les réponses SMS conversationnelles reçues du client vers la boîte de réception Front.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Étape 5.1 : Créez une catégorie de mots-clés SMS

Dans le tableau de bord de Braze, allez dans **Audience**, choisissez votre **groupe d'abonnement SMS**, puis sélectionnez **Ajouter un mot-clé personnalisé**. Pour créer une catégorie de mots-clés SMS exclusive pour Front, remplissez les champs suivants.

|Champ d'application|Descriptif|
|---|---|
|Catégorie de mots-clés|Le nom de votre catégorie de mots-clés, par exemple `FrontSMS1`.|
|Mots clés|Vos mots-clés personnalisés, tels que `TIMETOMOW`. Évitez les mots courants pour prévenir les déclencheurs accidentels. Gardez à l'esprit que les mots-clés sont insensibles à la casse, de sorte que `lawn` serait équivalent à `LAWN`.|
|Message de réponse|Le message qui sera envoyé lorsqu'un mot-clé est détecté, par exemple "Un paysagiste vous contactera sous peu".|
{: .reset-td-br-1 .reset-td-br-2 }

![Exemple de catégorie de mots-clés SMS dans Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Étape 5.2 : Créez votre première campagne webhook

Dans le tableau de bord de Braze, créez votre première campagne webhook à l'aide de l'URL [que vous avez créée précédemment](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Un exemple de la première campagne webhook qui devrait être créée dans Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Ajoutez ce qui suit au corps de votre requête :

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Dans l'onglet Paramètres, configurez vos en-têtes de requête `Authorization`, `content-type` et `accept`.

![Exemple de requête avec les trois en-têtes requis.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Étape 5.3 : Planifiez la première distribution

Pour **Schedule Delivery**, sélectionnez **Action-Based Delivery**, puis choisissez **Send an SMS Inbound Message** pour votre type de déclencheur. Ajoutez également le groupe d'abonnement SMS et la catégorie de mots-clés que vous avez [définis précédemment](#step-51-create-an-sms-keyword-category).

![La page "Planifier la distribution" pour la première campagne webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Sous **Contrôles de distribution**, activez la rééligibilité.

![Rééligibilité sélectionnée sous "Contrôles de distribution" pour la première campagne webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Étape 5.4 : Créez votre deuxième campagne webhook

Étant donné que votre deuxième campagne webhook correspondra à la première, vous pouvez [dupliquer la première et la renommer.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns) Vous pouvez le faire dès maintenant.

#### Étape 5.5 : Planifiez la seconde distribution

Pour la **distribution planifiée**, définissez le **déclencheur basé sur l'action** et le **groupe d'abonnement SMS** de la même manière que pour [la première distribution](#step-53-schedule-the-first-delivery). Toutefois, pour la **catégorie de mots-clés**, choisissez **Autre**.

![La page "Distribution planifiée" de la deuxième campagne webhook, avec "Autre" comme catégorie de mot-clé.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Étape 5.6 : Ajouter un filtre d'audience

Votre campagne webhook peut désormais transmettre les réponses SMS entrantes de vos clients. Pour filtrer les réponses SMS afin que seuls les messages pour les chats en direct soient transférés, ajoutez le filtre de segmentation **Dernier message reçu d'une campagne spécifique à** l'**étape Audiences cibles**.

![Un filtre d'audience avec "Dernier message reçu d'une campagne spécifique" sélectionné.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Configurez ensuite votre filtre :

1. Pour **Campagne**, sélectionnez la campagne SMS [que vous avez créée précédemment](#step-2-create-an-outbound-sms-campaign).
2. Pour **Opérateur**, sélectionnez **Moins que**.
3. Pour **Fenêtre de temps**, choisissez la durée pendant laquelle un chat doit rester ouvert sans réponse de la part du client.

![Les paramètres de configuration du filtre d'audience sélectionné.]({% image_buster /assets/img/front/front_target_audience.png %})

## Considérations

### Segments facturables

- Chez Braze, les envois de messages SMS sont facturés par segment de message. Il est essentiel de comprendre ce qui définit un segment et comment ces messages seront répartis pour savoir comment vous serez facturé pour les messages. Vous trouverez plus d'informations dans notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments).
- Les longues réponses des agents consommeront davantage de segments facturables.

### Consommation de points de données

Actuellement, cette intégration nécessite l'écriture d'un événement personnalisé dans le profil de l'utilisateur à chaque fois qu'un agent en ligne envoie un SMS depuis Front. Cela peut convenir à des échanges rapides qui ne durent que quelques messages, mais lorsque les conversations deviennent plus longues, les points de données deviennent de plus en plus importants. Un point de données est consommé pour chaque événement personnalisé enregistré dans Braze.

### Inclure des liens dans les messages SMS

Des balises HTML supplémentaires seront ajoutées à un lien envoyé à partir du chat en direct de Front.

### Joindre un fichier image depuis Front

Les fichiers images en Front ne s'afficheront pas dans les messages SMS envoyés par Braze.

### Options de désabonnement 

Les messages conversationnels risquent davantage de contenir le mot "stop" ou un texte informel similaire pouvant être interprété comme une demande de désabonnement.
