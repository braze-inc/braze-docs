---
nav_title: Étape du message
article_title: Étape du message
alias: "/fr/message_pas/"
page_order: 5
page_type: Référence
description: "Cet article de référence traite de la façon de créer un message autonome en utilisant l'étape de messagerie de Canvas ."
tool: Toile
---

# Étape du message

Les Étapes de message vous permettent d'ajouter un message autonome où vous voulez dans votre flux Canvas .

{% alert important %}
Les Étapes de message Canvas sont actuellement en accès anticipé. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à l'accès anticipé.
{% endalert %}

## Créer une étape de message

![Etape du message Canvas[1]{: style="float:right;max-width:19%;margin-left:15px;"}

Pour créer une étape de message, ajoutez une étape à votre Canevas. Ensuite, utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner **Message**.

Avec une étape de message, tous les utilisateurs qui entrent dans l'étape suivante lorsque l'une des conditions suivantes est remplie :
- Tout message est envoyé
- Un message n'est pas envoyé car l'utilisateur n'est pas joignable avec un canal
- Un message n'est pas envoyé car il est limité à la fréquence
- Un message n'est pas envoyé car il est abandonné

!\[Étape du message Canvas\]\[2\]{: style="max-width:75%;"}

L'Étape de message comprend également les paramètres pour la livraison intelligente et les heures silencieuses de remplacement.

L'Étape de message vous permet d'activer le Timing Intelligent avec une option de repli lorsque le profil d'un utilisateur n'a pas assez de données pour calculer un temps optimal. Sélectionnez **Utiliser le Timing Intelligent** dans **Paramètres de livraison**. Ici, vous pouvez choisir le moment le plus populaire ou un temps de repli spécifique.

Si les heures silencieuses sont activées, l'étape de message vous permet également de remplacer ce paramètre.

!\[Étape du message Canvas\]\[4\]

{% alert note %}
Pour les étapes de message Canvas , `event_properties` ne sont pas pris en charge. Au lieu de cela, utilisez `canvas_entry_properties`.
{% endalert %}

## Analyses

| Métrique                         | Libellé                                                                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Entrées                          | Le nombre de fois où l'étape a été saisie. Si votre Canevas a une rééligibilité et qu'un utilisateur entre deux fois un message, deux entrées seront enregistrées.                               |
| Procédé à l'étape suivante       | Le nombre d'entrées qui sont passées à l'étape suivante dans le Canvas.                                                                                                                          |
| Envoie                           | Le nombre total de messages que l'étape a envoyés. Si votre Canvas rééligibilité et qu'un utilisateur entre deux fois dans un message, deux entrées seront enregistrées.                         |
| Destinataires uniques            | Le nombre d'utilisateurs qui ont reçu des messages de cette étape.                                                                                                                               |
| Événement de conversion primaire | Le nombre de fois où un événement défini s'est produit après avoir interagi ou vu un message reçu d'une campagne de Braze. Vous définissez cet événement lors de la construction de la campagne. |
| Revenus                          | Le revenu total en dollars provenant des bénéficiaires de la campagne dans la fenêtre de conversion principale définie.                                                                          |
{: .reset-td-br-1 .reset-td-br-2}

!\[Étape du message Canvas\]\[3\]{: style="max-width:20%;"}
\[1]: {% image_buster /assets/img/canvas_components/message_step1.png %} [2]: {% image_buster /assets/img/canvas_components/message_step2. ng %} [3\]\[3\] : {% image_buster /assets/img/canvas_components/message_step3.png %} [4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
