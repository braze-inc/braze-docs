---
permalink: /support_contact/
nav_title: Hilfe | Braze
hide_nav: true
layout: basic
hide_toc: true
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/docsearch.js/2/docsearch.min.css" />

<style type="text/css">

#main-container {
  margin-top: 20px;
  margin-bottom: 50px;
  min-height: 800px;
}
#main-container label {
  font-weight: bold;
  font-size: 18px;
}

.container {
  margin-top: 40px;
}

.popover{
  max-width: 65%;
  min-width: 350px;
  top: -15px !important;
}
@media (max-width:600px)  {
  .popover{
    max-width: 95%;
  }
}
.container-fluid {
  max-width: 1280px;
}

.header {
  margin-top: 20px;
  margin-bottom: 20px;
}

.header .navbar-brand img {
    max-width: none;
    width: 112px;
    height: 51px;
}

#ticket_resources {
  border-left: solid 1px #c9c9c9;
  padding-left: 40px;
  min-height: 340px;
}
@media (max-width:600px)  {
  #ticket_resources {
    padding-left: 15px;
    border: none;
  }
}

.algolia-autocomplete-listbox-2 {
    display: inline !important;
}

#algolia-autocomplete-listbox-2 {
  position: relative !important;
}

.algolia-autocomplete {
  line-height: normal;
  display: inline !important;
}
#search-input {
    padding: 0 0 20px;
    position: relative;
}

#search-input input[type="text"] {
    padding: .5em 0 .5em 0;
    outline: 0;
    border: 0;
    border-bottom: solid 2px #c9c9c9;
    width: 100%;
    font-size: 15px;
    display: inline-block;
    background-image:url(/docs/assets/img/search_black_shark.svg);
    background-position: right 10px top 9px;
    background-size: 14px 14px;
    background-repeat: no-repeat;
}

#search-input .fa-search {
  line-height: normal;
  position: relative;
  top: 15px;
  left: 5px;
}

.aa-suggestion {
  margin-top: 5px;
  line-height: 25px;
}

#ticket_search div.aa-suggestion {
  color: #6d6d70;
  cursor: pointer;
  display: inline;
  border-bottom-width: 0px;
}

#ticket_search aa-suggestions:hover div {
  text-decoration: none;
  color: #6d6d70;
  border-bottom-width: 2px;
  border-color: #3accdd;
}


#ticket_search aa-suggestion--highlight{

}

#ticket_search .algolia-docsearch-footer {
  padding-top: 5px;
}

.gradient-line {
  background: linear-gradient(90deg, rgba(201,196,255,1) 30%, rgba(128,30,215,1) 60%, rgba(255,165,36,1) 90%);
  height: 3px;
  width: 108px;
}

a {
  font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  display: inline;
  color: rgb(128, 30, 215);
  font-weight: normal;
  @media print {
    font-weight: normal;
  }
  transition: all ease 0.2s;
  -webkit-transition: all ease 0.2s;
  -moz-transition: all ease 0.2s;
  border-color: rgb(128, 30, 215);
  border-bottom-width: 2px;
  border-bottom-style: solid;
  line-height: 2.5;
}

a:hover {
  background-color: rgb(128, 30, 215);
  text-decoration: none;

}

#ticket_mainform {
  margin-top: 20px;
}
#ticket_leftmain {
  padding-right: 40px;

}
#ticket_reference {
  line-height: normal;
}

#ticket_footer {
  margin-left: auto;
  margin-right: auto;
  border-top: 1px solid #dfdfe3;
  text-align: center;
  font-size: 12px;
  padding-top: 10px;
  color: #6e6e70;
}

#ticket_footer a {
  text-decoration: none;
  color: #6e6e70;
}
#ticket_footer li {
  display: inline;
  margin: 8px;

}
.h1, h1  {
  font-size: 44px;
}

.h2, h2 {
  font-size: 20px;
}


#ticket_submit_option {
  margin-top: 20px;
}

#ticket_form button[type=submit] {
  display: inline-block;
  vertical-align: middle;
  font: inherit;
  text-align: center;
  margin: 0;
  cursor: pointer;
  font-size: 14px;
  font-size: 1rem;
  line-height: 1.4;
  font-family: "Aribau Grotesk Regular", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  text-transform: uppercase;
  padding: 1.14286rem 2.85714rem;
  border-radius: 0;
  letter-spacing: .10714rem;
  white-space: normal;
  border: 2px solid #212123;
  color: #212123;
  background-color: transparent;
  position: relative;
  z-index: 1;
  overflow: hidden;
  transition: color .3s cubic-bezier(.5, 0, .1, 1), border-color .3s cubic-bezier(.5, 0, .1, 1);
  will-change: color, border-color
}

@media (min-width:36em) {
  #ticket_form button[type=submit] {
    padding: 1.64286rem 3.92857rem
  }
}

#ticket_form button[type=submit]:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  height: 100%;
  background-color: #212123;
  transform-origin: top right;
  width: 100%;
  transform: translate3d(-101%, 0, 0);
  transition: transform .3s cubic-bezier(.5, 0, .1, 1);
  will-change: transform
}

#ticket_form button[type=submit]:focus, #ticket_form button[type=submit]:hover {
  color: #fff
}

#ticket_form button[type=submit]:focus:before, #ticket_form button[type=submit]:hover:before {
  transform: translateZ(0)
}

#ticket_form button[type=submit] {
  color: #fff
}

#ticket_form button[type=submit]:before {
  background-color: #fff
}

#ticket_form button[type=submit]:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: -2;
  height: 100%;
  width: 100%;
  background-color: #212123;
}

#ticket_form button[type=submit]:focus, #ticket_form button[type=submit]:hover {
  color: #212123
}

