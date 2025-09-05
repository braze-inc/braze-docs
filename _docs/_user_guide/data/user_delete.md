---
nav_title: User Delete
article_title: User Delete
page_order: 0
description: "TODO" 
---

# User Delete

> User deletion is a tool that Braze customers can use to manage their user base.  Customers who have proper user permissions can perform deletion of user profiles that are no longer needed, created in error, or are undergoing a deletion request for regulatory reasons.

## About user deletion

* Remove errant user profiles  
* Complete a regulatory request to delete a user  
* All without using our [/users/delete endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete) (which requires engineering resources) or asking a support engineer at Braze (takes time).
* Remove errant user profiles  
* Keep user profile counts low by pruning your user base.    
  * For customers on the new FY26 pricing scheme, this can help you avoid overages.  
* Complete a regulatory request (GDPR, CCPA) to delete a user  
* All without using our [/users/delete endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete) (takes engineering resources) or asking a support engineer at Braze (takes time).  
  * Before today, customers can delete through the /users/delete endpoint, using [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/cloud_ingestion/delete_users), or opening a support request.  This gives our customers a more native solution for handling this use case.

other considerations: 

* Braze can delete 100 million user profiles in one given bulk user deletion job run.  
  * A job includes the cool down period of 7-days plus the time it takes to actually do the deletion.  
* You cannot have more than one deletion job running at the same time.    
  * A job includes the cool down period of 7-days plus the time it takes to actually do the deletion.  
* If you have an urgent need to delete more than 100 million user profiles at once, we recommend opening a support case for assistance.

## Prerequisites

Before you get started, make sure your user must be enabled with the “Delete User” permission or you must be an admin.

## Deleting a single user

You should also have the user profile page for the user you want to be deleted. You can get to the user profile page by using user search.

1. Find the user you want to delete via user search.  
2. Click on the “More Actions” button and then the “Delete User” button on the user profile to start the process.   
3. If you can’t click on “Delete User”, it may mean that you do not have the proper permissions.  You can ask an admin to update your permissions if this is in error.  
Note: If you have duplicate users (i.e. user profiles that share the same email address or phone number), you should confirm you are on the page for the profile you want to delete.  Braze will only delete the profile for the profile page you are on.
4. Next, confirm the deletion.    
5. Once you do, we will process the deletion.  This may take a few minutes.  
6. There is **no way to undo a deletion after you have submitted confirmation.**  Please be sure this is the profile you want to delete.

## Deleting multiple users

### Step 1: Verify users

You should be able to identify the user profiles you want to be deleted.

* You should have a segment of users you want to delete **already saved** in Braze.  
  * If you have a CSV file, you can upload this to Braze and use that to create a [segment](https://www.braze.com/docs/user_guide/data/user_data_collection/user_import/#creating-segments-from-a-user-import).  
  * Learn how to create a segment [here](https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment).  
  * If you need to define a subset of a segment, you will need to turn those users into a new segment and select that new segment here.

Note: When you go through the bulk user deletion flow, we’ll “lock” the set of users to be deleted since segments can change dynamically.  You’ll have access to a special inclusion filter that will allow you to find all the user profiles marked for deletion.

### Step 2: Choose a segment

1. Navigate to the Manage Audience Page and the “Delete Users” tab.  
2. If you see a message saying you do not have proper permissions, you will need to get this added to your dashboard user.  You cannot proceed without this permission.  
3. Select the name of the segment of users you want to delete.  
   * You cannot build a segment in this tool, you must build, name, and save the segment in the [segment builder](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/targeting_users/?tab=single%20segment).  
Note: If you need to delete multiple user profiles that share the same email address or phone numbers, ensure your segment contains all of those user profiles.

### Step 3: Confirm your choice

1. Next, you need to confirm that you want to proceed with the deletion.    
* Once you do, we will mark the user profiles as pending deletion.  
* You will have access to a “Segment Membership” filter called “Pending Deletion” where you can pick users scheduled to be deleted on a specific date.  This filter contains all user profiles that have been marked for deletion on that date.  You can use this to target or even to exclude these users from your messaging.  You can use this to generate a list of user profiles to be deleted in case you need it for record keeping.![][image2]  
Note: When we’re marking users for deletion, you won’t see the deletion date show up until all users have been marked.  If you don’t see the date available, we recommend waiting a few hours and coming back to check again.  
* These users will remain in a pending deletion state for 7 days.  
* You (the user who initiated this), your account manager, and your company admins will receive a notification 24 hours prior to the deletion.  
* At any point during the 7-day cooldown period, you may cancel the deletion and we will unmark the users previously marked for deletion.

### Step 4: Delete selected users

* When it is time, Braze will start to delete the user profiles.  
* Bulk user deletion jobs can take some time.  You can always come back to the ‘Delete Users’ tab to see its status.  
  * The “Run Date” field is the date of deletion.  You can use the segment membership filter and this run date to find all the user profiles marked for deletion for an upcoming run date.  
  * The “Segment Name” field is the segment originally used to produce the set of user profiles marked for deletion.  
    * Please note that if your segment is dynamic, there can be drift.  If you need to access the set of users pending deletion, please use the “Pending Deletion” segment membership filter.  
* You can only have one bulk user deletion job scheduled at once.  You must wait for a job to finish before you can schedule another job.  The 7-day cool down period is considered a part of a bulk user deletion job.

![][image3]

## Canceling bulk deletions

* You have 7 days to cancel your deletion job.  
* You can come to the User Deletion tab in Manage Audience at any time in the 7-day cooldown window to cancel your job.  
  * Only users with “Delete User” permissions can cancel a job.  
* When a deletion job is running, you can also cancel the job.  Note that any users who were already deleted cannot be recovered.

## Deleting duplicate users

If you need to delete multiple user profiles that share the same email address or phone number, you must build a segment that contains all of those user profiles. 

## Checking logs

* When a deletion job is finished, you will receive an email telling you that the job is completed.    
* You will see a record on your User Deletion tab in Manage Audience.  This record shows you the dashboard user who initiated the job, its status, and how many user profiles were deleted as a result of the job.  
* You can find an additional log entry through the [Security Event Report](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/security_settings).  
* You will no longer be able to search and find deleted profiles.  
Note: If you need a list of users to be deleted, you will need to get this list beforehand using the provided segmentation [filter]().
* You will also no longer be able to search and find the profile.  

Note: If you search and find the profile again, that may mean that the deletion is not yet finished processing and you may need to wait a few minutes.

## Frequently asked questions {#faq}

### Why is the profile still here after deleting?

No, you may need to wait a few minutes for the request to finish. 

### Can I delete segments with more than 100 million users?

You will not be able to proceed with deletion if the segment is over 100 million.  We recommend opening a support case if you have this use case or using a smaller segment.

### Does automated user merging affect user deletion?

In the event that you have a scheduled merge that includes user profiles that are pending deletion, Braze will **skip** over the user profiles and will not merge them.  This is to avoid polluting the user profiles with data that is due to be removed.  If you want to merge these profiles, you will need to remove them from deletion.

### What happens to data sent to users pending deletion? 

If external systems or SDKs send data to a user who’s in a pending deletion state, the data will still be accepted. However, the users will still be deleted as scheduled--regardless of any recent activity.

### Will Canvases and campaigns trigger for users pending deletion?  

Yes. There is a segment inclusion filter available that you can add to segmentation to exclude all users who have “pending deletion” on their profiles. 

### Can I recover deleted user profiles?  

Yes for bulk. No for single--permanent.
