---
nav_title: Réchauffement d'adresses IP
article_title: Réchauffement d'adresses IP
page_order: 1
page_type: reference
description: "Le présent article de référence couvre le sujet du réchauffement d'adresses IP et des bonnes pratiques."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/automated_ip_warming/'
---

# Réchauffement d'adresses IP

> Le réchauffement d'adresses IP consiste à habituer les fournisseurs de boîtes de réception e-mail à recevoir des messages provenant de vos adresses IP dédiées. Il s'agit d'une étape essentielle de l'envoi d'e-mails avec n'importe quel fournisseur de services d'e-mailing (ESP) et d'une pratique courante chez Braze pour garantir que vos messages atteignent leur boîte de réception à un taux élevé et constant.

Le réchauffement d'adresses IP est conçu pour vous aider à établir une réputation positive auprès des fournisseurs de services Internet (ISP). Chaque fois qu'une nouvelle adresse IP est utilisée pour envoyer un e-mail, les fournisseurs de services Internet surveillent ces e-mails de manière programmatique afin de vérifier qu'ils ne sont pas utilisés pour envoyer des courriers indésirables aux utilisateurs. Considérez la réputation de votre IP et de votre domaine comme un score de crédit : les fournisseurs de services Internet s'appuient sur cette réputation pour déterminer si votre courrier arrive dans la boîte de réception ou dans le dossier spam. Tout comme un score de crédit, il faut du temps pour bâtir une réputation positive, et encore plus pour en reconstruire une mauvaise.

## Que faire si je n'ai pas le temps de réchauffer les adresses IP ?

**Le réchauffement d'adresses IP est requis.** Si vous ne réchauffez pas les adresses IP de manière appropriée et que le modèle de vos e-mails suscite des soupçons, votre vitesse de distribution des e-mails pourrait être considérablement réduite ou ralentie. Votre domaine ou votre IP peuvent également être bloqués par les fournisseurs de services Internet, ce qui peut entraîner l'envoi direct de vos e-mails dans le dossier spam de la boîte de réception de vos utilisateurs. Il est donc important de réchauffer correctement vos adresses IP.

Les fournisseurs de services Internet limitent le débit de distribution des e-mails lorsqu'une suspicion de spam apparaît, afin de protéger leurs utilisateurs. Par exemple, si vous envoyez à 100 000 utilisateurs, le fournisseur de services Internet peut ne distribuer l'e-mail qu'à 5 000 d'entre eux au cours de la première heure. Le fournisseur de services Internet surveille ensuite les indicateurs d'engagement tels que les taux d'ouverture, les taux de clics, les désabonnements et les signalements de courrier indésirable. Si un nombre important de signalements de courrier indésirable se produit, il peut choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le distribuer dans la boîte de réception de l'utilisateur. 

Si l'engagement est modéré, il peut continuer à limiter le débit de vos e-mails afin de collecter davantage de données d'engagement et de déterminer avec plus de certitude si l'e-mail est indésirable ou non. Si l'e-mail affiche des indicateurs d'engagement très élevés, il peut cesser entièrement de limiter le débit de cet e-mail. Ces données servent à construire une réputation e-mail qui déterminera à terme si vos e-mails sont automatiquement filtrés comme spam.

Si votre domaine ou votre IP est bloqué par un fournisseur de services Internet, les journaux de messages dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) contiendront des informations sur les sites web à consulter pour faire appel auprès de ces fournisseurs et sortir de ces listes.

## Planifications de réchauffement d'adresses IP

Nous recommandons fortement de respecter strictement une planification de réchauffement d'adresses IP pour garantir la livrabilité. Il est également important de ne pas sauter de jours, car une montée en charge régulière améliore les indicateurs de distribution. Choisissez une planification en fonction de votre historique d'envoi d'e-mails et de vos indicateurs de livrabilité existants.

{% alert tip %}
Si vous souhaitez bénéficier d'une ressource dédiée à la livrabilité au sein de votre équipe de compte, contactez votre Account Manager Braze pour en savoir plus.
{% endalert %}

{% tabs local %}
{% tab Conservative %}

La planification conservatrice est une approche plus lente et plus prudente qui aide à établir une solide réputation d'envoi en partant de zéro. Elle est recommandée si vous débutez dans l'envoi d'e-mails, si vous migrez depuis une IP partagée, ou si vous avez rencontré des problèmes de livrabilité tels que la limitation de débit ou le blocage par un fournisseur de boîte de réception.

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1 000
11 | 1 000
12 | 1 000
13 | 2 000
14 | 2 000
15 | 2 000
16 | 4 000
17 | 4 000
18 | 4 000
19 | 8 000
20 | 8 000
21 | 8 000
22+ | Doublez tous les 3 jours jusqu'à atteindre le volume souhaité

