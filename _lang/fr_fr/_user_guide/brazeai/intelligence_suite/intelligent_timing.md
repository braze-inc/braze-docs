---
nav_title: Timing intelligent
article_title: Timing intelligent
page_order: 1.3
description: "Cet article propose un aperçu du Timing Intelligent (appelé auparavant Livraison intelligente) et comment vous pouvez tirer parti de cette fonctionnalité dans vos campagnes et vos Canvas."

---

# [![Cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"} Intelligent Timing

> Utilisez le timing intelligent pour transmettre votre message à chaque utilisateur au moment où Braze détermine le moment optimal d'envoi, c'est-à-dire lorsque l'utilisateur est le plus susceptible d'interagir (ouvrir ou cliquer). Cela vous permet de vérifier plus facilement que vous effectuez l'envoi de messages à vos utilisateurs à l'heure qui leur convient le mieux, ce qui peut entraîner un engagement accru.

## À propos du timing intelligent

Braze détermine le moment optimal pour l'envoi en se basant sur une analyse statistique des interactions passées de vos utilisateurs avec votre application et de leurs interactions avec chaque canal de communication. Les données d'interaction suivantes sont utilisées : 

- Horaires des sessions
- Ouverture directe par poussée
- Ouvertures influencées de notification push
- Clics sur des e-mails
- Ouvertures d'e-mail (à l'exclusion des [ouvertures de machines)]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens)
- Clics SMS (uniquement si [le raccourcissement des liens]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) et le suivi avancé sont activés)

Par exemple, Sam peut ouvrir régulièrement vos e-mails le matin, mais elle préfère ouvrir votre application et interagir avec les notifications en soirée. Ceci veut dire que Sam recevrait une campagne e-mail avec un timing intelligent le matin, alors qu’elle recevrait les campagnes avec notifications push ou messages in-app en soirée, quand elle a plus de chance d’interagir.

Si un utilisateur ne dispose d'aucune donnée d'engagement pertinente permettant à Braze de calculer l'heure d'envoi optimale, vous pouvez définir une heure de secours.

## Cas d’utilisation

- Envoyer des campagnes récurrentes qui ne sont pas sensibles au facteur temps
- Automatiser des campagnes avec des utilisateurs dans plusieurs fuseaux horaires
- Lorsque vous envoyez des messages à vos utilisateurs les plus engagés (ils auront le plus de données d’engagement)

## Utiliser le Timing Intelligent

Cette section décrit comment configurer le Timing Intelligent pour vos campagnes et vos Canvas.

{% tabs local %}
{% tab Campaign %}
### Étape 1 : Ajouter un timing intelligent

