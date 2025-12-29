---
nav_title: Délai 
article_title: Délai 
alias: "/delay_step/"
page_order: 3
page_type: reference
description: "Cet article de référence explique comment ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé."
tool: Canvas

---

# Délai

> Les composants de délai vous permettent d'ajouter un délai autonome à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir besoin d'ajouter un message associé. 

Les retards peuvent rendre votre toile plus propre. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu'à une date exacte, jusqu'à un jour spécifique ou jusqu'à un jour spécifique de la semaine. <br> !Une étape du délai avec un délai d'un jour comme première étape d'un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Création d'un délai

Pour créer un délai, ajoutez une étape à votre canvas. Glissez-déposez le composant Délai depuis la barre latérale, ou cliquez sur le bouton plus <i class="fas fa-plus-circle"></i> au bas d'une étape et sélectionnez **Délai**.

Plusieurs détails sont à prendre en compte lorsque vous créez un délai dans votre parcours Canvas.

- Le délai est de 30 jours.
- Un composant Delay ne peut être connecté qu'à une seule étape suivante.

#### Délais prolongés

Vous pouvez désormais prolonger les délais jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré une session à le faire.

## Types de temporisation

Vous pouvez choisir le type de délai avant le prochain message dans votre Canvas. Vous pouvez soit fixer un délai pour vos utilisateurs jusqu'à la fin d'une période donnée, soit retarder vos utilisateurs jusqu'à une date et une heure spécifiques.

{% tabs %}
{% tab Duration %}

Le choix de la **durée** vous permet de retarder les utilisateurs pendant un certain nombre de secondes, de minutes, d'heures, de jours ou de semaines, et à une heure précise. Par exemple, vous pouvez retarder les utilisateurs de quatre heures ou d'un jour.
  
Notez la différence entre le mode de calcul des "jours" et des "jours calendaires".
  
- Un "jour" correspond à 24 heures et est calculé à partir de l'heure à laquelle l'utilisateur entre dans l'étape Délai. 
- Un "jour calendrier" définit le temps à attendre jusqu'à la prochaine heure spécifiée, qui peut être inférieure à 24 heures. Vous pouvez choisir de retarder l'heure de l'entreprise ou l'heure locale de l'utilisateur. Si aucune heure n'est spécifiée, l'utilisateur sera retardé jusqu'à minuit le jour suivant à l'heure de la société.

Vous pouvez également sélectionner **À un moment précis** pour spécifier quand les utilisateurs avanceront dans la toile. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape Délai. Si cette durée est supérieure à la durée configurée dans les paramètres, nous ajouterons des heures supplémentaires au délai. 

Par exemple, disons que nous sommes aujourd'hui le 11 décembre et que notre étape Délai est réglée sur **Durée d'** une semaine à 8 heures UTC. Si un utilisateur entre dans l'étape de report le 4 décembre, il sera libéré de l'étape de report pour poursuivre son voyage aujourd'hui s'il est entré à l'origine dans l'étape de report avant 8 heures UTC. S'il est entré dans l'étape Délai après cette heure, l'utilisateur sera retardé jusqu'au jour suivant (la prochaine occurrence de cette heure). 

{% endtab %}
{% tab Calendar date %}

La sélection de la **date du calendrier** vous permet de maintenir les utilisateurs dans l'étape jusqu'à une date et une heure spécifiques.

#### Considérations

##### Les utilisateurs ne recevront plus d'étapes ou de messages périmés.

Si la date et l'heure sélectionnées sont déjà passées au moment où les utilisateurs passent à l'étape du canvas, ils quitteront le canvas. Il peut s'écouler jusqu'à 31 jours entre le début du canvas et les dates choisies pour les étapes "attendre un jour précis".

{% alert important %}
Si vous participez à l' [accès anticipé à Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), vous pouvez fixer des délais allant jusqu'à deux ans.
{% endalert %}

Par exemple, les utilisateurs ne recevront pas d'étapes ou d'envois de messages dans ces scénarios :

