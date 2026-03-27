---
nav_title: Délai 
article_title: Délai 
alias: "/delay_step/"
page_order: 8
page_type: reference
description: "Cet article de référence aborde la façon d'ajouter un délai à votre Canvas sans avoir à ajouter un message associé."
tool: Canvas

---

# Délai

> Les composants de délai vous permettent d'ajouter un délai indépendant à un Canvas. Vous pouvez ajouter un délai à votre Canvas sans avoir à ajouter un message associé. 

Les délais peuvent simplifier votre Canvas. Vous pouvez également utiliser ce composant pour retarder une étape différente jusqu'à une date précise, un jour spécifique ou un jour spécifique de la semaine. Un composant de délai peut être relié à une seule étape suivante au maximum. <br> ![Une étape de délai d'un jour comme première étape d'un Canvas.]({% image_buster /assets/img/canvas_delay.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

## Création d'un délai

Pour créer un délai, ajoutez une étape à votre Canvas. Faites glisser et déposez le composant de délai depuis la barre latérale, ou cliquez sur le <i class="fas fa-plus-circle"></i> bouton plus en bas d'une étape et sélectionnez **Delay**.

#### Délais prolongés

Vous pouvez désormais prolonger les étapes de délai jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application lors de l'onboarding, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré de session.

## Types de délai

Vous pouvez choisir le type de délai avant le message suivant dans votre Canvas. Vous pouvez définir une durée de délai pour vos utilisateurs jusqu'à une période désignée, ou retarder vos utilisateurs jusqu'à une date et une heure spécifiques.

{% tabs %}
{% tab Duration %}

La sélection de **Durée** vous permet de retarder les utilisateurs pendant un nombre défini de secondes, minutes, heures, jours ou semaines, et à une heure précise. Par exemple, vous pouvez retarder des utilisateurs pendant quatre heures ou pendant un jour.
  
Prenez en compte la différence entre les calculs des « jours » et des « jours civils ».
  
- Un « jour » correspond à 24 heures et est calculé à partir du moment où l'utilisateur accède à l'étape Délai. 
- Un « jour civil » définit le temps à attendre jusqu'à la prochaine heure spécifiée, qui peut être inférieure à 24 heures. Vous avez la possibilité de retarder à l'heure de l'entreprise ou à l'heure locale de l'utilisateur. Si aucune heure n'est spécifiée, l'utilisateur sera retardé jusqu'à minuit le jour suivant à l'heure de la société.

Vous pouvez également sélectionner **À un moment précis** pour spécifier quand les utilisateurs avanceront dans le Canvas. Cette option prend en compte l'heure à laquelle l'utilisateur est entré dans l'étape Délai. Si cette heure dépasse l'heure configurée dans les paramètres, des heures supplémentaires seront ajoutées au délai. 

À titre d'exemple, supposons que nous sommes aujourd'hui le 11 décembre et que notre étape de délai est définie sur une **Durée** d'une semaine à 8 h UTC. Si un utilisateur entre dans l'étape de délai le 4 décembre, il sera libéré de l'étape de délai pour poursuivre son parcours aujourd'hui s'il est entré à l'origine dans l'étape de délai avant 8 h UTC. S'il est entré dans l'étape Délai après cette heure, l'utilisateur sera retardé jusqu'au jour suivant (la prochaine occurrence de cette heure). 

{% endtab %}
{% tab Calendar date %}

En sélectionnant **Date du calendrier**, vous pouvez maintenir les utilisateurs dans cette étape jusqu'à une date et une heure spécifiques.

#### Considérations

##### Les utilisateurs ne recevront pas d'étapes ou de messages dont la date est passée

Si la date et l'heure sélectionnées sont déjà passées lors de la progression des utilisateurs vers l'étape de délai, ces derniers quitteront le Canvas. Il peut y avoir jusqu'à 31 jours entre le début du Canvas et les dates choisies pour les étapes « attendre jusqu'à un jour précis ».

{% alert important %}
Si vous participez à l'[accès anticipé Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), vous pouvez définir des délais allant jusqu'à deux ans.
{% endalert %}

Par exemple, les utilisateurs ne recevront pas d'étapes ou de messages dans ces scénarios :

