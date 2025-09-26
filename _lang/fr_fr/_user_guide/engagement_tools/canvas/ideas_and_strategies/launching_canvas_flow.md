---
nav_title: Lancement avec Canvas Flow
article_title: Lancement avec Canvas Flow
page_order: 3
description: "Cet article de référence explique comment préparer et tester un Canvas créé à l’aide de Canvas Flow avant son lancement."
page_type: reference
tool: Canvas
---

# Lancement avec Canvas Flow

> Cet article de référence explique comment préparer et tester un Canvas créé à l’aide de Canvas Flow avant son lancement. Ceci comprend le fait d’identifier les points de contrôle importants de Canvas tel que les conditions d’entrée dans le Canvas, les sommaires d’audiences et les segments d’utilisateur.

Lorsque vous vous préparez à lancer votre Canvas, Braze vous conseille de vérifier, à chaque étape du générateur de Canvas, les paramètres de votre Canvas susceptible d’avoir un impact sur l’envoi de votre message, y compris :
* [Conditions de concurrence](#race-conditions)
* [Heures de livraison](#delivery-times)
* [Segments utilisateurs](#segment-users)

## Conditions de concurrence 

Prenez en compte les [conditions de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) susceptibles de se produire avant de lancer votre Canvas. 

Pour entrer dans un Canvas, les utilisateurs doivent se trouver dans l’audience d’entrée avant que sa planification n’arrive, que le Canvas soit planifié, par événement ou déclenché par API. 

![Un canvas basé sur l'action qui saisit les utilisateurs lorsqu'ils effectuent un achat pendant l'heure locale de l'utilisateur, du 30 avril 2025 à 12 heures au 7 mai 2025 à 12 heures.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Notez que les utilisateurs qui se qualifient pour votre audience d’entrée après le lancement du Canvas n’y entreront pas.

{% alert tip %}
Consultez la rubrique [Types de planification d'entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) pour obtenir des conseils et des détails sur le moment où il convient d'utiliser la réception/distribution planifiée, basée sur des actions ou déclenchée par l'API pour votre Canvas !
{% endalert %}

### Vérifiez les filtres d’audience d’entrée

De façon générale, évitez de configurer un Canvas par événement ou déclenché par API avec le même déclencheur que le filtre d’audience. Par exemple, après le lancement d’un Canvas, les utilisateurs effectuant une action données seront ajoutés dans l’audience d’entrée. Il n’est donc pas nécessaire d’ajouter cet événement en tant que filtre d’audience. 

Pour plus de détails sur les filtres de segmentation disponibles pour cibler votre audience, voir [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Requêtes API multiples par lots

Effectuez vos requêtes avec le même appel API plutôt que plusieurs appels pour confirmer que le profil utilisateur est créé et mis à jour au préalable. Reportez-vous à la section [Utilisation de plusieurs endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) pour plus d'exemples.

### Ajouter un délai

Une autre option permettant d’éviter les conditions de concurrence est d’utiliser l’étape de délai (de préférence réglée sur 5 minutes) en tant que première étape de votre Canvas. 

Ceci laisse le temps nécessaire pour envoyer les attributs, adresses e-mail et jetons de notification push vers les nouveaux profils utilisateur avant qu’ils ne soient ciblés par les étapes Canvas suivantes. Sans cette étape de délai, il est possible qu'un e-mail soit envoyé à un utilisateur dont l'e-mail n'a pas encore été mis à jour.

## Heures de livraison

La définition d'un délai de réception/distribution de Canvas en temps réel peut conduire à l'augmentation des taux d'engagement et de conversion. Prenez en compte l’heure de livraison que vous avez définie pour votre Canvas. Pour aider à augmenter les taux d'engagement et de conversion, il est préférable de déclencher les Canvases en temps réel plutôt que de manière planifiée et récurrente.

Si vous avez sélectionné une livraison planifiée pour votre Canvas, Braze conseille de planifier votre Canvas au moins 24 heures avant l’heure de déclenchement prévue pour laisser la possibilité d’effectuer des ajustements dans votre Canvas.

## Segments utilisateurs

Avant des saturer le Canvas Flow de votre parcours utilisateur avec des composants, prenez en compte le fait que vous pourriez désirer que votre parcours utilisateur reste simple. Utilisez la vision simplifiée de l’éditeur Canvas pour avoir une meilleure idée des ramifications de votre parcours utilisateur. 

Il existe quatre composants principaux pouvant être utilisés pour segmenter vos utilisateurs d’une manière simple et efficace :

* [Parcours d’audience](#audience-paths)
* [Arbre décisionnel](#decision-split)
* [Parcours d’actions](#action-paths)
* [Chemins d’expérience](#experiment-paths)

### Parcours d’audience

Utilisez les étapes [des parcours audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) pour segmenter les utilisateurs dans le Canvas en fonction des attributs personnalisés, des événements personnalisés et des données d'engagement aux messages précédents provenant des profils des utilisateurs.

### Arbre décisionnel

L'étape de [l’arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) vous permet d'envoyer vos utilisateurs vers différents parcours en fonction de leurs réponses à une question centrale.

### Parcours d’actions

[Les parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se concentrent sur la segmentation des utilisateurs en fonction de leurs comportements en temps réel, tels que les événements personnalisés, les achats et les changements d'attributs personnalisés. 

### Chemins d’expérience

À l'instar des parcours d'action, vous pouvez tirer parti des étapes [des chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) dans votre Canvas pour tester plusieurs parcours Canvas les uns par rapport aux autres, ainsi qu'un groupe de contrôle. Ceci permet de suivre la performance des chemins, vous permettant de prendre des décisions bien renseignées lorsque vous construisez votre parcours Canvas. 

## Tester avant le lancement

Après avoir passé en revue les détails de votre Canvas, consultez la rubrique [Envoi de Canvas de test]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) pour connaître les différentes méthodes que vous pouvez utiliser pour tester votre Canvas auprès d'utilisateurs test.

## Résolution des problèmes

{% details Pourquoi mes utilisateurs ne reçoivent-ils pas mes messages Canvas ? %}
**Vérifier la disponibilité des utilisateurs**
- Assurez-vous qu'ils répondent à vos critères de segmentation.
- Confirmez que leur état d'abonnement à Push est "abonné" ou "abonné" **et que** leur état " **Push Enabled** " est défini sur "true". Si vous avez ajouté ces règles d’entrées Canvas, il est possible que les utilisateurs aient été désinscrits entre le moment de leur accession au Canvas et l’étape de réception du message.
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

