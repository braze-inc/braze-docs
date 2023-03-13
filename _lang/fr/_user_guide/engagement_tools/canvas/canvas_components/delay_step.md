---
nav_title: Délai 
article_title: Délai 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Cet article de référence aborde la façon d’ajouter un délai à votre Canvas sans avoir à ajouter un message associé."
tool: Canvas

---

# Délai

Les composants de délai vous permettent d’ajouter un délai indépendant à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir à ajouter un message associé. Les délais peuvent simplifier votre Canvas. Alors que précédemment vous deviez créer deux étapes complètes, vous pouvez désormais créer une étape de délai et une seule étape complète. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu’à une date précise, un jour spécifique ou un jour spécifique de la semaine.

## Créer un délai

Pour créer un délai, commencez par ajouter une étape à votre Canvas. Glissez-déplacez le composant de délai depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **Delay (Délai)**.

Plusieurs détails doivent être pris en compte lors de la création d’un délai dans votre parcours Canvas.
- La limite de délai est de 30 jours.
- Un composant de délai peut être uniquement relié à une étape suivante.

### Options de délai temporel

Vous pouvez choisir le type de délai avant le message suivant dans votre Canvas. Vous pouvez définir une durée du délai pour vos utilisateurs jusqu’à une période désignée, ou une date et heure spécifiques.

{% tabs %}
  {% tab After a duration %}

  L’option **Après une durée** vous permet de retarder vos utilisateurs pendant un nombre défini de secondes, minutes, heures, jours ou semaines à un moment spécifique. Par exemple, vous pouvez retarder des utilisateurs pendant quatre heures ou pendant un jour. Prenez en compte la différence entre les calculs des « jours » et des « jours civils ». Un « jour » comprend 24 heures et est calculé à partir du moment où l’utilisateur entre dans l’étape de délai. Un « jour civil » signifie qu’un jour est la période entre le moment où l’utilisateur entre dans l’étape de délai et minuit dans son fuseau horaire.

  {% endtab %}
  {% tab Until a specific date %}

  L’option **Jusqu’à une date** vous permet de conserver les utilisateurs dans l’étape jusqu’à une date et une heure spécifiques.

  {% alert important %}
  Si la date et l’heure sélectionnées sont déjà passées lors de la progression des utilisateurs vers l’étape de délai, ces derniers quitteront le Canvas. Un délai maximum de 31 jours peut survenir entre le début de Canvas et les dates sélectionnées pour les étapes « Attendre jusqu’à la date précise ».
  {% endalert %}
  {% endtab %}
  {% tab Until a specific day of the week %}

  L’option **Jusqu’à un jour spécifique de la semaine** vous permet de conserver les utilisateurs dans l’étape jusqu’à un jour spécifique de la semaine, à une heure spécifique. Par exemple, vous pouvez retarder des utilisateurs jusqu’au jeudi suivant 16 h, dans le fuseau horaire de l’entreprise. 

  Pour configurer correctement ce processus, vous devrez également sélectionner le mode d’action si l’utilisateur accède au Canvas le jour de la semaine sélectionné (par ex. jeudi), mais après l’heure indiquée. Vous pouvez choisir soit d’avancer l’utilisateur au même jour ou le conserver jusqu’à la semaine suivante.
  {% endtab %}
{% endtabs %}

## Utilisation des étapes de délai

Supposons que nous soyons le 10 juin. Le 11 juin, vous souhaiteriez que les utilisateurs accèdent au Canvas et reçoivent un message concernant une promotion à venir. Puis vous souhaitez conserver les utilisateurs dans le Canvas jusqu’au 17 juin 15 h, heure locale. À 15 h heure locale le 17 juin, vous souhaitez envoyer un message de rappel aux utilisateurs, concernant la promotion.

Vous pouvez commencer par ajouter une étape complète envoyant un message immédiatement après l’accès des utilisateurs au Canvas, le 11 juin. Puis vous pouvez créer une étape de délai qui conserve les utilisateurs dans l’étape jusqu’au 17 juin 15 h, heure locale. Ensuite, vous pouvez relier l’étape de délai à une étape complète, envoyant le message immédiatement.

### Retarder les composants à la fin du Canvas {#delay-as-last-step}

Si vous ajoutez un composant de délai à votre Canvas, mais qu’il n’y a plus d’étape après le composant de délai, tout utilisateur atteignant la dernière étape est automatiquement exclu du Canvas. Ce processus s’applique également si l’heure de l’étape de délai n’a pas encore été atteinte. Cela signifie que les utilisateurs ayant déjà atteint l’étape de délai ne recevront plus les messages que vous ajoutez après l’étape de délai. Cependant, si un utilisateur n’a pas atteint l’étape de délai et qu’un message est ajouté, il recevra ce message.

## Analytique du délai

Les délais disposent de trois statistiques disponibles dans la vue analytique d’un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| `Entered` | Illustre le nombre total d’accès à l’étape. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à une étape de fractionnement des décisions, les deux entrées seront enregistrées. |
| `Poursuivre vers l’étape suivante` | Illustre le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| `Sortis de Canvas` | Illustre le nombre d’entrées pour quitter le Canvas et ne pas poursuivre à l’étape suivante. |
{: .reset-td-br-1 .reset-td-br-2}

Les séries chronologiques pour ces éléments analytiques sont disponibles dans la vue du composant développée.

[1]: {% image_buster /assets/img/canvas_delay.png %}
