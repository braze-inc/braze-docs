---
nav_title: Réchauffement d’adresses IP
article_title: Réchauffement d’adresses IP
page_order: 1
page_type: reference
description: "Le présent article de référence couvre le sujet du réchauffement d’adresses IP et des bonnes pratiques."
channel: email

---

# Réchauffement d’adresses IP

> Le réchauffement d’adresses IP est la pratique consistant à obtenir des fournisseurs de boîte de réceptions e-mail de recevoir des communications à partir de vos adresses IP dédiées. Il s’agit d’une partie extrêmement importante de l’envoi par e-mail avec tout fournisseur de services de courrier électronique et de pratique courante de Braze pour s’assurer que vos messages atteignent les boîtes de réception à un taux toujours élevé.

Le réchauffement d’adresses IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu’une nouvelle adresse IP est utilisée pour envoyer un e-mail, les ISP surveillent les e-mails de manière programmatique afin de vérifier qu’ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs.

## Que faire si je n’ai pas le temps de réchauffer les adresses IP ?

**Le réchauffement d’adresses IP est requis.** Si vous ne réchauffez pas les adresses IP de manière appropriée et que le modèle de votre e-mail suscite des soupçons, votre vitesse de livraison des e-mails pourrait être considérablement réduite ou ralentie. Votre domaine ou IP peuvent également être bloquées par les Fournisseurs de services Internet ce qui peut entraîner que vos e-mails passent directement dans le dossier spam de la boîte de réception de votre utilisateur à la place. Il est donc important de réchauffer correctement vos adresses IP.

Les ISP arrêtent la livraison des e-mails lorsque la suspicion de spam se produit afin de protéger leurs utilisateurs. Par exemple, si vous envoyez à 100 000 utilisateurs, le fournisseur de services Internet peut envoyer l’e-mail à seulement 5 000 de ces utilisateurs au cours de la première heure. Le Fournisseur de services Internet surveille ensuite les mesures d’engagement telles que les taux d’ouverture, les taux de clics, les désinscriptions et les rapports de spam. Donc, si un nombre important de rapport de courrier indésirable se produit, ils peuvent choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le remettre dans la boîte de réception de l'utilisateur. 

Si l’engagement est modéré, il peut continuer à faire passer votre e-mail afin de recueillir davantage de données d’engagement afin de déterminer si le courrier est un spam avec plus de certitude. Si l’e-mail a des mesures d’engagement très élevées, il peut cesser de faire passer cet e-mail entièrement. Ils utilisent ces données pour créer une réputation de courrier électronique qui déterminera finalement si vos e-mails sont filtrés automatiquement vers le spam.

Si votre domaine ou votre adresse IP est bloquée par un fournisseur de services internet, les codes de réponse dans la Developer Console de Braze contiendront des informations sur les sites Web à visiter pour faire appel auprès des Fournisseurs de services Internet afin d’être exclu de ces listes.

## Planifications de réchauffement d’adresses IP

Nous recommandons fortement de respecter strictement cette planification de réchauffement d’adresses IP pour garantir la délivrabilité. Il est également important de ne pas sauter les jours car une échelle constante améliore la délivrabilité.

Jour | Nombre d’e-mails à envoyer
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1 000
5 | 5 000
6 | 10 000
7 | 20 000
8 | 40 000
9 | 70 000
10 | 100 000
11 | 150 000
12 | 250 000
13 | 400 000
14 | 600 000
15 | 1 000 000
16 | 2 000 000
17 | 44 000 000
18+ | Deux fois par jour jusqu’à ce que le volume souhaité soit atteint

Une fois le réchauffement terminé et que vous avez atteint le volume quotidien souhaité, vous devez viser à maintenir ce volume tous les jours. Une certaine fluctuation est possible, mais atteindre le volume souhaité, puis ne faire qu’un envoi de masse une fois par semaine, peut affecter négativement votre délivrabilité et votre réputation d’expéditeur. 

{% alert important %}
La plupart des ISP stockent les données de réputation uniquement pendant 30 jours. Si vous passez un mois sans envoi de messages, vous devrez répéter le processus de réchauffement d’adresses IP.
{% endalert %}

## Comment limiter les envois pendant le réchauffement

La fonctionnalité de limitation de l’utilisateur intégrée de Braze sert d’outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messagerie souhaités pendant la création de campagnes, à l’étape [Target Users (Cibler des utilisateurs)]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-5-choose-your-target-segment) sélectionnez le menu déroulant **Advanced Options (Options avancées)** pour limiter vos utilisateurs. Au fur et à mesure que votre planification de réchauffement se poursuit, vous pouvez augmenter progressivement cette limite pour augmenter le volume d’e-mails que vous envoyez.

![][18]

## Segmentation du sous-domaine

