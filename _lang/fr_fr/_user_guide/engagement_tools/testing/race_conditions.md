---
nav_title: Conditions de concurrence
article_title: Conditions de concurrence
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Cet article présente les meilleures pratiques pour éviter que les conditions de concurrence n'affectent vos campagnes de communication."
toc_headers: h2
---

# Conditions de concurrence

> Une condition de concurrence se produit lorsqu'un résultat dépend de la séquence ou de la synchronisation de plusieurs événements. Par exemple, si la séquence d'événements souhaitée est "événement A" puis "événement B", mais que parfois "événement A" arrive en premier, et d'autres fois "événement B" arrive en premier, il s'agit d'une condition de concurrence. Cela peut entraîner des résultats inattendus ou des erreurs, car ces événements sont en concurrence pour l'accès aux ressources ou aux données partagées.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

Dans Braze, des conditions de concurrence peuvent se produire lorsque plusieurs actions sont déclenchées en même temps sur la base de données ou d'événements utilisateur. Par exemple, si un utilisateur déclenche plusieurs campagnes (comme l'inscription à une lettre d'information ou un achat), il se peut qu'il ne reçoive pas les messages dans le bon ordre.

## Types de conditions de concurrence

Les types de conditions de concurrence les plus courants peuvent se produire lorsque vous effectuez les opérations suivantes :

- Le ciblage des nouveaux utilisateurs
- Utiliser plusieurs endpoints d'API
- Correspondance entre les filtres d'audience et les déclencheurs basés sur l'action. 

Examinez les scénarios suivants et mettez en œuvre les meilleures pratiques pour éviter ces conditions de concurrence.

## Scénario 1 : Le ciblage des nouveaux utilisateurs

Dans Braze, l'une des conditions de concurrence les plus courantes se produit avec les messages qui ciblent les utilisateurs nouvellement créés. L'ordre prévu des événements est le suivant :

1. Un utilisateur est créé ;
2. Le même utilisateur est immédiatement ciblé par un message, effectue un événement personnalisé ou enregistre un attribut personnalisé.

Toutefois, dans certains cas, le second événement se déclenche en premier. Cela signifie qu'un message tente d'être envoyé à un utilisateur qui n'existe pas encore. Par conséquent, l'utilisateur ne le reçoit jamais. Cela s'applique également aux événements ou aux attributs, lorsque l'événement ou l'attribut tente d'être enregistré dans un profil utilisateur qui n'a pas encore été créé.

### Meilleures pratiques

#### Introduire des retards

Après la création d'un nouvel utilisateur, vous pouvez ajouter un délai avant l'envoi de toute campagne de ciblage ou de Canevas. Ce délai permet la création du profil utilisateur et la mise à jour de tout attribut pertinent susceptible de déterminer l'admissibilité de l'utilisateur à recevoir le message.

Par exemple, lorsqu'un utilisateur s'inscrit à votre application, vous pouvez lui envoyer une offre promotionnelle après 24 heures. Par ailleurs, si vous créez un utilisateur ou enregistrez un attribut personnalisé, vous pouvez ajouter un délai d'une minute avant de poursuivre votre processus afin d'éviter cette condition de concurrence.

Vous pouvez également ajouter ce délai dans le [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration) pour l'événement personnalisé spécifique qui déclenche l'entrée d'un nouvel utilisateur dans un Canvas. 

## Scénario 2 : Utiliser plusieurs endpoints d'API

{% alert important %}
Nous utilisons un traitement asynchrone pour maximiser la vitesse et la flexibilité. Cela signifie que lorsque des appels API nous sont envoyés séparément, nous ne pouvons pas garantir qu'ils seront traités dans l'ordre où ils ont été envoyés.
{% endalert %}

Il existe quelques scénarios dans lesquels plusieurs endpoints de l'API peuvent également entraîner cette condition de concurrence, par exemple lorsque :

- Utiliser des endpoints API distincts pour créer des utilisateurs et déclencher des Canvases ou des campagnes.
- Effectuer plusieurs appels distincts à l'endpoint `/users/track` pour mettre à jour des attributs personnalisés, des événements ou des achats.

Lorsque les informations de l'utilisateur sont envoyées à Braze à l'aide de l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), leur traitement peut parfois prendre quelques secondes. Cela signifie que lorsque des demandes sont simultanément adressées à `/users/track` et à des endpoints de messages tels que `/campaign/trigger/send`, il n'est pas garanti que les informations relatives à l'utilisateur soient mises à jour avant l'envoi d'un message.

{% alert note %}
Si les attributs de l'utilisateur et les événements sont envoyés dans la même demande (à partir de `/users/track` ou du SDK), Braze traitera les attributs avant les événements ou la tentative d'envoi d'un message.
{% endalert %}

### Meilleures pratiques

#### Si vous utilisez plusieurs endpoints, envoyez vos demandes une à la fois.

Si vous utilisez plusieurs endpoints, vous pouvez essayer d'échelonner vos demandes de manière à ce que chaque demande soit terminée avant que la suivante ne commence. Cela peut réduire le risque de condition de concurrence. Par exemple, si vous devez mettre à jour les attributs de l'utilisateur et envoyer un message, attendez d'abord que le profil utilisateur soit complètement mis à jour avant d'envoyer un message à l'aide d'un endpoint.

