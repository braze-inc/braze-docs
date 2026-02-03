---
nav_title: Histoire complète
article_title: Histoire complète
description: "Cet article de référence présente le partenariat entre Braze et Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Histoire complète

La plateforme de données comportementales de Fullstory aide les leaders technologiques à prendre de meilleures décisions, plus éclairées. En injectant des données comportementales numériques dans leur pile technologique, la technologie brevetée de Fullstory libère la puissance des données comportementales de qualité à grande échelle, transformant chaque visite numérique en informations exploitables. 

*Cette intégration est maintenue par Fullstory*

## À propos de cette intégration
Vous pouvez exploiter les informations de Fullstory dans Braze pour créer des images instantanées de l'expérience d'un utilisateur sur un site web ou une application, afin de diffuser des envois hyper-contextuels. L'API de résumé de session de Fullstory permet de capturer des métadonnées détaillées sur le comportement de navigation d'un utilisateur pour les utiliser dans les messages Braze, ce qui est particulièrement puissant dans le cadre d'un envoi de messages en plusieurs étapes comme un Canvas. 

La valeur en temps réel des données du résumé de session de Fullstory est mieux exploitée grâce au contenu connecté. En utilisant du contenu connecté dans une étape du contexte Canvas, vous pouvez stocker les données de Fullstory tout au long du parcours Canvas d'un utilisateur pour les utiliser dans toutes les étapes Canvas suivantes. Cela évite également de devoir écrire ces données dans un profil utilisateur Braze par le biais d'événements et d'attributs personnalisés. 

Dans l'exemple suivant, les données de contexte Canvas sont exploitées dans une étape Canvas de l'intelligence artificielle de l'agent afin de générer le message optimal pour encourager un utilisateur à reprendre un panier abandonné. Cependant, vous pouvez exploiter les données pour personnaliser directement le message, pour déterminer le parcours de l'utilisateur via les parcours d'audience, ou pour déterminer la copie ou les ressources utilisées dans les étapes ultérieures de l'envoi des messages.

## Cas d’utilisation

![Diagramme montrant les cas d'utilisation de l'intégration de Fullstory avec Braze]({% image_buster /assets/img/fullstory/1.png %})

## Conditions préalables

Avant de commencer, vous devez disposer des éléments suivants :

|Condition     | Description |                        
|-----------------------|-----------------|
| Un jeton d'autorisation de l'API Fullstory Session   | Voir l'étape 1 ci-dessous.  | 
| Un jeton d'autorisation de contenu connecté de Braze activé | Voir la note ci-dessous sur l'accès anticipé |
| Une étape du canvas Braze |Voir la note ci-dessous sur l'accès anticipé |
| Activation de l'étape de l'agent de l'intelligence artificielle de Braze | Voir la note ci-dessous sur l'accès anticipé|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Intégration de l'histoire complète

### Étape 1 : Configurer Fullstory pour l'activation de l'API de résumé de session

#### A : Récupération du [jeton d'authentification](https://developer.fullstory.com/server/authentication/) pour l'endpoint de l'API de résumé de session

Pour créer une clé API Fullstory, naviguez sur la plateforme Fullstory, puis **Paramètres** > **Clés API.** Sélectionnez le niveau d'autorisation **Standard** et copiez immédiatement la valeur de la clé, car elle n'apparaît qu'une seule fois.

#### B : Création d'un résumé de session ID du profil

En suivant les [conseils de Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), créez un profil de résumé de session à l'aide de l'endpoint dédié. C'est ici que vous définissez le type de données que vous souhaitez que la réponse Résumé de la session fournisse à Braze.
En réponse à cette demande, Fullstory fournit un "ID de profil" de session. Cet ID de profil est un élément clé du corps de la demande de contenu connecté utilisé dans le cas d'utilisation suivant.


### Étape 2 : Créer le jeton d'authentification du contenu connecté
1. Dans Braze, accédez à **Paramètres > Paramètres de l'espace de travail > Contenu connecté > Ajouter un justificatif > Authentification par jeton**. 

2. Nommez l'authentification "fullstory".

3. Ajoutez la clé d'en-tête "Authorization". Indiquez la valeur de l'en-tête Fullstory fournie à l'étape précédente. 

4. Sous Domaine autorisé, soumettez "api.fullstory.com".

![Capture d'écran de Braze montrant les champs Modifier le justificatif d'identité]({% image_buster /assets/img/fullstory/2.png %})

## Cas d’utilisation : Exploitez les données de résumé de session Fullstory et les étapes du canvas contextuel de Braze ainsi que les agents d'intelligence artificielle pour créer des envois de messages dynamiques.

