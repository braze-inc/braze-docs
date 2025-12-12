---
nav_title: FAQ
article_title: FAQ sur les toiles
page_order: 8
alias: "/canvas_v2_101/"
description: "Cet article fournit des réponses aux questions fréquemment posées sur Canvas."
tool: Canvas

---

# Questions fréquemment posées

> Cet article apporte des réponses à certaines questions fréquemment posées à propos de Canvas.

### Combien d'étapes puis-je inclure dans un canvas ?

Vous pouvez ajouter jusqu'à 200 étapes dans un canvas.

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour une toile qui a une variante, mais plusieurs branches ?

Nous mettons en file d'attente un travail pour chaque étape - ils s'exécutent à peu près en même temps, et l'un d'entre eux "gagne". Dans la pratique, le tri peut être assez uniforme, mais il est probable qu'il y ait au moins un léger biais en faveur de l'étape qui a été créée en premier. 

En outre, nous ne pouvons donner aucune garantie quant à la forme exacte que prendra cette distribution. Si vous souhaitez une répartition uniforme, ajoutez un filtre de [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Puis-je lancer un canvas avec des étapes déconnectées ?

Oui. Vous pouvez également enregistrer des toiles après le lancement avec des étapes déconnectées. 

### Où les utilisateurs se rendent-ils lorsqu'ils ont atteint une étape déconnectée ?

Si un utilisateur se trouve à une étape déconnectée de votre flux de travail Canvas, il passera à l'étape suivante, s'il y en a une, et les paramètres de l'étape détermineront la manière dont l'utilisateur doit avancer. L'objectif est de permettre aux utilisateurs d'apporter des modifications aux étapes sans avoir à les relier directement au reste du Canvas. Vous disposez ainsi d'une certaine marge de manœuvre pour effectuer des tests avant de passer immédiatement à la ligne/en production/instantanée, ce qui vous permet d'enregistrer un brouillon.

Nous vous recommandons de vérifier la vue analyse/analytique des utilisateurs en attente dans une étape du canvas avant de déconnecter une étape.

### Que se passe-t-il lorsque vous arrêtez une toile ?

Lorsque vous arrêtez une toile, les règles suivantes s'appliquent :

- Les utilisateurs ne pourront pas entrer dans la toile.
- Aucun autre message ne sera envoyé, quelle que soit la position de l'utilisateur dans le flux.
- **Exception :** Les toiles contenant des e-mails ne s'arrêteront pas immédiatement. Une fois que les demandes d'envoi sont envoyées à Sendgrid, nous ne pouvons rien faire pour les empêcher d'être transmises à l'utilisateur.

### Dois-je créer un seul canvas ou des canvas distincts par cycle de vie de l'utilisateur ?

En fonction de ce que vous cherchez à accomplir avec votre Canvas, vous pouvez avoir besoin de différentes approches dans la façon dont vous créez votre parcours utilisateur. La flexibilité de Canvas vous permet de mapper les parcours des utilisateurs pour n'importe quelle étape du cycle de vie de l'utilisateur. Consultez nos [modèles de canvas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) pour obtenir plusieurs exemples d'approches rationalisées pour créer des parcours utilisateurs efficaces.

### Quand les messages in-app sont-ils envoyés dans Canvas ?

Les messages in-app sont envoyés au démarrage de la session suivante. Cela signifie que si l'utilisateur entre dans l'étape du canvas avant que le canvas ne soit arrêté, il recevra toujours le message in-app au début de sa prochaine session, tant que le message in-app n'a pas expiré.

Il est possible qu'un utilisateur démarre une session avant l'arrêt du Canvas, mais qu'il ne reçoive pas immédiatement le message in-app. Cela peut se produire si le message in-app est déclenché par un événement personnalisé ou est retardé. Cela signifie qu'il est possible pour un utilisateur d'enregistrer une impression de message in-app et de "recevoir" le message in-app après l'arrêt du Canvas. Cependant, l'utilisateur aurait dû démarrer la session avant l'arrêt du canvas, mais **après avoir** reçu l'étape du canvas.

{% alert note %}
L'arrêt d'un canvas n'entraînera pas la sortie du parcours utilisateur des utilisateurs qui attendent de recevoir des messages. Si vous réactivez le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (sauf si la date à laquelle le message aurait dû leur être envoyé est passée, auquel cas ils ne le recevront pas).
{% endalert %}

### Quand un événement d'exception se déclenche-t-il ?

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action à l'avancement, l'événement d'exception ne se déclenchera pas. Si vous souhaitez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Comment la modification d'un Canvas affecte-t-elle les utilisateurs déjà présents dans le Canvas ?

Si vous modifiez certaines des étapes d'un Canvas à plusieurs étapes, les utilisateurs qui faisaient déjà partie de l'audience mais qui n'ont pas reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que s'ils n'ont pas encore été évalués pour l'étape en question.

Pour plus d'informations sur ce que vous pouvez modifier après le lancement, reportez-vous à la section [Modifier votre canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

### Comment les conversions des utilisateurs sont-elles suivies dans un canvas ?

Un utilisateur ne peut effectuer qu'une seule conversion par entrée dans le canvas. Les conversions sont attribuées au message le plus récent reçu par l'utilisateur pour cette entrée. Le bloc de résumé au début d'un canvas reflète toutes les conversions effectuées par les utilisateurs à l'intérieur de ce canvas, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions qui se sont produites pendant l'étape la plus récente que l'utilisateur a reçue.

{% details Expand for examples %}

**Exemple 1**

Il y a un parcours Canvas avec 10 notifications push et l'événement de conversion est " début de session " (" ouvre l'appli ") :

- L'utilisateur A ouvre l'appli après être entré mais avant d'avoir reçu le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :** Le résumé indiquera deux conversions, tandis que les étapes individuelles indiqueront une conversion de un pour la première étape et de zéro pour toutes les étapes suivantes.

{% alert note %}
Si les heures calmes sont actives au moment de l'événement de conversion, les mêmes règles s'appliquent.
{% endalert %}

**Exemple 2**

Il existe un Canvas en une étape avec les heures calmes activées :

1. L'utilisateur entre dans le Canvas.
2. La première étape ne comporte pas de délai, mais se situe dans les heures calmes définies, de sorte que le message est supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :** L'utilisateur sera comptabilisé comme converti dans la variante globale du canvas, mais pas l'étape puisqu'il n'a pas reçu l'étape.

{% enddetails %}

### Quelle est la différence entre les différents types de taux de conversion ?

- Le nombre total de conversions Canvas reflète le nombre d'utilisateurs uniques ayant effectué un événement de conversion, et non le nombre de conversions effectuées par chacun d'entre eux. 
- La variante taux de conversion ou bloc récapitulatif au début d'un canvas reflète toutes les conversions effectuées par les utilisateurs au sein de ce parcours, qu'ils aient ou non reçu un message, sous la forme d'un total agrégé. 
- Le taux de conversion reflète le nombre de personnes qui ont reçu l'envoi du message et qui ont effectué l'un des événements de conversion décrits.

### Quelle est la différence entre un composant et une étape ?

Un [composant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) est une partie individuelle de votre Canvas que vous pouvez utiliser pour déterminer l'efficacité de votre Canvas. Les composants peuvent inclure des actions telles que la division de votre parcours utilisateur, l'ajout d'un délai, et même le test de plusieurs parcours Canvas. Une étape du canvas fait référence au parcours personnalisé de l'utilisateur dans vos branches Canvas. Essentiellement, votre Canvas est constitué de composants individuels qui créent des étapes pour votre parcours utilisateur.

### Comment puis-je consulter les analyses/analytiques pour chacun de mes composants Canvas ?

Pour afficher l'analyse/analytique d'un composant Canvas, accédez à votre Canvas et faites défiler la page **Détails du Canvas**. Ici, vous pouvez consulter les analyses/analytiques de chaque composant. Consultez l'[analyse/analytique de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour plus de détails.

### Si l'on considère le nombre d'utilisateurs uniques, l'analyse/analytique de Canvas ou la segmentation est-elle plus précise ?

Le segmenteur est une statistique plus précise pour les données d'utilisateurs uniques par rapport aux statistiques de Canvas ou de campagne. En effet, les statistiques des Canvas et des campagnes sont des nombres que Braze incrémente lorsque quelque chose se produit, ce qui signifie qu'il existe des variables qui pourraient faire en sorte que ce nombre soit différent de celui de la segmentation. Par exemple, les utilisateurs peuvent se convertir plusieurs fois pour un canvas ou une campagne.

### Pourquoi le nombre d'utilisateurs entrant dans un canvas ne correspond-il pas au nombre attendu ?

Le nombre d'utilisateurs entrant dans un Canvas peut différer de votre nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Les utilisateurs qui ne font pas partie de l'audience sélectionnée seront exclus de la toile avant que les actions déclencheurs ne soient évaluées.

### Qu'advient-il des utilisateurs anonymes au cours de leur parcours dans Canvas ?

Bien que les utilisateurs anonymes puissent entrer et sortir de Canvases, leurs actions ne sont pas associées à un profil utilisateur spécifique jusqu'à ce qu'ils soient identifiés, de sorte que leurs interactions peuvent ne pas être entièrement suivies dans votre analyse/analytique. Vous pouvez utiliser le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/query_builder/) pour générer un rapport sur ces indicateurs.

