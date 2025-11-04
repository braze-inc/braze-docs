---
nav_title: "réchauffement d'adresses IP"
article_title: "Réchauffement d'adresses IP"
page_order: 1
page_type: reference
description: "Cet article de référence traite du réchauffement d'adresses IP et des meilleures pratiques."
channel: email

---

# réchauffement d'adresses IP

> Le réchauffement d'adresses IP consiste à habituer les fournisseurs de boîtes de réception d'e-mails à recevoir des messages provenant de vos adresses IP dédiées. Il s'agit d'un élément extrêmement important de l'envoi d'e-mails avec n'importe quel fournisseur de services e-mailing (ESP) et d'une pratique courante chez Braze pour confirmer que vos messages atteignent leur boîte de réception à un taux élevé et constant.

Le réchauffement d'adresses IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (FAI). Chaque fois qu'une nouvelle adresse IP est utilisée pour envoyer un e-mail, les FAI contrôlent ces e-mails de manière programmatique afin de vérifier qu'elle n'est pas utilisée pour envoyer des spams aux utilisateurs.

## Que faire si je n'ai pas le temps de réchauffer les IP ?

**Le réchauffement d'adresses IP est nécessaire.** Si vous ne réchauffez pas les IP de manière appropriée et que le modèle de vos e-mails éveille des soupçons, la vitesse de réception/distribution de vos e-mails pourrait être considérablement réduite ou ralentie. Votre domaine ou votre IP peut également être bloqué par les fournisseurs d'accès à Internet, ce qui peut avoir pour conséquence que vos e-mails se retrouvent directement dans le dossier spam de la boîte de réception de l'utilisateur. Il est donc important de réchauffer correctement vos IP.

Les FAI limitent la réception/distribution des e-mails en cas de suspicion de spam afin de protéger leurs utilisateurs. Par exemple, si vous envoyez un message à 100 000 utilisateurs, le fournisseur d'accès à Internet pourrait ne délivrer l'e-mail qu'à 5 000 d'entre eux au cours de la première heure. Ensuite, le FAI surveille les mesures d'engagement telles que les taux d'ouverture, les taux de clics, les désabonnements et les rapports signalement de courrier indésirable. Ainsi, si un nombre important de signalement de courrier indésirable se produit, ils peuvent choisir de reléguer le reste de l'envoi dans le dossier spam plutôt que de le livrer dans la boîte de réception de l'utilisateur. 

Si l'engagement est modéré, ils peuvent continuer à étrangler votre e-mail pour collecter davantage de données d'engagement afin de déterminer avec plus de certitude s'il s'agit ou non d'un spam. Si les indicateurs d'engagement de l'e-mail sont très élevés, il se peut qu'ils cessent complètement d'envoyer cet e-mail. Ils utilisent ces données pour créer une réputation d'e-mail qui déterminera finalement si vos e-mails sont ou non filtrés automatiquement vers le spam.

Si votre domaine ou votre IP est bloqué par un FAI, les messages du [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contiendront des informations sur les sites web à visiter pour faire appel à ces FAI et pour sortir de ces listes.

## Planification du réchauffement d'adresses IP

Nous vous recommandons vivement de respecter cette planification du réchauffement d'adresses IP dans le strict but de favoriser la livrabilité. Il est également important de ne pas sauter de jours, car une mise à l'échelle régulière améliore les indicateurs de réception/distribution.

Jour | \# Nombre d'e-mails à envoyer
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 5,000
6 | 10,000
7 | 20,000
8 | 40,000
9 | 70,000
10 | 100,000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | Doublement quotidien jusqu'au volume désiré

Nous vous conseillons de vous échauffer jusqu'à votre envoi maximal. En d'autres termes, si vous envoyez normalement 2 millions d'e-mails par jour mais que vous prévoyez d'en envoyer 7 millions pendant une période saisonnière, c'est à ce "pic" d'envoi que vous devez vous préparer.

Une fois que le réchauffement est terminé et que vous avez atteint le volume quotidien souhaité, vous devez vous efforcer de maintenir ce volume quotidiennement. Il est normal qu'il y ait des fluctuations, mais si vous atteignez le volume souhaité et que vous ne procédez à un envoi massif qu'une fois par semaine, vous risquez de nuire à vos indicateurs de réception/distribution et à la réputation de l'expéditeur. 

{% alert important %}
La plupart des FAI ne conservent les données de réputation que pendant 30 jours. Si vous restez un mois sans envoyer de messages, vous devrez recommencer le processus de réchauffement d'adresses IP.
{% endalert %}

## Comment limiter les envois pendant le réchauffement

Notre fonctionnalité intégrée de limitation du nombre d'utilisateurs est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messages souhaités lors de la création de la campagne, à l'étape [Utilisateurs ciblés]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), sélectionnez le menu déroulant **Options avancées** pour limiter vos utilisateurs. Au fur et à mesure de votre planification, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails que vous envoyez.

