---
nav_title: Rich Notifications
article_title: Rich Push Notifications for iOS
platform: iOS
page_order: 3
description: "This article covers how to implement rich push notifications in your iOS application."
channel:
  - push

---

# iOS 10 Rich Notifications

iOS 10 introduces the ability to send push notifications with images, gifs, and video. To enable this functionality, clients must create a `Service Extension`, a new type of extension that enables modification of a push payload before it is displayed.

## Creating A Service Extension
To create a [Notification Service Extension][23], navigate to `File > New > Target` and select `Notification Service Extension`.

![Adding a Service Extension][26]

Ensure that `Embed In Application` is set to embed the extension in your application.

## Setting Up The Service Extension
A `Notification Service Extension` is its own binary that is bundled with your app. As such, it must be set up in the [Apple Developer Portal][27] with its own App ID and Provisioning Profile.

### Configuring The Service Extension To Work With Braze
Braze sends down an attachment payload in the APNs payload under the `ab` key that we use to configure, download and display rich content:

For example:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

The relevant payload values are:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

To manually display push with a Braze payload, download the content from the value under `AppboyAPNSDictionaryAttachmentURLKey`, save it as a file with the file type stored under the `AppboyAPNSDictionaryAttachmentTypeKey` key, and add it to the notification attachments.

You can write the Service Extension in either Objective-C or Swift. To implement the Service Extension using our sample code, you can copy the below code into your `Notification Service Extension` and change its class name to the one you picked.

{% tabs %}
{% tab OBJECTIVE-C %}

#### NotificationService.h

```objc
#import <UserNotifications/UserNotifications.h>

@interface NotificationService : UNNotificationServiceExtension

@end
```

#### NotificationService.m

