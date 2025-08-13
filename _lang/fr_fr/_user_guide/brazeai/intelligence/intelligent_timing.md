---
nav_title: Timing intelligent
article_title: Timing intelligent
page_order: 1.3
description: "Cet article propose un aperçu du Timing Intelligent (appelé auparavant Livraison intelligente) et comment vous pouvez tirer parti de cette fonctionnalité dans vos campagnes et vos Canvas."

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Timing intelligent

> Utilisez le Timing Intelligent pour livrer vos messages à chaque utilisateur lorsque Braze détermine que cet utilisateur a plus de chance de s’engager (ouvrir ou cliquer), ce qui est appelé l’heure d’envoi optimale. Vous pouvez ainsi vérifier plus facilement que vous envoyez des messages à vos utilisateurs au moment qu'ils préfèrent, ce qui peut conduire à un engagement plus important.

## À propos du timing intelligent

Braze calcule l’heure d’envoi optimale en fonction d’une analyse statistique des dernières interactions de votre utilisateur avec votre application ainsi que leurs interactions avec chaque canal de communication. Les données d'interaction suivantes sont utilisées : 

- Horaires des sessions
- Ouverture directe par poussée
- Ouvertures influencées de notification push
- Clics sur des e-mails
- Ouvertures d'e-mail (à l'exclusion des [ouvertures de machines)]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens)

Par exemple, Sam peut ouvrir régulièrement vos e-mails le matin, mais elle préfère ouvrir votre application et interagir avec les notifications en soirée. Ceci veut dire que Sam recevrait une campagne e-mail avec un timing intelligent le matin, alors qu’elle recevrait les campagnes avec notifications push ou messages in-app en soirée, quand elle a plus de chance d’interagir.

Si un utilisateur ne dispose pas de suffisamment de données d'engagement pour que Braze calcule l'heure d'envoi optimale, vous pouvez spécifier une heure de repli.

## Cas d’utilisation

- Envoyer des campagnes récurrentes qui ne sont pas sensibles au facteur temps
- Automatiser des campagnes avec des utilisateurs dans plusieurs fuseaux horaires
- Lorsque vous envoyez des messages à vos utilisateurs les plus engagés (ils auront le plus de données d’engagement)

## Utiliser le Timing Intelligent

Cette section décrit comment configurer le Timing Intelligent pour vos campagnes et vos Canvas.

{% tabs local %}
{% tab Campagne %}
### Étape 1 : Ajouter un timing intelligent

