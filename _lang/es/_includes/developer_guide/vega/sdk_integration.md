## 

 

## 

###  







```bash
npm install @braze/vega-sdk --save
```



```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```





```bash
yarn add @braze/vega-sdk
```



```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```



###  







```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```


 


## 

### 

 

#### 



```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```





#### 



```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### 



```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 



```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## 



```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 



1. 
2. 
3. 
4. 
5. 


