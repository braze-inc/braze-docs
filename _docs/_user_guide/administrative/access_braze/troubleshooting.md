---
nav_title: Troubleshooting
article_title: Troubleshooting Braze Access
page_order: 8
page_type: reference
description: "This article guides you through troubleshooting issues you may have when trying to access Braze."

---

# Troubleshooting Braze access

> This article helps you troubleshooting issues you may have when trying to access Braze.

## Locked out of account

So you're locked out of your Braze Account—no worries! We can help you get back in.	

You can tell what kind of lock out you're experiencing by the error message you receive:	

- [I see an error about my password.](#password-error)	
- [I don't see an error, but Braze still won't let me in.](#instance-error)	
- [I see an error about account suspension.](#account-suspension)	

### Password error

Your account security is important to us, so passwords are required to log into your Braze account.	
- Check that you are logging into the correct [Braze dashboard instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Check with your account administrator or Braze account manager to be sure.	
- Your password may have expired, so you'll need to [reset it]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- If you use a [single sign-on]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) service, check with your account administrator that the set up has been completed properly.	
- If your company is on several instances of Braze, you may be using the incorrect email to log in.  	

When in doubt, you can always [reset your password]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Instance error

If you are using the same machine you usually do to log in, Braze should automatically detect the correct instance. However, in the event that it doesn't or you're logging in for the first time, we recommend that you consider the following:	

- Check that you are logging into the correct [Braze dashboard instance]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Check with your account administrator or Braze account manager to be sure.
- If your company is on several instances of Braze, you may be using the incorrect email to log in.	

### Account suspension	

This doesn't happen very often, but we take account suspension and deletions very seriously. If you encounter this error, we recommend reaching out to your company's Braze administrator, Braze account manager, or [Support][support].

## Braze dashboard won't load or work as expected

First, test if the dashboard will load in a different browser. If the issue doesn't persist in a different browser, try the following:

- **Re-launch the dashboard:** Log out, quit your browser, then try to log into your dashboard.
- **Refresh your local browser:** [Clear your cookies and browser cache]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies), then try to log into your dashboard again.
- **Use compatible plugins or third-party tools:** Ad-blockers or security software may prevent the Braze dashboard from loading. Test this by disabling an ad-blocker, then logging into your Braze dashboard.
        - You can also check your browser console logs. Errors related to `ERR_BLOCKED_BY_CLIENT` may indicate the content is blocked by an ad blocker.
- **Check your connection quality:** Your connection quality may be poor. Try logging into your Braze dashboard on a different device.
- **Confirm you're accessing the correct cluster:** Make sure you're logging into the cluster that is assigned to your company. For example, you may be assigned to US-03, but you're logging into US-01.
- **Update your browser:** Update your browser to the latest [supported browser]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers), then try to log into your dashboard.

If the issue occurs on all browsers, try the following:

- **Check your network connection:** Try turning off your VPN, if possible, or disable and re-enable your network connection.
- **Restart your device:** Try logging into your Braze dashboard after restarting your device.

If you've solved the prior issues and your dashboard still won't load or work as expected, contact [Support]({{site.baseurl}}/braze_support/).

## The user belongs to no workspace

Verify this by going to **Settings** > **Company Users** and checking the user's workspace-level permissions. Add the necessary workspaces to **Workspaces**.

## Troubleshooting as a new user

If you're a new Braze user having trouble logging in or accessing your account for the first time, follow these steps to resolve common issues:

### I never received the welcome email

- Check your spam folder: Confirm that the account activation email wasn't filtered into your spam or junk folder.
- Verify your email address: Have your admin check the email address associated with your new Braze account to confirm it's correct.
- IT policies: Confirm with your IT team that there aren't policies in place that might prevent the activation email from being received.

### I received the email, but I'm stuck setting up two-factor authentication (2FA)

- Reset 2FA: If you're having trouble setting up 2FA, your admin can reset 2FA for your user account in the settings.
- Re-add user: If issues persist, the admin can delete your user account from the dashboard and re-add you. This allows for the creation of the user with the same details.

If problems continue after these steps, contact [Support]({{site.baseurl}}/braze_support/) for further assistance.