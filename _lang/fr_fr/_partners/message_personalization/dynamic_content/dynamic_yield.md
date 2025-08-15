---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Cet article de référence décrit le partenariat entre Braze et Dynamic Yield. Ce partenariat vous permet de tirer parti du moteur de recommandation et de segmentation de Dynamic Yield pour créer des Blocs d'Expérience qui peuvent être intégrés dans les messages Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), une entreprise Mastercard, aide les entreprises de divers secteurs à offrir des expériences client numériques personnalisées, optimisées et synchronisées. Avec [Experience OS](http://www.dynamicyield.com/experience-os) de Dynamic Yield, les marketeurs, les chefs de produit, les développeurs et les équipes digitales peuvent faire correspondre algorithmiquement le contenu, les produits et les offres à chaque client pour accélérer le chiffre d'affaires et la fidélité des clients.

_Cette intégration est maintenue par Dynamic Yield._

## À propos de l'intégration

Le partenariat entre Braze et Dynamic Yield vous permet de tirer parti du moteur de recommandation et de segmentation de Dynamic Yield pour créer des Blocs d'Expérience qui peuvent être intégrés dans les messages Braze. Les blocs d'expérience peuvent être composés de :
- **Blocs de recommandations**: Définir des algorithmes et des filtres pour obtenir le contenu personnalisé des utilisateurs qui se propage lorsque l'e-mail est ouvert. 
- **Blocs de contenu dynamique**: Cibler différentes promotions et messages à différents utilisateurs. Le ciblage peut être basé soit sur l'affinité, soit sur l'audience. Dynamic Yield détermine quelle expérience personnalisée servir lorsque l'e-mail est ouvert. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamic Yield | Un compte [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer un bloc d'expérience

Pour créer un bloc d'expérience dans Dynamic Yield, accédez à **E-mail > E-mails d'expérience > Nouveau**.

Ensuite, sélectionnez **Créer un bloc d'expérience** pour concevoir un bloc de contenu dynamique ou de recommandations à intégrer dans un modèle d'e-mail Braze.<br>![][8]

### Étape 2 : Rédigez le brouillon de votre message

L'image suivante montre un e-mail créé à partir de zéro dans le générateur.<br>![][6]

1. Entrez un nom de campagne, une note et des étiquettes pour la campagne dans la zone d'en-tête.<br><br>
2. Insérer un bloc d'expérience. Ces blocs incluent :
  - [Recommandations](#configure-a-recommendations-block): Un widget offrant aux utilisateurs des recommandations entièrement personnalisées.
  - [Contenu dynamique](#configure-a-dynamic-content-block) : Envoyer divers messages et promotions à différents publics.<br><br>
3. Mettre à jour les paramètres:
  - Utilisez les paramètres d'URL pour suivre les clics dans votre logiciel d'analyse (facultatif). Ajouter des paramètres aux affichages par défaut selon les besoins.
  - Sélectionnez une fenêtre d'attributs, soit sept jours (par défaut) ou un jour.<br><br>
4. Enregistrer et quitter. Vous pouvez revenir pour modifier tous les éléments de votre e-mail à tout moment avant que le code ne soit généré. Après la génération du code, vous pouvez modifier tout ce qui [n'affecte pas le code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurer un bloc de recommandations

Le bloc de recommandations vous permet de définir des algorithmes et des filtres pour obtenir le contenu personnalisé des utilisateurs qui se propage à l'ouverture de l'e-mail. 

1. Faites glisser un bloc de recommandations depuis le volet d'édition dans le corps de votre e-mail.<br><br>
2. Sélectionnez votre algorithme souhaité (popularité, affinité utilisateur, similarité, et plus). En fonction de l'algorithme sélectionné, des options supplémentaires sont affichées : 
  - Si votre recommandation est basée sur la popularité, vous pouvez mélanger les résultats pour éviter de servir la même recommandation à partir de différents e-mails que le spectateur ouvre.
  - D'autres algorithmes, tels que la similarité, s'appuient sur le contexte pour fournir des recommandations nécessitant que vous sélectionniez des éléments à inclure. Ces éléments peuvent être ajoutés dans le générateur ou [ajouter une étiquette de fusion au code d'intégration](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) pour le rendre dynamique, par exemple, pour ajouter des éléments similaires dans les e-mails de confirmation d'expédition. <br><br>
3. Vous pouvez exclure les produits que l'utilisateur a déjà achetés pour éviter de recommander ces produits.<br><br>
4. Vous pouvez ajouter une [règle de filtre personnalisé](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) pour épingler des produits spécifiques à des emplacements, ou inclure et exclure des produits par propriétés de produit. Par exemple, ne montrez pas de produits qui code moins de 5 $ ou uniquement des produits de la catégorie shorts.<br><br>
5. Enfin, configurez la conception du bloc de recommandation. Pour ce faire, sélectionnez un modèle d'élément, définissez le nombre d'éléments à afficher et en combien de lignes. 

### Configurer un bloc de contenu dynamique
Utilisez le contenu dynamique pour cibler différentes promotions et messages à différents utilisateurs. Le ciblage peut être basé soit sur l'affinité, soit sur l'audience. Dynamic Yield détermine quelle expérience personnalisée servir lorsque l'e-mail est ouvert. 

1. Faites glisser un bloc de contenu dynamique depuis le volet d'édition dans le corps de votre e-mail.<br><br> 
2. Sélectionnez un modèle pour la première variation. Vous pouvez maintenant définir des variables de conception et de contenu. Enregistrer la variation une fois terminée. <br>![][4]<br><br> 
3. Définissez l'audience dans le volet de contenu dynamique.<br>![][5]<br><br> 
4. Ajoutez une autre variation pour cibler un autre public spécifique ou tous les utilisateurs. Répétez si nécessaire.<br><br> 
5. Définissez les priorités de vos variations en utilisant les flèches vers le haut et vers le bas. <br><br> 
6. Les priorités déterminent quelle variation est servie lorsqu'un utilisateur est éligible à plus d'une expérience.

### Étape 3 : Intégrez votre e-mail à Braze

Cette intégration vous permet d'ajouter des widgets de recommandation personnalisés et du contenu dynamique alimenté par Dynamic Yield dans vos campagnes d'e-mail Braze. L'intégration de ces campagnes dans les campagnes Braze se fait avec un simple code d'intégration que vous collez dans l'éditeur d'e-mail Braze.

1. Cliquez sur l'icône d'intégration ESP sur la page de la liste des e-mails d'expérience.<br><br> 
2. Entrez le jeton pertinent de Braze qui insère le l’identifiant unique du client et l'ID d’e-mail de l'utilisateur.<br>![][3]
  
Lorsque vous êtes satisfait de votre e-mail, l'étape suivante consiste à générer le code à intégrer dans Braze.
1. Dans **Expérience Emails**, cliquez sur **Générer le code**.<br><br> 
2. Ensuite, cliquez sur **Copier dans le presse-papiers**.<br>![][1]<br><br> 
3. Collez le code dans votre campagne d'e-mail Braze, puis continuez à concevoir, tester et publier votre campagne d'e-mail.


[1]: {% image_buster /assets/img/dynamic_yield/dynamic_yield.png %}
[2]: {% image_buster /assets/img/dynamic_yield/dynamic_yield1.png %}
[3]: {% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %}
[4]: {% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %}
[5]: {% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %}
[6]: {% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %}
[7]: {% image_buster /assets/img/dynamic_yield/dynamic_yield6.png %}
[8]: {% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %}
