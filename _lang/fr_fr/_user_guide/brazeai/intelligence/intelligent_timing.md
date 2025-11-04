---
nav_title: Le timing intelligent
article_title: Le timing intelligent
page_order: 1.3
description: "Cet article donne un aperçu du timing intelligent (anciennement réception/distribution intelligente) et de la manière dont vous pouvez exploiter cette fonctionnalité dans vos campagnes et Canevas."

---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"} Timing intelligent

> Utilisez le timing intelligent pour envoyer votre message à chaque utilisateur au moment où Braze détermine que cet utilisateur est le plus susceptible de s'engager (ouvrir ou cliquer), c'est-à-dire au moment optimal d'envoi. Vous pouvez ainsi vérifier plus facilement que vous envoyez des messages à vos utilisateurs au moment qu'ils préfèrent, ce qui peut conduire à un engagement plus important.

## À propos du timing intelligent

Braze calcule l'heure d'envoi optimale sur la base d'une analyse statistique des interactions passées de votre utilisateur avec votre appli, et de ses interactions avec chaque canal de communication. Les données d'interaction suivantes sont utilisées : 

- Horaires des sessions
- Push Direct Opens
- Ouvertures influencées par la poussée
- Clics sur les e-mails
- Ouvertures d'e-mail (à l'exclusion des [ouvertures de machines)]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens)

Par exemple, Sam peut ouvrir régulièrement vos e-mails le matin, mais elle ouvre votre appli et interagit avec les notifications le soir. Cela signifie que Sam recevrait une campagne e-mail avec timing intelligent le matin, tandis qu'elle recevrait des campagnes avec notifications push le soir, lorsqu'elle est plus susceptible de s'engager.

Si un utilisateur ne dispose pas de suffisamment de données d'engagement pour que Braze calcule l'heure d'envoi optimale, vous pouvez spécifier une heure de repli.

## Cas d'utilisation

- Envoyez des campagnes récurrentes qui ne sont pas soumises à des contraintes de temps
- Automatiser les campagnes avec des utilisateurs situés dans plusieurs fuseaux horaires
- Lors de l'envoi de messages à vos utilisateurs les plus engagés (ce sont eux qui auront le plus de données sur l'engagement).

## Utilisation du timing intelligent

Cette section décrit comment configurer le timing intelligent pour vos campagnes et vos toiles.

{% tabs local %}
{% tab Campaign %}
### Étape 1 : Ajouter un timing intelligent

