---
nav_title: Meilleures pratiques
hidden: true
---

# Cycle de vie de l'utilisateur et meilleures pratiques en matière d'identifiants

## Collecte des données

En savoir plus sur la manière dont Braze recueille les données :
- [Collecte de données par SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)
- [Meilleures pratiques en matière de collecte de données]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)
- [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)

## Identifiants de Braze

- `braze_id`: Un identifiant attribué par la Braze qui est immuable et associé à un utilisateur particulier lorsqu'il est créé dans notre base de données.
- `external_id`: Un identifiant attribué par le client, généralement un UUID. Nous recommandons aux clients d'attribuer le `external_id` lorsque l'utilisateur peut être identifié de manière unique. Une fois qu'un utilisateur est identifié, il ne peut pas redevenir anonyme.
- `user_alias`: Un identifiant unique alternatif que le client peut attribuer comme moyen de référencer l'utilisateur par un ID avant l'attribution d'un `external_id`. Les alias des utilisateurs peuvent être fusionnés avec d'autres alias ou avec le site `external_id` lorsqu'un alias est disponible via l'endpoint d'[identification de l'utilisateur de]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) Braze.
    - Dans l'endpoint [Identification de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), le champ `merge_behavior` peut être utilisé pour spécifier quelles données du profil d'alias utilisateur doivent être conservées dans le profil utilisateur connu.
    - Notez que pour que l'alias d'utilisateur soit un profil pouvant être envoyé, vous devez toujours inclure l'e-mail et/ou le téléphone comme attribut standard du profil.
- `device_id`: Un identifiant spécifique à l'appareil, généré automatiquement. Un profil utilisateur peut être associé à plusieurs `device_ids`. Par exemple, un utilisateur qui s'est connecté à son compte sur son ordinateur professionnel, son ordinateur personnel, sa tablette et son application iOS aurait 4 `device_ids` associés à son profil.
- Adresse e-mail et numéro de téléphone :
    - Pris en charge en tant qu'identifiant dans l'endpoint utilisateur de Braze track. 
    - Lorsque l'adresse e-mail ou le numéro de téléphone est utilisé comme identifiant dans une requête, trois résultats sont possibles :
        1. Si un utilisateur ayant cet e-mail/téléphone n'existe pas dans Braze, un profil utilisateur e-mail/téléphone uniquement sera créé et toutes les données de la requête seront ajoutées au profil.
        2. Si un profil avec cet e-mail/téléphone existe déjà dans Braze, il sera mis à jour pour inclure toutes les données envoyées dans la requête.
        3. Dans un cas d'utilisation avec plus d'un profil avec cet e-mail/téléphone, le profil le plus récemment mis à jour sera prioritaire.
    - Notez que si un profil utilisateur uniquement par e-mail/téléphone existe et qu'un profil identifié avec le même e-mail/téléphone est ensuite créé (par exemple un autre profil avec la même adresse e-mail ET un ID externe), Braze créera un deuxième profil. Les mises à jour ultérieures seront envoyées au profil portant l'ID externe.
        - Les deux profils peuvent être fusionnés à l'aide de l'endpoint [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) Braze.

## Gestion des utilisateurs anonymes

