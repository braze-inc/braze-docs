---
nav_title: Plafond et plafonnement de fréquence
article_title: Plafond et plafonnement de fréquence
page_order: 6
tool: Campagnes
page_type: Référence
description: "Cet article de référence traite du concept de limitation de taux et de plafonnement de fréquence, et de la manière dont vous pouvez exercer une pression de commercialisation pour améliorer l'expérience utilisateur."
---

# Limitation de fréquence et plafonnement de fréquence

> Cet article de référence traite du concept de limitation de taux et de plafonnement de fréquence, et de la manière dont vous pouvez appliquer cette pression de commercialisation pour améliorer l'expérience des utilisateurs. <br> <br> Nous voulons tous que nos utilisateurs aient la meilleure expérience possible, avec limitation de débit et plafonnement de fréquence, vous pouvez vous assurer que vos utilisateurs reçoivent le message dont ils ont besoin et qu'aucun de ceux qu'ils n'ont pas.

## Limitation de taux

Braze vous permet de contrôler la pression de marketing en mettant en œuvre deux types de limitation de taux différents pour vos campagnes. La première est de fournir la meilleure expérience pour l'utilisateur final, tandis que la seconde prend en considération la bande passante de vos serveurs.

### Limitation de débit centrée sur l'utilisateur

Au fur et à mesure que vous créez plus de segments, il y aura des cas où l'appartenance de ces segments se chevauchera. Si vous envoyez des campagnes à ces segments, vous voulez être sûr que vous ne envoyez pas trop souvent de messages à vos utilisateurs. Si un utilisateur reçoit trop de messages dans un court laps de temps, ils se sentiront trop encombrés et désactiveront les notifications push ou désinstalleront votre application.

#### Filtres de segment pertinents

Braze fournit les filtres suivants afin de vous aider à limiter la vitesse à laquelle vos utilisateurs reçoivent des messages :

- Dernier engagement avec le message
- Dernier message reçu
- Dernière campagne de push reçue
- Dernier email reçu
- Dernier SMS reçu
- Dernier fil d'actualité consulté

#### Filtres d'implémentation

Considérez le segment d'exemple suivant :

!\[Exemple de limite de tarification\]\[1\]

Il s'agit d'un segment standard de réengagement. Si vous avez d'autres segments plus ciblés recevant des notifications récemment, il se peut que vous ne vouliez pas que vos utilisateurs soient ciblés par des campagnes plus génériques dirigées vers ce segment. Ajout du filtre "Dernier envoi reçu" à ce segment, l'utilisateur a veillé à ce que s'il a reçu une autre notification dans les dernières 24 heures, ils vont glisser de ce segment pour les prochaines 24 heures. S'ils satisfont toujours aux autres critères du segment 24 heures plus tard et n'ont plus reçu de notifications, ils glisseront dans le segment.

L'ajout de ce filtre à tous les segments ciblés par campagnes ferait en sorte que vos utilisateurs reçoivent un maximum de push toutes les 24 heures. Vous pourriez alors prioriser votre messagerie en vous assurant que vos messages les plus importants sont envoyés avant les messages moins importants.

#### Définition d'un plafond maximum d'utilisateur

De plus, dans la section « Utilisateurs cibles » de votre composition de campagne, vous pouvez limiter le nombre total d'utilisateurs qui recevront votre message. Cette fonction sert de vérification indépendante des filtres de votre campagne, vous permettant de segmenter librement les utilisateurs sans avoir à vous soucier du spamming.

!\[Exemple de limite totale\]\[2\]

En sélectionnant la limite maximale d'utilisateur, vous pouvez limiter la fréquence à laquelle vos utilisateurs reçoivent des notifications par canal ou globalement, pour tous les types de messages.

#### Définir une limite maximale pour l'impression

Pour les messages intégrés à l'application, vous pouvez contrôler la pression de marketing en définissant un nombre maximum d'impressions qui seront affichées à votre base d'utilisateurs, après quoi Braze n'enverra pas plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n'est pas exact. Les nouvelles règles de messages intégrés sont envoyées à une application au démarrage de la session, ce qui signifie que Braze peut envoyer un message dans l'application à l'utilisateur avant que le cap ne soit atteint, mais au moment où l'utilisateur déclenche le message, la limite a été touchée. Dans ce cas, l'appareil affichera toujours le message.

