---
nav_title: FAQ
article_title: FAQ Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Cet article fournit des réponses aux questions fréquemment posées sur Canvas."
tool: Canvas

---

# Foire aux questions

> Cet article fournit des réponses à des questions fréquemment posées sur Canvas.

### Combien d'étapes puis-je inclure dans un canvas ?

Vous pouvez ajouter jusqu'à 200 étapes dans un canvas.

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour un canvas qui a une variante, mais plusieurs branches ?

Nous mettons en file d'attente un travail pour chaque étape : ils sont exécutés à peu près simultanément et l'un d'entre eux « gagne ». En pratique, ce processus peut être quelque peu uniforme, mais il y a parfois une légère distorsion en faveur de l'étape créée en premier. 

De plus, nous ne pouvons pas garantir avec précision ce à quoi ressemblera cette répartition. Si vous souhaitez une répartition égale, ajoutez un filtre de [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Puis-je lancer un canvas avec des étapes déconnectées ?

Oui. Vous pouvez également enregistrer vos Canvas après lancement avec des étapes déconnectées. 

### Où les utilisateurs se rendent-ils lorsqu'ils ont atteint une étape déconnectée ?

Si un utilisateur se trouve à une étape déconnectée de votre flux de travail Canvas, il passera à l'étape suivante, s'il y en a une, et les paramètres de l'étape détermineront la manière dont l'utilisateur doit avancer. Cette fonctionnalité est prévue pour permettre aux utilisateurs d'effectuer des changements sur des étapes sans avoir à les connecter directement au reste du canvas. Cela vous offre également la possibilité de tester avant de mettre en production immédiatement, en permettant d'enregistrer un brouillon.

Nous vous recommandons de vérifier l'affichage des analyses pour les utilisateurs en attente dans une étape du canvas avant de la déconnecter.

### Que se passe-t-il lorsque vous arrêtez un canvas ?

Lorsque vous arrêtez un canvas, les éléments suivants s'appliquent :

- L'accès au canvas sera bloqué pour les utilisateurs.
- Plus aucun message ne sera envoyé, quel que soit le niveau auquel se situe un utilisateur dans le flux.
- **Exception :** Les Canvas avec des e-mails ne seront pas automatiquement arrêtés. Une fois que les requêtes d'envoi sont transmises à Sendgrid, nous ne pouvons rien faire pour arrêter la distribution à l'utilisateur.

### Dois-je créer un seul canvas ou des canvas distincts par cycle de vie de l'utilisateur ?

En fonction de ce que vous cherchez à accomplir avec votre canvas, vous pouvez avoir besoin de différentes approches dans la façon dont vous créez votre parcours utilisateur. La flexibilité de Canvas vous permet de mapper les parcours des utilisateurs pour n'importe quelle étape du cycle de vie de l'utilisateur. Consultez nos [modèles de canvas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) pour obtenir plusieurs exemples d'approches rationalisées pour créer des parcours utilisateurs efficaces.

### Quand les messages in-app sont-ils envoyés dans Canvas ?

Les messages in-app sont envoyés au démarrage de la session suivante. Cela signifie que si l'utilisateur entre dans l'étape du canvas avant que le canvas ne soit interrompu, il recevra toujours le message in-app lors de son prochain démarrage de session, tant que le message in-app n'a pas encore expiré.

Il est possible qu'un utilisateur démarre une session avant l'arrêt du canvas, mais qu'il ne reçoive pas immédiatement le message in-app. Cela peut se produire si le message in-app est déclenché par un événement personnalisé ou est retardé. Il est donc possible pour un utilisateur d'enregistrer une impression de message in-app et de « recevoir » le message in-app après l'arrêt du canvas. Cependant, l'utilisateur aurait dû démarrer la session avant l'arrêt du canvas, mais **après avoir** reçu l'étape du canvas.

{% alert note %}
L'arrêt d'un canvas ne forcera pas les utilisateurs en attente de réception de messages à quitter leur parcours utilisateur. Si vous réactivez le canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le temps d'envoi du message se soit écoulé, auquel cas ils ne le recevront pas).
{% endalert %}

### À quel moment un événement d'exception est-il déclenché ?

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action à l'avance, l'événement d'exception ne sera pas déclenché. Si vous souhaitez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### En quoi la modification d'un canvas affecte-t-elle les utilisateurs déjà présents dans le canvas ?

Si vous modifiez certaines étapes d'un canvas à plusieurs étapes, les utilisateurs qui étaient déjà dans l'audience, mais n'ayant pas encore reçu les étapes, recevront la version mise à jour du message. Notez que ce cas se produit uniquement s'ils n'ont pas encore été évalués pour l'étape.

Pour plus d'informations sur ce que vous pouvez modifier après le lancement, reportez-vous à la section [Modifier votre canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

### Comment le suivi des conversions utilisateur est-il effectué dans Canvas ?

Un utilisateur peut uniquement effectuer une conversion par entrée Canvas. Les conversions sont affectées au message le plus récent reçu par l'utilisateur pour cette entrée. Le bloc de synthèse au début d'un canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu un message ou non. Chaque étape suivante affichera uniquement les conversions effectuées lorsque l'utilisateur a reçu l'étape la plus récente.

{% alert note %}
Lorsqu'un utilisateur entre à nouveau dans un canvas, les événements de conversion ne sont suivis que pour l'entrée la plus récente. Les événements de conversion ne sont pas enregistrés pour les entrées antérieures, même si l'événement de conversion est complété rétroactivement.
{% endalert %}

{% details Développer pour voir des exemples %}

**Exemple 1**

Il existe un parcours Canvas avec 10 notifications push et l'événement de conversion est « lancement de session » (« Ouvre l'application ») :

