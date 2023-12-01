## Locating the directory

In your text editor, select the `_docs` directory, then open the directory of the [Jekyll collection]() you'd like to add your page to.

```plaintext
_docs
├── _api
├── _developer_guide
├── _docs_pages
├── _help
├── _hidden
├── _home
├── _partners
└── _user_guide
```

Next, find the directory of the subsection you'd like to add your new page to. For example, to add a new page to the [Getting Started]({{site.baseurl}}developer_guide/platform_wide/getting_started) section in the [Developer Guide]({{site.baseurl}}developer_guide/home), go to:

```plaintext
_docs
├── _api
├── _developer_guide
│   └── platform_wide
│       └── getting_started
├── _docs_pages
├── _help
├── _hidden
├── _home
├── _partners
└── _user_guide
```

{% alert tip %}
URLs on Braze Docs always match the directory structure within the docs repository. Use a page or section's URL to help find your way around.
{% endalert %}