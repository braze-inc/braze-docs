---
nav_title: FAQ
article_title: FAQ Canvas
page_order: 10
description: "Cet article fournit des réponses aux questions fréquemment posées sur Canvas."
tool: Canvas

---

# FAQ Canvas

> Cet article fournit des réponses à des questions fréquemment posées sur Canvas.

### Que se passe-t-il si l’audience et l’heure d’envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ?

Nous mettons en file d’attente un travail pour chaque étape, ils sont exécutés à peu près simultanément et l’un d’entre eux « gagne ». En pratique ce processus peut être quelque peu uniforme, mais il y a parfois une légère distorsion par rapport à l’étape créée en premier. 

De plus, nous ne pouvons pas garantir avec précision ce à quoi ressemblera cette répartition. Si vous voulez garantir un fractionnement uniforme, ajoutez un filtre [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/).

### Que se passe-t-il lorsque vous arrêtez un Canvas ?

Lorsque vous arrêtez un Canvas, les éléments suivants s’appliquent :

- L’accès au Canvas sera bloqué pour les utilisateurs.
- Plus aucun message ne sera envoyé, quel que soit le niveau auquel se situe un utilisateur dans le flux.
- **Exception :** Les Canvas e-mail ne seront pas automatiquement arrêtés. Une fois que les requêtes sont transmises à SendGrid, nous ne pouvons rien faire pour arrêter la livraison à l’utilisateur.

{% alert note %}
L’arrêt de Canvas n’impactera pas les utilisateurs en attente de réception de messages. Si vous activez à nouveau le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le temps d’envoi du message se soit écoulé, dans ce cas, ils ne le recevront pas).
{% endalert %}

### À quel moment un événement d’exception est-il déclenché ?

[Les événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) sont uniquement déclenchés alors qu’un utilisateur attend de recevoir la Canvas Step associée. Si un utilisateur effectue une action à l’avance, l’événement d’exception ne sera pas déclenché.

Si vous souhaitez créer une exception pour des utilisateurs ayant effectué un événement spécifique en avance, utilisez plutôt [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### En quoi la modification d’un Canvas affecte-t-elle des utilisateurs déjà présents dans les Canvas ?

Si vous modifiez certaines étapes d’un Canvas à plusieurs étapes, les utilisateurs qui étaient déjà dans le public, mais n’ayant pas encore reçu les étapes, recevront la version mise à jour du message. Notez que ce cas se produit uniquement s’ils n’ont pas encore été évalués pour l’étape.

Pour plus d’informations sur ce que vous pouvez modifier ou pas après le lancement, consultez [Modification de votre Canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/change_your_canvas_after_launch/).

### Comment le suivi des conversions utilisateur est-il effectué dans Canvas ?

Un utilisateur peut uniquement effectuer une conversion par entrée Canvas.

Les conversions sont affectées au message le plus récent reçu par l’utilisateur pour cette entrée. Le blocage de synthèse au début d’un Canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu’ils aient reçu un message ou pas. Chaque message suivant affichera uniquement les conversions effectuées lorsque l’utilisateur a reçu l’étape la plus récente.

{% details Examples %}

#### Exemple 1

Il existe un chemin Canvas avec 10 notifications push et l’événement de conversion est « lancement de session » (« Ouvre l’application ») :

- L’utilisateur A ouvre l’application après l’accès, mais avant la réception du premier message.
- L’utilisateur B ouvre l’application après chaque notification push.

**Résultat :**
La synthèse affichera deux conversions alors que chaque étape affichera une conversion pour la première étape et aucune conversion pour toutes les étapes suivantes.

{% alert note %}
Si des heures calmes sont actives lorsque l’événement de conversion se produit, les mêmes règles s’appliquent.
{% endalert %}

#### Exemple 2

Il existe un Canvas avec des heures calmes :

1. L’utilisateur accède au Canvas.
2. La première étape ne présente pas de retard, mais se situe dans les heures calmes, le message est donc supprimé.
3. L’utilisateur effectue l’événement de conversion.

**Résultat :**
La conversion de l’utilisateur sera prise en compte dans l’ensemble de Canvas Variant, mais pas l’étape, faute d’avoir été reçue.

{% enddetails %}

### Lorsqu’on examine le nombre d’utilisateurs uniques, l’analyse Canvas est-elle plus précise que la segmentation ?

La segmentation est une statistique plus précise pour les données de l’utilisateur unique par rapport aux statistiques de Canvas ou de la campagne. Cela est dû au fait que les statistiques Canvas et des campagnes sont des nombres incrémentés par Braze en fonction des opérations effectuées. En d’autres termes, des variables peuvent entraîner cette différence de nombre par rapport à l’outil de segmentation. Par exemple, des utilisateurs peuvent effectuer plus de conversions pour un Canvas ou une campagne.  

### Pourquoi le nombre d’utilisateurs qui accèdent à un Canvas ne correspond pas au nombre prévu ?

Le nombre d’utilisateurs accédant à un Canvas peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d’attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) est utilisé). Les utilisateurs seront alors exclus du Canvas s’ils ne font pas partie de l’audience que vous avez sélectionnée, avant l’évaluation des actions de déclenchement.
