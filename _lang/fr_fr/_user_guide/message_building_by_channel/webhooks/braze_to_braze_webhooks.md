---
nav_title: "Création d'un webhook Braze à Braze"
article_title: "Création d'un webhook Braze à Braze"
page_order: 3
channel:
  - webhooks
description: "Cet article explique comment créer un webhook Braze à Braze pour les principaux cas d'utilisation."

---

# Création d'un webhook Braze à Braze

> Vous pouvez utiliser des webhooks pour communiquer avec l'[API REST de]({{site.baseurl}}/api/basics/) Braze, essentiellement pour faire tout ce que notre API vous permet de faire. C'est ce que nous appelons un webhook Braze à Braze - un webhook qui communique de Braze à Braze. Les cas d'utilisation présentés sur cette page supposent que vous connaissez le [fonctionnement des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) et que vous savez comment [créer un webhook à]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) Braze.

## Conditions préalables

Pour créer un webhook Braze à Braze, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec des permissions pour l'endpoint que vous souhaitez atteindre.

## Configuration de votre webhook Braze à Braze

Bien que les spécificités de votre demande de webhook varient d'un cas d'utilisation à l'autre, le flux de travail général pour créer un webhook Braze à Braze reste le même.

1. [Créez un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en tant que composant de campagne ou de canvas. 
2. Sélectionnez **Modèle vierge**.
3. Dans l'onglet **Composer**, spécifiez l'**URL du webhook** et le **corps de la requête** comme indiqué pour votre cas d'utilisation.
4. Dans l'onglet **Paramètres**, spécifiez la **méthode HTTP** et les **en-têtes de requête** comme indiqué pour votre cas d'utilisation.
5. Continuez à créer le reste de votre webhook selon vos besoins. Certains cas d'utilisation nécessitent des paramètres de réception/distribution spécifiques, comme le déclenchement de la campagne ou du Canvas à partir d'un événement personnalisé.

## Cas d'utilisation

Les webhooks de Braze à Braze vous permettent de faire beaucoup de choses, mais voici quelques cas d'utilisation pour vous aider à démarrer :

- Incrémente un attribut personnalisé de type entier pour un compteur lorsqu'un utilisateur reçoit un message.
- Déclencher un second canvas à partir d'un premier canvas.

{% alert tip %}
Ajoutez une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) à votre canvas pour suivre les attributs, les événements et les achats d'un utilisateur dans un compositeur JSON. De cette manière, ces mises à jour sont mises en lots afin que Braze puisse les traiter plus efficacement qu'un webhook Braze à Braze.
{% endalert %}

### Cas d'utilisation : Incrémenter un attribut personnalisé entier pour un compteur

Ce cas d'utilisation implique la création d'un attribut personnalisé et l'utilisation de Liquid pour compter le nombre de fois qu'une action spécifique s'est produite. 

Par exemple, vous pourriez vouloir compter combien de fois un utilisateur a vu une campagne de messages in-app active et l'empêcher de recevoir à nouveau la campagne après l'avoir vue trois fois. Pour plus d'idées sur ce que vous pouvez faire avec la logique Liquid dans Braze, consultez notre [bibliothèque de cas d'utilisation Liquid.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)

Suivez les étapes générales de création d'un webhook Braze à Braze, et reportez-vous à ce qui suit lors de la configuration de votre webhook :

- **URL du webhook :** L'[URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) votre [endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) suivi de `/users/track`. Par exemple, pour l'instance `US-06`, l'URL serait `https://rest.iad-06.braze.com/users/track`.
- **Corps de la demande :** Texte brut

#### En-têtes de requête et méthode

Braze exige un en-tête HTTP pour l'autorisation qui inclut votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de la demande :**
  - **Autorisation :** Porteur {YOUR_API_KEY}
  - **Content-Type :** application/json
- **Méthode HTTP :** POST

Remplacez `YOUR_API_KEY` par une clé API Braze avec les autorisations `users.track`. Vous pouvez créer une clé API dans le tableau de bord de Braze sous **Paramètres** > **Clés API.**

\![Les en-têtes de la requête pour le webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corps de la demande

Ajoutez votre demande de suivi de l'utilisateur dans le corps de la requête et le liquide pour assigner une variable de compteur. Pour plus de détails, reportez-vous à l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Voici un exemple du liquide requis et du corps de la requête pour cet endpoint, où `your_attribute_count` est l'attribut que vous utilisez pour compter le nombre de fois qu'un utilisateur a vu un message :

{% raw %}
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
Chaque fois qu'un compteur d'attribut personnalisé est mis à jour (incrémenté ou décrémenté), il consommera un [point de données]({{site.baseurl}}/user_guide/data/data_points/), qui comptera dans votre consommation globale.
{% endalert %}

### Cas d'utilisation : Déclencher un second canvas à partir d'un premier canvas

Pour ce cas d'utilisation, vous allez créer deux Canvas et utiliser un webhook pour déclencher le second Canvas à partir du premier Canvas. Il s'agit d'un déclencheur d'entrée lorsqu'un utilisateur atteint un certain point dans un autre Canvas.

1. Commencez par créer votre deuxième Canvas - le Canvas qui doit être déclenché par votre Canvas initial. 
2. Pour la **planification de l'entrée dans** le canvas, sélectionnez **API-Triggered (déclenché par l'API)**.
3. Notez votre **ID canvas**. Vous en aurez besoin dans une étape ultérieure.
4. Continuez à créer les étapes de votre second Canvas, puis enregistrez le Canvas.
5. Enfin, créez votre premier Canvas. Trouvez l'étape où vous souhaitez déclencher le second Canvas et créez une nouvelle étape avec un webhook. 

Reportez-vous à ce qui suit lors de la configuration de votre webhook :

- **URL du webhook :** L'[URL de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) votre [endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) suivi de `canvas/trigger/send`. Par exemple, pour l'instance US-06, l'URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la demande :** Texte brut

#### En-têtes de requête et méthode

Braze exige un en-tête HTTP pour l'autorisation qui inclut votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de la demande :**
  - **Autorisation :** Porteur `YOUR_API_KEY`
  - **Content-Type :** application/json
- **Méthode HTTP :** POST

Remplacez `YOUR_API_KEY` par une clé API Braze avec les autorisations `canvas.trigger.send`. Vous pouvez créer une clé API dans le tableau de bord de Braze sous **Paramètres** > **Clés API.**

\![Les en-têtes de la requête pour le webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corps de la demande

Ajoutez votre demande `canvas/trigger/send` dans le champ de texte. Pour plus d'informations, reportez-vous à la section [Envoi de messages canvas via la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Voici un exemple du corps de la requête pour cet endpoint, où `your_canvas_id` est l'ID du Canvas de votre deuxième Canvas : 

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

## Ce qu'il faut savoir

- Les webhooks Braze à Braze sont soumis aux [limites de débit des]({{site.baseurl}}/api/api_limits/) endpoints.
- Les mises à jour du profil utilisateur entraîneront des [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) supplémentaires, alors que le déclenchement d'un autre message par le biais des points d'extrémité de messages n'en entraînera pas.
- Si vous souhaitez cibler des [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), vous pouvez utiliser `braze_id` au lieu de `external_id` dans le corps de la requête de votre webhook.
- Vous pouvez enregistrer votre webhook Braze à Braze comme [modèle]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) à réutiliser.
- Vous pouvez consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) pour visualiser et résoudre les problèmes liés aux webhooks.


