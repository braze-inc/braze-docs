---
<<<<<<< HEAD
nav_title: Réchauffement IP
article_title: Réchauffement IP
=======
nav_title: Réchauffement d’adresses IP
article_title: Réchauffement d’adresses IP
>>>>>>> c74f78153 (1177663|i18n_30_Dec_2022_08_00_01_270_33|1672408833874-GlobalLink Translation)
page_order: 5
page_type: reference
description: "Le présent article de référence couvre le sujet du réchauffement IP et des meilleures pratiques."
channel: (e-mail)

---

# Réchauffement IP

## Qu’est-ce que le réchauffement IP ?

Le réchauffement IP est la pratique consistant à obtenir des fournisseurs d’e-mails pour recevoir des messages à partir de vos adresses IP dédiées. Il s’agit d’une partie extrêmement importante de l’envoi par e-mail avec tout fournisseur de services de courrier électronique et de pratique courante au Braze pour s’assurer que vos messages atteignent les boîtes de destination à un taux toujours élevé.

Le réchauffement IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu’une nouvelle adresse IP est utilisée pour envoyer un e-mail, les ISP surveillent les e-mails de manière programmatique afin de vérifier qu’ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs.

## Que faire si je n’ai pas le temps de réchauffer les IP ?

**Le réchauffement IP est requis.** Si vous ne parvenez pas à réchauffer les IP de manière appropriée, et que le modèle de votre e-mail provoque une suspicion, tout ou partie des éléments suivants peut se produire :

1. **Votre vitesse de livraison par e-mail pourrait être considérablement étranglée ou ralentie.**
      - Les ISP arrêtent la livraison des e-mails lorsque la suspicion de spam se produit afin de protéger leurs utilisateurs. Par exemple, si vous envoyez à 100000 utilisateurs, le fournisseur de services Internet peut envoyer l’e-mail à seulement 5 000 de ces utilisateurs au cours de la première heure. Le Fournisseur de services Internet surveille ensuite les mesures d’engagement telles que les taux d’ouverture, les taux de clics, les désinscriptions et les rapports de spam.
      - Si un nombre important de rapport de courrier indésirable se produit, ils peuvent choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le remettre dans la boîte de réception de l'utilisateur.
      - Si l’engagement est modéré, il peut continuer à faire passer votre e-mail afin de recueillir davantage de données d’engagement afin de déterminer si le courrier est un spam avec plus de certitude.
      - Si l’e-mail a des mesures d’engagement très élevées, il peut cesser de faire passer cet e-mail entièrement. Ils utilisent ces données pour créer une réputation de courrier électronique qui déterminera finalement si vos e-mails sont filtrés automatiquement vers le spam.<br><br>
2. **Votre domaine et ou IP peuvent être répertoriés sur liste noire par les Fournisseurs de services Internet à ce moment-là, tous vos e-mails commenceront à accéder directement au dossier spam de la boîte de réception de votre utilisateur.**
  - Si cela se produit, les codes de réponse dans le **Developer Console de Braze** contiendront des informations sur les sites Web à visiter pour faire appel auprès des Fournisseurs de services Internet afin d’être exclu de ces listes.

## Meilleures pratiques de réchauffement IP

Toutes ces conséquences sont totalement évitables si vous suivez les directives suivantes :
<<<<<<< HEAD
=======

