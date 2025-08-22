---
nav_title: Balise de suppléments de message
article_title: Balise de suppléments de message
page_order: 1
description: "Cet article explique comment utiliser la balise Liquid de suppléments de message et comment vérifier la syntaxe."
alias: "/message_extras_tag/"
---

# Balise Liquid de suppléments de message

> Utilisez l'étiquette Liquid `message_extras` pour annoter vos événements d'envoi avec des données dynamiques provenant de contenus connectés, de catalogues, d'attributs personnalisés (tels que la langue, le pays), de propriétés d'entrée Canvas ou d'autres sources de données.

L'étiquette Liquid `message_extras` ajoute des paires clé-valeur à l'événement d'envoi correspondant dans Currents et le partage de données Snowflake. 

Pour renvoyer des données dynamiques ou supplémentaires à votre événement d'envoi de partage de données Currents ou Snowflake, insérez l'étiquette Liquid appropriée dans le corps de votre message. 

Voici un exemple de format d'étiquette Liquid standard pour `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Vous pouvez ajouter ces balises si nécessaire pour vos paires clé-valeur dans le corps du message. Toutefois, la longueur de toutes les clés et valeurs ne doit pas dépasser 1 Ko. Dans Currents et le partage de données Snowflake, vous verrez un nouveau champ d'événement appelé `message_extras` pour vos événements d'envoi. Il générera une chaîne de caractères sérialisée JSON dans un champ.

## Canaux pris en charge

L'étiquette `message_extras` est prise en charge pour tous les types de messages avec un événement d'envoi, ainsi que pour les événements d'impression de messages in-app. L'utilisation de `message_extras` avec des messages in-app nécessite le respect de certaines [versions minimales du SDK](#iam-sdk).

## Comment utiliser l'étiquette `message_extras`?

1. Dans le corps du message pour le canal, entrez l'étiquette Liquid `message_extras`. Vous pouvez également utiliser la fenêtre modale/boîte de dialogue de l'**ajout de personnalisation** et sélectionner " **Message Extras"** pour le type de personnalisation. 

![La fenêtre modale/boîte de dialogue de la personnalisation avec Message Extras sélectionné comme type de personnalisation.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Saisissez la [paire clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour chaque étiquette `message_extras`. 

![Un exemple de paires clé-valeur pour la balise de suppléments de message. Le champ de titre indique « Vos nouveaux favoris ». Le message indique les paires clé-valeur pour la balise des suppléments de message ainsi que la phrase suivante : "Nous sommes ravis de vous proposer une sélection de produits frais et passionnants qui deviendront certainement vos nouveaux favoris."]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Après l'envoi de votre campagne ou de votre canvas, Braze joint les données dynamiques au moment de l'envoi, via les événements d'envoi de Currents ou le partage de données Snowflake, au champ `message_extras`.

## Vérifier la syntaxe

Toute autre entrée qui ne correspond pas à la norme d'étiquette mentionnée ci-dessus peut ne pas être transmise à Currents ou à Snowflake. Vérifiez que votre syntaxe ou formatage n’inclut pas les éléments suivants :

- Délimiteurs inexistants, vides ou mal saisis
- Clés en double (Braze enverra par défaut la paire clé-valeur rencontrée en premier)
- Texte supplémentaire avant la définition des clés ou des valeurs
- Clés et valeurs désordonnées 
  - {% raw %}Par exemple, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Considérations

- Si vos valeurs-clés dépassent 1 Ko, elles seront tronquées. 
- Les espaces blancs sont pris en compte dans le nombre de caractères. Notez que Braze omet les espaces blancs de tête et de fin.
- Le JSON résultant ne produira que des valeurs de chaîne de caractères.
- Vous pouvez inclure des variables Liquid en tant que clé ou valeur, mais vous ne pouvez pas utiliser d'autres étiquettes Liquid dans `message_extras`.
  - Par exemple, vous pouvez utiliser le Liquid suivant : {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Foire aux questions

#### Comment puis-je associer le champ message_extras dans les événements d'envoi à mes événements d'engagement comme les ouvertures et les clics ? 

Un `dispatch_id` est généré et fourni dans vos événements d’envoi, qui peut être utilisé comme identifiant unique pour relier à des événements spécifiques de clic, d’ouverture ou de livraison. Vous pourrez utiliser et interroger ce champ dans Currents ou Snowflake. En savoir plus sur le [comportement de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### Puis-je utiliser message_extras avec les messages in-app ? {#iam-sdk}

Oui, vous pouvez utiliser `message_extras` dans vos messages in-app à condition que les appareils de vos utilisateurs disposent des versions minimales suivantes du SDK :

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

