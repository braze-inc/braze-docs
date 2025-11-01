---
nav_title: Conventions de dénomination des événements
article_title: Conventions de dénomination des événements
page_order: 10
page_type: reference
description: "Cet article de référence couvre les conventions de dénomination des événements et les meilleures pratiques."

---

# Conventions de dénomination des événements

> Cette page traite des conventions de dénomination des événements et des meilleures pratiques. En maintenant la cohérence de votre taxonomie d'événements et d'attributs, vous garderez vos données propres et utilisables pour les utilisateurs nouveaux et existants de la plateforme Braze. Cela permet d'éviter des problèmes ultérieurs, comme le déclenchement d'une campagne auprès de la mauvaise audience ou la génération de mauvais résultats après avoir utilisé le mauvais événement.

## Meilleures pratiques

- Veillez à ce que votre convention d'appellation soit claire.
- Utilisez des majuscules et un formatage cohérents pour les noms d'événements.
- Évitez de donner des noms similaires aux événements.
- Évitez les longues chaînes de caractères d'attributs d'événements, qui seront tronquées ou coupées dans le tableau de bord de Braze.

## Conventions d'appellation

### Utiliser des groupes d'événements

Utilisez des groupes pour différencier les parties de votre produit afin de nommer les événements. En classant votre produit par catégories, tout utilisateur peut clairement comprendre à quoi l'événement fait référence et ce qu'il fait.

### Structure de dénomination des événements

La structure de dénomination la plus courante est `group_noun_action`. Les événements doivent tous être en minuscules afin d'éviter les erreurs d'instrumentation et d'identification des propriétés.

### Propriétés

Étiquetez un événement, puis identifiez les différences à l'aide des propriétés. Ceci est utile pour les événements qui sont intrinsèquement les mêmes mais qui présentent des différences mineures, comme les canaux d'une campagne. Nous pouvons également voir facilement comment les utilisateurs passent d'un événement à l'autre. Reportez-vous à l'[objet propriétés d'événement]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) pour un exemple et un contexte supplémentaire.

## Exemples

Imaginons que vous fassiez partie d'une entreprise de commerce électronique et que vous souhaitiez savoir quand les clients se sont inscrits à votre application et quand ils se sont abonnés à votre lettre d'information. Voici des exemples de noms d'événements efficaces :

- `user_signup`
- `newsletter_subscribed`

Ces deux noms d'événements indiquent clairement l'événement qu'ils suivent. Au fur et à mesure que vous créez des événements personnalisés, veillez à ce que vos conventions d'appellation restent compréhensibles. Par exemple, évitez d'utiliser des noms d'événements tels que `signup_event_1`, car ils manquent de clarté et n'indiquent pas ce que l'événement est en train de suivre, contrairement à `user_signup`.
