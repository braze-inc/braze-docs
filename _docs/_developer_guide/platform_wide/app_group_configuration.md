---
nav_title: App Group Configuration
page_order: 1
---
# App Group Configuration

Braze organizes your apps via "App Groups." Think of each of these app groups as an individual title. For example, you should group the iOS and Android versions of the same application or a free and paid versions. These two apps should be in the same group to allow for ease of navigation, segmentation, and messaging across both platforms.

## Creating your App Group in "My Apps"

### Step 1: Click on the "<i class='icon-plus'> </i>  Add App Group" button in the sidebar

![Add App Group][3]

Type the name of your app group into the form.

Once you have created your app group, you will be taken to the app settings page. Generally, you can access this page by navigating to the Apps tab at the top of the page and pressing the <i class='icon-cog'></i> icon on the sidebar.

![Braze App Settings][4]

### Step 2: Add Your Apps

Using the form at the top right of your screen, select your platform, type in the name of your app, and click "Add App"

- After adding your app, you will have access to its API key, which you will need to complete SDK integration.
    - You must create separate app instances for each version of your app on each platform. For example, if you have Free and Pro versions of your app on both iOS and Android you will have 4 app instances within your app group and must use the appropriate API key that is generated for each app.

![Braze API Input][5]

### Step 3: Add a Testing App Group

Braze recommends that you create a "Testing App Group" for integration and campaign testing. The App Group feature can also be utilized for app testing by completely sandboxing certain users from your production instance. Simply create a new app group and remember to switch your API codes so your production environments are not corrupted with false data. When you publish your application, be sure to change the API key that Braze is using to match that of your "Production App Group" rather than your "Testing App Group"

[3]: {% image_buster /assets/img_archive/add_appgroup.png %}
[4]: {% image_buster /assets/img_archive/new_app_landing.png %} "Braze App Settings"
[5]: {% image_buster /assets/img_archive/App_Setup_API.png %} "Braze API Input"