#firefox_warning {
  width: 100%;
  text-align: center;
  background-color: #f4f4f7;
  padding: 10px;
}
#firefox_warning a, #ticket_thankyou_msg a{
  color: #3accdd;
  text-decoration: none;
}
#firefox_warning a:hover, #ticket_thankyou_msg a:hover {
  color: #3accdd;
  text-decoration: none;
}
#support-search-panel .aa-Panel {
  top: 0px !important;
  position: static;
  box-shadow: none;
}
#support-search-panel .aa-Item {
  top: 0px !important;
  position: static;
  box-shadow: none;
  min-height: 1.8em;
  line-height: 1.3em;
}
#support-search-panel .aa-PanelLayout {
  padding-top: 0px;
}
#support-search-div {
  padding-bottom: 15px;
}
#support-search-div .aa-Form {
  box-shadow: none;
  border-color: transparent;
  border-radius: 0px;
  border-bottom: solid 2px #c9c9c9;
}
#support-search-div .aa-Form button {
  padding-top: 10px;
}
</style>


<script type="text/javascript">
function support_doc_submit(){
  window.location = base_url + '/search/?query=' + encodeURIComponent($('#support-search-form .aa-Form .aa-Input').val());
  return false;
}

String.prototype.mapReplace = function(map) {
  var mstr = this;
  for (var wd in map) {
    if (map.hasOwnProperty(wd)) {
        var rep = new RegExp('\\b' + wd + '\\b','gi');
        mstr = mstr.replace(rep,map[wd]);
    }
  }
  return mstr;
};

