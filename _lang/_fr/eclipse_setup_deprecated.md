---
nav_title: Initial SDK Setup with Eclipse
page_order: 1
page_type: update
description: "This archived article describes how to perform an initial SDK setup with Eclipse. Braze has deprecated support for the Eclipse IDE."
---

# Initial SDK setup with Eclipse

{% alert update %}
Braze has removed support for the Eclipse IDE due to [Google sunsetting support for the Eclipse Android Developer Tools Plugin](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). If you need assistance with your Eclipse integration prior to migration please [email Support]({{site.baseurl}}/support_contact/) for assistance.
{% endalert %}

## Step 1
In your command line, clone the [Braze Android Github Repository][03].

```bash
$ git clone git@github.com:Appboy/appboy-android-sdk.git
```

## Step 2
Import the Braze project into your local workspace

In Eclipse:

  - Navigate to File > Import.

    ![File Import][2]
  - Select Android > Existing Android Code into Workspace.

    ![Android Import][3]
  - Click "Browse."

    ![Browse][4]
  - Check the Braze UI project folder as well as "copy project into workspace" and click "Finish."

    ![Select Android UI Project][5]

## Step 3
Reference Braze in your own project. In Eclipse:

  - Right click your project and select "Properties."

    ![Click Properties][6]
  - Under "Android," click "Add..." in the Library section and add android-sdk-ui as a library to your app.

    ![Braze Add][7]

## Step 4
Resolve dependency errors and correct build target.

At this time, you may see errors coming up with the Braze code, that is because its dependencies are not populated and the build target is possibly incorrect:

   - Right click the Braze UI project and  select Properties->Android to make sure build target is set to Braze’s current build tools version.

      ![Build Target][8]
   - Right click the Braze UI project and  select Properties->Java Build Path->Add JARs… and add ‘android-support-v4.jar’ from the main application as a library.

      ![Support][9]

## Step 5

Add final pieces.

  - For SDK version 1.10.0 or higher, you will need to add `<service android:name="com.appboy.services.AppboyDataSyncService" />` to your AndroidManifest.xml, as Eclipse does not support manifest merging.

  - For SDK version 1.7.0 or higher, you will need to copy "assets/fontawesome-webfont.ttf" from our library project to your application. Eclipse does not automatically include the assets folder from libraries.

[2]: {{site.baseurl}}/assets/img_archive/file_import.png
[3]: {{site.baseurl}}/assets/img_archive/android_import.png
[4]: {{site.baseurl}}/assets/img_archive/click_browse.png
[5]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[6]: {{site.baseurl}}/assets/img_archive/click_properties.png
[7]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[8]: {{site.baseurl}}/assets/img_archive/build_target.png
[9]: {{site.baseurl}}/assets/img_archive/android_support_v4.png

[03]: https://github.com/appboy/appboy-android-sdk "Appboy Android Github Repository"