- L'utilisateur A ouvre l'application après l'entrée, mais avant la réception du premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :** Le résumé indiquera deux conversions, tandis que les étapes individuelles indiqueront une conversion de un pour la première étape et de zéro pour toutes les étapes suivantes.

{% alert note %}
Si des heures calmes sont actives lorsque l'événement de conversion se produit, les mêmes règles s'appliquent.
{% endalert %}

**Exemple 2**

Il existe un canvas à une seule étape avec les heures calmes activées :

1. L'utilisateur accède au canvas.
2. La première étape ne présente pas de retard, mais se situe dans les heures calmes, le message est donc supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :** La conversion de l'utilisateur sera prise en compte dans l'ensemble de la variante du canvas, mais pas dans l'étape, faute d'avoir été reçue.

{% enddetails %}

### Quelle est la différence entre les différents types de taux de conversion ?

- Le nombre total de conversions Canvas reflète le nombre d'utilisateurs uniques ayant effectué un événement de conversion, et non le nombre de conversions effectuées par chacun d'entre eux. 
- Le taux de conversion de la variante ou le bloc de synthèse au début d'un canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu'ils aient reçu un message ou non, sous forme d'un total agrégé. 
- Le taux de conversion d'étape illustre le nombre d'individus qui ont reçu cette étape de message et terminé n'importe lequel des événements de conversion décrits.

### Quelle est la différence entre un composant et une étape ?

Un [composant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) est une partie individuelle de votre canvas que vous pouvez utiliser pour déterminer l'efficacité de votre canvas. Les composants peuvent comprendre des actions telles que découper votre parcours utilisateur, ajouter un délai et même tester plusieurs parcours Canvas. Une étape du canvas fait référence au parcours utilisateur personnalisé dans les branches du canvas. Pour simplifier, votre canvas est constitué de composants individuels qui créent des étapes dans votre parcours utilisateur.

### Comment puis-je afficher les analyses pour chacun des composants de mon canvas ?

Pour afficher l'analyse d'un composant Canvas, accédez à votre canvas et faites défiler la page **Détails du Canvas.** Vous pouvez y visualiser les analyses de chacun des composants. Consultez l'[analyse de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour plus de détails.

### Lorsqu'on examine le nombre d'utilisateurs uniques, l'analyse Canvas est-elle plus précise que la segmentation ?

La segmentation est une statistique plus précise pour les données de l'utilisateur unique par rapport aux statistiques de Canvas ou de la campagne. En effet, les statistiques des Canvas et des campagnes sont des nombres que Braze incrémente lorsque quelque chose se produit, ce qui signifie qu'il existe des variables qui pourraient faire en sorte que ce nombre soit différent de celui de la segmentation. Par exemple, des utilisateurs peuvent effectuer plusieurs conversions pour un canvas ou une campagne.

### Pourquoi le nombre d'utilisateurs qui accèdent à un canvas ne correspond-il pas au nombre prévu ?

Le nombre d'utilisateurs accédant à un canvas peut être différent du nombre prévu selon le mode d'évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Les utilisateurs seront alors exclus du canvas s'ils ne font pas partie de l'audience que vous avez sélectionnée, avant l'évaluation des actions de déclenchement.

