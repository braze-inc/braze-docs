---
nav_title: Création de tests
article_title: Création de tests multivariés et de tests A/B
page_order: 1
page_type: reference
description: "Cet article explique comment créer des tests multivariés et des tests A/B avec Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Création de tests multivariés et de tests A/B {#creating-tests}

> Vous pouvez créer un [test multivarié ou un test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour toute campagne qui cible un seul canal et un seul appareil. Par exemple, si vous souhaitez utiliser le test multivarié ou le test A/B pour une campagne push, vous pouvez cibler uniquement les appareils iOS ou uniquement les appareils Android - et non les deux types d'appareils dans la même campagne.

\![La liste déroulante permettant de choisir entre multicanal et monocanal à partir du bouton "Créer une campagne".]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Étape 1 : Créez votre campagne

1. Allez dans **Envoi de messages** > Campagnes.
2. Sélectionnez **Créer une campagne** et un canal pour la campagne dans la section qui permet les tests multivariés et les tests A/B. Pour obtenir une documentation détaillée sur chaque canal de communication, reportez-vous à la section [Créer une campagne.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)

## Étape 2 : Composez vos variantes

Vous pouvez créer jusqu'à huit variantes de votre message, en différenciant les titres, le contenu, les images, etc. Le nombre de différences entre les messages détermine s'il s'agit d'un test multivarié ou d'un test A/B. Un test A/B examine l'effet de la modification d'une variable, tandis qu'un test multivarié en examine deux ou plus.

Pour avoir quelques idées sur la manière de commencer à différencier vos variantes, reportez-vous à [Conseils pour les différents canaux.](#tips-different-channels)

\![Sélection de "Ajouter une variante" pour une campagne.]({% image_buster /assets/img/ab_create_2.png %})

## Étape 3 : Planifiez votre campagne

La planification de votre campagne multivariée fonctionne de la même manière que la planification de n'importe quelle autre campagne Braze. Tous les [types de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) standard sont disponibles.

Une fois qu'un test multivarié a commencé, vous ne pouvez plus apporter de modifications à la campagne. Si vous modifiez les paramètres, tels que la ligne d'objet ou le corps HTML, Braze considérera que l'expérience est compromise et la désactivera immédiatement.

{% alert important %}
Pour utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponible pour certains canaux), planifiez votre campagne pour qu'elle soit diffusée une seule fois. Les optimisations ne sont pas disponibles pour les campagnes qui se répètent ou dont la rééligibilité est activée.
{% endalert %}

## Étape 4 : Choisissez un segment et répartissez vos utilisateurs dans les variantes.

Sélectionnez les segments à cibler, puis répartissez ses membres entre les variantes sélectionnées et le [groupe de contrôle](#including-a-control-group) facultatif. Pour connaître les meilleures pratiques concernant le choix d'un segment d'essai, reportez-vous à la section [Choix d'un segment](#choosing-a-segment).

Pour les campagnes push, e-mail et webhook planifiées pour être envoyées une seule fois, vous pouvez également utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Vous réservez ainsi une partie de votre audience cible du test A/B et la gardez pour un deuxième envoi optimisé en fonction des résultats du premier test.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible à un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant toute la durée de la campagne.

Lorsque vous consultez vos résultats, vous pouvez comparer les taux de conversion de vos variantes à un taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer à la fois les effets de vos variantes et les effets de vos variantes par rapport au taux de conversion qui résulterait de l'absence totale d'envoi de message.

!panneau de test A/B qui montre la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Il n'est pas recommandé d'utiliser un groupe de contrôle pour déterminer un gagnant en fonction du _nombre d'ouvertures_ ou de _clics_. Comme le groupe de contrôle ne recevra pas le message, ces utilisateurs ne pourront pas ouvrir ou cliquer. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne constitue pas une comparaison pertinente avec les variantes.
{% endalert %}

#### Groupes de contrôle avec test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Utilisez des fenêtres de conversion appropriées pour éviter ce biais.

#### Groupes de contrôle avec sélection intelligente

La taille du groupe de contrôle pour une campagne avec [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, alors le groupe de contrôle est de 20 % et les variantes sont réparties de manière égale sur les 80 % restants. Toutefois, si vous avez suffisamment de variantes pour que chaque variante soit envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit être plus petit. Lorsque la sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle s'agrandit ou se réduit en fonction des résultats.

## Étape 5 : Désigner un événement de conversion (facultatif)

La définition d'un événement de conversion pour une campagne vous permet de voir combien de destinataires de cette campagne ont effectué une action particulière après l'avoir reçue.

Cela n'affecte le test que si vous avez choisi **Taux de conversion primaire** dans les étapes précédentes. Pour plus d'informations, reportez-vous à la rubrique [Événements de conversion.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 

## Étape 6 : Examen et lancement

Sur la page de confirmation, passez en revue les détails de votre campagne multivariée et lancez le test ! Ensuite, apprenez à [comprendre les résultats de vos tests.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/)

## Ce qu'il faut savoir

Si l'envoi de votre expérience a déjà commencé et que vous modifiez le message, l'expérience sera invalidée et tous les résultats de l'expérience seront supprimés.

- Pour éviter toute interférence avec le comportement attendu de l'expérience, nous vous recommandons d'éviter de modifier les messages dans l'heure qui suit le lancement de la campagne de communication.
- Si votre expérience est terminée et que vous modifiez le message après son envoi, les résultats de l'expérience resteront disponibles dans votre tableau de bord analytique. Toutefois, si vous relancez la campagne, les résultats de l'expérience seront supprimés.

### Conseils pour les différents canaux {#tips-different-channels}

Selon le canal choisi, vous pouvez tester différents éléments de votre message. Par exemple, vous pouvez essayer de composer des variantes en ayant une idée de ce que vous voulez tester et de ce que vous espérez prouver. Quels sont les leviers à actionner et quels sont les effets recherchés ? Bien qu'il existe des millions de possibilités que vous pouvez étudier à l'aide d'un test multivarié et d'un test A/B, nous avons quelques suggestions pour vous aider à démarrer :

| Chaîne | Les aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Pousser | Copie <br> Utilisation d'images et d'Emoji <br> Liens profonds  <br> Présentation des chiffres (par exemple, "tripler" par rapport à "augmenter de 200%")  <br> Présentation de l'heure (par exemple, "se termine à minuit" ou "se termine dans 6 heures") | Ouvertures  <br> Taux de conversion |
| e-mail | Sujet <br> Nom d'affichage <br> Salutation <br> Texte du corps <br> Utilisation d'images et d'Emoji <br> Présentation des chiffres (par exemple, "tripler" par rapport à "augmenter de 200%") <br> Présentation de l'heure (par exemple, "se termine à minuit" ou "se termine dans 6 heures") | Ouvertures  <br> Taux de conversion |
| Message in-app | Aspects listés pour "push" (pousser) <br> [Format du message]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) | Cliquez sur <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Lorsque vous exécutez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) qui vous permettent de comprendre l'impact de chaque variante sur votre entonnoir de conversion, en particulier si, pour votre entreprise, la "conversion" implique de franchir plusieurs étapes ou d'effectuer plusieurs actions.
{% endalert %}

En outre, la durée idéale de votre test peut également varier en fonction de la chaîne. Gardez à l'esprit le temps moyen nécessaire à la plupart des utilisateurs pour s'engager sur chaque canal.

Par exemple, si vous testez un push, vous pouvez obtenir des résultats significatifs plus rapidement que lorsque vous testez un e-mail, car les utilisateurs voient les push immédiatement, alors qu'il peut s'écouler des jours avant qu'ils ne voient ou n'ouvrent un e-mail. Si vous testez des messages in-app, gardez à l'esprit que les utilisateurs doivent ouvrir l'application pour voir la campagne, vous devriez donc attendre plus longtemps pour collecter les résultats à la fois de vos utilisateurs les plus actifs qui ouvrent l'application et de vos utilisateurs les plus typiques.

Si vous n'êtes pas sûr de la durée de votre test, la fonctionnalité de [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) peut s'avérer utile pour trouver efficacement une variante gagnante.

### Choix d'une segmentation {#choosing-a-segment}

Étant donné que les différents segments de vos utilisateurs peuvent réagir différemment à l'envoi de messages, le succès d'un message particulier en dit long à la fois sur le message lui-même et sur son segment cible. Essayez donc de concevoir un essai en tenant compte de votre segmentation cible.

Par exemple, alors que les utilisateurs actifs peuvent avoir le même taux de réponse à "Cette offre expire demain !" et à "Cette offre expire dans 24 heures !", les utilisateurs qui n'ont pas ouvert l'application depuis une semaine peuvent être plus réceptifs à la dernière formulation, car elle crée un plus grand sentiment d'urgence.

En outre, lorsque vous choisissez le segment sur lequel vous allez effectuer votre essai, assurez-vous que la taille de ce segment sera suffisante pour votre essai. En général, les tests multivariés et les tests A/B comportant plus de variantes nécessitent un groupe de test plus important pour obtenir des résultats statistiquement significatifs. En effet, plus il y a de variantes, moins les utilisateurs verront chaque variante individuellement.

{% alert tip %}
À titre indicatif, vous aurez probablement besoin d'environ 15 000 utilisateurs par variante (y compris le témoin) pour obtenir un niveau de confiance de 95 % dans les résultats de votre test. Toutefois, le nombre exact d'utilisateurs dont vous avez besoin peut être supérieur ou inférieur à ce chiffre, en fonction de votre cas particulier. Pour obtenir des indications plus précises sur les tailles d'échantillon variantes, pensez à vous référer à un [calculateur de taille d'échantillon](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Biais et randomisation

Une question fréquente concernant les groupes de contrôle et de test est de savoir s'ils peuvent introduire un biais dans vos tests. D'autres se demandent parfois comment nous pouvons savoir si ces affectations sont réellement aléatoires.

Les utilisateurs sont affectés aux variantes de message, aux variantes Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l'ID de campagne ou Canvas (généré aléatoirement), en prenant le module de cette valeur avec 100, puis en ordonnant les utilisateurs dans des tranches qui correspondent aux affectations en pourcentage pour les variantes et le contrôle facultatif choisi dans le tableau de bord. Il n'y a donc aucun moyen pratique pour que les comportements des utilisateurs avant la création d'une campagne ou d'un Canvas particulier varient systématiquement entre les variantes et le contrôle. Il n'est pas non plus pratique d'être plus aléatoire (ou plus précisément pseudo-aléatoire) que cette mise en œuvre.

#### Les erreurs à éviter

Il y a quelques erreurs courantes à éviter qui donnent l'impression de différences en fonction du canal de communication si les audiences ne sont pas filtrées correctement.

Par exemple, si vous envoyez un message push à une large audience avec un contrôle, le groupe de test n'enverra des messages qu'aux utilisateurs disposant d'un jeton push. Cependant, le groupe de contrôle comprendra à la fois des utilisateurs qui disposent d'un jeton push et d'autres qui n'en ont pas. Dans ce cas, votre audience initiale pour la campagne ou le Canvas doit filtrer pour avoir un jeton de poussée (`Foreground Push Enabled` est `true`). Il faut faire de même pour l'éligibilité à recevoir des messages sur d'autres canaux : opted in, has a push token, subscribed, etc.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoire pour les groupes de contrôle, vérifiez les [éléments à surveiller]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) dans vos groupes de contrôle.
{% endalert %}

