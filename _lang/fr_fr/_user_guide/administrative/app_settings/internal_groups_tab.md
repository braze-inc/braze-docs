---
nav_title: Groupes internes
article_title: Groupes interne
page_order: 10
page_type: reference
description: ""

---

# Groupes internes

>   

{% alert tip %}

{% endalert %}

## 



## 

 

1. Allez dans **Réglages** > **Groupes internes**.
2. 
3. 
4. 

|          | Description                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
|    | Utilisé pour vérifier les événements ou les journaux de votre appareil de test.                                    |
|  | Peut être utilisé pour les notifications push, les e-mails et les messages dans l’application pour envoyer une copie de rendu du message. |
|          | Envoie automatiquement une copie de l’e-mail à tous les groupes initiateurs lors de l’envoi.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Ajout d’utilisateurs de test

 

1. 
2. 

|                   | Description                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  |                                                                                                                                                            |
|   | Recherchez par adresse IP. Donnez ensuite un nom pour chaque utilisateur de test ajouté. Il s'agit du nom auquel tous les journaux des événements seront associés sur la page [Journal des événements utilisateurs.]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/)  |
|       |  Vous ne pouvez ajouter que des utilisateurs déjà connus dans le tableau de bord.           |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Groupes de test de contenu

Semblable à l'envoi d'un test de prévisualisation d'un message, le groupe de test de contenu vous fait gagner du temps et vous permet de lancer simultanément des tests auprès d'une liste prédéfinie d'utilisateurs de Braze.  Seuls les groupes étiquetés comme groupes de test de contenu seront disponibles dans la section de prévisualisation d'un message.

{% alert note %}
Les messages de test [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) ne peuvent être envoyés qu'à des numéros de téléphone valides figurant dans la base de données.
{% endalert %}

 Si votre message comprend un liquide ou une autre personnalisation dynamique, Braze utilisera les attributs disponibles pour chaque utilisateur afin de personnaliser le contenu du message. Pour les utilisateurs qui n’ont aucun attribut, Braze utilisera la valeur par défaut définie.

En outre, si vous prévisualisez le message en tant qu’utilisateur aléatoire, utilisateur personnalisé ou utilisateur existant, vous pouvez envoyer cette version prévisualisée à la place. Si vous ne cochez pas cette case, vous pouvez envoyer des messages en fonction des attributs de chaque utilisateur par rapport à la version prévisualisée.





### Groupes initiateurs

 

  

 

 

- 
-  
- 
- 

{% alert tip %}

{% endalert %}

#### Pour les campagnes



Les groupes initiateurs sont envoyés à chaque variante de courriel une fois et sont délivrés la première fois que votre utilisateur reçoit cette variante particulière. Pour les messages planifiés, il s'agit généralement de la première fois que la campagne est lancée. Pour les campagnes basées sur des actions ou déclenchées par l’API, il s’agira du moment où le premier utilisateur reçoit un message.

 

{% alert note %}

{% endalert %}



#### Pour le Canvas

Les groupes initiateurs de Canvas fonctionnent de la même manière que n'importe quelle campagne déclenchée. Braze détecte automatiquement toutes les étapes qui contiennent un message e-mail  et les envoie lorsque votre utilisateur atteint pour la première fois cette étape particulière.

Si une étape e-mail a été mise à jour après que le groupe initiateur a été envoyé par e-mail, l’option d’envoyer uniquement des étapes mises à jour, toutes les étapes ou de désactiver les initiateurs sera présentée.

