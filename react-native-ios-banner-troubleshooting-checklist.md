# React Native iOS Banner Display Troubleshooting Checklist

This checklist covers the most common issues that prevent banners from displaying in React Native iOS applications using Google Mobile Ads SDK.

## 🔧 SDK Setup and Configuration

### ✅ SDK Installation
- [ ] **Correct package installed**: Using `react-native-google-mobile-ads` (not deprecated packages like `react-native-admob`)
- [ ] **Version compatibility**: Using compatible versions of React Native and Google Mobile Ads SDK
- [ ] **Clean installation**: Run clean install if upgrading from older versions
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  cd ios && pod install
  ```

### ✅ iOS Project Configuration
- [ ] **Minimum iOS version**: App targets iOS 12.4 or higher
- [ ] **Deployment target**: Set in both Xcode project settings and Podfile
- [ ] **Swift version**: Project uses Swift 5.2 or higher
- [ ] **Static frameworks**: If using static frameworks, add `$RNGoogleMobileAdsAsStaticFramework = true` to Podfile

## 🏗️ App ID and Ad Unit Configuration

### ✅ Google AdMob Setup
- [ ] **Valid Google AdMob account**: Account is active and verified
- [ ] **iOS app registered**: App is properly registered in AdMob console
- [ ] **App ID configured**: iOS App ID is correctly set in project configuration
- [ ] **Ad units created**: Banner ad units are created in AdMob dashboard

### ✅ Configuration Files
- [ ] **app.json/app.config.js**: Properly configured with iOS app ID
  ```json
  {
    "react-native-google-mobile-ads": {
      "ios_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx",
      "android_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx"
    }
  }
  ```
- [ ] **Expo config plugin**: If using Expo, plugin is properly configured
- [ ] **Bundle ID match**: Bundle ID in Xcode matches AdMob app registration

## 🔑 iOS Permissions and Settings

### ✅ Info.plist Configuration
- [ ] **App Transport Security**: Configured to allow ad network requests
- [ ] **User Tracking Usage Description**: Added if using personalized ads
  ```xml
  <key>NSUserTrackingUsageDescription</key>
  <string>This identifier will be used to deliver personalized ads to you.</string>
  ```
- [ ] **SKAdNetwork items**: Added for iOS 14+ attribution tracking

### ✅ Capabilities and Permissions
- [ ] **App Tracking Transparency**: Properly requested before initializing SDK
- [ ] **Internet permissions**: App has network access
- [ ] **Ad ID permission**: `com.google.android.gms.permission.AD_ID` if applicable

## 🧪 Development vs Production Setup

### ✅ Test vs Production IDs
- [ ] **Test IDs in development**: Using `TestIds.BANNER` during development
- [ ] **Production IDs**: Using real ad unit IDs for production builds
- [ ] **Environment detection**: Proper `__DEV__` conditional logic
  ```javascript
  const adUnitId = __DEV__ ? TestIds.BANNER : 'ca-app-pub-xxxxx/yyyyy';
  ```

### ✅ Build Configuration
- [ ] **Release scheme**: Using Release configuration for production builds
- [ ] **Code signing**: Proper development team and provisioning profile
- [ ] **Bundle identifier**: Matches AdMob app registration exactly

## 🔍 SDK Initialization and Usage

### ✅ Proper SDK Initialization
- [ ] **Initialize before ads**: `mobileAds().initialize()` called before loading ads
- [ ] **Request configuration**: Set before initialization if needed
- [ ] **European consent**: UMP consent handled if targeting EU users
- [ ] **Initialization completion**: Wait for initialization promise to resolve

### ✅ Banner Implementation
- [ ] **Correct component usage**: Using `BannerAd` component properly
- [ ] **Required props**: `unitId` and `size` props provided
- [ ] **Ad loading state**: Handling loading states with `onAdLoaded` callback
- [ ] **Error handling**: Implementing `onAdFailedToLoad` callback

## 🚀 Build and Deployment

### ✅ Build Process
- [ ] **Clean build**: Clean build folder and rebuild
  ```bash
  cd ios
  rm -rf build
  rm -rf Pods
  rm -rf Podfile.lock
  pod install
  ```
- [ ] **Xcode build**: Build successfully in Xcode without errors
- [ ] **No JavaScript errors**: Metro bundler running without errors
- [ ] **Simulator vs Device**: Test on both simulator and physical device

### ✅ Deployment Configuration
- [ ] **App Store compliance**: "Yes, my app contains ads" selected in App Store Connect
- [ ] **AdMob policy compliance**: App content complies with AdMob policies
- [ ] **Privacy policy**: Privacy policy includes ad usage disclosure

## 🔬 Debugging Steps

### ✅ Console Logging
- [ ] **Enable debug logging**: Check for SDK initialization logs
- [ ] **Xcode console**: Monitor native iOS logs in Xcode console
- [ ] **JavaScript console**: Check for JavaScript errors in Metro
- [ ] **Network requests**: Verify ad requests are being made

### ✅ Common Debugging Commands
```bash
# Check if SDK is properly initialized
console.log('AdMob initializing...');
mobileAds().initialize().then(() => {
  console.log('AdMob initialized successfully');
});