- L'envoi d'un message est planifié pour le 3 mai à 21 heures, mais l'étape du délai expire le 3 mai à 9 heures. 
- Une étape du canvas est retardée jusqu'à une heure spécifique dans le fuseau horaire local de l'utilisateur, mais les utilisateurs n'ont pas défini de fuseau horaire dans leur profil utilisateur. Le délai passe alors par défaut au fuseau horaire de l'entreprise pour ces utilisateurs, qui a déjà dépassé l'heure spécifiée. 
  
##### Les utilisateurs quitteront le système si une étape de retard subséquente se trouve dans la ligne de temps d'une étape de retard précédente.

Si le canvas comporte deux étapes de délai, mais que la première étape de délai est plus longue que la seconde, les utilisateurs quitteront également le canvas. 

Par exemple, supposons qu'une toile comporte les étapes suivantes :
- Étape 1 : Étape du message
- Étape 2 : Retarder l'étape jusqu'au 13 décembre à 22 heures
- Étape 3 : Étape du message
- Étape 4 : Report de l'étape jusqu'au 13 décembre à 19 heures
- Étape 5 : Étape du message
  
Les utilisateurs qui entrent dans l'étape 4 quitteront le canvas avant de recevoir l'étape 5, car le délai de l'étape 4 fait partie du délai de l'étape 2.

{% endtab %}
{% tab Day of the week %}

La sélection de l'option **Jour de la semaine** vous permet de maintenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure spécifique. Par exemple, vous pouvez retarder les utilisateurs jusqu'au prochain jeudi à 16 heures dans le fuseau horaire de l'entreprise. 

Pour réussir cette configuration, vous devrez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, le jeudi), mais après l'heure spécifiée. Vous pouvez choisir d'avancer l'utilisateur le jour même ou de le mettre en attente jusqu'à la semaine suivante.
{% endtab %}
{% endtabs %}

## Utilisation des étapes de retard

Disons que nous sommes le 10 juin. Le 11 juin, vous souhaitez que les utilisateurs entrent dans le canvas et reçoivent un message concernant une promotion à venir. Ensuite, vous voulez maintenir les utilisateurs dans la toile jusqu'au 17 juin à 15 heures, heure locale. Le 17 juin à 15 heures (heure locale), vous souhaitez envoyer aux utilisateurs un message de rappel concernant la promotion.

L'enchaînement des étapes du canvas pourrait ressembler à ce qui suit :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs ont pénétré dans le Canvas le 11 juin.
2. Créez une étape Délai qui retient les utilisateurs jusqu'à 13 heures, heure locale, le 17 juin.
3. Reliez l'étape Délai à une autre étape Message qui envoie son message immédiatement.

### Retarder les composants à la fin d'un canvas {#delay-as-last-step}

Si vous ajoutez un composant Délai à votre canvas et qu'il n'y a pas d'étapes ultérieures, tout utilisateur qui atteint la dernière étape sera automatiquement avancé hors du canvas. Ceci est vrai même si le temps de l'étape Delay n'a pas encore été atteint. Cela signifie que les utilisateurs qui ont déjà atteint l'étape Délai ne recevront pas les messages que vous ajoutez après cette étape. Toutefois, si un utilisateur n'a pas atteint l'étape du délai et qu'un message est ajouté, il recevra ce message.

### Délais personnalisés

{% alert important %}
Les délais personnalisés et les délais prolongés sont en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Sélectionnez la bascule **Personnaliser** le délai pour définir un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour sélectionner la variable contextuelle à retarder. Cette option remplace l'heure définie dans l'attribut ou la propriété sélectionné(e). Cette fonction est utile lorsque vous appliquez un décalage en jours ou en semaines et que vous souhaitez que les utilisateurs avancent à un moment précis. Le fuseau horaire provient de l'attribut ou de la propriété, ou utilise la solution de remplacement si aucune n'est disponible. 

#### Comportement en fonction du fuseau horaire pour "à une heure précise"

Lorsque vous configurez des délais personnalisés avec l'option **à une heure précise**, le comportement du fuseau horaire dépend du type de données de votre attribut ou de votre variable contextuelle :

