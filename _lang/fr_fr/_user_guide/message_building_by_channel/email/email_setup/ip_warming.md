---
nav_title: Réchauffement d’adresses IP
article_title: Réchauffement d’adresses IP
page_order: 1
page_type: reference
description: "Le présent article de référence couvre le sujet du réchauffement d’adresses IP et des bonnes pratiques."
channel: email

---

# Réchauffement d’adresses IP

> Le réchauffement d’adresses IP est la pratique consistant à obtenir des fournisseurs de boîte de réceptions e-mail de recevoir des communications à partir de vos adresses IP dédiées. Il s'agit d'une partie extrêmement importante de l'envoi d'e-mails avec n'importe quel fournisseur de services e-mailing (ESP) et d'une pratique courante chez Braze pour confirmer que vos messages atteignent leur boîte de réception à un taux élevé et constant.

Le réchauffement d’adresses IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu’une nouvelle adresse IP est utilisée pour envoyer un e-mail, les fournisseurs de services Internet surveillent les e-mails de manière programmatique afin de vérifier qu’ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs.

## Que faire si je n’ai pas le temps de réchauffer les adresses IP ?

**Le réchauffement d'adresses IP est requis.** Si vous ne réchauffez pas les adresses IP de manière appropriée et que le modèle de votre e-mail suscite des soupçons, votre vitesse de livraison des e-mails pourrait être considérablement réduite ou ralentie. Votre domaine ou IP peuvent également être bloquées par les Fournisseurs de services Internet ce qui peut entraîner que vos e-mails passent directement dans le dossier spam de la boîte de réception de votre utilisateur à la place. Il est donc important de réchauffer correctement vos adresses IP.

Les fournisseurs de services Internet arrêtent la livraison des e-mails lorsque la suspicion de spam se produit afin de protéger leurs utilisateurs. Par exemple, si vous envoyez à 100 000 utilisateurs, le fournisseur de services Internet peut envoyer l’e-mail à seulement 5 000 de ces utilisateurs au cours de la première heure. Le fournisseur de services Internet surveille ensuite les mesures d’engagement telles que les taux d’ouverture, les taux de clics, les désinscriptions et les rapports de courriers indésirables. Donc, si un nombre important de rapport de courrier indésirable se produit, ils peuvent choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le remettre dans la boîte de réception de l'utilisateur. 

Si l’engagement est modéré, il peut continuer à faire passer votre e-mail afin de recueillir davantage de données d’engagement afin de déterminer si le courrier est un spam avec plus de certitude. Si l’e-mail a des mesures d’engagement très élevées, il peut cesser de faire passer cet e-mail entièrement. Ils utilisent ces données pour créer une réputation de courrier électronique qui déterminera finalement si vos e-mails sont filtrés automatiquement vers le spam.

Si votre domaine ou votre IP est bloqué par un FAI, les messages du [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contiendront des informations sur les sites web à visiter pour faire appel à ces FAI et pour sortir de ces listes.

## Planifications de réchauffement d’adresses IP

Nous recommandons fortement de respecter strictement cette planification de réchauffement d’adresses IP pour garantir la livrabilité. Il est également important de ne pas sauter de jours, car une mise à l'échelle régulière améliore les indicateurs de livraison.

Jour | Nombre d’e-mails à envoyer
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
10 | 100 000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18 et + | Deux fois par jour jusqu’à ce que le volume souhaité soit atteint

Nous vous conseillons un réchauffement jusqu'à votre envoi maximal. En d'autres termes, si vous envoyez normalement 2 millions d'e-mails par jour mais que vous prévoyez d'en envoyer 7 millions pendant une période saisonnière, c'est à ce "pic" d'envoi que vous devez vous préparer.

Une fois le réchauffement terminé et que vous avez atteint le volume quotidien souhaité, vous devez viser à maintenir ce volume tous les jours. Il est normal qu'il y ait des fluctuations, mais si vous atteignez le volume souhaité et que vous ne procédez à un envoi massif qu'une fois par semaine, vous risquez de nuire à vos indicateurs de livraison et à votre réputation d'expéditeur. 

{% alert important %}
La plupart des fournisseurs de services Internet stockent les données de réputation uniquement pendant 30 jours. Si vous passez un mois sans envoi de messages, vous devrez répéter le processus de réchauffement d’adresses IP.
{% endalert %}

## Comment limiter les envois pendant le réchauffement

Notre fonctionnalité intégrée de limitation du nombre d'utilisateurs est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messages souhaités lors de la création de la campagne, à l'étape [Utilisateurs ciblés]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), sélectionnez le menu déroulant **Options avancées** pour limiter vos utilisateurs. Au fur et à mesure que votre planification de réchauffement se poursuit, vous pouvez augmenter progressivement cette limite pour augmenter le volume d’e-mails que vous envoyez.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentation du sous-domaine