1. Créez une campagne et composez votre message.
2. Sélectionnez la **livraison planifiée** comme type de réception/distribution.
3. Sous **Options de planification en fonction du temps**, sélectionnez **Timing intelligent**.
4. Réglez la fréquence d'entrée. Pour les envois uniques, sélectionnez **Une fois** et choisissez une date d'envoi. Pour les envois récurrents, sélectionnez **Quotidien**, **Hebdomadaire** ou **Mensuel** et configurez les options de récurrence. Voir les [limitations](#limitations) pour plus d'informations.
5. En option, configurez les [heures calmes](#quiet-hours).
6. Spécifiez un [délai de repli](#campaign-fallback). Ce message est envoyé lorsque le profil utilisateur ne contient aucun événement pertinent permettant de calculer un moment optimal.

![Écran de planification de campagne affichant le réglage de timing intelligent avec les paramètres de temps de secours et d'heures calmes]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Heures calmes {#quiet-hours}

Utilisez les heures calmes pour empêcher l'envoi de messages pendant certaines heures. Cette fonction est utile lorsque vous souhaitez éviter d'envoyer des messages tôt le matin ou pendant la nuit, tout en permettant à Intelligent Timing de déterminer le meilleur créneau de réception/distribution.

{% alert note %}
Le paramètre Heures calmes a remplacé le paramètre **N'envoyer qu'à des heures précises.** Au lieu de choisir quand les messages peuvent être envoyés, vous choisissez maintenant quand ils ne doivent pas être envoyés. Par exemple, pour envoyer des messages entre 16 et 18 heures, réglez les heures calmes de 18 à 16 heures le lendemain.
{% endalert %}

1. Sélectionnez **Activer heures calmes**.
2. Sélectionnez l'heure de début et de fin à laquelle il **ne faut pas** envoyer de messages.

![La fonction « Heures calmes » est basculée, avec des heures de début et de fin définies pour bloquer la réception/distribution des messages pendant la nuit.]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Lorsque les heures calmes sont activées, Braze n'envoie pas de messages pendant la période de silence, même si cette période correspond à l'heure d'envoi optimale de l'utilisateur. Si l'heure optimale d'un utilisateur se situe à l'intérieur de la fenêtre de silence, le message sera envoyé à la place au bord le plus proche de la fenêtre.

Par exemple, si les heures calmes sont définies entre 22h00 et 6h00, et que l'heure optimale d'un utilisateur est 5h30, Braze mettra le message en attente et l'enverra à 6h00, soit l'heure la plus proche en dehors de la fenêtre calmes.

#### Prévisualiser les horaires de livraison

Pour afficher une estimation du nombre d’utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation (uniquement pour les campagnes).

1. Ajouter des segments ou des filtres dans l’étape d’audience cible.
2. Dans la section **Prévisualiser les horaires de livraison** (qui apparaît à la fois dans les étapes d’audiences cibles et de livraison planifiée), sélectionnez votre canal.
3. Cliquez sur **Actualiser les données**.

![Le graphique de prévisualisation de la réception/distribution pour Android Push indique que le pic d'engagement se situe entre 12 h et 14 h, et que l'heure la plus populaire pour l'application est 14 h.]({% image_buster /assets/img/intel-timing-preview.png %})

### Étape 2 : Choisissez une date d'envoi

Ensuite, sélectionnez une date d'envoi pour votre campagne. Veuillez garder à l'esprit les points suivants lors de la planification de campagnes avec le timing intelligent :

#### Lancer la campagne 48 heures à l'avance

Lancez votre campagne au moins 48 heures avant la date d’envoi planifiée. La variation entre les fuseaux horaires en est la raison. Braze calcule le moment optimal à minuit, heure des Samoa (UTC+13), un des premiers fuseaux horaires du monde. Une journée dure environ 48 heures à travers le monde, ce qui signifie que si vous lancez une campagne dans ce délai de 48 heures, il est possible que le moment optimal pour un utilisateur soit déjà passé dans son fuseau horaire et que le message ne soit pas envoyé.

{% alert important %}
Si une campagne est lancée et que le moment optimal pour un utilisateur était il y a moins d’une heure, le message sera envoyé immédiatement. Si le moment optimal était il y a plus d’une heure, le message n’est pas envoyé du tout.
{% endalert %}

#### Fenêtre de 3 jours pour les filtres de segmentation

Si vous ciblez une audience qui a effectué une action au cours d’une certaine période, autorisez une fenêtre d’au moins 3 jours dans vos filtres de segment. Par exemple, au lieu de `First used app more than 1 day ago` et `First used app less than 3 days ago`, utilisez 1 jour et 4 jours.

![Filtres pour l'audience cible lorsque la campagne vise les utilisateurs qui ont utilisé l'application pour la première fois il y a 1 à 4 jours.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Cela est également dû aux fuseaux horaires : sélectionner une période de moins de 3 jours peut faire sortir certains utilisateurs du segment avant que leur moment optimal ne soit atteint.

Pour plus d'informations, consultez le site [FAQ : Timing intelligent](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### La planification des variantes gagnantes deux jours après le test A/B

Si vous exploitez les [tests A/B avec une optimisation]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), comme l'envoi automatique de la **variante gagnante** ou l'utilisation d'une **variante personnalisée**, le timing intelligent peut affecter la durée et le moment de votre campagne.

Lorsque vous utilisez le timing intelligent, nous vous recommandons de planifier l'heure d'envoi de la variante gagnante au moins **2 jours après le** début du test A/B. Par exemple, si votre test A/B commence le 16 avril à 16h00, planifiez l'envoi de la variante gagnante au plus tôt le 18 avril à 16h00. Cela donne à Braze suffisamment de temps pour évaluer le comportement de l'utilisateur et envoyer des messages au moment optimal.

![Sections de test A/B affichant le test A/B avec la variante gagnante sélectionnée, les critères de sélection, la date d'envoi et l'heure locale d'envoi.]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Étape 3 : Choisissez une fenêtre de réception/distribution (facultatif)

En option, vous pouvez choisir de limiter la fenêtre de réception/distribution. Cela peut être utile si votre campagne concerne un événement, une vente ou une promotion spécifique, mais n'est généralement pas recommandé lorsque vous utilisez le timing intelligent. Pour plus d'informations, reportez-vous aux [limitations](#limitations).

Lorsque cela est spécifié, Braze utilise uniquement les données d'engagement dans cette fenêtre pour déterminer le délai de réception/distribution optimal d'un utilisateur. Si aucun événement pertinent ne se produit pendant cette période, le message sera envoyé à l'heure de secours que vous avez définie.

Pour définir une fenêtre de réception/distribution :

1. Lors de la configuration du timing intelligent, sélectionnez **N'envoyer les messages qu'à des heures précises**.
2. Saisissez l’heure de début et de fin de la fenêtre de livraison.

![Case à cocher avec « N’envoyer des messages que pendant une plage horaire donnée » sélectionné, pour laquelle la fenêtre horaire est définie entre 8 h et 24 h dans le fuseau horaire de l’utilisateur.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Étape 4 : Choisissez une heure de repli {#campaign-fallback}

Veuillez sélectionner une heure de repli à utiliser si le profil utilisateur ne contient aucun événement pertinent pour calculer une heure de réception/distribution optimale.

![Planifier une campagne avec le timing intelligent]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Étape 5 : Prévisualiser les horaires de livraison

Pour obtenir une estimation du nombre d'utilisateurs qui recevront le message à chaque heure de la journée, utilisez le graphique de prévisualisation.

1. Ajouter des segments ou des filtres dans l’étape d’audience cible.
2. Dans la section **Prévisualiser les horaires de livraison** (qui apparaît à la fois dans les étapes d’audiences cibles et de livraison planifiée), sélectionnez votre canal.
3. Sélectionnez **Actualiser les données**.

![Exemple d'aperçu des délais de réception/distribution pour Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Chaque fois que vous modifiez des paramètres du timing intelligent ou de votre audience de campagne, rafraîchissez à nouveau les données pour afficher un graphique mis à jour.

Le graphique indique en bleu les utilisateurs qui ont eu des événements pertinents pour calculer un moment optimal et en rouge ceux qui utiliseront le moment de repli. Utilisez les filtres de calcul pour ajuster la prévisualisation pour afficher une visualisation plus granulaire pour chaque groupe d’utilisateur.
{% endtab %}

{% tab Canvas %}

### Étape 1 : Ajouter un timing intelligent

Dans votre Canvas, ajoutez une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), puis allez dans **Paramètres de réception/distribution** et sélectionnez **Utiliser le timing intelligent**.

Les messages seront envoyés aux utilisateurs qui ont franchi l'étape ce jour-là à leur heure locale optimale. Toutefois, si l'heure optimale est déjà passée ce jour-là, la livraison sera effectuée à cette heure-là le jour suivant. Les étapes de message ciblant plusieurs canaux peuvent essayer d’envoyer les messages à différents horaires pour divers canaux. Lorsque le premier message dans une étape de message essaie de s’envoyer, tous les utilisateurs progressent automatiquement.

### Étape 2 : Choisissez une heure de repli

Veuillez sélectionner une heure de secours pour l'envoi du message aux utilisateurs de votre audience qui ne disposent pas de données d'engagement pertinentes permettant à Braze de calculer l'heure d'envoi optimale. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Étape 4 : Ajouter une étape de retard

Contrairement aux campagnes, vous n'avez pas besoin de lancer votre Canvas 48 heures avant la date d'envoi car le timing intelligent est défini au niveau de l'étape et non du Canvas.

Veuillez ajouter un [délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) d'au moins deux jours du calendrier entre le moment où l'utilisateur accède au canvas et celui où il reçoit l'étape du timing intelligent.

#### Calendrier vs. Jours de 24 heures

Lorsque vous utilisez le timing intelligent après une étape de retard, la date de réception/distribution peut varier en fonction de la façon dont vous calculez votre retard. Cela ne s'applique que lorsque votre délai est réglé sur **Après une durée**, car il existe une différence entre le mode de calcul des "jours" et des "jours calendaires".

- **Jours :** 1 jour correspond à 24 heures, calculées à partir du moment où l'utilisateur entre dans l'étape Délai.
- **Jours calendaires :** 1 jour correspond à la période qui s'écoule entre le moment où l'utilisateur entre dans l'étape Délai et minuit dans son fuseau horaire. Ceci signifie qu’un jour civil peut comporter seulement quelques minutes.

Lorsque vous utilisez le timing intelligent, nous vous recommandons d'utiliser des jours du calendrier pour les délais plutôt que des jours de 24 heures. En effet, avec les jours du calendrier, le message sera envoyé le dernier jour du délai, au moment le plus opportun. Avec une journée de 24 heures, il est possible que le moment optimal pour l'utilisateur soit avant qu'il n'entre dans l'étape, ce qui signifie qu'un jour supplémentaire sera ajouté à son retard.

Par exemple, imaginons que le moment optimal de Luka est à 14 h. Il entre dans l’étape de délai à 14 h 01 le 1er mars et le délai est défini sur 2 jours.

- Le premier jour s’achève le 2 mars à 14 h 01
- Le deuxième jour s’achève le 3 mars à 14 h 01

Cependant, le timing intelligent est défini pour livrer à 14 h, heure qui est déjà passée. Luka ne recevra donc pas le message avant le jour suivant : 4 mars à 14 h 00.

![Graphique illustrant la différence entre les jours et les jours du calendrier, où si l'heure optimale d'un utilisateur est 14 h, mais qu'il entre dans l'étape de délai à 14 h 01, et que le délai est fixé à 2 jours. Days transmet le message 3 jours plus tard, car l'utilisateur a saisi l'étape après le délai optimal, tandis que le calendrier transmet le message 2 jours plus tard, le dernier jour du délai.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Restrictions

- Les messages in-app et les webhooks sont transmis immédiatement et ne sont pas envoyés à des moments optimaux.
- Le timing intelligent n’est pas disponible pour les campagnes par événement ou déclenchées par API.
- Le timing intelligent ne devrait pas être utilisé dans les scénarios suivants :
    - **Limite de débit :** Si une limitation du taux et un timing intelligent sont utilisés, il n’y a aucune garantie quant à la date à laquelle le message sera livré. Les campagnes récurrentes quotidiennes avec Timing Intelligent ne prennent pas en charge avec précision un plafond total d’envoi de messages.
    - **Campagnes de réchauffement d'adresses IP :** Certains comportements de timing intelligent peuvent causer des problèmes pour atteindre les volumes journaliers nécessaires lorsque vous réchauffez pour la première fois vos adresses IP. La raison en est que le timing intelligent évalue deux fois les segments : une fois quand la campagne ou le Canvas est créé et une fois avant de l’envoyer aux utilisateurs pour vérifier s’ils devraient toujours être dans ce segment. Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.

## Résolution des problèmes

### Graphique de prévisualisation affichant peu d’utilisateurs disposant de moments optimaux

Si aucun événement pertinent n'est disponible pour un utilisateur (par exemple, les nouveaux utilisateurs peu ou pas engagés), Braze utilise le paramètre de secours configuré, soit votre heure de secours personnalisée, soit l'heure la plus populaire pour utiliser l'application parmi tous les utilisateurs.

### Impact du fuseau horaire sur la réception/distribution du timing intelligent

La fonctionnalité timing intelligent s'appuie sur le fuseau horaire local spécifié par chaque utilisateur. Par conséquent, la date et l'heure de réception/distribution prévues peuvent varier d'un utilisateur à l'autre.

Si les utilisateurs ne reçoivent pas les messages comme prévu, veuillez vérifier que le champ du fuseau horaire dans leur profil utilisateur est correctement renseigné. Si le champ du fuseau horaire est vide, l'utilisateur peut recevoir des messages correspondant au fuseau horaire de l'entreprise plutôt qu'à son heure locale.

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

#### Quels sont les calculs de repli s'il n'y a pas d'événements pertinents ?

Si aucun événement pertinent n'est disponible pour un utilisateur, le timing intelligent utilise le paramètre de repli configuré dans vos paramètres de message, soit une heure de repli personnalisée, soit l'heure la plus populaire pour utiliser l'application parmi tous les utilisateurs. 

### Campagnes

#### Combien de temps à l’avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ?

Braze calcule le moment optimal à minuit, heure des Samoa, un des premiers fuseaux horaires du monde. Un seul jour couvre environ 48 heures. Par exemple, une personne dont le temps optimal est 12 h 01 qui vit en Australie a déjà dépassé cette heure optimale et il est donc « trop tard » pour leur envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l'avance pour réussir à livrer toutes les personnes qui utilisent votre application dans le monde.

#### Pourquoi ma campagne de timing intelligent affiche-t-elle aucun ou peu d’envois ?

Si aucun événement d'engagement pertinent n'est détecté pour un utilisateur (par exemple, les nouveaux utilisateurs qui cliquent ou ouvrent rarement ou jamais), le timing intelligent utilise le paramètre de secours configuré, soit votre heure de secours personnalisée, soit l'heure la plus populaire pour utiliser l'application parmi tous les utilisateurs.

#### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ?

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous tirez parti des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes à timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante pour deux jours au lieu d'un. 

### Fonctionnalité

#### Quand est-ce que Braze vérifie les critères d’éligibilité pour les segments ou les filtres d’audience ?

Braze effectue deux vérifications lorsqu’une campagne est lancée :

1. **Vérification initiale :** A minuit dans le premier fuseau horaire le jour de l'envoi.
2. **Vérification de l'heure planifiée :** Juste avant l'envoi, à l'heure de la sélection intelligente choisie par l'utilisateur.

Soyez prudent lorsque vous filtrez sur la base d'autres envois de campagne afin d'éviter de cibler des segments inéligibles. Par exemple, si vous envoyez deux campagnes le même jour à des heures différentes et que vous ajoutez un filtre qui n'autorise les utilisateurs à recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. En effet, personne n'était éligible lorsque la campagne a été créée et que les segments ont été formés.

#### Puis-je utiliser des heures calmes dans ma campagne de timing intelligent ?

Les heures calmes peuvent être utilisées dans le cadre d'une campagne utilisant le timing intelligent. L'algorithme de timing intelligent évitera les heures calmes afin d'envoyer le message à tous les utilisateurs éligibles. Cela dit, nous vous recommandons de désactiver les heures calmes, à moins qu'il n'y ait des implications en termes de politique, de conformité ou d'autres implications légales quant au moment où les messages peuvent ou ne peuvent pas être envoyés.

#### Que se passe-t-il si le moment optimal pour un utilisateur se situe pendant les heures calmes ? 

Si l'heure optimale déterminée tombe pendant les heures calmes, Braze trouve le bord le plus proche des heures calmes et planifie le message pour la prochaine heure autorisée avant ou après les heures calmes. Le message est mis en file d'attente pour être envoyé à la limite la plus proche des heures calmes par rapport à l'heure optimale.

#### Puis-je utiliser un timing intelligent et une limitation du taux ?

La limite de débit peut être utilisée dans le cadre d'une campagne utilisant le timing intelligent. Cependant, la nature même de la limitation du débit implique que certains utilisateurs peuvent recevoir leur message à un moment moins qu'optimal, en particulier si un nombre important d'utilisateurs par rapport à la taille de la limite de débit sont planifiés à l'heure de repli parce qu'ils n'ont pas d'événements pertinents. 

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
