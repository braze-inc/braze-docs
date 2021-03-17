---
nav_title: Implementation Guide
platform: iOS
page_order: 7
description: ""
---

# Push Notification Implementation Guide

## Content Extensions

Notifcation Content Extension

When a push notification (abbreviated banner view) is 3D pressed or "view"ed, content notification extensions enable a custom view of the expanded push notitfication.

Push Stores are a custom view for notification content extension! What other kinds of custom views can be created?

## Implementation Walkthrough

### Interactive Push Notification

Push notifications can respond to user actions inside a content extension. As of iOS 12, content extensions now have the option of being interactive. 

Push notifications can be opened via 3D press or explicitly slecting "View." 3D press can be diasbled in the device settings.

#### Dashboard Configuration

Custom category is used to determine which view to be displaying in the content extension. Configured on the compose tab by toggling Notication Buttons. 

#### Other Use Cases

Gamification - GAP created this campaign with a custom HTML in-app message. This could be replicated in a push notification

### Personalized Push Notifications

Push notifications can display user-specific information incide a content extension. 

#### Dashboard Configuration

#### Handling Key-Value Pairs

#### Other Use Cases

### Information Capture Push Notification

Push notifications can capture user information incide a content extension.

#### Dashboard Configuration

#### Handling Buttom Actions

Push notication action buttons are uniquely identified to handle responses from buttom presses accordingly.

Push notifcations can be automatically dismissed from an action button press.

#### Other Use Cases

User Input. Other ideas, SMS Capture, Complete Profile, Submit Feedback

## Logging vs. Analytics

Loggin analytics can only be done in real-time with the help of the customer;s server hitting Braze's API user/track endpoint. 

Requires userId parameter, which cannot be queried from Braze SDK.

### Saving Custom Event

1. Initialize a dictionary with event meta data
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending Custom Events to Braze

After the SDK is initialized is the best time to log any saved analytics from a notification content extension

1. Loop through array of pending events
2. Loop through each key-value pair in pending event dictionary
3. Explicitly checking key for “Event Name” to set the value accordingly
4. Every other key-value will be added to the properties dictionary
5. Log individual custom event 
6. Remove all pending events from storage

### Saving Custom Attributes

1. Initialize a dictionary with attribute meta data
2. Initialize userDefaults to retrieve and store the attribute data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending Custom Attributes to Braze

1. Loop through array of pending attributes
2. Loop through each key-value pair in pending attributes dictionary
3. Log individual custom attribute with corresponding key and value
4. Remove all pending attributes from storage

### Saving User Attributes

Custom object that saves user attributes tied to a specific field  (firstName, lastName, email, phoneNumber, etc.)

1. Initialize an encoded UserAttribute object with corresponding type (email)
2. Initialize userDefaults to retrieve and store the event data
3. If there is an existing array, append new data to existing array and save
4. If there is not an existing array, save new array to userDefaults

### Sending User Attributes to Braze

1. Loop through array of pending attribute data
2. Initialize an encoded UserAttribute object from attribute data
3. Set specific user field based on the User Attribute type (email)
4. Remove all pending user attributes from storage

## Key Takeaway

Push Notifications can be extended to function as a new channel:
Out-App Messages* *not a real thing, just made up the names for the sake of the Keynote*

### Public Repository:
https://github.com/braze-inc/braze-growth-shares-ios-demo-app