{% endtab %}
{% tab Moderate %}

La planification modérée est une approche équilibrée qui augmente le volume d'envoi à un rythme régulier. Elle est recommandée pour la plupart des expéditeurs, y compris ceux qui disposent d'un certain historique d'envoi d'e-mails et qui passent à une nouvelle IP.

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1 000
5 | 2 000
6 | 4 000
7 | 8 000
8 | 16 000
9 | 25 000
10 | 35 000
11 | 50 000
12 | 75 000
13 | 100 000
14 | 150 000
15 | 200 000
16 | 275 000
17 | 375 000
18 | 500 000
19 | 650 000
20 | 825 000
21 | 1 000 000
22+ | Doublez tous les 2 jours jusqu'à atteindre le volume souhaité

{% endtab %}
{% tab Aggressive %}

{% alert important %}
La planification agressive est l'approche la plus rapide et n'est recommandée que pour les expéditeurs disposant d'un historique d'envoi positif et établi, ainsi que d'indicateurs de livrabilité conformes aux bonnes pratiques, notamment des taux d'ouverture élevés, des taux de clics élevés et des taux de rebond faibles. Utiliser cette planification sans un historique éprouvé peut nuire à votre réputation d'expéditeur.
{% endalert %}

Jour | Nombre d'e-mails à envoyer
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1 000
5 | 2 500
6 | 5 000
7 | 9 000
8 | 16 000
9 | 29 000
10 | 52 000
11 | 98 000
12 | 160 000
13 | 225 000
14 | 315 000
15 | 450 000
16 | 615 000
17 | 875 000
18 | 1 200 000
19 | 1 750 000
20 | 2 750 000
21+ | Doublez chaque jour jusqu'à atteindre le volume souhaité

{% endtab %}
{% endtabs %}

Dans la plupart des cas, réchauffez jusqu'à votre volume d'envoi quotidien moyen plutôt que votre volume de pointe. Les fournisseurs de services Internet examinent principalement le comportement d'envoi des dernières semaines pour évaluer votre réputation. Si vous n'atteignez votre volume de pointe que tous les quelques mois (par exemple, 7 millions pendant une période saisonnière), vous pouvez monter en charge vers ce pic plus près de la date d'envoi. En revanche, si vous atteignez votre volume de pointe toutes les une à deux semaines, réchauffez jusqu'à ce pic dès le départ.

Une fois le réchauffement d'adresses IP terminé et le volume quotidien souhaité atteint, vous devez vous efforcer de maintenir ce volume quotidiennement. Certaines fluctuations sont normales, mais atteindre le volume souhaité puis n'effectuer qu'un seul envoi massif par semaine pourrait avoir un impact négatif sur vos indicateurs de distribution et la réputation de l'expéditeur. 

{% alert important %}
La plupart des fournisseurs de services Internet ne conservent les données de réputation que pendant 30 jours. Si vous passez un mois sans envoyer de messages, vous devrez recommencer le processus de réchauffement d'adresses IP.
{% endalert %}

## Comment limiter les envois pendant le réchauffement

La fonctionnalité intégrée de limitation du nombre d'utilisateurs est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi les segments de messages souhaités lors de la création de la campagne, à l'étape [Utilisateurs ciblés]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), sélectionnez le menu déroulant **Options avancées** pour limiter vos utilisateurs. Au fur et à mesure que votre planification de réchauffement se poursuit, vous pouvez augmenter progressivement cette limite pour accroître le volume d'e-mails envoyés.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentation par sous-domaine

De nombreux fournisseurs de services Internet et fournisseurs d'accès à l'e-mail ne filtrent plus uniquement en fonction de la réputation des adresses IP. Ces technologies de filtrage prennent désormais également en compte la réputation basée sur le domaine. Cela signifie que les filtres analysent toutes les données associées au domaine de l'expéditeur et ne se limitent pas à l'adresse IP seule. Pour cette raison, en plus de réchauffer votre adresse IP, nous vous recommandons également de disposer de domaines ou sous-domaines distincts pour le marketing, les e-mails transactionnels et la messagerie d'entreprise. 

{% alert important %}
La segmentation par sous-domaine est particulièrement importante pour les expéditeurs à gros volumes. Ces expéditeurs doivent travailler avec un conseiller Braze lors de la configuration de leur compte afin de s'assurer qu'ils respectent cette pratique.
{% endalert %}