De nombreux fournisseurs de services d’accès aux courriels et fournisseurs d’accès aux courriels ne filtrent plus uniquement la réputation de l’adresse IP. Ces technologies de filtrage représentent désormais une réputation basée sur le domaine. Cela signifie que les filtres analyseront toutes les données associées au domaine de l’expéditeur et non pas seulement à l’adresse IP. Pour cette raison, en plus de réchauffer votre e-mail adresse IP, nous vous recommandons également de disposer de domaines ou sous-domaines distincts pour le marketing, la transaction et la messagerie d’entreprise. 

{% alert important %}
La segmentation sous-domaine est particulièrement importante pour les expéditeurs à gros volumes. Ces expéditeurs doivent travailler avec un conseiller de Braze lors de la configuration de leur compte pour s’assurer qu’ils adhèrent à cette pratique.
{% endalert %}

Nous vous recommandons de segmenter vos domaines de sorte que le courrier d’entreprise soit envoyé par le biais de votre domaine de premier niveau et que le marketing et le courrier transactionnel soient envoyés par différents domaines ou sous-domaines.

## Bonnes pratiques

Toutes les conséquences d’une absence de réchauffement d’adresses IP peuvent être évitées si vous suivez ces bonnes pratiques de réchauffement.

### Commencez par envoyer de petits volumes d’e-mails

Augmentez la quantité que vous envoyez chaque jour aussi progressivement que possible. Les campagnes e-mail abruptes et à haut volume sont considérées avec le plus grand scepticisme par les Fournisseurs d’accès Internet. Par conséquent, vous devez commencer par envoyer de petites quantités d’e-mails et augmenter graduellement vers le volume d’e-mails que vous avez l’intention d’envoyer à terme. Quel que soit le volume, nous vous suggérons de réchauffer votre adresse IP pour être sûr. Consultez la [Planification de réchauffement d’adresses IP](#ip-warming-schedule).

### Ayez un contenu d’introduction attrayant

Assurez-vous que votre premier contenu est très intéressant et optimise la probabilité que les utilisateurs cliquent, s’ouvrent et s’engagent dans votre e-mail. Privilégiez toujours les e-mails bien ciblés pour éviter des lancements en masse sans discrimination lors du réchauffement des adresses IP.

### Définissez une cadence d’envoi cohérente

Une fois le réchauffement d’adresses IP terminé, créez une cadence d’envoi, en veillant également à diffuser vos e-mails sur un ou plusieurs jours. En créant une planification aussi cohérente que possible, vous pouvez empêcher un refroidissement d’adresses IP, qui peut se produire si le volume envoyé s’arrête ou diminue considérablement pendant plus de quelques jours. 

Utilisez notre [Planification de réchauffement d’adresses IP](#ip-warming-schedules) pour étaler vos envois sur une période plus longue, plutôt que d’effectuer un envoi de masse à un seul moment spécifique.

### Nettoyez vos listes d’e-mails

Assurez-vous que votre liste d’e-mails est propre et qu’il n’y a pas d’e-mails anciens ou non vérifiés. Vérifier que vous êtes [Conforme CASL-et CAN-SPAM][40] est idéal.

### Surveillez votre réputation d’expéditeur

Lorsque que vous effectuez le processus de réchauffement d’adresses IP, surveillez attentivement votre réputation d’expéditeur. Il est important de surveiller ces indicateurs spécifiques :
- **Taux de rebonds :** Si une campagne dépasse de 3 à 5 %, vous devez évaluer la propreté de votre liste en suivant les directives de notre [Gardez-le propre : Article sur l’importance de l’hygiène des listes d’e-mails][43]. En outre, vous devriez envisager de mettre en œuvre un [politique de temporisation][46] pour arrêter d’envoyer des adresses e-mail non engagées ou dormantes.
- **Rapports de courrier indésirable :** Si une campagne est signalée comme courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vous assurer qu’il cible une audience intéressé et veiller à ce que vos courriels soient correctement formulés pour susciter leur intérêt.
- **Scores de réputation de l’expéditeur :** [SenderScore][44] de ReturnPath et [SenderBase][45] IronPort de Cisco sont des ressources utiles pour vérifier l’évolution de votre réputation.

{% alert tip %}
Braze recommande d’utiliser [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) pour réchauffer vos adresses IP. Étant donné que les campagnes de réchauffement d’adresses IP sont certaines des premières campagnes que vous envoyez, Braze n’aura pas suffisamment d’informations sur vos utilisateurs pour calculer un temps d’envoi optimal. Dans ce cas, tous les messages avec timing intelligent constitueront par défaut le temps de retour et envoyés en même temps.
{% endalert %}

[18]: {% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %}
[40]: {{site.baseurl}}/user_guide/onboarding_with_braze/spam_regulations/
[43]: https://www.braze.com/blog/email-list-hygiene/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
