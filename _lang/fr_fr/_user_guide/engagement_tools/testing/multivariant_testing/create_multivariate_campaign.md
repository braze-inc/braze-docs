---
nav_title: Créer des tests
article_title: Créez des tests multivariés et des tests A/B
page_order: 1
page_type: reference
description: "Cet article explique comment créer des tests A/B et multivariés avec Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Créer des tests multivariés et des tests A/B {#creating-tests}

> Vous pouvez créer un [test multivarié ou un test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour toute campagne qui cible un seul canal et un seul appareil. Par exemple, si vous souhaitez utiliser le test multivarié ou le test A/B pour une campagne push, vous pouvez cibler uniquement les appareils iOS ou uniquement les appareils Android — et non les deux types d'appareils dans la même campagne.

![La liste déroulante qui apparaît en sélectionnant le bouton « Créer une campagne » permet de choisir entre le multicanal et le monocanal.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Étape 1 : Créer votre campagne

1. Accédez à **Envoi de messages** > **Campagnes**.
2. Sélectionnez **Créer une campagne** et un canal pour la campagne dans la section qui permet les tests multivariés et les tests A/B. Pour obtenir une documentation détaillée sur chaque canal de communication, reportez-vous à la section [Créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Étape 2 : Composer vos variantes

Vous pouvez créer jusqu'à huit variantes de votre message, en changeant les titres, le contenu, les images, etc. Le nombre de différences entre les messages détermine s'il s'agit d'un test multivarié ou d'un test A/B. Un test A/B examine l'effet de la modification d'une variable, alors qu'un test multivarié en examine deux ou plus.

Découvrez de nouvelles idées sur la manière de différencier vos variantes en consultant nos [conseils pour différents canaux](#tips-different-channels).

![Sélection de l'option « Ajouter une variante » pour une campagne.]({% image_buster /assets/img/ab_create_2.png %})

## Étape 3 : Planifier votre campagne

Planifier votre campagne multivariée fonctionne comme pour toute autre campagne Braze. Tous les [types de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) standard sont disponibles.

Après le début d'un test multivarié, vous ne pouvez plus apporter de modifications à la campagne. Si vous modifiez les paramètres, tels que la ligne d'objet ou le corps HTML, Braze considère que l'expérience est compromise et la désactive immédiatement.

{% alert important %}
Pour utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponible pour certains canaux), planifiez votre campagne pour qu'elle soit diffusée une seule fois. Les optimisations ne sont pas disponibles pour les campagnes récurrentes ou pour lesquelles la rééligibilité est activée.
{% endalert %}

## Étape 4 : Choisir un segment et répartir vos utilisateurs entre les variantes

Sélectionnez les segments à cibler, puis répartissez les membres entre les variantes sélectionnées et le [groupe de contrôle](#including-a-control-group) facultatif. Pour connaître les bonnes pratiques concernant le choix d'un segment de test, reportez-vous à la section [Choisir un segment](#choosing-a-segment).

Pour les campagnes push, e-mail et webhook planifiées pour être envoyées une seule fois, vous pouvez également utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Une optimisation réserve une partie de votre audience cible du test A/B et la retient pour un second envoi optimisé en fonction des résultats du premier test.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible pour créer un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant la durée de la campagne.

Lorsque vous consultez vos résultats, vous pouvez comparer les taux de conversion de vos variantes par rapport au taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer les effets de vos variantes, mais aussi de les comparer au taux de conversion que vous obtiendriez si vous n'aviez envoyé aucun message.

![Panneau des tests A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Il n'est pas recommandé d'utiliser un groupe de contrôle pour déterminer un gagnant en fonction du _nombre d'ouvertures_ ou de _clics_. Étant donné que le message n'est pas envoyé au groupe de contrôle, ces utilisateurs ne peuvent effectuer ni ouvertures ni clics. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne constitue pas une comparaison pertinente avec les variantes.
{% endalert %}

#### Groupes de contrôle avec test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Utilisez des fenêtres de conversion appropriées pour éviter ce biais.

#### Groupes de contrôle avec sélection intelligente

La taille du groupe de contrôle pour une campagne avec [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, alors le groupe de contrôle est de 20 % et les variantes sont réparties de manière égale sur les 80 % restants. Cependant, si vous avez suffisamment de variantes pour que chacune soit envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit alors être plus petit. Lorsque la sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle s'agrandit ou se réduit en fonction des résultats.

## Étape 5 : Désigner un événement de conversion (facultatif)

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires ont effectué une action donnée après réception.

Cela n'affecte le test que si vous avez choisi **Taux de conversion primaire** dans les étapes précédentes. Pour plus d'informations, reportez-vous à la section [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/). 

## Étape 6 : Vérifier et lancer le test

Sur la page de confirmation, vérifiez les informations de votre campagne multivariée et lancez le test ! Ensuite, apprenez à [comprendre les résultats de vos tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Bon à savoir

Si l'envoi de votre expérience a déjà commencé et que vous modifiez le message, l'expérience est invalidée et tous les résultats sont supprimés.

- Pour éviter toute interférence avec le comportement attendu de l'expérience, nous vous recommandons de ne pas modifier les messages dans l'heure qui suit le lancement de la campagne.
- Si votre expérience est terminée et que vous modifiez le message après son envoi, les résultats de l'expérience restent disponibles dans l'analytique de votre tableau de bord. Toutefois, si vous relancez la campagne, les résultats de l'expérience sont supprimés.

### Conseils pour différents canaux {#tips-different-channels}

Selon le canal choisi, vous pouvez tester différents éléments de votre message. Par exemple, vous pouvez essayer de composer des variantes en ayant une idée de ce que vous voulez tester et de ce que vous espérez prouver. Quels sont les leviers à actionner et quels sont les effets recherchés ? Bien qu'il existe des millions de possibilités à explorer à l'aide d'un test A/B ou multivarié, voici quelques suggestions pour vous aider à démarrer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Notification push | Texte <br> Utilisation des images et des émojis <br> Liens profonds  <br> Présentation des chiffres (par exemple, « tripler » par rapport à « augmenter de 200 % »)  <br> Présentation de l'heure (par exemple, « se termine à minuit » ou « se termine dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| E-mail | Objet <br> Nom affiché <br> Salutations <br> Corps du message <br> Utilisation des images et des émojis <br> Présentation des chiffres (par exemple, « tripler » par rapport à « augmenter de 200 % ») <br> Présentation de l'heure (par exemple, « se termine à minuit » ou « se termine dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| Message in-app | Aspects listés pour « notification push » <br> [Spécifications des images de messages in-app]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#in-app-messages) | Clic <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Lorsque vous exécutez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) afin de comprendre l'impact de chaque variante sur votre tunnel de conversion, en particulier si, pour votre entreprise, la « conversion » implique plusieurs étapes ou actions.
{% endalert %}

De plus, la durée idéale de votre test peut varier en fonction du canal. Gardez à l'esprit le temps moyen dont la plupart des utilisateurs ont besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats probants plus rapidement qu'avec un e-mail, car les utilisateurs voient immédiatement les notifications push, alors qu'ils peuvent mettre plusieurs jours à voir et ouvrir un e-mail. Si vous testez des messages in-app, gardez à l'esprit que les utilisateurs doivent ouvrir l'application pour voir la campagne : vous devriez donc attendre plus longtemps pour collecter les résultats à la fois de vos utilisateurs les plus actifs et de vos utilisateurs plus occasionnels.

Si vous n'êtes pas sûr de la durée idéale de votre test, la fonctionnalité de [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) peut s'avérer utile pour trouver efficacement une variante gagnante.

### Choisir un segment {#choosing-a-segment}

Étant donné que différents segments d'utilisateurs peuvent réagir différemment à vos messages, la réussite d'un message donné révèle quelque chose à la fois sur le message lui-même et sur son segment cible. Essayez donc de concevoir un test en pensant à votre segment cible.

Par exemple, alors que les utilisateurs actifs peuvent avoir le même taux de réponse à « Cette offre expire demain ! » et à « Cette offre expire dans 24 heures ! », les utilisateurs qui n'ont pas ouvert l'application depuis une semaine peuvent être plus réceptifs à la seconde formulation, car elle crée un plus grand sentiment d'urgence.

En outre, lorsque vous choisissez le segment sur lequel effectuer votre test, assurez-vous que sa taille est suffisante. En général, les tests A/B et multivariés qui comportent un plus grand nombre de variantes nécessitent un groupe de test plus important pour obtenir des résultats statistiquement significatifs. En effet, plus il y a de variantes, moins il y a d'utilisateurs qui voient chacune d'entre elles.

{% alert tip %}
À titre indicatif, vous aurez probablement besoin d'environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour obtenir un niveau de confiance de 95 % dans vos résultats de test. Toutefois, le nombre exact d'utilisateurs nécessaire peut être supérieur ou inférieur, en fonction de votre cas particulier. Pour obtenir des indications plus précises sur les tailles d'échantillons des variantes, utilisez un [calculateur de taille d'échantillon](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Biais et randomisation

Une question fréquente concernant les groupes de contrôle et de test est de savoir s'ils peuvent introduire un biais dans vos tests. D'autres se demandent parfois comment nous pouvons garantir que ces affectations sont réellement aléatoires.

Les utilisateurs sont affectés à des variantes de message, des variantes de Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l'ID de campagne ou de Canvas (généré aléatoirement), en prenant le modulo de cette valeur avec 100, puis en ordonnant les utilisateurs en tranches qui correspondent aux pourcentages d'affectation pour les variantes et le contrôle facultatif choisis dans le tableau de bord. Il n'y a donc aucun moyen pratique pour que les comportements des utilisateurs avant la création d'une campagne ou d'un Canvas particulier varient systématiquement entre les variantes et le contrôle. Il n'est pas non plus possible d'être plus aléatoire (ou, plus précisément, pseudo-aléatoire) que cette implémentation.

#### Erreurs à éviter

Il existe des erreurs courantes qui peuvent créer l'apparence de différences en fonction du canal de communication si les audiences ne sont pas filtrées correctement.

Par exemple, si vous envoyez un message push à une large audience avec un contrôle, le groupe de test envoie des messages uniquement aux utilisateurs disposant d'un jeton de notification push. Cependant, le groupe de contrôle comprend à la fois des utilisateurs qui disposent d'un jeton de notification push et d'autres qui n'en ont pas. Dans ce cas, votre audience initiale pour la campagne ou le Canvas doit filtrer sur la possession d'un jeton de notification push (`Foreground Push Enabled` est `true`). Il faut faire de même pour l'éligibilité à la réception de messages sur d'autres canaux : opt-in, possession d'un jeton de notification push ou abonnement.

Notez que si une variante de contrôle ne comprend aucune étape du canvas, les événements liés aux critères de sortie ne sont pas enregistrés pour les utilisateurs de la variante de contrôle.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoire pour les groupes de contrôle, consultez les [éléments à surveiller]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) dans vos groupes de contrôle.
{% endalert %}