De nombreux fournisseurs de services d’accès aux courriels et fournisseurs d’accès aux courriels ne filtrent plus uniquement la réputation de l’adresse IP. Ces technologies de filtrage représentent désormais une réputation basée sur le domaine. Cela signifie que les filtres analyseront toutes les données associées au domaine de l’expéditeur et non pas seulement à l’adresse IP. Pour cette raison, en plus de réchauffer votre e-mail adresse IP, nous vous recommandons également de disposer de domaines ou sous-domaines distincts pour le marketing, la transaction et la messagerie d’entreprise. 

{% alert important %}
La segmentation sous-domaine est particulièrement importante pour les expéditeurs à gros volumes. Ces expéditeurs doivent travailler avec un conseiller de Braze lors de la configuration de leur compte afin de s’assurer qu’ils respectent cette pratique.
{% endalert %}

Nous vous recommandons de segmenter vos domaines de sorte que le courrier d’entreprise soit envoyé par le biais de votre domaine de premier niveau et que le marketing et le courrier transactionnel soient envoyés par différents domaines ou sous-domaines.

## Bonnes pratiques

Toutes les conséquences d’une absence de réchauffement d’adresses IP peuvent être évitées si vous suivez ces bonnes pratiques de réchauffement.

### Commencez par envoyer de petits volumes d’e-mails

Augmentez la quantité que vous envoyez chaque jour aussi progressivement que possible. Les campagnes e-mail abruptes et à haut volume sont considérées avec le plus grand scepticisme par les Fournisseurs d’accès Internet. C'est pourquoi vous devez commencer par envoyer de petites quantités d'e-mails et augmenter progressivement jusqu’à atteindre le volume d'e-mails que vous avez l'intention d'envoyer. Quel que soit le volume, nous vous suggérons de réchauffer votre adresse IP pour être sûr. Consultez la rubrique [Planification du réchauffement d'adresses IP](#ip-warming-schedule).

### Ayez un contenu d’introduction attrayant

Assurez-vous que votre premier contenu est très engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et interagissent avec votre e-mail. Privilégiez toujours les e-mails bien ciblés pour éviter des lancements en masse sans discrimination lors du réchauffement des adresses IP.

### Définissez une cadence d’envoi cohérente

Une fois le réchauffement d’adresses IP terminé, créez une cadence d’envoi, en veillant également à diffuser vos e-mails sur un ou plusieurs jours. En créant une planification aussi cohérente que possible, vous pouvez empêcher un refroidissement d’adresses IP, qui peut se produire si le volume envoyé s’arrête ou diminue considérablement pendant plus de quelques jours. 

Reportez-vous à notre [planification du réchauffement d'adresses IP](#ip-warming-schedules) pour étaler vos envois sur une période plus longue, plutôt que d'effectuer un envoi de masse à un moment précis.

### Nettoyez vos listes d’e-mails

Assurez-vous que votre liste d'e-mails est propre et qu'elle ne contient pas d'adresses e-mail anciennes ou non vérifiées. L'idéal est de s'assurer que vous êtes à la fois [conforme à la CASL et à la CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Surveillez votre réputation d’expéditeur

Lorsque que vous effectuez le processus de réchauffement d’adresses IP, surveillez attentivement votre réputation d’expéditeur. Il est important de surveiller ces indicateurs spécifiques :
- **Taux de rebond :** Si une campagne dépasse de 3 à 5 %, vous devez évaluer la propreté de votre liste en suivant les directives de notre [Gardez-le propre : Article sur l’importance de l’hygiène des listes d’e-mails](https://www.braze.com/blog/email-list-hygiene/). En outre, vous devriez envisager de mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) afin de cesser d'envoyer des e-mails à des adresses non sollicitées ou inactives.
- **Signalement de courrier indésirable :** Si une campagne est signalée comme étant du courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vérifier qu'il cible une audience intéressée et vous assurer que vos e-mails sont formulés de manière à susciter son intérêt.
- **Taux d'ouverture :** Les taux d'ouverture sont un indicateur utile de l'emplacement de la boîte de réception. Si votre taux d'ouverture unique est supérieur à 25 %, vous êtes probablement bien placé dans la boîte de réception, ce qui indique une réputation positive de l'expéditeur.

{% alert tip %}
Braze vous déconseille d'utiliser le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) pour réchauffer vos adresses IP. Étant donné que les campagnes de réchauffement d’adresses IP sont certaines des premières campagnes que vous envoyez, Braze n’aura pas suffisamment d’informations sur vos utilisateurs pour calculer un temps d’envoi optimal. Dans ce cas, tous les messages avec timing intelligent constitueront par défaut le temps de retour et envoyés en même temps.
{% endalert %}

{% alert tip %}
Il est normal que le courrier soit envoyé dans le dossier spam pendant le réchauffement d'adresses IP, car votre domaine et votre IP n'ont pas encore acquis une réputation positive. Si le courrier arrive dans votre dossier spam, il se peut que votre administrateur de messagerie doive ajouter le domaine et l'IP d'envoi de Braze à la liste d'autorisation de votre entreprise.
{% endalert %}

