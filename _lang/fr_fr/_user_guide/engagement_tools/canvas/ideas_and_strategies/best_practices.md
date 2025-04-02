---
nav_title: Bonnes pratiques
article_title: Bonnes pratiques relatives à Canvas
page_order: 1
description: "Cet article présente une partie des bonnes pratiques pour la création et la personnalisation des parcours utilisateurs avec Canvas et Canvas Flow."
tool: Canvas

---

# Bonnes pratiques relatives à Canvas

> Cet article présente une partie des bonnes pratiques pour la création et la personnalisation des parcours utilisateurs avec Canvas et Canvas Flow.

## Identifiez votre but

Plongez-vous dans le quoi, le qui et le pourquoi !
- Qu’essayez-vous d’aider les utilisateurs à accomplir ?
- Quels sont les utilisateurs que vous désirez atteindre ?
- Pourquoi créez-vous ce Canvas ?

## Combinez

Débloquez de nouvelles combinaisons de parcours utilisateurs grâce aux [composants Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Divisez vos utilisateurs avec [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) et créez des flux de travail différents.
- Échelonnez vos parcours utilisateurs avec une étape [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
- Ajoutez des [messages autonomes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) où vous le souhaitez dans votre flux Canvas. 

## Créer des messages enrichis

Attirez vos utilisateurs avec des messages enrichis.

- Créez des [messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) pour les canvas d'onboarding afin de tirer le meilleur parti de votre première impression.
- Introduisez les [cartes de contenu]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) dans un parcours Canvas pour les offres promotionnelles et les notifications push.

## Tester vos parcours utilisateurs

Déterminez l’impact de vos envois de message Canvas en ajoutant des groupes de contrôle. Vous pouvez ainsi comprendre comment votre Canvas a été reçu !

- Donnez un nom à chaque étape de votre Canvas pour identifier votre parcours utilisateur.
- Exploitez le composant [Chemins d'expérience de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) votre parcours utilisateur pour affecter de manière aléatoire les utilisateurs aux différents chemins que vous créez. 
- Diversifiez vos parcours utilisateurs avec des étapes de délais et de messages pour essayer de trouver le parcours le plus efficace.
- Consultez l'[analyse/analytique de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) pour connaître les performances de chaque composant de votre parcours utilisateur.
- [Modifiez votre canvas]({{site.baseurl}}/post-launch_edits/) après le lancement initial.

## Planification de vos toiles

{% alert note %}
Canvas vous empêchera d'utiliser l'envoi planifié avec une heure déjà passée. Toutefois, il est possible de lancer un Canvas exactement à la minute où la campagne est planifiée (ou dans les secondes qui précèdent). Cela peut conduire à ce que le canvas ne soit pas saisi à l'heure prévue et à ce que les utilisateurs n'entrent pas dans le canevas. Nous vous recommandons d'envoyer les canevas immédiatement au cas où des campagnes seraient modifiées dans les minutes qui suivent l'heure d'envoi prévue.
{% endalert %}

Pour les étapes du canvas, tenez compte des détails suivants lors de la planification de votre canvas :

- Les changements de planification ne s'appliqueront qu'aux utilisateurs qui ne sont pas déjà en attente de recevoir l'étape.
- Les changements d'audience s'appliquent par défaut à tous les utilisateurs, sauf si vous planifiez les changements pour qu'ils s'appliquent aux utilisateurs qui n'attendent pas de recevoir l'étape.
- Si vous modifiez un canvas dont la planification prévoit une livraison dès qu'il est déployé et que vous sélectionnez **Mettre à jour**, il sera essentiellement envoyé.
