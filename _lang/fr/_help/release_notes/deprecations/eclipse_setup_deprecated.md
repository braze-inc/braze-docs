---
nav_title: Configuration initiale du SDK avec Eclipse
page_order: 1

page_type: update
description: "Cet article archivé décrit comment effectuer une configuration initiale du SDK avec Eclipse. Braze ne prend plus en charge Eclipse IDE."
---

# Configuration initiale du SDK avec Eclipse

{% alert update %}
Braze a arrêté sa prise en charge de l’IDE Eclipse, car [Google arrête sa prise en charge du plug-in Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si vous avez besoin d’aide pour votre intégration Eclipse avant la migration, [envoyez un e-mail à notre Service d’assistance]({{site.baseurl}}/support_contact/) pour obtenir de l’aide.
{% endalert %}

## Étape 1
Via la ligne de commande, clonez le [référentiel GitHub Android de Braze][03].

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Étape 2
Importez le projet Braze dans votre espace de travail local

Dans Éclipse :

  - Accédez à File (Fichier) > Import (Importer).

    ![Importation de fichiers][04]
  - Sélectionnez Android > Code Android existant dans le Workspace.

    ![Importation Android][05]
  - Cliquez sur Parcourir."

    ![Parcourir][06]
  - Cochez le dossier du projet de l’IU Braze ainsi que « copier le projet dans l’espace de travail » et cliquez sur « Terminer »."

    ![Sélectionner le Projet IU Android][07]

## Étape 3
Référencez Braze dans votre propre projet.
Dans Éclipse :

  - Cliquez avec le bouton droit de la souris sur votre projet et sélectionnez Propriétés."

    ![Cliquer sur Propriétés][08]
  - Sous « Android », cliquez sur « Add » (Ajouter) dans la section Bibliothèque et ajoutez android-sdk-ui à votre application en tant que bibliothèque.

    ![Ajouter Braze][09]

## Étape 4
Résoudre les erreurs de dépendance et corriger la cible du build.

À ce stade, vous pouvez avoir des erreurs avec le code Braze, notamment si certaines de ses dépendances ne sont pas présentes, ou bien la cible du build est peut-être incorrecte :

   - Cliquez avec le bouton droit de la souris sur le projet de l’IU Braze et sélectionnez Properties (Propriétés) -> Android pour vous assurer que la cible de build est définie sur la version actuelle des outils de build Braze.

      ![Construire la cible][10]
   - Cliquez avec le bouton droit de la souris sur le projet de l’IU Braze et sélectionnez Properties (Propriétés) -> Java Build Path (Chemin de build Java) -> Add JARs… (Ajouter des JARs...) puis ajoutez ‘android-support-v4.jar’ en tant que bibliothèque à partir de l’application principale.

      ![Prise en charge][11]

## Étape 5

Ajouter les éléments restants.

  - Pour SDK version 1.10.0 ou supérieure, vous devrez ajouter
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  à votre AndroidManifest.xml, car Eclipse ne prend pas en charge le manifest merging (fusion de manifeste).

  - Pour le SDK version 1.7.0 ou supérieure, vous devrez copier « assets/fontawesome-webfont.ttf » de notre projet Bibliothèque vers votre application. Eclipse n’inclut pas automatiquement le dossier des assets à partir des bibliothèques.

[03]: https://github.com/braze-inc/braze-android-sdk "Appboy Android GitHub Repository"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