Dans le cas où vous devez créer ou mettre à jour un profil utilisateur dans Braze sans avoir accès à `external_id`, un autre identifiant tel qu'une adresse e-mail ou un numéro de téléphone peut être transmis à l'endpoint Braze [Exporter l’utilisateur par l’identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour déterminer si un profil utilisateur existe dans Braze. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Si un utilisateur existe dans Braze avec cet e-mail ou ce téléphone, son profil sera renvoyé. Sinon, un tableau "users" vide sera renvoyé. L'avantage d'utiliser l'endpoint d'exportation pour déterminer si un utilisateur avec cette adresse e-mail existe déjà est que cela vous permettra de déterminer si des profils utilisateurs anonymes sont associés à l'utilisateur. Par exemple, un profil anonyme créé via le SDK (qui aura l’ID `braze_id`) ou un profil d’alias d'utilisateur créé précédemment. 

Si la requête ne renvoie pas de profil utilisateur, vous pouvez choisir de créer un alias d'utilisateur ou de créer un utilisateur par e-mail uniquement :

### Alias d'utilisateur

Utilisez l'endpoint de suivi des utilisateurs pour créer un alias d'utilisateur, en utilisant l'identifiant que vous avez choisi comme nom d'alias. En incluant `_update_existing_only` comme `false` dans l'objet attribut, événement ou achat où le nouvel alias utilisateur est défini, vous pouvez créer le profil de l'alias et ajouter simultanément des attributs, des événements et des achats à ce profil. 

Pour que l'alias d'utilisateur soit un profil envoyable, vous devez inclure l'adresse e-mail dans le champ `email`, comme indiqué ci-dessous.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Vous pouvez par la suite identifier et fusionner cet alias d'utilisateur avec un `external_id` lorsqu'un alias est disponible grâce à notre endpoint [Identifier les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

### Création d'un utilisateur uniquement par e-mail

Utilisez l'adresse e-mail comme identifiant dans l'endpoint de suivi de l'utilisateur. 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé.
{% endalert %}

## Synchronisation des données avec les profils utilisateurs

[Suivi de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Il s'agit d'un endpoint accessible au public qui peut créer et mettre à jour des utilisateurs dans Braze, par exemple en enregistrant des attributs dans le profil utilisateur. Cet endpoint a une limite de débit de 50 000 requêtes par minute appliquée au niveau de l'espace de travail.
- Lorsque vous utilisez cet endpoint, incluez la clé `partner` comme indiqué dans notre documentation pour les partenaires.

[Ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Comme pour l'endpoint de suivi des utilisateurs, les données peuvent être synchronisées avec les profils utilisateurs par le biais de l'ingestion de données dans le nuage. Lorsque vous utilisez cet outil, les attributs, les événements et les achats sont enregistrés dans les profils en configurant et en connectant la table ou la vue de l'entrepôt de données que vous souhaitez synchroniser avec l'espace de travail Braze souhaité.

[Points de données]({{site.baseurl}}/user_guide/data/data_points/)
- Braze dispose d'un modèle de consommation de points de données dans lequel des points de données sont générés par "écriture" dans le profil utilisateur, que la valeur ait changé ou non. C'est pourquoi nous vous recommandons de n'envoyer à Braze que les attributs qui ont été modifiés. 

## Envoi d'audiences d'utilisateurs à Braze

[Documentation sur les partenaires de synchronisation de l'importation de la cohorte]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Les audiences d'utilisateurs peuvent être synchronisées vers Braze en tant que cohorte à l'aide des endpoints de l'API d'importation de cohorte de Braze. Plutôt que de stocker ces audiences dans le profil de l'utilisateur sous forme d'attributs, les clients peuvent créer et cibler cette cohorte à l'aide d'un filtre propre au partenaire dans notre outil de segmentation. Cela peut faciliter la recherche et le ciblage d'un segment particulier d'utilisateurs pour les clients.
- Les endpoints d'importation de la cohorte ne sont pas publics et sont spécifiques à chaque partenaire. Pour cette raison, les synchronisations avec les endpoints de la cohorte ne seront pas prises en compte dans les limites de débit de l'espace de travail d'un client. 

[Suivi de l'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Il s'agit d'un endpoint accessible au public qui peut être utilisé immédiatement pour créer des utilisateurs dans Braze en désignant un utilisateur dans une audience particulière par le biais d'un attribut d'utilisateur. La principale différence entre cet endpoint et l'endpoint d'importation de cohorte est que les audiences envoyées à l'aide de cet endpoint seront stockées dans le profil utilisateur, alors que l'endpoint d'importation de cohorte apparaîtra comme un élément de remplissage dans notre outil de segmentation. Cet endpoint a une limite de débit de 50 000 requêtes par minute appliquée au niveau de l'espace de travail.
- Lorsque vous utilisez cet endpoint, assurez-vous que vous incluez la clé `partner` comme indiqué dans la [documentation de notre partenaire]({{site.baseurl}}/partners/isv_partners/api_partner).

[Points de données]({{site.baseurl}}/user_guide/data/data_points/)<br>
- Braze dispose d'un modèle de consommation de points de données dans lequel des points de données sont générés par "écriture" dans le profil utilisateur, que la valeur ait changé ou non.
- Les points de données proviennent à la fois de l'importation de la cohorte et des endpoints du suivi de l'utilisateur.

## Diffusion en continu des analyses d'engagement vers le partenaire

### Currents

Les Currents sont un outil d'analyse/analytique de l'engagement des messages en temps quasi réel dans Braze. Cela transmettra des données d'utilisateur pour chaque envoi, distribution, ouverture, clics, etc. pour les campagnes et les canvas envoyés depuis l'espace de travail du client. Quelques points à noter : Les flux Currents sont tarifés par connecteur pour le client, de sorte que tous les nouveaux partenaires Currents doivent passer par un processus d'EA. Nous demandons à nos partenaires d'avoir cinq clients dans le cadre de l'EA avant de créer l'interface utilisateur personnalisée et de mettre le connecteur à la disposition du public. 
- [Documentation du partenaire]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) \- tous les clients qui achètent un connecteur Currents auront accès à ces événements.
- [Événements liés au comportement de l'utilisateur]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) \- tous les clients qui achètent un connecteur Currents n'achètent pas un connecteur "tous les événements" qui inclura ces événements. 

### Partage des données Snowflake

Les clients qui achètent un connecteur Snowflake Data Share auront automatiquement accès aux événements d'engagement des messages et de comportement des clients. Lorsque Snowflake Data Share est utilisé en tant qu'intégration de partenaire, Braze provisionne un partage sur l'instance Snowflake du partenaire au nom du client. Le partage de données inter-régions ayant un coût plus élevé pour nos clients ; nous demandons donc aux partenaires souhaitant s'intégrer à Snowflake de prévoir un compte dans la région correspondante : `US-EAST-1` et/ou `EU-CENTRAL-1`
- [Documentation du partenaire]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## Créer et déclencher des campagnes et des canevas

### Créer des ressources dans Braze
Braze propose un certain nombre d'endpoints qui permettent aux clients et aux partenaires de créer/mettre à jour des modèles d'e-mail et des blocs de contenu dans l'espace de travail d'un client. Ces modèles et blocs de contenu peuvent, à leur tour, être utilisés dans les campagnes et canevas Braze du client.
- Modèles d'e-mail
    - [Créer un endpoint de modèle]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Mise à jour de l'endpoint du modèle]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Créer un endpoint de bloc de contenu]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Endpoint Mettre à jour le bloc de contenu]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### Campagnes déclenchées par l'API et Canvases

Les clients peuvent mettre en œuvre des campagnes et des canevas qui seront déclenchés par l'API. Les requêtes API pour déclencher ces campagnes peuvent être utilisées pour personnaliser et segmenter davantage la campagne en transmettant des propriétés API-trigger et des paramètres d'audience ou de destinataire. 
- [Déclencher des campagnes via l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Les campagnes sont des messages singuliers, tels que des e-mails individuels.
- [Déclencher des canvas via l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas est une interface unifiée où les marketeurs peuvent créer des campagnes avec plusieurs messages et étapes pour former un parcours cohérent. Lorsque vous déclenchez un Canvas, vous introduisez un utilisateur dans le flux Canvas, où il continuera à recevoir des messages jusqu'à ce qu'il ne corresponde plus aux critères du Canvas. 
- [Propriétés du déclencheur API/Propriétés de l'entrée dans le canevas]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Données qui peuvent être intégrées de manière dynamique dans le message au moment de l'envoi.

### Campagnes API
Lors de la création de campagnes API (différentes des campagnes déclenchées par l'API référencées ci-dessus), le tableau de bord de Braze est uniquement utilisé pour générer un `campaign_id`, qui permet au client de suivre les analyses pour le reporting de la campagne. Le message de la campagne lui-même est défini dans la requête d'API. 
- [Envoyer immédiatement une campagne API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Planifier une campagne API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### Envoyer des ID
Utilisez l'endpoint Braze pour générer un ID d'envoi qui peut être utilisé pour ventiler les analyses/analytiques de la campagne par envoi. Par exemple, si un paramètre `campaign_id` (campagne API) est créé par emplacement, un ID d'envoi pourrait être généré par envoi pour suivre l'efficacité des différents messages pour un emplacement particulier. 
- [Envoyer des ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Contenu connecté

Le contenu connecté peut être utilisé dans n'importe quel type de canal pour envoyer une requête API à l'endpoint spécifié au moment de l'envoi et intégrer dans le message ce qui est renvoyé dans la réponse.

La polyvalence des contenus connectés en fait une fonctionnalité utilisée par nombre de nos clients pour insérer des contenus qui n’existent pas ou ne peuvent pas être déployés dans Braze. Voici quelques-uns des cas d'utilisation les plus courants :
- Modélisation du contenu d'un blog ou d'un article en messages
- Recommandations de contenu
- Métadonnées du produit
- Localisation et traduction

A savoir :
- Les appels à l'API ne sont pas facturés par Braze et ne sont pas pris en compte dans le calcul de votre nombre de points de données.
- Les réponses au contenu connecté sont limitées à 1 Mo.
- Les appels au contenu connecté se feront lors de l'envoi du message, sauf pour les messages in-app, qui effectueront cet appel lors de la consultation du message.
- Les appels de contenu connecté qui ne suivent pas redirects.Braze exigent que le temps de réponse du serveur soit inférieur à 2 secondes pour des raisons de performances ; si le serveur met plus de 2 secondes à répondre, le contenu ne sera pas inséré.
- Les systèmes de Braze peuvent effectuer le même appel API de contenu connecté plus d'une fois par destinataire. Cela est dû au fait que Braze peut avoir besoin d'effectuer un appel API de contenu connecté pour générer un message, et les contenus de message peuvent être générés plusieurs fois par destinataire pour des raisons de validation, de logique de nouvelle tentative ou d'autres besoins internes. 

Consultez ces articles pour en savoir plus sur le contenu connecté :
- [Faire un appel au contenu connecté][1]
- [Abandon d'un contenu connecté][2]
- [Nouvelles tentatives de contenu connecté][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
