---
nav_title: Webhooks Braze à Braze
article_title: Webhooks Braze à Braze
page_order: 3
channel:
  - Webhooks
description: "Cet article décrit comment créer des webhooks Braze à Braze pour des cas d’utilisation clés."

---

# Webhooks Braze à Braze

> Vous pouvez utiliser des webhooks pour communiquer avec l’[API REST][2] de Braze et faire tout ce que notre API vous permet de faire. C’est ce que nous appelons un webhook Braze à Braze, un webhook qui communique depuis Braze vers Braze. 

## Conditions préalables

Pour créer un webhook Braze à Braze, vous aurez besoin d’une [clé API][3] avec des permissions pour les endpoints que vous désirez atteindre. Par exemple, si vous utilisez l’endpoint de suivi des utilisateurs, vous aurez besoin d’une clé API avec les permissions `users.track`.

## Cas d’utilisation

Vous pouvez accomplir de nombreuses choses avec les webhooks Braze à Braze, mais voici quelques cas d’utilisation communs pour commencer :

- Écrire ou mettre à jour des attributs personnalisés sur un profil utilisateur.
- Faites référence à une propriété d’événement tout au long d’un Canvas en enregistrant la propriété de l’événement sur le profil utilisateur en tant qu’attribut.
- Incrémentez un attribut personnalisé sous forme d’entier pour créer un compteur lorsqu’un utilisateur reçoit un message.
- Déclencher un deuxième Canvas depuis un premier Canvas.

Les exemples de cas d’utilisation sur cette page partent du principe que vous êtes déjà familiarisés avec [la manière dont fonctionne les webhooks][4] et comment [créer un webhook][5] dans Braze.

## Étapes pour créer un webhook Braze à Braze

Même si les détails de votre requête webhook varient entre chaque cas d’utilisation, le flux de travail global pour créer un webhook Braze à Braze reste le même.

1. [Créer un webhook][5] en tant que campagne ou composant de Canvas. 
2. Choisissez un **Modèle vide**.
3. Dans l’onglet **Composer**, définissez l’**URL webhook** et le **corps de la requête** comme indiqué pour votre cas d’utilisation.
4. Dans l’onglet **Paramètres**, définissez votre **méthode HTTP** et les **en-têtes de requête** as noted for your use case.
5. Continuez à construire le reste de votre webhook au besoin. Remarquez que certains cas d’utilisation nécessitent des paramètres de livraison particuliers tels que le déclenchement de la campagne ou du Canvas à partir d’un événement personnalisé.

### Cas d’utilisation : Ajouter un événement ou un attribut à un profil utilisateur

Avec ce cas d’utilisation, vous pouvez mettre à jour un profil utilisateur avec un événement, une propriété d’événement ou un attribut au sein d’une campagne ou d’un Canvas. Par exemple, un site Internet B2C peut ajouter un attribut de `purchase_lapsers=true` à un profil utilisateur s’ils ne se convertissent pas à partir d’une campagne ou d’un Canvas de panier abandonné pour permettre à ces utilisateurs d’être reciblés avec une communication ultérieure.

Un autre cas d’utilisation fréquent est une solution de contournement pour permettre à des propriétés de l’événement de perdurer tout au long d’un Canvas plutôt qu’à la première étape uniquement. Ceci implique d’ajouter une propriété d’événement en tant qu’attribut personnalisé pour que vous puissiez référencer cette propriété tout au long d’un Canvas. Utiliser les résolutions des [propriétés d’entrée persistantes dans Canvas][6] pour ce problème.

{% alert important %}
Pour pouvoir référencer une propriété d’événement tout au long d’un Canvas, vous devez ajouter une propriété d’événement au profil utilisateur en tant qu’attribut dans la première étape du Canvas. De plus, le Canvas lui-même doit être déclenché par cet événement.
{% endalert %}

Suivez ces étapes globales pour créer un webhook Braze à Braze et consultez les étapes suivantes lors de la configuration de votre webhook :

- **URL du webhook** : Votre [URL d’endpoint REST][7] suivie de `/users/track`. Par exemple, pour l’instance US-06, l’URL serait `https://rest.iad-06.braze.com/users/track`.
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

Braze nécessite pour l’autorisation un en-tête HTTP qui comprend votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de requête** :
  - **Autorisation** : Bearer `YOUR_API_KEY`
  - **Type de contenu** : application/json
- **Méthode HTTP** : POST

Remplacez `YOUR_API_KEY` par une clé d’API REST Braze avec des autorisations `users.track`. Vous pouvez créer une clé d’API, dans le tableau de bord de Braze dans **Developer Console** > **Clé d’API REST** > **Créer une nouvelle clé d’API**.

![][1]

#### Corps de la demande

Ajoutez votre requête de suivi utilisateur dans le corps de la requête. Pour plus de détails, consultez le [Suivi utilisateur][8]. Vous trouverez ci-dessous un exemple de corps de requête pour cet endpoint lorsque vous ajoutez une propriété d’événement en tant qu’attribut personnalisé à un profil utilisateur :

{% raw %}

```json
{
  "attributes": [
    {
      "external_id": "{{${user_id}}}",
      "new_custom_attribute": "{{event_properties.${your_event_property}}}"
    }
  ]
}
```

{% endraw %}

{% alert note %}
Chaque événement personnalisé, attribut d’événement ou attribut mis à jour sur un profil utilisateur est comptabilisé dans votre communication de [point de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/). 
{% endalert %}

#### Paramètres supplémentaires
 
