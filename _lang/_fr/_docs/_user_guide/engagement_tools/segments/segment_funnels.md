---
nav_title: Funnels de Segment
article_title: Funnels de Segment
page_order: 3
page_type: Référence
tool: Segments
description: "Cet article de référence explique comment utiliser Braze Segment Funnels, leurs meilleures pratiques et des exemples de cas d'utilisation."
---

# Funnels de Segment

> Cet article de référence explique comment utiliser Braze Segment Funnels, leurs meilleures pratiques et les cas d'utilisation. <br> <br> Les entonnoirs de segment sont parfaits pour rétrécir votre public pour un cas d'utilisation de campagne spécifique. en apprenant sur ce public et sur leurs interactions et en utilisant ces connaissances pour stratégier et développer des campagnes efficaces.

Les entonnoirs de segment vous permettent de voir comment chaque filtre ajouté impacte les statistiques de vos segments. Lors de la création d'un segment, une ligne de données apparaîtra sous chaque filtre. Ces données fourniront les informations suivantes aux utilisateurs qui sont ciblés par tous les filtres jusqu'à ce point :

- Nombre total d'utilisateurs ciblés et le pourcentage de votre audience de base
- LTV et LTV pour les utilisateurs payants
- Nombre d'utilisateurs par e-mail
- Nombre d'utilisateurs dans l'e-mail
- Nombre d'utilisateurs qui sont activés par push
- Nombre d'utilisateurs ayant choisi de pousser

!\[Vue d'ensemble de l'entonnoir du segment\]\[1\]

## Meilleures pratiques

- En ajoutant des filtres qui documentent votre flux d'utilisateurs, vous pouvez voir les points où les utilisateurs tombent. Par exemple, si vous êtes une application de réseau social et que vous voulez voir où vous pourriez perdre des utilisateurs pendant votre processus d'intégration, vous pouvez ajouter des filtres de données personnalisés pour vous inscrire, ajouter des amis et envoyer le premier message. Si vous trouvez que 85% des utilisateurs s'inscrivent et ajoutent des amis, mais seulement 45% ont envoyé le premier message, vous saurez alors vous concentrer sur l'encouragement des messages envoyés lors de vos campagnes d'intégration et de marketing.

- Les entonnoirs de segment vous permettent de comparer le pourcentage d'utilisateurs qui commettent différentes actions. Par exemple, les utilisateurs actifs, ou ceux ayant une haute TV LTV, [ont tendance à interagir davantage avec les messages push ou email][4]? Pour le savoir, créez un segment d'utilisateurs actifs avec un ou plusieurs filtres, puis voir comment les statistiques changent lorsque vous ajoutez un filtre pour opter pour pousser, et lorsque vous ajoutez un filtre pour vous inscrire au courriel.

- Analysez comment LTV change au fur et à mesure que vous ajoutez des filtres. Pour les utilisateurs actifs, ceux qui se connectent à Facebook ou ceux qui se connectent à Twitter ont-ils un LTV plus élevé ? Ou est-ce que LTV est beaucoup plus élevé pour ceux qui se sont connectés aux deux ? Si vous trouvez, par exemple, que la connexion à Twitter a très peu d'impact sur LTV mais la connexion à Facebook a un impact important, vous pouvez vouloir que vos campagnes de marketing se concentrent sur l'incitation aux connexions Facebook.

## Exemple de cas d'utilisation

### Impact d'une action utilisateur spécifique sur les conversions {#push-email}

En analysant l'impact d'une action d'un certain utilisateur (comme ajouter des éléments à une liste de souhaits) sur une conversion (comme faire des achats) vous pouvez répondre aux questions suivantes :

- L'action de l'utilisateur coïncide-t-elle avec plus d'achats?
- Quelle est la prévalence de l'action de l'utilisateur ? Devriez-vous créer des campagnes de marketing qui encouragent davantage cette action?

Dans l'exemple ci-dessous, tous les utilisateurs qui ont ajouté des articles à une liste de souhaits ont également fait un achat. Comme seulement un petit pourcentage d'utilisateurs ont ajouté des éléments à une liste de souhaits, cette application peut vouloir encourager davantage ce comportement par le biais de campagnes de marketing.

!\[Entonnoir de segment pour les utilisateurs\]\[3\]

### Comparer les canaux de messagerie

Créer un segment d'utilisateurs actifs (ou utilisateurs avec les traits souhaités) et comparer leurs interactions avec les différents canaux d'engagement, comme le fil d'actualité, les messages électroniques et les notifications push. Par exemple, si des utilisateurs plus fidèles sont abonnés à push, vous pouvez passer plus de temps à envoyer des campagnes utilisateur actives via push. Cependant, si vous trouvez que le LTV est plus élevé pour ceux qui sont abonnés à l'email, vous pouvez demander à des utilisateurs plus actifs de vous abonner au courriel.

!\[Entonnoir de segment pour courriel\]\[5\]
[1]: {% image_buster /assets/img_archive/segment_funnel_example.png %} [3]: {% image_buster /assets/img_archive/Wish_List_2.png %} [5]: {% image_buster /assets/img_archive/Wish_List_Email.png %}

[4]: #push-email
