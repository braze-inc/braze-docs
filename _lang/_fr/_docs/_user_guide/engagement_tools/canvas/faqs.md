---
nav_title: Foire aux questions
article_title: FAQ sur la toile
page_order: 10
description: "Cet article fournit des réponses aux questions fréquemment posées sur Canvas."
tool: Toile
---

# FAQ sur la toile

> Cet article fournit des réponses à certaines questions fréquemment posées au sujet de Canvas.

### Que se passe-t-il si le public et le temps d'envoi sont identiques pour une toile qui a une variante, mais plusieurs branches?

Nous mettons en file d'attente un emploi pour chaque étape, ils courent à la même heure, et l'un d'eux "gagne". Dans la pratique, cela peut être trié de manière un peu égale, mais il est probable qu'il y ait au moins un léger parti pris pour l'étape qui a été créée en premier.

De plus, nous ne pouvons pas garantir exactement à quoi ressemblera cette distribution. Si vous voulez vous assurer une division pair, ajoutez un filtre [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/) pour vous assurer qu'il soit bien divisé.

### Que se passe-t-il lorsque vous arrêtez un Canvas?

Lorsque vous arrêtez un Canvas, ce qui suit s'applique :

- Les utilisateurs ne seront pas autorisés à entrer dans le Canvas.
- Aucun autre message ne sera envoyé, malgré l'endroit où un utilisateur est dans le flux.
- **Exception :** Les Canevas Email ne s'arrêteront pas immédiatement. Une fois que les demandes d'envoi sont envoyées à SendGrid, nous ne pouvons rien faire pour les empêcher d'être livrés à l'utilisateur.

{% alert note %}
Arrêt d'une Canvas n'effacera pas les utilisateurs qui attendent de recevoir des messages. Si vous réactivez le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (sauf si le temps où le message leur a été envoyé, alors ils ne le recevront pas).
{% endalert %}

### Quand un événement d’exception se déclenche-t-il?

[Événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) ne se déclenche que lorsque l'utilisateur attend de recevoir l'étape Canvas à laquelle elle est associée. Si un utilisateur effectue une action à l'avance, l'événement d'exception ne se déclenchera pas.

Si vous voulez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) à la place.

### Comment la modification d'un Canvas affecte-t-elle les utilisateurs déjà présents dans le Canvas?

Si vous modifiez certaines des étapes d'une toile en plusieurs étapes, les utilisateurs qui étaient déjà dans le public mais qui n'ont pas reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que si elles n'ont pas encore été évitées.

Pour plus d'informations sur ce que vous pouvez ou ne pouvez pas modifier après le lancement, consultez [Changer votre Canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/change_your_canvas_after_launch/).

### Comment les conversions d’utilisateurs sont-elles suivies dans un Canvas?

Un utilisateur ne peut convertir qu'une seule fois par entrée sur Canvas .

Les conversions sont assignées au message le plus récent reçu par l'utilisateur pour cette entrée. Le bloc de résumé au début d'une toile reflète toutes les conversions effectuées par les utilisateurs dans ce chemin, qu'ils aient reçu ou non un message. Chaque étape suivante ne montrera que les conversions qui se sont produites alors que c'était l'étape la plus récente que l'utilisateur a reçu.

{% details Examples %}

#### Exemple 1

Il y a un chemin Canvas avec 10 notifications push et l'événement de conversion est "démarrage de la session" ("Ouvre l'application") :

- L'utilisateur A ouvre l'application après avoir entré mais avant de recevoir le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :** Le résumé montrera deux conversions alors que les étapes individuelles montreront une conversion d'une sur la première étape et zéro pour toutes les étapes suivantes.

{% alert note %}
Si des heures silencieuses sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.
{% endalert %}

#### Exemple 2

Il y a une toile en une étape avec des heures silencieuses :

1. L'utilisateur entre dans le Canevas.
2. La première étape n'a pas de délai, mais est dans les heures silencieuses, donc le message est supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :** L'utilisateur comptera comme converti dans la variante globale de Canvas, mais pas l'étape depuis qu'il n'a pas reçu l'étape.

{% enddetails %}

### Lorsqu’on regarde le nombre d’utilisateurs uniques, l’analyse de Canvas ou le segmenteur est-il plus précis?

Le segmenteur est une statistique plus précise pour les données utilisateur uniques contre Canvas ou les statistiques de campagne. C'est parce que les statistiques de Canvas et de campagne sont des nombres que Braze incrémente quand quelque chose se passe — ce qui signifie qu'il y a des variables qui pourraient faire que ce nombre soit différent de celui du segmenter. Par exemple, les utilisateurs peuvent convertir plusieurs fois pour une Canvas ou une campagne.  