### Qu'advient-il des utilisateurs anonymes au cours de leur parcours dans Canvas ?

Bien que les utilisateurs anonymes puissent entrer et sortir de Canvas, leurs actions ne sont pas associées à un profil utilisateur spécifique tant qu'ils ne sont pas identifiés, de sorte que leurs interactions peuvent ne pas être entièrement suivies dans votre analyse. Vous pouvez utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/) pour générer un rapport sur ces indicateurs.

### Pourquoi le taux de conversion de mon étape du canvas est-il différent du taux de conversion total de ma variante du canvas ?

Il est fréquent que le total des conversions pour une variante du canvas soit plus élevé que la somme des totaux de ses étapes. Cela s'explique par le fait qu'un utilisateur peut effectuer un événement de conversion pour une variante dès qu'il entre dans la variante. Cependant, ce même événement de conversion n'est pas compté pour une étape du canvas. Ainsi, tout utilisateur qui entre dans le canvas et effectue l'événement de conversion avant de recevoir la première étape du canvas sera comptabilisé dans le total de conversion de la variante, et non dans le total des étapes. La même chose est vraie pour un utilisateur qui entre dans le canvas, mais quitte le canvas avant de recevoir une étape quelconque.

### Comment les audiences de Canvas sont-elles évaluées ? 

Par défaut, les filtres et segments pour des étapes complètes dans le canvas sont vérifiés à l'heure de l'envoi. L'étape de l'arbre décisionnel effectue une évaluation juste après la réception d'une étape précédente (ou avant un délai).

{% alert tip %}
Pour obtenir une aide supplémentaire dans la résolution des problèmes liés à Canvas, veillez à contacter l'assistance Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

### Quelle est la différence entre « N'est pas entré dans la variation Canvas » et « N'est pas dans le groupe de contrôle Canvas » ?

Reportez-vous à la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour obtenir les définitions complètes des filtres.

#### N'est pas entré dans la variation de Canvas

L'utilisateur n'a jamais emprunté un chemin de variation d'un canvas spécifique. Tous les utilisateurs qui ne font pas partie du groupe de contrôle sont inclus, qu'ils soient ou non entrés dans le canvas. Cela inclut les utilisateurs qui ont emprunté une autre variante et les utilisateurs qui n'ont emprunté aucune variante. 

#### Ne fait pas partie du groupe de contrôle de Canvas

L'utilisateur est entré dans le canvas, mais ne fait pas partie du groupe de contrôle et a donc reçu une variante. Cela ne concerne que les utilisateurs qui sont entrés dans le canvas.

Notez que l'affectation des variations a lieu à l'entrée du canvas. Si un utilisateur n'est pas entré dans un canvas, aucune variante ne lui sera attribuée. En d'autres termes, il ne fera pas partie du groupe de contrôle ni d'une variante.

{% details Développer pour voir les FAQ de l'éditeur Canvas d'origine %}

### Comment convertir un canvas existant de l'éditeur d'origine vers l'éditeur actuel ?

Vous pouvez [cloner votre Canvas]({{site.baseurl}}/cloning_canvases/). Cela permet de créer une copie de votre canvas d'origine dans le flux de travail Canvas le plus récent.

### Quelles sont les principales différences entre l'éditeur actuel et l'éditeur d'origine de Canvas ?

#### Barre d'outils du composant Canvas

Auparavant, avec l'éditeur Canvas d'origine, une étape complète était ajoutée par défaut chaque fois que vous ajoutiez une étape dans votre parcours utilisateur. Ces étapes complètes sont remplacées par différents composants Canvas, ce qui vous permet de bénéficier d'une visibilité et d'une personnalisation accrues pour votre expérience d'édition. Vous pouvez immédiatement voir tous vos composants Canvas dans la barre d'outils de l'étape du canvas.

#### Comportement des étapes

Auparavant, chaque étape complète comprenait des informations telles que les paramètres de délai et de planification, les événements d'exception, les filtres d'audience, la configuration des messages et les options d'avancement des messages dans un seul composant. Il s'agit de paramètres distincts dans l'éditeur actuel afin de rendre votre expérience Canvas plus personnalisable et d'introduire quelques différences de fonctionnalité.

#### Avancement du composant de message

