---
nav_title: Integration Overview
article_title: Getting started&#58; Integration Overview
page_order: 2
description: ""

---

# Getting started: Integration overview

> Before you begin to integrate the Braze, you may find yourself wondering what exactly you're building and integrating. You may be curious about how you can customize Braze to further to meet your needs. This article can help you answer all of your SDK questions. You can also check out our [Technical Integration Checklists and Toolkits](https://learning.braze.com/technical-integration-checklists-and-toolkits) course on Braze Learning.

The Braze platform has three primary components in its logic layer: the [SDK](#sdk), [API](#api), and [partner integrations](#partner-ecosystem). Its presentation layer consists of a UI component called the [dashboard](#dashboard-user-interface) that marketers and admins use to do their jobs.

## Dashboard user interface

The Braze dashboard is the UI component that gives access to all of the analytics and interactions at the heart of the Braze platform. This website displays graphs that are updated in real-time based upon a mix of [automatic and custom data you configure][2]. Marketers use the site to manage notifications, setup targeted messaging campaigns, and view analytics. Developers can use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

## SDK

The Braze SDK helps collect and sync user data across platforms to a consolidated user profile. The SDK automatically collects session data, device info and push tokens. The SDK is also responsible for tracking the engagement analytics (for example, clicking a push notification), and perhaps most importantly, it’s also responsible for ingesting your custom data, such as custom attributes and high-value events that are specific to your business and industry.

The SDK is key not only for data ingestion, but it also displays and handles messaging channels like in-app messages, push notifications, and Content Cards your marketers create in the dashboard.

### Integration  

Our [integration guides][4] provide a step-by-step process for integrating the SDK with many different platforms.

The Braze SDKs are designed to be very well-behaved, and not interfere with other SDKs present in your app. The Braze SDKs have a very small footprint. We automatically change the rate that we flush user data depending on the quality of the network, in addition to allowing manual network control. We automatically batch API requests from the SDK to make sure that data is logged quickly while maintaining maximum network efficiency. Lastly, the amount of data sent from the client to Braze within each API call is extremely small.

#### Default analytics and session handling

Certain user data is collected automatically by our SDK&mdash;for example, First Used App, Last Used App, Total Session Count, Device OS, etc. If you follow our integration guides to implement our SDKs, you will be able to take advantage of this [default data collection][1]. 

{% alert note %}
All of our features are configurable, but we recommend fully implementing the default data collection model and not limiting the collection of data.
{% endalert %}

#### Messaging channels

The SDK powers Braze's messaging tools, allowing for multichannel communication with your users. Your marketing team will use these messaging channels to re-engage lost users, retain active users, and energize your brand ambassadors. For example, here's a view of the dashboard where a marketer would compose a push notification. Because of your work integrating the Braze SDK with your site or app, this notification will be delivered to Android, iOS, and web platforms.

![The push message editor displaying an example push message and title to be sent to the Android, iOS, and Web messaging channels.][5]

### Customization
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#### Crawl
Eu non diam phasellus vestibulum lorem sed. Facilisis sed odio morbi quis commodo odio. Etiam tempor orci eu lobortis elementum nibh tellus. Leo a diam sollicitudin tempor id eu. At ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget. Magna fermentum iaculis eu non diam. Justo nec ultrices dui sapien. Purus non enim praesent elementum. Enim ut tellus elementum sagittis vitae et leo. Leo integer malesuada nunc vel risus. Tincidunt id aliquet risus feugiat. Id faucibus nisl tincidunt eget. Scelerisque eu ultrices vitae auctor eu augue. Aliquet eget sit amet tellus cras adipiscing enim eu turpis. Vitae aliquet nec ullamcorper sit amet risus nullam. Tincidunt vitae semper quis lectus nulla at volutpat. Orci nulla pellentesque dignissim enim sit. Pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Dui id ornare arcu odio ut sem.


#### Walk
Netus et malesuada fames ac turpis egestas. Molestie nunc non blandit massa enim nec dui. Eu consequat ac felis donec et odio pellentesque. Magnis dis parturient montes nascetur ridiculus mus mauris. Accumsan lacus vel facilisis volutpat est velit. Fermentum iaculis eu non diam phasellus vestibulum. Non pulvinar neque laoreet suspendisse interdum consectetur libero. Feugiat scelerisque varius morbi enim nunc faucibus. Tortor id aliquet lectus proin nibh nisl. Suscipit tellus mauris a diam. Et tortor consequat id porta nibh. Est lorem ipsum dolor sit amet consectetur adipiscing. Condimentum vitae sapien pellentesque habitant morbi tristique. Ipsum dolor sit amet consectetur.

#### Run
Nibh venenatis cras sed felis eget velit aliquet. Leo vel fringilla est ullamcorper eget nulla facilisi. Urna et pharetra pharetra massa massa ultricies mi quis. Amet risus nullam eget felis eget nunc lobortis mattis. Morbi tincidunt ornare massa eget egestas purus viverra accumsan. Metus dictum at tempor commodo ullamcorper a. Aliquet eget sit amet tellus. Nisl tincidunt eget nullam non nisi est sit. In eu mi bibendum neque egestas. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Risus quis varius quam quisque. Pretium aenean pharetra magna ac placerat vestibulum lectus mauris. Nunc sed augue lacus viverra vitae. Ullamcorper malesuada proin libero nunc consequat. Amet est placerat in egestas erat imperdiet sed. Facilisi morbi tempus iaculis urna id volutpat lacus laoreet.


## API

The Braze REST API supplements the SDK by providing additional functionality. With the API you can sync offline high-value information like orders, coupons, or other data happening outside of your app, as well as maintain email opt-in/opt-out and tons of other data. We have tons of purpose-built endpoints, as well as sample requests and responses in our [documentation][3].

### Endpoints

Aliquet eget sit amet tellus cras adipiscing enim eu turpis. Vitae aliquet nec ullamcorper sit amet risus nullam. Tincidunt vitae semper quis lectus nulla at volutpat. Orci nulla pellentesque dignissim enim sit. Pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Dui id ornare arcu odio ut sem.

### Objects
Netus et malesuada fames ac turpis egestas. Molestie nunc non blandit massa enim nec dui. Eu consequat ac felis donec et odio pellentesque. Magnis dis parturient montes nascetur ridiculus mus mauris. Accumsan lacus vel facilisis volutpat est velit. Fermentum iaculis eu non diam phasellus vestibulum. Non pulvinar neque laoreet suspendisse interdum consectetur libero.

### Postman
Feugiat scelerisque varius morbi enim nunc faucibus. Tortor id aliquet lectus proin nibh nisl. Suscipit tellus mauris a diam. Et tortor consequat id porta nibh. Est lorem ipsum dolor sit amet consectetur adipiscing. Condimentum vitae sapien pellentesque habitant morbi tristique. Ipsum dolor sit amet consectetur.

### Important considerations
Nibh venenatis cras sed felis eget velit aliquet. Leo vel fringilla est ullamcorper eget nulla facilisi. Urna et pharetra pharetra massa massa ultricies mi quis. 

#### Rate limiting
Amet risus nullam eget felis eget nunc lobortis mattis. Morbi tincidunt ornare massa eget egestas purus viverra accumsan.

#### Send requests in bulk when possible
Metus dictum at tempor commodo ullamcorper a. Aliquet eget sit amet tellus. Nisl tincidunt eget nullam non nisi est sit.

#### Add the x-braze-bulk header to bulk uploads
In eu mi bibendum neque egestas. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Risus quis varius quam quisque.

#### Allow for latency when exporting
Pretium aenean pharetra magna ac placerat vestibulum lectus mauris. Nunc sed augue lacus viverra vitae. Ullamcorper malesuada proin libero nunc consequat. Amet est placerat in egestas erat imperdiet sed. Facilisi morbi tempus iaculis urna id volutpat lacus laoreet.

#### Incorporate retry logic
Accumsan tortor posuere ac ut consequat semper viverra. Est ultricies integer quis auctor elit sed vulputate. Purus faucibus ornare suspendisse sed.

#### Make use of threaded requests
Consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus. Cras tincidunt lobortis feugiat vivamus. Semper feugiat nibh sed pulvinar proin gravida hendrerit lectus. 

#### Restrict user data uploads to delta values only
At augue eget arcu dictum varius duis at consectetur. Ac turpis egestas maecenas pharetra convallis posuere morbi leo. Ullamcorper malesuada proin libero nunc consequat interdum varius sit amet. Posuere lorem ipsum dolor sit amet consectetur. Mollis aliquam ut porttitor leo a. Sit amet purus gravida quis. Phasellus egestas tellus rutrum tellus pellentesque eu.

## Partner ecosystem
Lastly, Braze has 50+ technology partnership integrations, or "alloys" as we call them. Braze makes it easy to sync data from our partner integrations to your systems, providing your marketing team with attribution functionality, data augmentation, and audience insights. 

Cursus eget nunc scelerisque viverra mauris in aliquam. Eget est lorem ipsum dolor sit amet consectetur adipiscing elit. Consequat interdum varius sit amet mattis vulputate enim nulla. In nulla posuere sollicitudin aliquam ultrices sagittis orci. Amet risus nullam eget felis eget nunc. Vitae semper quis lectus nulla at. Lacinia quis vel eros donec. Commodo odio aenean sed adipiscing. Odio euismod lacinia at quis risus sed vulputate odio. Id interdum velit laoreet id donec ultrices tincidunt arcu non. Egestas purus viverra accumsan in nisl nisi. Tortor at risus viverra adipiscing at. Amet dictum sit amet justo donec enim. Ornare lectus sit amet est placerat in egestas erat imperdiet. Orci ac auctor augue mauris augue.

[1]: {{site.baseurl}}/developer_guide/platform_wide/getting_started/data_overview/#automatically-collected-data
[2]: {{site.baseurl}}/developer_guide/platform_wide/getting_started/data_overview
[3]: {{site.baseurl}}/api/home
[4]: {{site.baseurl}}/developer_guide/home
[5]: {% image_buster /assets/img_archive/UOiOSPush.png %} "Example Push dashboard"