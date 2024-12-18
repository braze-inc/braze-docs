---
nav_title: "Création d'un webhook Braze à Braze"
article_title: "Création d'un webhook Braze à Braze"
page_order: 3
channel:
  - webhooks
description: "Cet article explique comment créer un webhook Braze à Braze pour les principaux cas d'utilisation."

---

# Création d'un webhook Braze à Braze

> Vous pouvez utiliser des webhooks pour communiquer avec l'[API REST][2] de Braze, essentiellement pour faire tout ce que notre API vous permet de faire. C’est ce que nous appelons un webhook Braze à Braze, un webhook qui communique depuis Braze vers Braze. Les cas d'utilisation présentés sur cette page supposent que vous connaissez [le fonctionnement des webhooks][4] et comment [créer un webhook][5] à Braze.

## Conditions préalables

Pour créer un webhook Braze à Braze, vous aurez besoin d'une [clé API][3] avec des autorisations pour l'endpoint que vous souhaitez atteindre.

## Configuration de votre webhook Braze à Braze

Bien que les spécificités de votre demande de webhook varient d'un cas d'utilisation à l'autre, le flux de travail général pour créer un webhook Braze à Braze reste le même.

1. [Créez un webhook][5] en tant que composant de campagne ou de canvas. 
2. Sélectionnez **Modèle vierge**.
3. Dans l'onglet **Composer**, spécifiez l'**URL du webhook** et le **corps de la requête** comme indiqué pour votre cas d'utilisation.
4. Dans l'onglet **Paramètres**, spécifiez la **méthode HTTP** et les **en-têtes de requête** comme indiqué pour votre cas d'utilisation.
5. Continuez à créer le reste de votre webhook au besoin. Certains cas d’utilisation nécessitent des paramètres de distribution particuliers, tels que le déclenchement de la campagne ou du canvas à partir d’un événement personnalisé.

## Cas d’utilisation

Les webhooks de Braze à Braze permettent de réaliser de nombreuses choses, mais voici quelques cas d'utilisation pour vous aider à démarrer :

- Incrémentez un attribut personnalisé sous forme d’entier pour créer un compteur lorsqu’un utilisateur reçoit un message.
- Déclencher un deuxième Canvas depuis un premier Canvas.

{% alert tip %}
Ajoutez une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) à votre canvas pour suivre les attributs, les événements et les achats d'un utilisateur dans un compositeur JSON. De cette manière, ces mises à jour sont mises en lots afin que Braze puisse les traiter plus efficacement qu'un webhook Braze à Braze.
{% endalert %}

### Cas d’utilisation : Incrémentez un attribut personnalisé sous forme d’entier pour obtenir un compteur

Ce cas d’utilisation implique de créer un attribut personnalisé et d’utiliser Liquid pour décompter le nombre de fois où une action donnée a eu lieu. 

Par exemple, vous pourriez vouloir compter combien de fois un utilisateur a vu une campagne de messages in-app active et l'empêcher de recevoir à nouveau la campagne après l'avoir vue trois fois. Pour plus d'idées sur ce que vous pouvez faire avec la logique Liquid dans Braze, consultez notre [bibliothèque de cas d'utilisation Liquid.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)

Suivez les étapes générales de création d'un webhook Braze à Braze, et reportez-vous à ce qui suit lors de la configuration de votre webhook :

- **URL du webhook :** Votre [URL de l'endpoint REST][7] suivi de `/users/track`. Par exemple, pour l'instance `US-06`, l'URL serait `https://rest.iad-06.braze.com/users/track`.
- **Corps de la requête :** Texte brut

#### En-têtes et méthode de la requête

Braze nécessite pour l’autorisation un en-tête HTTP qui comprend votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de la requête :**
  - **Autorisation :** Porteur {YOUR_API_KEY}
  - **Content-Type :** application/json
- **Méthode HTTP :** POST

Remplacez `YOUR_API_KEY` par une clé API REST Braze avec des autorisations `users.track`. Vous pouvez créer une clé API dans le tableau de bord de Braze sous **Paramètres** > **Clés API.**

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez créer une clé API à partir de la **console de développement** > **Paramètres API.**
{% endalert %}

![L'onglet "Settings" avec les en-têtes de requête pour le webhook.][1]

#### Corps de la demande

Ajoutez votre requête de suivi des utilisateurs dans le corps de la requête et le Liquid pour assigner une variable de décompte. Pour plus de détails, reportez-vous au [`/users/track` endpoint][8].

Vous trouverez ci-après un exemple du Liquid et du corps de requête nécessaire pour cet endpoint, dans lequel `your_attribute_count` est l’attribut que vous utilisez pour décompter le nombre de fois où un utilisateur a vu le message :

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
Chaque fois qu'un compteur d'attribut personnalisé est mis à jour (incrémenté ou décrémenté), il consommera un [point de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/), qui comptera dans votre consommation globale.
{% endalert %}

### Cas d’utilisation : Déclencher un deuxième Canvas depuis un premier Canvas

Pour ce cas d’utilisation, vous allez créer deux Canvas et utiliser un webhook pour déclencher le second Canvas depuis le premier. Ceci agit comme un déclencheur d’entrée pour le moment auquel un utilisateur atteint un certain point dans un autre Canvas.

1. Commencez par créer votre deuxième Canvas, celui qui doit être déclenché par le Canvas d’origine. 
2. Pour la **planification d'entrée** du canvas, sélectionnez **Déclenché par l'API**.
3. Prenez note de votre **ID de canvas**. Vous en aurez besoin dans une étape ultérieure.
4. Continuez à créer les étapes de votre deuxième Canvas, puis enregistrez-le.
5. Ensuite, créez votre premier Canvas. Trouvez l’étape à laquelle vous désirez déclencher le deuxième Canvas et créez une nouvelle étape avec un webhook. 

Référez-vous aux informations ci-dessous lorsque vous configurez votre webhook :

- **URL du webhook :** Votre [URL de l'endpoint REST][7] suivi de `canvas/trigger/send`. Par exemple, pour l’instance US-06, l’URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la requête :** Texte brut

#### En-têtes et méthode de la requête

Braze nécessite pour l’autorisation un en-tête HTTP qui comprend votre clé API et un autre qui déclare votre `content-type`.

- **En-tête de la requête :**
  - **Autorisation :** Bearer `YOUR_API_KEY`
  - **Content-Type :** application/json
- **Méthode HTTP :** POST

Remplacez `YOUR_API_KEY` par une clé API REST Braze avec des autorisations `canvas.trigger.send`. Vous pouvez créer une clé API dans le tableau de bord de Braze sous **Paramètres** > **Clés API.**

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez créer une clé API à partir de la **console de développement** > **Paramètres API.**
{% endalert %}

![L'onglet "Settings" avec les en-têtes de requête pour le webhook.][1]

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
- Les mises à jour du profil utilisateur entraîneront des [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count) supplémentaires, alors que le déclenchement d'un autre message par le biais des points d'extrémité de messages n'en entraînera pas.
- Si vous souhaitez cibler des [utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), vous pouvez utiliser `braze_id` au lieu de `external_id` dans le corps de la requête de votre webhook.
- Vous pouvez enregistrer votre webhook Braze à Braze comme [modèle]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) à réutiliser.
- Vous pouvez consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/) pour visualiser et résoudre les problèmes liés aux webhooks.


[1]: {% image_buster /assets/img_archive/webhook_settings.png %}
[2]: {{site.baseurl}}/api/basics/
[3]: {{site.baseurl}}/api/api_key/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/
[7]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
