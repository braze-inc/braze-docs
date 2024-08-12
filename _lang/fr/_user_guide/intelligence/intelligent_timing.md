---
nav_title: Timing Intelligent
article_title: Timing Intelligent
page_order: 2
description: "Cet article propose un aperçu du Timing Intelligent (appelé auparavant Livraison intelligente) et comment vous pouvez tirer parti de cette fonctionnalité dans vos campagnes et vos Canvas."

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Timing Intelligent

> Utilisez le Timing Intelligent pour livrer vos messages à chaque utilisateur lorsque Braze détermine que cet utilisateur a plus de chance de s’engager (ouvrir ou cliquer), ce qui est appelé l’heure d’envoi optimale. Vous pourrez vous assurer ainsi plus facilement que vous envoyez des messages à vos utilisateurs à l’heure qu’ils préfèrent ce qui peut entraîner un engagement plus important.

## Cas d’utilisation

- Envoyer des campagnes récurrentes qui ne sont pas sensibles au facteur temps
- Automatiser des campagnes avec des utilisateurs dans plusieurs fuseaux horaires
- Lorsque vous envoyez des messages à vos utilisateurs les plus engagés (ils auront le plus de données d’engagement)

## Fonctionnement

Braze calcule l’heure d’envoi optimale en fonction d’une analyse statistique des dernières interactions de votre utilisateur avec votre application ainsi que leurs interactions avec chaque canal de communication.

Par exemple, Sam peut ouvrir régulièrement vos e-mails le matin, mais elle préfère ouvrir votre application et interagir avec les notifications en soirée. Ceci veut dire que Sam recevrait votre campagne e-mail avec un Timing Intelligent le matin, alors qu’elle recevrait vos campagnes comprenant des notifications push ou des messages in-app en soirée, quand elle a plus de chance d’interagir avec eux.