\![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentation des sous-domaines

De nombreux FAI et fournisseurs d'accès à l'e-mail ne filtrent plus seulement en fonction de la réputation des adresses IP. Ces technologies de filtrage prennent désormais également en compte la réputation basée sur le domaine. Cela signifie que les filtres examineront toutes les données associées au domaine de l'expéditeur et pas seulement l'adresse IP. C'est pourquoi, outre le réchauffement d'adresses IP pour votre e-mail, nous vous recommandons d'avoir des domaines ou des sous-domaines distincts pour le marketing, les transactions et le courrier d'entreprise. 

{% alert important %}
La segmentation des sous-domaines est particulièrement importante pour les expéditeurs de gros volumes. Ces expéditeurs doivent travailler avec un conseiller de Braze lors de la création de leur compte pour confirmer qu'ils adhèrent à cette pratique.
{% endalert %}

Nous vous recommandons de segmenter vos domaines de manière à ce que le courrier de l'entreprise soit envoyé par votre domaine de premier niveau, et que le courrier marketing et transactionnel soit envoyé par des domaines ou sous-domaines différents.

## Meilleures pratiques

Toutes les conséquences du réchauffement d'adresses IP peuvent être évitées si vous suivez ces meilleures pratiques en matière de réchauffement d'adresses IP.

### Commencez par envoyer de petits volumes d'e-mail

Augmentez le montant que vous envoyez chaque jour aussi progressivement que possible. Les campagnes d'e-mail brutales et à fort volume sont considérées avec le plus grand scepticisme par les fournisseurs d'accès à Internet. C'est pourquoi vous devez commencer par envoyer de petites quantités d'e-mails et augmenter progressivement le volume d'e-mails que vous avez l'intention d'envoyer. Quel que soit le volume, nous vous conseillons de réchauffer votre IP pour plus de sécurité. Voir la [planification du réchauffement d'adresses IP](#ip-warming-schedule).

### Proposez un contenu introductif attrayant

Confirmez que votre premier contenu est très engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et s'engagent avec votre e-mail. Lors du réchauffement d'adresses IP, préférez toujours des e-mails bien ciblés à des envois sans discernement.

### Établir une cadence d'envoi cohérente

Une fois le réchauffement d'adresses IP terminé, créez une cadence d'envoi, en veillant également à répartir vos e-mails sur une journée ou plusieurs jours. En établissant une planification aussi cohérente que possible, vous pouvez éviter un refroidissement de la propriété intellectuelle, qui peut se produire si le volume d'envoi s'arrête ou diminue de manière significative pendant plus de quelques jours. 

Reportez-vous à notre [planification du réchauffement d'adresses IP](#ip-warming-schedules) pour étaler vos envois sur une période plus longue, plutôt que d'envoyer un message en masse à un moment précis.

### Nettoyez vos listes d'e-mails

Confirmez que votre liste d'e-mails est propre et qu'elle ne contient pas d'e-mails anciens ou non vérifiés. L'idéal est de s'assurer que vous êtes à la fois [conforme à la CASL et à la CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Contrôlez la réputation de votre expéditeur

Veillez à surveiller attentivement la réputation de votre expéditeur pendant le processus de réchauffement IP. Ces indicateurs spécifiques sont importants à surveiller :
- **Taux de rebond :** Si le taux de rebond d'une campagne est supérieur à 3-5 %, vous devez évaluer la propreté de votre liste en suivant les recommandations de notre site [: L'importance de l'hygiène des listes d'e-mails](https://www.braze.com/blog/email-list-hygiene/) article. En outre, vous devriez envisager de mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) afin de cesser d'envoyer des e-mails à des adresses non sollicitées ou inactives.
- **Signalement de courrier indésirable :** Si une campagne est signalée comme étant du courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vérifier qu'il cible une audience intéressée et vous assurer que vos e-mails sont formulés de manière à susciter son intérêt.
- **Taux d'ouverture :** Les taux d'ouverture sont un indicateur utile de la place occupée dans la boîte de réception. Si votre taux d'ouverture unique est supérieur à 25 %, vous êtes probablement bien placé dans la boîte de réception, ce qui indique une réputation positive de l'expéditeur.

{% alert tip %}
Braze vous déconseille d'utiliser le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) pour réchauffer vos adresses IP. Les campagnes de réchauffement d'adresses IP étant parmi les premières que vous envoyez, Braze ne disposera pas de suffisamment d'informations sur vos utilisateurs pour calculer une heure d'envoi optimale. Dans ce cas, tous les messages dotés d'un timing intelligent prendront par défaut l'heure de repli et seront de toute façon envoyés à la même heure.
{% endalert %}

{% alert tip %}
Il est normal que le courrier soit envoyé dans le dossier spam pendant le réchauffement d'adresses IP, car votre domaine et votre IP n'ont pas encore acquis une réputation positive. Si le courrier arrive dans votre dossier spam, il se peut que votre administrateur de messagerie doive ajouter le domaine et l'IP d'envoi de Braze à la liste d'autorisation de votre entreprise.
{% endalert %}