Par exemple, disons que vous avez un jeu avec un message dans l'application qui se déclenche lorsqu'un utilisateur bat un niveau, et vous la coiffez à 100 impressions. Il y a eu 99 impressions jusqu'à présent. Alice et Bob ouvrent le jeu et Braze dit à leurs appareils qu'ils sont éligibles à recevoir le message quand ils ont battu un niveau. Alice bat un niveau d'abord et reçoit le message. Bob bat le niveau suivant, mais puisque son appareil n'a pas communiqué avec les serveurs de Braze depuis le début de sa session, son appareil ne sait pas que le message a atteint son plafond, et il recevra également le message. Cependant, une fois qu'une limite d'impressions a été touchée, la prochaine fois qu'un appareil demandera la liste des messages admissibles dans l'application. ce message ne sera pas envoyé vers le bas et sera supprimé de cet appareil.

### Limitation de vitesse de livraison

Si vous prévoyez de grandes campagnes entraînant une augmentation de l'activité de l'utilisateur et surchargeant vos serveurs, vous pouvez spécifier une limite de taux par minute pour l'envoi de messages. En ciblant les utilisateurs lors de la création de campagne, vous pouvez accéder aux Options Avancées pour sélectionner une limite de taux (en différents incréments allant de 50 à 500K messages par minute). Notez que les campagnes sans limites de taux peuvent dépasser ces limites de livraison. Sachez toutefois que les messages seront annulés s'ils sont retardés de 72 heures ou plus en raison d'une limite de taux faible. L'utilisateur qui a créé la campagne recevra des alertes dans le tableau de bord et par e-mail si la limite de taux est trop basse.

!\[Exemple de limite de taux par minute\]\[3\]

Par exemple, si vous essayez d'envoyer 75K messages avec une limite de 10K par minute, la livraison sera étalée sur 8 minutes. Votre campagne livrera 10k pour chacune des 7 premières minutes et 5K au cours de la dernière minute. Veillez toutefois à retarder les messages temporaires avec cette forme de limitation de taux. Si le segment contient 30M d'utilisateurs mais que nous définissons la limite de taux à 10K par minute, une grande partie de la base d'utilisateurs ne recevra pas le message avant le lendemain.

{% alert important %}
Lorsque vous envoyez une campagne multicanal avec une limite de vitesse, chaque canal est envoyé indépendamment des autres. L'effet est que les utilisateurs peuvent recevoir les différents canaux à des moments différents, et il n'est pas prévisible quel canal ils obtiendront en premier. Par exemple, si vous envoyez une campagne contenant un e-mail et une notification push, vous pouvez avoir 10K utilisateurs avec des jetons de push valides mais 50K utilisateurs avec des adresses e-mail valides. Si vous définissez la campagne pour envoyer 100 messages par minute (une limite de taux lente pour la taille de la campagne), un utilisateur pourrait recevoir la notification push lors du premier lot d'envoi et le dernier envoi par courriel, presque 9 heures plus tard.
{% endalert %}

#### Tentatives de limitation de taux et de contenu connecté

Lorsque la fonctionnalité [Réessayer de contenu connecté][19] est activée, Braze réessaiera les échecs d'appel tout en respectant la limite de taux que vous avez définie pour chaque renvoyé. Réfléchissons à nouveau aux messages de 75 Ko avec une limite de 10 Ko par minute. Dans la première minute, l'appel échoue ou est lent et n'envoie que des messages de 4K.

Au lieu d'essayer de rattraper le retard et d'envoyer les 4K restants dans la seconde minute ou de l'ajouter au 10K il est déjà configuré pour envoyer, Braze va déplacer ces 6K messages échoués vers le "retour de la file d'attente" et ajouter une minute supplémentaire, si nécessaire, au total les minutes qu'il faudrait pour envoyer votre message.

| Minute | Pas d'échec | 6K d'échec dans la minute 1 |
| ------ | ----------- | --------------------------- |
| 1      | 10Ko        | 4K                          |
| 2      | 10Ko        | 10Ko                        |
| 3      | 10Ko        | 10Ko                        |
| 4      | 10Ko        | 10Ko                        |
| 5      | 10Ko        | 10Ko                        |
| 6      | 10Ko        | 10Ko                        |
| 7      | 10Ko        | 10Ko                        |
| 8      | 5Ko         | 10Ko                        |
| 9      | 0K          | 6K                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Campagnes multi-canaux

