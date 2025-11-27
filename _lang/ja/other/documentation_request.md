---
nav_title: ドキュメントのリクエスト
permalink: "/request/"
hide_nav: true
layout: basic
hide_toc: true
---

  <style type="text/css">
  body {
      line-height: 2;
      background-color: #fff;
      font-weight: 400;
      font-size: 15px;
      font-family: Sailec W00 Regular,Arial,sans-serif;
      font-style: normal;
      color: #212123;
  }

  #main-container label {
    font-weight: bold;
    font-size: 18px;
  }
  #main-container {
    margin-top: 40px;
  }

  .container {
    margin-top: 40px;
  }
  @media (min-width: 768px) {
    #main-container {
      margin-top: 80px;
    }
  }
  @media (min-width: 1200px) {
    #main-container {
      margin-top: 60px;
    }
  }
  .popover{
    max-width: 95%;
    min-width: 350px;
  }


  .container-fluid {
    max-width: 820px;
  }
  .gradient-line {
      background: linear-gradient(30deg,#3accdd,#f7918e 64%,#ff9349 90%);
      height: 2px;
      width: 50%;
      margin-bottom:20px;
  }

  a {
    color: #3bcddf;
  }
  a:hover {
    color: #333;
  }


    @media (min-width: 1400px) {
      .container {
        max-width: 1340px;
      }
    }
    @media (min-width: 992px) {
      #doc_div {
        padding-top: 16px;
      }
    }
    .h1, h1  {
      font-size: 34pt;
      font-family: Sailec W00 Bold, Arial, sans-serif;
      margin-bottom: 24px;
    }

    .h2, h2 {
      font-size: 20px;
    }
    .subhead {
      font-size: 14pt;
      font-family: Sailec W00 Regular,Arial,sans-serif;
      margin-bottom: 16px;
    }

    #ticket_footer {
      margin-left: auto;
      margin-right: auto;
      border-top: 1px solid #c9c9c9;
      text-align: center;
      font-size: 10px;
      padding-top: 10px;
    }

    #ticket_footer a {
      text-decoration: none;
      color: #212123;
    }
    #ticket_footer li {
      display: inline;
      margin: 10px;

    }
    .form-control {
      border-color: rgb(0, 130, 148);
    }
    .btn, input[type=submit] {
      display: inline-block;
      vertical-align: middle;
      font: inherit;
      text-align: center;
      margin: 0;
      cursor: pointer;
      padding: 0px 1.5rem;
      height: 40px;
      min-width: 200px;
      font-family: Sailec W00 Bold, Arial, sans-serif;
      font-size: 12pt;
      font-weight: 700;
      border-radius: 2px;
      white-space: normal;
      background-color: rgb(0, 130, 148);
      border-color: rgb(0, 130, 148);
      color: rgb(255, 255, 255);
      position: relative;
      z-index: 1;
      overflow: hidden;
      transition: color .3s cubic-bezier(.5, 0, .1, 1), border-color .3s cubic-bezier(.5, 0, .1, 1);
      will-change: color, border-color
    }
    .btn:focus, .btn:hover, input[type=submit]:focus, input[type=submit]:hover {
      background: rgb(13, 175, 197);
      border-color: rgb(13, 175, 197);
    }
    .lds-ring {
      display: inline-block;
      position: relative;
      width: 30px;
      height: 25px;
    }
    .lds-ring div {
      box-sizing: border-box;
      display: block;
      position: absolute;
      width: 22px;
      height: 22px;
      margin: 8px;
      border: 4px solid #fff;
      border-radius: 50%;
      animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
      border-color: #fff transparent transparent transparent;
    }
    .lds-ring div:nth-child(1) {
      animation-delay: -0.45s;
    }
    .lds-ring div:nth-child(2) {
      animation-delay: -0.3s;
    }
    .lds-ring div:nth-child(3) {
      animation-delay: -0.15s;
    }
    @keyframes lds-ring {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
    #submit_progress {
      display: none;
    }
    #submit_text{
      display: inline;
    }
    .btn-small {
      padding: 1.07143rem 1.78571rem !important
    }
    .form-group {
      margin-bottom: 16px;
    }
    .form-group label {
      font-size: 13pt !important;
      font-family: Sailec W00 Bold, Arial, sans-serif;
      margin-bottom: 6px;
    }
    input[type=text] {
      border-radius: 0;
    }
    textarea {
      border-radius: 0 !important;
    }
    #doc_verify_label {
      font-size: 12pt !important;
      font-family: Sailec W00 Regular,Arial,sans-serif;
    }
    input[type="checkbox"] {
        display:none;
    }
    input[type="checkbox"] + label {
      font-size: 14pt !important;
      font-family: Sailec W00 Regular,Arial,sans-serif;
    }
    .form-check {
      padding-left: 0;
    }
    .sublabel {
      font-size: 12pt !important;
      font-family: Sailec W00 Regular,Arial,sans-serif;
      color: #5E6C75;
      line-height: 1.4;
    }
    .email-input {
      border-radius:0;
      padding-left: 36px;
      display: inline-block
    }
    .email-icon {
      position: absolute;
      left: 12px;
      top: 10px;
      font-size: 20px;
      z-index: 5;
    }
    input[type="checkbox"] + label span {
      display:inline-block;
      width:19px;
      height:19px;
      margin:-1px 4px 0 0;
      vertical-align:middle;
      cursor:pointer;
      border-radius: 2px;
      border-radius: 2px;
      border: 1px solid rgb(168, 179, 184);
    }
    input[type="checkbox"]:checked + label span {
      border-radius: 2px;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' style='fill: none; stroke: white; stroke-width: 3px; background: rgb(0, 130, 148);'%0AviewBox='0 0 24 24' %3E%3Cpolyline aria-hidden='true' style=' stroke: white; stroke-width: 3px; border: 1px solid rgb(0, 130, 148);%0Atransition: all 150ms ease 0s;%0Aline-height: normal;%0Abackground: rgb(0, 130, 148); ' points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E");
      background-repeat: no-repeat no-repeat;
      background-position: center center;
      background-size: cover;
    }
    .drop-down-sel {
      background-color: rgb(255, 255, 255);
      border-color: rgb(168, 179, 184);
      border-radius: 2px;
      border-style: solid;
      border-width: 1px;
      box-shadow: none;
      width: 100%;
      padding: 0.25rem;
      color: #495057;
    }
    .drop-down-sel:focus, .drop-down-sel:active, .drop-down-sel:hover,.drop-down-sel:focus-visible {
      border-color: rgb(0, 130, 148);
    }
    .inline_text {
      display: flex;
      font-family: Sailec, Arial, sans-serif;
      font-size: 10pt;
    }
    #braze_internal {
      width: 100%;
      text-align: center;
      background-color: #FFEEE3;
      padding: 10px;
      height: 45px;
      font-family: Sailec W00 Bold, Arial, sans-serif;
      font-size: 12tpt;
      position: absolute;
      left: 0;
      top: 60px;
      z-index: 10;
      color: #D45F24;
    }
    #braze_internal a {
      color: #27368F;
      text-decoration: none;
    }
    #braze_internal a:hover{
      color: #27368F;
    }
  </style>
  <script type="text/javascript">
    ! function(e, i) {
      if ("function" == typeof define && define.amd) define(["exports", "jquery"], function(e, r) {
        return i(e, r)
      });
      else if ("undefined" != typeof exports) {
        var r = require("jquery");
        i(exports, r)
      } else i(e, e.jQuery || e.Zepto || e.ender || e.$)
    }(this, function(e, i) {
      function r(e, r) {
        function n(e, i, r) {
          return e[i] = r, e
        }

        function a(e, i) {
          for (var r, a = e.match(t.key); void 0 !== (r = a.pop());)
            if (t.push.test(r)) {
              var u = s(e.replace(/\[\]$/, ""));
              i = n([], u, i)
            } else t.fixed.test(r) ? i = n([], r, i) : t.named.test(r) && (i = n({}, r, i));
          return i
        }

        function s(e) {
          return void 0 === h[e] && (h[e] = 0), h[e]++
        }

        function u(e) {
          switch (i('[name="' + e.name + '"]', r).attr("type")) {
            case "checkbox":
              return "on" === e.value ? !0 : e.value;
            default:
              return e.value
          }
        }

        function f(i) {
          if (!t.validate.test(i.name)) return this;
          var r = a(i.name, u(i));
          return l = e.extend(!0, l, r), this
        }

        function d(i) {
          if (!e.isArray(i)) throw new Error("formSerializer.addPairs expects an Array");
          for (var r = 0, t = i.length; t > r; r++) this.addPair(i[r]);
          return this
        }

        function o() {
          return l
        }

        function c() {
          return JSON.stringify(o())
        }
        var l = {},
          h = {};
        this.addPair = f, this.addPairs = d, this.serialize = o, this.serializeJSON = c
      }
      var t = {
        validate: /^[a-z_][a-z0-9_]*(?:\[(?:\d*|[a-z0-9_]+)\])*$/i,
        key: /[a-z0-9_]+|(?=\[\])/gi,
        push: /^$/,
        fixed: /^\d+$/,
        named: /^[a-z0-9_]+$/i
      };
      return r.patterns = t, r.serializeObject = function() {
        return new r(i, this).addPairs(this.serializeArray()).serialize()
      }, r.serializeJSON = function() {
        return new r(i, this).addPairs(this.serializeArray()).serializeJSON()
      }, "undefined" != typeof i.fn && (i.fn.serializeObject = r.serializeObject, i.fn.serializeJSON = r.serializeJSON), e.FormSerializer = r, r
    });
  </script>
  <script type="text/javascript">
    $(document).ready(function() {
      var braze_internal = $('#braze_internal').remove();
      $('#header_nav').after(braze_internal);
      
      // Handle Form Element visibility
      function toggleFormElements() {
        var selectedValue = $('#doc_urgent').val();
        if (selectedValue === 'suggestion') {
            $('[id^="disclosure"]').show();
            $('[id^="resource_urls"]').hide();
        } else if (selectedValue === 'feature') {
            $('[id^="disclosure"]').hide();
            $('[id^="resource_urls"]').show();
        } else {
            $('[id^="disclosure"]').hide();
            $('[id^="resource_urls"]').hide();
        }
      }
      
      // Show/hide disclosures on page load
      toggleFormElements();
      
      // Show/hide disclosures when selection changes
      $('#doc_urgent').change(function() {
        toggleFormElements();
      });
      
      $('#doc_form').submit(function(e) {
        $('#submit_progress').css('display','inline');
        $('#submit_text').html('Submitting');
        $('#ticket_submit_button').prop("disabled",true);

        e.preventDefault();
        var mform = $(this);
        var url = 'https://c9616da7-4322-4bed-9b51-917c1874fb31.trayapp.io/request';

        var jqxhr = $.ajax({
          url: url,
          method: "GET",
          dataType: "json",
          data: mform.serializeObject()
        }).done(function() {
          $('#doc_div').hide();
          $('#doc_thankyou').show();
          $('#doc_thankyou_msg').fadeTo(800,0,function(){
              $(this).html('<h3>Thanks for your submission!</h3> Someone from our team will contact you if we have any questions. To view the status of your ticket or add comments, check your email for your ticket confirmation.').fadeTo(800,1);
          });
        });

      });

    });
  </script>

