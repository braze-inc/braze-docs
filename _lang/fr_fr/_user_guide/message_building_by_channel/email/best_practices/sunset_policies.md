---
nav_title: Politiques de temporisation 
article_title: Politiques de temporisation des e-mails
page_order: 8
page_type: reference
description: "Le présent article couvre les meilleures pratiques en matière de temporisation et décrit les situations dans lesquelles il vaut mieux arrêter d’envoyer des communications à des utilisateurs désengagés."
channel: email

---

# Politiques de temporisation

> Bien sûr, il est parfois tentant d’envoyer des campagnes à autant d’utilisateurs que possible, mais il existe des situations où il vaut vraiment mieux arrêter d’envoyer des messages aux utilisateurs désengagés. 

Pour les e-mails, votre adresse IP d’envoi a un score de réputation basé sur l’engagement, le signalement de spam, les blocages, etc. Vous pouvez utiliser des outils tels que [Sender Score](https://www.senderscore.org/) ou le [Smart Network Data Service d'Outlook](https://postmaster.live.com/snds/) pour surveiller votre score de réputation. Si votre score de réputation est constamment faible, les filtres de fournisseurs de services Internet et boîte aux lettres peuvent envoyer automatiquement vos e-mails dans un dossier spam ou à faible priorité pour tous les destinataires, même ceux qui sont engagés. La création d'une politique de temporisation permet d'envoyer vos e-mails uniquement aux destinataires actifs. 

Les filtres de segmentation permettent d'éviter que vos messages n'apparaissent comme du spam en vous permettant de mettre facilement en œuvre des politiques de temporisation pour les e-mails, les notifications push et les notifications in-app. Voici quelques éléments à prendre en compte en créant une politique de temporisation

- Comment définit-on un utilisateur « non engagé » ? 
- L’engagement est-il défini par des clics, des achats, l’utilisation de l’appli ou une combinaison de ces comportements ? 
- Quelle durée d’inactivité avant d’arrêter d’envoyer des messages ?
- Allez-vous envoyer des campagnes spéciales aux utilisateurs avant de les exclure de vos segments ?
- À quels canaux de messagerie votre politique de temporisation sera-t-elle appliquée ? 

Par exemple, si vous avez des utilisateurs qui optent pour la [protection de la confidentialité dans Mail (MPP) d'Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), réfléchissez à l'impact que cela peut avoir sur vos campagnes d'e-mail et vos indicateurs de livrabilité et déterminez la meilleure façon de structurer votre politique de temporisation.

Pour intégrer les politiques de temporisation dans vos campagnes, créez un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) qui exclut automatiquement les utilisateurs qui ont marqué vos e-mails comme étant des spams ou qui n'ont pas interagi avec vos messages pendant une certaine période.  

Pour configurer ces segments, choisissez les filtres `Has Marked You As Spam` et `Last Engaged With Message` situés dans la section **reciblage** dans le menu déroulant des filtres. 

Lorsque vous appliquez le filtre `Last Engaged With Message`, spécifiez le type de message (push, e-mail ou notification in-app) avec lequel l’utilisateur a ou n’a pas interagi, ainsi que le nombre de jours depuis la dernière interaction avec l’utilisateur. Après avoir créé un segment, choisissez de cibler ce segment avec n'importe quel [canal de communication]({{site.baseurl}}/user_guide/message_building_by_channel/).

![Page des détails du segment avec le filtre "Dernier envoi de message" sélectionné.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Alors que Braze arrête automatiquement d'envoyer des e-mails aux utilisateurs qui vous ont marqué comme spam, le filtre `Has Marked You As Spam` vous permet d'envoyer également à ces utilisateurs des messages push ciblés et des notifications in-app. Ce filtre est utile pour les [campagnes de reciblage]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Par exemple, vous pouvez envoyer aux utilisateurs désengagés des messages pour leur rappeler les fonctionnalités ou offres qu’ils manquent quand ils n’ouvrent pas vos e-mails.

Les politiques de temporisation peuvent être particulièrement utiles dans les campagnes par e-mail qui ciblent les utilisateurs inactifs. En effet, ces campagnes se concentrent sur des segments qui n’ont pas interagi avec votre application depuis un certain temps, et elles peuvent avoir un impact sur la livrabilité de vos e-mails si vous incluez systématiquement des utilisateurs désengagés. Les politiques de temporisation vous permettent de cibler les utilisateurs inactifs sans terminer dans le dossier Courrier Indésirables.

