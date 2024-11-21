---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Cet article de référence explique comment configurer Inbox Vision, une fonctionnalité qui permet aux spécialistes du marketing d’afficher leurs e-mails du point de vue de divers clients de messagerie et appareils mobiles."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision vous permet de visualiser vos e-mails du point de vue de différents clients de messagerie et appareils mobiles. 

## Tester votre e-mail dans Inbox Vision

Inbox Vision fonctionne lorsque l'**utilisateur aléatoire** est sélectionné pour la **prévisualisation en tant qu'utilisateur** et ne conserve aucun utilisateur personnalisé ni aucun autre paramètre d'utilisateur de prévisualisation. Cela signifie que si vous sélectionnez **Utilisateur personnalisé** et que vous exécutez Vision de la boîte de réception, ce qui s'affiche dans Vision de la boîte de réception peut différer de l'aperçu du message ailleurs. 

Pour tester votre message e-mail dans Inbox Vision, procédez comme suit :

1. Allez dans votre éditeur par glisser-déposer ou dans votre éditeur d'e-mails HTML. 
2. Ouvrez l'onglet **Prévisualisation et test**.
3. Sélectionnez **Inbox Vision** et cliquez sur **Exécuter Inbox Vision**. <br><br> ![][3]{: style="max-width:80%;"} <br><br> Braze envoie ensuite une version HTML de votre e-mail à différents clients e-mail utilisés dans le monde entier, ce qui peut prendre entre deux et dix minutes. <br><br> Les aperçus HTML rendus seront divisés en trois sections : 
- **Clients Web** 
- **Clients de l’application** 
- **Clients mobiles** <br><br>
4. Sélectionnez une mosaïque pour afficher l’aperçu plus en détail. <br><br> Votre e-mail doit inclure une ligne d’objet et un domaine d’envoi valide afin de voir ces aperçus. Prenez garde au fait que votre e-mail peut s’afficher différemment sur les ordinateurs de bureau que sur les appareils mobiles. En affichant ces prévisualisations, vous pouvez vous assurer que le contenu de vos e-mails s’affiche comme vous le désirez.

{% alert tip %}
Utilisez Inbox Vision pour tester les différences entre les modes sombre et lumineux afin de confirmer que vous recevez bien vos e-mails !
{% endalert %}

![Overview d’Inbox Vision pour l’éditeur HTML.][1]

{: start="5"}
5\. Apportez des modifications à un modèle, si nécessaire, puis cliquez sur **Réexécuter le test** pour voir les aperçus mis à jour.

{% alert important %}
En général, votre e-mail ne fonctionnera pas avec Inbox Vision si le contenu de votre e-mail repose sur des informations de modélisation, telles que les informations du profil utilisateur. En effet, Braze modélise un utilisateur vide lorsque nous envoyons des e-mails à l’aide de cette fonctionnalité.
{% endalert %}

## Analyse des codes

L’analyse des codes est un moyen pour Braze de mettre en évidence les problèmes qui peuvent exister avec votre HTML, indiquant le nombre d’occurrences de chaque problème et fournissant des informations sur les éléments HTML non pris en charge. 

### Visualisation des informations relatives à l'analyse du code

Vous trouverez ces informations dans l'onglet **Vision de la boîte de réception** en sélectionnant <i class="fas fa-list"></i> **List view.** Cette vue de liste n'est disponible que pour les modèles d'e-mail HTML. Si vous utilisez des modèles d'e-mail à glisser-déposer, vérifiez plutôt les aperçus pour résoudre les éventuels problèmes.

![Exemple d’analyse de code sur l’aperçu d’Inbox Vision.][2]

{% alert note %}
Parfois, l’analyse de code s’affiche plus rapidement que l’aperçu d’un client par e-mail particulier. C’est parce que Braze attend que l’e-mail arrive dans la boîte de réception avant de prendre la capture d’écran.
{% endalert %}

## Tests de courrier indésirable

Les tests de courrier indésirable visent à prédire si votre e-mail s’affichera dans les dossiers de courrier indésirable ou dans les boîtes de réception de vos clients. Les tests de courrier indésirable portent sur les principaux filtres anti-spam, tels que IronPort, SpamAssassin et Barracuda, ainsi que sur les principaux filtres des fournisseurs de services Internet (FAI), tels que Gmail.com et Outlook.com.

### Consultation des résultats des tests courrier indésirable

Pour vérifier les résultats de votre test de courrier indésirable, cliquez sur l'onglet **Tests de courrier indésirable** dans la section **Vision de la boîte de réception**. Le tableau **Résultat du test de courrier** indésirable répertorie le nom, l'état et le type du filtre anti-spam.

![Tableau des résultats des tests de courrier indésirable à trois colonnes : Nom, État et Type. Il existe une liste de filtres anti-spam et de filtres de fournisseurs de services Internet qui ont réussi les tests de courrier indésirable, indiquant que la campagne par e-mail ne s’affichera pas dans le dossier de courrier indésirable.][4]

Après avoir examiné ces résultats et apporté d'éventuels ajustements à votre campagne e-mail, cliquez sur **Ré-exécuter le test** pour recharger les résultats de votre test de courrier indésirable.

## Précision du test

Tous nos tests sont exécutés à l’aide de clients par e-mail réels. Braze s'efforce de vérifier que tous les rendus sont aussi précis que possible. Si vous constatez systématiquement un problème avec un client e-mail, ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
