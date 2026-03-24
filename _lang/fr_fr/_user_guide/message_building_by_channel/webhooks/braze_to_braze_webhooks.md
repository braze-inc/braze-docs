---
nav_title: Créer un webhook Braze à Braze
article_title: Créer un webhook Braze à Braze
page_order: 3
channel:
  - webhooks
description: "Cet article de référence explique quand utiliser les mises à jour utilisateur par rapport aux webhooks Braze à Braze et comment créer un webhook Braze à Braze."

---

# Créer un webhook Braze à Braze

> Les webhooks Braze à Braze vous permettent d'appeler l'[API REST Braze]({{site.baseurl}}/api/basics/) depuis Braze à l'aide d'un [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) dans une [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [un canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/). Veuillez utiliser cette fonctionnalité pour les tâches d'orchestration telles que le déclenchement d'un [canvas déclenché par une API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Pour mettre à jour [les attributs utilisateur]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [les événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) ou [les achats]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) depuis canvas, veuillez utiliser [la mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/). Il est conçu pour modifier les profils utilisateurs et traiter les mises à jour de manière plus efficace.

Pour tirer le meilleur parti de cet article, il est recommandé de bien comprendre [le fonctionnement des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) et la manière de [créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) dans Braze.

## Veuillez utiliser la mise à jour utilisateur pour modifier les données utilisateur.

Pour mettre à jour les profils utilisateur à partir d'un Canvas, y compris pour modifier [les attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), enregistrer [des événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) ou enregistrer [des achats]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), veuillez utiliser [la mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) plutôt qu'un webhook Braze à Braze. 

La mise à jour utilisateur regroupe plusieurs modifications et les envoie par lots, ce qui la rend plus rapide que les webhooks. Il est plus simple à configurer qu'un webhook et prend en charge les mises à jour complexes grâce à son [compositeur JSON avancé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer). Par exemple, pour compter le nombre de fois qu'un utilisateur a vu un message, veuillez utiliser [la fonctionnalité d'incrémentation et de décrémentation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values) de User Update plutôt qu'un webhook Braze à Braze.

{% alert tip %}
Veuillez ajouter [la mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) à votre canvas afin de mettre à jour les attributs, les événements et les achats d'un utilisateur à l'aide d'un compositeur JSON.
{% endalert %}

## Quand utiliser un webhook Braze à Braze

La mise à jour utilisateur peut gérer presque toutes les mêmes tâches qu'un webhook Braze à Braze pour la mise à jour des profils utilisateurs. Pour les mises à jour complexes qui dépassent le cadre des attributs personnalisés simples, il est possible d'utiliser le [compositeur JSON avancé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer).

Vous pouvez utiliser un webhook Braze à Braze lorsque vous avez besoin d'appeler [l'API REST]({{site.baseurl}}/api/basics/) de Braze depuis Braze pour des scénarios autres que les mises à jour directes des utilisateurs à partir des étapes du canvas. Voici quelques exemples courants :

- Déclenchement d'un [canvas déclenché par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) à partir d'un autre canvas
- Appel d'autres [endpoints d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) pour les modèles d'orchestration dans lesquels un flux de travail dans Braze doit invoquer une API qui ne dispose pas d'un composant Canvas dédié.

Pour les mises à jour des utilisateurs dans Canvas, il est recommandé d'utiliser la fonction [« User Update »]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) (Mise à jour des utilisateurs).

## Conditions préalables

Pour créer un webhook Braze à Braze, il est nécessaire de disposer d'une [clé API]({{site.baseurl}}/api/api_key/) avec les autorisations requises pour l'endpoint que vous souhaitez atteindre. Par exemple, pour déclencher un canvas déclenché par API, vous avez besoin d'une clé API avec `canvas.trigger.send`l'autorisation.

## Configuration de votre webhook Braze à Braze

Le processus général de création d'un webhook Braze à Braze comprend les étapes suivantes :

1. [Créez un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) en tant que composant de campagne ou de canvas. 
2. Sélectionnez **Modèle vierge**.
3. Dans l'onglet **Composer**, veuillez indiquer l'**URL** **du webhook** et **le corps de la requête** pour votre cas d'utilisation de l'API.
4. Dans l'onglet **Paramètres**, veuillez indiquer votre **méthode HTTP** et **vos en-têtes de requête** conformément aux exigences de l'endpoint.
5. Veuillez configurer tous les paramètres de réception/distribution supplémentaires (par exemple, le déclencheur à partir d'un événement personnalisé) et créer le reste de votre campagne ou de votre canvas.

## Déclencher un deuxième Canvas depuis un premier Canvas

Dans ce cas d'utilisation, vous créez deux canevas et utilisez un webhook Braze à Braze pour servir de déclencheur au deuxième canevas à partir du premier. Ceci agit comme un déclencheur d’entrée pour le moment auquel un utilisateur atteint un certain point dans un autre Canvas.

1. Commencez par créer votre deuxième Canvas, celui qui doit être déclenché par le Canvas d’origine.
2. Pour la **planification d'entrée** du canvas, sélectionnez **Déclenché par l'API**.
3. Prenez note de votre **ID de canvas**. Vous en aurez besoin dans une étape ultérieure.
4. Continuez à créer les étapes de votre deuxième Canvas, puis enregistrez-le.
5. Ensuite, créez votre premier Canvas. Trouvez l’étape à laquelle vous désirez déclencher le deuxième Canvas et créez une nouvelle étape avec un webhook.

Référez-vous aux informations ci-dessous lorsque vous configurez votre webhook :

- **URL du webhook :** L'[URL de votre endpoint REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) suivie de `/canvas/trigger/send`. Par exemple, dans `US-06`l'instance présente, l'URL serait `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corps de la requête :** Texte brut

#### En-têtes et méthode de la requête

Braze nécessite un en-tête HTTP pour l'autorisation, qui comprend votre clé API et un autre en-tête qui indique votre Content-Type.

- **En-têtes de requête :**
  - **Autorisation :** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **Méthode HTTP :** `POST`

Veuillez remplacer`YOUR_API_KEY`par une clé API Braze disposant`canvas.trigger.send`des autorisations nécessaires. Vous pouvez créer une clé API dans le tableau de bord de Braze en accédant à **Paramètres** > **Clés API**.

![En-têtes de requête pour le webhook affichant les champs Authorization et Content-Type dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corps de la demande

Ajoutez votre requête `/canvas/trigger/send` dans le champ de texte. Pour plus de détails, veuillez consulter [la section Envoi de messages Canvas via une réception/distribution déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Vous trouverez ci-après un exemple du corps de la requête pour cet endpoint, dans lequel `your_canvas_id` est l’ID Canvas de votre deuxième Canvas :

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

Lorsqu'un utilisateur atteint cette étape du canvas dans le premier Canvas, Braze déclenche le deuxième Canvas pour cet utilisateur via l'API.

## Considérations

- **Mises à jour utilisateur :** Pour mettre à jour les profils utilisateurs à partir de Canvas (attributs, événements, achats), veuillez utiliser [la fonctionnalité « User Update »]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) plutôt que les webhooks Braze à Braze afin d'optimiser l'efficacité et la rentabilité.
- Les webhooks Braze à Braze sont soumis à [des limites de débit]({{site.baseurl}}/api/api_limits/) au niveau des endpoints.
- Les mises à jour du profil utilisateur entraînent [des points de données]({{site.baseurl}}/user_guide/data/data_points/) qui sont comptabilisés dans votre consommation globale, tandis que le déclenchement d'un autre message via les points d'envoi de messages n'est pas comptabilisé.
- Pour le ciblage [des utilisateurs anonymes]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles), veuillez utiliser`braze_id`  au lieu de`external_id`  dans le corps de la requête de votre webhook.
- Vous pouvez enregistrer votre webhook Braze à Braze en tant que [modèle]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) [de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) afin de le réutiliser ultérieurement.
- Vous pouvez consulter le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) pour visualiser et résoudre les problèmes liés aux webhooks.


