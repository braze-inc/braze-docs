---
nav_title: Resetting push permissions
article_title: Resetting Push Permissions
page_type: solution
description: "This help article covers how to reset browser push permissions and data."
channel: push
---

# Resetting push permissions

If you're experiencing issues with push notifications in your browser, you may need to reset your site's notification permissions and clear your site's storage. Refer to these steps for help.

## Reset Chrome on desktop

1. Next to your URL in the Chrome browser, click the **View Site Information** slider icon.
2. Under **Notifications**, click **Reset permission**.
3. Open Chrome DevTools. The following are the relevant shortcuts per operating system.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Keyboard shortcuts                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4. In DevTools, navigate to the **Application** tab.
5. In the sidebar, select **Storage**.
6. Click **Clear site data**.
7. Chrome will prompt you to reload the page to apply your updated settings. Click **Reload**.

Your push permissions are now reset. Open a new tab to your site and try it out.

## Reset Chrome on Android

If you have a notification from your site visible in your Android notification drawer:

1. From the push notification, tap <i class="fas fa-cog" title="Settings"></i> and select **Site settings**.
2. From **Site settings**, tap **Clear & Reset**.

If you don't have a notification from your site open:

1. Open Chrome on Android.
2. Tap the <i class="fas fa-ellipsis-vertical"></i> menu.
3. Go to **Settings** > **Site Settings** > **Notifications**.
4. Verify notifications are set to "Ask before sending (recommended)".
5. Find your site on the list.
6. Select the entry and tap **Clear and Reset**.

Your push permissions are now reset. Open a new tab to your site and try it out.

## Reset Firefox on desktop

1. Next to your site URL, click <i class="fa-solid fa-circle-info" alt="info icon"></i> or <i class="fas fa-lock" alt="lock icon"></i>.
2. Under **Permissions**, next to **Receive Notifications**, select <i class="fa-solid fa-circle-xmark" title="Clear this permission and ask again"></i> to clear notification permissions.
3. On the same menu, select **Clear Cookies and Site Data**.
4. A dialog will appear to confirm your choice. Click **OK**.

Your push permissions are now reset. Open a new tab to your site and try it out.

## Reset Firefox on Android

To reset push permissions on Android, refer to this [Mozilla support article](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

## Reset Safari on macOS

{% alert note %}
These steps are for macOS only, as Apple does not support Web Push for Safari on Windows.
{% endalert %}

1. Open Safari.
2. From the [menu bar on Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), go to **Safari** > **Settings** > **Websites** > **Notifications**.
3. Select your site from the list.
4. Click **Remove** to delete notification permissions for the site.
5. Then, go to **Privacy** > **Manage Website Data**.
6. Select your site from the list.
7. Click **Remove**, or to remove all site data, click **Remove All**.
8. Click **Done**.

Your push permissions are now reset. Open a new tab to your site and try it out.


*Last updated on February 12, 2024*