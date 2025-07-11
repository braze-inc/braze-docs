# Braze React Native iOS Banner Troubleshooting Guide

## Overview
This guide covers troubleshooting steps for when Braze banners are not displaying in your React Native iOS application. Banners are distinct from in-app messages and have their own specific requirements.

## Essential Implementation Checklist

### 1. SDK Installation & Setup
- [ ] **Correct SDK Version**: Ensure you're using the latest version of `braze-react-native-sdk`
- [ ] **Proper Installation**: Verify React Native autolinking worked correctly
- [ ] **iOS Dependencies**: Confirm CocoaPods installation completed successfully

```bash
# Install the SDK
npm install braze-react-native-sdk

# iOS setup
cd ios && pod install
```

### 2. SDK Configuration
- [ ] **API Key**: Verify your API key is correct and matches your Braze dashboard
- [ ] **Endpoint**: Ensure the correct endpoint URL is configured
- [ ] **SDK Initialization**: Confirm the SDK is properly initialized

```javascript
import Braze from 'braze-react-native-sdk';

// Initialize the SDK
Braze.initialize('YOUR_API_KEY', {
  baseUrl: 'YOUR_ENDPOINT_URL',
  enableLogging: true // Enable for debugging
});
```

### 3. iOS-Specific Requirements
- [ ] **Bundle Identifier**: Matches exactly between your app and Braze dashboard
- [ ] **iOS Deployment Target**: Meets minimum requirements (iOS 12.0+)
- [ ] **Swift Version**: Ensure compatible Swift version (5.0+)

### 4. Banner Campaign Configuration
- [ ] **Campaign Status**: Verify the banner campaign is active in Braze dashboard
- [ ] **Targeting**: Confirm your user meets the targeting criteria
- [ ] **Scheduling**: Check if campaign is scheduled correctly
- [ ] **Frequency Capping**: Ensure user hasn't exceeded frequency limits

## Common Issues & Solutions

### Issue 1: Banners Not Displaying at All

**Check SDK Initialization:**
```javascript
// Verify SDK is initialized before trying to display banners
const isInitialized = await Braze.isInitialized();
if (!isInitialized) {
  console.log('Braze SDK not initialized');
}
```

**Enable Debug Logging:**
```javascript
// Add to your configuration
Braze.initialize('YOUR_API_KEY', {
  baseUrl: 'YOUR_ENDPOINT_URL',
  enableLogging: true,
  logLevel: 'debug'
});
```

### Issue 2: User Not Receiving Banners

**Verify User Identification:**
```javascript
// Ensure user is properly identified
Braze.changeUser('user_id_123');

// Set user attributes if needed
Braze.setFirstName('John');
Braze.setLastName('Doe');
Braze.setEmail('john.doe@example.com');
```

**Check User Eligibility:**
```javascript
// Manually request banner display (if supported)
Braze.requestBannerRefresh();
```

### Issue 3: iOS-Specific Problems

**Info.plist Configuration:**
Ensure your `Info.plist` includes necessary permissions:
```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <false/>
</dict>
```

**AppDelegate Configuration:**
Verify your `AppDelegate.m` or `AppDelegate.swift` is properly configured:

```objc
// AppDelegate.m
#import <BrazeKit/BrazeKit.h>

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Initialize Braze
    [BRZBraze configureWithConfiguration:configuration];
    
    return YES;
}
```

### Issue 4: Banner Display Timing

**Session Management:**
```javascript
// Ensure sessions are properly tracked
Braze.openSession();

// Track when app comes to foreground
import { AppState } from 'react-native';

AppState.addEventListener('change', (nextAppState) => {
  if (nextAppState === 'active') {
    Braze.openSession();
  }
});
```

## Debug Steps

### 1. Enable Comprehensive Logging
```javascript
// Enable all logging
Braze.initialize('YOUR_API_KEY', {
  baseUrl: 'YOUR_ENDPOINT_URL',
  enableLogging: true,
  logLevel: 'verbose'
});
```

### 2. Check Network Connectivity
- [ ] Verify device has internet connection
- [ ] Check if corporate firewall blocks Braze endpoints
- [ ] Test on different networks (WiFi vs cellular)

### 3. Test with Different Users
- [ ] Create a test user in Braze dashboard
- [ ] Set up a simple banner campaign targeting test users
- [ ] Test with different user attributes

### 4. Platform-Specific Testing
- [ ] Test on iOS Simulator
- [ ] Test on physical iOS device
- [ ] Test on different iOS versions

## Validation Steps

### 1. Verify in Braze Dashboard
- [ ] Check campaign analytics for impressions
- [ ] Verify user appears in audience
- [ ] Check campaign eligibility rules

### 2. Test Banner Triggers
```javascript
// Trigger custom events that might show banners
Braze.logCustomEvent('banner_trigger_event', {
  'property': 'value'
});
```

### 3. Manual Testing
- [ ] Fresh app install
- [ ] Clear app data and test
- [ ] Test in different app states (foreground/background)

## Common Troubleshooting Commands

```bash
# Clean and rebuild iOS
cd ios
rm -rf Pods/ Podfile.lock
pod install
cd ..
npx react-native run-ios

# Check React Native version compatibility
npx react-native info

# Verify SDK installation
npm ls braze-react-native-sdk
```

## When to Contact Support

Contact Braze support if:
- [ ] All checklist items are verified but banners still don't display
- [ ] SDK logs show errors you can't resolve
- [ ] Campaigns work on other platforms but not iOS
- [ ] You need help with advanced banner customization

## Additional Resources

- **Braze React Native SDK Documentation**: [Link to official docs]
- **Braze iOS SDK Requirements**: [Link to iOS requirements]
- **Campaign Setup Guide**: [Link to campaign setup]
- **Troubleshooting Forum**: [Link to community forum]

## Notes

- Banners may have different display behaviors compared to in-app messages
- Some banner types may require specific SDK versions
- Always test on physical devices when possible
- Check iOS version compatibility with your Braze SDK version