[Les composants de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) font avancer tous les utilisateurs qui entrent dans l'étape. Il n'est pas nécessaire de spécifier le comportement d'avancement des messages, ce qui facilite la configuration générale de l'étape. Si vous souhaitez mettre en œuvre l'option **Avance lors de l'envoi du message**, ajoutez un parcours d'audience distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.  

#### Délai du comportement « dans »

Les [composants de temporisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) attendent la durée totale de la temporisation avant de passer à l'étape suivante. 

Par exemple, le 12 avril, nous avons un composant de délai configuré pour transférer l'utilisateur à l'étape suivante un jour plus tard, à 14 h 00. Un utilisateur entre dans le composant à 14 h 01 le 13 avril. 
- Pour le flux de travail d'origine, l'utilisateur passe à l'étape suivante à 14 h 00 le 14 avril, soit moins d'un jour après l'entrée. 
- Dans l'éditeur actuel, l'utilisateur passera à l'étape suivante le 15 avril à 14 h 00. Notez qu'il s'agit de la même heure, mais plus d'un jour après l'heure d'entrée. 

#### Comportement du timing intelligent

Étant donné que le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) est stocké dans le composant Message, les retards seront appliqués avant les calculs du timing intelligent. Cela signifie que, en fonction de l'heure à laquelle l'utilisateur accède au composant, il peut recevoir le message plus tard que dans un canvas créé avec le flux de travail Canvas d'origine.

Imaginons que votre délai est réglé sur 2 jours, que le timing intelligent est activé et qu'il a déterminé que la meilleure heure d'envoi de votre message était à 14 h 00. Un utilisateur entre dans l'étape de délai à 14 h 01.
- **Flux de travail actuel :** Il faudra 48 heures pour que le délai s'achève et l'utilisateur recevra donc le message le troisième jour à 14 h 00.
- **Flux de travail d'origine :** L'utilisateur reçoit le message le deuxième jour à 14 h 00.

Prenez en compte le fait que si le timing intelligent est activé, le message sera envoyé dans les 24 heures suivant l'entrée de l'utilisateur dans le composant de message à l'heure intelligente identifiée (même si aucun composant de délai n'est impliqué).

#### Événements d'exception

##### Heures calmes

L'événement d'exception est appliqué à l'aide de parcours d'action, qui sont distincts des étapes du message. Les heures calmes sont appliquées dans le composant de message. Cela signifie que si un utilisateur a déjà passé le parcours d'action (et n'a pas été exclu par l'événement d'exception), qu'il rencontre des heures calmes lorsqu'il arrive au composant Message et que son canvas est configuré de manière à ce que le message soit envoyé à nouveau après la période d'heures calmes, l'événement d'exception ne s'appliquera plus. Notez que ce cas d'utilisation n'est pas fréquent.

Pour les segments et les filtres, l'étape Message dispose de validations de réception/distribution qui permettent aux utilisateurs de configurer des segments et des filtres supplémentaires qui sont validés au moment de l'envoi. Cela empêche le cas susmentionné avec les heures calmes.

##### Réglage de la planification « dans » ou « suivant »/« prochain »

Les événements d'exception sont créés à l'aide de parcours d'action. Les parcours d'action ne prennent en charge que l'expression « après une fenêtre de temps X » et non « dans X temps » ou « au prochain X temps ».

{% enddetails %}

### Que dois-je inclure lorsque je soumets un ticket d'assistance pour une erreur « Request Timed Out » ?

Si vous rencontrez une erreur « Request Timed Out » lors de la modification d'un canvas et que vous devez contacter l'[assistance Braze]({{site.baseurl}}/braze_support/), incluez les informations suivantes pour accélérer la résolution :

- **Enregistrement d'écran :** Un enregistrement des étapes que vous avez effectuées avant de voir l'erreur, y compris les transitions de page.
- **Horodatage et fuseau horaire :** L'heure exacte à laquelle l'erreur s'est produite et votre fuseau horaire.
- **Navigateur et version :** Le navigateur que vous utilisez (par exemple, Chrome 120, Safari 17) et si vous avez essayé de reproduire l'erreur dans un autre navigateur.
- **Étapes de reproduction :** Une description claire des actions qui déclenchent l'erreur, y compris les étapes ou configurations spécifiques du canvas concernées.
- **Journaux réseau (facultatif) :** Ouvrez les outils de développement de votre navigateur (onglet **Réseau**), reproduisez l'erreur et exportez le journal réseau sous forme de fichier journal HTTP Archive (HAR). Cela aide l'équipe d'assistance à identifier quel appel API est en dépassement de délai.