1. Créez une campagne et composez votre message.
2. Sélectionnez la **livraison planifiée** comme type de **réception/distribution**.
3. Sous **Options de planification en fonction du temps**, sélectionnez **Timing intelligent**.
4. Réglez la fréquence d'entrée. Pour les envois uniques, sélectionnez **Une fois** et choisissez une date d'envoi. Pour les envois récurrents, sélectionnez **Quotidien**, **Hebdomadaire** ou **Mensuel** et configurez les options de récurrence. Voir les [limitations](#limitations) pour plus d'informations.
5. En option, configurez les [heures calmes](#quiet-hours).
6. Spécifiez un [délai de repli](#campaign-fallback). C'est à ce moment-là que le message sera envoyé si le profil de l'utilisateur ne dispose pas de suffisamment de données pour calculer une heure optimale.

L'écran de planification de la campagne montre le timing intelligent avec l'heure de repli et les heures calmes.]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Heures calmes {#quiet-hours}

Utilisez les heures calmes pour empêcher l'envoi de messages pendant certaines heures. Cette fonction est utile lorsque vous souhaitez éviter d'envoyer des messages tôt le matin ou pendant la nuit, tout en permettant à Intelligent Timing de déterminer le meilleur créneau de réception/distribution.

{% alert note %}
Le paramètre Heures calmes a remplacé le paramètre **N'envoyer qu'à des heures précises.**  Au lieu de choisir quand les messages peuvent être envoyés, vous choisissez maintenant quand ils ne doivent pas être envoyés. Par exemple, pour envoyer des messages entre 16 et 18 heures, réglez les heures calmes de 18 à 16 heures le lendemain.
{% endalert %}

1. Sélectionnez **Activer heures calmes**.
2. Sélectionnez l'heure de début et de fin à laquelle il **ne faut pas** envoyer de messages.

Le basculement des heures calmes est activé avec une heure de début et une heure de fin pour bloquer la réception/distribution des messages pendant la nuit.]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Lorsque les heures calmes sont activées, Braze n'envoie pas de messages pendant la période de silence, même si cette période correspond à l'heure d'envoi optimale de l'utilisateur. Si l'heure optimale d'un utilisateur tombe dans la fenêtre de silence, le message sera envoyé à la place au bord le plus proche de la fenêtre.

Par exemple, si les heures calmes sont définies entre 22h00 et 6h00, et que l'heure optimale d'un utilisateur est 5h30, Braze mettra le message en attente et l'enverra à 6h00, soit l'heure la plus proche en dehors de la fenêtre calmes.

#### Prévisualisation des délais de réception/distribution

Pour obtenir une estimation du nombre d'utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation (campagnes uniquement).

1. Ajoutez des segments ou des filtres dans l'étape Audiences cibles.
2. Dans la section **Prévisualiser les heures de réception/distribution pour** (qui apparaît à la fois dans les étapes Cibler les audiences et Planifier la réception/distribution), sélectionnez votre chaîne.
3. Cliquez sur **Actualiser les données**.

Graphique de réception/distribution pour Android Push montrant un pic d'engagement entre 12h et 14h, et l'heure de l'application la plus populaire étant 14h.]({% image_buster /assets/img/intel-timing-preview.png %})

### Étape 2 : Choisissez une date d'envoi

Ensuite, sélectionnez une date d'envoi pour votre campagne. Gardez les points suivants à l'esprit lorsque vous planifiez des campagnes avec le timing intelligent :

#### Lancer la campagne 48 heures à l'avance

Lancez votre campagne au moins 48 heures avant la date d'envoi prévue. Ceci est dû aux variations des fuseaux horaires. Braze calcule l'heure optimale à minuit en heure de Samoa (UTC+13), l'un des premiers fuseaux horaires au monde. Une journée s'étend sur environ 48 heures dans le monde entier, ce qui signifie que si vous lancez une campagne dans ce laps de temps de 48 heures, il est possible que l'heure optimale d'un utilisateur soit déjà passée dans son fuseau horaire et que le message ne soit pas envoyé.

{% alert important %}
Si une campagne est lancée et que le temps optimal d'un utilisateur est de moins d'une heure, le message est envoyé immédiatement. Si l'heure optimale se situe plus d'une heure dans le passé, le message n'est pas envoyé du tout.
{% endalert %}

#### Fenêtre de 3 jours pour les filtres de segmentation

Si vous ciblez une audience qui a effectué une action dans un certain laps de temps, prévoyez une fenêtre d'au moins 3 jours dans vos filtres de segmentation. Par exemple, au lieu de `First used app more than 1 day ago` et `First used app less than 3 days ago`, utilisez 1 jour et 4 jours.

\![Filtres pour l'audience cible où la campagne vise les utilisateurs qui ont utilisé l'application pour la première fois il y a entre 1 et 4 jours.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Cela s'explique également par les fuseaux horaires : en choisissant une période de moins de trois jours, certains utilisateurs risquent de sortir du segment avant que leur heure d'envoi optimale ne soit atteinte.

Pour plus d'informations, consultez le site [FAQ : Timing intelligent](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Planifier les variantes gagnantes 2 jours après le test A/B

Si vous exploitez les [tests A/B avec une optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), comme l'envoi automatique de la **variante gagnante** ou l'utilisation d'une **variante personnalisée**, le timing intelligent peut affecter la durée et le moment de votre campagne.

Lorsque vous utilisez le timing intelligent, nous vous recommandons de planifier l'heure d'envoi de la variante gagnante au moins **2 jours après le** début du test A/B. Par exemple, si votre test A/B commence le 16 avril à 16h00, planifiez l'envoi de la variante gagnante au plus tôt le 18 avril à 16h00. Cela donne à Braze suffisamment de temps pour évaluer le comportement de l'utilisateur et envoyer des messages au moment optimal.

Les sections de test A/B montrent le test A/B avec la variante gagnante sélectionnée, avec les critères gagnants, la date d'envoi et l'heure d'envoi locale sélectionnées.]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Étape 3 : Choisissez une fenêtre de réception/distribution (facultatif)

En option, vous pouvez choisir de limiter la fenêtre de réception/distribution. Cela peut être utile si votre campagne concerne un événement, une vente ou une promotion spécifique, mais n'est généralement pas recommandé lorsque vous utilisez le timing intelligent. Pour plus d'informations, reportez-vous aux [limitations](#limitations).

Lorsque cela est spécifié, Braze utilise uniquement les données d'engagement dans cette fenêtre pour déterminer le délai de réception/distribution optimal d'un utilisateur. S'il n'y a pas suffisamment de données d'engagement dans cette fenêtre, le message est envoyé à l'heure de repli que vous avez définie.

Pour définir une fenêtre de réception/distribution :

1. Lors de la configuration du timing intelligent, sélectionnez **N'envoyer les messages qu'à des heures précises**.
2. Saisissez l'heure de début et de fin de la fenêtre de réception/distribution.

\![Case à cocher pour "N'envoyer des messages qu'au cours d'heures spécifiques" sélectionnée, où la fenêtre temporelle est fixée entre 8 h et 12 h à l'heure locale de l'utilisateur.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Étape 4 : Choisissez une heure de repli {#campaign-fallback}

Choisissez une heure de repli à utiliser si le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure de réception/distribution optimale.

!Planification d'une campagne avec le timing intelligent]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Étape 5 : Prévisualisation des délais de réception/distribution

Pour obtenir une estimation du nombre d'utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation.

1. Ajoutez des segments ou des filtres dans l'étape Audiences cibles.
2. Dans la section **Prévisualiser les heures de réception/distribution pour** (qui apparaît à la fois dans les étapes Cibler les audiences et Planifier la réception/distribution), sélectionnez votre chaîne.
3. Sélectionnez **Actualiser les données**.

!Exemple d'aperçu des délais de réception/distribution pour Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Chaque fois que vous modifiez des paramètres concernant le timing intelligent ou l'audience de votre campagne, actualisez à nouveau les données pour afficher un graphique mis à jour.

Le graphique montre en bleu les utilisateurs qui avaient suffisamment de données pour calculer un temps optimal et en rouge les utilisateurs qui utiliseront le temps de repli. Utilisez les filtres de calcul pour ajuster l'aperçu afin d'obtenir une vue plus granulaire de l'un ou l'autre groupe d'utilisateurs.
{% endtab %}

{% tab Canvas %}

### Étape 1 : Ajouter un timing intelligent

Dans votre Canvas, ajoutez une [étape du message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), puis allez dans **Paramètres de** **réception/distribution** et sélectionnez **Utiliser le timing intelligent**.

Les messages seront envoyés aux utilisateurs qui ont franchi l'étape ce jour-là à leur heure locale optimale. Toutefois, si l'heure optimale est déjà passée ce jour-là, la livraison sera effectuée à cette heure-là le jour suivant. Les étapes du message qui ciblent plusieurs canaux peuvent envoyer ou tenter d'envoyer des messages à des moments différents pour différents canaux. Lorsque le premier message d'une étape Message tente d'être envoyé, tous les utilisateurs sont automatiquement avancés.

### Étape 2 : Choisissez une heure de repli

Choisissez une heure de repli pour le message à envoyer aux utilisateurs de votre audience qui ne disposent pas de suffisamment de données d'engagement pour que Braze calcule une heure d'envoi optimale. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Étape 4 : Ajouter une étape de retard

Contrairement aux campagnes, vous n'avez pas besoin de lancer votre Canvas 48 heures avant la date d'envoi car le timing intelligent est défini au niveau de l'étape et non du Canvas.

Au lieu de cela, ajoutez une [étape de délai d']({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) au moins deux jours calendrier entre le moment où l'utilisateur entre dans le canvas et celui où il reçoit l'étape de timing intelligent.

#### Calendrier vs. Jours de 24 heures

Lorsque vous utilisez le timing intelligent après une étape de retard, la date de réception/distribution peut varier en fonction de la façon dont vous calculez votre retard. Cela ne s'applique que lorsque votre délai est réglé sur **Après une durée**, car il existe une différence entre le mode de calcul des "jours" et des "jours calendaires".

- **Jours :** 1 jour correspond à 24 heures, calculées à partir du moment où l'utilisateur entre dans l'étape Délai.
- **Jours calendaires :** 1 jour correspond à la période qui s'écoule entre le moment où l'utilisateur entre dans l'étape Délai et minuit dans son fuseau horaire. Cela signifie qu'un jour calendaire peut être aussi court que quelques minutes.

Lorsque vous utilisez le timing intelligent, nous vous recommandons d'utiliser des jours calendaires pour vos retards plutôt que des jours de 24 heures. En effet, avec les jours calendaires, le message sera envoyé le dernier jour du délai, au moment optimal. Avec une journée de 24 heures, il est possible que l'heure optimale de l'utilisateur se situe avant qu'il n'entre dans l'étape, ce qui signifie qu'un jour supplémentaire sera ajouté à son délai.

Par exemple, supposons que l'heure optimale de Luka soit 14 heures. Il entre dans l'étape Délai à 14h01 le 1er mars, et le délai est fixé à 2 jours.

- Le jour 1 se termine le 2 mars à 14h01
- Le jour 2 se termine le 3 mars à 14h01

Cependant, le timing intelligent est prévu pour une livraison à 14 heures, heure déjà passée. Luka ne recevra donc le message que le lendemain : Le 4 mars à 14 heures.

Graphique illustrant la différence entre les jours et les jours calendaires : si l'heure optimale d'un utilisateur est 14 heures, mais qu'il entre dans l'étape de retardement à 14 h 01 et que le délai est fixé à 2 jours. Days délivre le message 3 jours plus tard parce que l'utilisateur est entré dans l'étape après son heure optimale, tandis que calendar days délivre le message 2 jours plus tard, le dernier jour du délai.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limites

- Les messages in-app, les cartes de contenu et les webhooks sont délivrés immédiatement et ne bénéficient pas de délais optimaux.
- Le timing intelligent n'est pas disponible pour les campagnes basées sur des actions ou déclenchées par l'API.
- Le timing intelligent ne doit pas être utilisé dans les scénarios suivants :
    - **Limite de débit :** Si la limitation du débit et le timing intelligent sont tous deux utilisés, il n'y a aucune garantie quant au moment où le message sera délivré. Les campagnes quotidiennes récurrentes avec le timing intelligent ne prennent pas en charge avec précision un plafond d'envoi total de messages.
    - **Campagnes de réchauffement d'adresses IP :** Certains comportements du timing intelligent peuvent entraîner des difficultés à atteindre les volumes quotidiens nécessaires lorsque vous commencez à chauffer votre IP. En effet, le timing intelligent évalue les segments à deux reprises - une première fois lors de la création de la campagne ou du canvas, et une seconde fois avant l'envoi aux utilisateurs afin de vérifier qu'ils devraient toujours faire partie de ce segment. Les segments peuvent ainsi se déplacer et changer, ce qui conduit souvent certains utilisateurs à sortir du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond d'utilisateurs que vous pouvez atteindre.

## Résolution des problèmes

### Graphique de prévisualisation montrant quelques utilisateurs avec des temps optimaux

Braze a besoin d'un certain nombre de données d'engagement pour faire une bonne estimation. S'il n'y a pas assez de données de session ou si les utilisateurs ciblés ont peu ou pas de clics ou d'ouvertures (comme les nouveaux utilisateurs), Braze adopte par défaut le délai de repli. Selon votre configuration, il peut s'agir de l'heure de l'application la plus populaire ou d'une heure de repli personnalisée.

### Impact du fuseau horaire sur la réception/distribution du timing intelligent

Le timing intelligent s'appuie sur le fuseau horaire local spécifié de chaque utilisateur, de sorte que la date et l'heure de réception/distribution prévues peuvent varier d'un utilisateur à l'autre.

Si les utilisateurs ne reçoivent pas les messages comme prévu, vérifiez que le champ du fuseau horaire dans leur profil est correctement renseigné. Si le champ du fuseau horaire est vide, l'utilisateur peut recevoir des messages qui s'alignent sur le fuseau horaire de l'entreprise au lieu de son heure locale.

### Envoi au-delà de la date planifiée

Il se peut que votre campagne de timing intelligent soit envoyée après la date prévue si vous utilisez des [tests A/B avec une optimisation.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) Les campagnes utilisant les optimisations des tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test initial terminé, ce qui augmente la durée de la campagne. Par défaut, les campagnes avec optimisation enverront la variante gagnante aux utilisateurs restants le lendemain du test initial, mais vous pouvez modifier cette date d'envoi.

Si vous utilisez le timing intelligent, nous vous recommandons de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante 2 jours après le test initial au lieu d'un jour.

## Foire aux questions (FAQ) {#faq}

### Général

#### Que prédit le timing intelligent ?

Le timing intelligent se concentre sur la prédiction du moment où un utilisateur est le plus susceptible d'ouvrir ou de cliquer sur vos messages pour s'assurer que vos messages atteignent les utilisateurs à des moments d'engagement optimaux.

#### Le timing intelligent est-il calculé séparément pour chaque jour de la semaine ?

Non, le timing intelligent n'est pas lié à des jours spécifiques. Au lieu de cela, il personnalise les heures d'envoi en fonction des modèles d'engagement uniques de chaque utilisateur et du canal que vous utilisez, comme l'e-mail ou les notifications push. Ainsi, vos messages parviennent aux utilisateurs au moment où ils sont le plus réceptifs.

### Calculs

#### Quelles sont les données utilisées pour calculer l'heure optimale pour chaque utilisateur ?

Pour calculer l'heure optimale, utilisez la fonction Timing intelligent :

1. Analyse les données d'interaction de chaque utilisateur enregistrées par le SDK de Braze. Il s'agit notamment de
  - Horaires des sessions
  - Ouverture directe par poussée
  - La poussée influencée s'ouvre
  - Clics sur l'e-mail
  - Ouvertures d'e-mail (à l'exclusion des ouvertures de machines)
2. Regroupe ces événements par heure, en identifiant l'heure d'envoi optimale pour chaque utilisateur.

#### Les Opens Machine sont-ils pris en compte dans le calcul du temps optimal ?

Non, les [ouvertures de machines]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) sont exclues des calculs du temps optimal. Cela signifie que les heures d'envoi sont basées uniquement sur l'engagement réel des utilisateurs, offrant un timing plus précis pour vos campagnes.

#### Quelle est la précision de la durée optimale ?

Le timing intelligent planifie les messages pendant l'heure où l'utilisateur est le plus engagé, en fonction de ses débuts de session et des événements d'ouverture des messages. Au cours de cette heure, l'heure du message est arrondie aux cinq minutes les plus proches. Par exemple, si l'heure optimale d'un utilisateur est calculée comme étant 16 h 58, le message sera planifié pour 17 h 00. Il peut y avoir de légers retards dans la réception/distribution en raison de l'activité du système pendant les périodes d'affluence.

#### Quels sont les calculs de secours en cas de manque de données ?

S'il y a moins de cinq événements pertinents pour un utilisateur, le timing intelligent utilise l'heure de repli indiquée dans les paramètres de votre message. 

### Campagnes

#### Combien de temps à l'avance dois-je lancer une campagne de timing intelligent pour qu'elle soit diffusée avec succès à tous les utilisateurs dans tous les fuseaux horaires ?

Braze calcule l'heure optimale à minuit à l'heure de Samoa, l'un des premiers fuseaux horaires au monde. En une seule journée, elle s'étend sur environ 48 heures. Par exemple, une personne dont l'heure optimale est 0h01 et qui vit en Australie a déjà vu son heure optimale passer, et il est "trop tard" pour lui envoyer. Pour ces raisons, vous devez planifier 48 heures à l'avance pour réussir à livrer toutes les personnes qui utilisent votre application dans le monde.

#### Pourquoi ma campagne de timing intelligent n'envoie-t-elle que peu ou pas d'envois ?

Braze a besoin d'un nombre de points de données de référence pour faire une bonne estimation. S'il n'y a pas assez de données de session ou si les utilisateurs ciblés ont peu ou pas de clics ou d'ouvertures d'e-mails (comme les nouveaux utilisateurs), le timing intelligent peut prendre par défaut l'heure la plus populaire de l'espace de travail pour ce jour de la semaine. S'il n'y a pas assez d'informations sur l'espace de travail, nous revenons à l'heure par défaut de 17 heures. Vous pouvez également choisir de fixer un délai de repli spécifique.

#### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date prévue ?

Il se peut que votre campagne de timing intelligent soit envoyée après la date prévue parce que vous avez recours à des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes à timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante pour deux jours au lieu d'un. 

### Fonctionnalité

#### Quand Braze vérifie-t-il les critères d'éligibilité des filtres de segmentation et d'audience ?

Braze effectue deux contrôles lorsqu'une campagne est lancée :

1. **Vérification initiale :** A minuit dans le premier fuseau horaire le jour de l'envoi.
2. **Vérification de l'heure planifiée :** Juste avant l'envoi, à l'heure de la sélection intelligente choisie par l'utilisateur.

Soyez prudent lorsque vous filtrez sur la base d'autres envois de campagne afin d'éviter de cibler des segments inéligibles. Par exemple, si vous envoyez deux campagnes le même jour à des heures différentes et que vous ajoutez un filtre qui n'autorise les utilisateurs à recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. En effet, personne n'était éligible au moment de la création de la campagne et de la formation des segments.

#### Puis-je utiliser les heures calmes dans ma campagne de timing intelligent ?

Les heures calmes peuvent être utilisées dans le cadre d'une campagne utilisant le timing intelligent. L'algorithme de timing intelligent évitera les heures calmes afin d'envoyer le message à tous les utilisateurs éligibles. Cela dit, nous vous recommandons de désactiver les heures calmes, à moins qu'il n'y ait des implications en termes de politique, de conformité ou d'autres implications légales quant au moment où les messages peuvent ou ne peuvent pas être envoyés.

#### Que se passe-t-il si le moment optimal pour un utilisateur se situe pendant les heures calmes ? 

Si l'heure optimale déterminée tombe pendant les heures calmes, Braze trouve le bord le plus proche des heures calmes et planifie le message pour la prochaine heure autorisée avant ou après les heures calmes. Le message est mis en file d'attente pour être envoyé à la limite la plus proche des heures calmes par rapport à l'heure optimale.

#### Puis-je utiliser le timing intelligent et la limitation de débit ?

La limite de débit peut être utilisée dans le cadre d'une campagne utilisant le timing intelligent. Toutefois, en raison de la nature de la limitation du débit, certains utilisateurs peuvent recevoir leur message à un moment qui n'est pas optimal, en particulier si un grand nombre d'utilisateurs par rapport à la taille de la limite de débit sont planifiés au moment du repli en raison d'un manque de données. 

Nous vous recommandons de n'utiliser la limite de débit sur une campagne de timing intelligent que lorsque des exigences techniques doivent être respectées à l'aide de la limite de débit.

#### Puis-je utiliser le timing intelligent pendant le réchauffement IP ?

Braze ne recommande pas l'utilisation du timing intelligent lors du premier réchauffement IP, car certains de ses comportements peuvent entraîner des difficultés à atteindre les volumes quotidiens. Ce problème est dû au fait que le timing intelligent évalue deux fois les segments de la campagne. Une première fois lors de la création de la campagne et une seconde fois avant l'envoi aux utilisateurs pour vérifier qu'ils font toujours partie de ce segment.

Les segments peuvent ainsi se déplacer et changer, ce qui conduit souvent certains utilisateurs à sortir du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond d'utilisateurs que vous pouvez atteindre.

#### Comment est déterminée l'heure de l'application la plus populaire ?

L'heure de l'application la plus populaire est déterminée par l'heure moyenne de début de la session pour l'espace de travail (en heure locale). Vous trouverez ces indicateurs en rouge dans le tableau de bord lorsque vous prévisualisez les heures d'une campagne.

#### Le timing intelligent tient-il compte des ouvertures de machines ?

Oui, les ouvertures de machines sont filtrées par le timing intelligent, de sorte qu'elles n'influencent pas son rendement.

#### Comment puis-je m'assurer que le timing intelligent fonctionne le mieux possible ?

Le timing intelligent utilise l'historique individuel de l'engagement de chaque utilisateur dans les messages, quelle que soit l'heure à laquelle il les a reçus. Avant d'utiliser le timing intelligent, assurez-vous d'avoir envoyé aux utilisateurs des messages à différents moments de la journée. De cette manière, vous pouvez "échantillonner" le moment le plus propice pour chaque utilisateur. Un échantillonnage inadéquat des différents moments de la journée peut conduire Intelligent Timing à choisir une heure d'envoi sous-optimale pour un utilisateur.