- Un message est prévu pour être envoyé le 3 mai à 21 h, mais l'étape Délai expire le 3 mai à 9 h. 
- Une étape du Canvas est retardée jusqu'à une heure spécifique dans le fuseau horaire local de l'utilisateur, mais les utilisateurs n'ont pas défini de fuseau horaire dans leur profil utilisateur. Le délai passe alors par défaut au fuseau horaire de l'entreprise pour ces utilisateurs, qui a déjà dépassé l'heure spécifiée. 
  
##### Les utilisateurs quitteront le Canvas si une étape de délai subséquente se trouve dans la chronologie d'une étape de délai précédente

Si le Canvas comporte deux étapes de délai, mais que la première étape de délai est plus longue que la seconde, les utilisateurs quitteront également le Canvas. 

Par exemple, supposons qu'un Canvas comporte les étapes suivantes :
- Étape 1 : Étape Message
- Étape 2 : Étape Délai jusqu'au 13 décembre à 22 h
- Étape 3 : Étape Message
- Étape 4 : Étape Délai jusqu'au 13 décembre à 19 h
- Étape 5 : Étape Message
  
Les utilisateurs qui entrent dans l'étape 4 quitteront le Canvas avant de recevoir l'étape 5, car le délai de l'étape 4 fait partie de la chronologie de l'étape 2.

{% endtab %}
{% tab Day of the week %}

En sélectionnant **Jour de la semaine**, vous pouvez retenir les utilisateurs dans l'étape jusqu'à un jour spécifique de la semaine, à une heure précise. Par exemple, vous pouvez retarder des utilisateurs jusqu'au jeudi suivant à 16 h, dans le fuseau horaire de l'entreprise. 

Pour configurer cela correctement, vous devrez également sélectionner ce qui se passe si l'utilisateur entre dans le Canvas le jour de la semaine sélectionné (par exemple, jeudi), mais après l'heure spécifiée. Vous pouvez choisir soit d'avancer l'utilisateur le même jour, soit de le retenir jusqu'à la semaine suivante.
{% endtab %}
{% endtabs %}

## Utilisation des étapes de délai

Supposons que nous soyons le 10 juin. Le 11 juin, vous souhaiteriez que les utilisateurs accèdent au Canvas et reçoivent un message concernant une promotion à venir. Puis vous souhaitez conserver les utilisateurs dans le Canvas jusqu'au 17 juin à 15 h, heure locale. À 15 h heure locale le 17 juin, vous souhaitez envoyer un message de rappel aux utilisateurs concernant la promotion.

L'enchaînement des étapes du Canvas pourrait ressembler à ce qui suit :

1. Commencez par ajouter une étape Message qui s'envoie immédiatement après que les utilisateurs sont entrés dans le Canvas le 11 juin.
2. Créez une étape Délai qui retient les utilisateurs jusqu'à 13 h, heure locale, le 17 juin.
3. Reliez l'étape Délai à une autre étape Message qui envoie son message immédiatement.

### Composants de délai à la fin d'un Canvas {#delay-as-last-step}

Si vous ajoutez un composant Délai à votre Canvas et qu'il n'y a pas d'étapes ultérieures, tout utilisateur qui atteint la dernière étape sera automatiquement avancé hors du Canvas. Ce processus s'applique même si l'heure de l'étape de délai n'a pas encore été atteinte. Cela signifie que les utilisateurs qui ont déjà atteint l'étape Délai ne recevront pas les messages que vous ajoutez après cette étape. Cependant, si un utilisateur n'a pas atteint l'étape de délai et qu'un message est ajouté, il recevra ce message.

### Délais personnalisés

{% multi_lang_include early_access_beta_alert.md feature='The personalized delays and extended delays feature' %}

Activez la bascule **Personnaliser le délai** pour définir un délai personnalisé pour vos utilisateurs. Vous pouvez l'utiliser avec une [étape Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour sélectionner la variable de contexte à utiliser pour le délai. Cela remplacera l'heure définie dans l'attribut ou la propriété sélectionné(e). Cette fonctionnalité est utile lorsque vous appliquez un décalage en jours ou en semaines et que vous souhaitez que les utilisateurs avancent à un moment précis. Le fuseau horaire provient de l'attribut ou de la propriété, ou utilise la valeur de repli si aucun n'est disponible. 

#### Comportement du fuseau horaire pour « à une heure précise »

Lors de la configuration de délais personnalisés avec l'option **à une heure précise**, le comportement du fuseau horaire dépend du type de données de votre attribut ou variable de contexte :

