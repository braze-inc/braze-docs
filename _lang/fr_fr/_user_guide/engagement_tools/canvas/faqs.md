---
nav_title: FAQ
article_title: FAQ Canvas
page_order: 8
alias: "/canvas_v2_101/"
description: "Cet article fournit des réponses aux questions fréquemment posées sur Canvas et Canvas Flow."
tool: Canvas

---

# Foire aux questions

> Cet article apporte des réponses à certaines questions fréquemment posées sur Canvas et [Canvas Flow](#canvas-flow).

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% endalert %}

## Généralités

### Que se passe-t-il si l’audience et l’heure d’envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ?

Nous mettons en file d’attente un travail pour chaque étape, ils sont exécutés à peu près simultanément et l’un d’entre eux « gagne ». En pratique ce processus peut être quelque peu uniforme, mais il y a parfois une légère distorsion par rapport à l’étape créée en premier. 

De plus, nous ne pouvons pas garantir avec précision ce à quoi ressemblera cette répartition. Si vous souhaitez une répartition égale, ajoutez un filtre de [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

### Que se passe-t-il lorsque vous arrêtez un Canvas ?

Lorsque vous arrêtez un Canvas, les éléments suivants s’appliquent :

- L’accès au Canvas sera bloqué pour les utilisateurs.
- Plus aucun message ne sera envoyé, quel que soit le niveau auquel se situe un utilisateur dans le flux.
- **Exception :** Les Canvas avec des e-mails ne seront pas automatiquement arrêtés. Une fois que les requêtes d’envoi sont transmises à SendGrid, nous ne pouvons rien faire pour arrêter la distribution à l’utilisateur.

### Dois-je créer un seul canvas ou des canvas distincts par cycle de vie de l'utilisateur ?

En fonction de ce que vous cherchez à accomplir avec votre Canvas, vous pouvez avoir besoin de différentes approches dans la façon dont vous créez votre parcours utilisateur. La flexibilité de Canvas vous permet de mapper les parcours des utilisateurs pour n'importe quelle étape du cycle de vie de l'utilisateur. Consultez nos [modèles de canvas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) pour obtenir plusieurs exemples d'approches rationalisées pour créer des parcours utilisateurs efficaces.

#### Messages in-app de Canvas

Les messages in-app sont envoyés au démarrage de la session suivante. Cela signifie que si l'utilisateur entre dans l'étape du canvas avant que le canvas ne soit interrompu, il recevra toujours le message in-app lors de son prochain démarrage de session, tant que le message in-app n'a pas encore expiré.

Il est possible qu'un utilisateur démarre une session avant l'arrêt du canvas, mais qu'il ne reçoive pas immédiatement le message in-app. Cela peut se produire si le message in-app est déclenché par un événement personnalisé ou est retardé. Cela signifie qu'il est possible pour un utilisateur d'enregistrer une impression de message in-app et de "recevoir" le message in-app après l'arrêt du Canvas. Cependant, l'utilisateur aurait dû démarrer la session avant l'arrêt du canvas, mais **après avoir** reçu l'étape du canvas.

{% alert note %}
L’arrêt de Canvas ne forcera pas les utilisateurs en attente de réception de messages à quitter leur parcours utilisateur. Si vous activez à nouveau le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (à moins que le temps d’envoi du message se soit écoulé, dans ce cas, ils ne le recevront pas).
{% endalert %}

### À quel moment un événement d’exception est-il déclenché ?

Les [événements d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action à l’avance, l’événement d’exception ne sera pas déclenché. Si vous souhaitez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### En quoi la modification d’un Canvas affecte-t-elle des utilisateurs déjà présents dans les Canvas ?

Si vous modifiez certaines étapes d’un Canvas à plusieurs étapes, les utilisateurs qui étaient déjà dans l’audience, mais n’ayant pas encore reçu les étapes, recevront la version mise à jour du message. Notez que ce cas se produit uniquement s’ils n’ont pas encore été évalués pour l’étape.

Pour plus d'informations sur ce que vous pouvez modifier après le lancement, consultez la rubrique [Modifier votre canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

### Comment le suivi des conversions utilisateur est-il effectué dans Canvas ?

Un utilisateur peut uniquement effectuer une conversion par entrée Canvas. Les conversions sont affectées au message le plus récent reçu par l’utilisateur pour cette entrée. Le blocage de synthèse au début d’un Canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu’ils aient reçu un message ou pas. Chaque message suivant affichera uniquement les conversions effectuées lorsque l’utilisateur a reçu l’étape la plus récente.

{% details Exemples %}

**Exemple 1**

Il existe un chemin Canvas avec 10 notifications push et l’événement de conversion est « lancement de session » (« Ouvre l’application ») :

- L’utilisateur A ouvre l’application après l’accès, mais avant la réception du premier message.
- L’utilisateur B ouvre l’application après chaque notification push.

**Résultat :** Le résumé indiquera deux conversions, tandis que les étapes individuelles indiqueront une conversion de un pour la première étape et de zéro pour toutes les étapes suivantes.

{% alert note %}
Si des heures calmes sont actives lorsque l’événement de conversion se produit, les mêmes règles s’appliquent.
{% endalert %}

**Exemple 2**

Il existe un Canvas à une seule étape avec les heures calmes activées :

1. L’utilisateur accède au Canvas.
2. La première étape ne présente pas de retard, mais se situe dans les heures calmes, le message est donc supprimé.
3. L’utilisateur effectue l’événement de conversion.

**Résultat :** La conversion de l’utilisateur sera prise en compte dans l’ensemble de Canvas Variant, mais pas l’étape, faute d’avoir été reçue.

{% enddetails %}

### Quelle est la différence entre les différents types de taux de conversion ?

- Le nombre total de conversions Canvas reflète le nombre d'utilisateurs uniques ayant effectué un événement de conversion, et non le nombre de conversions effectuées par chacun d'entre eux. 
- Le taux de conversion de la variante ou le bloc de synthèse au début d’un Canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu’ils aient reçu un message ou pas, sous forme d’un total additionné. 
- Le taux de conversion d’étape illustre le nombre d’individus qui ont reçu cette étape de message et terminé n’importe lequel des événements de conversion décrits.

### Quelle est la différence entre un composant et une étape ?

Un [composant]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) est une partie individuelle de votre Canvas que vous pouvez utiliser pour déterminer l'efficacité de votre Canvas. Les composants peuvent comprendre des actions telles que découper votre parcours utilisateur, ajouter un délai et même tester plusieurs parcours Canvas. Une étape du Canvas fait référence au parcours utilisateur personnalisé dans les branches du Canvas. Pour simplifier, votre Canvas est constitué de composants individuels qui créent des étapes dans votre parcours utilisateur.

### Comment puis-je afficher les analyses pour chacun des composants de mon Canvas ?

Pour afficher l'analyse/analytique d'un composant Canvas, accédez à votre Canvas et faites défiler la page **Détails du Canvas.**  Vous pouvez y visualiser les analyses de chacun des composants. Consultez l'[analyse/analytique de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour plus de détails.

### Lorsqu’on examine le nombre d’utilisateurs uniques, l’analyse Canvas est-elle plus précise que la segmentation ?

La segmentation est une statistique plus précise pour les données de l’utilisateur unique par rapport aux statistiques de Canvas ou de la campagne. En effet, les statistiques des Canvas et des campagnes sont des nombres que Braze incrémente lorsque quelque chose se produit, ce qui signifie qu'il existe des variables qui pourraient faire en sorte que ce nombre soit différent de celui de la segmentation. Par exemple, des utilisateurs peuvent effectuer plus de conversions pour un Canvas ou une campagne.

### Pourquoi le nombre d’utilisateurs qui accèdent à un Canvas ne correspond pas au nombre prévu ?

Le nombre d’utilisateurs accédant à un Canvas peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Les utilisateurs seront alors exclus du Canvas s’ils ne font pas partie de l’audience que vous avez sélectionnée, avant l’évaluation des actions de déclenchement.

### Qu'advient-il des utilisateurs anonymes au cours de leur parcours dans Canvas ?

Bien que les utilisateurs anonymes puissent entrer et sortir de Canvases, leurs actions ne sont pas associées à un profil utilisateur spécifique jusqu'à ce qu'ils soient identifiés, de sorte que leurs interactions peuvent ne pas être entièrement suivies dans votre analyse/analytique. Vous pouvez utiliser le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/query_builder/) pour générer un rapport sur ces indicateurs.

