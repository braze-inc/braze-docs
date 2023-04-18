---
nav_title: Politiques de temporisation 
article_title: Politiques de temporisation pour les notifications push
page_order: 3
page_type: reference
description: "Le présent article fournit les bonnes pratiques concernant la temporisation des notifications push pour un segment d’utilisateurs."
channel: push

---

# Politiques de temporisation pour les notifications push {#push-sunset-policies}

> Même lorsque vous vous assurez d’envoyer uniquement des notifications push pertinentes et opportunes, certains utilisateurs peuvent toujours ne pas y répondre et les trouver indésirables. Si un utilisateur à l’habitude d’ignorer de façon répétée vos notifications push, il est conseillé d’arrêter de leur en envoyer avant qu’ils ne s’agacent des communications de votre application ou la désinstallent complètement. Pour ce faire, créez un [politique de temporisation][1] qui finit par arrêter d’envoyer des notifications push aux utilisateurs qui n’ont pas eu d’ouverture directe ou influencée pendant une longue période. 

Avant d’arrêter d’envoyer des notifications push à un segment d’utilisateurs, vous devez fournir une notification finale qui explique pourquoi ils ne recevront plus de notification push et leur fournit la possibilité de montrer qu’ils désirent continuer à en recevoir en ouvrant cette notification. Une fois que la politique de temporisation entre en vigueur, utilisez un [message in-app][2] pour rappeler à ces utilisateurs que même s’ils ne recevront plus de notification push, les canaux de communication in-app continueront de fournir des informations intéressantes et utiles.

Bien que vous puissiez être réticents à l’idée d’arrêter d’envoyer des notifications push à des utilisateurs qui s’y étaient abonnés à l’origine, gardez à l’esprit qu’il existe d’autres canaux de messagerie qui peuvent atteindre plus efficacement ces utilisateurs, en particulier s’ils ont déjà ignoré vos notifications push. Si l’utilisateur ouvre vos e-mails, les campagnes d’e-mail sont un bon moyen de les contacter à l’extérieur de votre application. Si ce n’est pas le cas, les messages in-app sont la meilleure façon de fournir du contenu sans risquer que l’utilisateur désinstalle votre application.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/
[3]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
