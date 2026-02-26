---
nav_title: Configuration initiale du SDK avec Eclipse
page_order: 1

page_type: update
description: "Cet article archivé décrit comment effectuer une configuration initiale du SDK avec Eclipse. Braze ne prend plus en charge Eclipse IDE."
---

# Configuration initiale du SDK avec Eclipse

{% alert update %}
Braze a supprimé la prise en charge de l'IDE Eclipse en raison de la [temporisation par Google de la prise en charge du plugin Eclipse Android Developer Tools.](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) Si vous avez besoin d'aide pour l'intégration d'Eclipse avant la migration, [envoyez un e-mail au service d'assistance.]({{site.baseurl}}/support_contact/)
{% endalert %}

## Étape 1
Dans votre ligne de commande, clonez le [dépôt GitHub de Braze Android](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Étape 2
Importez le projet Braze dans votre espace de travail local

Dans Éclipse :

  - Accédez à File (Fichier) > Import (Importer).

    ![Importation de fichiers]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Sélectionnez Android > Code Android existant dans le Workspace.

    ![Importation Android]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Cliquez sur "Parcourir".

    ![Parcourir]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Cochez le dossier du projet Braze UI ainsi que "copier le projet dans l'espace de travail" et cliquez sur "Terminer".

    ![Sélectionnez le projet Android UI]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Étape 3
Référencez Braze dans votre propre projet.
Dans Éclipse :

  - Cliquez avec le bouton droit de la souris sur votre projet et sélectionnez "Propriétés".

    ![Cliquez sur Propriétés]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - Sous « Android », cliquez sur « Add » (Ajouter) dans la section Bibliothèque et ajoutez android-sdk-ui à votre application en tant que bibliothèque.

    ![Braze Ajouter]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Étape 4
Résoudre les erreurs de dépendance et corriger la cible du build.

À ce stade, vous pouvez avoir des erreurs avec le code Braze, notamment si certaines de ses dépendances ne sont pas présentes, ou bien la cible du build est peut-être incorrecte :

   - Cliquez avec le bouton droit de la souris sur le projet de l’IU Braze et sélectionnez Properties (Propriétés) -> Android pour vous assurer que la cible de build est définie sur la version actuelle des outils de build Braze.

      ![Créer un ciblage]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Cliquez avec le bouton droit de la souris sur le projet de l’IU Braze et sélectionnez Properties (Propriétés) -> Java Build Path (Chemin de build Java) -> Add JARs… (Ajouter des JAR...), puis ajoutez « android-support-v4.jar » en tant que bibliothèque à partir de l’application principale.

      ![Assistance]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Étape 5

Ajouter les éléments restants.

  - Pour SDK version 1.10.0 ou supérieure, vous devrez ajouter
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  à votre AndroidManifest.xml, car Eclipse ne prend pas en charge la fusion des manifestes.

  - Pour la version 1.7.0 ou supérieure du SDK, vous devrez copier "assets/fontawesome-webfont.ttf" de notre projet de bibliothèque vers votre application. Eclipse n’inclut pas automatiquement le dossier des assets à partir des bibliothèques.