<div id="braze_internal" ><i class="fa-solid fa-lock"></i> 内部専用。顧客と共有しないでください。</div>
<div class="container-fluid" id="main-container">

      <div id="doc_div">
        <form id="doc_form">
          <div class="row">
            <div class="col">
              <h1 class="h1">Documentation Request Form</h1>
              <p class="subhead">All fields are required unless otherwise noted.</p>
              <div class="gradient-line"></div>
            </div>
          </div>
          <div class="row">
            <div class="col">
              <input type='hidden' name='Name' value='' />
              <div class="form-group" id="doc_urgent_div">
              <div class="form-check">
                <label class="form-check-label" for="doc_urgent" style="display: block;">
                Request Type
                </label>
              <select id="doc_urgent" name="Request_Type" class="drop-down-sel">
              <option value="urgent">Urgent: I am raising smoke about an issue on Braze Docs or have a high-priority update</option>
              <option value="feature">Feature: I have a new feature or new behavior for an existing feature</option>
              <option value="suggestion" selected="selected">Suggestion: I have a proposed improvement or need clarification for an article</option>
              </select>

              </div>
            
              <div style="height: 12px;"></div>

              <div id="disclosure-warning" class="alert alert-important" role="alert">
                <div class="alert-msg">
                  <b>Important: </b>
                  Copilot will author this suggestion, and it will be reviewed by the Docs team. Confirm that <strong>no customer-specific information</strong> or <strong>links</strong> are included.
                </div>
              </div>
              </div>

              <div class="form-group">
                <label for="doc_due_date" id="doc_due_date_label">Due date (optional)</label>
                <div class="sublabel">If this request is time-sensitive or related to a feature release, please enter a due date.</div>
                <div class="input-group">
                  <input type="date" class="form-control" id="doc_due_date" maxlength="80" name="Due_Date" value="" />
                </div>
              </div>
              <div class="form-group">

                <label for="doc_email" id="doc_email_label">Email address</label>
                <div class="input-group">
                  <input type="email" class="form-control email-input" id="doc_email" maxlength="80" name="Email" placeholder="e.g., firstname.lastname@braze.com" required="required" value="" />
                  <i class="fa-solid fa-envelope email-icon"></i>
                  </div>
              </div>
              <div class="form-group" id="doc_request_div">
                <label for="doc_request" id="doc_request_label">Request summary</label>
                <div class="sublabel">This is the name for your ticket</div>
                <input type="text" name="Request_Subject" id="doc_request" maxlength="180" required="required" value="" placeholder="Enter your request" class="form-control" />
              </div>

              <div class="form-group" id="doc_request_url">
                <label for="doc_request" id="doc_request_url_label">Braze URL</label>
                <input type="url" name="Request_Url" id="doc_request_url" maxlength="180" required="required" value="" placeholder="e.g., https://www.braze.com/docs/" class="form-control" />
              </div>

              <div class="form-group">

                <label for="doc_description" id="doc_description_label" style="margin-bottom:6px;line-height:1.2;">Description</label>
                <div class="sublabel" style="margin-bottom:6px;">Provide as much detail as possible about the requested update.</div>
                <textarea name="Description" class="form-control" id="doc_description" data-toggle="popover" data-trigger="focus" data-placement="top" data-content=""
                  rows="7"></textarea>
              </div>

              <div class="form-group" id="resource_urls">
                <label for="resource_urls" id="resource_urls_label">Resource URLs</label>
                 <div class="sublabel" style="margin-bottom:6px;">Include URLs from Confluence, Productboard, Google Docs, Jira, or any other resources about this feature.</div>
                <textarea name="Resource_Urls" class="form-control" id="resource_urls" data-toggle="popover" data-trigger="focus" data-placement="top" data-content=""
                  rows="2" ></textarea>

              </div>

              <div class="form-group">

                <label for="doc_snippet" id="doc_snippet_label" style="margin-bottom:6px;line-height:1.2;">Code snippets (optional)</label>
                <div class="sublabel" style="margin-bottom:6px;">This is useful if you're a developer. Include context and make sure it's clear what code language is used.</div>
                <textarea name="Snippet" class="form-control" id="doc_snippet" data-toggle="popover" data-trigger="focus" data-placement="top" data-content=""
                  rows="7"></textarea>
              </div>
              <div class="form-group" id="doc_verify_div">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Y" id="doc_verify" name="Verified">
                <label class="form-check-label" for="doc_verify" id="doc_verify_label">
                <span></span> I have verified this information with the respective product team
              </label>
              </div>
              </div>
              <div class="inline_text">
              Please wait up to ten seconds after submitting for your request to process.
              </div>
              <button type="submit" name="Submit Question" value="Submit" class="btn" id="ticket_submit_button" role="button">

              <div id="submit_progress"><div class="lds-ring"><div></div><div></div><div></div><div></div></div></div>
              <div id="submit_text"> Submit Request </div></button>

            </div>

          </div>
        </form>
      </div>


      <div id="doc_thankyou" style="display:none;"><div class="row"><div class="col" id="doc_thankyou_msg"></div></div></div>

    </div>
<br /><br /><br />
