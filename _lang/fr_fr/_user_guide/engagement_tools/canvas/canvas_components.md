---
nav_title: Composants Canvas
article_title: Composants Canvas
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Composants Canvas"
guide_top_text: "Améliorez votre parcours Canvas avec les composants Canvas. Les composants Canvas peuvent être utilisés pour simplifier le processus d’évaluation de l’efficacité de votre Canvas en remplaçant les étapes superflues par une seule étape. Les composants du Canvas font référence au parcours utilisateur personnalisé dans les branches du Canvas."

page_type: landing
description: "Cette page d’accueil contient les articles de composant Canvas qui vous permettront de créer des canvas optimisés. Certains de ces composants comprennent l’étape de message, de délai, de la décision de séparation, etc."
tool: Canvas

guide_featured_title: "Section Articles"
guide_featured_list:
  - name: Étape Message
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Étape de délai
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: "Étape d'arbre décisionnel"
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Étape de parcours d’audience
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Étape de parcours d’action  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Étape des chemins d’expérience
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Étape de mise à jour de l’utilisateur
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Drapeaux de fonctionnalité dans Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Synchronisation d’audience Canvas
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## À propos des composants Canvas

Avec les composants Canvas, vous pouvez débloquer de nouveaux parcours utilisateurs pour améliorer votre processus et améliorer l’efficacité de la sensibilisation de votre audience.

### Parcours utilisateur de Customizing

![Exemple d'un parcours utilisateur Canvas avec une étape de l'arbre décisionnel suivie d'étapes de délai et de message.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utilisez les [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) pour diviser votre parcours utilisateur en fonction des actions et des événements d'engagement tels que la réalisation d'un achat. Si vous souhaitez filtrer et cibler vos audiences, les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) permettent de simplifier le ciblage des utilisateurs en leur faisant suivre différents parcours canvas en fonction de critères d'audience.

Les composants d'[arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) utilisent une simple logique "oui ou non" pour créer deux parcours mutuellement exclusifs pour vos voyages d'utilisateurs qui sont basés sur une action ou un attribut de l'utilisateur. Ce processus permet d’identifier et de cibler vos groupes d’utilisateurs.

Les composants de [retardement]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) vous permettent de retarder une seule étape de votre canvas. Cette étape de délai indépendante dans votre Canvas est plutôt utilisée pour transmettre des messages à vos utilisateurs à un moment précis. De plus, les composants de délai peuvent également élargir votre audience en lui offrant plus de temps pour répondre aux critères du composant.

### Test

Lorsque vous créez vos parcours utilisateur, vous pourriez également tester le parcours Canvas le plus efficace. Avec les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step), vous pouvez tester plusieurs chemins Canvas à n'importe quelle étape. Vous pouvez également utiliser les connexions entre les étapes comme un aperçu de haut niveau. Les connexions orange indiquent que l'étape précédente permet aux utilisateurs de passer immédiatement à l'étape suivante.

### Intégration

Vous souhaitez effectuer une synchronisation avec les données utilisateur internes de votre marque ? Tirez parti des options de synchronisation d'audience disponibles pour [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) et [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