Nous vous recommandons de segmenter vos domaines de sorte que le courrier d'entreprise soit envoyé par le biais de votre domaine de premier niveau, et que le marketing et le courrier transactionnel soient envoyés par différents domaines ou sous-domaines.

## Bonnes pratiques

Vous pouvez éviter toutes les conséquences d'un manque de réchauffement d'adresses IP en suivant ces bonnes pratiques :

### Commencez par envoyer de petits volumes d'e-mails

Augmentez la quantité que vous envoyez chaque jour aussi progressivement que possible. Les campagnes e-mail abruptes et à haut volume sont considérées avec le plus grand scepticisme par les fournisseurs de services Internet. C'est pourquoi vous devez commencer par envoyer de petites quantités d'e-mails et augmenter progressivement jusqu'à atteindre le volume que vous avez l'intention d'envoyer. Gardez à l'esprit que vous réchauffez votre IP auprès de chaque fournisseur de services Internet individuellement : les fournisseurs de services Internet ne partagent pas les données de réputation entre eux. Lorsque vous planifiez vos volumes de réchauffement, veillez à ne pas augmenter le volume trop rapidement auprès d'un seul fournisseur de services Internet. Quel que soit le volume, nous vous suggérons de réchauffer votre adresse IP par précaution. Consultez la rubrique [Planifications de réchauffement d'adresses IP](#ip-warming-schedules).

### Proposez un contenu d'introduction attrayant

Assurez-vous que votre premier contenu est très engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et interagissent avec votre e-mail. Privilégiez toujours les e-mails bien ciblés plutôt que les envois massifs indiscriminés lors du réchauffement des adresses IP.

### Définissez une cadence d'envoi cohérente

Une fois le réchauffement d'adresses IP terminé, établissez une cadence d'envoi en veillant également à répartir vos e-mails sur un ou plusieurs jours. En maintenant une planification aussi régulière que possible, vous pouvez éviter un refroidissement d'adresses IP, qui peut se produire si le volume d'envoi s'arrête ou diminue considérablement pendant plus de quelques jours. 

Reportez-vous à notre [planification de réchauffement d'adresses IP](#ip-warming-schedules) pour étaler vos envois sur une période plus longue, plutôt que d'effectuer un envoi massif à un moment précis.

### Nettoyez vos listes d'e-mails

Assurez-vous que votre liste d'e-mails est propre et qu'elle ne contient pas d'adresses e-mail anciennes ou non vérifiées. L'idéal est de vous assurer que vous êtes à la fois [conforme à la CASL et à la CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Surveillez votre réputation d'expéditeur

Lors du processus de réchauffement d'adresses IP, surveillez attentivement votre réputation d'expéditeur. Il est important de suivre ces indicateurs spécifiques :
- **Taux de rebond :** Si une campagne dépasse un taux de rebond de 3 à 5 %, vous devez évaluer la propreté de votre liste en suivant les directives de notre article [Keep It Clean: The Importance of Email List Hygiene](https://www.braze.com/blog/email-list-hygiene/). En outre, vous devriez envisager de mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) afin de cesser d'envoyer des e-mails à des adresses inactives ou non sollicitées.
- **Signalements de courrier indésirable :** Si une campagne est signalée comme courrier indésirable à un taux supérieur à 0,08 %, vous devez réévaluer le contenu que vous envoyez, vérifier qu'il cible une audience intéressée et vous assurer que vos e-mails sont formulés de manière à susciter son intérêt.
- **Taux d'ouverture :** Les taux d'ouverture sont un indicateur utile du placement en boîte de réception. Si votre taux d'ouverture unique est supérieur à 25 %, vous bénéficiez probablement d'un bon placement en boîte de réception, ce qui indique une réputation positive de l'expéditeur.

{% alert tip %}
Braze vous déconseille d'utiliser le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) pour réchauffer vos adresses IP. Étant donné que les campagnes de réchauffement d'adresses IP font partie des premières campagnes que vous envoyez, Braze ne disposera pas de suffisamment d'informations sur vos utilisateurs pour calculer un moment d'envoi optimal. Dans ce cas, tous les messages avec le timing intelligent utiliseront par défaut l'heure de repli et seront envoyés en même temps.
{% endalert %}

{% alert tip %}
Il est normal que des e-mails arrivent dans le dossier spam pendant le réchauffement d'adresses IP, car votre domaine et votre IP n'ont pas encore acquis une réputation positive. Si des e-mails arrivent dans votre dossier spam, votre administrateur de messagerie devra peut-être ajouter le domaine et l'IP d'envoi de Braze à la liste d'autorisation de votre entreprise.
{% endalert %}