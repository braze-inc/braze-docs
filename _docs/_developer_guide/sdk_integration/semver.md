---
page_order: 1.4
nav_title: SDK Version Management
article_title: Managing your Braze SDK version
description: "This reference article provides best practice recommendations for Braze SDK version management."
---
# Version Support

> In order to get the latest features and quality improvements, we recommend that you adopt newer versions of the Braze SDKs as rapidly as possible.

Braze is continually investing in the feature set, stability and quality of its SDKs. We release new SDK versions rapidly in order to be able to unlock your ability to reach your users consistently, in high quality and with the smoothest developer and marketer experience possible.

Older versions of the Braze SDKs will not always receive bugfixes, and therefore we strongly recommend that you continuously update as part of your regular development process.

## Semantic Versioning

In order to lower the cost of updating versions, all Braze SDKs use [Semantic Versioning](https://semver.org/).

Braze will always respect Semantic Versioning's specifications to update Major, Minor and Patch versions.

Patch version updates are always non breaking, and include important bug fixes. You should always update to the latest patch version for your current major and minor as soon as possible, and the updates will always be safe.

Minor version updates are always non breaking, and include net new functionality. You should update to the latest minor version for your current major version as soon as possible, and updating will never require changes in your application code.

Major version updates are breaking changes, and will likely require changes in your application code.

## Versions with known issues

In order to not break our customers' build pipelines, **we will never alter or remove a release once it is published to a distribution system**, even if that particular release has known issues.

We will publish new patch versions for impacted major and/or minor versions as applicable and appropriate.

Additionally, we will retroactively update changelogs when applicable to indicate that a given version has known issues and should not be used.