En utilisant les [flux d'activation de](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) Fullstory, vous pouvez déclencher les toiles de Braze immédiatement après les interactions clés de l'utilisateur. La puissance de cette intégration réside dans l'unique `client_session_id` (accessible via {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que le système passe automatiquement de Fullstory à Braze. Cet ID sert de clé, permettant à Braze de récupérer le résumé de session complet de ce que l'utilisateur a vécu. 

En tirant parti des étapes du contexte Canvas et du contenu connecté, vous pouvez utiliser cet ID pour effectuer une demande d'API à Fullstory, récupérer les données de session et les stocker en tant que variable pour les utiliser plus tard dans le parcours. 

![Capture d'écran de l'étape du canvas canvas contextuel de Braze montrant la variable de contexte `summary_result` créée et alimentée par un appel de contenu connecté à Fullstory, pour récupérer un résumé de session.]({% image_buster /assets/img/fullstory/3.png %})

Avec le jeton d'autorisation créé précédemment, utilisez la structure de requête suivante pour extraire les données du résumé de la session. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 La réponse est enregistrée sous la forme de l'étiquette Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Nous utilisons cette étiquette Contexte dans les étapes suivantes du canvas.
{% endalert %}

À ce stade, le canvas peut accéder à la réponse à l'appel Contenu connecté, qui contient l'intégralité de l'envoi des messages pour la session d'un utilisateur.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Vous pouvez exploiter n'importe laquelle des données disponibles dans l'objet ci-dessus à l'aide de l'étiquette Liquid contextuelle à un stade ultérieur du parcours Canvas de l'utilisateur. Les étapes suivantes montrent comment vous pouvez utiliser ces données dans une étape du canvas de l'[agent d'intelligence artificielle](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step).

{% alert Note %}
Pour éviter tout comportement inattendu, incluez une étape de parcours d'audience après l'étape de contexte, qui peut faire sortir les utilisateurs du contexte si leur étiquette de contexte est vide, ce qui indique que l'appel au contenu connecté a échoué ou n'a pas renvoyé d'informations.

![Capture d'écran de l'étape Braze Audience]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Créer un agent d'intelligence artificielle capable d'analyser les charges utiles de Fullstory et de produire une copie appropriée pour votre cas d'utilisation.

[Le guide des agents de]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) Braze indique comment les utilisateurs de Braze peuvent créer des agents d'intelligence artificielle. En insérant une étape de l'agent d'intelligence artificielle dans un canvas déclenché par Fullstory, et en incluant l'étape du contexte du canvas décrite ci-dessus, les utilisateurs peuvent alimenter leur agent d'intelligence artificielle avec les données récapitulatives de la session de Fullstory, pour un large éventail d'objectifs. 

Dans cet exemple, nous utilisons ces données pour permettre à l'agent d'intelligence artificielle de générer un texte de message approprié à utiliser dans une carte de contenu, qui peut encourager l'utilisateur à retourner dans son panier abandonné.

![Capture d'écran du créateur de contexte de l'agent Braze avec l'invite]({% image_buster /assets/img/fullstory/4.png %})

Utilisez le même nom pour l'étiquette Context Liquid créée dans cette étape que pour l'étiquette Context Liquid utilisée dans l'étape Agent d'intelligence artificielle créée précédemment. 

L'invite requise pour votre cas d'utilisation varie, mais pour connaître nos meilleures pratiques en matière de création d'invites efficaces pour les agents, reportez-vous à la section [Rédaction d'instructions]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) dans *Création d'agents*. 


Dans votre canvas, sélectionnez une étape de l'agent d'intelligence artificielle, puis l'agent "Contexte de la session" créé dans le menu déroulant. Enregistrez la sortie sous forme de variable, dans ce cas "message", que vous pouvez placer dans la copie de message en utilisant l'étiquette Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Capture d'écran de l'étape du canvas contextuel de l'agent Braze avec l'invite]({% image_buster /assets/img/fullstory/5.png %})

Créez une étape de message qui exploite la copie créée par l'agent d'intelligence artificielle. Utilisez l'étiquette Liquid pour cette étape. 

{% alert Note %}

L'API de résumé de session de Fullstory peut renvoyer des données d'utilisateur sensibles et identifiables. Pour garantir la conformité lors du traitement des IIP (informations d'identification personnelle), assurez-vous que vos règles de capture de données Fullstory excluent les IIP avant de tirer parti de ce cas d'utilisation.

{% endalert %}