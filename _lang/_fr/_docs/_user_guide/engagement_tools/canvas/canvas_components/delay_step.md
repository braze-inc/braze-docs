---
nav_title: Délai
article_title: Délai
alias: "/fr/delay_step/"
page_order: 3
page_type: Référence
description: "Cet article de référence explique comment ajouter un délai à votre Canvas sans avoir à ajouter un message associé."
tool: Toile
---

# Délai

Les étapes de délai vous permettent d'ajouter un délai autonome à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir à ajouter un message associé. Les étapes de délai peuvent rendre votre Canvas plus propre. Là où vous avez précédemment besoin de créer deux étapes complètes, vous pouvez créer une étape de délai et une étape unique et complète.

Vous pouvez également utiliser Canvas Delay Steps pour retarder une étape jusqu'à une date exacte, jusqu'à un jour spécifique, ou jusqu'à un jour précis de la semaine.

!\[Canvas Delay Step\]\[1\]{: style="float:right;max-width:30%;margin-left:15px;"}

## Créer une étape de délai

Pour créer une étape de délai, ajoutez une étape à votre Canevas. Ensuite, utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner **Delay**.

- Une étape de délai ne peut pas avoir des étapes fraternelles en pleine étapes. En d'autres termes, vous ne pouvez pas créer une étape complète qui branche en une étape de délai et une étape complète. Cette restriction existe car s'il y avait une branche avec une étape de délai et une étape complète, il ne serait pas clair quels utilisateurs de la branche descendraient.
- Une étape de délai ne peut se connecter qu'à une étape suivante.

### Options de délai

Vous pouvez choisir le type de délai avant le message suivant dans votre Canvas. Vous pouvez soit définir un délai pour que vos utilisateurs puissent durer après une période spécifiée, ou retardez vos utilisateurs jusqu'à une date et heure précises.

{% tabs %}
  {% tab After a duration %}

  L'option **Après une durée** vous permet de retarder les utilisateurs pour un nombre défini de secondes, minutes, heures, jours ou semaines, et à une heure précise. Par exemple, vous pouvez retarder les utilisateurs pour quatre heures ou pour une journée.

  {% endtab %}
  {% tab Until a specific date %}

  L'option **Jusqu'à une date spécifique** vous permet de maintenir les utilisateurs à l'étape jusqu'à une date et heure spécifique.

  {% alert important %}
  Si la date et l'heure sélectionnées sont déjà passées par le moment où les utilisateurs passent à l'étape de retard, les utilisateurs quitteront le Canvas. Il peut y avoir un maximum de 31 jours entre le début de la toile et les dates choisies pour les étapes « Attendre jusqu’à la date exacte ».
  {% endalert %}
  {% endtab %}
  {% tab Until a specific day of the week %}

  L'option **Jusqu'à un jour spécifique de la semaine** vous permet de conserver les utilisateurs à l'étape jusqu'à un jour spécifique de la semaine, à un moment précis. Par exemple, vous pouvez retarder les utilisateurs jusqu'à ce que le jeudi suivant arrive à 16h dans le fuseau horaire de la société.

  Pour configurer cela avec succès vous devrez également sélectionner ce qui se passera si l'utilisateur entre dans Canvas le jour de la semaine sélectionné (e. Jeudi), mais après l'heure spécifiée. Vous pouvez choisir d'avancer l'utilisateur le même jour ou de le maintenir jusqu'à la semaine suivante.
  {% endtab %}
{% endtabs %}

## Utiliser les étapes de délai

Disons que c’est le 10 juin. Le 11 juin, vous aimeriez que les utilisateurs entrent sur le Canvas et reçoivent un message au sujet d’une promotion à venir. Ensuite, vous voulez tenir les utilisateurs dans le Canvas jusqu'au 17 juin à 15h heure locale. À 15h heure locale le 17 juin, vous voulez envoyer aux utilisateurs un message de rappel au sujet de la promotion.

Vous commencerez par ajouter une étape complète qui vous enverra immédiatement après l’entrée des utilisateurs sur Canvas le 11 juin. Ensuite, vous créerez une étape de retard qui contiendra les utilisateurs à l’étape jusqu’à 15h heure locale le 17 juin. Après cela, vous liez le délai à une étape complète qui envoie un message immédiatement.

### Délai des étapes à la fin d'une toile {#delay-as-last-step}

Si vous ajoutez une étape de retard à votre Canvas, mais qu'il n'y a plus aucune étape après l'étape de retard, tout utilisateur qui atteint l'étape de retard est automatiquement avancé hors du Canvas. C'est vrai même si le temps de l'étape de retard n'a pas encore été atteint. Cela signifie que, pour les utilisateurs qui ont déjà atteint l'étape de retard, ils ne recevront aucun message que vous ajouterez après l'étape de délai. Cependant, si un utilisateur n'a pas atteint l'étape de retard et qu'un message est ajouté, il recevra ce message.

## Délai de l'analyse des étapes

Les étapes de retard comportent trois statistiques disponibles dans la vue analytique d'un Canvas actif ou déjà actif.

| Métrique                     | Libellé                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Entré`                      | Reflète le nombre de fois où l'étape a été entrée. Si votre Canvas a une rééligibilité et qu'un utilisateur entre deux fois dans un délai, deux entrées seront enregistrées. |
| `Procédé à l'étape suivante` | Reflète le nombre d'entrées qui ont franchi l'étape suivante dans le Canvas.                                                                                                 |
| `Toile Sortie`               | Reflète le nombre d'entrées qui ont quitté le Canvas et ne sont pas passées à l'étape suivante.                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

Les séries temporelles pour ces analyses sont disponibles dans la vue étapes.
[1]: {% image_buster /assets/img/canvas_delay.png %}
