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

Les délais peuvent simplifier votre Canvas. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu’à une date précise, un jour spécifique ou un jour spécifique de la semaine. <br> ![Une étape du canvas avec un délai d'un jour comme première étape du canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Création d'un délai

Pour créer un délai, ajoutez une étape à votre canvas. Faites glisser et déposez le composant de délai depuis la barre latérale, ou cliquez sur le <i class="fas fa-plus-circle"></i> bouton plus en bas d'une étape et sélectionnez **Delay**.

Plusieurs détails doivent être pris en compte lors de la création d’un délai dans votre parcours Canvas.

- La limite de délai est de 30 jours.
- Un composant de délai peut être uniquement relié à une étape suivante.

### Délais personnalisés

{% alert important %}
Les délais personnalisés et les délais prolongés sont en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Sélectionnez la bascule **Personnaliser** le délai pour définir un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour sélectionner la variable contextuelle à retarder.

Imaginons que vous souhaitiez rappeler à vos clients d'acheter du dentifrice dans 30 jours. En combinant une étape Contexte et une étape Délai, vous pouvez sélectionner la variable contextuelle à retarder. Dans ce cas, votre étape Contexte comportera les champs suivants :

- **Nom de la variable contextuelle :** product_reminder_interval
- **Type de données :** Date
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Le "product_reminder_interval" et sa valeur.]({% image_buster /assets/img/context_step1.png %})

Ensuite, comme vous souhaitez rappeler à vos clients qu'ils n'ont que 30 jours à partir de maintenant, vous sélectionnerez **Jusqu'à un jour précis** comme option de délai et vous sélectionnerez **Personnaliser le délai** pour utiliser les informations de l'étape Contexte. Cela signifie que vos utilisateurs seront retardés jusqu'à la variable de contexte sélectionnée.

![Exemple d'utilisation de variables contextuelles avec une étape Delay pour retarder les utilisateurs en fonction de l'intervalle de rappel du produit.]({% image_buster /assets/img/context_step2.png %})

#### Délais prolongés

Vous pouvez désormais prolonger les délais jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré une session à le faire.

### Options de délai temporel

Vous pouvez choisir le type de délai avant le message suivant dans votre Canvas. Vous pouvez définir une durée du délai pour vos utilisateurs jusqu’à une période désignée, ou une date et heure spécifiques.

{% tabs %}
{% tab Après une certaine durée %}

L'option **Après une durée** vous permet de retarder les utilisateurs pendant un certain nombre de secondes, minutes, heures, jours ou semaines, et à une heure spécifique. Par exemple, vous pouvez retarder des utilisateurs pendant quatre heures ou pendant un jour.
  
Prenez en compte la différence entre les calculs des « jours » et des « jours civils ».
  
- Un « jour » comprend 24 heures et est calculé à partir du moment où l’utilisateur entre dans l’étape de délai. 
- Un "jour calendaire" définit un jour comme étant 24 heures après une heure donnée. Lorsqu'un jour calendaire est choisi et que l'heure est spécifiée, vous pouvez choisir de retarder le délai à l'heure de l'entreprise ou à l'heure locale de l'utilisateur. Si aucune heure n'est spécifiée, l'utilisateur sera retardé jusqu'à minuit le jour suivant à l'heure de la société.

Vous pouvez également sélectionner **À un moment précis** pour spécifier quand les utilisateurs avanceront dans la toile. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape Délai. Si cette durée est supérieure à la durée configurée dans les paramètres, nous ajouterons des heures supplémentaires au délai. Par exemple, disons que nous sommes aujourd'hui le 11 décembre et que notre étape Délai est réglée sur **Après une durée d'** une semaine à 8 heures UTC. Si un utilisateur entre dans l'étape de report le 4 décembre, il sera libéré de l'étape de report pour poursuivre son voyage aujourd'hui s'il est entré à l'origine dans l'étape de report avant 8 heures UTC. S'il est entré dans l'étape Délai après cette heure, l'utilisateur sera retardé jusqu'au jour suivant (la prochaine occurrence de cette heure). 

{% endtab %}
{% tab Jusqu'à une date spécifique %}

L'option **Jusqu'à une date spécifique** vous permet de maintenir les utilisateurs dans l'étape jusqu'à une date et une heure spécifiques.

#### Considérations

##### Les utilisateurs ne recevront plus d'étapes ou de messages périmés.

Si la date et l’heure sélectionnées sont déjà passées lors de la progression des utilisateurs vers l’étape de délai, ces derniers quitteront le Canvas. Il peut s'écouler jusqu'à 31 jours entre le début du canvas et les dates choisies pour les étapes "Attendre la date exacte". 

{% alert important %}
Si vous participez à l' [accès anticipé à l'étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), vous pouvez fixer des délais allant jusqu'à 2 ans.
{% endalert %}