var wordmap = {
  'REST' : 'REST',
  'API' : 'API',
  'APIs' : 'APIs',
  'iOS' : 'iOS',
  'ID' : 'ID',
  'IDs' : 'IDs',
  'FAQ' : 'FAQ',
  'FAQS' : 'FAQs',
  'Android' : 'Android'
}
var ticket_lookuptable = {
  'SelectText' : 'What can we help you with?',
  'Label': '* What can we help you with?',
  'SelectDefault': 'Select a topic...',
  'LinksTitle': ['Marketer documentation','Developer documentation','Marketer troubleshooting guide','Frequently Asked Questions'],
  'Links': ['{{site.baseurl}}/user_guide/introduction/','{{site.baseurl}}/developer_guide/platform_wide/platform_features/','{{site.baseurl}}/help/home/','{{site.baseurl}}/help/faqs/'],
  'SelectOption': {
    'Technical Issue': {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Platform Features'],
      'Links' : ['{{site.baseurl}}/developer_guide/platform_wide/platform_features/'],
      'SelectOption' : {
        'SDK Integrations' : {
          'Label': 'My question is about... *',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['Self-Service SDK Debugging Tool','iOS: Initial SDK Setup','Android: Initial SDK Setup','Web: Initial SDK Setup','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
          'Links': ['{{site.baseurl}}/developer_guide/sdk_integration/debugging','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview','{{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits'],
          'SelectOption' : {
            'Push' : {
              'SelectDefault': 'Select a platform...',
              'LinksTitle': [],
              'Links': [],
              'Label': 'Platform *',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: Push Integration','Android: Push Troubleshooting'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: Push Integration', 'iOS: Push Troubleshooting'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: Push Integration','Web: Error Logging'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'In-App Messages': {
              'LinksTitle': [''],
              'Links':  [''],
              'Label': 'Platform *',
              'SelectDefault': 'Select data type...',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: In-App Message Integration','Android: In-App Message Customization','Android: In-App Message Troubleshooting'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/troubleshooting/']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: In-App Message Integration','iOS: In-App Message Customization','iOS: In-App Message Troubleshooting'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/troubleshooting/']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: In-App Message Integration','Web: In-App Message Customization','Web: In-App Message Troubleshooting','Web: Error Logging'],
                  'Links': ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/troubleshooting/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'Content Cards': {
              'LinksTitle': [''],
              'Label': 'Platform *',
              'SelectDefault': 'Select data type...',
              'SelectOption' : {
                'Android' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Android: Content Card Integration','Android: Content Card Customization'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization']
                },
                'iOS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['iOS: Content Card Integration','iOS: Content Card Customization'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/customization']
                },
                'Web' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Web: Content Card Integration','Web: Content Card Customization','Web: Error Logging'],
                  'Links' : ['{{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization','{{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#error-logging']
                },
                'Other' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Braze Developer Guide','SDK Changelog','Sending Test Messages','Braze Learning Course: Technical Integration Checklist and Toolkits'],
                  'Links' : ['{{site.baseurl}}/developer_guide/home','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs','{{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/','https://learning.braze.com/technical-integration-checklists-and-toolkits']
                }
              }
            },
            'User Data' :{
              'ShowSubmit': false,
              'Label': 'Category *',
              'LinksTitle': ['Automatically Collected Data','Event Naming Conventions','User Profile Lifecycle'],
              'Links': ['{{site.baseurl}}/developer_guide/platform_wide/analytics_overview#automatically-collected-data','{{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/','{{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle'],
                'SelectOption' : {
                'Custom Events, Purchase Event, and Properties' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Custom Events','Purchase Events','Android: Tracking Custom Events','iOS: Tracking Custom Events','Web: Tracking Custom Events'],
                  'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/custom_data/events/','{{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events']
                },
                'Custom Attributes' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Custom Attributes','Android: Setting Custom Attributes','iOS: Setting Custom Attributes','Web: Setting Custom Attributes'],
                  'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes','{{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/','{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/','{{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/']
                }
              }
            },
            'Other' :{
              'ShowSubmit': true,
              'LinksTitle': [''],
              'Links': ['']
            }
          }
        },
        'REST APIs' : {
          'Label': 'My question is about... *',
          'SelectDefault': 'Select a type...',
          'LinksTitle': ['REST API: Endpoint Dictionary'],
          'Links': ['{{site.baseurl}}/api/home'],
          'SelectOption' : {
            'Errors' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Errors and Responses'],
              'Links' : ['{{site.baseurl}}/api/errors/']
            },
            'Importing Data' : {
              'ShowSubmit': true,
              'LinksTitle': ['User Import', 'REST API: User Data Endpoints'],
              'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/','{{site.baseurl}}/api/endpoints/user_data']
            },
            'Exporting Data' : {
              'ShowSubmit': true,
              'LinksTitle': ['Exporting Braze Data','REST API: Export Endpoints', 'Export Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data','{{site.baseurl}}/api/endpoints/export','{{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/faqs/']
            },
            'API Campaigns' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Campaign Overview','REST API: Send API-Triggered Campaign Endpoint','REST API: Schedule API-Triggered Campaign Endpoint'],
              'Links' : ['{{site.baseurl}}/api/api_campaigns/','{{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/','{{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/']
            },
            'Rate Limits' : {
              'ShowSubmit': true,
              'LinksTitle': ['API Rate Limits'],
               'Links' : ['{{site.baseurl}}/api/api_limits/']
             },
             'Other' : {
               'ShowSubmit': true,
               'LinksTitle': ['API Basics', 'API Connectivity Issues','Postman and Sample Requests'],
               'Links' : ['{{site.baseurl}}/api/basics/','{{site.baseurl}}/api/network_connectivity_issues','{{site.baseurl}}/api/postman_collection/']
             }
          }
        },
        'Email' : {
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['Email Best Practices','Email Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/','{{site.baseurl}}/user_guide/message_building_by_channel/email/faq/'],
          'SelectOption': {
            'Setup (whitelabeled IPs, DNS records)' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Onboarding Resources','Setting Up IPs and Domains','IP warming'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/setting_up_ips_and_domains/','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup#ip-warming']
            },
            'Reporting and Analytics' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Reporting and Analytics'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/']
            },
            'Email Editors' : {
              'ShowSubmit': true,
              'LinksTitle': ['Email Drag-and Drop Editor', 'Email HTML Editor', 'Drag-And-Drop Editor Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop','{{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor','{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/faq/']
            },
            'Deliverability' :{
              'ShowSubmit': true,
              'LinksTitle': ['Deliverability Pitfalls and Spam Traps','IP Warming','Braze Learning Course: Achieving High Email Deliverability'],
               'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps#deliverability-pitfalls-and-spam-traps','{{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/#ip-warming','https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability']
            },
            'User Subscriptions' :{
              'ShowSubmit': true,
              'LinksTitle': ['Managing User Subscriptions'],
               'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/']
            },
            'Email Templates' : {
              'ShowSubmit': true,
              'LinksTitle': ['Creating an Email Template','Email Template Frequently Asked Questions'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template#step-3-customize-your-template','{{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/']
            },
            'Liquid' : {
              'ShowSubmit': true,
              'LinksTitle': ['Liquid Templating in Messages','Liquid Frequently Asked Questions','Braze Learning Course: Dynamic Personalization with Liquid'],
              'Links' : ['{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/faq/','https://learning.braze.com/dynamic-personalization-with-liquid']
            }
          }
        },
        'SMS and MMS' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['SMS Best Practices','SMS Frequently Asked Questions', 'MMS Frequently Asked Questions', 'Braze Learning Course: SMS Fundamentals'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices','{{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/','{{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/faqs/','https://learning.braze.com/sms-fundamentals'],
          'SelectOption': {
            'Setup' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS Onboarding Resources'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup']
            },
            'Subscription Groups' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS Subscription Groups'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_subscription_groups/']
            },
            'Short and Long Codes' : {
              'ShowSubmit': true,
              'LinksTitle': ['Short and Long Codes'],
              'Links' : ['{{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/']
            },
            'User Retargeting' : {
              'ShowSubmit': true,
              'LinksTitle': ['SMS User Retargeting'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/']
            }
          }
        },
        'WhatsApp' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['WhatsApp Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/faqs/'],
          'SelectOption': {
            'Setup' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp Setup Overview'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/']
            },
            'Subscription Groups' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp User Subscription'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/']
            },
            'User Phone Numbers' : {
              'ShowSubmit': true,
              'LinksTitle': ['WhatsApp User Phone Numbers'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/']
            }
          }
        },
        'Campaigns and Canvas' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['Campaign Frequently Asked Questions','Canvas Frequently Asked Questions'],
          'Links' : ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/','{{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/'],
          'SelectOption': {
            'Messaging Personalization' : {
              'ShowSubmit': true,
              'LinksTitle': ['Personalization and Dynamic Content','Personalization Using Liquid Tags','Liquid Use Case Library','Connected Content'],
              'Links' : ['{{site.baseurl}}/user_guide/personalization_and_dynamic_content','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases','{{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content']
            },
            'Targeting and Segmentation' : {
              'ShowSubmit': true,
              'LinksTitle': ['Segmentation','Segment Insights','Braze Learning Course: Segmentation',''],
              'Links' : ['{{site.baseurl}}/user_guide/engagement_tools/segments','{{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/','https://learning.braze.com/segmentation-course']
            },
            'Message Composition by Channel' : {
              'LinksTitle': ['Available Channels','Know Before You Send: Channels'],
              'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel','{{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/'],
              'Label': 'Channel *',
              'SelectDefault': 'Select channel...',
              'SelectOption' : {
                'Email' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating an Email Campaign with the Drag-And-Drop Editor','Creating an Email Campaign with the HTML Editor'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/','{{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/']
                },
                'Push' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Push Campaign','Braze Learning Course: Push'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#creating-a-push-message','https://learning.braze.com/messaging-channels-push']
                },
                'In-App Messages' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['In-App Message Drag-And-Drop Editor Campaign','In-App Message Traditional Editor Campaign','Braze Learning Course: In-App and In-Browser Messages'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/','{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/','https://learning.braze.com/messaging-channels-in-app-in-browser']
                },
                'Content Cards' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Content Card Campaign','Braze Learning Course: Content Cards'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/','https://learning.braze.com/messaging-channels-content-cards']
                },
                'Webhooks' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Creating a Webhook Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/']
                },
                'SMS and MMS' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Create an SMS Campaign','Creating as MMS Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/create/','{{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/create/']
                },
                'WhatsApp' : {
                  'ShowSubmit': true,
                  'LinksTitle': ['Create a WhatsApp Campaign'],
                  'Links' : ['{{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/']
                }
              }             
            }
          }
        },
        'Login Issues' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': [''],
          'Links' : [''],
          'SelectOption': {
            'Password Error' : {
              'ShowSubmit': true,
              'LinksTitle': ['Locked Out of Account'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/#password-error']
            },
            'Instance Error' : {
              'ShowSubmit': true,
              'LinksTitle': ['Instance Error'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/#instance-error']
            },
            'SAML and Single Sign On' : {
              'ShowSubmit': true,
              'LinksTitle': ['SAML and Single Sign On'],
              'Links' : ['{{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Account Login Issues'],
              'Links' : ['{{site.baseurl}}/help/help_articles/account/locked_out/']
            }
          }
        },
        'Technology Partners' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': [''],
          'Links' : [''],
          'SelectOption': {
            'Message Personalization' : {
              'ShowSubmit': true,
              'LinksTitle': ['Message Personalization Partners'],
              'Links' : ['{{site.baseurl}}/partners/message_personalization']
            },
            'Message Orchestration' : {
              'ShowSubmit': true,
              'LinksTitle': ['Message Orchestration Partners'],
              'Links' : ['{{site.baseurl}}/partners/message_orchestration']
            },
            'Data Infrastructure and Agility' : {
              'ShowSubmit': true,
              'LinksTitle': ['Data and Infrastructure Agility Partners'],
              'Links' : ['{{site.baseurl}}/partners/data_and_infrastructure_agility']
            },
            'Other' : {
              'ShowSubmit': true,
              'LinksTitle': ['Available Partner Integrations'],
              'Links' : ['{{site.baseurl}}/partners/home']
            }
          }
        },
        'System Status' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'LinksTitle': ['System Status'],
          'ShowSubmit': true,
          'Links' : ['https://braze.statuspage.io/'],
        },
        'Other' :{
          'SelectDefault': 'Select a type...',
          'Label': 'My question is about... *',
          'ShowSubmit': true,
          'LinksTitle': ['System Status','SDK Changelogs'],
          'Links' : ['https://braze.statuspage.io/','{{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs'],
        }
      }
    },
    'Strategy Assistance' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'LinksTitle': ['Campaign Ideas and Strategies','Canvas Ideas and Strategies','Building Accessible Messages in Braze','Braze Learning Course: Create Customer Journeys with Canvas Flow'],
      'Links': ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/','{{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies','{{site.baseurl}}/help/accessibility/','https://learning.braze.com/create-customer-journeys-with-canvas-flow'],
      'SelectOption' : {
        'Tools and Use Cases' : {
          'ShowSubmit': true,
          'LinksTitle': ['Campaign Ideas and Strategies', 'Canvas Ideas and Strategies','Braze Learning Course: Customer Engagement Tools and Use Cases'],
          'Links':  ['{{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/','{{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies','https://learning.braze.com/braze-customer-engagement-tools-use-cases']
        },
        'Best Practices and Frequently Asked Questions' :{
          'ShowSubmit': true,
          'LinksTitle': ['Best Practices and Frequently Asked Questions'],
          'Links':  ['{{site.baseurl}}/help/faqs']
        },
        'Other' :{
          'ShowSubmit': true,
          'LinksTitle': [''],
          'Links':  ['']
        }
      }
    },

    'Account Administration' : {
      'Label': '* Category',
      'SelectDefault': 'Select a category...',
      'Links': [],
      'ReferenceText': 'Your account manager is a great resource for billing and contract related questions. ',
      'SelectOption' : {
        'Data Points' : {
          'ShowSubmit': true,
          'LinksTitle': ['Data Points'],
          'Links': ['{{site.baseurl}}/user_guide/data_and_analytics/data_points#data-points']
        },
        'Billing' : {
          'ShowSubmit': true,
          'LinksTitle': ['Billing'],
          'Links': ['{{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/']
        },
        'Other' :{
          'ShowSubmit': true,
          'ReferenceText': 'Your account manager is a great resource for billing and contract related questions. ',
          'LinksTitle': [''],
          'Links':  ['']
        }
      }
    }
  }
}
var ticket_options = ticket_lookuptable['SelectOption'];
$( document ).ready(function() {

  $.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
      return null;
    }
    else{
      return decodeURIComponent(results[1]) || 0;
    }
  }

  var autofilllist = {
    'name': '#ticket_name',
    'email': '#ticket_email'
  };
  var hiddenlist = {
    'appgroup': '00N0V000009G0NE',
    'appgroupid': '00N0V000009G0N9',
    'companyid': '00NVP0000002y6X',
    'developerid': '00NVP0000004UvZ',
  };

  $.each(autofilllist, function(k,v){
    if ($.urlParam(k) ){
      $(v).val($.urlParam(k));
    };
  });

  var droplist = ['ticket_topic','ticket_category','ticket_subcategory','ticket_type'];
  var result_div = 'ticket_result';

  function reset_page(ind = 1){
    for(var i = ind; i < droplist.length;i++){
        $('#' + droplist[i]).empty();
    };
    $('#' + result_div).html('');
    /* if (!$("#submit_ticket").prop("checked")) {
      $("#submit_ticket").prop("checked", false);
      $("#submit_ticket").trigger("change");
    }*/
  }
  function hide_page(ind){
    for(var i = 0; i < droplist.length;i++){
        if (i < ind){
          $('#' + droplist[i]).attr('required',true);
          $('#' + droplist[i] + '_div').show();
        }
        else {
          $('#' + droplist[i]).attr('required',false);
          $('#' + droplist[i] + '_div').hide();
        }
    };
  }
  function removeleadingslash(str){
    var rstr = str;
    if (rstr.slice(-1) === "/") {
      rstr = rstr.slice(0, -1);
    }
    return rstr;
  }
  function notEmpty(listarr){
    var empty = false;
    if (Array.isArray(listarr) && listarr.length){
      for (var i = 0; i < listarr.length; i++){
        if (listarr[i]){
          empty = true;
          i = listarr.length;
        }
      }
    }
    return empty;    
  }
  function showlinks(curquestion){
    if (curquestion) {
      var linklist = curquestion['Links'];
      var linkstitle = curquestion['LinksTitle'];
      var resdiv = $('#ticket_reference');
      var resmsg = $('#ticket_message');

      var resstr = '';
      if ('ReferenceText' in curquestion){
        resstr += curquestion['ReferenceText'] + '<br />'
      }
      if (notEmpty(linklist) && (linklist.length > 0)){
        resmsg.html('Have you tried...')
        for (var i = 0 ; i < linklist.length; i++ ) {
          var title = '';
          if ((typeof linkstitle !== 'undefined') && (i in linkstitle) && linkstitle[i]) {
            title = linkstitle[i];
          }
          else {
            var linkparts =  linklist[i].split('#');
            var linkurl = removeleadingslash(linkparts[0]);
            var urlpart = linkurl.split('/')


            if (urlpart.length > 1) {
              title += ' ' + urlpart[urlpart.length-1].replace(/\_/g,' ').replace(/\-/g,' ');;
            }
            if (linkparts.length > 1) {
              var hashpart = linkparts[linkparts.length-1].replace(/\b\w/g, function(l){ return l.toUpperCase() });
              title += ': ' + hashpart.replace(/\_/g,' ').replace(/\-/g,' ');
            }
            title = title.mapReplace(wordmap)
          }
          resstr += '<a href="' + linklist[i] + '" target="braze_reference">' + title+ '</a><br />';
        }
        if ('ShowSubmit' in curquestion) {
          if (curquestion['ShowSubmit']) {
            $('#ticket_submit_option').show();
          }
          else {
            $('#ticket_submit_option').hide();
          }
        }
        else {
          $('#ticket_submit_option').hide();
        }
        if (resstr) {
          resdiv.html(resstr);
          resdiv.show();
        }
        else {
          resdiv.hide();
        }
      }
      else {
        resmsg.html('');
        if (notEmpty(linklist) ) {
          $('#ticket_submit_option').show();
        }
        else {
          resdiv.html('');
          resdiv.hide();
          if ('ShowSubmit' in curquestion) {
            if (curquestion['ShowSubmit']) {
              $('#ticket_submit_option').show();
            }
            else {
              $('#ticket_submit_option').hide();
            }
          }
          else {
            $('#ticket_submit_option').hide();
          }
        }
        if (resstr) {
          resdiv.html(resstr);
          resdiv.show();
        }
        else {
          resdiv.hide();
        }
      }

      /*if ('ShowSubmit' in curquestion) {
        if (curquestion['ShowSubmit']) {
          if (!$("#submit_ticket").prop("checked")) {
            $("#submit_ticket").prop("checked", true);
            $("#submit_ticket").trigger("change");
          }
        }
      }*/
    }
  }

  function subtype_change(e){
    var topic_selected =  $('#ticket_topic option:selected').val();
    var category_selected =  $('#ticket_category option:selected').val();
    var type_selected =  $('#ticket_subcategory option:selected').val();

    var subtype_selected =  $('#ticket_type option:selected').val();
    var subtype_links = ticket_options[topic_selected]['SelectOption'][category_selected]['SelectOption'][type_selected]['SelectOption'][subtype_selected];
    showlinks(subtype_links)

  }

  function type_change(e) {
    reset_page(3);
    var topic_selected =  $('#ticket_topic option:selected').val();
    var category_selected =  $('#ticket_category option:selected').val();
    var type_selected =  $('#ticket_subcategory option:selected').val();
    var subtype_selected = this.value;

    var subtype_options = ticket_options[topic_selected]['SelectOption'][category_selected]['SelectOption'][type_selected];
    if (subtype_options && ('Label' in subtype_options)){
      $('#ticket_type_label').html(subtype_options['Label']);
    }

    if (subtype_selected && 'SelectOption' in subtype_options) {
      hide_page(4);
      if ('SelectDefault' in subtype_options) {
        subtype_menu.append($('<option>',{value: ''}).html(subtype_options['SelectDefault']));
      }
      else {
        subtype_menu.append($('<option>',{value: ''}).html('Select a type...'));
      }
      $.each(subtype_options['SelectOption'],function(subtype)  {
        subtype_menu.append($('<option>',{value: subtype}).html(subtype));
      });
    }
    else {
      hide_page(3);
      //showlinks(subtype_options);
    }
    showlinks(subtype_options);
  }

  function category_change(e) {
    reset_page(2);

    var topic_selected =  $('#ticket_topic option:selected').val();
    var type_selected = this.value;
    var type_options = ticket_options[topic_selected]['SelectOption'][type_selected];
    //type_menu.empty();

    if (type_selected && 'SelectOption' in type_options) {
      hide_page(3);
      if ('SelectDefault' in type_options) {
        type_menu.append($('<option>',{value: ''}).html(type_options['SelectDefault']));
      }
      else {
        type_menu.append($('<option>',{value: ''}).html('Select a subcategory...'));
      }
      $.each(type_options['SelectOption'],function(type)  {
        type_menu.append($('<option>',{value: type}).html(type));
      });

    }
    else {
      hide_page(2);
    }
    showlinks(type_options);
  }

  function topic_change(e) {
    reset_page(1);
    var topic_selected = this.value;
    var category_options = ticket_options[topic_selected];
    if (topic_selected && 'SelectOption' in category_options ) {
      hide_page(2);
      if ('SelectDefault' in category_options) {
        category_menu.append($('<option>',{value: ''}).html(category_options['SelectDefault']));
      }
      else {
        category_menu.append($('<option>',{value: ''}).html('Select a category...'));
      }
      $.each(category_options['SelectOption'],function(category) {
        category_menu.append($('<option>',{value: category}).html(category));
      });
      // showlinks(category_options);
    }
    else {
      hide_page(1);
    }
    showlinks(category_options);
  }


  var tmenu = $('#ticket_menu');
  var topic_menu = $('#ticket_topic');
  var subtype_menu = $('#ticket_type');
  var type_menu = $('#ticket_subcategory');
  var category_menu = $('#ticket_category');

  function settopic(){
    reset_page(0);
    hide_page(1);

    //topic_menu.empty();
    if ('SelectDefault' in ticket_lookuptable) {
      topic_menu.append($('<option>',{value: ''}).html(ticket_lookuptable['SelectDefault']));
    }
    else {
      topic_menu.append($('<option>',{value: ''}).html('Select a topic...'));
    }
    /* Generate Initial Menu */
    $.each(ticket_options,function(topic)  {
      topic_menu.append($('<option>',{value: topic}).html(topic));
    });

  };
  settopic();

  /* if menu changes, dynamically create new menu */
  category_menu.on('change',category_change);
  type_menu.on('change',type_change);
  topic_menu.on('change',topic_change);
  subtype_menu.on('change',subtype_change);

  $('#ticket_submit_option').hide();
  /* $('#submit_ticket').on('change',function(e){
    if(this.checked){
      $('#ticket_submit_option').show();
    }
    else{
      $('#ticket_submit_option').hide();
    }
  });*/
  //showlinks(ticket_lookuptable);
  function iframeform(url) {
      var object = this;
      object.time = new Date().getTime();
      object.form = $('<form action="'+url+'" target="iframe'+object.time+'" method="post" style="display:none;" id="form'+object.time+'" name="form'+object.time+'"></form>');

      object.addParameter = function(parameter,value) {
          $("<input type='text' />")
           .attr("name", parameter)
           .attr("value", value)
           .appendTo(object.form);
      }
      object.addBodyText = function(parameter,value) {
          $("<textarea type='hidden' />")
           .attr("name", parameter)
           .html(value)
           .appendTo(object.form);
      }
      object.send = function() {
          var iframe = $('<iframe data-time="'+object.time+'" style="display:none;" id="iframe'+object.time+'"  name="iframe'+object.time+'" ></iframe>');
          $( "body" ).append(iframe);
          $( "body" ).append(object.form);
          object.form.submit();
          iframe.on('load',function(){  $('#form'+$(this).data('time')).remove();  $(this).remove();   });
      }
  }

  $('#ticket_form').submit(function(e){
    e.preventDefault();
    var mform = $(this);
    var sels = mform.find('select');
    var user_name = $('#ticket_name').val();
    var user_email = $('#ticket_email').val();
    var user_ccemail = $('#ticket_ccemail').val();

    var user_subject = $('#ticket_subject').val();

    var user_issue = $('#ticket_issue').val();

    var sf_submit = new iframeform('https://webto.salesforce.com/servlet/servlet.WebToCase?encoding=UTF-8');

    sf_submit.addParameter('orgid','00Dd0000000e3l4');
    sf_submit.addParameter('retURL','https://braze.com');
    sf_submit.addParameter('name',user_name);
    sf_submit.addParameter('email',user_email);
    sf_submit.addParameter('subject',user_subject);
    if (user_ccemail) {
      sf_submit.addParameter('00N0V000008wX0Y',user_ccemail);
    }
    sf_submit.addBodyText('description',user_issue);
    $.each(sels,function(k,v){
      var selopt = $(this);
      var selval = selopt.find(':selected');
      if (typeof selval !== 'undefined') {
        sf_submit.addParameter(selopt.attr('name'),selval.val());
      }
    });
    $.each(hiddenlist, function(k,v){
      if ($.urlParam(k) ){
        sf_submit.addParameter(v,$.urlParam(k));
      };
    });

    sf_submit.addParameter('external','1');
    sf_submit.send();

    var gs_submit = new iframeform('https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/support_request');
    gs_submit.addParameter('Name', user_name);
    gs_submit.addParameter('Email', user_email);
    gs_submit.addParameter('Subject', user_subject);
    if (user_ccemail) {
      gs_submit.addParameter('CC_Email',user_ccemail);
    }
    gs_submit.addBodyText('Question', user_issue);
    var gs_mapping = {
      "00N0V000009G0MG" : "Topic", // Topic
      "00N0V000009G0MB" : "Category",  // Category
      "00N0V000009G0ML" : "Subcategory", // Subcategory
      "00N0V000009G0MQ" : "Type", // Type
      "priority" : "Priority", // Priority
    }

    $.each(sels,function(k,v){
      var selopt = $(this);
      var selval = selopt.find(':selected');
      if (typeof selval !== 'undefined') {
        if (gs_mapping[selopt.attr('name')]) {
          gs_submit.addParameter(gs_mapping[selopt.attr('name')],selval.val());
        }
      }
    });
    $.each(hiddenlist, function(k,v){
      if ($.urlParam(k) ){
        gs_submit.addParameter(v,$.urlParam(k));
      };
    });
    gs_submit.send();

    $('#ticket_mainform').hide();

    $('#ticket_thankyou').fadeIn("slow");
    $('#ticket_thankyou_msg').html('<h3>Thanks for your submission!</h3>A member of our Support team will respond to your ticket soon.<br />If you did not get a confirmation email, check your browser\'s addon, content/privacy setting and email spam folder.<br />Otherwise, contact your success manager (or email us at <a href="mailto:support@braze.com">support@braze.com</a>) to make sure your ticket has been submitted.');
    $("html, body").animate({ scrollTop: 0 }, "slow");
  });
  $('#ticket_issue').popover();
  $('#ticket_comment').popover();
  $('#ticket_priority_info').popover({
    html: true
  });

  $("#submit_ticket").trigger("change");


  function string_to_slug(str) {
    if (str) {
      str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
    }
    return str;
  }
  const algoliaInsightsPluginSupport = createAlgoliaInsightsPlugin({
    insightsClient,
    onItemsChange({ insights, insightsEvents }) {
      const events = insightsEvents.map((insightsEvent) => ({
        ...insightsEvent,
        eventName: 'Viewed from Support Search',
      }));
      insights.viewedObjectIDs(...events);
    },
    onSelect({ insights, insightsEvents }) {
      const events = insightsEvents.map((insightsEvent) => ({
        ...insightsEvent,
        eventName: 'Clicked from Support Search',
      }));
      insights.clickedObjectIDsAfterSearch(...events);
    },
  });
  autocomplete({
    container: "#support-search-div",
    panelContainer: "#support-search-panel",
    debug: true,
    placeholder: "Search",
    plugins: [algoliaInsightsPluginSupport],
    detachedMediaQuery: 'none',
    onSubmit(e){
      var query = e.state.query;
      window.location = base_url + '/search/?query=' + encodeURIComponent(query);
    },
    getSources() {
      return [{
          sourceId: "querySuggestions",
          getItemInputValue: ({ item }) => item.query,
          getItems({ query }) {
            return getAlgoliaResults({
              searchClient,
              queries: [
                {
                  indexName: "DocSearch",
                  query,
                  params: {
                    hitsPerPage: 5,
                    attributesToSnippet: ["description:12"],
                    snippetEllipsisText: " ...",
                    clickAnalytics: true,
                  },
                },
              ],
            });
          },
          getItemUrl({ item }) {
           return base_url + item.url;
         },
         templates: {
           noResults({createElement}) {
             return createElement("div", {
               dangerouslySetInnerHTML: {
                 __html: '<div class="no_results">No results were found with your current search. Try to change the search query.</div>',
                 },
               })
          },

          item({ item, createElement }) {
            var content = "";
            var title = "";
            var type = "";
            var category = "";
            var platform = "";
            var subname = "";
            var heading = "";

            if ("nav_title" in item) {
              title = item.nav_title.replaceUnder();
            } else {
              title = item.title.replaceUnder();
            }
            if ("type" in item) {
              type = item.type.replaceUnder().upCaseWord();
            }
            if ("category" in item) {
              category = item.category.replaceUnder();
            }

            if ("platform" in item) {
              if (Array.isArray(item.platform)){
                platform = item.platform.join(',').replace(/\%20/g, ' ').replace(/\_/g, ' ') + ' > ';
              }
              else {
                platform = item.platform.replace(/\%20/g, ' ').replace(/\_/g, ' ') + ' > ';
              }
            }
            if ("headings" in item) {
              if (item["headings"]) {
                heading = item["headings"][item["headings"].length - 1];
              }
            }

            var url = item.url;
            if (heading) {
              url += "#" + string_to_slug(heading);
            }
            var resulttemplate = '<a href="' +
                base_url + url + '"><div class="title"> * ' +
                platform + title + ' <div class="category">' +
                subname.replace(/\_/g, " ") +
                "</div></div></a>";
            return createElement("div", {
              dangerouslySetInnerHTML: {
                __html: resulttemplate,
              },
            });
          },
        },
      }];
    }
  });

 if (navigator.userAgent.toLowerCase().indexOf('firefox') > -1 ) {
   var ff_div = $('#firefox_warning').detach();
   ff_div.insertBefore($('#basic_page')).show();
 }
});
</script>
<div id="firefox_warning" style="display:none;">Für Nutzer:innen von Firefox sollten Sie diese Seite zulassen oder Ihre <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Privacy/Tracking_Protection?utm_source=mozilla&utm_medium=firefox-console-errors&utm_campaign=default" target="_blank">Tracking-Schutzeinstellungen</a> überprüfen, da Ihr Ticket sonst möglicherweise nicht übermittelt wird.</div>

