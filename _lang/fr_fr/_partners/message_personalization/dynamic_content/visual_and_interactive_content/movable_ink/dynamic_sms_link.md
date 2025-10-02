---
nav_title: Aperçu du lien SMS dynamique
article_title: Aperçu du lien SMS dynamique
description: "Cet article de référence explique comment activer et utiliser la fonctionnalité d'aperçu de lien SMS de Movable Ink."
page_type: partner
search_tag: Partner
---

# Aperçu du lien SMS dynamique

> Avec l'aperçu de lien SMS dynamique de Movable Ink, vous pouvez tirer parti de l'immersion de MMS au même coût que les SMS. Cela vous permet d'utiliser Braze et Movable Ink pour offrir des expériences d'envoi de messages riches, personnalisées et rentables.

## Conditions préalables

| Condition | Descriptif |
| --- | --- |
| Compte Movable Ink | Un compte Movable Ink est nécessaire pour bénéficier de ce partenariat. |
| source de donnée | Vous devez connecter une source de données à Movable Ink. Cela peut être fait via un fichier CSV, l’importation de site Web ou une API. |
| Capacités d'envoi de MMS | Confirmez que vous êtes configuré pour MMS via Braze.
| [Raccourcissement de lien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) | Confirmez que le raccourcissement des liens est activé. | 
| Carte de contact | Votre marque (l'expéditeur) doit être enregistrée en tant que contact sur le téléphone de l'utilisateur pour que l'aperçu du lien fonctionne avec iOS. Cela peut être fait avec une carte de contact ou une autre méthode. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Suivez les étapes respectives ci-dessous pour envoyer des liens SMS dynamiques pour les systèmes d'exploitation iOS et Android.

### iOS

{% alert important %}
Pour autoriser les aperçus de liens pour iOS, les utilisateurs doivent ajouter votre marque (l'expéditeur) en tant que contact.
{% endalert %}

#### Étape 1 : Créez une campagne de cartes de contact

Une fois que les utilisateurs auront enregistré votre marque en tant que contact, que ce soit par le biais d'une [carte de contact]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) ou d'une autre méthode, ils pourront voir les invites de **prévisualisation Tap to Load** et les liens Movable Ink.

![1]{: style="max-width:30%;"}

#### Étape 2 : Envoyer des liens Movable Ink

1. Créez une campagne SMS dans Movable Ink et générez votre URL de clic.
2. Dans le tableau de bord de Braze, allez à **campagnes** et configurez une nouvelle campagne SMS/MMS à partir du menu déroulant **Créer une campagne**.
3. Dans le compositeur de campagne SMS :
    - Définissez votre groupe d'abonnement.
    - Entrez votre message.
    - Ajoutez votre lien Movable Ink **en dernier**, après tout autre texte dans le corps du message. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Consultez [liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) pour un rappel sur la personnalisation liquid.  
{% endalert %}

{: start="4"}
4\. Vous êtes prêt à tester et lancer votre campagne d'aperçu de lien SMS dynamique.

![3]{: style="max-width:70%;"}

Après que les utilisateurs aient chargé l'aperçu du lien, une image personnalisée s'affichera avec la possibilité de créer un lien vers votre site web, application ou page de destination.

![4]{: style="max-width:30%;"}

### Android (appareils Google et Samsung)

Les utilisateurs d'Android ne sont pas tenus d'enregistrer votre marque en tant que contact pour recevoir des aperçus de liens SMS dynamiques. Cependant, il est toujours recommandé afin que l'appareil puisse charger automatiquement les aperçus de liens.

![5]{: style="max-width:30%;"}

Les utilisateurs qui n'ont pas enregistré votre marque en tant que contact et qui ont activé les aperçus automatiques devront sélectionner **Tap to load preview** pour charger l'image d'aperçu.

![6]{: style="max-width:30%;"}

## Considérations

- N'incluez qu'un seul lien d'aperçu dans votre message. Le contenu ne sera pas généré avec plusieurs liens dans le corps de votre SMS. 
- N'incluez aucun caractère après votre lien de prévisualisation ou l'expérience pourrait être perturbée.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
