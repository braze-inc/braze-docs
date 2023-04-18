---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 6
description: "Cet article de référence explique comment configurer Inbox Vision, une fonctionnalité qui permet aux spécialistes du marketing d’afficher leurs e-mails du point de vue de divers clients de messagerie et appareils mobiles."
tool:
  - Dashboard
channel:
  - e-mail

---

# Inbox Vision

> Inbox Vision permet aux marketeurs de consulter leurs e-mails du point de vue de différents clients e-mail et appareils mobiles. 

Pour tester votre e-mail dans Inbox Vision, allez sur l’onglet **Preview and Test (Aperçu et test)** dans votre éditeur Drag & Drop ou l’éditeur d’e-mail HTML. Sélectionner **Inbox Vision** et cliquez sur **Run Inbox Vision (Exécuter Inbox Vision)**.

![][3]{: style="max-width:80%;"}

Braze envoie ensuite une version HTML de votre e-mail à différents clients e-mail utilisés dans le monde entier, ce qui peut prendre entre deux et dix minutes. Ces aperçus HTML sont divisés en trois sections : **Web Clients (Clients Web)**, **Application Clients (Clients d’application)**, et **Mobile Clients (Clients mobiles)**. 

Sélectionnez une mosaïque pour afficher l’aperçu plus en détail. Votre e-mail doit inclure une ligne d’objet et un domaine d’envoi valide afin de voir ces aperçus. Prenez garde au fait que votre e-mail peut s’afficher différemment sur les ordinateurs de bureau que sur les appareils mobiles. En affichant ces prévisualisations, vous pouvez vous assurer que le contenu de vos e-mails s’affiche comme vous le désirez.

{% alert tip %}
Utilisez Inbox Vision pour tester les différences entre les modes clairs et sombres pour vous assurer que vos e-mails sont parfaits !
{% endalert %}

![Overview d’Inbox Vision pour l’éditeur HTML.][1]

Lorsque vous apportez des modifications à un modèle, cliquez sur **Re-run Test (Relancer le test)** pour voir les aperçus mis à jour.

{% alert important %} 
En général, votre e-mail ne fonctionnera pas avec Inbox Vision si le contenu de votre e-mail s’appuie sur des informations de modèles, telles que les informations de profil utilisateur. En effet, Braze modélise un utilisateur vide lorsque nous envoyons des e-mails à l’aide de cette fonctionnalité. 
{% endalert %}

## Analyse des codes

L’analyse des codes est un moyen pour Braze de mettre en évidence les problèmes qui peuvent exister avec votre HTML, indiquant le nombre d’occurrences de chaque problème et fournissant des informations sur les éléments HTML non pris en charge. Ces informations sont disponibles dans l’onglet **Inbox Vision** en sélectionnant <i class="fas fa-list"></i> **List view (Afficher la liste)**.

![Exemple d’analyse de code sur l’aperçu d’Inbox Vision.][2]

{% alert note %} 
Parfois, l’analyse de code s’affiche plus rapidement que l’aperçu d’un client par e-mail particulier. C’est parce que Braze attend que l’e-mail arrive dans la boîte de réception avant de prendre la capture d’écran. 
{% endalert %}

## Tests de courrier indésirable

Les tests de courrier indésirable visent à prédire si votre e-mail s’affichera dans les dossiers de courrier indésirable ou dans les boîtes de réception de vos clients. Les tests de courrier indésirable sont exécutés sur les principaux filtres anti-spam, comme IronPort, SpamAssassin et Barracuda, ainsi que sur les principaux filtres de fournisseurs de services Internet (ISP), tels que Gmail.com et Outlook.com.

Pour vérifier les résultats de vos tests de courrier indésirable, cliquez sur l’onglet **Spam Testing (Tests de courrier indésirable)** dans la section **Inbox Vision**. Le tableau **Spam Test Result (Résultats des tests de courrier indésirable)** répertorie le nom, l’état et le type du filtre de courrier indésirable.

![Tableau des résultats des tests de courrier indésirable à trois colonnes : Nom, État et Type. Il existe une liste de filtres anti-spam et de filtres de fournisseurs de services Internet qui ont réussi les tests de courrier indésirable, indiquant que la campagne par e-mail ne s’affichera pas dans le dossier de courrier indésirable.][4]

Après avoir examiné ces résultats et effectué des ajustements à votre campagne par e-mail, cliquez sur **Re-run Test (Relancer le test)** pour recharger vos résultats de tests de courrier indésirable.

## Précision du test

Tous nos tests sont exécutés à l’aide de clients par e-mail réels. Nous travaillons dur pour garantir que tous les rendus sont aussi précis que possible. Si vous constatez systématiquement un problème avec un client par e-mail, ouvrez un [ticket d’assistance]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