### Pourquoi le taux de conversion de mes étapes du canvas n'est-il pas égal au taux de conversion total de ma variante du canvas ?

Il est fréquent que le total de la conversion d'une variante du canvas soit supérieur à la somme de ses étapes. Cela s'explique par le fait qu'un utilisateur peut effectuer un événement de conversion pour une variante dès qu'il entre dans cette variante. Cependant, ce même événement de conversion ne compte pas pour une étape du canvas. Ainsi, tout utilisateur qui entre dans le Canvas et effectue l'événement de conversion avant de recevoir la première étape du Canvas sera comptabilisé dans le total de la variante de conversion et non dans le total des étapes. Il en va de même pour un utilisateur qui entre dans le canvas mais en sort avant d'avoir reçu une étape.

### Comment les audiences de Canvas sont-elles évaluées ? 

Par défaut, les filtres et les segments pour les étapes complètes du canvas sont vérifiés au moment de l'envoi. L'étape de l'arbre décisionnel effectue une évaluation juste après la réception d'une étape précédente (ou avant un délai).

{% alert tip %}
Pour obtenir une aide supplémentaire dans la résolution des problèmes liés à Canvas, veillez à contacter le service d'assistance de Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Quelle est la différence entre "N'est pas entré dans la variation Canvas" et "N'est pas dans le groupe de contrôle Canvas" ?

