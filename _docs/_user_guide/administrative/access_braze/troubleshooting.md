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
- Check that you are logging into the correct [Braze dashboard instance][1]. Check with your account administrator or Braze account manager to be sure.	
- Your password may have expired, so you'll need to [reset it][2].	
- If you use a [single sign-on][3] service, check with your account administrator that the set up has been completed properly.	
- If your company is on several instances of Braze, you may be using the incorrect email to log in.  	

When in doubt, you can always [reset your password][2].	

### Instance error

If you are using the same machine you usually do to log in, Braze should automatically detect the correct instance. However, in the event that it doesn't or you're logging in for the first time, we recommend that you consider the following:	

- Check that you are logging into the correct [Braze dashboard instance][1]. Check with your account administrator or Braze account manager to be sure.
- If your company is on several instances of Braze, you may be using the incorrect email to log in.	

### Account suspension	

This doesn't happen very often, but we take account suspension and deletions very seriously. If you encounter this error, we recommend reaching out to your company's Braze administrator, Braze account manager, or [Support][support].

## Braze dashboard won't load or work as expected 

Your dashboard may not load or work because of the following:

- **You're accessing the wrong cluster:** Make sure you're logging into the cluster that is assigned to your company. For example, you may be assigned to US-03, but you're logging into US-01.
- **Your connection quality is poor:** Try logging into your Braze dashboard on a different device.
- **Your local browser needs to be refreshed:** [Clear your cookies and browser cache]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies), then try to log into your dashboard again.
- **Your browser is outdated:** Update your browser to the latest [supported browser]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers), then try to log into your dashboard.
- **You're using incompatible plugins or third-party tools:** Ad-blockers or security software may prevent the Braze dashboard from loading. Test this by disabling an ad-blocker, then logging into your Braze dashboard.

If you've solved the prior issues and your dashboard still won't load or work as expected, contact [Support][support].

[support]: {{site.baseurl}}/braze_support/	
[1]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances
[2]: {{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/
[45]: {% image_buster /assets/img_archive/enable_reset.png %}
