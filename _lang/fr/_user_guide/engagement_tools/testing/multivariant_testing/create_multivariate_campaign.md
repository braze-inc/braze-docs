---
nav_title: Créer des tests
article_title: Créer des tests A/B et multivariés
page_order: 1
page_type: reference
description: "Cet article explique comment créer des tests A/B et multivariés avec Braze."
---

# Créer des tests A/B et multivariés avec Braze {#creating-tests}

Vous pouvez créer un [test A/B ou multivarié]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour n’importe quelle campagne qui cible un canal unique.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## Étape 1 : Créer votre campagne

Cliquez sur **Create Campaign (Créer une campagne)** et sélectionnez un canal pour la campagne dans la section qui prend en charge les tests A/B et multivariés. Pour obtenir des informations détaillées sur chaque canal de communication, consultez l’article [Créer une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Étape 2 : Composer vos variantes

Vous pouvez créer jusqu’à 8 variantes de votre message, en changeant les titres, le contenu, les images, etc. Le nombre de différences entre les messages détermine s’il s’agit d’un test A/B ou multivarié. Un test A/B examine l’effet de la modification d’une variable alors qu’un test multivarié en examine deux ou plus.

Découvrez de nouvelles idées sur la manière de différencier vos variantes en consultant nos [Conseils pour différents canaux](#tips-different-channels).

![][3]

## Étape 3 : Planifier votre campagne

Planifier votre campagne multivariée fonctionne comme pour toute autre planification de campagne Braze. Tous les [types de livraison][4] habituels sont disponibles.

{% alert important %}
Si vous désirez utiliser une [optimisation](#optimizations) (disponible pour des canaux donnés), planifiez votre campagne pour qu’elle ne soit livrée qu’une fois. Les optimisations ne sont pas disponibles pour les campagnes qui sont répétées ou pour lesquelles une nouvelle éligibilité est activée.
{% endalert %}

## Étape 4 : Choisir un segment et répartir vos utilisateurs entre les variantes

Sélectionnez les segments à cibler, puis répartissez leurs membres entre les différentes variantes que vous avez choisies et le [groupe de contrôle](#including-a-control-group) optionnel. Pour connaître les meilleures pratiques concernant le choix d’un segment à tester, consultez la section [Choisir un segment](#choosing-a-segment).

Pour les campagnes de notification push, d’e-mails ou de webhook qui sont planifiées pour n’être envoyées qu’une fois, vous pouvez également utiliser une [optimisation](#optimizations). Ceci séparera une partie de votre audience cible du test A/B et les réservera pour un second envoi optimisé selon les résultats du premier test.

### Groupe de contrôle {#including-a-control-group}

Vous pouvez réserver un pourcentage de votre audience cible pour créer un groupe de contrôle randomisé. Les utilisateurs du groupe de contrôle ne reçoivent pas le test, mais Braze surveille leur taux de conversion pendant la durée de la campagne.

Lorsque vous visualisez vos résultats, vous pouvez comparer les taux de conversion de vos variantes par rapport au taux de conversion de référence fourni par votre groupe de contrôle. Cela vous permet de comparer les effets de vos variantes, mais aussi de comparer les effets de vos variantes au taux de conversion que vous obtiendriez si vous n’aviez envoyé aucun message.

![Panneau des tests A/B montrant la répartition en pourcentage du groupe de contrôle, de la variante 1, de la variante 2 et de la variante 3 avec 25 % pour chaque groupe.][5]

{% alert important %}
Notez qu’il n’est pas recommandé d’utiliser un groupe de contrôle pour trouver la variante gagnante en se basant sur les ouvertures ou les clics. Étant donné que le message n’est pas envoyé au groupe de contrôle, ces utilisateurs ne peuvent pas effectuer d’ouverture ou de clics. Par conséquent, le taux de conversion de ce groupe est de 0 % par définition et ne peut être comparé avec les variantes.
{% endalert %}

#### Groupes de contrôle avec sélection intelligente

La taille du groupe de contrôle d’une campagne avec [Sélection intelligente][1] est basée sur le nombre de variantes. Si chaque variante est envoyée à plus de 20 % des utilisateurs, cela signifie que le groupe de contrôle représente 20 % de votre audience et que les variantes sont réparties uniformément entre les 80 % restants. Cependant, si vous avez assez de variantes pour que chaque variante soit envoyée à moins de 20 % des utilisateurs, le groupe de contrôle doit alors être plus petit. Lorsque la Sélection intelligente commence à analyser les performances de votre test, le groupe de contrôle augmente ou diminue en fonction des résultats.

### Optimisation {#optimizations}

Pour les campagnes d’e-mails, de notification push, de SMS, de webhook et WhatsApp qui sont planifiées pour n’être envoyées qu’une fois, vous pouvez sélectionner une optimisation. Il existe deux options d’optimisation : La **Variante gagnante** et la **Variante personnalisée**.

![Options d’optimisation présentées dans la section de test A/B lorsque vous choisissez votre audience cible. Trois options sont présentées : Pas d’optimisation, Variante gagnante et Variante personnalisée. Variante personnalisée est sélectionnée.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Les deux options fonctionnent en envoyant un test initial à un pourcentage de votre segment cible. Après la fin du test, les utilisateurs restants de votre audience sont envoyés soit à la variante la plus efficace (Variante gagnante) soit à la variante avec laquelle ils ont le plus de chance d’interagir (Variante personnalisée).

{% tabs %}
{% tab Winning Variant %}

Envoyer la variante gagnante est similaire à un test A/B standard. Les utilisateurs de ce groupe recevront la variante gagnante une fois le test d’origine terminé.

1. Sélectionnez **Variante gagnante** puis indiquez le pourcentage de votre audience de campagne qui doit être affecté au groupe de la variante gagnante.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- | 
| Indicateurs d’optimisation | L’indicateur pour lequel il faut optimiser. Choisissez entre *ouverture unique* ou *clics* pour les e-mails, *ouvertures* pour les notifications push ou *taux de conversion primaire* pour tous les canaux. Le fait de sélectionner *ouvertures* ou *clics* pour déterminer la variante gagnante n’affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) que vous choisissez pour la campagne. <br><br>N’oubliez pas que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer d’*ouverture*, ou de *clics*. La performance du groupe de contrôle sera donc systématiquement `0`. Par conséquent, le groupe de contrôle ne peut pas gagner le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle afin de suivre d’autres mesures pour les utilisateurs qui ne reçoivent pas de message. |
| Heure de départ du test d’origine | La date et l’heure du début du test d’origine. |
| Heure de fin du test d’origine | La date et l’heure de la fin du test d’origine. Il s’agit du moment où la variante gagnante est envoyée aux utilisateurs restants.<br><br>Si la variante gagnante est envoyée en fonction de l’heure locale des utilisateurs ou avec la fonction Timing Intelligent, celle-ci doit être envoyée au moins 24 heures après le test A/B afin de s’assurer que tous les utilisateurs du groupe de la variante gagnante la reçoivent. |
| Solution de secours | Ce qui se passe si aucune variante ne gagne par une marge statistiquement significative. Choisissez entre envoyer quand même à la variante la plus performante ou achever le test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Personalized Variant %}

Utilisez des variantes personnalisées pour envoyer à chaque utilisateur de votre segment cible la variante avec laquelle il est le plus susceptible d’interagir.

Pour déterminer la meilleure variante pour chaque utilisateur, Braze enverra le test d’origine à une partie de votre audience cible pour chercher des associations entre les caractéristiques des utilisateurs et les préférences de message. Selon la réponse des utilisateurs à chaque variante dans le test d’origine, ces caractéristiques seront utilisées pour déterminer lesquels, parmi les utilisateurs restants, recevront chaque variante. Si aucune association n’a été trouvée et qu’il est impossible de faire une personnalisation, la variante gagnante sera automatiquement envoyée aux utilisateurs restants. Pour en savoir plus sur la manière dont les variantes personnalisées sont déterminées, rapportez-vous à la section [Analytiques des tests A/B et multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Sélectionnez **Winning Variant (Variante personnalisée)** puis indiquez le pourcentage de votre audience de campagne qui doit être affecté au groupe de la variante personnalisée.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- | 
| Indicateurs d’optimisation | L’indicateur pour lequel il faut optimiser. Choisissez entre *ouverture unique* ou *clics* pour les e-mails, *ouvertures* pour les notifications push ou *taux de conversion primaire* pour tous les canaux. Le fait de sélectionner *ouvertures* ou *clics* pour déterminer la variante gagnante n’affecte pas les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) que vous choisissez pour la campagne. <br><br>N’oubliez pas que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer d’*ouverture*, ou de *clics*. La performance du groupe de contrôle sera donc systématiquement `0`. Par conséquent, le groupe de contrôle ne peut pas gagner le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle afin de suivre d’autres mesures pour les utilisateurs qui ne reçoivent pas de message. |
| Heure de départ du test d’origine | La date et l’heure du début du test d’origine. |
| Heure de fin du test d’origine | La date et l’heure de la fin du test d’origine. Il s’agit du moment où les variantes personnalisées sont envoyées aux utilisateurs restants. Nous vous recommandons d’utiliser une ligne de base de 24 heures pour vous assurer d’obtenir des résultats significatifs et ayant un sens statistique. Plus la durée autorisée pour le test est longue, plus vous recevrez de réponses et plus Braze peut s’optimiser. Ceci est particulièrement important pour les campagnes par e-mail. Les tests d’origine pour les variantes personnalisées ne devraient pas durer moins de 4 heures.<br><br>Si les variantes personnalisées sont envoyées en fonction de l’heure locale des utilisateurs ou avec la fonction Timing Intelligent, celle-ci doit être envoyée au moins 24 heures après le test A/B afin de s’assurer que tous les utilisateurs du groupe de la variante gagnante la reçoivent. |
| Solution de secours | Que se passe-t-il si aucune variante personnalisée n’est trouvée ? Choisissez entre envoyer à la place à la variante gagnante ou achever le test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Étape 5 : Désigner un événement de conversion (Facultatif)

Définir un événement de conversion pour une campagne vous permet de voir combien de destinataires de la campagne ont effectué une action donnée après réception.

Cela affecte uniquement le test si vous avez sélectionné **Taux de conversion primaire** aux étapes précédentes. Pour plus d’informations, consultez l’article sur les [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). 

## Étape 6 : Vérifier et lancer le test

Sur la page de confirmation, vérifiez les informations de votre campagne multivariée et lancez le test une fois terminé ! Apprenez ensuite comment [comprendre les résultats de votre test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Choses à savoir

### Conseils pour différents canaux {#tips-different-channels}

Vous pouvez tester différents composants de votre message en fonction du canal que vous avez choisi. Essayez de créer des variantes en ayant une idée de ce que vous voulez tester et de ce que vous espérez prouver.

Quels leviers devez-vous utiliser et quels sont les effets souhaités ? Bien qu’il existe des millions d’éléments à étudier à l’aide d’un test A/B ou multivarié, nous avons réuni quelques suggestions pour vous aider à démarrer :

| Canal | Aspects du message que vous pouvez modifier | Résultats à rechercher |
| ---------------------| --------------- | ------------- |
| Notification push | Copier <br> Utilisation des images et des émojis <br> Liens profonds  <br> Présentation des nombres (p. ex., « triple » par rapport à « augmentation de 200 % »)  <br> Présentation des heures (p. ex., « se termine à minuit » par rapport à « fini dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| E-mail | Objet <br> Nom affiché <br> Salutations <br> Copie du corps <br> Utilisation des images et des émojis <br> Présentation des nombres (p. ex., « triple » par rapport à « augmentation de 200 % ») <br> Présentation des heures (p. ex., « se termine à minuit » par rapport à « fini dans 6 heures ») | Ouvertures  <br> Taux de conversion |
| Message in-app | Aspects listés pour « notification push » <br> [Format de message][7] | Clic <br> Taux de conversion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert tip %}
Lorsque vous effectuez des tests A/B, n’oubliez pas de générer des [rapports d’entonnoir]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/) afin de comprendre comment chaque variante a affecté votre tunnel de conversion, surtout si cette « conversion » implique pour vous de prendre plusieurs mesures ou actions.
{% endalert %}

De plus, la longueur idéale de votre test peut également varier en fonction du canal. Gardez à l’esprit la durée moyenne dont la plupart des utilisateurs peuvent avoir besoin pour interagir avec chaque canal.

Par exemple, si vous testez une notification push, vous pouvez obtenir des résultats probants plus rapidement qu’en testant des e-mails, car les utilisateurs voient immédiatement les notifications push, alors qu’ils peuvent mettre plusieurs jours à voir et ouvrir un e-mail. Si vous testez des messages in-app, gardez à l’esprit que les utilisateurs doivent ouvrir l’application pour voir la campagne, il est donc préférable d’attendre plus longtemps avant de recueillir les résultats concernant les personnes qui ouvrent le plus souvent l’application et vos utilisateurs type.

Si vous n’êtes pas sûr de la durée de votre test, la [Sélection intelligente][6] peut vous aider à trouver rapidement une variante gagnante.

### Choisir des segments {#choosing-a-segment}

Étant donné que différents segments d’utilisateurs peuvent réagir différemment à votre message, la réussite d’un message donné révèle quelque chose à la fois sur le message lui-même et sur son segment cible. Essayez donc de créer un test en pensant à votre segment cible.

Par exemple, même si les utilisateurs actifs peuvent réagir de la même manière à « Cette offre se termine demain ! » et « Cette offre se termine dans 24 heures ! », les utilisateurs qui n’ont pas ouvert l’application pendant une semaine peuvent être plus réceptifs à la deuxième formulation, car elle crée un plus grand sentiment d’urgence.

Par ailleurs, lorsque vous choisissez un segment à tester, assurez-vous que la taille de ce segment sera suffisamment grande pour votre test. En général, les tests A/B et multivariés qui comportent un plus grand nombre de variantes nécessitent un groupe de test plus grand pour obtenir des résultats probants sur le plan statistique. En effet, plus le nombre de variantes est important, plus le nombre d’utilisateurs voyant chaque variante sera réduit.

{% alert tip %}
À titre de référence, vous aurez probablement besoin d’environ 15 000 utilisateurs par variante (y compris le groupe de contrôle) pour obtenir une confiance de 95 % dans vos résultats de test. Cependant, le nombre exact d’utilisateurs dont vous aurez besoin pourrait être supérieur ou inférieur en fonction de la situation. Pour obtenir des conseils plus précis sur la taille des échantillons pour les tests de variantes, utilisez le [Calculateur de taille d’échantillon d’Optimizely](https://www.optimizely.com/resources/sample-size-calculator/).
{% endalert %}

### Affectations et biais des groupes de contrôle et de test

Une question courante concernant les affectations de groupe de contrôle et de test est de se demander s’ils peuvent introduire un biais dans vos tests.

Les utilisateurs sont affectés à des variantes de message, des variantes de Canvas ou à leurs groupes de contrôle respectifs en concaténant leur ID utilisateur (généré aléatoirement) avec l’ID de campagne (généré aléatoirement) ou l’ID de Canvas, en prenant le module de cette valeur avec 100, puis en ordonnant les utilisateurs en tranches qui correspondent aux affectations de pourcentage pour les variantes et le contrôle facultatif choisi dans le tableau de bord. Il n’existe donc aucun moyen pratique pour que les comportements des utilisateurs avant la création d’une campagne particulière ou un Canvas puissent varier systématiquement entre les variantes et le contrôle.

#### Erreurs à éviter

Il existe des erreurs courantes pour éviter de créer l’apparence de différences en fonction du canal de communication si les audiences ne sont pas filtrées correctement.

Par exemple, si vous envoyez une notification push à une large audience avec un contrôle, le groupe de test n’enverra des messages qu’aux utilisateurs avec un jeton push. Cependant, le groupe de contrôle inclura à la fois les utilisateurs qui ont un jeton de notification push et les utilisateurs qui n’en ont pas. Dans ce cas, votre audience initiale pour la campagne ou Canvas doit filtrer pour avoir un jeton de notification push (`Push Enabled` est `true`). Il en va de même pour l’éligibilité à recevoir des messages sur d’autres canaux : s’est inscrit, a un jeton de notification push, s’est abonné, etc.

{% alert note %}
Si vous utilisez manuellement des numéros de compartiment aléatoires pour les groupes de contrôle, référencez cette liste de [choses à surveiller]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) dans vos groupes témoins.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