Reportez-vous à la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour obtenir les définitions complètes des filtres.

#### N'est pas entré dans la variation de Canvas

L'utilisateur n'a jamais saisi de chemin de variation d'un Canvas spécifique. Tous les utilisateurs qui ne font pas partie du groupe de contrôle sont inclus, qu'ils soient ou non entrés dans le Canvas. Cela inclut les utilisateurs qui ont saisi une autre variante et les utilisateurs qui n'ont saisi aucune variante. 

#### Ne fait pas partie du groupe de contrôle de Canvas

L'utilisateur est entré dans le Canvas, mais ne fait pas partie du groupe de contrôle et a donc reçu une variante. Cela ne concerne que les utilisateurs qui sont entrés dans le Canvas.

Notez que l'affectation des variations a lieu à l'entrée de la toile. Si un utilisateur n'a pas saisi de canvas, aucune variante ne lui sera attribuée. En d'autres termes, ils ne feront pas partie du groupe de contrôle ou d'une variante.

{% details Expand for original Canvas editor FAQs %}

### Comment convertir un canvas existant de l'éditeur d'origine vers l'éditeur actuel ?

Vous pouvez [cloner votre Canvas]({{site.baseurl}}/cloning_canvases/). Cela permet de créer une copie de votre canvas original dans le flux de travail Canvas le plus récent.

### Quelles sont les principales différences entre les éditeurs actuels et les éditeurs originaux de Canvas ?

#### Barre d'outils du composant canvas

