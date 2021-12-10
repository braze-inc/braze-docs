---
nav_title: Réchauffement IP
article_title: Réchauffement IP
page_order: 5
page_type: Référence
description: "Cet article de référence couvre le thème du réchauffement de la propriété intellectuelle et des meilleures pratiques."
channel: Email
---

# Le réchauffement IP

## Qu'est-ce que le réchauffement de la propriété intellectuelle ?

IP Warming est la pratique consistant à obtenir des fournisseurs de messagerie électronique utilisés pour recevoir des messages à partir de vos adresses IP dédiées. C'est une partie extrêmement importante de l'envoi de courriels avec n'importe quel fournisseur de service de messagerie et la pratique standard à Braze pour s'assurer que vos messages arrivent à leur boîte de réception à un taux constamment élevé.

Le chauffage par IP est conçu pour vous aider à établir une réputation positive auprès des FAI (fournisseurs de services Internet). Chaque fois qu'une nouvelle adresse IP est utilisée pour envoyer un e-mail, Les FAI surveillent par programme ces courriels pour vérifier qu'ils ne sont pas utilisés pour envoyer des pourriels aux utilisateurs.

## Que se passe-t-il si je n'ai pas le temps de réchauffer les adresses IP?

__Il faut chauffer l'IP.__ Si vous ne réussissez pas à réchauffer les adresses IP de manière appropriée, et le schéma de votre e-mail est source de suspicion, tout ou partie des éléments suivants peuvent se produire :

1. __Votre vitesse d'envoi de courrier électronique pourrait être considérablement réduite ou ralentie.__
      - Les FAI limitent l'envoi de courriels lorsque des soupçons de spam se font jour afin qu'ils puissent protéger leurs utilisateurs. Par exemple, si vous envoyez 100000 utilisateurs, le FAI peut envoyer le courriel à 5000 utilisateurs seulement au cours de la première heure. Le FAI surveille ensuite les mesures d'engagement telles que les taux d'ouverture, les taux de clic, les désinscriptions et les rapports de spam.
      - Si un nombre significatif de signalements de spam se produisent, ils peuvent choisir de reléguer le reste de cet envoi dans le dossier spam plutôt que de le livrer dans la boîte de réception de l'utilisateur.
      - Si l'engagement est modéré, ils peuvent continuer à restreindre votre e-mail pour collecter plus de données d'engagement pour déterminer si le courrier est ou non spam avec plus de certitude.
      - Si le courriel comporte des mesures d’engagement très élevées, il peut cesser d’étouffer complètement ce courriel. Ils utilisent ces données pour créer une réputation de courrier électronique qui déterminera éventuellement si vos courriels sont automatiquement filtrés ou non.<br><br>
2. __Votre domaine et ou votre IP pourraient être mis sur liste noire par les FAI, à quel moment tous vos courriels commenceront à aller directement dans le dossier spam de la boîte de réception de votre utilisateur.__
  - Si cela se produit, les codes de réponse dans la __Braze Developer Console__ contiendront des informations sur les sites Web à visiter pour appeler ces FAI à les supprimer.

## Meilleures pratiques de réchauffement de la propriété intellectuelle

Toutes les conséquences ci-dessus sont entièrement évitables si vous suivez les directives suivantes :

1. __Commencez par envoyer de petits volumes d'e-mail et augmentez le montant que vous envoyez chaque jour le plus graduellement possible. _<br> Les campagnes e-mail à volume élevé et aberrantes sont considérées avec le plus de scepticisme par les FAI. Par conséquent, vous devriez commencer par envoyer de petites quantités de courriels et graduellement vers le volume de courriels que vous avez l'intention d'envoyer en fin de compte. Indépendamment du volume, nous vous suggérons de réchauffer votre adresse IP pour être sûr. Veuillez consulter le calendrier ci-dessous pour plus de détails.<br><br>
2. __Assurez-vous que votre premier contenu est hautement engageant et maximise la probabilité que les utilisateurs cliquent, ouvrent et engagent avec votre email. _<br>Préférez toujours les courriels bien ciblés aux explosions aveugles lors du réchauffement des IP.<br><br>
3. __Lorsque le réchauffement IP est terminé, continuez à envoyer une cadence aussi constante que possible. _<br> Les IP peuvent se refroidir si le volume s'arrête ou diminue significativement pendant plus de quelques jours.<br><br>
4. __Répandez vos envois de courriels sur une journée ou plusieurs jours. _<br> Des fonctionnalités comme la livraison du fuseau horaire local de Braze et le [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) peuvent vous aider à répartir automatiquement votre envoi sur une période plus longue, plutôt que d'envoyer une projection de masse à un seul moment précis.<br><br>
5. __Assurez-vous que votre liste de courriels est propre et qu'elle n'a pas d'e-mails anciens ou non vérifiés. _<br>S'assurer que vous êtes à la fois [conforme à CASL- et au CAN-SPAM][40] est idéal.<br><br>
6. __Surveille soigneusement votre réputation de l'expéditeur pendant que vous menez le processus de réchauffement IP.__ <br> Les mesures suivantes sont importantes à surveiller pendant le réchauffement :
- __Taux de rebond__: Si une campagne rebondit à plus de 3-5%, vous devriez évaluer la propreté de votre liste en suivant les directives de notre article ["Garder propre : L'importance de la liste d'e-mails Hygiène"][43]. De plus, vous devriez envisager de mettre en œuvre une [politique de Sunset][46] pour arrêter d'envoyer des courriels non engagés ou dormants.
- __Rapports Spam__: Si une campagne est signalée comme spam à un taux supérieur à 0. 8%, vous devriez réévaluer le contenu que vous envoyez, vous assurer qu'il s'adresse à un public intéressé, et assurez-vous que vos courriels sont bien formulés pour pique leur intérêt.
- __Scores de réputation de l'expéditeur__: Les services suivants sont utiles pour vérifier la progression de votre réputation : [SenderScore de RetournPath's][44] & Port de fer de Cisco [SenderBase][45]

