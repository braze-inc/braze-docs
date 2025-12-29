---
nav_title: Lancement avec le flux Canvas
article_title: Lancement avec Canvas Flow
page_order: 3
description: "Cet article de référence explique comment préparer et tester un canvas créé avec Canvas Flow avant son lancement."
page_type: reference
tool: Canvas
---

# Lancement avec Canvas Flow

> Cet article de référence explique comment préparer et tester un canvas créé à l'aide de Canvas Flow avant son lancement. Il s'agit notamment d'identifier les points de contrôle Canvas importants, tels que les conditions d'entrée dans Canvas, les résumés d'audience et les segments d'utilisateurs.

Alors que vous vous préparez à lancer votre Canvas, Braze vous recommande de vérifier votre Canvas à chaque étape du générateur de Canvas pour les paramètres qui peuvent avoir un impact sur l'envoi de votre message, notamment :
* [Conditions de concurrence](#race-conditions)
* [Délais de réception/distribution](#delivery-times)
* [Segments d'utilisateurs](#segment-users)

## Conditions de concurrence 

Prenez en compte les [conditions de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) susceptibles de se produire avant de lancer votre Canvas. 

Pour entrer dans un Canvas, les utilisateurs doivent se trouver dans l'audience d'entrée avant que la planification d'entrée ne se produise, que le Canvas soit planifié, basé sur une action ou déclenché par l'API. 

Un canvas basé sur l'action qui entre dans les utilisateurs lorsqu'ils effectuent un achat pendant l'heure locale de l'utilisateur du 30 avril 2025 à 12 heures au 7 mai 2025 à 12 heures.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Notez que les utilisateurs qui se qualifient pour votre audience après le lancement du Canvas n'entreront pas dans le Canvas.

{% alert tip %}
Consultez les [types de planification d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) pour obtenir des conseils et des détails sur l'utilisation de la réception/distribution planifiée, basée sur des actions ou déclenchée par l'API pour votre Canvas !
{% endalert %}

### Examinez les filtres d'audience d'entrée

En général, évitez de configurer un Canvas basé sur une action ou déclenché par une API avec le même déclencheur que le filtre d'audience. Par exemple, après le lancement d'un Canvas, les utilisateurs qui effectuent une action spécifique seront inclus dans l'audience d'entrée, il n'est donc pas nécessaire d'ajouter l'événement en tant que filtre d'audience. 

Pour plus de détails sur les filtres de segmentation disponibles pour cibler votre audience, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Regrouper plusieurs demandes d'API en lots

Effectuez vos demandes dans le même appel API, plutôt que dans plusieurs appels, pour confirmer que le profil utilisateur est créé ou mis à jour en premier. Reportez-vous à la section [Utilisation de plusieurs endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) pour plus d'exemples.

### Ajouter un délai

Une autre option pour éviter les conditions de concurrence consiste à utiliser l'étape du délai (idéalement réglée sur 5 minutes) comme première étape de votre canvas. 

Cela laisse le temps aux attributs, aux adresses e-mail et aux jetons de poussée d'être traités dans les nouveaux profils utilisateurs avant qu'ils ne soient ciblés pour les étapes suivantes de Canvas. Sans cette étape de délai, il est possible qu'un e-mail soit envoyé à un utilisateur dont l'e-mail n'a pas encore été mis à jour.

## Délais de réception/distribution

La définition d'un délai de réception/distribution de Canvas en temps réel peut conduire à l'augmentation des taux d'engagement et de conversion. Prenez note de l'heure de réception/distribution que vous avez fixée pour votre Canvas. Pour aider à augmenter les taux d'engagement et de conversion, il est préférable de déclencher les Canvases en temps réel plutôt que de manière planifiée et récurrente.

Si vous avez choisi une réception/distribution planifiée pour votre Canvas, Braze recommande de planifier votre Canvas au moins 24 heures avant son lancement afin de permettre d'éventuels ajustements à votre Canvas.

## Segments d'utilisateurs

Avant de sursaturer votre parcours utilisateur Canvas Flow de composants, réfléchissez à la manière dont vous pourriez garder un parcours utilisateur simple. Utilisez la vue simplifiée dans l'éditeur Canvas pour avoir une meilleure idée de la façon dont votre parcours utilisateur se ramifie. 

Vous pouvez utiliser quatre éléments principaux pour segmenter vos utilisateurs de manière simple et efficace :

* [Parcours d'audience](#audience-paths)
* [Arbre décisionnel](#decision-split)
* [Parcours d'action](#action-paths)
* [Chemins d'expérience](#experiment-paths)

### Parcours d'audience

Utilisez les étapes [des parcours audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) pour segmenter les utilisateurs dans le Canvas en fonction des attributs personnalisés, des événements personnalisés et des données d'engagement aux messages précédents provenant des profils des utilisateurs.

### Arbre décisionnel

L'étape de l'arbre [décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) vous permet d'envoyer vos utilisateurs vers différents parcours en fonction de leurs réponses à une question polaire.

### Parcours d'action

[Les parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se concentrent sur la segmentation des utilisateurs en fonction de leurs comportements en temps réel, tels que les événements personnalisés, les achats et les changements d'attributs personnalisés. 

### Chemins d'expérience

À l'instar des parcours d'action, vous pouvez exploiter les étapes des [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) dans votre Canvas pour tester plusieurs parcours Canvas les uns par rapport aux autres, ainsi qu'un groupe de contrôle. Cela permet de suivre les performances du parcours, ce qui vous permet de prendre des décisions éclairées lorsque vous créez votre parcours Canvas. 

## Tests avant le lancement

Après avoir revu les détails de votre Canvas, consultez la rubrique [Envoi de Canvas de test]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) pour connaître les différentes méthodes que vous pouvez utiliser pour tester votre Canvas auprès d'utilisateurs test.

## Liste de contrôle pour le lancement

### Vérifier la disponibilité des utilisateurs

- Assurez-vous que vos utilisateurs répondent à vos critères de segmentation.
- Confirmez que l'état de l'abonnement est "abonné" ou "abonné" et que le jeton Push existe. Si vous avez ajouté ces règles en tant que règles d'entrée dans le Canvas, il est possible que les utilisateurs aient été désabonnés entre l'entrée dans le Canvas et la réception de l'étape du message.
- Confirmez qu'ils correspondent à vos paramètres d'envoi de Canvas. (Si les utilisateurs sont "abonnés" mais que les paramètres sont "Abonnés", les utilisateurs ne seront pas activés pour le canal).
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois où chaque utilisateur peut recevoir un message provenant d'un canal spécifique.
- Si les heures calmes sont activées, l'heure d'envoi de votre message peut être affectée, ce qui signifie que votre message peut être envoyé à la prochaine heure disponible (à la fin des heures calmes) ou être entièrement annulé.
- Vérifiez la disponibilité des utilisateurs pour des filtres supplémentaires dans votre étape du canvas.

### Confirmer qu'ils ont effectué l'événement personnalisé ou l'achat préalable.

- Vérifiez s'il existe une condition de concurrence, qui a une incidence sur les messages que les utilisateurs reçoivent s'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre les différentes étapes d'un même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message peuvent être arrêtés par un filtre qui exige la réalisation d'une autre étape sur une autre branche.
- Confirmez que les utilisateurs satisfont à des règles de validation supplémentaires.
- Confirmez que l'étape du canvas était connectée à l'étape précédente au moment de l'envoi.

### Confirmez que votre canvas s'enregistre correctement et que toutes les étapes sont valables.

Si votre Canvas ne se charge pas et ne progresse pas, cela peut être dû au fait qu'une version précédente du Canvas n'a pas été enregistrée correctement et contient des étapes non valides. Vous pouvez dupliquer le canvas à partir du tableau de bord. Si le problème persiste, ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)

## Résolution des problèmes

{% details Why are my users not receiving my Canvas messages? %}
**Vérifier la disponibilité des utilisateurs**
- Assurez-vous qu'ils répondent à vos critères de segmentation.
- Confirmez que leur état d'abonnement à Push est "abonné" ou "abonné" **et que** leur état " **Push Enabled** " est défini sur "true". Si vous avez ajouté ces règles en tant que règles d'entrée dans le Canvas, il est possible que les utilisateurs aient été désabonnés entre le moment où ils sont entrés dans le Canvas et celui où ils ont reçu l'étape du message.
- Confirmez qu'ils correspondent à vos paramètres d'envoi de Canvas. (Si les utilisateurs sont "abonnés" mais que les paramètres sont "Abonnés", les utilisateurs ne seront pas activés pour le canal).
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois où chaque utilisateur peut recevoir un message provenant d'un canal spécifique. 
- Si les heures calmes sont activées, l'heure d'envoi de votre message peut être affectée, ce qui signifie que votre message peut être envoyé à la prochaine heure disponible (à la fin des heures calmes) ou être entièrement annulé.

**Vérifiez la disponibilité des utilisateurs pour des filtres supplémentaires dans votre étape du canvas**
- Confirmez qu'ils ont effectué l'événement personnalisé ou l'achat préalable.
- Vérifiez s'il existe une [condition de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), qui a une incidence sur les messages que les utilisateurs reçoivent s'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre les différentes étapes d'un même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message peuvent être arrêtés par un filtre qui exige la réalisation d'une autre étape sur une autre branche.
- Confirmez que les utilisateurs satisfont à des règles de validation supplémentaires.
- Confirmez que l'étape du canvas était connectée à l'étape précédente au moment de l'envoi.
{% enddetails %}

