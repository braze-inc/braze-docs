---
nav_title: Apptimize Partnerschaft
page_order: 0

page_type: update
description: "Dieser archivierte Artikel behandelt die Partnerschaft zwischen Apptimize und Braze. Braze hat die Unterstützung für die Apptimize-Partnerschaft im September 2019 eingestellt."
---

# Apptimize

{% alert update %}
Braze hat die Unterstützung für die Apptimize-Partnerschaft im September 2019 eingestellt.

<br>

Wenn Sie derzeit Apptimize mit Braze verwenden, werden Sie keine Unterbrechung des Dienstes erleben. Sie können weiterhin benutzerdefinierte Apptimize-Attribute für Braze Benutzerprofile festlegen. Es wird jedoch keine formale Eskalationsunterstützung mit dem Partner angeboten.

<br>

Wenden Sie sich an Ihren Braze- oder Apptimize-Vertreter, wenn Sie weitere Fragen haben.
{% endalert %}


[Apptimize](https://apptimize.com/) ist eine Plattform zum Testen und Wachsen von mobilen Anwendungen
die es Kunden ermöglicht, während des gesamten Entwicklungsprozesses einer App schnell zu iterieren.

Apptimize kann in Verbindung mit Braze verwendet werden, um Ihr Wachstum zu ergänzen
Marketing-/CRM-Strategien mit Produkt-UI-Tests durch Synchronisierung von Experimenten und
Daten über beide Plattformen hinweg.

## Anwendungsfälle

Mit Braze und Apptimize zusammen können Sie beide Plattformen zusammen nutzen
um leistungsstarke End-to-End-Erlebnisse zu schaffen:

* Synchronisieren Sie die In-App- und CRM-Marketing-Erlebnisse für eine individuelle Werbeaktion.
* Testen Sie ein neues Onboarding-Erlebnis in Apptimize und verwenden Sie Braze, um die Benutzer während des neuen Ablaufs zu pflegen.
* Testen Sie gleichzeitig die Konfigurationen der Produktfunktionen und die dazugehörige Benutzeransprache.
* Schneiden Sie die In-App-Erlebnisse und die dazugehörigen Nachrichten für verschiedene Nutzergruppen zu.

## Wie es funktioniert

Braze und Apptimize können zusammen integriert werden, um Daten von SDK zu SDK zu übertragen.
Sie können aktive A/B-Testgruppen von Apptimize mit Braze synchronisieren, so dass Sie
die Benutzer in einem bestimmten Apptimize-Test innerhalb von Braze per Push, E-Mail erneut ansprechen,
oder In-App-Nachrichten.

Wir haben einen Beispiel-Integrationscode, der zeigt, wie Braze und Apptimize
SDKs können Daten weitergeben, um benutzerdefiniertes Targeting und Segmentierung in Braze zu ermöglichen, basierend auf
Apptimize Experiment Daten.

Mit dieser Beispielintegration werden benutzerdefinierte Attribute für die Braze User Ihrer Benutzer festgelegt.
Profile für die folgenden Apptimize Daten:

* Die vollständige Liste der aktiven Experimente, für die der Benutzer derzeit eingeschrieben ist.
* Die vollständige Liste der Experimente, an denen der Benutzer jemals teilgenommen hat, einschließlich abgeschlossener Experimente.
* Die Variante(n), die der Benutzer im Rahmen der Teilnahme an einem Experiment gesehen hat.

> Feature Flags werden als Experimente betrachtet, bei denen die einzige Variante darin besteht, ob das Feature Flag eingeschaltet ist. Wenn das Feature-Flag deaktiviert ist, werden keine Daten gemeldet.

Darüber hinaus protokolliert diese Integration ein benutzerdefiniertes Ereignis von Braze für das erste
Teilnahmeveranstaltung eines Experiments. Es gibt zwei Möglichkeiten, dies zu tun:

* Es wird ein benutzerdefiniertes Ereignis mit Eigenschaftsdaten erzeugt, die den Experimentnamen, die Experiment-ID, den Variantennamen und die Varianten-ID enthalten. Anschließend können Sie die Nutzer über die aktionsbasierten Auslieferungskampagnen und Canvases von Braze in Echtzeit erneut ansprechen. Verwenden Sie diese Eigenschaften, um das genaue Apptimize Experiment zu identifizieren, das Sie auslösen möchten.
* Es wird ein Attribut-Array mit Einträgen für jede stattgefundene Teilnahme erstellt. Jede Teilnahme ist formatiert als `experiment_id_EXPERIMENT_ID:variant_id_VARIANT_ID:experiment_name_EXPERIMENT_NAME:variant_name_VARIANT_NAME`

Sie können dann die aktionsbasierten Versandkampagnen von Braze oder Canvases verwenden, um
Folgemeldungen an Benutzer in Echtzeit, wenn diese Ereignisse ausgelöst werden.

## Integration

### iOS
Für die Integration in Ihre App importieren Sie die folgenden `Appboy-Apptimize.m` und
`Apptimize-Appboy.h` Dateien in Ihr Xcode-Projekt, importieren Sie die `Appboy-Apptimize.h`
Header in Ihre AppDelegate-Implementierung ein und fügen Sie folgendes zu
`didFinishLaunchingWithOptions` nachdem Sie sowohl Appboy als auch Apptimize initialisiert haben:

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

importieren Sie die Klasse `apptimizeappboy.java` in Ihre App und in Ihre Haupt `activity`
Implementierung, erstellen Sie ein privates Mitglied `appboyApptimizeIntegration`:

```java
private ApptimizeAppboy appboyApptimizeIntegration;
```

Dann, in Ihrer onCreate-Methode, nach der Initialisierung von Braze und Apptimize:

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
