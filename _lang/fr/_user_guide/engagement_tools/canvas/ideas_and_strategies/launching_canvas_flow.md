---
nav_title: Lancement avec Canvas Flow
article_title: Lancement avec Canvas Flow
page_order: 3
description: "Cet article de référence explique comment préparer et tester un Canvas construit à l’aide de Canvas Flow avant son lancement."
page_type: reference
tool: Canvas
---

# Lancement avec Canvas Flow

> Cet article de référence explique comment préparer et tester un Canvas construit à l’aide de Canvas Flow avant son lancement. Ceci comprend le fait d’identifier les points de contrôle importants de Canvas tel que les conditions d’entrée dans le Canvas, les sommaires d’audiences et les segments d’utilisateur.

Lorsque vous vous préparez à lancer votre Canvas, Braze vous conseille de vérifier, à chaque étape du générateur de Canvas, les paramètres de votre Canvas susceptible d’avoir un impact sur l’envoi de votre message, y compris :
* [Conditions de concurrence](#race-conditions)
* [Heures de livraison](#delivery-times)
* [Segments utilisateurs](#segment-users)

## Conditions de concurrence 

Prenez en compte les [conditions de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) susceptibles de se produire avant de lancer votre Canvas. 

Pour entrer dans un Canvas, les utilisateurs doivent se trouver dans l’audience d’entrée avant que sa planification n’arrive, que le Canvas soit planifié, par événement ou déclenché par API. 

![][1]{: style="max-width:75%;"}

Notez que les utilisateurs qui se qualifient pour votre audience d’entrée après le lancement du Canvas n’y entreront pas.

{% alert tip %}
Consultez les [types de planification d’entrée]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) pour obtenir des conseils et des détails sur les moments où choisir la livraison planifiée, par événement ou déclenchée par API pour vos Canvas !
{% endalert %}

### Vérifiez les filtres d’audience d’entrée

De façon générale, évitez de configurer un Canvas par événement ou déclenché par API avec le même déclencheur que le filtre d’audience. Par exemple, après le lancement d’un Canvas, les utilisateurs effectuant une action données seront ajoutés dans l’audience d’entrée. Il n’est donc pas nécessaire d’ajouter cet événement en tant que filtre d’audience. 

Pour plus de détails sur les filtres de segmentation disponibles pour cibler votre audience, consultez les [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Requêtes API multiples par lots

Effectuez vos requêtes avec le même appel API plutôt que plusieurs appels pour confirmer que le profil utilisateur est créé et mis à jour au préalable. Consultez la section [Utiliser plusieurs endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) pour plus d’exemples.

### Ajouter un délai

Une autre option permettant d’éviter les conditions de concurrence est d’utiliser l’étape de délai (de préférence réglée sur 5 minutes) en tant que première étape de votre Canvas. 

Ceci laisse le temps nécessaire pour envoyer les attributs, adresses e-mail et jetons de notification push vers les nouveaux profils utilisateur avant qu’ils ne soient ciblés par les étapes Canvas suivantes. Sans l’étape de délai, il est possible qu’un e-mail soit envoyé à un utilisateur dont l’e-mail n’a pas encore été mis à jour.

## Heures de livraison

En réglant l’heure de livraison d’un Canvas en temps réel, ceci peut entraîner l’augmentation de l’engagement et du taux de conversion. Prenez en compte l’heure de livraison que vous avez définie pour votre Canvas. Pour aider à augmenter l’engagement et les taux de conversion, il vaut mieux que le Canvas se déclenche en temps réel plutôt que selon une planification récurrente.

Si vous avez sélectionné une livraison planifiée pour votre Canvas, Braze conseille de planifier votre Canvas au moins 24 heures avant l’heure de déclenchement prévue pour laisser la possibilité d’effectuer des ajustements dans votre Canvas.

## Segments utilisateurs

Avant des saturer le Canvas Flow de votre parcours utilisateur avec des composants, prenez en compte le fait que vous pourriez désirer que votre parcours utilisateur reste simple. Utilisez la vision simplifiée de l’éditeur Canvas pour avoir une meilleure idée des ramifications de votre parcours utilisateur. 

Il existe quatre composants principaux pouvant être utilisés pour segmenter vos utilisateurs d’une manière simple et efficace :

* [Parcours d’audience](#audience-paths)
* [Décision de séparation](#decision-split)
* [Parcours d’action](#action-paths)
* [Chemins d’expérience](#experiment-paths)

### Parcours d’audience

Utilisez les étapes de [parcours d’audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) pour segmenter vos utilisateurs au sein du Canvas selon des attributs et des événements personnalisés ainsi que les données antérieures d’engagement avec les messages tirées des profils utilisateur.

### Décision de séparation

L’étape de [décision de séparation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) vous permet d’envoyer vos utilisateurs dans différents chemins de parcours utilisateur selon leurs réponses à une question centrale.

### Parcours d’actions

Les [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se concentrent sur la segmentation des utilisateurs selon leurs comportements en temps réel tels que des événements personnalisés ou d’achats ainsi que des modifications d’attributs personnalisés. 

### Chemins d’expérience

De la même manière que pour les parcours d’action, vous pouvez tirer parti des étapes de [chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_paths/) dans votre Canvas pour tester plusieurs chemins de Canvas les uns par rapport aux autres ainsi qu’un groupe de contrôle. Ceci permet de suivre la performance des chemins, vous permettant de prendre des décisions bien renseignées lorsque vous construisez votre parcours Canvas. 

## Tester avant le lancement

Après avoir examiné tous les détails de votre Canvas, consultez la section [Envoyer des tests]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) de Canvas pour y trouver plusieurs méthodes que vous pouvez utiliser pour tester votre Canvas avec des utilisateurs de test.

## Résolution des problèmes

{% details Pourquoi mes utilisateurs ne reçoivent-ils pas mes messages Canvas ? %}
- Vérifiez que leur statut d’abonnement aux notifications push est « abonné » ou « inscrit » **et** que leur statut **Notifications push activées** est défini sur « vrai ». Si vous avez ajouté ces règles d’entrées Canvas, il est possible que les utilisateurs aient été désinscrits entre le moment de leur accession au Canvas et l’étape de réception du message.
- Si la limite de fréquence globale est activée pour votre Canvas, selon vos règles spécifiques, le nombre de fois où un utilisateur devrait recevoir un message d’un canal donné peut être limité. 
- Si les heures calmes sont activées, l’heure d’envoi de votre message peut être affecté, ce qui signifie que votre message peut être envoyé à l’heure disponible suivante (lorsque les heures calmes s’achèvent) ou annuler complètement le message.
{% enddetails %}

[1]: {% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}