# Debug ad loading
<BannerAd
  unitId={adUnitId}
  size={BannerAdSize.BANNER}
  onAdLoaded={() => console.log('Ad loaded')}
  onAdFailedToLoad={(error) => console.log('Ad failed to load:', error)}
/>
```

### ✅ Testing Checklist
- [ ] **Test ads show**: Test ads appear in development
- [ ] **Different ad sizes**: Test multiple banner sizes
- [ ] **Network connectivity**: Test with different network conditions
- [ ] **App backgrounding**: Test ad behavior when app goes to background

## 🌐 Network and Display Issues

### ✅ Network Configuration
- [ ] **Internet connection**: Device has active internet connection
- [ ] **Firewall/VPN**: No blocking of ad network requests
- [ ] **Geographic restrictions**: Account and app available in test region
- [ ] **Ad inventory**: Ads available for the target demographic

### ✅ Display Issues
- [ ] **Layout constraints**: Banner has proper layout constraints
- [ ] **Container size**: Parent container has sufficient space
- [ ] **Z-index issues**: Banner not hidden behind other elements
- [ ] **Visibility**: Banner component is actually visible in view hierarchy

## 📱 Device-Specific Issues

### ✅ iOS Version Compatibility
- [ ] **Minimum iOS version**: Target iOS 12.4 or higher
- [ ] **Simulator limitations**: Some features only work on physical devices
- [ ] **App Tracking Transparency**: Properly handled on iOS 14+
- [ ] **Device orientation**: Test in both portrait and landscape

### ✅ Physical Device Testing
- [ ] **Development profile**: Device has development profile installed
- [ ] **Trusted developer**: Developer certificate trusted on device
- [ ] **Debug connection**: Device properly connected for debugging
- [ ] **Real device testing**: Test on actual iOS device, not just simulator

## 🔧 Advanced Troubleshooting

### ✅ If Ads Still Not Showing
- [ ] **Check AdMob dashboard**: Verify app status and ad unit status
- [ ] **Review policy violations**: Check for any policy violations in AdMob
- [ ] **Test with different ad units**: Try creating new ad units
- [ ] **Contact AdMob support**: If all else fails, contact Google AdMob support

### ✅ Performance Considerations
- [ ] **Memory usage**: Monitor app memory usage with ads
- [ ] **Refresh rates**: Implement appropriate ad refresh intervals
- [ ] **Loading indicators**: Show loading states to users
- [ ] **Error fallbacks**: Implement fallback UI for failed ad loads

## 📞 Support Resources

- **Google Mobile Ads SDK Documentation**: https://developers.google.com/admob/ios/quick-start
- **React Native Google Mobile Ads**: https://docs.page/invertase/react-native-google-mobile-ads
- **AdMob Policy Center**: https://support.google.com/admob/answer/6128877
- **AdMob Community Forum**: https://groups.google.com/g/google-admob-ads-sdk

---

## 💡 Quick Win Checklist

If you're short on time, start with these most common issues:

1. [ ] Verify test ads work with `TestIds.BANNER`
2. [ ] Check App ID is correctly configured in app.json
3. [ ] Ensure `mobileAds().initialize()` is called before loading ads
4. [ ] Verify internet connectivity and no VPN blocking
5. [ ] Test on a physical iOS device, not just simulator
6. [ ] Check Xcode console for native error messages

---

*This checklist is based on common React Native iOS banner display issues as of 2025. Always refer to the latest Google Mobile Ads SDK documentation for the most up-to-date information.*