- **Chaîne de caractères avec le fuseau horaire :** Si l'attribut ou la variable de contexte est un type de données de type chaîne de caractères qui comprend des informations sur le fuseau horaire, il se conforme au fuseau horaire spécifié dans la chaîne de caractères. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC-8.
- **Chaîne de caractères sans fuseau horaire :** Si l'attribut ou la variable de contexte est un type de données de type chaîne de caractères sans information sur le fuseau horaire, il se conforme au fuseau horaire de repli. Par exemple, `2025-06-10` utilise le fuseau horaire de repli.
- **Type de données temporelles :** Si l'attribut ou la variable de contexte est un type de données temporelles, il est conforme à UTC. En effet, le type de données "time" est toujours converti en UTC lorsqu'il est enregistré dans la base de données, de sorte que "at specific time" fera toujours référence à UTC lorsque la variable est définie dans le type de données "time". Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC+0.

{% alert note %}
Il est possible qu'un attribut personnalisé ou une variable contextuelle n'ait ni heure spécifique ni fuseau horaire s'il s'agit d'une donnée de type chaîne de caractères. S'il s'agit d'un type de données temporelles, vous devrez spécifier l'heure et le fuseau horaire. Toutefois, si l'attribut personnalisé ou la variable contextuelle est une chaîne de caractères "non pertinente" (telle que "product_name"), ), l'utilisateur quittera le Canvas.
{% endalert %}

#### Cas d'utilisation

Imaginons que vous souhaitiez rappeler à vos clients d'acheter du dentifrice dans 30 jours. En combinant une étape Contexte et une étape Délai, vous pouvez sélectionner la variable contextuelle à retarder. Dans ce cas, votre étape Contexte comportera les champs suivants :

- **Nom de la variable contextuelle :** product_reminder_interval
- **Type de données :** L'heure
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

\![Le site "product_reminder_interval" et sa valeur.]({% image_buster /assets/img/context_step1.png %})

Ensuite, comme vous souhaitez rappeler à vos clients qu'ils n'ont que 30 jours à partir de maintenant, vous sélectionnerez **Jusqu'à un jour précis** comme option de délai et vous sélectionnerez **Personnaliser le délai** pour utiliser les informations de l'étape Contexte. Cela signifie que vos utilisateurs seront retardés jusqu'à la variable de contexte sélectionnée.

## Analyse/analytique des retards (si utilisé anjective)

Les composants de délai disposent des indicateurs suivants dans la vue analyse/analytique d'un Canvas actif ou précédemment actif.

| Indicateurs | Description |
|---|---|
| _Entré_ | Reflète le nombre de fois que l'étape a été saisie. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape du canvas, deux entrées seront enregistrées. |
| _Passage à l'étape suivante_ | Reflète le nombre d'entrées qui sont passées à l'étape suivante du canvas. |
| _Exited Canvas_ | Reflète le nombre d'entrées qui ont quitté le canvas et ne sont pas passées à l'étape suivante. |
| _Échec de la personnalisation_ | Reflète le nombre de fois où un message ou un contenu personnalisé destiné à un utilisateur n'a pas pu être délivré pour les raisons suivantes :<br> {::nomarkdown}<ul><li>La valeur du délai est dans le passé</li><li>La valeur du délai est supérieure à 2 ans dans le futur</li><li><b>Après une</b> valeur de <b>durée</b> qui n'est pas un nombre</li><li><b>Jusqu'à ce que la</b> valeur d'<b>un jour donné</b> ne soit pas une date ou une chaîne de caractères formatée par la date.</li></ul>{:/} <br>Pour plus de détails, voir les [erreurs de personnalisation qui ont échoué](#personaliztion-failed-errors). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les séries temporelles pour ces analyses/analytiques sont disponibles dans la vue élargie des composants.

## Résolution des problèmes

### Erreurs de personnalisation échouées

Si les utilisateurs ne déclenchent pas de délai personnalisé, c'est peut-être parce que l'étape Contexte que vous avez définie pour les qualifier pour l'étape Délai ne fonctionne pas comme vous l'espériez. Lorsqu'une [variable de contexte n'est pas valide]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), l'utilisateur poursuivra son parcours dans votre canvas sans que son contexte n'ait été défini par l'étape du canvas. Ils risquent ainsi de ne pas pouvoir bénéficier des étapes ultérieures de votre Canvas, comme les délais de personnalisation.

