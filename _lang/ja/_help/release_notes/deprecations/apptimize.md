---
nav_title: パートナーシップを最適化
page_order: 0

page_type: update
description: "このアーカイブ記事では、ApptimizeとBrazeのパートナーシップについて説明しています。Braze は、2019 年 9 月をもって Apptimize パートナーシップのサポートを終了しました。"
---

# 最適化する

{% alert update %}
Braze は、2019 年 9 月をもって Apptimize パートナーシップのサポートを終了しました。

<br>

現在 Apptimize を Braze と一緒に使用している場合、サービスの中断は発生しません。Apptimize カスタム属性を Braze ユーザープロファイルに設定することは引き続き可能です。ただし、パートナーとの正式なエスカレーションサポートは提供されません。

<br>

ご不明な点がございましたら、Braze または Apptimize の担当者にお問い合わせください。
{% endalert %}


[Apptimizeは](https://apptimize.com/)、モバイルアプリのテストおよび成長プラットフォームです
これにより、顧客はアプリ開発プロセス全体を迅速に反復できます。

AptimizeはBrazeと組み合わせて使用することで、あなたの成長を補完することができます
マーケティング/CRM戦略と実験の同期による製品UIテストと
両方のプラットフォームにわたるデータ。

## ユースケース

Braze と Apptimize を併用すると、両方のプラットフォームを組み合わせて活用できます。
パワフルなエンドツーエンドのエクスペリエンスを実現するには:

* アプリ内マーケティングエクスペリエンスとCRMマーケティングエクスペリエンスを同期して、カスタムプロモーションを行います。
* Apptimize で新しいオンボーディング体験をテストし、Braze を使って新しいフロー全体でユーザーを育成しましょう。
* 適切なユーザーメッセージとともに、製品の機能構成を同時にテストします。
* さまざまなユーザーセグメントに合わせて、アプリ内エクスペリエンスと適切なメッセージをカスタマイズします。

## 仕組み

Braze と Apptimize を統合して、SDK から SDK にデータを渡すことができます。
アクティブな Apptimize A/B テストグループを Braze に同期することで、次のことが可能になります。
Braze内の特定のApptimizeテストでユーザーをプッシュ、メールなどでリターゲティングします。
またはアプリ内メッセージング。

BrazeとApptimizeがどのように機能するかを示すサンプル統合コードがあります
SDK は、以下に基づいてデータを渡して Braze のカスタムターゲティングとセグメンテーションを強化できます。
実験データを最適化します。

このサンプルインテグレーションでは、ユーザーの Braze User にカスタム属性を設定します
以下の Aptimize データのプロファイル:

* ユーザーが現在登録しているアクティブなテストの全リスト。
* ユーザーがこれまでに登録したテストの全リスト (完了したテストを含む)。
* ユーザーが実験参加の一環として見たバリアント。

> 機能フラグは、機能フラグがオンになっているかどうかが唯一のバリエーションである実験とみなされます。機能フラグがオフの場合、データは報告されません。

さらに、この統合により、Braze カスタムイベントが初めてログに記録されます
実験の参加イベント。これは次の 2 つの方法のいずれかで実行できます。

* カスタムイベントは、テスト名、テスト ID、バリアント名、バリアント ID を示すプロパティデータを使用して生成されます。その後、Brazeのアクションベースの配信キャンペーンとCanvasesを使用してリアルタイムトリガーでユーザーをリターゲティングできます。これらのプロパティを使用して、トリガーしたいAptimize Experimentを正確に特定してください。
* 発生したすべての参加のエントリを含む属性配列が生成されます。各参加は次のようにフォーマットされます `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`

その後、Brazeのアクションベースの配信キャンペーンまたはCanvasesを使用して送信できます
これらのイベントがトリガーされると、ユーザーにリアルタイムでフォローオンメッセージが送信されます。

## インテグレーション

### iOS
アプリと統合するには、`Appboy-Apptimize.m`以下をインポートして
`Apptimize-Appboy.h` Xcode プロジェクトにファイルをインポートし、 `Appboy-Apptimize.h`
AppDelegate の実装にヘッダーを追加し、以下を追加します
`didFinishLaunchingWithOptions` アプリボーイとアプリティマイズの両方を初期化した後:

```objc
[ApptimizeAppboy setupExperimentTracking];
```

#### appboy-apptimize.h:

\`\`\`オブジェクト
//アプリティマイズ-AppBoy.h

\#ifndef Apptimize\_Appboy\_h
\#define Apptimize\_Appboy\_h

@interface apptimizeAppBoy:NSObject
\+ (void) セットアップ実験トラッキング;
@end

\#endif /* Apptimize_Appboy_h */
\`\`

#### AppBoy-apptimize.m:

\`\`\`オブジェクト
//アプリティマイズ-アプリボーイ.m

\#import <Foundation/Foundation.h>

\#import "Apptimize-Appboy.h"

\#import <Apptimize/Apptimize.h>
#import <Apptimize/Apptimize+Variables.h>

\#import "Appboy.h"
\#import "ABKUser.h"

//以前の登録辞書を保存して、登録が変更されたかどうかを確認するためのキー
nsString \*const appTimizeAppBoy TestEnrollmentStorageKey = @「AppTimizeAppBoy TestEnrollmentStorageKey」;

@implementation apptimizeAppBoy

+ (void) 実験追跡のセットアップ
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

+ (無効) AppTimize テストが処理されました:(NS 通知\*) 通知
{
    NSLog (@ "Appboy-Apptimize インテグレーション処理中の新しいオプティマイズテスト」);
    [新しいテストのセルフアップデート];
}

+ (無効) 新しいテストの更新
{
    nsDictionary * SavedEnrollmentDictionary = [[NS ユーザーデフォルト標準ユーザーデフォルト] オブジェクトフォーキー:apptimizeAppBoy TestEnrollmentStorageKey];
    NS Dictionary * 現在の登録辞書 = [TestInfo から登録辞書を自分で取得];

    BOOL 登録が変更されました = いいえ;

    for (現在の登録辞書の ID キー) {
if (![savedEnrollmentDictionary[key] isEqualToString:currentEnrollmentDictionary[key]]) {
enrollmentChanged = YES;
NSString *testAttributeKey = [@"apptimize_test_" stringByAppendingString:key];
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:testAttributeKeyvalue :currentEnrollmentDictionary[key]];
}
        }

    if (現在の登録辞書。カウント!= 登録辞書を保存しました。カウント) {
        登録変更 = はい;
    }

    if (登録が変更されました) {
        [[Appboy SharedInstance] .user setCustomAttributeArray (キー付き): @ "active\_apptimize\_tests」配列:現在の登録ディクショナリ。すべてのキー];

        for (id key in currentEnrollmentDictionary.allKeys) {
            [[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"all_apptimize_tests" value:key];
        }

        [[NSUserDefaults standardUserDefaults] setObject:currentEnrollmentDictionary forKey:ApptimizeAppboyTestEnrollmentStorageKey];
        [[NSUserDefaults standardUserDefaults] synchronize];
    }
}

//テスト ID をキーにしたバリアント ID を持つディクショナリ。両方とも NSString
\+ (NSミュータブル辞書\*) テスト情報から登録辞書を取得
{
    NSミュータブルディクショナリ\*登録ディクショナリ= [NSミュータブルディクショナリディクショナリ];

    for(id key in [Apptimize testInfo]) {
        NSLog(@"key=%@ value=%@", key, [[Apptimize testInfo] objectForKey:key]);
        NSDictionary<ApptimizeTestInfo> *testInfo = [[Apptimize testInfo] objectForKey:key];
        enrollmentDictionary[[testInfo.testID stringValue]] = [testInfo.enrolledVariantID stringValue];
    }

    return enrollmentDictionary;
}

+ (無効) 実験ディジェットが表示されました:(NS 通知\*) 通知
{
    もし (![notification.userinfo [AppTimizeTestFirstRunUserInfoKey] BoolValue]) {
        返品;
    }

    //Apptimize は ID で通知しないので、すべての実験を繰り返して一致するものを見つけます。
    nsString \*name = notification.userInfo [apptimizeTestNameUserInfoKey];
    NSString \*variant = notification.userInfo [apptimizeVariantNameUserInfoKey];

    [テスト情報を最適化する] ブロックを使用してキーとオブジェクトを列挙する:^ (id キー、id 実験、BOOL \*停止) <ApptimizeTestInfo> {
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
\`\`

### Android

`apptimizeappboy.java`クラスをアプリとメインにインポートする `activity`
実装、プライベートメンバーの作成`appboyApptimizeIntegration`:

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

次に、onCreateメソッドで、BrazeとApptimizeを初期化した後、次のことを行います。

```java
appboyApptimizeIntegration = new ApptimizeAppboy();
appboyApptimizeIntegration.configureExperimentTracking(this);
```    

#### ApptimizeAppboy.java:

\`\`\`ジャワ
パッケージ com.apptimize.appboykit;

java.io ファイルをインポートします。
java.io.File入力ストリームをインポートします。
java.io.file 出力ストリームをインポートします。
java.io.ObjectInputStream をインポートします。
java.io.object 出力ストリームをインポートします。
java.util.Map をインポート;
java.util.HashMap をインポート;
android.util.log をインポート;

android.content.Context をインポート;

com.apptimize.appTimize; をインポート;
import com.apptimize.apptimizeTestInfo;
import com.apptimize.apptimize.onExperimentsProcsedListener;
com.apptimize.apptimize.onExperimentRunListener; をインポート;

com.appboy.AppBoy; をインポート;
com.appboy.AppBoyUser; をインポート;
com.appboy.models.outgoing.AppBoyProperties; をインポートする;

パブリッククラスアプリイマイズアプリボーイ
        AppTimize.onExperimize.onExperimentRunListener を実装しています。
                    apptimize.onExperimentsProcsedListener {

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
\`\`