<div class="container-fluid" id="main-container">
      <div class="row">
          <div class="col" >
              <h1 class="h1">Brauchen Sie Hilfe? </h1>
              <div class="gradient-line"></div>
          </div>
      </div>
        <div id="ticket_mainform" class="row">
        <div class="col-sm-7" id="ticket_leftmain">
          <form id="ticket_form">


                <div class="row">
                    <div class="col">
                        <div class="form-group" id="ticket_topic_div">
                          <label for="ticket_topic" id="ticket_topic_label"> What can we help you with? *</label>
                          <select id="ticket_topic" name="00N0V000009G0MG"  class="form-control" ></select>

                        </div>
                        <div class="form-group" id="ticket_category_div">
                          <label for="ticket_category" id="ticket_category_label">Category * </label>
                          <select id="ticket_category" name="00N0V000009G0MB"  class="form-control" ></select>
                        </div>
                        <div class="form-group" id="ticket_subcategory_div">
                          <label for="ticket_subcategory" id="ticket_subcategory_label">My question is about... * </label>
                          <select id="ticket_subcategory" name="00N0V000009G0ML"  class="form-control" ></select>
                        </div>
                        <div class="form-group" id="ticket_type_div">
                          <label for="ticket_type" id="ticket_type_label">Platform * </label>
                          <select id="ticket_type" name="00N0V000009G0MQ"  class="form-control" ></select>
                        </div>
                        <div class="form-group">
                          <label id="ticket_message"></label>
                          <div id="ticket_reference"></div>
                        </div>
                    </div>

                </div>
                <!-- div class="row">
                  <div class="col">
                    <label for="submit_ticket" class="checkbox-inline">

                    <input type="checkbox" value="submit_ticket" name="submit_ticket" id="submit_ticket"  />
                    Submit a ticket.</label>
                  </div>
                </div -->

                <div class="row">

                  <div class="col">
                    <div id="ticket_submit_option">
                      <h2>Not finding what you need? Contact our Support team.</h2>
                      <div class="form-group" >
                          <label for="ticket_name" id="ticket_name_label">  Name *</label>
                          <input type="text" name="Name" id="ticket_name"  maxlength="80" required="required" value="" placeholder="Enter your name" class="form-control" />
                      </div>
                      <div class="form-group" >

                        <label for="ticket_email" id="ticket_email_label"> Email address *</label>
                        <div class="input-group">
                          <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">@</span>
                          </div>
                          <input type="email" class="form-control" id="ticket_email"  maxlength="80" name="Email" placeholder="Enter email" required="required" value="" /></div>
                      </div>
                      <div class="form-group" >
                        <label for="ticket_email" id="ticket_ccemail_label"> CC Email address </label>
                        <div class="input-group">
                          <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon1">@</span>
                          </div>
                          <input type="email" class="form-control" id="ticket_ccemail"  maxlength="80" name="CCEmail" placeholder="Enter CC email"  value="" /></div>
                      </div>
                      <div class="form-group" >
                          <label for="ticket_subject" id="ticket_subject_label">   Subject *</label>
                          <input type="text" class="form-control" id="ticket_subject"  maxlength="80" name="Subject" placeholder="What's your question about?" required="required" value="" />
                      </div>

                      <div class="form-group" id="ticket_priority_div">
                        <label for="ticket_priority" id="ticket_priority_label">Issue severity * </label>
                        <a id="ticket_priority_info" title="Issue Severity Description"
                          data-toggle="popover" data-placement="top" data-trigger="click"
                          data-content="A <b>Critical severity</b> issue has a critical business impact on use of the Braze services that impact all Users. Examples include complete system unavailability or data integrity issues, with no workaround available at the time the issue is logged with Braze Technical Support.<br />
                          A <b>High severity</b> issue is causing a significant loss or reductions of functionality to the customer’s use of the platform causing a serious impact to the customer’s operational activities.<br />
                          A <b>Medium severity</b> issue causes a material loss or reduction of functionality which has an impact on the customer’s normal use of the platform.<br />
                          A <b>Low severity</b> issue is any question about the use of Braze services and analytics or a minor loss or disruption of normal platform functionality."><span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-question-circle" ></span></a>
                        <select id="ticket_priority" name="priority"  class="form-control" >
                          <option value="Critical">Critical: System is down or severe data integrity issues</option>
                          <option value="High">High: Severe loss of functionality or a campaign will not send</option>
                          <option value="Medium">Medium: Degraded performance or issue causing significant business impact</option>
                          <option value="Low" selected="selected">Low: Question about Braze functionality or analytics</option>
                        </select>
                      </div>

                      <div class="form-group" >

                          <label for="ticket_issue" id="ticket_issue_label">     Question * </label>

                          <textarea name="ticket_issue" class="form-control" id="ticket_issue"  required="required" data-toggle="popover" data-trigger="focus" data-placement="top"
                          data-content="Include information helpful for investigation and troubleshooting, such as your platform, SDK version, REST API endpoints, links to segments or campaigns, relevant user IDs, and steps to reproduce your issue.   "
                          placeholder="Include information helpful for investigation and troubleshooting, such as your:
- Plattform
- SDK-Version
- REST API Endpunkte,
- Links zu Segmenten oder Kampagnen
- Relevante Nutzer:innen IDs
- SDK Debugger Session ID
- Schritte, um Ihr Problem zu reproduzieren " rows="7"></textarea>
                      </div>
                      <!-- div class="form-group" >

                          <label for="ticket_comment"  id="ticket_comment_label">     Additional comments and screenshots  </label>

                          <textarea name="Issue_Steps" class="form-control" id="ticket_comment" data-toggle="popover" data-trigger="focus" data-placement="top"
                          data-content="Add any other comments and link to any relevant screenshots or screencasts."
                          placeholder="Add any other comments and link to any relevant screenshots or screencasts." rows="7"></textarea>
                      </div -->
                      <div class="form-group">
                          <label style="font-size: 12px;">
                         In order to provide you with technical support or address service or technical problems, be aware that Braze may need to access your dashboard and data.
                          </label>
                          <label style="font-size: 12px;">
                          Braze technical support hours of operation are from 9:00 am–5:00 pm GMT and 8:00 am–8:00 pm ET, Monday - Friday, excluding Braze recognized holidays. For issues logged outside of these hours, you should anticipate a response on the next business day.
                          </label>
                      </div>
                      <button type="submit" name="Submit Ticket" value="Submit" class="btn btn-black" id="ticket_submit_button" role="button"> SUBMIT TICKET </button>
                      </div>
                  </div>
              </div>
              </form>
        </div>
        <div class="col-sm-5" id="ticket_resources">
        <div id="support-search-div">
         </div>

           <div id="support-search-panel"></div>

            <legend>Useful Resources</legend>

            <div id="ticket_usefulresources">
              <a target="" href="{{site.baseurl}}/user_guide/introduction/">User Guide</a><br />
              <a target="" href="{{site.baseurl}}/developer_guide/platform_wide/platform_features/">Developer Guide</a><br />
              <a target="" href="{{site.baseurl}}/help/home/">Help & Troubleshooting Guides</a><br />
              <a target="" href="{{site.baseurl}}/help/faqs/">Frequently Asked Questions</a><br />
              <a target="" href="https://learning.braze.com/">Braze Learning</a><br />
              <a target="" href="https://dashboard.braze.com/">Braze Dashboard</a><br />
            </div>

        </div>
    </div>
    <div id="ticket_thankyou" style="display:none;"><div class="row"><div class="col" id="ticket_thankyou_msg"></div></div></div>
</div>
