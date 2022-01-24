---
nav_title: Endpoints
article_title: API endpoint index
page_order: 1
description: "This page lists the available Braze endpoints."
page_type: reference
---

# API endpoint index

## User data

| Method | Endpoints |
| --- | --- |
| POST | [/users/alias/new][/users/alias/new]<br>[/users/delete][/users/delete]<br>[/users/identify][/users/identify]<br>[/users/track][/users/track]<br>[/users/external_ids/rename][/users/external_ids/rename]<br>[/users/external_ids/remove][/users/external_ids/remove]<br>[/users/export/ids][/users/export/ids]<br>[/users/export/segment][/users/export/segment]<br>[/users/export/global_control_group][/users/export/global_control_group] |
{: .reset-td-br-1 .reset-td-br-2}

## Send messages

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

[/sends/id/create]
[/messages/send]
[/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send]
[/campaigns/trigger/send]
[/canvas/trigger/send]


## Schedule messages

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Subscription groups

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Email

email and email templates

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Campaigns

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Canvas

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Segments

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Custom events

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Content Blocks

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## KPI

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## News Feed

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## SMS

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}

## Purchases

| Method | Endpoints |
| --- | --- |
| POST |
| GET |
{: .reset-td-br-1 .reset-td-br-2}


<!--- Links for user data --->

[/users/alias/new]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[/users/delete]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[/users/identify]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[/users/track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[/users/external_ids/rename]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[/users/external_ids/remove]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[/users/export/ids]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[/users/export/segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[/users/export/global_control_group]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/

<!--- Links for send messages --->

[/sends/id/create]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/ 
[/messages/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/
[/campaigns/trigger/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[/canvas/trigger/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