### Pourquoi est-ce que le taux de conversion de mon étape Canvas est différent du taux de conversion total de ma variante de Canvas ?

Il est fréquent que le total des conversions pour une variante de Canvas soit plus élevé que le total de ses étapes. La cause en est qu’un utilisateur peut effectuer un événement de conversion pour une variante dès qu’ils entrent dans la variante. Cependant, ce même événement de conversion n’est pas compté pour une étape Canvas. Ainsi, tout utilisateur qui entre dans le Canvas et effectue l'événement de conversion avant de recevoir la première étape du Canvas sera comptabilisé dans le total de la variante de conversion et non dans le total des étapes. La même chose est vraie pour un utilisateur qui entre dans le Canvas, mais quitte le Canvas avant de recevoir une étape quelconque.

### Comment les audiences de Canvas sont-elles évaluées ? 

Par défaut, les filtres et segments pour des étapes complètes dans le Canvas sont cochés à l’heure de l’envoi. Pour Canvas Flow, le composant de Décision de séparation effectue une évaluation juste après avoir reçu l’étape précédente (ou avant un délai).

{% alert tip %}
Pour obtenir une aide supplémentaire dans la résolution des problèmes liés à Canvas, veillez à contacter le service d'assistance de Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

## Canvas Flow

### Qu’est-ce que le Canvas Flow ?

