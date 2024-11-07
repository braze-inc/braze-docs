---
nav_title: Apptimize 파트너십
page_order: 0

page_type: update
description: "이 아카이브 문서에서는 Apptimize와 Braze의 파트너십에 대해 설명합니다. Braze는 2019년 9월부터 Apptimize 파트너십에 대한 지원을 중단했습니다."
---

# Apptimize

{% alert update %}
Braze는 2019년 9월부터 Apptimize 파트너십에 대한 지원을 중단했습니다.

<br>

현재 Braze와 함께 Apptimize를 사용 중인 경우 서비스 중단은 발생하지 않습니다. 여전히 Apptimize 커스텀 속성을 Braze 고객 프로필에 설정할 수 있습니다. 그러나 파트너와의 공식적인 에스컬레이션 지원은 제공되지 않습니다.

<br>

추가 질문이 있는 경우 Braze 또는 Apptimize 담당자에게 문의하세요.
{% endalert %}


[Apptimize](https://apptimize.com/)는 모바일 앱 테스트 및 성장 플랫폼이며
이를 이용하면 고객이 앱 개발 프로세스 전반을 빠르게 반복할 수 있습니다.

Apptimize와 Braze를 함께 사용하여 성장
마케팅/CRM 전략으 실험을 두 플랫폼 전반에 걸쳐 실험과 데이터를 동기화하여 제품 UI 테스트를
보완할 수 있습니다.

## 사용 사례

Braze와 Apptimize를 함께 사용하면 두 플랫폼을 함께 활용하여
강력한 엔드투엔드 경험을 만들 수 있습니다.

* 맞춤형 프로모션을 위해 인앱 및 CRM 마케팅 경험을 동기화하세요.
* Apptimize에서 새로운 온보딩 경험을 테스트하고, Braze를 사용하여 새로운 흐름 전반에 걸쳐 사용자를 육성하세요.
* 적절한 사용자 메시지와 함께 제품 기능 구성을 동시에 테스트할 수 있습니다.
* 다양한 사용자 세그먼트에 맞게 인앱 경험과 적절한 메시지를 맞춤 설정할 수 있습니다.

## 작동 원리

Braze와 Apptimize를 함께 통합하여 SDK에서 SDK로 데이터를 전달할 수 있습니다.
활성 Apptimize A/B 테스트 그룹을 다시 Braze에 동기화하여
푸시, 이메일 또는 인앱 메시징을 통해 Braze 내 특정 Apptimize 테스트의 사용자를
리타겟팅할 수 있습니다.

Apptimize 실험 데이터를 바탕으로 Braze와 Apptimize SDK가
어떻게 데이터를 전달하여 커스텀 타겟팅 및 세분화를 지원하는지 보여주는 샘플 통합 코드가 준비되어 있습니다.
실험 데이터를 최적화합니다.

이 샘플 통합은 사용자의 Braze 사용자에 대한 사용자 지정 속성을 설정합니다.
다음 Apptimize 데이터에 대한 프로필:

* 사용자가 현재 등록되어 있는 활성 실험의 전체 목록입니다.
* 완료된 실험을 포함하여 사용자가 등록한 모든 실험의 전체 목록입니다.
* 사용자가 실험 참여의 일부로 본 배리언트입니다.

> 피처 플래그는 피처 플래그가 켜져 있는지 여부가 유일한 배리언트인 실험으로 간주됩니다. 기능 플래그가 꺼져 있으면 데이터가 보고되지 않습니다.

또한, 이 통합은 첫 번째 Braze 커스텀 이벤트를 기록합니다.
실험 참여 이벤트입니다. 이 작업은 두 가지 방법 중 하나로 수행할 수 있습니다.

* 실험 이름, 실험 ID, 배리언트 상품 이름 및 배리언트 상품 ID를 나타내는 속성정보 데이터로 커스텀 이벤트가 생성됩니다. 그런 다음 Braze의 실행 기반 전달 캠페인과 캔버스를 사용하여 실시간 트리거링을 통해 사용자를 리타겟팅할 수 있습니다. 이러한 속성을 사용하여 트리거할 정확한 Apptimize 실험을 식별할 수 있습니다.
* 발생한 모든 참여에 대한 항목이 포함된 속성 배열이 생성됩니다. 각 참여의 형식은 다음과 같습니다. `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`

그런 다음 Braze의 실행 기반 전달 캠페인 또는 캔버스를 사용하여
이러한 이벤트가 트리거되었을 때 실시간으로 사용자에게 후속 메시지를 보낼 수 있습니다.

## 통합

### iOS
앱과 통합하려면 다음 `Appboy-Apptimize.m` 및
`Apptimize-Appboy.h` 파일을 Xcode 프로젝트로 가져오고 `Appboy-Apptimize.h` 헤더를
AppDelegate 구현에 추가하고
Appboy와 Apptimize를 모두 초기화한 후 `didFinishLaunchingWithOptions`에 다음을 추가합니다.

```objc
[ApptimizeAppboy setupExperimentTracking];
```

#### Appboy-Apptimize.h:

```objc
//  Apptimize-Appboy.h

#ifndef Apptimize_Appboy_h
#define Apptimize_Appboy_h

@interface ApptimizeAppboy : NSObject
+ (void)setupExperimentTracking;
@end

#endif /* Apptimize_Appboy_h */
```

#### Appboy-Apptimize.m:

```objc
//  Apptimize-Appboy.m

#import <Foundation/Foundation.h>

#import "Apptimize-Appboy.h"

#import <Apptimize/Apptimize.h>
#import <Apptimize/Apptimize+Variables.h>

#import "Appboy.h"
#import "ABKUser.h"

// Key to store previous enrollment dictionary to check against to see if enrollment has changed
NSString *const ApptimizeAppboyTestEnrollmentStorageKey = @"ApptimizeAppboyTestEnrollmentStorageKey";

@implementation ApptimizeAppboy

+ (void)setupExperimentTracking
{
    // Track for enrollment changes
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(apptimizeTestsProcessed:)
                                                    name:ApptimizeTestsProcessedNotification
                                                object:nil];
    // Track for participation events
    [[NSNotificationCenter defaultCenter] addObserver:self
                                                selector:@selector(experimentDidGetViewed:)
                                                    name:ApptimizeTestRunNotification
                                                object:nil];
}

+ (void)apptimizeTestsProcessed:(NSNotification*)notification
{
    NSLog(@"Appboy-Apptimize integration processing new Apptimize tests");
    [self updateForNewTests];
}

+ (void)updateForNewTests
{
    NSDictionary *savedEnrollmentDictionary = [[NSUserDefaults standardUserDefaults] objectForKey:ApptimizeAppboyTestEnrollmentStorageKey];
    NSDictionary *currentEnrollmentDictionary = [self getEnrollmentDictionaryFromTestInfo];

    BOOL enrollmentChanged = NO;

    for (id key in currentEnrollmentDictionary) {
        if (![savedEnrollmentDictionary[key] isEqualToString:currentEnrollmentDictionary[key]]) {
            enrollmentChanged = YES;
            NSString *testAttributeKey = [@"apptimize_test_" stringByAppendingString:key];
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:testAttributeKeyvalue :currentEnrollmentDictionary[key]];
        }
    }

    if (currentEnrollmentDictionary.count != savedEnrollmentDictionary.count) {
        enrollmentChanged = YES;
    }

    if (enrollmentChanged) {
        [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"active_apptimize_tests" array:currentEnrollmentDictionary.allKeys];

        for (id key in currentEnrollmentDictionary.allKeys) {
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"all_apptimize_tests" value:key];
        }

        [[NSUserDefaults standardUserDefaults] setObject:currentEnrollmentDictionary forKey:ApptimizeAppboyTestEnrollmentStorageKey];
        [[NSUserDefaults standardUserDefaults] synchronize];
    }
}

// Dictionary with variant IDs keyed by test ID, both as NSStrings
+ (NSMutableDictionary *)getEnrollmentDictionaryFromTestInfo
{
    NSMutableDictionary *enrollmentDictionary = [NSMutableDictionary dictionary];

    for(id key in [Apptimize testInfo]) {
        NSLog(@"key=%@ value=%@", key, [[Apptimize testInfo] objectForKey:key]);
        NSDictionary<ApptimizeTestInfo> *testInfo = [[Apptimize testInfo] objectForKey:key];
        enrollmentDictionary[[testInfo.testID stringValue]] = [testInfo.enrolledVariantID stringValue];
    }

    return enrollmentDictionary;
}

+ (void)experimentDidGetViewed:(NSNotification*)notification
{
    if (![notification.userInfo[ApptimizeTestFirstRunUserInfoKey] boolValue]) {
        return;
    }

    // Apptimize doesn't notify with IDs, so we iterate over all experiments to find the matching one.
    NSString *name = notification.userInfo[ApptimizeTestNameUserInfoKey];
    NSString *variant = notification.userInfo[ApptimizeVariantNameUserInfoKey];

    [[Apptimize testInfo] enumerateKeysAndObjectsUsingBlock:^(id key, id<ApptimizeTestInfo> experiment, BOOL *stop) {
        BOOL match = [experiment.testName isEqualToString:name] && [experiment.enrolledVariantName isEqualToString:variant];
        if (!match) {
            return;
        }

        // If you want to log a custom event for each participation
        [[Appboy sharedInstance] logCustomEvent:@"apptimize_experiment_viewed"
                                    withProperties: @{@"apptimize_experiment_name" : [experiment testName],
                                                        @"apptimize_variant_name" : [experiment enrolledVariantName],
                                                        @"apptimize_experiment_id" : [experiment testID],
                                                        @"apptimize_variant_id" : [experiment enrolledVariantID]}];

        // If you want a custom attribute array set for each participation
        [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"apptimize_experiments"
                                                                    value:[NSString stringWithFormat:@"experiment_id_%@:variant_id_%@:experiment_name_%@:variant_name_%@",
                                                                            [experiment testID], [experiment enrolledVariantID], [experiment testName], [experiment enrolledVariantName] ]];
        *stop = YES;
    }];
}

@end
```

### Android

`apptimizeappboy.java` 클래스를 앱으로 가져오고 기본 `activity`
구현, `appboyApptimizeIntegration` 개인 구성원을 만듭니다.

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

그런 다음 onCreate 메서드에서 Braze 및 Apptimize를 초기화한 후 사용합니다.

```java
appboyApptimizeIntegration = new ApptimizeAppboy();
appboyApptimizeIntegration.configureExperimentTracking(this);
```    

#### ApptimizeAppboy.java:

```java
package com.apptimize.appboykit;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Map;
import java.util.HashMap;
import android.util.Log;

import android.content.Context;

import com.apptimize.Apptimize;
import com.apptimize.ApptimizeTestInfo;
import com.apptimize.Apptimize.OnExperimentsProcessedListener;
import com.apptimize.Apptimize.OnExperimentRunListener;

import com.appboy.Appboy;
import com.appboy.AppboyUser;
import com.appboy.models.outgoing.AppboyProperties;

public class ApptimizeAppboy
        implements Apptimize.OnExperimentRunListener,
                    Apptimize.OnExperimentsProcessedListener {

    public void configureExperimentTracking(Context context) {
        appboyInstance = Braze.getInstance(context);
        enrollmentStorage = new File(context.getDir("apptimize-appboy", Context.MODE_PRIVATE), ApptimizeAppboyTestEnrollmentStorage);

        Apptimize.setOnExperimentRunListener(this);
        Apptimize.addOnExperimentsProcessedListener(this);
    }

    @Override
    public void onExperimentRun(String experimentName, String variantName, boolean firstRun) {
        if (!firstRun) {
            return;
        }
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();

        if (testInfoMap == null) {
            return;
        }

        String experimentId = "";
        String variantId = "";

        Log.d("Apptimize-Appboy", "In onExperimentRun");

        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            if (testInfo.getTestName().equals(experimentName) &&
                testInfo.getEnrolledVariantName().equals(variantName)) {
                experimentId = String.valueOf(testInfo.getTestId());
                variantId = String.valueOf(testInfo.getEnrolledVariantId());
            }
        }
        Log.d("Apptimize-Appboy", "Logging participation for " + experimentName + ":" + experimentId + " and variant " + variantName + ":" + variantId);

        // If you want to log a custom event for each participation
        logParticipationEventAsEvent(experimentName, variantName, experimentId, variantId);

        // If you want a custom attribute array set for each participation
        logParticipationEventAsAttributes(experimentName, variantName, experimentId, variantId);
    }

    private void logParticipationEventAsEvent(String experimentName, String variantName, String experimentId, String variantId) {
        AppboyProperties eventProperties = new AppboyProperties();

        eventProperties.addProperty("apptimize_experiment_name", experimentName);
        eventProperties.addProperty("apptimize_variant_name", variantName);
        eventProperties.addProperty("apptimize_experiment_id", experimentId);
        eventProperties.addProperty("apptimize_variant_id", variantId);

        appboyInstance.logCustomEvent("apptimize_experiment_viewed", eventProperties);
    }

    private void logParticipationEventAsAttributes(String experimentName, String variantName, String experimentId, String variantId) {
        appboyInstance.getCurrentUser().addToCustomAttributeArray("apptimize_experiments",
                "experiment_id_" + experimentId + ":variant_id_" + variantId + ":experiment_name_" + experimentName + ":variant_name_" + variantName);
    }

    @Override
    public void onExperimentsProcessed() {
        Map<String,String> currentEnrollmentDictionary = getEnrollmentDictionary();
        Map<String,String> savedEnrollmentDictionary = getPreviousEnrollmentDictionary();
        AppboyUser appboyUser = appboyInstance.getCurrentUser();

        boolean enrollmentChanged = false;

        Log.d("Apptimize-Appboy", "Processing experiments");

        for (String key : currentEnrollmentDictionary.keySet()) {
            if (savedEnrollmentDictionary == null ||
                !currentEnrollmentDictionary.get(key).equals(savedEnrollmentDictionary.get(key))) {
                Log.d("Apptimize-Appboy", "Found change in enrollment" + currentEnrollmentDictionary.get(key));
                enrollmentChanged = true;
                String testAttributeKey = "apptimize_test_" + key;
                appboyUser.addToCustomAttributeArray(testAttributeKey, currentEnrollmentDictionary.get(key));
            }
        }

        if (currentEnrollmentDictionary.size() == 0 && savedEnrollmentDictionary.size() != 0) {
            enrollmentChanged = true;
        }

        if (enrollmentChanged) {
            Log.d("Apptimize-Appboy", "Enrollment changed");
            appboyUser.setCustomAttributeArray("active_apptimize_tests", currentEnrollmentDictionary.keySet().toArray(new String[0]));

            for (String key : currentEnrollmentDictionary.keySet()) {
                appboyUser.addToCustomAttributeArray("all_apptimize_tests", key);
            }

            storePreviousEnrollmentDictionary(currentEnrollmentDictionary);
        }
    }

    private Map<String,String> getEnrollmentDictionary()
    {
        Map<String,String> enrollment = new HashMap<String,String>();
        Map<String,ApptimizeTestInfo> testInfoMap = Apptimize.getTestInfo();
        for (ApptimizeTestInfo testInfo : testInfoMap.values()) {
            Log.d("Apptimize-Appboy", "TestID: " + String.valueOf(testInfo.getTestId()) + " VariantID: " + String.valueOf(testInfo.getEnrolledVariantId()));
            enrollment.put(String.valueOf(testInfo.getTestId()), String.valueOf(testInfo.getEnrolledVariantId()));
        }
        return enrollment;
    }

    private Map<String,String> getPreviousEnrollmentDictionary()
    {
        ObjectInputStream enrollmentStream;
        try {
            enrollmentStream = new ObjectInputStream(new FileInputStream(enrollmentStorage));
        } catch(Exception e) {
            Log.d("Apptimize-Appboy", "Unable to open file");
            return null;
        }

        Map<String, String> previousEnrollment;
        try {
                previousEnrollment = (Map<String,String>)enrollmentStream.readObject();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to get previous enrollment");
            return null;
        }

        return previousEnrollment;
    }

    private void storePreviousEnrollmentDictionary(Map<String,String> enrollmentDictionary)
    {
        try {
            ObjectOutputStream enrollmentStream = new ObjectOutputStream(new FileOutputStream(enrollmentStorage));
            enrollmentStream.writeObject(enrollmentDictionary);
            enrollmentStream.flush();
            enrollmentStream.close();
        } catch (Exception e) {
            Log.d("Apptimize-Appboy", "Unable to save enrollment information");
        }

    }

    private Appboy appboyInstance;
    private File enrollmentStorage;

    private static String ApptimizeAppboyStorageDirectory;
    private static String ApptimizeAppboyTestEnrollmentStorage = "ApptimizeAppboyTestEnrollmentStorage";
}
```
