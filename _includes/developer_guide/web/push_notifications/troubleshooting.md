## Troubleshooting

If you're experiencing issues after setting up push notifications, consider the following:

- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `braze.isPushSupported()` returns `true` in the browser.
- Some browsers, such as Firefox, do not display images in push notifications. For details on browser support, refer to the [MDN documentation for Notification images](https://developer.mozilla.org/en-/docs/Web/API/Notification/image).
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.
