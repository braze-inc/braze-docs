---
nav_title: Apptimize のパートナーシップ
page_order: 0

page_type: update
description: "このアーカイブされた記事は、ApptimizeとBrazeの提携を網羅しています。2019年9月より、Braze は Apptimize のパートナーシップに関するサポートを廃止しています。"
---

# Apptimize

{% alert update %}
2019年9月より、Braze は Apptimize のパートナーシップに関するサポートを廃止しています。

<br>

現在、Braze で Apptimize を使用している場合、サービスは中断されません。Apptimize のカスタム属性を Braze のユーザープロファイルに設定することもできます。ただし、パートナーとの正式なエスカレーションサポートは提供されません。

<br>

ご質問がある場合は、BrazeまたはApptimizeの担当者に問い合わせること。
{% endalert %}


[Apptimize](https://apptimize.com/) は、モバイルアプリのテストおよび拡張プラットフォームです。
このアプリを使用することで、アプリ開発プロセス全体を通じて反復処理を迅速に進めることができます。

Apptimize は、Braze と組み合わせて使用できます。
それにより、成長マーケティングと CRM の戦略を製品 UI テストで補完できます。
そのために、2つのプラットフォーム間で実験とデータを同期させます。

## ユースケース

BrazeとApptimizeを一緒に使えば、両方のプラットフォームを使ってパワフルなエンドツーエンドの体験を作ることができる：

* カスタムプロモーション用のアプリ内およびCRM マーケティングのエクスペリエンスを同期します。
* Apptimize で新しいオンボーディングエクスペリエンスをテストし、Braze を使用して新しいフロー全体でユーザーを育成します。
* 製品機能の構成と適切なユーザーメッセージングを同時にテストします。
* ユーザーのさまざまなセグメントに合わせて、アプリ内エクスペリエンスと適切なメッセージングをカスタマイズします。

## その仕組み

Braze と Apptimize を統合して、SDK 間でデータを受け渡すことができます。
有効なApptimize A/BテストグループをBrazeに同期し、次の操作を実行できます
プッシュ、メール、またはアプリ内メッセージングを使用して、Braze 内の特定の Apptimize
テストでユーザーをリターゲティングします。

BrazeとApptimizeの方法を示す標本積分コードがあります
Apptimize の実験データに基づいて Braze でカスタムターゲティングとセグメンテーションを強化するために、SDK
はデータを渡すことができます。

このサンプルインテグレーションでは、ユーザーのBraze ユーザーにカスタム属性s を設定します
次のApptimize データのプロファイル:

* ユーザーが現在登録されているすべてのアクティブな実験の一覧。
* 完成した実験を含め、ユーザーがこれまでに登録したすべての実験の一覧。
* ユーザーが実験に参加しているとみなされたバリアント。

> 特徴フラグは、唯一のバリアントが特徴フラグが有効かどうかである実験と考えられる。フィーチャーフラグがオフの場合は、データがレポートされません。

さらに、このインテグレーションでは、最初のBraze カスタムイベントが記録されます
(実験の参加イベント)。これは、次の 2 つの方法のいずれかで実行できます。

* 実験名、実験 ID、バリアント名、バリアント ID を示すプロパティデータを使用してカスタムイベントが生成されます。その後、Braze のアクションベースの配信キャンペーンとキャンバスを使用し、リアルタイムトリガーを介してユーザーをリターゲティングできます。これらのプロパティを使用して、トリガーする Apptimize の実験を正確に識別します。
* 属性配列は、発生したすべての参加のエントリとともに生成されます。それぞれの参加の書式は `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME` になります。

その後、Brazeのアクションベースの配信キャンペーンまたはキャンバスを使用して送信できます
(これらのイベントがトリガーされたときに、後続メッセージをユーザーにリアルタイムで送信)。

## 統合

### iOS
アプリと統合するには、次の `Appboy-Apptimize.m` および
`Apptimize-Appboy.h` ファイルを Xcode プロジェクトにインポートして、`Appboy-Apptimize.h`
ヘッダーを AppDelegate 実装にインポートし、Appboy と Apptimize の両方を初期化した後に以下を
`didFinishLaunchingWithOptions` に追加します。

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

`apptimizeappboy.java` クラスをアプリにインポートして、メインの `activity`
実装で非公開メンバー `appboyApptimizeIntegration` を作成します。

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

次に、onCreate メソッドで、Braze とApptimize を初期化した後、次のようにします。

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
