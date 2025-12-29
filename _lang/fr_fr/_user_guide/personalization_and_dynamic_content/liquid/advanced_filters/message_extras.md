---
nav_title: "Étiquette d'envoi de messages supplémentaires"
article_title: Message Extras Tag
page_order: 1
description: "Cet article explique comment utiliser l'étiquette Liquid d'envoi de messages et comment vérifier la syntaxe."
alias: "/message_extras_tag/"
---

# Suppléments de message Étiquette Liquid

> Utilisez l'étiquette Liquid `message_extras` pour annoter vos événements d'envoi avec des données dynamiques provenant de contenus connectés, de catalogues, d'attributs personnalisés (tels que la langue, le pays), de propriétés d'entrée Canvas ou d'autres sources de données.

L'étiquette Liquid `message_extras` ajoute des paires clé-valeur à l'événement d'envoi correspondant dans Currents et Snowflake Data Sharing. 

Pour renvoyer des données dynamiques ou supplémentaires à votre événement d'envoi de partage de données Currents ou Snowflake, insérez l'étiquette Liquid appropriée dans le corps de votre message. 

Voici un exemple de format d'étiquette Liquid standard pour `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Vous pouvez ajouter ces tags si nécessaire pour vos paires clé-valeur dans le corps du message. Toutefois, la longueur de toutes les clés et valeurs ne doit pas dépasser 1 Ko. Dans Currents et Snowflake Data Sharing, vous verrez un nouveau champ d'événement appelé `message_extras` pour vos événements d'envoi. Cela générera une chaîne de caractères sérialisée JSON dans un champ.

## Canaux pris en charge

L'étiquette `message_extras` est prise en charge pour tous les types de messages avec un événement d'envoi, ainsi que pour les événements d'impression de messages in-app. L'utilisation de `message_extras` avec des messages in-app nécessite le respect de certaines [versions minimales du SDK](#iam-sdk).

## Comment utiliser l'étiquette `message_extras`?

1. Dans le corps du message pour le canal, entrez l'étiquette Liquid `message_extras`. Vous pouvez également utiliser la fenêtre modale/boîte de dialogue de l'**ajout de personnalisation** et sélectionner " **Message Extras"** pour le type de personnalisation. 

\![La fenêtre modale/boîte de dialogue de la personnalisation, avec l'option Message Extras sélectionnée comme type de personnalisation.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Saisissez la [paire clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour chaque étiquette `message_extras`. 

\![Exemple de paire clé-valeur pour l'étiquette d'envoi de messages. Le champ du titre indique "Vos nouveaux favoris". Le message lit les paires clé-valeur pour l'étiquette des extras du message et la phrase suivante : "Nous sommes ravis de vous apporter une sélection latérale de produits frais et passionnants qui deviendront certainement vos nouveaux favoris."]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Après l'envoi de votre campagne ou de votre canvas, Braze joint les données dynamiques au moment de l'envoi via les événements d'envoi de Currents ou de Snowflake Data Sharing au champ `message_extras`.

## Vérification de la syntaxe

Toute autre entrée qui ne correspond pas à la norme d'étiquette mentionnée ci-dessus peut ne pas être transmise à Currents ou à Snowflake. Vérifiez que votre syntaxe ou votre formatage ne comporte aucun des éléments suivants :

- Délimiteurs inexistants, vides ou mal saisis
- Doubles clés (Braze enverra par défaut la paire clé-valeur rencontrée en premier).
- Texte supplémentaire avant la définition des clés ou des valeurs
- Clés et valeurs en désordre 
  - {% raw %}Par exemple, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Envoi d'informations sur les codes de promotion à Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Considérations

- Si vos valeurs-clés dépassent 1 Ko, elles seront tronquées. 
- Les espaces blancs sont pris en compte dans le nombre de caractères. Notez que Braze omet les espaces blancs de début et de fin.
- Le fichier JSON résultant ne contiendra que des chaînes de caractères.
- Vous pouvez inclure des variables Liquid en tant que clé ou valeur, mais vous ne pouvez pas utiliser d'autres étiquettes Liquid dans `message_extras`.
  - Par exemple, vous pouvez utiliser le Liquid suivant : {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Questions fréquemment posées

#### Comment puis-je associer le champ message_extras dans les événements d'envoi à mes événements d'engagement comme les ouvertures et les clics ? 

Un `dispatch_id` est généré et fourni dans vos événements d'envoi, qui peut être utilisé comme identifiant unique pour relier des événements spécifiques de clic, d'ouverture ou de livraison. Vous pourrez utiliser et interroger ce champ dans Currents ou Snowflake. En savoir plus sur le [comportement de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### Puis-je utiliser message_extras avec des messages in-app ? {#iam-sdk}

Oui, vous pouvez utiliser `message_extras` dans vos messages in-app à condition que les appareils de vos utilisateurs disposent des versions minimales suivantes du SDK :

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