Gardez à l'esprit que la limite de taux à la minute est ajustée selon la campagne. Si plusieurs canaux sont utilisés dans le cadre d'une campagne, la limite de tarifs s'appliquera à chacun de ces canaux. Si votre campagne utilise des bannières e-mail et in-app avec une limite de 10K de taux par minute, nous enverrons 20K messages au total chaque minute (10K email, 10K push).

#### Campagnes Push Multi-Plateforme

Pour les campagnes de push livrées sur plusieurs plates-formes, la limite de taux sélectionnée sera distribuée équitablement entre les plates-formes. Une campagne de poussée utilisant Android, iOS et Windows avec une limite de fréquence de 10K par minute distribuera également les 10K messages sur les 3 plateformes.

## Plafond de fréquence

Au fur et à mesure que votre base d'utilisateurs continue de croître et que votre messagerie évolue pour inclure le cycle de vie, déclenché, transactionnel, et les campagnes de conversion, il est important d'éviter que vos notifications n'apparaissent comme des spammeurs ou comme des perturbateurs. En accordant un plus grand contrôle sur l’expérience de vos utilisateurs, le plafonnement des fréquences vous permet de créer les campagnes que vous désirez sans submerger votre public.

### Aperçu des fonctionnalités {#freq-cap-feat-over}

Le plafonnement de fréquence est appliqué au niveau d'envoi de la campagne ou de l'étape Canvas et peut être configuré pour chaque groupe d'applications en sélectionnant __Paramètres globaux des messages__ dans l'onglet **Engagement**. À partir de là, vous pouvez choisir ce qui suit :

- Quel canal de messagerie vous souhaitez capturer : push, email, SMS, webhook, ou l'un de ces quatre.
- Combien de fois chaque utilisateur doit recevoir une campagne ou Canvas pas envoie d'un canal dans un certain laps de temps.
- Combien de fois chaque utilisateur doit recevoir une campagne ou l'étape Canvas envoie par [tag](#frequency-capping-by-tag) dans un certain laps de temps.

Cette période de temps peut être mesurée en minutes, jours, semaines (7 jours) ou mois, avec une durée maximale de 30 jours.

Chaque ligne de fréquences sera connectée à l'aide de l'opérateur `ET` , et vous pouvez ajouter jusqu'à 10 règles par groupe d'applications. De plus, vous pouvez inclure plusieurs majuscules pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs à un maximum d'une poussée par jour et pas plus de trois poussées par semaine.

!\[Cappage Fréquence\]\[14\]

### Règles de livraison

Il peut y avoir des campagnes, comme des messages transactionnels, que vous voulez toujours atteindre l'utilisateur, même s'ils ont déjà atteint leur limite de fréquence. Par exemple, une application de livraison peut vouloir envoyer un e-mail ou un push quand un article est distribué, quel que soit le nombre de campagnes reçues par l'utilisateur.

Si vous voulez qu'une campagne particulière remplace les règles de plafonnement de fréquence, vous pouvez configurer cela dans le tableau de bord Braze en planifiant la livraison de cette campagne en basculant **le plafonnement de fréquence** sur **OFF**. Après cela, on vous demandera si vous voulez toujours que cette campagne compte dans votre limite de fréquence. Les messages qui comptent pour le plafonnement des fréquences sont inclus dans les calculs du filtre du canal intelligent. Lors de l'envoi de [campagnes API][15], qui sont souvent transactionnelles, vous aurez la possibilité de spécifier qu'une campagne devrait ignorer les règles de plafonnement de fréquence [dans la requête API][16] en définissant `override_messaging_limits` à `true`.

Par défaut, les nouvelles campagnes et les canevas qui n'obéissent pas aux fréquences ne compteront pas non plus pour eux. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement change le comportement par défaut lorsque vous désactivez le plafonnement de fréquence pour une campagne ou Canvas. Les changements sont compatibles avec les versions antérieures et n'affectent pas les messages qui sont actuellement en production.
{% endalert %}

!\[Mise à jour du plafonnement des fréquences\]\[18\]

