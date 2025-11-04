---
nav_title: Configuration des IP et des domaines
article_title: Configuration des IP et des domaines
page_order: 0
page_type: tutorial
channel: email
description: "Cet article vous explique comment configurer vos IP et domaines pour l'envoi d'e-mails via Braze."

---

# Configuration des IP et des domaines

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> Cet article vous guidera à travers les exigences et les étapes nécessaires pour configurer vos adresses IP et pools, ainsi que les domaines et sous-domaines nécessaires avant de pouvoir commencer à envoyer des e-mails avec Braze.<br><br>Bien que la majeure partie de la configuration soit effectuée par Braze, nous avons décrit les exigences et les matériaux nécessaires à cette configuration.

## Méthode 1 : Coordonner avec Braze (recommandé)

### Étape 1 : Informations générales

Envoyez les informations suivantes à votre conseiller Braze :

* Les domaines et sous-domaines de votre choix
* Le nombre approximatif d'e-mails que vous enverrez chaque mois, ce qui vous aidera à déterminer le nombre d'adresses IP dont vous aurez besoin.
* Comment préférez-vous mapper vos domaines d'envoi à l'adresse IP qui vous a été attribuée ?

### Étape 2 : Braze configure les informations

Après réception de votre e-mail, nous nous mettrons au travail pour configurer vos IP, domaines et sous-domaines, et pools d'IP.

### Étape 3 : Ajouter des enregistrements DNS

Une fois vos IP, domaines, sous-domaines et pools d'IP configurés, nous vous enverrons une liste d'enregistrements DNS. Demandez à vos ingénieurs et développeurs d'ajouter ces enregistrements DNS là où c'est nécessaire, et une fois qu'ils ont été ajoutés, informez-en l'équipe Braze Onboarding.

### Prochaines étapes

Nous vérifierons votre configuration et validerons toutes les informations dans nos systèmes internes. L'équipe d'onboarding de Braze vous informera lorsque vous serez prêt à partir, ou s'il y a des problèmes avec vos enregistrements DNS que vous devez aborder avec votre équipe d'ingénieurs.

## Méthode 2 : Configuration de l'e-mail en libre-service

Cette méthode permet de mettre en place un domaine d'envoi, un domaine de suivi et une IP au total pour une entreprise. Si vous envisagez d'en mettre d'autres en place, veuillez consulter l'équipe Braze Onboarding (méthode 1).

{% alert important %}
Cette fonctionnalité de configuration des e-mails en libre-service est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la version bêta.<br>Si vous utilisez la fonctionnalité de configuration des e-mails en libre-service, n'oubliez pas de consulter également l'équipe Braze Onboarding.
{% endalert %}

### Conditions préalables

Pour utiliser la configuration des e-mails en libre-service, vous devez remplir les conditions préalables suivantes :

1. Vous êtes un nouveau client en phase d'onboarding.
2. Vous disposez de l'autorisation "Peut gérer les paramètres de l'entreprise" au niveau de l'entreprise.

### Étape 1 : Commencer la configuration

1. Allez dans **Paramètres** > **Paramètres administratifs** sous **Paramètres de l'entreprise**. 
2. Ensuite, sélectionnez l'onglet **Vérification de l'expéditeur**. Pour afficher cet onglet, vous devez avoir l'autorisation "Peut gérer les paramètres de l'entreprise" au niveau de l'entreprise.
3. Cliquez sur le bouton **Démarrer la configuration**.

### Étape 2 : Ajouter et vérifier un domaine d'envoi

Un domaine d'envoi est utilisé dans l'adresse "from" lors de l'envoi d'un e-mail. Entrez un domaine d'envoi et cliquez sur **Soumettre**. 

Ensuite, ajoutez les enregistrements TXT et CNAME du bas de la page à votre fournisseur de DNS. Retournez ensuite dans le tableau de bord de Braze et cliquez sur **Vérifier**.

\![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

{% alert important %}
Le domaine d'envoi doit être subordonné à un domaine que vous possédez. Par exemple, si vous possédez "example.com", un sous-domaine pourrait être "mail.example.com", ce qui vous permettrait d'utiliser l'adresse d'envoi " @mail.example.com".
{% endalert %}

### Étape 3 : Ajouter et vérifier un domaine de suivi

Un domaine de suivi est utilisé pour envelopper les liens dans vos e-mails à des fins de suivi des clics et d'image de marque. Elle sera visible par les utilisateurs lorsqu'ils survoleront ou cliqueront sur les liens de votre e-mail. Nous vous recommandons de le faire correspondre à votre domaine d'envoi.

Saisissez un domaine de suivi et cliquez sur **Soumettre**. Ensuite, ajoutez les enregistrements CNAME du bas de la page à votre fournisseur de DNS. Retournez ensuite dans le tableau de bord de Braze et cliquez sur **Vérifier**.

### Étape 4 : Ajouter une adresse IP

Braze génère un enregistrement A pour associer votre adresse IP à votre sous-domaine d'envoi dans une configuration appelée reverse DNS (rDNS). Ajoutez l'enregistrement A dans votre fournisseur de DNS puis cliquez sur **Configurer le rDNS** pour prendre en charge la livrabilité.

Notez que les domaines ajoutés n'apparaîtront pas dans la section **Vérification de l'expéditeur**. Pour ajouter d'autres domaines, contactez l'équipe d'assistance de Braze.

### Prochaines étapes

Une fois la vérification de l'expéditeur terminée, nous recommandons le réchauffement d'adresses IP afin que vos messages atteignent leur boîte de réception à un taux élevé et constant. Après avoir terminé cette configuration, veillez également à consulter l'équipe Braze Onboarding pour confirmer que vos domaines et votre [adresse IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) fonctionnent.