Si un utilisateur n’a pas assez de données d’engagement pour que Braze calcule l’heure d’envoi optimale, vous pouvez spécifier une [heure de secours](#fallback-time). De plus, les ouvertures automatiques sont exclues de la prise en compte dans le but de calculer un temps optimal.

## Utiliser le Timing Intelligent

Cette section décrit comment configurer le Timing Intelligent pour vos campagnes et vos Canvas.

### Campagnes

Pour utiliser le Timing Intelligent dans vos campagnes :

1. Créez une campagne et composez votre message.
2. Sélectionnez la **livraison planifiée** comme type de livraison.
3. Dans les **Options de planification basées sur le temps**, sélectionnez **Timing Intelligent**.
4. Sélectionnez la date d’envoi. Consultez les [nuances de campagne](#campaign-nuances) pour y trouver des considérations.
5. Déterminez si vous désirez [envoyer uniquement des messages durant des horaires spécifiques](#sending-within-specific-hours).
6. Spécifier l’[heure de secours](#fallback-time). Il s’agit du moment où votre message sera envoyé si un profil utilisateur n’a pas assez de données pour calculer une heure optimale.

![Planifier une campagne avec le timing intelligent][1]

#### Envoyer des messages durant des heures spécifiques {#sending-within-specific-hours}

Si vous le désirez, vous pouvez choisir de limiter l’heure optimale dans une plage horaire donnée. Cela est utile si votre campagne concerne un événement, une vente ou une promotion spécifique.

1. Lors de la configuration du Timing Intelligent, sélectionnez **N’envoyer des messages que pendant une plage horaire donnée**.
2. Saisissez l’heure de début et de fin de la fenêtre de livraison.

![Case à cocher avec « N’envoyer des messages que pendant une plage horaire donnée » sélectionné, pour laquelle la fenêtre horaire est définie entre 8 h et 24 h dans le fuseau horaire de l’utilisateur.][4]

Lorsqu’une fenêtre de livraison est spécifiée, Braze ne regarde que les données d’engagement durant cette période pour déterminer l’heure optimale pour l’utilisateur. S’il n’y a pas assez de données d’engagement au sein de cette fenêtre, le message s’enverra à l’[heure de secours](#fallback-time) définie.

#### Prévisualiser les horaires de livraison

Pour afficher une estimation du nombre d’utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation (uniquement pour les campagnes).

1. Ajouter des segments ou des filtres dans l’étape d’audience cible.
2. Dans la section **Prévisualiser les horaires de livraison** (qui apparaît à la fois dans les étapes d’audiences cibles et de livraison planifiée), sélectionnez votre canal.
3. Cliquez sur **Actualiser les données**.

![][2]

Chaque fois que vous modifiez des paramètres du timing intelligent ou de votre audience de campagne, rafraîchissez à nouveau les données pour afficher un graphique mis à jour.

Le graphique affiche en bleu les utilisateurs qui ont assez de données pour calculer une heure optimale et en rouge les utilisateurs qui utiliseront l’heure de secours. Utilisez les filtres de calcul pour ajuster la prévisualisation pour afficher une visualisation plus granulaire pour chaque groupe d’utilisateur.

#### Nuances de campagne

Voici certaines des nuances que vous devriez connaître lorsque vous planifiez des campagnes avec le timing intelligent.

##### Lancer la campagne

Lancez votre campagne au moins 48 heures avant la date d’envoi planifiée. La variation entre les fuseaux horaires en est la raison. Braze calcule le moment optimal à minuit, heure des Samoa (UTC+13), un des premiers fuseaux horaires du monde. Un jour complet couvre environ 48 heures autour de la planète, ce qui signifie que si vous lancez une campagne pendant ce tampon de 48 heures, il est possible que le moment optimal soit déjà passé dans le fuseau horaire d’un utilisateur et que le message ne s’envoie pas.

{% alert important %}
Si une campagne est lancée et que le moment optimal pour un utilisateur était il y a moins d’une heure, le message sera envoyé immédiatement. Si le moment optimal était il y a plus d’une heure, le message n’est pas envoyé du tout.
{% endalert %}

##### Choisir des segments

Si vous ciblez une audience qui a effectué une action au cours d’une certaine période, autorisez une fenêtre d’au moins 3 jours dans vos filtres de segment. Par exemple, au lieu de `First used these apps more than 1 day ago` et `First used these apps less than 3 days ago`, utilisez 1 jour et 4 jours.

![Filtres pour une audience cible pour lesquels la campagne cible les utilisateurs qui ont utilisé pour la première fois cette application entre 1 et 4 jours auparavant.][3]

Cela est également dû aux fuseaux horaires : sélectionner une période de moins de 3 jours peut faire sortir certains utilisateurs du segment avant que leur moment optimal ne soit atteint.

Apprenez-en plus sur [le moment où Braze vérifie le critère d’éligibilité pour les segments et les filtres]({{site.baseurl}}/user_guide/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

##### Tests A/B avec des optimisations

Si vous tirez parti des [tests A/B avec une optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations), par exemple en envoyant automatiquement la variante gagnante lorsque le test A/B est terminé, la durée de la campagne augmentera. Par défaut, les campagnes de timing intelligent enverront la variante gagnante aux utilisateurs restants le jour après le test d’origine, mais vous pouvez modifier cette date d’envoi.

Si vous utilisez à la fois le timing intelligent et les tests A/B, nous vous recommandons de planifier l’envoi de la variante gagnante 2 jours après le test d’origine au lieu d’un seul.

![Section Test A/B de l’étape d’audiences cibles pour laquelle le test s’achève et envoie la variante gagnante deux jours après le début du test d’origine.][5]

### Canvas

Cette section décrit comment utiliser le Timing Intelligent dans vos Canvas. Ces étapes varient légèrement selon le type de flux de travail Canvas que vous utilisez.

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section est disponible à titre de référence pour comprendre le fonctionnement du Timing Intelligent dans l’éditeur d’origine.<br><br>Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

{% tabs %}
{% tab Canvas Flow %}

Dans Canvas Flow, le timing intelligent est défini dans les étapes de message. Pour utiliser le Timing Intelligent dans vos Canvas :

1. Ajoutez une [étape de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à votre Canvas.
2. Allez dans les **Paramètres de livraison**.
3. Sélectionnez **Utiliser le Timing Intelligent**.
4. Spécifier l’[heure de secours](#fallback-time).

Les messages envoyés dans les 24 heures suivant l’entrée de l’utilisateur dans l’étape de message, la prochaine fois ou leur moment optimal subvient. Les étapes de message ciblant plusieurs canaux peuvent essayer d’envoyer les messages à différents horaires pour divers canaux. Lorsque le premier message dans une étape de message essaie de s’envoyer, tous les utilisateurs progressent automatiquement.

#### Étapes de délai et timing intelligent

Lorsque vous utilisez le timing intelligent après une [étape de délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), la date de livraison peut être différente selon la manière dont vous calculez votre délai. Ceci ne s’applique que lorsque votre délai est défini sur **Après une durée**, étant donné qu’il existe une différence dans la manière dont sont calculés les « jours » et les « jours civils ».

- **Jours :** 1 jour comprend 24 heures et est calculé à partir du moment où l’utilisateur entre dans l’étape de délai.
- **Jours civils :** 1 jour civil est la période entre le moment où l’utilisateur entre dans l’étape de délai et minuit dans son fuseau horaire. Ceci signifie qu’un jour civil peut comporter seulement quelques minutes.

Lorsque vous utilisez le timing intelligent, nous vous recommandons d’utiliser les jours civils en tant que délais au lieu de journées de 24 heures. La raison en est qu’avec les jours civils, le message s’enverra le dernier jour du délai, au moment optimal. Avec une journée de 24 heures, il est possible que le moment optimal de l’utilisateur soit avant son entrée dans l’étape, ce qui veut dire qu’un jour supplémentaire sera ajouté à leur délai.

Par exemple, imaginons que le moment optimal de Luka est à 14 h. Il entre dans l’étape de délai à 14 h 01 le 1er mars et le délai est défini sur 2 jours.

- Le premier jour s’achève le 2 mars à 14 h 01
- Le deuxième jour s’achève le 3 mars à 14 h 01

Cependant, le timing intelligent est défini pour livrer à 14 h, heure qui est déjà passée. Luka ne recevra donc pas le message avant le jour suivant : 4 mars à 14 h 00.

![Graphique montrant la différence entre les jours et les jours civils dans lequel le moment optimal d’un utilisateur est 14 h, mais où il entre dans l’étape de délai à 14 h 01 et le délai est défini sur 2 jours. Les jours livrent le message 3 jours plus tard, car l’utilisateur est entré dans l’étape après son moment optimal, alors que les jours civils livrent le message 2 jours plus tard, le dernier jour du délai.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab Original Canvas workflow %}

Dans le flux de travail Canvas d’origine, le timing intelligent est défini dans la section de délai d’une étape complète. Pour utiliser le Timing Intelligent dans vos Canvas :

1. Ajoutez une étape à votre Canvas.
2. Ouvrez un **délai** pour votre étape.
3. Choisissez **Planifié**.
4. Définissez un délai en utilisant *après*, *dans* ou *au prochain*.
   - Si vous sélectionnez *après*, définissez le délai en jours ou en semaines. Les délais sont calculés automatiquement en jours civils, ce qui veut dire que le message s’envoie le dernier jour du délai au moment optimal pour l’utilisateur. Le timing intelligent n’est pas disponible pour les délais plus courts qu’un jour.
5. Sélectionnez **Utiliser le Timing Intelligent**.
6. Spécifier l’[heure de secours](#fallback-time).

{% endtab %}
{% endtabs %}

### Heure de secours {#fallback-time}

Vous devez choisir une heure de secours pour que le message soit envoyé aux utilisateurs dans votre audience qui ne possèdent pas assez de données d’engagement pour que Braze puisse calculer un moment d’envoi optimal. Deux options existent :

- l’heure la plus populaire d’utilisation de l’application parmi les utilisateurs
- une heure de secours personnalisée donnée (dans le fuseau horaire local de l’utilisateur)

#### L’heure la plus populaire pour l’application

Le moment le plus populaire pour l’application est déterminé par l’heure de début de session moyenne pour votre groupe d’apps (en heure locale). L’heure est affichée en rouge sur le [graphique de prévisualisation](#preview-delivery-times) (uniquement pour les campagnes).

Pour les campagnes, si vous signalez une [fenêtre de livraison](#sending-within-specific-hours) et que l’heure la plus populaire pour utiliser votre application tombe en-dehors de cette fenêtre, le message s’enverra au plus près de la limite de la fenêtre de livraison. Par exemple, si votre fenêtre de livraison est entre 13 h et 20 h et que l’heure la plus populaire pour l’application est 22 h, le message s’enverra à 20 h.

**Pas assez de données de session**<br>
Dans l’éventualité rare dans laquelle votre application n’a pas assez de données de session pour calculer quand l’application est la plus utilisée (une application complètement nouvelle sans données), le message s’enverra à 17 h dans le fuseau horaire local de l’utilisateur. Si le fuseau horaire local de l’utilisateur est inconnu, il s’enverra à 17 h dans le fuseau horaire de votre société.

Il est important de connaître les limitations de l’utilisation précoce du timing intelligent dans le cycle de vie d’un utilisateur lorsque des données limitées sont disponibles. Il est toujours utile, car même les utilisateurs avec peu de sessions enregistrées peuvent offrir des informations sur leur comportement. Cependant, Braze peut calculer plus efficacement l’heure d’envoi optimale plus tard dans le cycle de vie d’un utilisateur.

#### Heure de secours personnalisée

Utilisez une heure de secours personnalisée pour choisir une heure différente à laquelle envoyer le message. De la même manière que pour l’heure la plus populaire de l’application, le message s’enverra à l’heure de secours dans le fuseau horaire local de l’utilisateur. Si le fuseau horaire local de l’utilisateur est inconnu, il s’enverra dans le fuseau horaire de votre société.

Pour les campagnes pour lesquelles une heure de secours personnalisée est définie, si vous lancez votre campagne à moins de 24 heures de la date d’envoi, les utilisateurs pour lesquels le moment d’envoi optimal est déjà dépassé recevront la campagne à l’heure de secours personnalisée. Si l’heure de secours personnalisée spécifiée est déjà passée dans leur fuseau horaire, le message s’enverra immédiatement.

## Limitations

- Le timing intelligent n’est pas disponible pour les campagnes par événement ou déclenchées par API.
- Le timing intelligent ne devrait pas être utilisé dans les scénarios suivants :
    - **Heures calmes :** Il est contreproductif d’utiliser à la fois les heures calmes et le timing intelligent étant donné que les heures calmes sont basées sur une hypothèse descendante du comportement des utilisateurs, comme le fait de ne pas envoyer de message à quelqu’un au milieu de la nuit, alors que le timing intelligent est basé sur l’activité de l’utilisateur. Il est possible que Sam consulte beaucoup ses notifications d’application à 3 h. C’est son choix.
    - **Limitation du taux :** Si une limitation du taux et un timing intelligent sont utilisés, il n’y a aucune garantie quant à la date à laquelle le message sera livré. Les campagnes récurrentes quotidiennes avec Timing Intelligent ne prennent pas en charge avec précision un plafond total d’envoi de messages.
    - **Campagnes de réchauffement d’adresses IP :** Certains comportements de timing intelligent peuvent causer des problèmes pour atteindre les volumes journaliers nécessaires lorsque vous réchauffez pour la première fois vos adresses IP. La raison en est que le timing intelligent évalue deux fois les segments : une fois quand la campagne ou le Canvas est créé et une fois avant de l’envoyer aux utilisateurs pour vérifier s’ils devraient toujours être dans ce segment. Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.

## Résolution des problèmes

### Graphique de prévisualisation affichant peu d’utilisateurs disposant de moments optimaux

Braze a besoin d’un certain nombre de données d’engagement pour réaliser une estimation correcte. S’il n’y a pas assez de données de session ou que les utilisateurs ciblés ont peu ou pas de clics ou d’ouvertures (tels que les nouveaux utilisateurs), Braze passera par défaut sur l’heure de secours. Selon votre configuration, ceci pourrait être soit l’heure la plus populaire pour l’application ou une heure de secours personnalisée.

### Envoyer au-delà de la date planifiée

Votre campagne de timing intelligent peut être envoyée après la date planifiée si vous tirez parti des [tests A/B avec une optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations). Les campagnes utilisant des optimisations de tests A/B peuvent envoyer automatiquement la variante gagnante après que le test A/B est terminé, augmentant ainsi la durée de la campagne. Par défaut, les campagnes avec une optimisation enverront la variante gagnante aux utilisateurs restants le jour après le test d’origine, mais vous pouvez modifier cette date d’envoi.

Si vous utilisez le timing intelligent, nous vous recommandons de laisser plus de temps pour que le test A/B s’achève et de planifier l’envoi de la variante gagnante 2 jours après le test d’origine au lieu d’un seul.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