Différents canaux dans une campagne multicanale compteront individuellement la limite de fréquence. Par exemple, si vous créez une campagne multi-canal avec push et email et que vous avez configuré un plafonnement de fréquence pour ces deux canaux, alors le push comptera pour une campagne de push et le message électronique comptera pour une campagne de message électronique. La campagne comptera également pour une « campagne de tout type ». Si les utilisateurs sont plafonnés à une campagne de push et une campagne email par jour et qu'un utilisateur reçoit cette campagne multi-canaux, alors ils ne seront plus éligibles pour le reste de la journée (sauf si une campagne ignore les règles de plafonnement des fréquences).

Les messages intégrés et les cartes de contenu ne sont pas comptés comme des majuscules sur les campagnes ou pas de Canvas de quelque type que ce soit.

{% alert important %}
Le plafonnement de la fréquence globale est programmé en fonction du fuseau horaire de l'utilisateur et est calculé par jour du calendrier, et non par période de 24 heures. Par exemple, si vous avez mis en place une règle de plafonnement des fréquences d'envoi pas plus d'une campagne par jour, un utilisateur peut recevoir un message à 23h dans son fuseau horaire local et il pourrait recevoir un autre message une heure plus tard.
{% endalert %}

#### Exemples

{% tabs %}
{% tab Example 1 %}

Disons que vous définissez une règle de plafonnement des fréquences qui demande à votre utilisateur de recevoir pas plus de trois campagnes de notification push ou Canvas par semaine de toutes les étapes de la campagne ou de Canvas pas.

Si votre utilisateur est censé recevoir trois notifications push, deux messages dans l'application. et une carte de contenu cette semaine, ils recevront tous ces messages.

{% endtab %}
{% tab Example 2 %}

Utilisation des règles suivantes de plafonnement des fréquences:

![règle]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Et le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne, `Campagne ABC` trois fois en une semaine.
- Cet utilisateur déclenche `ABC Campagne` une fois le lundi, une fois le mercredi, et une fois le jeudi.

__Ensuite, le comportement attendu est que :__

- Cet utilisateur recevra la campagne qui lui sera envoyée le lundi et le mercredi.
- Cet utilisateur ne recevra pas la troisième campagne envoyée jeudi car l'utilisateur a déjà reçu deux envois de campagne de push cette semaine.

{% endtab %}
{% endtabs %}

### Fréquence plafonnée par tag

