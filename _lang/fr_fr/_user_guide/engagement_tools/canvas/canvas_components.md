---
nav_title: Composants de la toile
article_title: Composants de la toile
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Composants de la toile"
guide_top_text: "Améliorez votre parcours dans Canvas avec les composants Canvas. Les composants de Canvas peuvent être utilisés pour simplifier le processus de détermination de l'efficacité de votre Canvas en remplaçant des étapes complètes excessives par une seule. Les composants dans Canvas font référence au parcours personnalisé de l'utilisateur dans vos branches Canvas."

page_type: landing
description: "Cette page d'atterrissage contient des articles sur les composants de Canvas qui vous aideront à créer des Canvas plus avancés. Parmi ces éléments, citons l'étape du message, l'étape du délai, l'étape de l'arbre décisionnel, etc."
tool: Canvas

guide_featured_title: "Articles de section"
guide_featured_list:
  - name: Étape du message
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Pas de retard
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: "Étape de l'arbre décisionnel"
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: "Parcours d'audience Étape"
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: "Parcours d'action Étape"  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: "étape des chemins d'expérience"
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: "Étape de mise à jour de l'utilisateur"
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Drapeaux de fonctionnalité dans Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "Synchronisation de l'audience de Canvas"
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## À propos des composants de Canvas

Grâce aux composants Canvas, vous pouvez débloquer de nouveaux parcours utilisateurs pour améliorer votre processus et accroître l'efficacité de la sensibilisation de votre audience.

### Personnaliser les parcours clients

Exemple d'un parcours utilisateur Canvas avec une étape décisionnelle suivie d'étapes de délai et d'envoi de messages.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utilisez les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) pour diviser votre parcours utilisateur en fonction des actions et des événements d'engagement tels que la réalisation d'un achat. Si vous souhaitez filtrer et cibler vos audiences, les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) permettent de simplifier le ciblage des utilisateurs en leur faisant suivre différents parcours canvas en fonction de critères d'audience.

Les composants d'[arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) utilisent une simple logique "oui ou non" pour créer deux parcours mutuellement exclusifs pour vos voyages d'utilisateurs qui sont basés sur une action ou un attribut de l'utilisateur. Cela peut aider à identifier et à cibler vos groupes d'utilisateurs.

Les composants de [retardement]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) vous permettent de retarder une seule étape de votre canvas. Cette étape du canvas est utilisée pour envoyer des messages à vos utilisateurs à un moment précis. En outre, les composants de délai peuvent également augmenter la portée de votre audience en donnant plus de temps à votre audience pour répondre aux critères du composant.

### Essais

Lorsque vous créez vos parcours utilisateurs, vous pouvez également tester le parcours Canvas le plus efficace. Avec les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step), vous pouvez tester plusieurs chemins Canvas à n'importe quelle étape. Vous pouvez également utiliser les connexions entre les étapes comme un aperçu de haut niveau. Les connexions orange indiquent que l'étape précédente permet aux utilisateurs de passer immédiatement à l'étape suivante.

### Intégration

Vous souhaitez vous synchroniser avec les données first-party des utilisateurs de votre marque ? Tirez parti des options de synchronisation d'audience disponibles pour [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) et [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