Canvas Flow est l’expérience d’édition améliorée qui simplifie la façon dont les spécialistes du marketing peuvent développer et gérer leurs parcours d’utilisateur Canvas. Vous pouvez facilement voir et utiliser les composants Canvas dans le générateur de Canvas. Vous avez également accès à plus de fonctions de modification après le lancement pour modifier les connexions entre les étapes, supprimer les étapes et des variantes et rediriger les utilisateurs vers différentes étapes.

### Comment convertir un Canvas existant en Canvas Flow ?

Vous pouvez [cloner votre canvas dans Canvas Flow]({{site.baseurl}}/cloning_canvases/). Vous créerez ainsi une copie de votre Canvas d’origine dans le flux de travail Canvas Flow.

### Qu'adviendra-t-il des toiles que j'ai créées à l'aide de l'éditeur original ?

Tous vos Canvas existants et la version d’origine de Canvas continueront d’exister et seront pris en charge par Braze. Les clients qui choisissent de rejoindre Canvas Flow en accès anticipé auront la possibilité de créer un Canvas en utilisant le workflow Canvas d’origine ou de Flow.

### Y a-t-il une limite au nombre d'étapes que je peux inclure ?

Oui. Un Canvas créé en utilisant Canvas Flow peut comprendre jusqu’à 200 étapes.

### Puis-je lancer un Canvas avec des étapes déconnectées ?

Oui ! Canvas Flow vous permet de lancer votre Canvas avec des étapes déconnectées. Vous pouvez également sauvegarder vos Canvas après lancement avec des étapes déconnectées. 

### Où les utilisateurs se rendent-ils lorsqu'ils ont atteint une étape déconnectée ?

Si un utilisateur se trouve dans une étape déconnectée d’un de vos flux de travail Canvas Flow, ils avanceront à l’étape suivante s’il en existe une et les paramètres de l’étape dicteront comment l’utilisateur devrait avancer. Ceci est prévu pour permettre aux utilisateurs d’effectuer des changements sur des étapes sans avoir à les connecter directement au reste du Canvas. Ceci vous offre également la possibilité de tester avant de le mettre immédiatement en ligne en permettant donc de sauvegarder un brouillon.

Nous vous recommandons de vérifier l’affichage des analyses pour les utilisateurs en attente dans une étape Canvas avant de le déconnecter.

### Quelles sont les principales différences entre Canvas Flow et l’éditeur Canvas d’origine ?

#### Barre d’outils de composant de Canvas