## Planification du réchauffement IP

Nous vous recommandons fortement de respecter strictement ce calendrier de réchauffement de la propriété intellectuelle afin d’assurer la délivrabilité. Il est également important que vous ne sautiez pas les jours car la mise à l'échelle constante améliore la livrabilité.

| Jour | # d'emails à envoyer                         |
| ---- | --------------------------------------------- |
| 1    | 50                                            |
| 2    | 100                                           |
| 3    | 500                                           |
| 4    | 1,000                                         |
| 5    | 5,000                                         |
| 6    | 10,000                                        |
| 7    | 20,000                                        |
| 8    | 40,000                                        |
| 9    | 70,000                                        |
| 10   | 100,000                                       |
| 11   | 150,000                                       |
| 12   | 250,000                                       |
| 13   | 400,000                                       |
| 14   | 600,000                                       |
| 15   | 1,000,000                                     |
| 16   | 2,000,000                                     |
| 17   | 4,000,000                                     |
| 18+  | Double volume quotidien jusqu'à volume désiré |

Une fois que le réchauffement est terminé et que vous avez atteint le volume quotidien souhaité, vous devriez vous efforcer de maintenir ce volume tous les jours. Certaines fluctuations sont correctes, mais atteignent le volume souhaité, alors seulement faire une explosion de masse une fois par semaine peut nuire à votre délivrabilité et à votre réputation de l'expéditeur. Enfin, la plupart des FAI ne stockent des données de réputation que pendant 30 jours. Si vous passez un mois sans envoi, vous devrez répéter le processus de réchauffement de la propriété intellectuelle.

## Comment limiter les envois pendant le réchauffement

La fonction de limitation des utilisateurs intégrée de Braze est un outil utile pour vous aider à réchauffer votre adresse IP. Après avoir choisi vos segments de messagerie lors de la création de la campagne, à l'étape [Utilisateurs cibles]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-5-choose-your-target-segment) sélectionnez le menu déroulant __Options avancées__ pour limiter vos utilisateurs. Au fur et à mesure que votre planning de réchauffement se poursuit, vous pouvez augmenter progressivement cette limite pour augmenter le volume de courriels que vous envoyez.

!\[Limiter les utilisateurs\]\[18\]

## Segmentation de sous-domaine

De nombreux FAI et fournisseurs d'accès aux courriels ne filtrent plus seulement par la réputation de l'adresse IP. Ces technologies de filtrage font désormais également partie de la réputation des domaines.  Cela signifie que les filtres examineront toutes les données associées au domaine de l'expéditeur et pas seulement l'adresse IP. Pour cette raison, en plus de réchauffer votre adresse IP, nous vous recommandons d'avoir des domaines ou des sous-domaines distincts pour le marketing, la transaction et le courrier d'entreprise. Nous vous recommandons de segmenter vos domaines de telle sorte que le courrier d'entreprise soit envoyé par votre domaine de premier niveau, et le marketing et le courrier transactionnel sont envoyés par différents domaines ou sous-domaines.

{% alert important %}
La segmentation du sous-domaine est particulièrement importante pour les expéditeurs de gros volumes. Ces expéditeurs devraient travailler avec un représentant de Braze pour établir leur compte afin de s'assurer qu'ils adhèrent à cette pratique.
{% endalert %}
[18]: {% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %}

[40]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[43]: https://www.braze.com/blog/email-list-hygiene/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
