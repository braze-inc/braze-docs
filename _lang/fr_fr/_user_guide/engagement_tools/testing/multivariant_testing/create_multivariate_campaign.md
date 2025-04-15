---
nav_title: Créer des tests
article_title: Créer des tests A/B et multivariés
page_order: 1
page_type: reference
description: "Cet article explique comment créer des tests A/B et multivariés avec Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Créer des tests A/B et multivariés {#creating-tests}

> Vous pouvez créer un [test multivarié ou un test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour toute campagne qui cible un seul canal.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## Étape 1 : Créer votre campagne

Cliquez sur **Créer une campagne** et sélectionnez un canal pour la campagne dans la section qui autorise les tests multivariés et A/B. Pour obtenir des informations détaillées sur chaque canal de communication, reportez-vous à la section [Créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Étape 2 : Composer vos variantes

Vous pouvez créer jusqu’à 8 variantes de votre message, en changeant les titres, le contenu, les images, etc. Le nombre de différences entre les messages détermine s’il s’agit d’un test A/B ou multivarié. Un test A/B examine l’effet de la modification d’une variable alors qu’un test multivarié en examine deux ou plus.

Découvrez de nouvelles idées sur la manière de différencier vos variantes en consultant nos [conseils pour différents canaux](#tips-different-channels).

![][3]

## Étape 3 : Planifier votre campagne

Planifier votre campagne multivariée fonctionne comme pour toute autre planification de campagne Braze. Tous les [types de distribution][4] standard sont disponibles.

Une fois qu'un test multivarié a commencé, vous ne pouvez plus apporter de modifications à la campagne. Si vous modifiez les paramètres, tels que la ligne d'objet ou le corps HTML, Braze considérera que l'expérience est compromise et la désactivera immédiatement.

{% alert important %}
Si vous souhaitez utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponible pour certains canaux), planifiez votre campagne pour qu'elle soit diffusée une seule fois. Les optimisations ne sont pas disponibles pour les campagnes qui sont répétées ou pour lesquelles une nouvelle éligibilité est activée.
{% endalert %}

## Étape 4 : Choisir un segment et répartir vos utilisateurs entre les variantes

Sélectionnez les segments à cibler, puis répartissez ses membres entre les variantes sélectionnées et le [groupe de contrôle](#including-a-control-group) facultatif. Pour connaître les meilleures pratiques concernant le choix d'un segment d'essai, reportez-vous à la section [Choix d'un segment](#choosing-a-segment).

Pour les campagnes push, e-mail et webhook planifiées pour être envoyées une seule fois, vous pouvez également utiliser une [optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Ceci séparera une partie de votre audience cible du test A/B et les réservera pour un second envoi optimisé selon les résultats du premier test.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible pour créer un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant la durée de la campagne.

Lorsque vous visualisez vos résultats, vous pouvez comparer les taux de conversion de vos variantes par rapport au taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer les effets de vos variantes, mais aussi de comparer les effets de vos variantes au taux de conversion que vous obtiendriez si vous n’aviez envoyé aucun message.

![Panneau des tests A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.][5]

{% alert important %}
Notez qu’il n’est pas recommandé d’utiliser un groupe de contrôle pour trouver la variante gagnante en se basant sur les ouvertures ou les clics. Étant donné que le message n’est pas envoyé au groupe de contrôle, ces utilisateurs ne peuvent pas effectuer d’ouverture ou de clics. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne peut être comparé avec les variantes.
{% endalert %}

#### Groupes de contrôle avec test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Utilisez des fenêtres de conversion appropriées pour éviter ce biais.

#### Groupes de contrôle avec sélection intelligente

La taille du groupe de contrôle pour une campagne avec [sélection intelligente][1] est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, cela signifie que le groupe de contrôle représente 20 % de votre audience et que les variantes sont réparties uniformément entre les 80 % restants. Cependant, si vous avez assez de variantes pour que chaque variante soit envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit alors être plus petit. Lorsque la sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle s'agrandit ou se réduit en fonction des résultats.

## Étape 5 : Désigner un événement de conversion (Facultatif)

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires de la campagne ont effectué une action donnée après réception.

Cela n'affecte le test que si vous avez choisi **Taux de conversion primaire** dans les étapes précédentes. Pour plus d'informations, reportez-vous à la section [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). 

## Étape 6 : Vérifier et lancer le test

Sur la page de confirmation, vérifiez les informations de votre campagne multivariée et lancez le test une fois terminé ! Ensuite, apprenez à [comprendre les résultats de vos tests.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/)

## Choses à savoir

{% alert important %}
Si vous modifiez les messages après le début de l'expérience, les résultats ne seront pas valables.

- Si votre expérience est en cours d'envoi et que vous modifiez le message, l'expérience sera rendue inutile et tous les résultats de l'expérience seront supprimés.
- Si votre expérience est terminée et que vous modifiez le message après son envoi, les résultats de l'expérience resteront disponibles sur la page d'analyse du tableau de bord. Si vous relancez la campagne, les résultats de l'expérience seront supprimés.
{% endalert %}

### Conseils pour différents canaux {#tips-different-channels}

Vous pouvez tester différents composants de votre message en fonction du canal que vous avez choisi. Essayez de créer des variantes en ayant une idée de ce que vous voulez tester et de ce que vous espérez prouver.

Quels leviers devez-vous utiliser et quels sont les effets souhaités ? Bien qu’il existe des millions d’éléments à étudier à l’aide d’un test A/B ou multivarié, nous avons réuni quelques suggestions pour vous aider à démarrer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Notification push | Copier <br> Utilisation des images et des émojis <br> Liens profonds  <br> Présentation des chiffres (par exemple, "tripler" par rapport à "augmenter de 200%")  <br> Présentation de l'heure (par exemple, "se termine à minuit" ou "se termine dans 6 heures") | Ouvertures  <br> Taux de conversion |
| E-mail | Objet <br> Nom affiché <br> Salutations <br> Copie du corps <br> Utilisation des images et des émojis <br> Présentation des chiffres (par exemple, "tripler" par rapport à "augmenter de 200%") <br> Présentation de l'heure (par exemple, "se termine à minuit" ou "se termine dans 6 heures") | Ouvertures  <br> Taux de conversion |
| Message in-app | Aspects listés pour « notification push » <br> [Format du message][7] | Clic <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Lorsque vous exécutez des tests A/B, n'oubliez pas de générer des [rapports d'entonnoir]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) afin de comprendre l'impact de chaque variante sur votre entonnoir de conversion, en particulier si, pour votre entreprise, la « conversion » implique plusieurs étapes ou plusieurs actions.
{% endalert %}

De plus, la longueur idéale de votre test peut également varier en fonction du canal. Gardez à l’esprit la durée moyenne dont la plupart des utilisateurs peuvent avoir besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats probants plus rapidement qu’en testant des e-mails, car les utilisateurs voient immédiatement les notifications push, alors qu’ils peuvent mettre plusieurs jours à voir et ouvrir un e-mail. Si vous testez des messages in-app, gardez à l’esprit que les utilisateurs doivent ouvrir l’application pour voir la campagne, il est donc préférable d’attendre plus longtemps avant de recueillir les résultats concernant les personnes qui ouvrent le plus souvent l’application et vos utilisateurs type.

Si vous n'êtes pas sûr de la durée de votre test, la fonctionnalité [Sélection intelligente][6] peut s'avérer utile pour identifier efficacement une variante gagnante.

### Choisir des segments {#choosing-a-segment}

Étant donné que différents segments d’utilisateurs peuvent réagir différemment à votre message, la réussite d’un message donné révèle quelque chose à la fois sur le message lui-même et sur son segment cible. Essayez donc de créer un test en pensant à votre segment cible.

Par exemple, alors que les utilisateurs actifs peuvent avoir le même taux de réponse à "Cette offre expire demain !" et à "Cette offre expire dans 24 heures !", les utilisateurs qui n'ont pas ouvert l'application depuis une semaine peuvent être plus réceptifs à la dernière formulation, car elle crée un plus grand sentiment d'urgence.

Par ailleurs, lorsque vous choisissez un segment à tester, assurez-vous que la taille de ce segment sera suffisamment grande pour votre test. En général, les tests A/B et multivariés qui comportent un plus grand nombre de variantes nécessitent un groupe de test plus grand pour obtenir des résultats probants sur le plan statistique. En effet, plus le nombre de variantes est important, plus le nombre d’utilisateurs voyant chaque variante sera réduit.

{% alert tip %}
À titre de référence, vous aurez probablement besoin d’environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour obtenir une confiance de 95 % dans vos résultats de test. Cependant, le nombre exact d’utilisateurs dont vous aurez besoin pourrait être supérieur ou inférieur en fonction de la situation. Pour obtenir des indications plus précises sur les tailles d'échantillons des variantes, utilisez un [calculateur de taille d'échantillon](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Biais et randomisation

Une question courante concernant les affectations de groupe de contrôle et de test est de se demander s’ils peuvent introduire un biais dans vos tests. D'autres se demandent parfois comment nous pouvons savoir si ces affectations sont réellement aléatoires.

Les utilisateurs sont affectés à des variantes de message, des variantes de Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l’ID de campagne (généré aléatoirement) ou l’ID de Canvas, en prenant le module de cette valeur avec 100, puis en ordonnant les utilisateurs en tranches qui correspondent aux affectations de pourcentage pour les variantes et le contrôle facultatif choisi dans le tableau de bord. Il n’existe donc aucun moyen pratique pour que les comportements des utilisateurs avant la création d’une campagne particulière ou un Canvas puissent varier systématiquement entre les variantes et le contrôle. Il n'est pas non plus pratique d'être plus aléatoire (ou, plus précisément, pseudo-aléatoire) que cette implémentation.

#### Erreurs à éviter

Il existe des erreurs courantes pour éviter de créer l’apparence de différences en fonction du canal de communication si les audiences ne sont pas filtrées correctement.

Par exemple, si vous envoyez une notification push à une large audience avec un contrôle, le groupe de test n’enverra des messages qu’aux utilisateurs avec un jeton push. Cependant, le groupe de contrôle inclura à la fois les utilisateurs qui ont un jeton de notification push et les utilisateurs qui n’en ont pas. Dans ce cas, votre audience initiale pour la campagne ou le Canvas doit filtrer pour avoir un jeton de notification push (`Push Enabled` est `true`). Il en va de même pour l’éligibilité à recevoir des messages sur d’autres canaux : s’est inscrit, a un jeton de notification push, s’est abonné, etc.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoire pour les groupes de contrôle, consultez cette liste de [points à surveiller]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) dans vos groupes de contrôle.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
