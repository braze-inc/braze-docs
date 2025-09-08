---
page_order: 10
nav_title: Version management
article_title: About version management for the Braze SDK
description: "Learn about version management for the Braze SDK."
---

# About version management

> Learn about version management for the Braze SDK, so your app can stay up-to-date with the latest features and quality improvements. Because older versions of the SDK may not receive the latest patch, bugfix, or support, we recommend always keeping your it up-to-date as a part of your ongoing development lifecycle.

## Versioning recommendations

All Braze SDKs adhere to the [Semantic Versioning Specification (SemVer)](https://semver.org/), so given a version number `MAJOR.MINOR.PATCH`, we recommend the following:

|Version|About this Version|Recommendation|
|-------|------------------|--------------|
| `PATCH` | Updates are always non-breaking, and include important bug fixes. They'll always be safe. | You should always try to update to the latest patch version of your current major and minor version immediately. |
| `MINOR` | Updates are always non-breaking, and include net new functionality. They'll never require changes in your application code. | While you don't need to do this immediately, you should update to the latest minor version of your current major version as soon as possible. 
| `MAJOR` | Updates are breaking changes, and may require changes in your application code. | Because this may require code changes, update to the latest major version in a timeframe that works best for your team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Sometimes new Android or Apple OS updates require changes to the Braze SDK. To ensure your app is compatible with newer phones, it's important you keep your SDK up-to-date.
{% endalert %}

## About known issues

To ensure our changes won't break your build pipelines, **we will never alter or remove a release after it's been published to a distribution system**&#8212;even if that particular release has known issues.

In these cases, we'll document the issue to the [Braze SDK changelog]({{site.baseurl}}/developer_guide/changelogs/), then release a new patch for the impacted major or minor versions as soon as possible.
