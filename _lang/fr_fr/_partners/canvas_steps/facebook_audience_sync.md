---
nav_title: Facebook
article_title: "Synchronisation de l'audience de Canvas avec Facebook"
description: "Cet article de référence expliquera comment utiliser la synchronisation des audiences Braze avec Facebook, pour diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Synchronisation de l'audience avec Facebook

> 

 



- 
- Reciblez les utilisateurs qui réagissent moins aux autres canaux de marketing.
- Créer des audiences de suppression pour empêcher les utilisateurs de recevoir des publicités lorsqu'ils sont déjà des consommateurs fidèles de votre marque.
- 

Cette fonctionnalité permet aux marques de contrôler quelles données first-party spécifiques sont partagées avec Facebook. Chez Braze, les intégrations avec lesquelles vous pouvez ou non partager vos données first-party font l'objet de la plus grande attention. Pour plus d'informations, consultez notre [politique de confidentialité](https://www.braze.com/privacy).

## Considérations sur la synchronisation des utilisateurs et la limite de débit
 
 Ce que cela signifie en pratique, c'est que Braze essaiera de regrouper et de traiter autant d'utilisateurs que possible toutes les 5 secondes avant d'envoyer ces utilisateurs à Facebook. 

 Si un client Braze atteint cette limite de débit, le canvas Braze retentera la synchronisation pendant environ 13 heures. Si la synchronisation n'est pas possible, ces utilisateurs sont répertoriés dans la métrique Utilisateurs erronés.

## Conditions préalables

 

| Exigence | Origine | Description |
| ----------- | ------ | ----------- |
| Facebook gestionnaire d'entreprise | [Facebook][1] | Un outil centralisé pour gérer les ressources Facebook de votre marque (par exemple, les comptes publicitaires, les pages et les applications). |
| Compte publicitaire Facebook | [Facebook][2] | Un compte publicitaire Facebook actif lié au gestionnaire d'entreprise de votre marque.<br><br> Assurez-vous également que vous avez accepté les conditions générales de votre compte publicitaire. |
| Conditions des audiences personnalisées de Facebook | [Facebook][3] | Acceptez les conditions des audiences personnalisées de Facebook pour vos comptes publicitaires Facebook que vous prévoyez d'utiliser avec Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

### Étape 1 : Connectez-vous à Facebook

Dans le tableau de bord de Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Facebook**. Sous Exportation de l'audience Facebook, sélectionnez **Connecter Facebook**.

![Page technologique Facebook dans Braze qui comprend une section Aperçu et une section Exportation de l'audience Facebook avec le bouton Facebook connecté.][4]{: style="max-width:85%;"}

Une fenêtre de dialogue oAuth Facebook apparaîtra pour autoriser Braze à créer des audiences personnalisées dans vos comptes publicitaires Facebook.

![La première boîte de dialogue Facebook demandant de "Se connecter en tant que X", où X est votre nom d'utilisateur Facebook.][6]{: style="max-width:30%;"}  ![La deuxième boîte de dialogue Facebook demandant l'autorisation de gérer les publicités pour vos comptes publicitaires.][5]{: style="max-width:40%;"}

Une fois que vous avez lié Braze à votre compte Facebook, vous pourrez alors sélectionner les comptes publicitaires que vous souhaitez synchroniser dans votre espace de travail Braze. 

![Une liste de comptes publicitaires disponibles que vous pouvez connecter à Facebook.][7]{: style="max-width:70%;"}



![Une version mise à jour de la page des partenaires technologiques de Facebook montrant les comptes publicitaires connectés avec succès.][8]{: style="max-width:85%;"}

Votre connexion Facebook est appliquée au niveau de l'espace de travail Braze. Si votre administrateur Facebook vous supprime de votre gestionnaire d'entreprise Facebook ou de l'accès aux comptes Facebook connectés, Braze détectera un jeton invalide. En conséquence, vos Canvases actifs utilisant des composants Facebook audience afficheront des erreurs, et Braze ne pourra pas synchroniser les utilisateurs. 

{% alert important %}
Pour les clients qui ont déjà suivi le processus de révision de l'application Facebook pour [Gestion des publicités](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) et [Accès standard à la gestion des publicités](https://developers.facebook.com/docs/marketing-api/access#standard), votre jeton d'utilisateur système sera toujours valide pour le composant audience de Facebook. Vous ne pourrez pas modifier ou révoquer le jeton d'utilisateur du système Facebook via la page partenaire Facebook. Au lieu de cela, vous pouvez connecter votre compte Facebook pour remplacer votre jeton d'utilisateur système Facebook dans votre espace de travail Braze. 

<br><br>
{% endalert %}

### Étape 2 : Accepter les conditions de service des audiences personnalisées



- 
- 






### Étape 3 : Ajoutez un composant audience Facebook dans Canvas Flow

Ajoutez un composant dans votre canvas et sélectionnez **Facebook audience**.

 

### Étape 4 : Configuration de la synchronisation

 



Sélectionnez le compte publicitaire Facebook souhaité. Sous le menu déroulant **Choisir une audience nouvelle ou existante**, tapez le nom d'une audience nouvelle ou existante. 

{% tabs %}
{% tab Créer une nouvelle audience %}

1. 
2.  
3. 



 





{% endtab %}
{% tab Synchronisation avec une audience existante %}

 

1. 
2.  
3.  

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
 
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 5 : Lancer canvas

 La nouvelle audience personnalisée sera créée, et les utilisateurs qui passent par l’étape d’audience Facebook seront transférés dans cette audience personnalisée sur Facebook. Si votre Canvas contient des étapes ultérieures, vos utilisateurs passeront ensuite à l’étape suivante de leur parcours utilisateur.

L'onglet **Historique** de l'audience personnalisée dans le gestionnaire d'audience Facebook reflétera le nombre d'utilisateurs envoyés à l'audience depuis Braze. Si un utilisateur revient à l'étape, il sera renvoyé sur Facebook.

![Détails de l'audience et l'onglet Historique pour une audience Facebook donnée qui comprend un tableau Historique de l'audience avec des colonnes pour l'activité, les détails de l'activité, les éléments modifiés, la date et l'heure.][9]{: style="max-width:80%;"}

## Comprendre les analyses

Le tableau suivant comprend des indicateurs et des descriptions pour vous aider à mieux comprendre les analyses de votre composant de synchronisation des audiences.

| Indicateurs | Description |
| --- | --- |
| Entré | Nombre d'utilisateurs qui sont entrés dans ce composant pour être synchronisés avec Facebook. |
| Procédé à l'étape suivante | Combien d'utilisateurs sont passés au composant suivant s'il y en a un. Tous les utilisateurs avanceront automatiquement s'il s'agit de la dernière étape de la branche canvas. |
| Utilisateurs synchronisés | Nombre d'utilisateurs qui ont été synchronisés avec succès à Facebook. |
| Utilisateurs non synchronisés | Nombre d'utilisateurs qui n'ont pas été synchronisés en raison de champs manquants. |
| Utilisateurs en attente | Nombre d'utilisateurs actuellement traités par Braze pour se synchroniser avec Facebook. |
| Utilisateurs en erreur | Nombre d'utilisateurs qui n'ont pas été synchronisés avec Facebook en raison d'une erreur d'API après environ 13 heures de tentatives. Les causes potentielles d'erreurs peuvent inclure un jeton Facebook non valide ou la suppression de l'audience personnalisée sur Facebook. |
| Sorti de canvas | Nombre d'utilisateurs qui ont quitté le canvas. Cela se produit lorsque la dernière étape dans un canvas est une étape Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}

{% endalert %}

## Foire aux questions

### Combien de temps faut-il pour que mes audiences soient générées dans le tableau de bord de mon partenaire de synchronisation d’audiences ?

Le temps nécessaire pour générer une audience dépend du partenaire spécifique. Tous les réseaux traiteront les requêtes de Braze et tenteront de faire correspondre les utilisateurs. 

### Que dois-je faire ensuite si je reçois une erreur de jeton non valide ?

Vous pouvez simplement déconnecter et reconnecter votre compte Facebook sur la page partenaire Facebook. 

### Pourquoi mon Canvas n’est-il pas autorisé à être lancé ?

- Assurez-vous que votre jeton utilisateur du système est authentifié et qu'il a accès aux comptes publicitaires souhaités dans Facebook Business Manager.
- Assurez-vous d'avoir sélectionné un compte publicitaire, saisi un nom pour la nouvelle audience personnalisée et sélectionné les champs à faire correspondre.
- Vous avez peut-être atteint la limite de 500 audiences personnalisées sur Facebook. 

### Comment puis-je savoir si les utilisateurs ont été mis en correspondance après les avoir transféré à Facebook ?

Facebook ne fournit pas cette information pour des raisons de confidentialité.

### Braze prend-il en charge les audiences personnalisées basées sur la valeur ?

Pour l'instant, les audiences personnalisées basées sur la valeur ne sont pas prises en charge par Braze. Si vous souhaitez synchroniser ces types d'audiences personnalisées, soumettez vos [commentaires sur le produit.]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)

### 



 

- 
- 
- 
- 



### 

Pour le moment, les audiences personnalisées similaires basées sur la valeur ne sont pas prises en charge par Braze. Si vous tentez de synchroniser avec cette audience, cela peut provoquer des erreurs au niveau de l’étape de synchronisation d'audience. Pour résoudre cela, suivez ces étapes :

1. Accédez à votre tableau de bord du gestionnaire de publicités Facebook et sélectionnez **Audiences**.
2. Sélectionnez **Créer une audience** > **Audience personnalisée**.
3. Sélectionnez **liste des clients**.
4. Téléchargez votre CSV ou liste sans la colonne **Value**. Sélectionnez **Non, continuer avec une liste de clients qui n'inclut pas la valeur du client**.
5. Terminez la création de votre audience personnalisée.
6. Dans Braze, mettez à jour l'étape de synchronisation de l'audience Facebook avec l'audience personnalisée que vous avez créée.

###  

Pour utiliser Audience Sync to Facebook, vous devez accepter les présentes conditions de service. 

- 
- 

Après avoir accepté les conditions de service de votre audience personnalisée Facebook, procédez comme suit :

1. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
2. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre canvas.



## Résolution des problèmes

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Erreur</th>
      <th>Description</th>
      <th>Marche à suivre pour résoudre le problème</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Jeton non valide</b></td>
      <td></td>
      <td> </td>
    </tr>
    <tr>
      <td><b>Taille de l'audience trop petite</b></td>
      <td> Si la taille de votre audience est proche de zéro, le réseau peut signaler que la taille de l'audience est trop petite pour être diffusée.</td>
      <td> </td>
    </tr>
    <tr>
      <td><b>L’audience n'existe pas</b></td>
      <td> </td>
      <td> <br><br>  <br><br></td>
    </tr>
    <tr>
      <td><b>Tentative d'accès au compte publicitaire</b></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>   </td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>
      </td>
    </tr>
    <tr>
      <td></td>
      <td>  </td>
      <td>
      </td>
    </tr>
  </tbody>
</table>

### 

 

#### 

1.  
2.  
3. 

#### 

 

1. 
- 
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`
- 
  - 
  - 





1. 
2. 
3. 



{:start="4"}

4.  



{:start="5"}
5\.   
6\. Actualisez votre jeton d'accès Facebook avec Braze en déconnectant et reconnectant votre compte Facebook.
7\. Réactivez votre étape de synchronisation d'audience Facebook en modifiant et en mettant à jour votre canvas. Braze pourra alors synchroniser les utilisateurs dès qu'ils atteindront l'étape de l'audience Facebook.
8\. 

####  



1. 
2. 
3.  <br> 
4.  <br> 

{:start="5"}

5.  <br> 

#### 



1. 
2. 

[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
[24]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}
[25]: {% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}