[Les règles de plafonnement de fréquence](#updated-frequency-capping-rules) peuvent être appliquées à des groupes d'applications en utilisant des balises spécifiques que vous avez appliquées à vos Campagnes/Canvases, vous permettant essentiellement de baser votre plafonnement de fréquence sur des groupes nommés sur mesure.

Vous pouvez combiner le plafonnement de fréquence régulier avec le plafonnement de fréquence par tags, comme indiqué ci-dessous.

!\[Règle de plafonnement de fréquence\]\[12\]

Les règles ci-dessus demandent aux utilisateurs de recevoir:

1. Pas plus de trois campagnes de notification push ou pas de Canvas par semaine à partir de toutes les étapes de la campagne et de Canvas . <br>**ET**
2. Pas plus de deux étapes de la campagne de notification push ou de Canvas par semaine avec le tag `promotion`.

Résultat: vos utilisateurs ne recevront pas plus de trois campagnes envoyées par semaine sur toutes les campagnes et toutes les étapes de Canvas et pas plus de deux campagnes de notification push ou pas de Canvas avec l'étiquette `promotion`.

{% alert important %}
Les toiles sont taguées au niveau de la Toile plutôt que de taguer par Step. Ainsi, chaque Étape de Canvas héritera de toutes les balises de niveau Canvas .
{% endalert %}

#### Règles en conflit

En cas de conflit de règles, la règle de limitation de fréquence la plus restrictive et la plus applicable sera appliquée à vos utilisateurs.

!\[global\]\[11\]

Dans cet exemple, votre utilisateur ne recevra pas plus d'une campagne de notification push ou pas de Canvas avec le tag "promotionnel" dans une semaine donnée. parce que vous avez spécifié que les utilisateurs ne devraient pas recevoir plus d'une campagne de notification push ou Canvas pas de toutes les campagnes et étapes de Canvas . En d'autres termes, la règle de fréquence applicable la plus restrictive est la règle qui sera appliquée à un utilisateur donné.

#### Nombre d'étiquettes

Les règles de fréquence par balises calculent au moment où un message est envoyé. Cela signifie que le plafonnement de fréquence par tag ne compte que les balises qui sont actuellement sur les campagnes ou les Canvases qu'un utilisateur a reçus dans le passé. Il ne compte pas les balises qui étaient sur les campagnes ou les Canvases pendant le temps où elles ont été envoyées, mais ont depuis été enlevées. Il comptera si un tag est ajouté plus tard à un message qu'un utilisateur a reçu dans le passé, mais avant que le message taggé le plus récent soit envoyé.

##### Exemple

Considérez les campagnes suivantes et les règles de fréquence par balises :

__Campagnes :__

- __Campagne A__ est une campagne de push marquée comme `promotionnelle`. Il est prévu d'envoyer à 9h00 le lundi.
- __Campagne B__ est une campagne de push marquée comme `promotionnelle`. Il est prévu d'envoyer à 9 h le mercredi.

__Capping de fréquence par règle d'étiquette :__

- Votre utilisateur ne devrait pas recevoir plus d'une campagne de notification push par semaine avec le tag `promotion`.<br><br>

| Action                                                                                                                                                                                                               | Résultat                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| La balise `promotionnelle` est retirée de la __Campagne A__ _après_ que votre utilisateur a reçu le message, mais _avant_ __La campagne B a été envoyée.__                                                           | Votre utilisateur recevra __Campagne B__.           |
| Le tag `promotionnel` est supprimé par erreur de la __Campagne A__ après que votre utilisateur ait reçu le message. <br> Le tag est ramené à __Campagne A__ mardi avant que la __Campagne B__ ne soit envoyée. | Votre utilisateur ne recevra pas la __Campagne B__. |
{: .reset-td-br-1 .reset-td-br-2}

#### Envoi à grandes échelles

Si vous envoyez plus de cent (100) messages par canal à partir de campagnes ou pas de Canvas avec un plafonnement de fréquence activé à un utilisateur spécifique au cours de la durée de votre plafonnement de fréquence par règle d'étiquette (par exemple, plus d'une semaine), la règle de plafonnement par balise peut ne pas toujours être appliquée correctement.

Par exemple, si votre règle de limitation de fréquence par balise est:

> Pas plus de deux campagnes e-mail ou pas de Canvas avec le tag `Promotional` à un utilisateur chaque semaine.

Et vous envoyez à l'utilisateur plus de cent (100) courriels provenant de campagnes et de Canvas Steps avec des plafonds de fréquence activés au cours d'une semaine, plus de deux e-mails peuvent être envoyés à l'utilisateur.

Étant donné que 100 messages par canal sont plus nombreux que ce que la plupart des marques envoient à leurs utilisateurs, il est peu probable que vous soyez affecté par cette limitation. Pour éviter cette limitation, vous pouvez définir un plafond pour le nombre maximum d'e-mails que vous souhaitez recevoir vos utilisateurs au cours d'une semaine.

Par exemple, vous pouvez configurer la règle suivante :

> Pas plus de trois campagnes de courriel ou pas de Canvas par semaine à partir de toutes les étapes de la campagne et de Canvas Steps.

Cette règle assurera qu'aucun utilisateur ne recevra plus de 100 e-mails par semaine parce que, tout au plus, les utilisateurs recevront 3 courriels par semaine de campagnes ou pas de Canvas dont le plafonnement de fréquence est activé.
[11]: {% image_buster /assets/img/global_rules.png %} "règles globales" [12]: {% image_buster /assets/img/tag_rule_fnfn. ng %} "rules" [13]: {% image_buster /assets/img/standard_rules_fnfn.png %} "rules standard" [1]: {% image_buster /assets/img_archive/rate_limit_daily. ng %} [2]: {% image_buster /assets/img_archive/total_limit.png %} [3]: {% image_buster /assets/img_archive/per_minute_rate_limit. ng %} [14]: {% image_buster /assets/img_archive/rate_limitting_overview_2.png %} [18]: {% image_buster /assets/img_archive/frequencycappingupdate.png %}

[15]: {{site.baseurl}}/developer_guide/rest_api/messaging/#messaging
[16]: {{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/