Auparavant, avec l'éditeur Canvas original, une étape complète était ajoutée par défaut chaque fois que vous créiez une étape dans votre parcours utilisateur. Ces étapes complètes sont remplacées par différents composants Canvas, ce qui vous permet de bénéficier d'une visibilité et d'une personnalisation accrues pour votre expérience modificative. Vous pouvez immédiatement voir tous vos composants Canvas à partir de la barre d'outils de l'étape du canvas.

#### Comportement par étapes

Auparavant, chaque étape complète comprenait des informations telles que les paramètres de délai et de planification, les événements d'exception, les filtres d'audience, la configuration des messages et les options d'avancement des messages, le tout dans un seul et même composant. Il s'agit de paramètres distincts dans l'éditeur actuel afin de rendre votre expérience Canvas plus personnalisable et d'introduire quelques différences de fonctionnalité.

#### Envoi de messages à l'avancement

[Les composants du message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) font avancer tous les utilisateurs qui entrent dans l'étape. Il n'est pas nécessaire de spécifier le comportement d'avancement des messages, ce qui simplifie la configuration de l'ensemble de l'étape. Si vous souhaitez mettre en œuvre l'option **Avance lors de l'envoi du message**, ajoutez un parcours d'audience distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.  

#### Comportement de retardement

Les [composants de la temporisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) attendent la durée totale de la temporisation avant de passer à l'étape suivante. 

Supposons que le 12 avril, nous ayons un composant Délai dans lequel le délai est défini pour envoyer votre utilisateur à l'étape suivante dans un jour, à 14 heures. Un utilisateur entre dans le composant à 14h01 le 13 avril. 
- Dans le cas du flux de travail original, l'utilisateur passe à l'étape suivante à 14 heures le 14 avril, soit moins d'un jour après l'heure de saisie. 
- Dans l'éditeur actuel, l'utilisateur passera à l'étape suivante le 15 avril à 14 heures. Notez qu'il s'agit de la même heure, mais à plus d'un jour de l'heure d'entrée. 

#### Comportement de timing intelligent

Étant donné que le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) est stocké dans le composant Message, les retards seront appliqués avant les calculs du timing intelligent. Cela signifie que, selon le moment où l'utilisateur entre dans le composant, il peut recevoir le message plus tard qu'il ne le ferait dans un canvas créé avec le flux de travail original du canvas.

Supposons que votre délai soit fixé à 2 jours, que le timing intelligent soit activé et qu'il ait déterminé que le meilleur moment pour envoyer votre message est 14 heures. Un utilisateur entre dans l'étape Retard à 14h01.
- **Flux de travail actuel :** Il faut 48 heures pour que le délai s'écoule, de sorte que l'utilisateur reçoit le message le troisième jour à 14 heures.
- **Flux de travail original :** L'utilisateur reçoit le message le deuxième jour à 14 heures.

Notez que si le timing intelligent est activé, le message sera envoyé dans les 24 heures suivant la saisie par l'utilisateur du composant Message à l'heure intelligente identifiée (même si aucun composant Délai n'est impliqué).

#### Événements d'exception

##### Heures calmes

L'événement d'exception est appliqué à l'aide de parcours d'action, qui sont distincts des étapes du message. Les heures calmes sont appliquées dans la composante "messages". Cela signifie que si un utilisateur a déjà passé le parcours d'action (et n'a pas été exclu par l'événement d'exception), qu'il rencontre des heures calmes lorsqu'il arrive au composant Message et que son Canvas est configuré de manière à ce que le message soit envoyé à nouveau après la période d'heures calmes, l'événement d'exception ne s'appliquera plus. Notez que ce cas d'utilisation n'est pas courant.

Pour les segments et les filtres, l'étape Message dispose de validations de réception/distribution qui permettent aux utilisateurs de configurer des segments et des filtres supplémentaires qui sont validés au moment de l'envoi. Cela permet d'éviter le cas de figure des heures calmes mentionné plus haut.

##### Réglage de la planification "En" ou "Au prochain".

Les événements d'exception sont créés à l'aide de parcours d'action. Les parcours d'action ne prennent en charge que l'expression "après une fenêtre de temps X" et non "dans X temps" ou "au prochain X temps".

{% enddetails %}