Pour vos paramètres de livraison, sélectionnez **Livraison par événement**. Définissez l’**action de déclenchement** sur « Effectuer l’événement personnalisé » et choisissez l’action qui doit déclencher ce webhook.

### Cas d’utilisation : Incrémentez un attribut personnalisé sous forme d’entier pour obtenir un compteur

Ce cas d’utilisation implique de créer un attribut personnalisé et d’utiliser Liquid pour décompter le nombre de fois où une action donnée a eu lieu. 

Vous pourriez par exemple désirer décompter le nombre de fois où un utilisateur a vu une campagne de communication in-app active et l’empêcher de recevoir une nouvelle fois la campagne après qu’ils l’aient vue trois fois. Consultez notre [bibliothèque de cas d’utilisation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases) pour obtenir plus d’idées sur ce que vous pouvez faire avec la logique Liquid dans Braze.

Suivez ces étapes globales pour créer un webhook Braze à Braze et consultez les étapes suivantes lors de la configuration de votre webhook :

- **URL du webhook** : Votre [URL d’endpoint REST][7] suivie de `/users/track`. Par exemple, pour l’instance US-06, l’URL serait `https://rest.iad-06.braze.com/users/track`.
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

Braze nécessite pour l’autorisation un en-tête HTTP qui comprend votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de requête** :
  - **Autorisation** : Bearer `YOUR_API_KEY`
  - **Type de contenu** : application/json
- **Méthode HTTP** : POST

Remplacez `YOUR_API_KEY` par une clé d’API REST Braze avec des autorisations `users.track`. Vous pouvez créer une clé d’API, dans le tableau de bord de Braze dans **Developer Console** > **Clé d’API REST** > **Créer une nouvelle clé d’API**.

![][1]

#### Corps de la demande

Ajoutez votre requête de suivi utilisateur dans le corps de la requête ainsi qu’au Liquid pour assigner une variable de décompte. Pour plus de détails, consultez le [Suivi utilisateur][8].

Vous trouverez ci-après un exemple du Liquid et du corps de requête nécessaire pour cet endpoint, dans lequel `your_attribute_count` est l’attribut que vous utilisez pour décompter le nombre de fois où un utilisateur a vu le message : {% raw %}

```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Chaque fois qu’un compteur d’attribut personnalisé est mis à jour (incrémenté ou décrémenté), il utilisera un [point de donnée]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/) comptant pour l’utilisation totale.
{% endalert %}

### Cas d’utilisation : Déclencher un deuxième Canvas depuis un premier Canvas

Pour ce cas d’utilisation, vous allez créer deux Canvas et utiliser un webhook pour déclencher le second Canvas depuis le premier. Ceci agit comme un déclencheur d’entrée pour le moment auquel un utilisateur atteint un certain point dans un autre Canvas.

1. Commencez par créer votre deuxième Canvas, celui qui doit être déclenché par le Canvas d’origine. 
2. Comme **planification d’entrée** du Canvas, sélectionnez **déclenché par API**.
3. Notez votre **ID Canvas**, vous en aurez besoin par la suite.
4. Continuez à construire les étapes de votre deuxième Canvas, puis enregistrez-le.
5. Ensuite, créez votre premier Canvas. Trouvez l’étape à laquelle vous désirez déclencher le deuxième Canvas et créez une nouvelle étape avec un webhook. 

Référez-vous aux informations ci-dessous lorsque vous configurez votre webhook :

- **URL du webhook** : Votre [URL d’endpoint REST][7] suivie de `canvas/trigger/send`. Par exemple, pour l’instance US-06, l’URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

Braze nécessite pour l’autorisation un en-tête HTTP qui comprend votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de requête** :
  - **Autorisation** : Bearer `YOUR_API_KEY`
  - **Type de contenu** : application/json
- **Méthode HTTP** : POST

Remplacez `YOUR_API_KEY` par une clé d’API REST Braze avec des autorisations `canvas.trigger.send`. Vous pouvez créer une clé d’API, dans le tableau de bord de Braze dans **Developer Console** > **Clé d’API REST** > **Créer une nouvelle clé d’API**.

![][1]

#### Corps de la demande

Ajoutez votre requête `canvas/trigger/send` dans le champ de texte. Pour plus de détails, consultez la section [Envoyer des messages Canvas à l’aide d’une livraison déclenchée par API][9]. Vous trouverez ci-après un exemple du corps de la requête pour cet endpoint, dans lequel `your_canvas_id` est l’ID Canvas de votre deuxième Canvas : 

{% raw %}
```json
{
      "canvas_id": "your_canvas_id",
      "recipients": [
        {
          "external_user_id": "{{${user_id}}}"
         }
      ]
}
```
{% endraw %}

## Choses à savoir

- Les webhooks Braze à Braze sont soumis aux [limites de débit]({{site.baseurl}}/api/api_limits/) des endpoints.
- Les mises à jour du profil utilisateur engendreront des [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) supplémentaires, alors que déclencher un autre message à l’aide d’endpoints d’envoi de messages ne le fera pas.
- Si vous désirez cibler les [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), vous pouvez utiliser `braze_id` au lieu de `external_id` dans le corps de la requête de votre webhook.
- Vous pouvez sauvegarder votre webhook Braze à Braze sous forme de [modèle]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) pour pouvoir le réutiliser.
- Vous pouvez consulter la [journalisation d’activités des messages]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) pour voir et résoudre les problèmes d’échecs de webhook.


[1]: {% image_buster /assets/img_archive/webhook_settings.png %}
[2]: {{site.baseurl}}/api/basics/
[3]: {{site.baseurl}}/api/api_key/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/
[7]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
