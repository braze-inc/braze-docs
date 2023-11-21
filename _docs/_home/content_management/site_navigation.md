---
nav_title: Site navigation
page_order: 3
noindex: true
---

# Site navigation

> TODO

## Page URLs

Within each folder, markdown files added will mimic the url link to the file. For example:

`/_docs/_developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup.md`

Will be:

`https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/`

## Navigation

The left navigation will use the URL to determine how to build the left navigation. In the above, the left nav will place each folder as a child of the parent folder.

```plaintext
From Developer Guide
└── Platform Integration Guides/
    └── iOS/
        └── Initial SDK Setup/
            └── Set Up/
```

## Updating Page Order and Weights

Add the desired page order into the YAML at the top of your edited `.md` file:

```yaml
---
nav_title: Creating a News Feed Item
page_order: 3
---
```

Refer to [YAML & Metadata Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts) for additional metadata options.
