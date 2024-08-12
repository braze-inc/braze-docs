---
nav_title: Sanitization
article_title: Sanitization
page_order: 4
description: "This article defines sanitization and its purpose for email messaging in Braze."
channel:
  - email

---

# About sanitization

> Sanitization is a process that occurs when Braze detects a specific type of JavaScript in your email message.

## Why do we perform sanitization?

The main purpose of sanitization is to prevent bad actors from accessing other Braze dashboard users’ session data. Without sanitization, a bad actor with basic read-only access can create an email using the CKEditor with JavaScript that "sends current browser session" to anywhere the bad actor wants using a network request.

When another dashboard user opens that email template, the JavaScript will execute and send the current user’s session data to the bad actor.

As a note, most email inbox providers do not process JavaScript, so this measure is also meant to remove unnecessary bloat from emails, reducing its size. 

## How does Braze sanitize messages?

If Braze detects JavaScript that is a security risk, before you go to the **Preview and Test** tab or the HTML editor to view the email message, we'll ask you to confirm that Braze can remove the JavaScript from your message before proceeding.

![]({% image_buster /assets/img/email_sanitization.png %})

## When are sanitizations persisted?

In both the drag-and-drop editor and the HTML editor, we sanitize, but do not persist the sanitized results for the following scenarios:

* The email is rendered in the following areas:
    * **Inbox Vision** section and **Spam Testing** tab
    * **Preview & Heatmap** section under **Email Performance** panel
* The email is sent in a test send

For the drag-and-drop editor, we sanitize and also persist the sanitization in the message when the
editor is closed and the campaign is saved. For the HTML editor, we sanitize and also persist the sanitization in the message when a user switches between editor types and the campaign is saved.

In all of these instances, a message displays if the sanitization modified the HTML. The user must accept this before sanitization is completed.