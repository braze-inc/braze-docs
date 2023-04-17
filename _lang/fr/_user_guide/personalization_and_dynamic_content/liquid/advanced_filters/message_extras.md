---
nav_title: Balise de suppléments de message
article_title: Balise de suppléments de message
page_order: 1
description: "Cet article explique comment utiliser la balise Liquid de suppléments de message et comment vérifier la syntaxe."
alias: "/message_extras_tag/"
---

# Balise Liquid de suppléments de message

À l’aide de la `message_extras`balise Liquid, vous pouvez annoter vos événements d’envoi avec des données dynamiques à partir du Contenu connecté, des attributs personnalisés (tels que la langue, le pays) et des propriétés d’entrée Canvas. Cette balise Liquid ajoute des paires clé-valeur à l’événement d’envoi correspondant dans Currents.

{% alert important %}
Cette balise Liquid est actuellement en version bêta pour les événements d’envoi d’e-mails, de SMS et de notifications push. Contactez votre gestionnaire du succès des clients Braze si vous souhaitez participer à la bêta. <br><br>

Cela sera pris en charge à l’avenir pour les webhooks et les cartes de contenu. Si vous souhaitez obtenir de l’aide pour les messages dans le navigateur ou in-app, envoyez des commentaires sur le produit à l’aide du [portail du produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

Pour renvoyer des données dynamiques ou supplémentaires à votre événement d’envoi Currents, insérez la balise Liquid appropriée dans le corps de votre message. Voici un exemple du format standard de la balise Liquid pour `message_extras` : 

{% raw %}
```
{% message_extras :key test :value 123 %}
```
{% endraw %}

Vous pouvez ajouter ces balises si nécessaire pour vos paires clé-valeur dans le corps du message. Cependant, la longueur de toutes les clés et valeurs ne doit pas dépasser 1 Ko. Dans Currents, vous verrez un nouveau champ d’événement appelé `message_extras` pour vos événements d’envoi. Il générera une chaîne de caractères sérialisée JSON dans un champ. 

## Comment l’utiliser

1. Dans le corps du message pour le canal, saisissez la balise Liquid `message_extras`. Vous pouvez également utiliser le modal **Add Personalization (Ajouter une personnalisation)** et sélectionner **Message Extras (Suppléments de message)** pour le type de personnalisation. <br>![Le modal Add Personalization (Ajouter une personnalisation) avec Message Extras (Suppléments de message) de sélectionné comme type de personnalisation.][1]{: style="max-width:70%;"}
2. Saisissez la [paire clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour chaque balise `message_extras`. <br>![Un exemple de paires clé-valeur pour la balise de suppléments de message. Le champ de titre indique « Vos nouveaux favoris ». Le message indique les paires clé-valeur pour la balise des suppléments de message ainsi que la phrase suivante : « Nous sommes ravis de vous proposer une sélection de produits frais et passionnants qui deviendront à coup sûr vos nouveaux favoris. »][2]{: style="max-width:70%;"}
3. Une fois votre campagne ou votre Canvas envoyé(e), Braze joindra les données dynamiques au moment de l’envoi à l’aide des événements d’envoi Currents vers le champ `message_extras`.

## Vérifier la syntaxe

Toute autre entrée qui ne correspond pas à la norme de balise susmentionnée peut ne pas être transmise à Currents. Vérifiez que votre syntaxe ou formatage n’inclut pas les éléments suivants :

- Délimiteurs inexistants, vides ou mal saisis
- Clés en double (Braze enverra par défaut la paire clé-valeur rencontrée en premier)
- Texte supplémentaire avant la définition des clés ou des valeurs
- Clés et valeurs désordonnées 
  - {% raw %}For example, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Considérations

- Si vos clé-valeurs dépassent 1 Ko, elles seront tronquées. 
- L’espace blanc comptera dans le nombre de caractères. Notez que Braze omet les espaces blancs de tête et de fin.
- Le JSON résultant ne produira que des valeurs de chaîne de caractères.
- Les variables Liquid peuvent être comprises en tant que clé ou valeur, mais les balises Liquid ne sont pas prises en charge directement. 
  - Par exemple,  {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Foire aux questions

#### Comment puis-je associer le champ message_extras dans les événements d’envoi à mes événements d’engagement tels que les ouvertures et les clics ? 

Un `dispatch_id` est généré et fourni dans vos événements d’envoi, qui peut être utilisé comme identifiant unique pour relier à des événements spécifiques de clic, d’ouverture ou de livraison. Vous pourrez utiliser et interroger ce champ dans Currents ou Snowflake. En savoir plus sur le [ comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

[1]: {% image_buster /assets/img_archive/message_extras1.png %}
[2]: {% image_buster /assets/img_archive/message_extras2.png %}