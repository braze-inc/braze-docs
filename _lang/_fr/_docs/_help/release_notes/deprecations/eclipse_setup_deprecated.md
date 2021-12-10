---
nav_title: Configuration initiale du SDK avec Eclipse
page_order: 1
page_type: Mettre à jour
description: "Cet article archivé décrit comment effectuer une installation initiale du SDK avec Eclipse. Braze a un support obsolète pour l'IDE Eclipse."
---

# Configuration initiale du SDK avec Eclipse

{% alert update %}
Braze a supprimé la prise en charge de l'IDE Eclipse en raison de la prise en charge de [Google sunsetting pour le plugin Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si vous avez besoin d'aide pour votre intégration à Eclipse avant la migration, veuillez [envoyer un e-mail à Support]({{site.baseurl}}/support_contact/) pour obtenir de l'aide.
{% endalert %}

## Étape 1
Dans votre ligne de commande, clonez le [Dépôt Github Android Braze][03].

```bash
$ git clone git@github.com:Appboy/appboy-android-sdk.git
```

## Étape 2
Importer le projet Braze dans votre espace de travail local

Dans Eclipse :

  - Naviguez vers Fichier > Importer.

    ![Importation de fichier][2]
  - Sélectionnez Android > Code Android existant dans l'espace de travail.

    ![Importation Android][3]
  - Cliquez sur "Parcourir".

    ![Parcourir][4]
  - Vérifiez le dossier du projet Braze UI ainsi que « copier le projet dans l'espace de travail » et cliquez sur « Terminer ».

    ![Sélectionnez le projet d'interface utilisateur Android][5]

## Étape 3
Référence Braze dans votre propre projet. Dans Eclipse :

  - Faites un clic droit sur votre projet et sélectionnez "Propriétés".

    ![Cliquez sur Propriétés][6]
  - Sous « Android», cliquez sur « Ajouter» dans la section de la bibliothèque et ajoutez android-sdk-ui en tant que bibliothèque à votre application.

    ![Ajout de Braze][7]

## Étape 4
Résoudre les erreurs de dépendance et corriger la cible de construction.

En ce moment, vous pouvez voir des erreurs venant avec le code de Braze, c'est parce que ses dépendances ne sont pas remplies et que la cible de compilation est peut-être incorrecte :

   - Faites un clic droit sur le projet de Braze UI et sélectionnez Propriétés->Android pour vous assurer que la cible de construction est définie sur la version actuelle des outils de construction de Braze.

      ![Construire la Cible][8]
   - Faites un clic droit sur le projet de l'interface de Braze et sélectionnez Propriétés->Chemin de compilation Java->Ajouter JARs… et ajoutez 'android-support-v4. ar’ de l’application principale en tant que bibliothèque.

      ![Soutien][9]

## Étape 5

Ajouter des pièces finales.

  - Pour le SDK version 1.10.0 ou supérieure, vous devrez ajouter `<service android:name="com.appboy.services.AppboyDataSyncService" />` à votre AndroidManifeste. ml, car Eclipse ne prend pas en charge la fusion des manifestes.

  - Pour le SDK version 1.7.0 ou supérieure, vous devrez copier "assets/fontawesome-webfont.ttf" de notre projet de bibliothèque vers votre application. Eclipse n'inclut pas automatiquement le dossier des ressources des bibliothèques.

[2]: {{site.baseurl}}/assets/img_archive/file_import.png
[3]: {{site.baseurl}}/assets/img_archive/android_import.png
[4]: {{site.baseurl}}/assets/img_archive/click_browse.png
[5]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[6]: {{site.baseurl}}/assets/img_archive/click_properties.png
[7]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[8]: {{site.baseurl}}/assets/img_archive/build_target.png
[9]: {{site.baseurl}}/assets/img_archive/android_support_v4.png

[03]: https://github.com/appboy/appboy-android-sdk "Appboy Android Github Repository"
