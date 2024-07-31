---
nav_title: アプティマイズパートナーシップ
page_order: 0

page_type: update
description: "この記事は、ApptimizeとBrazeの提携について説明しています。Brazeは2019年9月をもってApptimizeパートナーシップのサポートを廃止しました。"
---

# アプティマイズ

{% alert update %}
Brazeは2019年9月をもってApptimizeパートナーシップのサポートを廃止しました。

<br>

現在、ApptimizeをBrazeと一緒に使用している場合、サービスの中断は発生しません。まだApptimizeカスタム属性をBrazeユーザープロファイルに設定できます。しかし、パートナーとの正式なエスカレーションサポートは提供されません。

<br>

ご不明点がございましたら、BrazeまたはApptimizeの担当者にお問い合わせください。
{% endalert %}


[Apptimize](https://apptimize.com/)はモバイルアプリのテストおよび成長プラットフォームです
顧客がアプリ開発プロセス全体で迅速にIterateできるようにします。

ApptimizeはBrazeと連携して、成長を補完するために使用できます
マーケティング / CRM 戦略と製品UIテストを実験と同期させることによって
両方のプラットフォームにまたがるデータ。

## ユースケース

BrazeとApptimizeを一緒に使用することで、両方のプラットフォームを連携して活用できます。
強力なエンドツーエンドの体験を作成するために:

* カスタムプロモーションのために、アプリ内およびCRMマーケティング体験を同期させます。
* Apptimizeで新しいオンボーディング体験をテストし、新しいフロー全体でユーザーを育成するためにBrazeを使用します。
* 適切なユーザーメッセージングと並行して製品機能の構成をテストします。
* さまざまなユーザーセグメントに合わせて、アプリ内の体験とそれに適したメッセージングを調整します。

## その仕組み

BrazeとApptimizeは統合して、SDKからSDKにデータを渡すことができます。
ApptimizeのアクティブなA/BテストグループをBrazeに同期させることができます。
リターゲティングする the users in a particular Apptimize test within Braze via push, メール,
またはインアプリメッセージング。

サンプルの統合コードがあり、BrazeとApptimizeの使い方を示しています。
SDKは、Brazeに基づいてカスタムターゲティングとセグメンテーションを強化するためのデータを渡すことができます。
アプティマイズ実験データ。

このサンプル統合は、ユーザーのBrazeユーザーにカスタム属性を設定します
次のApptimizeデータのプロファイル：

* ユーザーが現在登録されているアクティブな実験の完全なリスト。
* ユーザーがこれまでに参加したすべての実験の完全なリスト（完了した実験を含む）。
* ユーザーが実験参加の一環として見たバリアント。

> フィーチャーフラグは、唯一のバリアントがフィーチャーフラグがオンかどうかである実験と見なされます。フィーチャーフラグがオフの場合、データは報告されません。

さらに、この統合は最初のBrazeカスタムイベントを記録します
実験の参加イベント。これは、次の 2 つの方法のいずれかで実行できます。

* カスタムイベントは、プロパティデータを使用して生成され、実験名、実験ID、バリアント名、およびバリアントIDを示します。次に、Brazeのアクションベースの配信キャンペーンとCanvasを使用して、リアルタイムトリガーを介してユーザーをリターゲティングすることができます。これらのプロパティを使用して、トリガーしたい正確なApptimize実験を特定します。
* 属性配列は、発生したすべての参加のエントリで生成されます。各参加は`experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`としてフォーマットされています

次に、Brazeのアクションベースの配信キャンペーンやCanvasを使用して送信できます
これらのイベントがトリガーされたときに、リアルタイムでユーザーにフォローオンメッセージを送信します。

## 統合

### iOS
アプリと統合するために、次の`Appboy-Apptimize.m`をインポートし
`Apptimize-Appboy.h` ファイルをXcodeプロジェクトにインポートし、`Appboy-Apptimize.h` をインポートします
ヘッダー into your AppDelegate implementation and add the following to
`didFinishLaunchingWithOptions` AppboyとApptimizeの両方を初期化した後:

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

インポート `apptimizeappboy.java` クラスをアプリにして、メイン `activity` に
実装、プライベートメンバー`appboyApptimizeIntegration`を作成します:

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

次に、onCreateメソッドで、BrazeとApptimizeを初期化した後: 

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
