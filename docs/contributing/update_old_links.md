
# Test page for `ulinks`

> This page is a test fixture for the [`ulinks`](bdocs.md#ulinks) command. Run `./bdocs ulinks docs/contributing/update_old_links.md` against this file to manually verify that bad links are updated and good links are left unchanged. When adding "bad links", the syntax needs to match the syntax documented in [Cross-referencing](content_management/cross_referencing.md).

No `/docs` should be found in the `site.baseurl`.

## Bad links

```
1. [Bad link 1]({{site.baseurl}}/best_practices/).
2. [Bad link 2]({{site.baseurl}}/best_practices/#android-push-category).
3. [Bad link 3]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/).
4. [Bad link 4]({{site.baseurl}}/docs/user_guide/message_building_by_channel/email/link_templates/).
```

## Good links

```
1. [Good link 1](https://www.braze.com/docs/developer_guide/platform_wide/getting_started/analytics_overview)
2. [Good link 2]({{site.baseurl}}/developer_guide/getting_started/analytics_overview)
```