Auparavant, avec l’éditeur Canvas d’origine, une étape complète était ajoutée par défaut chaque fois que vous ajoutiez une étape dans votre parcours utilisateur. Maintenant avec Canvas Flow, ces étapes complètes sont remplacées par différents composants Canvas, vous offrant ainsi une meilleure visibilité et personnalisation pour apporter des modifications. Vous pouvez immédiatement voir tous vos composants Canvas dans la barre d’outils de l'étape de Canvas.

#### Comportement des étapes

Auparavant, chaque étape complète comprenait des informations telles que les paramètres de délai et de planification, les événements d’exception, les filtres d’audience, la configuration des messages et les options d’avancement des messages dans un seul composant. Il s’agit de paramètres différents dans Canvas Flow pour rendre votre expérience de création de Canvas plus personnalisable et vous proposer des différences de fonctionnalité.

#### Avancement du composant de message

[Les composants du message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) font avancer tous les utilisateurs qui entrent dans l'étape. Il n’est pas nécessaire de spécifier le comportement d’avancement des messages, ce qui facilite la configuration générale de l’étape. Si vous souhaitez mettre en œuvre l'option **Avance lors de l'envoi du message**, ajoutez un parcours d'audience distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.  

#### Délai du comportement « dans »

Les [composants de la temporisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) attendent la durée totale de la temporisation avant de passer à l'étape suivante. 

Par exemple, le 12 avril, nous avons un composant de délai avec un délai défini de sorte que l’utilisateur est transféré sur l’étape suivante un jour plus tard, à 14 h 00. Un utilisateur saisit le composant à 14 h 01 le 13 avril. 
- Pour le flux de travail d’origine, l’utilisateur passe à l’étape suivante à 14 h 00 le 14 avril, moins d’un jour après l’entrée. 
- Pour Canvas Flow, l’utilisateur passera à l’étape suivante à 14 h 00 le 15 avril. Notez qu’il s’agit de la même heure, mais plus d’un jour après l’heure d’entrée. 

#### Comportement du Timing Intelligent

Étant donné que le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) est stocké dans le composant Message, les retards seront appliqués avant les calculs du timing intelligent. Cela signifie que, en fonction de l’heure à laquelle l’utilisateur accède au composant, il peut recevoir le message plus tard que dans un Canvas créé avec le flux de travail Canvas d’origine.

Imaginons que votre délai est réglé sur 2 jours, que le timing intelligent est activé et qu’il a déterminé que la meilleure heure d’envoi de votre message était à 14 h 00. Un utilisateur entre dans l’étape ayant un délai à 14 h 01.
- **Canvas Flow :** Il faudra 48 heures pour que le délai s’achève et l’utilisateur recevra donc le message le troisième jour à 14 h 00.
- **Flux de travail original :** L’utilisateur reçoit le message le deuxième jour à 14 h 00.

Prenez en compte le fait que si le timing intelligent est activé, le message sera envoyé dans les 24 heures suivant l’entrée de l’utilisateur dans le composant de message à l’heure intelligente identifiée (même si aucun composant de délai n’est impliqué).

#### Événements d'exception

##### Heures calmes

La fonctionnalité d’événement d’exception dans Canvas Flow fonctionne avec les parcours d’action, distincts des étapes de message. Les heures calmes sont appliquées dans le composant de message. Cela signifie que si un utilisateur a déjà franchi le parcours d’action (et n’a pas été exclu par l’événement d’exception à cet endroit), qu’il a atteint les heures calmes lorsqu’il est arrivé au composant de message, et que son Canvas a été configuré de telle sorte que le message soit renvoyé après la période des heures calmes, l’événement d’exception ne sera plus appliqué. Notez que ce cas d’utilisation n’est pas fréquent.

Pour les segments et filtres, le composant de message Canvas Flow comporte une nouvelle fonctionnalité appelée Validations de livraison qui permet aux utilisateurs de configurer des segments supplémentaires et des filtres validés au moment de l’envoi. Cela empêche le cas susmentionné avec les heures calmes.

##### Réglage de la planification « dans » ou « suivant »/« prochain »

Les événements d’exception dans Canvas Flow sont créés avec des parcours d’action. Les parcours d'action ne prennent en charge que l'expression "après une fenêtre de temps X" et non "dans X temps" ou "au prochain X temps".
