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

> Les composants de délai vous permettent d’ajouter un délai indépendant à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir à ajouter un message associé. 

Les délais peuvent simplifier votre Canvas. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu’à une date précise, un jour spécifique ou un jour spécifique de la semaine. <br> ![][1]{: style="float:right;max-width:35%;margin-left:15px;"}

## Créer un délai

Pour créer un délai, ajoutez une étape à votre canvas. Faites glisser et déposez le composant de délai depuis la barre latérale, ou cliquez sur le <i class="fas fa-plus-circle"></i> bouton plus en bas d'une étape et sélectionnez **Delay**.

Plusieurs détails doivent être pris en compte lors de la création d’un délai dans votre parcours Canvas.

- La limite de délai est de 30 jours.
- Un composant de délai peut être uniquement relié à une étape suivante.

### Délais personnalisés

{% alert important %}
Les délais personnalisés et les délais prolongés sont en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Sélectionnez la bascule **Personnaliser** le délai pour définir un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour sélectionner la variable contextuelle à retarder.

Braze sortira un utilisateur à l'étape si :

- La variable contextuelle ne renvoie à aucune valeur.
- Un appel de contenu connecté intégré échoue.
- Les types de variables contextuelles ne correspondent pas.

Imaginons que nous souhaitions rappeler à nos clients d'acheter du dentifrice dans 30 jours. En combinant une étape Contexte et une étape Délai, nous pouvons sélectionner la variable contextuelle à retarder. Dans ce cas, notre étape Contexte comporterait les champs suivants :

- **Nom de la variable contextuelle :** product_reminder_interval
- **Type de données :** Date
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Le "product_reminder_interval" et sa valeur.][2]

Ensuite, comme nous voulons rappeler à nos clients qu'ils n'auront que 30 jours à partir de maintenant, nous sélectionnerons **Jusqu'à un jour précis** comme option de délai et nous sélectionnerons **Personnaliser le délai** pour utiliser les informations de notre étape Contexte. Cela signifie que nos utilisateurs seront retardés jusqu'à la variable de contexte sélectionnée.

![Exemple d'utilisation de variables contextuelles avec une étape Delay pour retarder les utilisateurs en fonction de l'"intervalle de rappel du produit".][3]

#### Délais prolongés

Vous pouvez désormais prolonger les délais jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré une session à le faire.

### Options de délai temporel

Vous pouvez choisir le type de délai avant le message suivant dans votre Canvas. Vous pouvez définir une durée du délai pour vos utilisateurs jusqu’à une période désignée, ou une date et heure spécifiques.

{% tabs %}
  {% tab Après une certaine durée %}

  L'option **Après une durée** vous permet de retarder les utilisateurs pendant un certain nombre de secondes, minutes, heures, jours ou semaines, et à une heure spécifique. Par exemple, vous pouvez retarder des utilisateurs pendant quatre heures ou pendant un jour.
  
  Prenez en compte la différence entre les calculs des « jours » et des « jours civils ».
  
    - A "day" is 24 hours and calculated from the time the user enters the Delay step. 
    - A "calendar day" defines a day as 24 hours after a specified time. When a calendar day is chosen and the time is specified, you can choose to delay at company time or at a user's local time. If a time isn't specified, the user will be delayed until midnight the next day in company time.

  Vous pouvez également sélectionner **À un moment précis** pour spécifier quand les utilisateurs avanceront dans la toile. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape Délai. Si cette durée est supérieure à la durée configurée dans les paramètres, nous ajouterons des heures supplémentaires au délai. Par exemple, disons que nous sommes aujourd'hui le 11 décembre et que notre étape Délai est réglée sur **Après une durée d'** une semaine à 8 heures UTC. Si un utilisateur entre dans l'étape de report le 4 décembre, il sera libéré de l'étape de report pour poursuivre son voyage aujourd'hui s'il est entré à l'origine dans l'étape de report avant 8 heures UTC. S'il est entré dans l'étape Délai après cette heure, l'utilisateur sera retardé jusqu'au jour suivant (la prochaine occurrence de cette heure). 

  {% endtab %}
  {% tab Jusqu'à une date spécifique %}

  L'option **Jusqu'à une date spécifique** vous permet de maintenir les utilisateurs dans l'étape jusqu'à une date et une heure spécifiques.

  {% alert important %}
  Si la date et l’heure sélectionnées sont déjà passées lors de la progression des utilisateurs vers l’étape de délai, ces derniers quitteront le Canvas. Un délai maximum de 31 jours peut survenir entre le début de Canvas et les dates sélectionnées pour les étapes « Attendre jusqu’à la date précise ».
  {% endalert %}
  {% endtab %}
  {% tab Jusqu'à un jour spécifique de la semaine %}

  L'option **Jusqu'à un jour spécifique de la semaine** vous permet de maintenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure précise. Par exemple, vous pouvez retarder des utilisateurs jusqu’au jeudi suivant 16 h, dans le fuseau horaire de l’entreprise. 

  Pour configurer cela avec succès, vous devrez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, jeudi), mais après l'heure spécifiée. Vous pouvez choisir soit d’avancer l’utilisateur au même jour ou le conserver jusqu’à la semaine suivante.
  {% endtab %}
{% endtabs %}

## Utilisation des étapes de retard

Supposons que nous soyons le 10 juin. Le 11 juin, vous souhaiteriez que les utilisateurs accèdent au Canvas et reçoivent un message concernant une promotion à venir. Puis vous souhaitez conserver les utilisateurs dans le Canvas jusqu’au 17 juin 15 h, heure locale. À 15 h heure locale le 17 juin, vous souhaitez envoyer un message de rappel aux utilisateurs, concernant la promotion.

La séquence des étapes du canvas pourrait ressembler à ce qui suit :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs ont pénétré dans le Canvas le 11 juin.
2. Créez une étape Délai qui retient les utilisateurs jusqu'à 13 heures, heure locale, le 17 juin.
3. Reliez l'étape Délai à une autre étape Message qui envoie son message immédiatement.

### Retarder les composants à la fin du Canvas {#delay-as-last-step}

Si vous ajoutez un composant de délai à votre Canvas, mais qu’il n’y a plus d’étape après le composant de délai, tout utilisateur atteignant la dernière étape est automatiquement exclu du Canvas. Ce processus s’applique également si l’heure de l’étape de délai n’a pas encore été atteinte. Cela signifie que les utilisateurs ayant déjà atteint l’étape de délai ne recevront plus les messages que vous ajoutez après l’étape de délai. Cependant, si un utilisateur n’a pas atteint l’étape de délai et qu’un message est ajouté, il recevra ce message.

## Analyse du délai

Les délais disposent de trois statistiques disponibles dans la vue des analyses d’un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| `Entered` | Illustre le nombre total d’accès à l’étape. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape du canvas, deux entrées seront enregistrées. |
| `Proceeded to Next Step` | Illustre le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| `Exited Canvas` | Illustre le nombre d’entrées pour quitter le Canvas et ne pas poursuivre à l’étape suivante. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les séries chronologiques pour ces éléments d'analyse sont disponibles dans la vue du composant développée.

[1]: {% image_buster /assets/img/canvas_delay.png %}
[2]: {% image_buster /assets/img/context_step1.png %}
[3]: {% image_buster /assets/img/context_step2.png %}