Si vous envoyez une demande API de messages planifiés, ces demandes doivent être séparées et un utilisateur doit être créé avant d'envoyer la demande API planifiée.

#### Inclure des données clés dans le déclencheur

Au lieu d'utiliser plusieurs endpoints, vous pouvez inclure les [attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) et les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object) dans un seul appel API en utilisant l'[endpoint`campaign/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

Lorsque ces objets sont inclus dans le déclencheur, les attributs sont traités en premier, avant que le message ne soit déclenché, ce qui élimine les conditions de concurrence potentielles. Notez que les propriétés du déclencheur ne mettent pas à jour le profil utilisateur, mais sont utilisées uniquement dans le contexte du message.

#### Utilisez le POST : Suivi des utilisateurs (synchro) endpoint

Utilisez le [point de terminaison`/users/track/sync/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) pour enregistrer les événements et attributs clients personnalisés et mettre à jour les attributs du profil utilisateur de manière synchrone. L'utilisation de cet endpoint pour mettre à jour les profils utilisateurs en même temps et en un seul appel peut aider à prévenir d'éventuelles conditions de concurrence.

{% alert important %}
Cet endpoint est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la version bêta.
{% endalert %}

## Scénario 3 : Correspondance entre les déclencheurs basés sur l'action et les filtres d'audience.

Une autre condition de concurrence courante peut se produire si vous configurez une campagne basée sur une action ou un Canvas avec le même déclencheur que le filtre d'audience (tel qu'un attribut modifié ou l'exécution d'un événement personnalisé). L'utilisateur peut ne pas faire partie de l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il ne recevra pas la campagne ou n'entrera pas dans le Canvas.

### Meilleures pratiques

#### Vérifiez votre audience après un délai

Pour éviter d'utiliser des filtres d'audience contenant les critères de déclenchement, nous vous recommandons de vérifier votre audience avant la réception/distribution. Par exemple, vous pouvez [utiliser les validations de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) dans les étapes du canvas comme contrôle supplémentaire pour confirmer que votre audience répond aux critères de livraison lors de l'envoi du message. Vous pouvez également exploiter les critères de sortie pour Canvas afin de sortir n'importe quel utilisateur à n'importe quel moment du parcours utilisateur s'il répond à vos critères.

Pour les campagnes, vous pouvez utiliser les événements de sortie pour permettre aux campagnes avec un événement déclencheur d'interrompre les messages aux utilisateurs qui effectuent l'événement de sortie pendant le délai.

#### Utilisez des filtres uniques avec l'événement déclencheur

Lorsque vous configurez vos filtres, vous pouvez ajouter un filtre redondant "au cas où". Toutefois, cette redondance peut entraîner d'autres problèmes. Dans la mesure du possible, évitez plutôt d'utiliser un filtre contenant le déclencheur. C'est le moyen le plus sûr d'éviter une condition de concurrence.

Par exemple, si le déclencheur de votre campagne est "A effectué un achat" et que votre filtre d'audience est "A effectué n'importe quel achat", cette redondance peut provoquer une condition de concurrence. 

#### Évitez les filtres d'audience qui supposent que l'événement déclencheur a été mis à jour.

Cette bonne pratique est similaire à celle qui consiste à éviter les filtres redondants avec l'événement déclencheur. En général, un filtre qui suppose que l'événement déclencheur est mis à jour dans le profil utilisateur échoue.

#### Utiliser les interruptions de liquide (attributs uniquement)

Dans les campagnes et les étapes du canvas, utilisez les abandons liquides pour éviter d'utiliser les filtres d'audience qui contiennent les attributs du déclencheur au niveau de la planification d'entrée. Par exemple, disons que vous avez un tableau d'attributs "couleurs préférées" et que vous souhaitez cibler tout utilisateur qui met à jour le tableau d'attributs avec une valeur quelconque et qui a également la couleur "bleu" dans le tableau une fois la mise à jour effectuée. Si vous utilisez les filtres d'audience dans cet exemple, vous rencontrerez une condition de concurrence et manquerez les utilisateurs qui ajoutent "bleu" dans le tableau pour la première fois.

Dans ce cas, vous pouvez mettre en œuvre un délai de déclenchement dans une campagne ou utiliser une étape du canvas pour permettre au profil utilisateur de se mettre à jour pendant un certain temps, puis utiliser la logique d'annulation liquide suivante :

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirmer la façon dont les données des utilisateurs sont gérées

En cas de condition de concurrence lors de l'évaluation de l'entrée dans le Canvas, les utilisateurs peuvent entrer dans un Canvas qu'ils n'étaient pas censés entrer. Par exemple, le profil de l'utilisateur pourrait être défini pour être inclus dans l'audience et mis à jour ultérieurement après que le Canvas a mis en file d'attente les utilisateurs pour qu'ils ne soient plus éligibles dans l'audience. 

Nous vous recommandons de confirmer comment les données des utilisateurs sont gérées et mises à jour, en particulier quand et comment des attributs spécifiques sont mis à jour, par exemple par SDK, API, API par lots et d'autres méthodes. Cela peut aider à identifier et à clarifier la raison pour laquelle un utilisateur est entré dans une campagne ou un Canvas par rapport au moment où le profil de l'utilisateur a été mis à jour.
