---
nav\_title : Lignes directrices de la marque article\_title : Lignes directrices de la marque page\_order : 1 page\_type : référence description : "Cet article de référence décrit comment créer, gérer et utiliser les buidelines de marque qui peuvent être appliquées à vos messages grâce à l'assistant de rédaction de l'intelligence artificielle."
---

# Lignes directrices de la marque

> Adaptez le style de vos textes générés par l'intelligence artificielle à la voix, au ton et à la personnalité de votre marque grâce à des directives de marque personnalisées.

Vous pouvez créer et gérer vos directives de marque en allant dans **Paramètres** > **Directives de marque.** Vous pouvez également les créer dans l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).

## Créer des lignes directrices pour la marque

### Étape 1 : Créer une directive de marque

Sur la page **Lignes directrices de la marque**, sélectionnez **Créer un nouveau**. Si vous souhaitez que cette directive de marque soit la directive par défaut de l'espace de travail, cochez la case **Utiliser comme directive de marque par défaut**. Vous ne pouvez avoir qu'une seule valeur par défaut par espace de travail.

### Étape 2 : Décrire la personnalité de votre marque

Pour la **personnalité de la marque**, réfléchissez à ce qui rend votre marque unique. Incluez les caractéristiques, les valeurs, la voix et tous les archétypes qui définissent votre marque. Voici quelques caractéristiques à prendre en compte :

| **Caractéristique** | **Définition** | **Exemple** | |--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------| | Réputation | Comment vous souhaitez que votre marque soit perçue sur le marché. | Nous sommes connus pour être la marque la plus fiable et la plus orientée vers le client dans notre secteur d'activité. | Traits de personnalité | Caractéristiques humaines qui décrivent le caractère de votre marque. | Nous sommes connus pour être la marque la plus fiable et la plus orientée vers le client dans notre secteur d'activité. | Valeurs - Les valeurs fondamentales qui guident les actions et les décisions de votre marque. | Nous accordons de l'importance à la durabilité, à la transparence et à la communauté. | Différenciation - Qualités uniques qui distinguent votre marque de ses concurrents. | Nous nous distinguons en offrant un service client personnalisé qui va au-delà des attentes. | Voix de la marque | Le ton et le style de communication utilisés par votre marque. | Notre voix est décontractée mais informative, assurant la clarté sans être trop formelle. | La voix de votre marque est celle d'une personne qui s'identifie à votre marque et qui la représente. | Nous incarnons l'archétype de l'explorateur, toujours à la recherche de nouveaux défis et de nouvelles aventures. | { : .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Définir le langage à éviter (facultatif)

Pour les **exclusions**, énumérez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous voudrez peut-être éviter le « sarcasme », les « attitudes négatives » ou le ton « condescendant ».

La fenêtre "Créer une ligne directrice de marque" avec des champs pour saisir le nom, la description, la personnalité, les exclusions et le ton]\[1].

### Étape 4 : Tester vos directives

Testez vos directives pour en évaluer le résultat. Développez la section **Tester vos directives** pour générer des exemples de textes et, le cas échéant, les peaufiner.

### Étape 5 : Enregistrer vos directives

Lorsque vous êtes satisfait de vos directives, sélectionnez **Enregistrer la directive de marque**. Vos nouvelles directives seront enregistrées dans votre espace de travail pour une utilisation ultérieure.

{% alert important %} Vous pouvez changer la langue de sortie quelle que soit la langue de votre copie, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser. {% endalert %}

## Gérer les lignes directrices de la marque

Vous pouvez modifier les directives de marque en les sélectionnant sur la page **Directives de marque.**  Archivez une directive de marque pour la rendre inactive et la supprimer de l'assistant de rédaction de l'intelligence artificielle. Pour la rendre à nouveau active et sélectionnable, vous pouvez filtrer les directives de marque archivées et les désarchiver.

La page "Lignes directrices de la marque" a filtré les lignes directrices de la marque archivées]\[4].

## Utiliser les lignes directrices de la marque

Lors de la rédaction d'un message, ouvrez l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/) et sélectionnez votre directive de marque dans le menu déroulant **Appliquer la directive de marque**. Si vous désignez une ligne directrice spécifique comme ligne par défaut, elle sera automatiquement sélectionnée dans la liste déroulante, mais vous pouvez choisir une autre ligne directrice. 

\!["Assistant de rédaction d'intelligence artificielle avec "Alertes importantes ! !!" sélectionné comme ligne directrice de la marque.]\[2].

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Pour générer des copies à l'aide d'une ligne directrice de marque, Braze enverra votre requête, y compris le contenu de votre ligne directrice, à OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans les données que vous fournissez ou dans les données de vos compagnes antérieures si vous activez l’option « Faire référence aux données d’anciennes campagnes ». Conformément à la [politique d'](https://openai.com/policies/api-data-usage-policies)OpenAI, les données envoyées à l'API d'OpenAI à l'aide de Braze ne sont pas utilisées pour former ou améliorer leurs modèles et seront supprimées après 30 jours. Entre vous et Braze, tout contenu généré à l'aide de GPT constitue votre propriété intellectuelle. Braze ne fera valoir aucune revendication de propriété intellectuelle sur ce contenu et ne donne aucune garantie de quelque nature que ce soit concernant tout contenu généré par l’IA.

\[1] : {% image\_buster /assets/img/guidelines\_create.png %} \[2] : {% image\_buster /assets/img/guidelines\_ai\_assistant.png %} \[4] : {% image\_buster /assets/img/unarchive\_brand\_guideline.png %}