1. Créez une campagne et composez votre message.
2. Sélectionnez la **livraison planifiée** comme type de réception/distribution.
3. Sous **Options de planification en fonction du temps**, sélectionnez **Timing intelligent**.
4. Réglez la fréquence d'entrée. Pour les envois uniques, sélectionnez **Une fois** et choisissez une date d'envoi. Pour les envois récurrents, sélectionnez **Quotidien**, **Hebdomadaire** ou **Mensuel** et configurez les options de récurrence. Voir les [limitations](#limitations) pour plus d'informations.
5. En option, configurez les [heures calmes](#quiet-hours).
6. Spécifiez un [délai de repli](#campaign-fallback). Il s’agit du moment où votre message sera envoyé si un profil utilisateur n’a pas assez de données pour calculer une heure optimale.

![Écran de planification de la campagne montrant le timing intelligent avec l'heure de repli et les heures calmes]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Heures calmes {#quiet-hours}

Utilisez les heures calmes pour empêcher l'envoi de messages pendant certaines heures. Cette fonction est utile lorsque vous souhaitez éviter d'envoyer des messages tôt le matin ou pendant la nuit, tout en permettant à Intelligent Timing de déterminer le meilleur créneau de réception/distribution.

{% alert note %}
Le paramètre Heures calmes a remplacé le paramètre **N'envoyer qu'à des heures précises.**  Au lieu de choisir quand les messages peuvent être envoyés, vous choisissez maintenant quand ils ne doivent pas être envoyés. Par exemple, pour envoyer des messages entre 16 et 18 heures, réglez les heures calmes de 18 à 16 heures le lendemain.
{% endalert %}

1. Sélectionnez **Activer heures calmes**.
2. Sélectionnez l'heure de début et de fin à laquelle il **ne faut pas** envoyer de messages.

![La bascule des heures calmes est activée avec l'heure de début et de fin définie pour bloquer la réception/distribution des messages pendant la nuit]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %}).

Lorsque les heures calmes sont activées, Braze n'envoie pas de messages pendant la période de silence, même si cette période correspond à l'heure d'envoi optimale de l'utilisateur. Si l'heure optimale d'un utilisateur se situe à l'intérieur de la fenêtre de silence, le message sera envoyé à la place au bord le plus proche de la fenêtre.

Par exemple, si les heures calmes sont définies entre 22h00 et 6h00, et que l'heure optimale d'un utilisateur est 5h30, Braze mettra le message en attente et l'enverra à 6h00, soit l'heure la plus proche en dehors de la fenêtre calmes.

#### Prévisualiser les horaires de livraison

Pour afficher une estimation du nombre d’utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation (uniquement pour les campagnes).

1. Ajouter des segments ou des filtres dans l’étape d’audience cible.
2. Dans la section **Prévisualiser les horaires de livraison** (qui apparaît à la fois dans les étapes d’audiences cibles et de livraison planifiée), sélectionnez votre canal.
3. Cliquez sur **Actualiser les données**.

![Graphique de réception/distribution pour Android Push montrant un pic d'engagement entre 12 et 14 heures, et l'heure de l'application la plus populaire étant 14 heures.]({% image_buster /assets/img/intel-timing-preview.png %})

### Étape 2 : Choisissez une date d'envoi

Ensuite, sélectionnez une date d'envoi pour votre campagne. Gardez les points suivants à l'esprit lorsque vous planifiez des campagnes avec le timing intelligent :

#### Lancer la campagne 48 heures à l'avance

Lancez votre campagne au moins 48 heures avant la date d’envoi planifiée. La variation entre les fuseaux horaires en est la raison. Braze calcule le moment optimal à minuit, heure des Samoa (UTC+13), un des premiers fuseaux horaires du monde. Un jour complet couvre environ 48 heures autour de la planète, ce qui signifie que si vous lancez une campagne pendant ce tampon de 48 heures, il est possible que le moment optimal soit déjà passé dans le fuseau horaire d’un utilisateur et que le message ne s’envoie pas.

{% alert important %}
Si une campagne est lancée et que le moment optimal pour un utilisateur était il y a moins d’une heure, le message sera envoyé immédiatement. Si le moment optimal était il y a plus d’une heure, le message n’est pas envoyé du tout.
{% endalert %}

#### Fenêtre de 3 jours pour les filtres de segmentation

Si vous ciblez une audience qui a effectué une action au cours d’une certaine période, autorisez une fenêtre d’au moins 3 jours dans vos filtres de segment. Par exemple, au lieu de `First used app more than 1 day ago` et `First used app less than 3 days ago`, utilisez 1 jour et 4 jours.

![Filtres pour l'audience cible où la campagne vise les utilisateurs qui ont utilisé l'application pour la première fois il y a 1 à 4 jours.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Cela est également dû aux fuseaux horaires : sélectionner une période de moins de 3 jours peut faire sortir certains utilisateurs du segment avant que leur moment optimal ne soit atteint.

Pour plus d'informations, consultez le site [FAQ : Timing intelligent](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Planifier les variantes gagnantes 2 jours après le test A/B

Si vous exploitez les [tests A/B avec une optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), comme l'envoi automatique de la **variante gagnante** ou l'utilisation d'une **variante personnalisée**, le timing intelligent peut affecter la durée et le moment de votre campagne.

Lorsque vous utilisez le timing intelligent, nous vous recommandons de planifier l'heure d'envoi de la variante gagnante au moins **2 jours après le** début du test A/B. Par exemple, si votre test A/B commence le 16 avril à 16h00, planifiez l'envoi de la variante gagnante au plus tôt le 18 avril à 16h00. Cela donne à Braze suffisamment de temps pour évaluer le comportement de l'utilisateur et envoyer des messages au moment optimal.

![Sections du test A/B montrant le test A/B avec la variante gagnante sélectionnée, avec les critères gagnants, la date d'envoi et l'heure d'envoi locale sélectionnés]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Étape 3 : Choisissez une fenêtre de réception/distribution (facultatif)

En option, vous pouvez choisir de limiter la fenêtre de réception/distribution. Cela peut être utile si votre campagne concerne un événement, une vente ou une promotion spécifique, mais n'est généralement pas recommandé lorsque vous utilisez le timing intelligent. Pour plus d'informations, reportez-vous aux [limitations](#limitations).

Lorsque cela est spécifié, Braze utilise uniquement les données d'engagement dans cette fenêtre pour déterminer le délai de réception/distribution optimal d'un utilisateur. S'il n'y a pas suffisamment de données d'engagement dans cette fenêtre, le message est envoyé à l'heure de repli que vous avez définie.

Pour définir une fenêtre de réception/distribution :

1. Lors de la configuration du timing intelligent, sélectionnez **N'envoyer les messages qu'à des heures précises**.
2. Saisissez l’heure de début et de fin de la fenêtre de livraison.

![Case à cocher pour "N'envoyer des messages qu'au cours d'heures spécifiques", où la fenêtre temporelle est fixée entre 8 heures et 12 heures du matin à l'heure locale de l'utilisateur.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Étape 4 : Choisissez une heure de repli {#campaign-fallback}

Choisissez une heure de repli à utiliser si le profil d'un utilisateur ne dispose pas de suffisamment de données pour calculer une heure de réception/distribution optimale.

![Planification d'une campagne avec Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campagne" %}

### Étape 5 : Prévisualiser les horaires de livraison

Pour obtenir une estimation du nombre d'utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation.

1. Ajouter des segments ou des filtres dans l’étape d’audience cible.
2. Dans la section **Prévisualiser les horaires de livraison** (qui apparaît à la fois dans les étapes d’audiences cibles et de livraison planifiée), sélectionnez votre canal.
3. Sélectionnez **Actualiser les données**.

![Exemple d'aperçu des délais de réception/distribution pour Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Chaque fois que vous modifiez des paramètres du timing intelligent ou de votre audience de campagne, rafraîchissez à nouveau les données pour afficher un graphique mis à jour.

Le graphique affiche en bleu les utilisateurs qui ont assez de données pour calculer une heure optimale et en rouge les utilisateurs qui utiliseront l’heure de secours. Utilisez les filtres de calcul pour ajuster la prévisualisation pour afficher une visualisation plus granulaire pour chaque groupe d’utilisateur.
{% endtab %}

{% tab Canvas %}
{% alert important %}
À partir du 28 février 2023, les toiles utilisant l'éditeur original ne pourront plus être créées ou dupliquées. Pour savoir comment passer au nouveau flux de toiles, reportez-vous à la section [Clonage des toiles]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Étape 1 : Ajouter un timing intelligent

Dans votre Canvas, ajoutez une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), puis allez dans **Paramètres de réception/distribution** et sélectionnez **Utiliser le timing intelligent**.

Les messages seront envoyés aux utilisateurs qui ont franchi l'étape ce jour-là à leur heure locale optimale. Toutefois, si l'heure optimale est déjà passée ce jour-là, la livraison sera effectuée à cette heure-là le jour suivant. Les étapes de message ciblant plusieurs canaux peuvent essayer d’envoyer les messages à différents horaires pour divers canaux. Lorsque le premier message dans une étape de message essaie de s’envoyer, tous les utilisateurs progressent automatiquement.

### Étape 2 : Choisissez une heure de repli

Choisissez une heure de repli pour le message à envoyer aux utilisateurs de votre audience qui ne disposent pas de suffisamment de données d'engagement pour que Braze calcule une heure d'envoi optimale. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Étape 4 : Ajouter une étape de retard

Contrairement aux campagnes, vous n'avez pas besoin de lancer votre Canvas 48 heures avant la date d'envoi car le timing intelligent est défini au niveau de l'étape et non du Canvas.

Au lieu de cela, ajoutez une [étape de délai d']({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) au moins deux jours calendrier entre le moment où l'utilisateur entre dans le canvas et celui où il reçoit l'étape de timing intelligent.

#### Calendrier vs. Jours de 24 heures

Lorsque vous utilisez le timing intelligent après une étape de retard, la date de réception/distribution peut varier en fonction de la façon dont vous calculez votre retard. Cela ne s'applique que lorsque votre délai est réglé sur **Après une durée**, car il existe une différence entre le mode de calcul des "jours" et des "jours calendaires".

- **Jours :** 1 jour correspond à 24 heures, calculées à partir du moment où l'utilisateur entre dans l'étape Délai.
- **Jours calendaires :** 1 jour correspond à la période qui s'écoule entre le moment où l'utilisateur entre dans l'étape Délai et minuit dans son fuseau horaire. Ceci signifie qu’un jour civil peut comporter seulement quelques minutes.

Lorsque vous utilisez le timing intelligent, nous vous recommandons d’utiliser les jours civils en tant que délais au lieu de journées de 24 heures. La raison en est qu’avec les jours civils, le message s’enverra le dernier jour du délai, au moment optimal. Avec une journée de 24 heures, il est possible que le moment optimal de l’utilisateur soit avant son entrée dans l’étape, ce qui veut dire qu’un jour supplémentaire sera ajouté à leur délai.

Par exemple, imaginons que le moment optimal de Luka est à 14 h. Il entre dans l’étape de délai à 14 h 01 le 1er mars et le délai est défini sur 2 jours.

- Le premier jour s’achève le 2 mars à 14 h 01
- Le deuxième jour s’achève le 3 mars à 14 h 01

Cependant, le timing intelligent est défini pour livrer à 14 h, heure qui est déjà passée. Luka ne recevra donc pas le message avant le jour suivant : 4 mars à 14 h 00.

![Graphique montrant la différence entre les jours et les jours civils dans lequel le moment optimal d’un utilisateur est 14 h, mais où il entre dans l’étape de délai à 14 h 01 et le délai est défini sur 2 jours. L’option Jours délivre le message 3 jours plus tard parce que l'utilisateur est entré dans l'étape après son heure optimale, alors que l’option Jours calendaires délivre le message 2 jours plus tard, le dernier jour du délai.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitations

- Les messages in-app, les cartes de contenu et les webhooks sont délivrés immédiatement et ne bénéficient pas d’heures optimales.
- Le timing intelligent n’est pas disponible pour les campagnes par événement ou déclenchées par API.
- Le timing intelligent ne devrait pas être utilisé dans les scénarios suivants :
    - **Limite de débit :** Si une limitation du taux et un timing intelligent sont utilisés, il n’y a aucune garantie quant à la date à laquelle le message sera livré. Les campagnes récurrentes quotidiennes avec Timing Intelligent ne prennent pas en charge avec précision un plafond total d’envoi de messages.
    - **Campagnes de réchauffement d'adresses IP :** Certains comportements de timing intelligent peuvent causer des problèmes pour atteindre les volumes journaliers nécessaires lorsque vous réchauffez pour la première fois vos adresses IP. La raison en est que le timing intelligent évalue deux fois les segments : une fois quand la campagne ou le Canvas est créé et une fois avant de l’envoyer aux utilisateurs pour vérifier s’ils devraient toujours être dans ce segment. Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.

## Résolution des problèmes

### Graphique de prévisualisation affichant peu d’utilisateurs disposant de moments optimaux

Braze a besoin d’un certain nombre de données d’engagement pour réaliser une estimation correcte. S’il n’y a pas assez de données de session ou que les utilisateurs ciblés ont peu ou pas de clics ou d’ouvertures (tels que les nouveaux utilisateurs), Braze passera par défaut sur l’heure de secours. Selon votre configuration, ceci pourrait être soit l’heure la plus populaire pour l’application ou une heure de secours personnalisée.

### Envoyer au-delà de la date planifiée

Il se peut que votre campagne de timing intelligent soit envoyée après la date prévue si vous utilisez des [tests A/B avec une optimisation.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) Les campagnes utilisant les optimisations des tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test initial terminé, ce qui augmente la durée de la campagne. Par défaut, les campagnes avec optimisation enverront la variante gagnante aux utilisateurs restants le lendemain du test initial, mais vous pouvez modifier cette date d'envoi.

Si vous utilisez le timing intelligent, nous vous recommandons de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante 2 jours après le test initial au lieu d'un jour.

## Foire aux questions (FAQ) {#faq}

### Généralités

#### Que prédit le timing intelligent ?

Le timing intelligent se concentre sur la prédiction du moment où un utilisateur est le plus susceptible d'ouvrir ou de cliquer sur vos messages pour s'assurer que vos messages atteignent les utilisateurs à des moments d'engagement optimaux.

#### Le timing intelligent est-il calculé séparément pour chaque jour de la semaine ?

Non, le timing intelligent n'est pas lié à des jours spécifiques. Au lieu de cela, il personnalise les heures d'envoi en fonction des modèles d'engagement uniques de chaque utilisateur et du canal que vous utilisez, comme l'e-mail ou les notifications push. Ainsi, vos messages parviennent aux utilisateurs au moment où ils sont le plus réceptifs.

### Calculs

#### Quelles sont les données utilisées pour calculer l'heure optimale pour chaque utilisateur ?

Pour calculer l'heure optimale, utilisez la fonction Timing intelligent :

1. Analyse les données d'interaction de chaque utilisateur enregistrées par le SDK de Braze. Ceci comprend :
  - Horaires des sessions
  - Ouvertures directes de notification push
  - Ouvertures influencées de notification push
  - Clics sur des e-mails
  - Ouvertures d'e-mail (à l'exclusion des ouvertures de machines)
2. Regroupe ces événements par heure, en identifiant l'heure d'envoi optimale pour chaque utilisateur.

#### Les Opens Machine sont-ils pris en compte dans le calcul du temps optimal ?

Non, les [ouvertures de machines]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) sont exclues des calculs du temps optimal. Cela signifie que les heures d'envoi sont basées uniquement sur l'engagement réel des utilisateurs, offrant un timing plus précis pour vos campagnes.

#### Quelle est la précision de la durée optimale ?

Le timing intelligent planifie les messages pendant l'heure où l'utilisateur est le plus engagé, en fonction de ses débuts de session et des événements d'ouverture des messages. Au cours de cette heure, l'heure du message est arrondie aux cinq minutes les plus proches. Par exemple, si l'heure optimale d'un utilisateur est calculée comme étant 16 h 58, le message sera planifié pour 17 h 00. Il peut y avoir de légers retards dans la réception/distribution en raison de l'activité du système pendant les périodes d'affluence.

#### Quels sont les calculs de secours en cas de manque de données ?

S'il y a moins de cinq événements pertinents pour un utilisateur, le timing intelligent utilise l'heure de repli indiquée dans les paramètres de votre message. 

### Campagnes

#### Combien de temps à l’avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ?

Braze calcule le moment optimal à minuit, heure des Samoa, un des premiers fuseaux horaires du monde. Un seul jour couvre environ 48 heures. Par exemple, une personne dont le temps optimal est 12 h 01 qui vit en Australie a déjà dépassé cette heure optimale et il est donc « trop tard » pour leur envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l'avance pour réussir à livrer toutes les personnes qui utilisent votre application dans le monde.

#### Pourquoi ma campagne de timing intelligent affiche-t-elle aucun ou peu d’envois ?

Braze a besoin d’un nombre de points de données de référence pour réaliser une bonne estimation. S'il n'y a pas assez de données de session ou si les utilisateurs ciblés ont peu ou pas de clics ou d'ouvertures d'e-mails (comme les nouveaux utilisateurs), le timing intelligent peut prendre par défaut l'heure la plus populaire de l'espace de travail pour ce jour de la semaine. Si les informations sont insuffisantes concernant l’espace de travail, nous passons à 17 h, l’heure de secours par défaut. Vous pouvez également choisir de fixer un délai de repli spécifique.

#### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ?

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous tirez parti des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes à timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante pour deux jours au lieu d'un. 

### Fonctionnalité

#### Quand est-ce que Braze vérifie les critères d’éligibilité pour les segments ou les filtres d’audience ?

Braze effectue deux vérifications lorsqu’une campagne est lancée :

1. **Vérification initiale :** A minuit dans le premier fuseau horaire le jour de l'envoi.
2. **Vérification de l'heure planifiée :** Juste avant l'envoi, à l'heure de la sélection intelligente choisie par l'utilisateur.

Soyez prudent lorsque vous filtrez sur la base d'autres envois de campagne afin d'éviter de cibler des segments inéligibles. Par exemple, si vous envoyez deux campagnes le même jour à des heures différentes et que vous ajoutez un filtre qui n'autorise les utilisateurs à recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. La raison en est que personne n’était éligible lorsque la campagne a été créée et que les segments ont été formés.

#### Puis-je utiliser des heures calmes dans ma campagne de timing intelligent ?

Les heures calmes peuvent être utilisées dans le cadre d'une campagne utilisant le timing intelligent. L'algorithme de timing intelligent évitera les heures calmes afin d'envoyer le message à tous les utilisateurs éligibles. Cela dit, nous vous recommandons de désactiver les heures calmes, à moins qu'il n'y ait des implications en termes de politique, de conformité ou d'autres implications légales quant au moment où les messages peuvent ou ne peuvent pas être envoyés.

#### Que se passe-t-il si le moment optimal pour un utilisateur se situe pendant les heures calmes ? 

Si l'heure optimale déterminée tombe pendant les heures calmes, Braze trouve le bord le plus proche des heures calmes et planifie le message pour la prochaine heure autorisée avant ou après les heures calmes. Le message est mis en file d'attente pour être envoyé à la limite la plus proche des heures calmes par rapport à l'heure optimale.

#### Puis-je utiliser un timing intelligent et une limitation du taux ?

La limite de débit peut être utilisée dans le cadre d'une campagne utilisant le timing intelligent. Toutefois, en raison de la nature de la limitation du débit, certains utilisateurs peuvent recevoir leur message à un moment qui n'est pas optimal, en particulier si un grand nombre d'utilisateurs par rapport à la taille de la limite de débit sont planifiés au moment du repli en raison d'un manque de données. 

Nous vous recommandons de n'utiliser la limite de débit sur une campagne de timing intelligent que lorsque des exigences techniques doivent être respectées à l'aide de la limite de débit.

#### Puis-je utiliser un timing intelligent pendant le réchauffement d’adresses IP ?

Braze ne recommande pas l'utilisation du timing intelligent lors du premier réchauffement IP, car certains de ses comportements peuvent entraîner des difficultés à atteindre les volumes quotidiens. Cela est provoqué par un timing intelligent évaluant deux fois les segments de campagne. La première fois lorsque la campagne est créée et une seconde fois avant l’envoi aux utilisateurs pour vérifier qu’ils se trouvent toujours bien dans ce segment.

Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.

#### Comment est-ce que le moment le plus populaire pour l’application est-il déterminé ?

L'heure de l'application la plus populaire est déterminée par l'heure moyenne de début de la session pour l'espace de travail (en heure locale). Cet indicateur se trouve dans le tableau de bord lors de la prévisualisation des temps de synchronisation pour une campagne, affiché en rouge.

#### Le timing intelligent tient-il compte des ouvertures de machines ?

Oui, les ouvertures automatiques sont filtrées par le timing intelligent, de sorte qu'elles n'influencent pas son rendement.

#### Comment puis-je m'assurer que le timing intelligent fonctionne le mieux possible ?

Le timing intelligent utilise l'historique individuel de l'engagement de chaque utilisateur dans les messages, quelle que soit l'heure à laquelle il les a reçus. Avant d'utiliser le timing intelligent, assurez-vous d'avoir envoyé aux utilisateurs des messages à différents moments de la journée. De cette manière, vous pouvez "échantillonner" le moment le plus propice pour chaque utilisateur. Un échantillonnage inadéquat des différents moments de la journée peut conduire le timing intelligent à choisir une heure d'envoi non optimale pour un utilisateur.



