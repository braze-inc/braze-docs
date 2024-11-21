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
    link: /docs/developer_guide/platform_wide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Synchronisation d’audience Canvas
    link: /docs/partners/canvas_steps/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## À propos des composants Canvas

Avec les composants Canvas, vous pouvez débloquer de nouveaux parcours utilisateurs pour améliorer votre processus et améliorer l’efficacité de la sensibilisation de votre audience.

{% alert important %}
À compter du 28 février 2023, vous ne pourrez plus créer ou dupliquer de canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% endalert %}

### Parcours utilisateur de Customizing

![]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utilisez les [parcours d'action][1] pour diviser votre parcours utilisateur en fonction des actions et des événements d'engagement tels que la réalisation d'un achat. Si vous souhaitez filtrer et cibler vos audiences, les [parcours d'audience][2] permettent de simplifier le ciblage des utilisateurs en leur faisant suivre différents parcours canvas en fonction de critères d'audience.

Les composants d'[arbre décisionnel][3] utilisent une simple logique "oui ou non" pour créer deux parcours mutuellement exclusifs pour vos voyages d'utilisateurs qui sont basés sur une action ou un attribut de l'utilisateur. Ce processus permet d’identifier et de cibler vos groupes d’utilisateurs.

Les composants de [retardement][4] vous permettent de retarder une seule étape de votre canvas. Cette étape de délai indépendante dans votre Canvas est plutôt utilisée pour transmettre des messages à vos utilisateurs à un moment précis. De plus, les composants de délai peuvent également élargir votre audience en lui offrant plus de temps pour répondre aux critères du composant. 

### Test
Lorsque vous créez vos parcours utilisateur, vous pourriez également tester le parcours Canvas le plus efficace. Avec les [chemins d'expérience][5], vous pouvez tester plusieurs chemins Canvas à n'importe quelle étape. 

### Intégration 
Vous souhaitez effectuer une synchronisation avec les données utilisateur internes de votre marque ? Tirez parti des options de synchronisation d'audience disponibles pour [Facebook][6] et [Google][7]. <br><br>

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split
[4]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {{site.baseurl}}/partners/canvas_steps/facebook_audience_sync
[7]: {{site.baseurl}}/partners/canvas_steps/google_audience_sync