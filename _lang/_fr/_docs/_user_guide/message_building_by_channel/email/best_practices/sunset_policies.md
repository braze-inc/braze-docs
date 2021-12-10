---
nav_title: Politiques du coucher du soleil
article_title: Politiques du coucher du soleil pour les e-mails
page_order: 8
page_type: Référence
description: "Cet article couvre les meilleures pratiques entourant les politiques de mise en scène, en comprenant les situations où il est préférable d'arrêter les messages aux utilisateurs désengagés."
channel: Email
---

# Règles de Sunset pour les e-mails

Bien que vous puissiez être tenté d'envoyer des campagnes à autant d'utilisateurs que vous le pouvez, il y a des situations où il est vraiment sage d'arrêter les messages aux utilisateurs désengagés.  Par exemple, dans le cas des courriels, votre adresse IP a une note de réputation qui tient compte de l'engagement, du signalement de spam, de la liste noire, etc. Il existe de nombreux outils gratuits pour surveiller votre score de réputation IP, tels que [Sender Score](https://www.senderscore.org/ "Sender Score") ou [Outlook Smart Network Data Service](https://postmaster.live.com/snds/ "Outlook's Smart Network Data Service"). Si votre score de réputation est constamment faible, Les filtres de FSI et de boîte aux lettres peuvent automatiquement trier vos e-mails dans un dossier de spam ou de faible priorité pour tous les destinataires, même ceux engagés.  Pour éviter que cela ne se produise, vous devez créer une politique de couplage de soleil qui veille à ce que vos e-mails ne soient pas envoyés à des destinataires inactifs. Les filtres de segmentation de Braze aident à empêcher votre messagerie d'apparaître comme spam ou non pertinent en vous permettant d'implémenter facilement des politiques de couperet pour les e-mails, pushes, notifications dans l'application et cartes de flux d'actualités

Voici quelques choses à considérer lorsque vous créez une politique de coucher du soleil:

- Qu'est-ce qui compte comme un utilisateur "sans engagement" ? L'engagement est-il défini par les clics et les ouvertures, les achats, l'utilisation de l'application, ou une combinaison de ces comportements ?
- Combien de temps faudra-t-il pour que vous cessiez d'envoyer des messages ?
- Allez-vous livrer des campagnes spéciales aux utilisateurs avant de les exclure de vos segments ?
- À quels canaux de messagerie votre politique de coucher de soleil s'applique-t-elle ?

Intégrer les politiques de couché du soleil dans vos campagnes, [créez des segments][19] qui excluent automatiquement les utilisateurs qui ont marqué vos e-mails comme spam ou qui n'ont pas interagi avec vos messages pendant une certaine période de temps.

Pour configurer ces segments, choisissez les filtres « Vous a marqué comme spam » et/ou « Dernier message avec message », qui sont situés dans la section **Activité Marketing** dans le menu déroulant du filtre.  Lorsque vous appliquez le filtre "Last Engaged With Message", spécifiez le type de messagerie (push, email, etc.). ou une notification dans l'application) avec laquelle l'utilisateur a ou n'a pas interagi, ainsi que le nombre de jours écoulés depuis la dernière interaction. Après avoir créé un segment, choisissez de cibler ce segment avec n'importe quel canal de messagerie []({{site.baseurl}}/user_guide/message_building_by_channel/).

!\[Page de détails du segment avec le filtre "Dernière Engagée avec Message" sélectionné\]\[20\]

Alors que la plateforme Braze cesse automatiquement d'envoyer des e-mails aux utilisateurs qui vous ont marqué comme spams, le filtre "A marqué comme Spam" vous permet également d'envoyer à ces utilisateurs des messages push ciblés, des notifications dans l'application et des cartes de News Feed.  Ce filtre est utile pour [campagnes de reciblage][21] - par exemple, vous pouvez envoyer des messages aux utilisateurs non engagés ou des mises à jour des fils d'actualités qui leur rappellent les fonctionnalités et les offres sur lesquelles ils manquent quand ils n'ouvrent pas vos e-mails.

Les politiques Sunset peuvent être particulièrement utiles dans les campagnes de courriel qui ciblent les utilisateurs qui sont en train de disparaître.  Alors que ces campagnes se concentrent sur des segments qui n'ont pas interagi avec votre application pendant une période de temps, ils peuvent mettre en péril la délivrabilité de vos courriels s'ils incluent à plusieurs reprises des destinataires non engagés. Les règles de Sunset vous permettent de cibler les utilisateurs qui sont en train d'arriver sans atterrir dans le dossier spam.
[20]: {% image_buster /assets/img_archive/email_sunset_policies_new.png %}

[19]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