- **Type de données chaîne de caractères avec fuseau horaire :** Si l'attribut ou la variable de contexte est un type de données chaîne de caractères qui inclut des informations de fuseau horaire, il se conforme au fuseau horaire spécifié dans la chaîne de caractères. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC-8.
- **Type de données chaîne de caractères sans fuseau horaire :** Si l'attribut ou la variable de contexte est un type de données chaîne de caractères sans informations de fuseau horaire, il se conforme au fuseau horaire de repli. Par exemple, `2025-06-10` utilise le fuseau horaire de repli.
- **Type de données temporelles :** Si l'attribut ou la variable de contexte est de type données temporelles, il est conforme à l'UTC. En effet, le type de données temporelles est toujours converti en UTC lorsqu'il est enregistré dans la base de données. Par conséquent, « à une heure précise » fera toujours référence à l'UTC lorsque la variable est définie sur le type de données temporelles. Par exemple, `2025-06-10T10:00:00-08:00` utilise UTC+0.

{% alert note %}
Il est possible qu'un attribut personnalisé ou une variable de contexte ne dispose ni d'une heure spécifique ni d'un fuseau horaire s'il s'agit d'un type de données chaîne de caractères. S'il s'agit d'un type de données temporelles, il est nécessaire de préciser l'heure et le fuseau horaire. Cependant, si l'attribut personnalisé ou la variable de contexte est une chaîne de caractères « non pertinente » (telle que « product_name »), l'utilisateur quittera le Canvas.
{% endalert %}

#### Cas d'utilisation

Imaginons que vous souhaitiez rappeler à vos clients d'acheter du dentifrice dans 30 jours. En combinant une étape Contexte et une étape Délai, vous pouvez sélectionner la variable de contexte à utiliser pour le délai. Dans ce cas, votre étape Contexte comportera les champs suivants :

- **Nom de la variable de contexte :** product_reminder_interval
- **Type de données :** Date
- **Valeur :** {% raw %}`{{custom_attribute.${Order_filled_time}}}`{% endraw %}

![Le « product_reminder_interval » et sa valeur.]({% image_buster /assets/img/context_step1.png %})

Ensuite, comme vous souhaitez rappeler à vos clients dans 30 jours, vous sélectionnerez **Jusqu'à un jour précis** comme option de délai et vous activerez **Personnaliser le délai** pour utiliser les informations de l'étape Contexte. Vos utilisateurs seront ainsi retardés jusqu'à la variable de contexte sélectionnée.

## Analyse du délai

Les composants de délai disposent des indicateurs suivants dans la vue analytique d'un Canvas actif ou précédemment actif.

| Indicateur | Description |
|---|---|
| _Entrées_ | Reflète le nombre de fois où l'étape a été atteinte. Si votre Canvas est rééligible et qu'un utilisateur entre deux fois dans une étape de délai, deux entrées seront enregistrées. |
| _A poursuivi vers l'étape suivante_ | Reflète le nombre d'entrées ayant progressé vers l'étape suivante dans le Canvas. |
| _Sortie du Canvas_ | Reflète le nombre d'entrées ayant quitté le Canvas sans poursuivre vers l'étape suivante. |
| _Échec de la personnalisation_ | Reflète le nombre de fois où un message ou un contenu personnalisé destiné à un utilisateur n'a pas pu être délivré pour les raisons suivantes :<br> {::nomarkdown}<ul><li>La valeur du délai est dans le passé</li><li>La valeur du délai est supérieure à 2 ans dans le futur</li><li>La valeur <b>Après une certaine durée</b> n'est pas un nombre</li><li>La valeur <b>Jusqu'à un jour précis</b> n'est pas une date ou une chaîne de caractères au format date</li></ul>{:/} <br>Pour plus de détails, consultez les [erreurs d'échec de personnalisation](#personaliztion-failed-errors). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les séries chronologiques pour ces indicateurs sont disponibles dans la vue développée du composant.

## Résolution des problèmes

### Erreurs d'échec de personnalisation

Si les utilisateurs ne déclenchent pas un délai personnalisé, c'est peut-être parce que l'étape Contexte que vous avez définie pour les qualifier pour l'étape Délai ne fonctionne pas comme prévu. Lorsqu'une [variable de contexte n'est pas valide]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#troubleshooting), l'utilisateur poursuivra son parcours dans votre Canvas sans que son contexte n'ait été défini par l'étape Contexte. Ils risquent ainsi de ne pas remplir les conditions requises pour les étapes ultérieures de votre Canvas, comme les délais personnalisés.