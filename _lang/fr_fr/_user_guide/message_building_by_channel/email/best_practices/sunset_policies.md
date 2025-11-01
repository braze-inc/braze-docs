---
nav_title: Politiques de temporisation
article_title: "Politiques de temporisation pour l'e-mail"
page_order: 8
page_type: reference
description: "Cet article traite des meilleures pratiques concernant les politiques de temporisation et de la compréhension des situations dans lesquelles il est préférable d'interrompre les messages destinés aux utilisateurs désengagés."
channel: email

---

# Politiques de temporisation

> Bien que vous puissiez être tenté d'envoyer des campagnes à autant d'utilisateurs que possible, il y a des situations où il est en fait avantageux d'arrêter les messages aux utilisateurs désengagés. 

Pour les e-mails, votre IP d'envoi a un score de réputation qui prend en compte l'engagement, le signalement de courrier indésirable, la mise en liste de blocage, etc. Vous pouvez utiliser des outils tels que [Sender Score](https://www.senderscore.org/) ou le [Smart Network Data Service d'Outlook](https://postmaster.live.com/snds/) pour surveiller votre réputation. Si votre score de réputation est constamment bas, les filtres des FAI et des boîtes aux lettres risquent de classer automatiquement vos e-mails dans un dossier spam ou de faible priorité pour tous les destinataires, même ceux qui sont engagés. La création d'une politique de temporisation permet d'envoyer vos e-mails uniquement aux destinataires actifs. 

Les filtres de segmentation permettent d'éviter que vos messages n'apparaissent comme du spam en vous permettant de mettre facilement en œuvre des politiques de temporisation pour les e-mails, les notifications push et les notifications in-app. Voici quelques éléments à prendre en compte lors de l'élaboration d'une politique de temporisation :

- Qu'est-ce qu'un utilisateur "non engagé" ? 
- L'engagement est-il défini par les clics, les achats, l'utilisation de l'application ou une combinaison de ces comportements ? 
- Combien de temps doit durer l'interruption de l'engagement pour que vous cessiez d'envoyer des messages ?
- Allez-vous mener des campagnes spéciales auprès des utilisateurs avant de les exclure de vos segmentations ?
- À quels canaux de communication votre politique de temporisation s'appliquera-t-elle ? 

Par exemple, si vous avez des utilisateurs qui optent pour la [protection de la confidentialité dans Mail (MPP) d'Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), réfléchissez à l'impact que cela peut avoir sur vos campagnes d'e-mail et vos indicateurs de livrabilité et déterminez la meilleure façon de structurer votre politique de temporisation.

Pour intégrer les politiques de temporisation dans vos campagnes, créez un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) qui exclut automatiquement les utilisateurs qui ont marqué vos e-mails comme étant des spams ou qui n'ont pas interagi avec un de vos messages pendant une certaine période.  

Pour configurer ces segments, choisissez les filtres `Has Marked You As Spam` et `Last Engaged With Message` situés dans la section **reciblage** dans le menu déroulant des filtres. 

Lorsque vous appliquez le filtre `Last Engaged With Message`, indiquez le type d'envoi de messages (push, e-mail ou notification in-app) avec lequel l'utilisateur a ou n'a pas interagi, ainsi que le nombre de jours écoulés depuis la dernière interaction de l'utilisateur. Après avoir créé un segment, choisissez de cibler ce segment avec n'importe quel [canal de communication.]({{site.baseurl}}/user_guide/message_building_by_channel/)

!page de détails du segment avec le filtre "Dernier envoi de message" sélectionné.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Alors que Braze arrête automatiquement d'envoyer des e-mails aux utilisateurs qui vous ont marqué comme spam, le filtre `Has Marked You As Spam` vous permet d'envoyer également à ces utilisateurs des messages push ciblés et des notifications in-app. Ce filtre est utile pour les [campagnes de reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Par instance, vous pouvez envoyer aux utilisateurs non engagés des messages qui leur rappellent les fonctionnalités et les offres qu'ils manquent lorsqu'ils n'ouvrent pas vos e-mails.

Les politiques de temporisation peuvent être particulièrement utiles dans les campagnes d'e-mailing qui ciblent les utilisateurs en fin de droits. Bien que ces campagnes se concentrent sur des segments qui n'ont pas interagi avec votre appli pendant un certain temps, elles peuvent mettre en péril la livrabilité de vos e-mails si elles incluent de manière répétée des destinataires non engagés. Les politiques de temporisation vous permettent de cibler les utilisateurs en voie de temporisation sans atterrir dans le dossier spam.

