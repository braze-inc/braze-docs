### Adding images

To add images in your page, place the image's PNG file inside the relevant location within `assets/img`, then using the following syntax:

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

Replace the following:

| Placeholder | Description                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | The alt text for the image. This is required to ensure Braze Docs is equally accessible for those using screen readers. |
| `IMAGE`     | The relative path to your image starting from the `img` directory.                                                      |
{: .reset-td-br-1 .reset-td-br-2}

Your in-line image should be similar to the following:

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert note %}
For a full walkthrough, see [Adding a new image]({{site.baseurl}}/home/contributing/content_management/images/).
{% endalert %}
