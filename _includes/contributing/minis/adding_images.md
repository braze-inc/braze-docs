### Add images

To add images in your page, place the image's PNG file inside the relevant location within `assets/img`, then using the following syntax:

```markdown
{% raw %} {% image_buster /assets/PATH_TO_IMAGE %} {% endraw %}
```

Replace `PATH_TO_IMAGE` with the path to your image, including the file extension. Your image link should be similar to the following:

{% raw %}
```markdown
In Braze, select **User Settings**.

{% image_buster assets/img/braze_platform/user_settings.png %}
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Adding a new image]().
{% endalert %}