```objc
#import "NotificationService.h"
#import <UIKit/UIKit.h>

static NSString *const AppboyAPNSDictionaryKey = @"ab";
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";

@interface NotificationService ()

@property (nonatomic, strong) void (^contentHandler)(UNNotificationContent *contentToDeliver);
@property (nonatomic, strong) UNMutableNotificationContent *bestAttemptContent;
@property (nonatomic, strong) UNMutableNotificationContent *originalContent;
@property BOOL abortOnAttachmentFailure;
@property NSURLSession *session;

@end

@implementation NotificationService

- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {
  self.contentHandler = contentHandler;
  self.bestAttemptContent = [request.content mutableCopy];
  self.originalContent = [request.content mutableCopy];
  self.abortOnAttachmentFailure = NO;
  
  [self.class logMessage:@"Push with mutable content received"];
  
  NSMutableArray *attachments = [NSMutableArray arrayWithCapacity:1];
  NSDictionary *userInfo = request.content.userInfo;
  
  // Check that the push is from Braze
  if (userInfo == nil || userInfo[AppboyAPNSDictionaryKey] == nil) {
    [self.class logMessage:@"Push not from Braze."];
    // Note: if you have other push senders and want to handler here, fork your code here to handle
    [self displayOriginalContent];
    return;
  }
  
  NSDictionary *appboyPayload = userInfo[AppboyAPNSDictionaryKey];
  
  // Check that the push has an attachment
  if (appboyPayload[AppboyAPNSDictionaryAttachmentKey] == nil) {
    [self.class logMessage:@"Push has no attachment."];
    [self displayOriginalContent];
    return;
  }
  
  NSDictionary *attachmentPayload = appboyPayload[AppboyAPNSDictionaryAttachmentKey];
  
  // Check that the attachment has a URL
  if (attachmentPayload[AppboyAPNSDictionaryAttachmentURLKey] == nil) {
    NSLog(@"Push attachment has no url.");
    [self displayOriginalContent];
    return;
  }
  
  NSString *attachmentURLString = attachmentPayload[AppboyAPNSDictionaryAttachmentURLKey];
  [self.class logMessage:@"Attachment URL string is %@", attachmentURLString];
  
  // Get the type
  if (attachmentPayload[AppboyAPNSDictionaryAttachmentTypeKey] == nil) {
    NSLog(@"Push attachment has no type.");
    [self displayOriginalContent];
    return;
  }
  
  NSString *attachmentType = attachmentPayload[AppboyAPNSDictionaryAttachmentTypeKey];
  [self.class logMessage:@"Attachment type is %@", attachmentType];
  NSString *fileSuffix = [@"." stringByAppendingString:attachmentType];
  
  // Download, store, and attach the content to the notification
  if (attachmentURLString) {
    NSURL *attachmentURL = [NSURL URLWithString:attachmentURLString];
    self.session = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
    [[self.session downloadTaskWithURL:attachmentURL
                completionHandler:^(NSURL *temporaryFileLocation, NSURLResponse *response, NSError *error) {
                  if (error != nil) {
                    [self.class logMessage:@"Error fetching attachment, displaying content unaltered: %@", [error localizedDescription]];
                    [self displayOriginalContent];
                    return;
                  } else {
                    [self.class logMessage:@"Data fetched from server, processing with temporary file url %@", [temporaryFileLocation absoluteString]];

                    NSFileManager *fileManager = [NSFileManager defaultManager];
                    NSURL *typedAttachmentURL = [NSURL fileURLWithPath:[temporaryFileLocation.path stringByAppendingString:fileSuffix]];
                    [fileManager moveItemAtURL:temporaryFileLocation toURL:typedAttachmentURL error:&error];
                    
                    NSError *attachError = nil;
                    UNNotificationAttachment *attachment = [UNNotificationAttachment attachmentWithIdentifier:@"" URL:typedAttachmentURL options:nil error:&attachError];
                    if (attachment == nil) {
                      [self.class logMessage:@"Attachment returned error: %@", [attachError localizedDescription]];
                      [self displayOriginalContent];
                      return;
                    }

                    attachments[0] = attachment;
                    self.bestAttemptContent.attachments = attachments;
                    self.contentHandler(self.bestAttemptContent);
                    [self.session finishTasksAndInvalidate];
                  }
                }] resume];
  }
}

+ (void)logMessage:(NSString *)message, ... {
  va_list args;
  va_start(args, message);
  NSLog(@"%@", [[NSString alloc] initWithFormat:[@"[APPBOY] " stringByAppendingString:message] arguments:args]);
  va_end(args);
}

- (void)displayOriginalContent {
  [self.class logMessage:@"Displaying original content"];
  self.contentHandler(self.originalContent);
}

- (void)serviceExtensionTimeWillExpire {
  [self.session invalidateAndCancel];
  [self.class logMessage:@"Service extension called, displaying original content"];
  // Called just before the extension will be terminated by the system.
  // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.
  [self displayOriginalContent];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import UserNotifications
import UIKit

let AppboyAPNSDictionaryKey = "ab"
let AppboyAPNSDictionaryAttachmentKey = "att"
let AppboyAPNSDictionaryAttachmentURLKey = "url"
let AppboyAPNSDictionaryAttachmentTypeKey = "type"

class NotificationService: UNNotificationServiceExtension {
  
  var bestAttemptContent: UNMutableNotificationContent?
  var contentHandler: ((UNNotificationContent) -> Void)?
  var originalContent: UNMutableNotificationContent?
  var abortOnAttachmentFailure: Bool = false
  
  override func didReceive(_ request: UNNotificationRequest, withContentHandler handler: @escaping (UNNotificationContent) -> Void) {
    
    contentHandler = handler
    bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)
    originalContent = (request.content.mutableCopy() as? UNMutableNotificationContent)
      
    print("[APPBOY] Push with mutable content received.")
      
    guard let appboyPayload = request.content.userInfo[AppboyAPNSDictionaryKey] as? [AnyHashable : Any] else { return displayOriginalContent("Push is not from Appboy.") }
    
    guard let attachmentPayload = appboyPayload[AppboyAPNSDictionaryAttachmentKey] as? [AnyHashable : Any] else { return displayOriginalContent("Push has no attachment.") }
    
    guard let attachmentURLString = attachmentPayload[AppboyAPNSDictionaryAttachmentURLKey] as? String else { return displayOriginalContent("Push has no attachment.") }
    
    guard let attachmentURL = URL(string: attachmentURLString) else { return displayOriginalContent("Cannot parse \(attachmentURLString) to URL.") }
    
    print("[APPBOY] Attachment URL string is \(attachmentURLString)")
    
    guard let attachmentType = attachmentPayload[AppboyAPNSDictionaryAttachmentTypeKey] as? String else { return displayOriginalContent("Push attachment has no type.") }
    
    print("[APPBOY] Attachment type is \(attachmentType)")
    let fileSuffix: String = ".\(attachmentType)"
    
    // Download, store, and attach the content to the notification
    let session = URLSession(configuration: URLSessionConfiguration.default)
      
    session.downloadTask(
      with: attachmentURL,
      completionHandler: { (temporaryFileLocation, response, error) in
        
      guard let temporaryFileLocation = temporaryFileLocation, error == nil else {
        return self.displayOriginalContent("Error fetching attachment, displaying content unaltered: \(String(describing: error?.localizedDescription))")
      }
        
      print("[Appboy] Data fetched from server, processing with temporary file url \(temporaryFileLocation.absoluteString)")
        
      let typedAttachmentURL = URL(fileURLWithPath:"\(temporaryFileLocation.path)\(fileSuffix)")
        
      do {
        try FileManager.default.moveItem(at: temporaryFileLocation, to: typedAttachmentURL)
      }
      catch {
        return self.displayOriginalContent("Failed to move file path.")
      }
        
      guard let attachment = try? UNNotificationAttachment(identifier: "", url: typedAttachmentURL, options: nil) else { return self.displayOriginalContent("Attachment returned error.") }
        
      guard let bestAttemptContent = self.bestAttemptContent else { return self.displayOriginalContent("bestAttemptContent is nil") }
        
      bestAttemptContent.attachments = [attachment];
      handler(bestAttemptContent);
      }).resume()
  }
    
  func displayOriginalContent(_ extraLogging: String) {
    print("[APPBOY] \(extraLogging)")
    print("[APPBOY] Displaying original content.")
      
    guard let contentHandler = contentHandler, let originalContent = originalContent else { return }
    
    contentHandler(originalContent)
  }
    
  override func serviceExtensionTimeWillExpire() {
    // Called just before the extension will be terminated by the system.
    // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.
    displayOriginalContent("Service extension called, displaying original content.")
  }

}
```

{% endtab %}
{% endtabs %}

## Creating A Rich Notification In Your Dashboard

To create a rich notification in your Braze dashboard, simple create an iOS push and attach an image or gif, or provide a url that hosts an image, gif, or video.  Note that assets are downloaded on the receipt of push notifications, so that if you are hosting your own content you should plan for large, synchronous spikes in requests.

Also note the supported file types and sizes, listed [here][28].


[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
