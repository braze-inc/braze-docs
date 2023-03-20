---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Cet article de référence présente le partenariat entre Braze et Dynamic Yield. Ce partenariat vous permet de tirer parti du moteur de recommandations et de segmentations de Dynamic Yield pour créer des blocs d’expérience pouvant être intégrés à des messages Braze."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partenaire

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), une société de Mastercard, aide les entreprises de tous les secteurs à offrir des expériences client numériques personnalisées, optimisées et synchronisées. Grâce à l’[Experience OS](http://www.dynamicyield.com/experience-os) de Dynamic Yield, les marketeurs, les gestionnaires de produits, les développeurs et les équipes numériques peuvent faire correspondre du contenu, des produits et des offres à chaque client à l’aide d’algorithmes afin d’accélérer les revenus et la fidélisation des clients.

Le partenariat entre Braze et Dynamic Yield vous permet de tirer parti du moteur de recommandations et de segmentations de Dynamic Yield pour créer des blocs d’expérience pouvant être intégrés à des messages Braze. Les blocs d’expérience peuvent être constitués des éléments suivants :
- **Blocs de recommandations** : Définissez des algorithmes et appliquez des filtres au contenu personnalisé des utilisateurs se propageant lors que l’e-mail est ouvert. 
- **Blocs de contenu dynamique** : Adaptez les promotions et les messages aux différents utilisateurs ciblés. Le ciblage peut être réalisé en fonction de l’affinité ou de l’audience. Dynamic Yield détermine quelle expérience personnalisée offrir lorsque l’e-mail est ouvert. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamic Yield | Un compte [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer un bloc d’expérience

Pour créer un bloc d’expérience dans Dynamic Yield, accédez à **Email > Experience Emails > Create New (E-mail > E-mails d’expérience > Créer nouveau)**.

Ensuite, sélectionnez **Create Experience Block (Créer un bloc d’expérience)** pour concevoir un bloc de contenu dynamique ou de recommandations à intégrer dans un modèle d’e-mail Braze.<br>![][8]

### Étape 2 : Créer vos envois de messages

L’illustration suivante montre la création d’un e-mail à partir de zéro dans le générateur de blocs.<br>![][6]

1. Saisissez un nom de campagne, une remarque et des étiquettes pour la campagne dans la zone d’en-tête.<br><br>
2. Insérez un bloc d’expérience. Ces blocs incluent les éléments suivants :
  - [Recommandations](#configure-a-recommendations-block) : Un gadget offrant aux utilisateurs des recommandations entièrement personnalisées.
  - [Contenu dynamique](#configure-a-dynamic-content-block) : Adaptez les promotions et les messages aux différentes audiences ciblées.<br><br>
3. Mise à jour des paramètres :
  - Utilisez les paramètres de l’URL pour suivre les clics dans votre logiciel d’analyse (facultatif). Ajoutez des paramètres aux affichages par défaut, le cas échéant.
  - Sélectionnez une fenêtre d’attribut, soit sept jours (valeur par défaut), soit un jour.<br><br>
4. Enregistrez et quittez la page. Vous pouvez modifier tous les éléments de votre e-mail à tout moment avant que le code ne soit généré. Une fois le code généré, vous pouvez modifier tous les éléments [n’affectant pas le code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configurer un bloc de recommandations

Le block de recommandations vous permet de définir des algorithmes et d’appliquer des filtres au contenu personnalisé des utilisateurs se propageant lors que l’e-mail est ouvert. 

1. Glissez un bloc de recommandations du volet de modification vers le corps de votre e-mail.<br><br>
2. Sélectionnez l’algorithme souhaité (popularité, affinité de l’utilisateur, similarité, etc.). Selon l’algorithme sélectionné, certaines options sont affichées : 
  - Si vos recommandations se basent sur la popularité, vous pouvez mélanger les résultats pour éviter d’afficher les mêmes recommandations dans des e-mails différents.
  - D’autres algorithmes, comme celui basé sur la popularité, nécessitent du contexte pour offrir des recommandations. Par conséquent, vous devrez sélectionnez des éléments à inclure dans les recommandations. Ces éléments peuvent être ajoutés dans le générateur de blocs, ou vous pouvez [ajouter une balise de fusion pour intégrer du code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) afin de rendre le bloc dynamique, par exemple, pour ajouter des éléments similaires dans les e-mails de confirmation d’expédition. <br><br>
3. Vous pouvez exclure les produits que l’utilisateur a déjà achetés pour éviter de les recommander.<br><br>
4. Vous pouvez ajouter une [règle de filtre personnalisée](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) pour épingler certains produits à des emplacements, ou pour inclure et exclure des produits en fonction de leurs propriétés. Par exemple, ne pas afficher les produits valant moins de 5 USD, ou n’afficher que les produits de la catégorie « shorts ».<br><br>
5. Enfin, configurez le design du bloc de recommandations. Pour ce faire, sélectionnez un modèle d’élément, définissez le nombre d’éléments à afficher, ainsi que le nombre de rangées d’éléments. 

### Configurer un bloc de contenu dynamique
Utilisez du contenu dynamique pour adapter les promotions et les messages aux différents utilisateurs ciblés. Le ciblage peut être réalisé en fonction de l’affinité ou de l’audience. Dynamic Yield détermine quelle expérience personnalisée offrir lorsque l’e-mail est ouvert. 

1. Glissez un bloc de contenu dynamique du volet de modification vers le corps de votre e-mail.<br><br> 
2. Sélectionnez un modèle pour la première variation. Vous pouvez maintenant définir les variables de design et de contenu. Enregistrez la variation lorsque vous avez terminé. <br>![][4]<br><br> 
3. Définissez l’audience dans le volet Dynamic Content (Contenu dynamique).<br>![][5]<br><br> 
4. Ajoutez une autre variation pour cibler une autre audience spécifique, ou pour cibler tous les utilisateurs. Répétez l’opération en fonction de vos besoins.<br><br> 
5. Définissez les priorités de vos variations à l’aide des touches fléchées haut et bas. <br><br> 
6. Les priorités déterminent quelle variation est fournie lorsqu’un utilisateur peut se voir fournir plusieurs expériences.

### Étape 3 : Intégrer votre e-mail à Braze

Cette intégration vous permet d’ajouter des [gadgets de recommandations](https://support.dynamicyield.com/hc/en-us/articles/360022547394) personnalisés, ainsi que du [contenu dynamique](https://support.dynamicyield.com/hc/en-us/articles/360022547994) fourni par Dynamic Yield, à vos campagnes de marketing par e-mail Braze. Intégrer ces campagnes à vos campagnes Braze nécessite de copier/coller un code d’intégration dans votre éditeur d’e-mails Braze.

1. Cliquez sur l’icône d’intégration ESP sur la page Experience Emails list (Liste des e-mails d’expérience).<br><br> 
2. Saisissez le jeton pertinent à partir de Braze insérant le CUID et l’ID d’adresse e-mail de l’utilisateur.<br>![][3]
  
Lorsque votre e-mail vous convient, la prochaine étape consiste à générer le code servant à l’intégrer dans Braze.
1. Dans **Experience Emails (E-mails d’expérience)**, cliquez sur **Generate Code (Générer le code)**.<br><br> 
2. Ensuite, cliquez sur **Copy to Clipboard (Copier vers le presse-papier)**.<br>![][1]<br><br> 
3. Collez le code dans votre campagne e-mail dans Braze, puis continuez à concevoir, tester et publier votre campagne e-mail.


[1]: {% image_buster /assets/img/dynamic_yield/dynamic_yield.png %}
[2]: {% image_buster /assets/img/dynamic_yield/dynamic_yield1.png %}
[3]: {% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %}
[4]: {% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %}
[5]: {% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %}
[6]: {% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %}
[7]: {% image_buster /assets/img/dynamic_yield/dynamic_yield6.png %}
[8]: {% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %}