Par exemple, les utilisateurs ne recevront pas d'étapes ou d'envois de messages dans ces scénarios :
- L'envoi d'un message est planifié pour le 3 mai à 21 heures, mais l'étape de retardement expire le 3 mai à 9 heures. 
- Une étape du canvas est retardée jusqu'à une heure spécifique dans le fuseau horaire local de l'utilisateur, mais les utilisateurs n'ont pas défini de fuseau horaire dans leur profil utilisateur. Le délai passe alors par défaut au fuseau horaire de l'entreprise pour ces utilisateurs, qui a déjà dépassé l'heure spécifiée. 
  
##### Les utilisateurs quitteront le système si une étape de retard subséquente se trouve dans la ligne de temps d'une étape de retard précédente.

Si le canvas comporte deux étapes de délai utilisant "Attendre la date exacte" mais que la première étape de délai est plus longue que la seconde, les utilisateurs quitteront également le canvas. 

Par exemple, supposons qu'une toile comporte les étapes suivantes :
- Étape 1 : Étape du message
- Étape 2 : Retarder l'étape jusqu'au 13 décembre à 22 heures
- Étape 3 : Étape du message
- Étape 4 : Report de l'étape jusqu'au 13 décembre à 19 heures
- Étape 5 : Étape du message
  
Les utilisateurs qui entrent dans l'étape 4 quitteront le canvas avant de recevoir l'étape 5, car le délai de l'étape 4 fait partie du délai de l'étape 2.

{% endtab %}
{% tab Jusqu'à un jour spécifique de la semaine %}

L'option **Jusqu'à un jour spécifique de la semaine** vous permet de maintenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure précise. Par exemple, vous pouvez retarder des utilisateurs jusqu’au jeudi suivant 16 h, dans le fuseau horaire de l’entreprise. 

Pour configurer cela avec succès, vous devrez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, jeudi), mais après l'heure spécifiée. Vous pouvez choisir soit d’avancer l’utilisateur au même jour ou le conserver jusqu’à la semaine suivante.
{% endtab %}
{% endtabs %}

## Utilisation des étapes de retard

Supposons que nous soyons le 10 juin. Le 11 juin, vous souhaiteriez que les utilisateurs accèdent au Canvas et reçoivent un message concernant une promotion à venir. Puis vous souhaitez conserver les utilisateurs dans le Canvas jusqu’au 17 juin 15 h, heure locale. À 15 h heure locale le 17 juin, vous souhaitez envoyer un message de rappel aux utilisateurs, concernant la promotion.

L'enchaînement des étapes du canvas pourrait ressembler à ce qui suit :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs ont pénétré dans le Canvas le 11 juin.
2. Créez une étape Délai qui retient les utilisateurs jusqu'à 13 heures, heure locale, le 17 juin.
3. Reliez l'étape Délai à une autre étape Message qui envoie son message immédiatement.

### Retarder les composants à la fin du Canvas {#delay-as-last-step}

Si vous ajoutez un composant Délai à votre canvas et qu'il n'y a pas d'étapes ultérieures, tout utilisateur qui atteint la dernière étape sera automatiquement avancé hors du canvas. Ce processus s’applique également si l’heure de l’étape de délai n’a pas encore été atteinte. Cela signifie que les utilisateurs qui ont déjà atteint l'étape Délai ne recevront pas les messages que vous ajoutez après cette étape. Cependant, si un utilisateur n’a pas atteint l’étape de délai et qu’un message est ajouté, il recevra ce message.

## Analyse du délai

Les composants de délai disposent des indicateurs suivants dans la vue analyse/analytique d'un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| _Saisie_ | Illustre le nombre total d’accès à l’étape. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape du canvas, deux entrées seront enregistrées. |
| _A poursuivi vers l’étape suivante_ | Illustre le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| _Utilisateurs sortis du canvas_ | Illustre le nombre d’entrées pour quitter le Canvas et ne pas poursuivre à l’étape suivante. |
| _Échec de la personnalisation_ | Reflète le nombre de fois où un message ou un contenu personnalisé destiné à un utilisateur n'a pas pu être délivré pour les raisons suivantes :<br> {::nomarkdown}<ul><li>La valeur du délai est dans le passé</li><li>La valeur du délai est supérieure à 2 ans dans le futur</li><li>La valeur <b>Après une certaine durée</b> n’est pas un nombre</li><li>La valeur <b>Jusqu'à un jour donné</b> n’est pas une date ou une chaîne de caractères de format date.</li></ul>{:/} <br>Pour plus de détails, voir les [erreurs de personnalisation qui ont échoué](#personaliztion-failed-errors). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les séries chronologiques pour ces éléments d'analyse sont disponibles dans la vue du composant développée.

## Résolution des problèmes

### Erreurs de personnalisation échouées

Si les utilisateurs ne déclenchent pas de délai personnalisé, c'est peut-être parce que l'étape Contexte que vous avez définie pour les qualifier pour l'étape Délai ne fonctionne pas comme vous l'espériez. Lorsqu'une [variable de contexte n'est pas valide]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), l'utilisateur poursuivra son parcours dans votre canvas sans que son contexte n'ait été défini par l'étape du canvas. Ils risquent ainsi de ne pas pouvoir bénéficier des étapes ultérieures de votre Canvas, comme les délais de personnalisation.

