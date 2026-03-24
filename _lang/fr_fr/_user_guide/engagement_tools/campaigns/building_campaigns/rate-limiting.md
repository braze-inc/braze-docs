---
nav_title: Limitation du taux et limite de fréquence
article_title: Limitation du taux et limite de fréquence
page_order: 6
tool: Campaigns
page_type: reference
description: "Le présent article de référence aborde le concept de limitation du taux et la limite de fréquence dans les campagnes ainsi que la manière dont vous pouvez appliquer une pression marketing pour améliorer l’expérience utilisateur."

---

# Limitation du taux et limite de fréquence

> La limite de débit et la limite de fréquence peuvent être utilisées conjointement pour garantir que vos utilisateurs reçoivent les messages dont ils ont besoin.

## À propos de la limite de débit

Braze vous permet de contrôler la pression marketing par taux limitant vos campagnes, ce qui régule la quantité de trafic sortant de votre plate-forme. Vous pouvez mettre en œuvre deux types de limites de débit pour vos campagnes : 

1. [Limite de débit centrée sur l'utilisateur :](#user-centric-rate-limiting) Nous nous efforçons d'offrir la meilleure expérience possible à l'utilisateur.
2. [Limite de débit pour la vitesse de réception/distribution :](#delivery-speed-rate-limiting) Tient compte de la bande passante de vos serveurs.

Braze essaiera de répartir uniformément les envois de messages tout au long de la minute, mais ne peut le garantir. Par exemple, si vous avez une campagne avec une limite de débit de 5 000 messages par minute, nous essaierons de répartir les 5 000 demandes de manière égale tout au long de la minute (environ 84 messages par seconde), mais il peut y avoir une certaine variation dans le débit par seconde.

### Limite de débit centrée sur l'utilisateur

À mesure que vous créez plus de segments, il y aura des cas où l’appartenance à ces segments se chevauche. Si vous envoyez des campagnes à ces segments, vous devez être sûr que vous n’envoyez pas des messages trop souvent à vos utilisateurs. Si un utilisateur reçoit trop de messages sur une courte période, il va se sentir surchargé et désactiver les notifications push ou désinstaller votre application.

#### Filtres de segment pertinents

Braze propose les filtres suivants pour vous aider à limiter la fréquence à laquelle vos utilisateurs reçoivent des messages :

- Dernière interaction avec un message
- Dernier message reçu
- Dernière notification push reçue
- Dernier e-mail reçu
- Dernier SMS reçu

#### Implémenter des filtres

Supposons que nous ayons créé un segment intitulé « Filtre de reciblage Vitrine » avec un filtre « Dernière utilisation de l'application il y a plus de 7 jours » pour cibler les utilisateurs. Il s’agit d’un segment de ré-engagement standard.

Si vous avez récemment reçu des notifications concernant d'autres segments plus ciblés, il est possible que vous ne souhaitiez pas que vos utilisateurs soient ciblés par des campagnes plus génériques destinées à ce segment. En ajoutant le filtre « Dernière notification reçue » à ce segment, l'utilisateur s'assure que s'il a reçu une autre notification au cours des dernières 24 heures, il sera exclu de ce segment pendant les prochaines 24 heures. Si, 24 heures plus tard, ils répondent toujours aux autres critères du segment et n'ont reçu aucune autre notification, ils réintégreront le segment.

![Un segment intitulé « Vitrine des filtres de reciblage » avec le groupe de filtres « Dernière utilisation de l'application il y a plus de 7 jours ».]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"} 

En ajoutant ce filtre à tous les segments ciblés par les campagnes, vos utilisateurs ne peuvent recevoir qu’une notification push toutes les 24 heures au maximum. Vous pouvez ensuite prioriser votre messagerie en vous assurant que vos messages les plus importants sont envoyés avant les moins importants.

#### Fixer un plafond d'utilisateurs

Dans l'étape **Audiences cibles** du compositeur de votre campagne, vous pouvez également limiter le nombre total d'utilisateurs qui recevront votre message. Cela permet d'effectuer une vérification indépendante des filtres de votre campagne.

![Résumé de l'audience avec une case à cocher sélectionnée pour limiter le nombre de personnes qui reçoivent la campagne.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"} 

En sélectionnant la limite maximale d'utilisateurs, vous pouvez limiter le volume de messages envoyés par canal de communication ou globalement pour tous les types de messages.

{% alert note %}
Le plafond maximal limite le nombre d'utilisateurs affectés, et non le nombre de messages envoyés avec succès. Étant donné que les messages interrompus sont pris en compte dans ce plafond, le nombre réel de messages envoyés peut être inférieur à la limite configurée. Par exemple, si vous définissez une limite de 10 000 et que 2 000 messages sont interrompus en raison de la logique Liquid ou d'autres conditions, seuls 8 000 messages seront envoyés.
{% endalert %}

##### Nombre maximum d'utilisateurs avec optimisations

Si vous utilisez une optimisation telle que la variante gagnante ou la variante de personnalisation, la campagne comprendra deux envois : l'expérience initiale et l'envoi final. 

Pour implémenter un plafond d'utilisateurs dans ce scénario, sélectionnez **Limiter le nombre de personnes qui recevront cette campagne**, puis sélectionnez **Au total, cette campagne doit** et entrez une limite d'audience. Votre audience sera répartie selon les pourcentages indiqués dans le panneau **test A/B**. 

Si vous sélectionnez **Chaque fois que la campagne est planifiée**, ces deux phases seront limitées séparément au nombre défini. Ce n’est généralement pas souhaitable.

#### Définition d'un plafond d'impressions pour les campagnes

Pour les messages in-app, vous pouvez contrôler la pression marketing en définissant un nombre maximum d’impressions qui seront affichées à votre base d’utilisateurs, après quoi Braze n’enverra plus de messages à vos utilisateurs. Cependant, il est important de noter que ce plafond n’est pas exact. 

Les règles relatives aux messages in-app sont transmises à l'application au début de la session, ce qui signifie que Braze peut envoyer un message à l'utilisateur avant que la limite ne soit atteinte, mais au moment où l'utilisateur déclenche le message, la limite est déjà atteinte. Dans cette situation, l’appareil affichera quand même le message.

Supposons par exemple que vous ayez un jeu avec un message in-app qui se déclenche quand un utilisateur bat un niveau et que vous l’ayez plafonné à 100 impressions. Jusqu’à présent, il y a eu 99 impressions. Alice et Bob lancent tous deux le jeu, et Braze informe leurs appareils qu'ils sont éligibles pour recevoir le message lorsqu'ils terminent un niveau. Alice bat un niveau en premier et reçoit le message. Bob réussit ensuite le niveau, mais comme son appareil n'a pas communiqué avec les serveurs Braze depuis le début de sa session, il n'est pas informé que le message a atteint sa limite et le reçoit également. Toutefois, lorsqu'un plafond d'impressions a été atteint, la prochaine fois qu'un appareil demande la liste des messages in-app éligibles, le système n'envoie pas ce message et le supprime de cet appareil.

### Limite de débit et test A/B

Lorsque vous utilisez la limite de débit avec un test A/B, la limite de débit n'est pas appliquée au groupe de contrôle de la même manière qu'au groupe de test, ce qui constitue une source potentielle de biais temporel. Afin d'éviter ce biais, veuillez utiliser des fenêtres de conversion appropriées.

### Limiter le taux de vitesse de livraison

Si vous prévoyez que des campagnes de grande envergure entraîneront une augmentation de l'activité des utilisateurs et une surcharge de vos serveurs, vous pouvez définir une limite de débit par minute pour l'envoi de messages. Ainsi, Braze n'enverra pas plus que le nombre de messages défini dans votre paramètre de limite de débit par minute.

Lorsque vous effectuez le ciblage d'utilisateurs lors de la création d'une campagne, vous pouvez accéder à «** Audiences cibles** » (pour les campagnes) ou **« Paramètres d'envoi** » (pour Canvas) afin de sélectionner une limite de débit (par incréments allant de 10 à 500 000 messages par minute).

Notez que les campagnes sans limitation du taux peuvent dépasser ces limites de livraison. Veuillez toutefois noter que les messages seront interrompus s'ils sont retardés de 72 heures ou plus en raison d'une limite de débit faible. Si la limite de débit est trop basse, le créateur de la campagne recevra des alertes dans le tableau de bord et par e-mail.

#### Exemple

Si vous essayez d'envoyer 75 000 messages avec une limite de débit de 10 000 messages par minute, la réception/distribution s'étalera sur huit minutes. Votre campagne ne pourra envoyer plus de 10 000 messages pendant chacune des sept premières minutes, et 5 000 messages pendant la dernière minute.

#### Nombre d'envois

Veuillez noter que les messages à limite de débit peuvent ne pas être envoyés de manière uniforme au cours de chaque minute. En prenant l'exemple d'une limite de débit de 10 000 messages par minute, cela signifie que Braze s'assure que pas plus de 10 000 messages ne sont envoyés par minute. Cela pourrait signifier qu'un pourcentage plus élevé des 10 000 messages est envoyé au cours de la première demi-minute par rapport à la dernière demi-minute.

La limite de débit est appliquée au début de la tentative d'envoi du message. Lorsque le temps nécessaire à l'envoi varie, le nombre d'envois effectués peut légèrement dépasser la limite de débit pendant quelques minutes. Avec le temps, le nombre d'envois par minute se stabilisera au niveau de la limite de débit.

{% alert important %}
Cette forme de limitation de débit par rapport au nombre total d'utilisateurs dans un segment permet de ne pas retarder les envois de messages sensibles au facteur temps. Par exemple, si le segment contient 30 millions d'utilisateurs mais que nous fixons la limite de débit à 10 000 par minute, une grande partie de votre base d'utilisateurs ne recevra le message que le lendemain.
{% endalert %}

#### Campagnes multicanales et canevas

Lorsque vous définissez une limite de débit pour la réception/distribution d’une campagne multicanal ou de Canvas, vous avez la possibilité de choisir entre une limite commune ou une limite par canal.

Lorsqu'une campagne multicanal ou Canvas utilise une limite de débit partagée, cela signifie que le nombre total de messages envoyés par minute depuis la campagne ou Canvas ne dépasse pas la limite de débit. Par exemple, si votre canvas a une limite de débit de 500 000 par minute et contient des étapes d'e-mails et de SMS, Braze envoie un total de 500 000 messages par minute par e-mail et SMS.

![L'option permettant de limiter la fréquence d'envoi de la campagne, sélectionnée avec 500 000 messages par minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"} 

Lorsqu'une campagne multicanal ou canvas utilise une limitation de débit basée sur les canaux, la limite de débit s'applique à chacun des canaux que vous avez sélectionnés. Par exemple, vous pouvez configurer votre campagne ou votre Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 SMS par minute pour l'ensemble de la campagne ou du Canvas.

![Limites de débit distinctes pour deux canaux, webhook et SMS/MMS/RCS, avec respectivement 5 000 et 2 500 messages par minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Notifications push

Pour les campagnes ou les canvases utilisant des plateformes push (telles qu'Android, iOS, Web Push ou Kindle), il est possible de sélectionner **les notifications push** afin d'appliquer une limite de débit commune à toutes les plateformes push de votre campagne ou canvas.

![Le menu déroulant des canaux avec les options pour les plateformes push et les notifications push.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"} 

{% alert note %}
Si vous sélectionnez une limite pour les notifications push, il n'est pas possible de définir des limites de débit individuelles pour chaque canal push. De même, si vous sélectionnez des limites pour des canaux push individuels, il n'est pas possible de définir des limites communes pour les notifications push.
{% endalert %}

{% alert important %}
**Mises à jour de l'interface de limite de débit**<br>
Braze a mis à jour l'interface de limitation du débit afin d'offrir davantage de transparence et de contrôle sur la manière dont les limites de débit s'appliquent aux campagnes multicanales et aux canevas.<br><br>

- **Campagnes et canevas existants :** Toutes les campagnes et tous les canevas existants ont fait l'objet d'une migration vers cette interface. Leur comportement en matière de réception/distribution reste inchangé. Le tableau de bord indique si la campagne utilise une logique partagée ou par canal.<br>
- **Nouvelles campagnes et canevas :** Pour toutes les nouvelles campagnes et tous les nouveaux canevas, vous pouvez basculer manuellement pour sélectionner votre logique de limite de débit préférée. Veuillez vous assurer de sélectionner le comportement de limitation du débit qui correspond à votre intention lorsque vous définissez ou mettez à jour une campagne ou une limite de débit Canvas.
{% endalert %}

##### Considérations relatives à la limite de débit

Quelques remarques à garder à l'esprit lors de la configuration des limites de débit et du comportement auquel vous devez vous attendre :

- L'envoi de SMS est soumis à une limite de débit de 50 000 messages par groupe d'abonnement. Certains fournisseurs de SMS peuvent appliquer d'autres restrictions.
- Les messages suivants ne seront pas limités ni pris en compte dans la limite de débit :
    - Envois de tests
    - Groupes initiateurs
    - Cartes de contenu configurées pour créer une « première impression » (ceci sera contrôlé par le taux d'impressions de l'application). Veuillez consulter la section [Création de]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) [cartes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences) pour plus d'informations sur les différences entre les options de création de cartes.
- Les limites de débit de réception/distribution ne sont pas prises en charge pour les éléments suivants :
    - Réponses automatiques par SMS
    - Messages garantis par un accord de niveau de service (SLA) (tels que [les e-mails transactionnels]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign))
    - in-app Messages
    - Indicateurs de fonctionnalité
    - Bannières

#### Limitation du taux et nouvelles tentatives de contenu connecté

Lorsque le [rappel de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries/) est activé, Braze relance les échecs d'appel tout en respectant la limite de débit que vous avez définie pour chaque renvoi. Prenons le cas d'un envoi de 75 000 messages avec une limite de débit de 10 000 par minute. Imaginez que dans la première minute, l'appel échoue ou est lent et n'envoie que 4 000 messages.

Au lieu d'essayer de rattraper le retard et d'envoyer les 6 000 messages restants dans la deuxième minute ou de les ajouter aux 10 000 messages déjà prêts à être envoyés, Braze déplacera ces 6 000 messages en "fin de file d'attente" et ajoutera une minute, si nécessaire, au nombre total de minutes nécessaires à l'envoi de votre message.

| Minute | Pas de défaillance | 6 000 échecs à la minute 1 |
|--------|------------|---------------------------|
| 1      | 10,000     | 4,000                     |
| 2      | 10,000     | 10,000                    |
| 3      | 10,000     | 10,000                    |
| 4      | 10,000     | 10,000                    |
| 5      | 10,000     | 10,000                    |
| 6      | 10,000     | 10,000                    |
| 7      | 10,000     | 10,000                    |
| 8      | 5,000      | 10,000                    |
| 9      | 0          | 6,000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Les requêtes de contenu connecté ne sont pas soumises à une limite de débit indépendante et suivent la limite de débit des webhooks. Cela signifie que s'il y a un appel de contenu connecté à un endpoint unique par webhook, vous devriez vous attendre à 5 000 webhooks et également à 5 000 appels de contenu connecté par minute. Notez que la mise en cache peut avoir une incidence sur ce point et réduire le nombre d'appels au contenu connecté. En outre, les tentatives peuvent augmenter le nombre d'appels au contenu connecté. Nous vous recommandons donc de vérifier que le point de terminaison du contenu connecté peut supporter une certaine fluctuation à ce niveau.

{% alert note %}
**Les limites de débit sont des restrictions de vitesse et ne définissent pas une vitesse d'envoi précise.** En règle générale, les messages sont répartis de manière uniforme au cours d'une minute donnée et, dans la grande majorité des cas, ils sont envoyés à la limite configurée ou très près de celle-ci. Ce n'est pas toujours le cas, par exemple lorsque les messages sont très volumineux (comme les e-mails contenant de nombreux blocs de contenu, étiquettes de contenu connecté ou étiquettes d'éléments de catalogue), ou lorsqu'il y a de nombreux abandons Liquid (les messages abandonnés occupent toujours un emplacement et peuvent réduire les taux d'envoi effectifs).

Dans la pratique, le débit d'envoi soutenu (messages terminés par minute) peut être inférieur à la limite de débit configurée en raison des tentatives, de la variabilité du réseau, de la latence des endpoints en aval et du lissage par minute.

Si vous constatez régulièrement un débit nettement inférieur à celui attendu, veuillez vérifier les temps de réponse du contenu connecté, les taux d'erreur (tels que `429`) et le comportement de réessai.
{% endalert %}

## À propos de la limite de fréquence

Alors que votre base d'utilisateurs continue de croître et que votre envoi de messages s'étend pour inclure des campagnes sur le cycle de vie, des campagnes déclenchées, des campagnes transactionnelles et des campagnes de conversion, il est important d'éviter que vos messages ne paraissent "spammy" ou dérangeants. En offrant un meilleur contrôle sur l’expérience de vos utilisateurs, la limite de fréquence vous permet de créer les campagnes que vous souhaitez sans surcharger votre audience.

### Aperçu de la fonction User Search {#freq-cap-feat-over}

La limite de fréquence est appliquée au niveau de l'envoi de la campagne ou du composant Canvas et peut être configurée pour chaque espace de travail à partir de **Paramètres** > **Règles de limite de fréquence**.

Par défaut, la limite de fréquence est activée lorsque de nouvelles campagnes sont créées. Vous pouvez choisir ce qui suit :

- Le canal de communication que vous souhaitez limiter : push, e-mail, SMS, webhook, WhatsApp, LINE ou tout autre canal de ce type.
- Combien de fois chaque utilisateur devrait recevoir une campagne ou un composant canvas envoyé depuis un canal au cours d'une période donnée.
- Combien de fois chaque utilisateur devrait recevoir une campagne ou un composant canvas envoyé par [étiquette](#frequency-capping-by-tag) au cours d'une période donnée.

Ce délai peut être mesuré en minutes, en jours ou en semaines (sept jours), avec une durée maximale de 30 jours.

Chaque ligne de limite de fréquence est connectée à l'aide de`AND`l'opérateur, et il est possible d'ajouter jusqu'à 10 règles par espace de travail. Vous pouvez inclure plusieurs limites pour les mêmes types de messages. Par exemple, vous pouvez plafonner les utilisateurs pour qu’ils ne dépassent pas une notification push unique par jour et trois par semaine. Veuillez noter que les messages interrompus ne sont pas pris en compte dans la limite de fréquence.

![Section relative à la limite de fréquence, comprenant des listes de campagnes et de canevas auxquels les règles s'appliquent ou ne s'appliquent pas.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"} 

#### Comportement lorsque les utilisateurs sont limités en fréquence sur une étape du canvas

Si un utilisateur Canvas est soumis à une limite de fréquence en raison des paramètres globaux de limite de fréquence, il effectuera immédiatement l'avancement vers l'étape du canvas suivante. L'utilisateur ne quittera pas le Canvas à cause de la limite de fréquence.

### Règles de livraison

Il peut y avoir des campagnes, comme les messages transactionnels, que vous voulez voir envoyées à l’utilisateur tout le temps, même s’ils ont déjà atteint leur limite de fréquence. Par exemple, une application de réception/distribution peut souhaiter envoyer un e-mail ou une notification push lorsqu'un article est livré, quel que soit le nombre de campagnes que l'utilisateur a reçues.

Si vous souhaitez qu'une campagne particulière ne tienne pas compte des règles de limitation de fréquence, vous pouvez le faire dans le tableau de bord de Braze lors de la planification de la réception/distribution de cette campagne en basculant la **limitation de fréquence** sur **OFF**. 

Ensuite, il vous sera demandé si vous souhaitez toujours que cette campagne soit prise en compte dans votre limite de fréquence. Les messages qui comptent pour la limite de fréquence sont inclus dans les calculs du filtre du canal intelligent. 

Lors de l'envoi de [campagnes API]({{site.baseurl}}/developer_guide/rest_api/messaging/#messaging), qui sont souvent transactionnelles, vous avez la possibilité de spécifier qu'une campagne doit ignorer la limite de fréquence en définissant`override_frequency_capping`  sur`true`  dans la requête API.

Par défaut, les nouvelles campagnes et les Canevas qui n'obéissent pas aux limites de fréquence ne seront pas non plus pris en compte. Ceci est configurable pour chaque campagne et Canvas.

{% alert note %}
Ce comportement modifie le comportement par défaut lorsque vous désactivez la limitation de fréquence pour une campagne ou un Canvas. Les modifications sont rétro-compatibles et n’affectent pas les messages actuellement actifs.
{% endalert %}

![Section Contrôles de réception/distribution avec la fonctionnalité limite de fréquence activée.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"} 

Les différents canaux d'une campagne multicanal sont pris en compte individuellement dans le calcul de la limite de fréquence. Par exemple, si vous créez une campagne multicanal comprenant à la fois des notifications push et des e-mails, et que vous avez défini une limite de fréquence pour ces deux canaux, les notifications push sont comptabilisées dans une campagne de notifications push, et les e-mails sont comptabilisés dans une campagne d'e-mails. La campagne est également considérée comme une « campagne de tout type ». Si les utilisateurs sont limités à une notification push et à une campagne par e-mail par jour, et qu'un utilisateur reçoit cette campagne multicanal, il ne sera plus éligible aux campagnes push ou par e-mail pour le reste de la journée (sauf si une campagne ignore la limite de fréquence).

Les messages in-app et les cartes de contenu ne sont pas pris en compte dans le calcul des plafonds des campagnes ou des composants Canvas, quels qu'ils soient.

{% alert important %}
La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.
{% endalert %}

#### Cas d'utilisation

{% tabs %}
{% tab Use case 1 %}

Supposons que vous définissiez une limite de fréquence afin que vos utilisateurs ne reçoivent pas plus de trois campagnes de notifications push ou étapes du canvas par semaine, toutes campagnes ou étapes du canvas confondues.

Si votre utilisateur est censé recevoir trois notifications push, deux messages in-app et une carte de contenu cette semaine, il recevra tous ces messages.

{% endtab %}
{% tab Use case 2 %}

Ce scénario utilise une limite de fréquence afin que les utilisateurs ne reçoivent pas plus de deux campagnes de notifications push ou étapes du canvas par semaine, toutes campagnes ou étapes du canvas confondues.

**Lorsque le scénario suivant se produit :**

- Un utilisateur déclenche la même campagne`Campaign ABC`à trois reprises au cours d'une semaine.
- Cet utilisateur déclenche `Campaign ABC` une fois le lundi, une fois le mercredi et une fois le jeudi.

![Section « Limite de fréquence » avec la règle suivante : envoyer au maximum 2 campagnes de notifications push/étapes du canvas à partir de toutes les campagnes/étapes du canvas à un utilisateur toutes les semaines.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Le comportement attendu est alors le suivant :**

- Cet utilisateur recevra les envois de la campagne déclenchés le lundi et le mercredi.
- Cet utilisateur ne recevra pas la troisième campagne envoyée jeudi parce que l’utilisateur a déjà reçu deux campagnes de notification push cette semaine-là.

{% endtab %}
{% endtabs %}

### Limite de fréquence par tag

Les [règles de limitation de fréquence](#delivery-rules) peuvent être appliquées aux espaces de travail à l'aide des tags spécifiques que vous avez appliqués à vos campagnes et à vos toiles, ce qui vous permet essentiellement de baser votre limitation de fréquence sur des groupes aux noms personnalisés.

Avec une limite de fréquence par balise, les règles peuvent être définies sur les balises principales et imbriquées, pour que Braze prenne en compte toutes les balises. Par exemple, si vous avez choisi d'utiliser la balise principale A comme limite de fréquence, nous inclurons également les informations contenues dans toutes les étiquettes imbriquées (par exemple, les étiquettes B et C) lors de la détermination de la limite.

Vous pouvez également combiner une limite de fréquence régulière avec une limite de fréquence par balises. Prenez en compte les règles suivantes :

1. Pas plus de trois campagnes de notifications push ou composants canvas par semaine, toutes campagnes et étapes du canvas confondues. <br>**ET**
2. Pas plus de deux campagnes de notifications push ou composants Canvas par semaine avec l'étiquette`promotional`.

![Section « Limite de fréquence » avec deux règles limitant le nombre de campagnes de notifications push/Canvases pouvant être envoyées à un utilisateur chaque semaine.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Par conséquent, vos utilisateurs ne recevront pas plus de trois envois de campagnes par semaine depuis toutes les campagnes et étapes de Canvas et pas plus de deux campagnes de notification push ou de composant de Canvas avec la balise `promotional`.

{% alert important %}
Les Canvas reçoivent leur balise au niveau du Canvas et pas au niveau du composant. Ainsi, chaque composant Canvas héritera de toutes les étiquettes au niveau Canvas.
{% endalert %}

#### Règles contradictoires

En cas de conflit entre les règles, la limite de fréquence la plus restrictive et applicable est appliquée à vos utilisateurs. Par exemple, imaginons que vous ayez les règles suivantes :

1. Une seule campagne de notifications push ou composant Canvas par semaine est autorisée pour l'ensemble des campagnes et composants Canvas. <br>**ET**
2. Pas plus de trois campagnes de notification push ou de composant Canvas par semaine avec la balise `promotional`.

![Section « Limite de fréquence » avec des règles contradictoires visant à limiter le nombre de campagnes de notifications push/étapes du canvas envoyées à un utilisateur chaque semaine.]({% image_buster /assets/img/global_rules.png %} "global rules")

Dans cet exemple, votre utilisateur ne recevra pas plus d’une campagne de notification push ou de composants de Canvas avec la balise « promotionnel » pour une semaine donnée, car vous avez spécifié que les utilisateurs ne doivent pas recevoir plus d’une campagne de notification push ou de composant de Canvas depuis toutes les campagnes et composants de Canvas. En d’autres termes, la règle de fréquence applicable la plus restrictive est la règle qui sera appliquée à un utilisateur donné.

#### Nombre de balises

La limite de fréquence par règles d'étiquette est calculée au moment où un message est envoyé. Cela signifie que la limite de fréquence par balise compte uniquement des balises qui sont actuellement sur les campagnes ou les Canvas qu’un utilisateur a reçu par le passé. Les étiquettes qui figuraient sur les campagnes ou les canevas au moment de leur envoi, mais qui ont depuis été supprimées, ne sont pas prises en compte. Il est important de noter qu'une étiquette peut être ajoutée ultérieurement à un message qu'un utilisateur a reçu dans le passé, mais avant l'envoi du message balisé le plus récent.

##### Cas d’utilisation

Considérez la règle de campagne et de limite de fréquence par balise suivante :

**Campagnes**:

- La **campagne A** est une campagne de push étiquetée `promotional`. Il est prévu qu'il soit envoyé lundi à 9 heures.
- La **campagne B** est une campagne de push étiquetée `promotional`. Il est prévu qu'il soit envoyé mercredi à 9 heures.

**Limite de fréquence par règle de tag :**

- Votre utilisateur ne doit pas recevoir plus d'une campagne de notification push par semaine avec l'étiquette `promotional`.<br><br>

| Action | Résultat |
|---|---|
| L'étiquette `promotional` est retirée de la **campagne A** après que votre utilisateur a reçu le message, mais avant que **la campagne B ne l'ait envoyé.** | Votre utilisateur reçoit **la campagne B**.|
| L'étiquette `promotional` est supprimée par erreur de la **campagne A** après que votre utilisateur a reçu le message. <br> L'étiquette est ajoutée à nouveau à la **campagne A** le mardi, avant l'envoi de la **campagne B**. | Votre utilisateur ne reçoit pas **la campagne B**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Envoi à grande échelle {#sending-at-large-scales}

Les règles de limite de fréquence par balise peuvent ne pas être appliquées correctement à de grandes échelles, comme 100 messages par canal provenant de campagnes ou de composants Canvas.

Par exemple, si votre limite de fréquence par règle de balise est :

> Pas plus de deux campagnes d’e-mail ou de composants Canvas avec la balise `Promotional` pour un utilisateur chaque semaine.

Et que vous envoyez à l’utilisateur plus de 100 e-mails de campagnes et d'étapes de Canvas avec une limite de fréquence activée pour une semaine, plus de deux e-mails peuvent être envoyés à l’utilisateur.

Étant donné que 100 messages par canal représentent un nombre supérieur à celui envoyé par la plupart des marques à leurs utilisateurs, il est peu probable que cette limitation ait un impact. Pour l’éviter, vous pouvez définir un plafond pour le nombre maximum d’e-mails que vous souhaitez que vos utilisateurs reçoivent au cours d’une semaine.

Par exemple, vous pouvez configurer la règle suivante :

> Pas plus de trois campagnes par e-mail ou étapes du canvas par semaine pour l'ensemble des campagnes et des étapes du canvas.

Cette règle stipule qu'aucun utilisateur ne peut recevoir plus de 100 e-mails par semaine, car les utilisateurs reçoivent au maximum trois e-mails par semaine provenant de campagnes ou de composants canvas pour lesquels la limite de fréquence est activée.

## Foire aux questions

### Si je modifie un limiteur d'envoi sur un canvas actif, cela affecte-t-il les utilisateurs déjà présents dans le canvas ?

Oui, lorsque vous augmentez ou diminuez une limite de débit Canvas, la limite mise à jour prend effet pour les nouveaux messages dans les 30 secondes environ suivant la modification, en raison de la mise en cache.

### La limite de fréquence peut-elle inciter les utilisateurs à quitter un canvas ?

Non. Si un utilisateur Canvas est soumis à une limite de fréquence en raison des paramètres globaux de limite de fréquence, il effectuera immédiatement l'avancement vers l'étape du canvas suivante. L'utilisateur **ne** quittera **pas** le canvas en raison de la limite de fréquence.

### Comment puis-je identifier les utilisateurs qui ont atteint leur limite de fréquence dans un canvas ?

Les utilisateurs soumis à une limite de fréquence ne génèrent pas d'événement d'envoi pour cette étape. Pour identifier ces utilisateurs, vous pouvez utiliser [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) afin de suivre les événements liés à la limite de fréquence des messages. Vous pouvez également créer une [extension de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) afin d'analyser les utilisateurs qui ont accédé au Canvas mais n'ont pas reçu le message attendu.