1. **Commencez par envoyer de petits volumes d’e-mails et augmentez le montant que vous envoyez chaque jour aussi progressivement que possible.**<br>
Les campagnes e-mail abruptes et à haut volume sont considérées avec le plus grand scepticisme par les Fournisseurs d’accès Internet. Par conséquent, vous devez commencer par envoyer de petites quantités d’e-mails et augmenter graduellement vers le volume d’e-mails que vous avez l’intention d’envoyer à terme. Quel que soit le volume, nous vous suggérons de réchauffer votre adresse IP pour être sûr. Pour plus de détails, consultez la planification suivante :<br><br>
2. **Assurez-vous que votre premier contenu est très intéressant et optimise la probabilité que les utilisateurs cliquent, s’ouvrent et s’engagent dans votre e-mail.**<br>Privilégiez toujours les e-mails bien ciblés pour éviter des lancements en masse sans discrimination lors du réchauffement des adresses IP.<br><br>
3. **Lorsque le réchauffement IP est terminé, continuez à envoyer les e-mails aussi régulièrement que possible.**<br>
Les IP peuvent refroidir si le volume s’arrête ou diminue considérablement pendant plus de quelques jours.<br><br>
4. **Étalez vos envois par e-mail sur un jour ou plusieurs jours.**<br>
Utilisez notre [Planification de réchauffement IP](#ip-warming-schedules) pour transmettre vos envois sur une période plus longue, plutôt que d’envoyer une explosion de masse à un seul moment spécifique. Des caractéristiques telles que la [livraison fuseau horaire local]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#what-does-local-time-zone-delivery-offer) de Braze peuvent vous aider à envoyer des messages en fonction du fuseau horaire individuel d’un utilisateur, vous effectuez l’envoi lorsque les utilisateurs sont plus susceptibles d’être actifs.<br><br>
5. **Assurez-vous que votre liste d’e-mails est propre et qu’il n’y a pas d’e-mails anciens ou non vérifiés.**<br>Vérifier que vous êtes [Conforme CASL-et CAN-SPAM][40] est idéal.<br><br>
6. **Surveillez attentivement votre réputation de l’expéditeur pendant que vous effectuez le processus de réchauffement IP.** <br>
Les mesures suivantes sont importantes à observer pendant le réchauffement :
- **Taux de rebonds :** Si une campagne dépasse de 3 à 5 %, vous devez évaluer la propreté de votre liste en suivant les directives de notre [Gardez-le propre : Article sur l’importance de l’hygiène des listes d’e-mails][43]. En outre, vous devriez envisager de mettre en œuvre un [Politique de temporisation][46] pour arrêter d’envoyer des adresses e-mail non engagées ou dormantes.
- **Rapports de courrier indésirable :** Si une campagne est signalée comme courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vous assurer qu’il cible une audience intéressé et veiller à ce que vos courriels soient correctement formulés pour susciter leur intérêt.
- **Scores de réputation de l’expéditeur :** Les services suivants sont utiles pour vérifier la progression de votre réputation : [SenderScocre de ReturnPath ][44]et IronPort [SenderBase][45] de Cisco

{% alert note %}
Braze recommande d’utiliser [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) pour réchauffer vos adresses IP. Étant donné que les campagnes de réchauffement d’adresses IP sont certaines des premières campagnes que vous envoyez, Braze n’aura pas suffisamment d’informations sur vos utilisateurs pour calculer un temps d’envoi optimal. Dans ce cas, tous les messages avec timing intelligent constitueront par défaut le temps de retour et envoyés en même temps.
{% endalert %}
>>>>>>> c74f78153 (1177663|i18n_30_Dec_2022_08_00_01_270_33|1672408833874-GlobalLink Translation)

1. **Commencez par envoyer de petits volumes d’e-mails et augmentez le montant que vous envoyez chaque jour aussi progressivement que possible.**<br>
Les campagnes par e-mail abrupt et à haut volume sont considérées avec le plus grand scepticisme par les Fournisseurs d’accès Internet. Par conséquent, vous devez commencer par envoyer de petites quantités d’e-mails et graduellement vers le volume d’e-mails que vous avez finalement l’intention d’envoyer. Quel que soit le volume, nous vous suggérons de réchauffer votre IP pour être sûr. Pour plus de détails, consultez la planification suivante :<br><br>
2. **Assurez-vous que votre premier contenu est très intéressant et optimise la probabilité que les utilisateurs cliquent, s’ouvrent et s’engagent dans votre e-mail.**<br>Privilégiez toujours les e-mails bien ciblés pour éviter de discriminer les explosions lors de l’échauffement des IP.<br><br>
3. **Lorsque le réchauffement IP est terminé, continuez à envoyer les e-mails aussi régulièrement que possible.**<br>
Les IP peuvent refroidir si le volume s’arrête ou diminue considérablement pendant plus de quelques jours.<br><br>
4. **Étalez vos envois par e-mail sur un jour ou plusieurs jours.**<br>
Utilisez notre [Planification de réchauffement IP](#ip-warming-schedules) pour transmettre vos envois sur une période plus longue, plutôt que d’envoyer une explosion de masse à un seul moment spécifique. Des caractéristiques telles que la [livraison fuseau horaire local]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#what-does-local-time-zone-delivery-offer) de Braze peuvent vous aider à envoyer des messages en fonction du fuseau horaire individuel d’un utilisateur, vous effectuez l’envoi lorsque les utilisateurs sont plus susceptibles d’être actifs.<br><br>
5. **Assurez-vous que votre liste d’e-mails est propre et qu’il n’y a pas d’e-mails anciens ou non vérifiés.**<br>Vérifier que vous êtes à la fois [conforme CASL- et CAN-SPAM][40] est idéal.<br><br>
6. **Surveillez attentivement votre réputation de l’expéditeur pendant que vous effectuez le processus de réchauffement IP.** <br>
Les mesures suivantes sont importantes à observer pendant le réchauffement :
- **Taux de retour** Si une campagne dépasse de 3 à 5 %, vous devez évaluer la propreté de votre liste en suivant les directives de notre [Gardez-le propre : Article sur l’importance de l’hygiène des listes d’e-mails][43]. En outre, vous devriez envisager de mettre en œuvre une [Politique de temporisation][46] pour arrêter d’envoyer des adresses e-mail non engagées ou dormantes.
- **Rapports de courrier indésirable**: Si une campagne est signalée comme courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vous assurer qu’il est ciblé dans un public intéressé, et veiller à ce que vos courriels soient correctement formulés pour faire rayonner leur intérêt.
- **Scores de réputation de l’expéditeur**: Les services suivants sont utiles pour vérifier la progression de votre réputation : [SenderScocre][44] de ReturnPath et IronPort [SenderBase][45] de Cisco

{% alert note %}
Braze recommande d’utiliser [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) pour réchauffer vos IP. Étant donné que les campagnes de réchauffement IP sont certaines des premières campagnes que vous envoyez, Braze n’aura pas suffisamment d’informations sur vos utilisateurs pour calculer un temps d’envoi optimal. Dans ce cas, tous les messages avec timing intelligent constitueront par défaut le temps de retour et envoyés en même temps.
{% endalert %}

## Calendriers de réchauffement IP

Nous recommandons fortement de respecter strictement cette planification de réchauffement IP pour garantir la délivrabilité. Il est également important de ne pas sauter les jours car une échelle constante améliore la délivrabilité.

Jour | # d’envoi des e-mails
----|--------------------------|
1 | 50
2 | 100
3 | 500
<<<<<<< HEAD
4 | 1 000
5 | 5 000
6 | 10 000
7 | 20 000
8 | 40 000
9 | 70 000
10 | 100 000
11 | 150 000
12 | 250 000
13 | 400 000
14 | 600 000
15 | 1 000 000
16 | 2 000 000
17 | 4 000 000
18+ | Deux fois par jour jusqu’à ce que le volume souhaité soit souhaité
=======
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
>>>>>>> c74f78153 (1177663|i18n_30_Dec_2022_08_00_01_270_33|1672408833874-GlobalLink Translation)

Une fois le réchauffement terminé et que vous avez atteint le volume quotidien souhaité, vous devez viser à maintenir ce volume tous les jours. Une certaine fluctuation est possible, mais l’atteinte du volume souhaité, alors ne faites qu’une explosion de masse une fois par semaine, susceptible d’affecter négativement votre délivrabilité et la réputation de l’expéditeur. Enfin, la plupart des ISP stockent les données de réputation uniquement pendant 30 jours. Si passez un mois sans envoi, vous devrez répéter le processus de réchauffement IP.

## Comment limiter les envois pendant le réchauffement

La fonction de limitation de l’utilisateur intégrée de Braze sert d’outil utile pour vous aider à chauffer votre adresse IP. Après avoir choisi les segments de messagerie souhaités pendant la création de campagnes, sur [Utilisateurs cibles]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-5-choose-your-target-segment) sélectionnez **Options avancées** pour limiter vos utilisateurs. Au fur et à mesure que votre planification de réchauffement se poursuit, vous pouvez augmenter progressivement cette limite pour augmenter le volume d’e-mails que vous envoyez.

![Limiter les utilisateurs][18]

## Segmentation sous-domaine

De nombreux fournisseurs de services d’accès aux courriels et fournisseurs d’accès aux courriels ne filtrent plus uniquement la réputation de l’adresse IP. Ces technologies de filtrage représentent désormais une réputation basée sur le domaine.  Cela signifie que les filtres analyseront toutes les données associées au domaine de l’expéditeur et non pas seulement à l’adresse IP. Pour cette raison, en plus de réchauffer votre e-mail adresse IP, nous vous recommandons également de disposer de domaines ou sous-domaines distincts pour le marketing, la transaction et la messagerie d’entreprise. Nous vous recommandons de segmenter vos domaines de sorte que le courrier d’entreprise soit envoyé par le biais de votre domaine de premier niveau et que le marketing et le courrier transactionnel soient envoyés par différents domaines ou sous-domaines.

{% alert important %}
La segmentation sous-domaine est particulièrement importante pour les expéditeurs à gros volumes. Ces expéditeurs doivent travailler avec un conseiller de Braze lors de la configuration de leur compte pour s’assurer qu’ils adhèrent à cette pratique.
{% endalert %}

[18]: {% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %}
[40]: {{site.baseurl}}/user_guide/onboarding_with_braze/spam_regulations/
[43]: https://www.braze.com/blog/email-list-hygiene/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
