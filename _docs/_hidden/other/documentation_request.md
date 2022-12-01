---
nav_title: Documentation Request
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
  #main-container {
    margin-top: 20px;
  }
  #main-container label {
    font-weight: bold;
    font-size: 18px;
  }

  .container {
    margin-top: 40px;
  }


  .popover{
    max-width: 95%;
    min-width: 350px;
  }


  .container-fluid {
    max-width: 820px;
  }
  .header {
    margin-top: 20px;
    margin-left: 5%;
  }
  .header .navbar-brand img {
      max-width: none;
      width: 112px;
      height: 51px;
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
    #doc_pm_label {
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
    .request_info {
      display: flex;
      -webkit-box-align: stretch;
      align-items: stretch;
      -webkit-box-pack: justify;
      justify-content: space-between;
      min-height: 38px;
      font-family: Sailec W00 Bold, Arial, sans-serif;
      font-size: 12px;
      background-color: rgb(255, 255, 255);
      border-width: 1px 1px 1px 8px;
      border-style: solid;
      border-image: initial;
      border-radius: 3px;
      padding: 6px 12px 6px 36px;
      border-color: rgb(13, 175, 197);
      margin-bottom: 24px;
      background-image: url("data:image/png;base64,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");
      background-repeat: no-repeat;
      background-position-y: center;
      background-position-x: 6px;
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
      $('#doc_form').submit(function(e) {
        $('#submit_progress').css('display','inline');
        $('#submit_text').html('Submitting');
        $('#ticket_submit_button').prop("disabled",true);

        e.preventDefault();

        $('#doc_thankyou').fadeIn("slow");
        $('#doc_thankyou_msg').html('<h3>Please wait, your request is being processed.</h3>');

        var mform = $(this);
        e.preventDefault();
        $('#doc_div').hide();
        var url = 'https://script.google.com/macros/s/AKfycbzDu2Q-VK18apU8-UAMEQFGteT-MuD5b648QWiE-MvmN99XfyBm/exec';

        var jqxhr = $.ajax({
          url: url,
          method: "GET",
          dataType: "json",
          data: mform.serializeObject()
        }).done(function() {
          $('#doc_thankyou_msg').fadeTo(3200,0,function(){
              $(this).html('<h3>Thanks for your submission!</h3> Somebody should reach out to you shortly.').fadeTo(3200,1);
          });
        });

      });
    });
  </script>




<div class="container-fluid" id="main-container">

      <div id="doc_div">
        <form id="doc_form">
          <div class="row">
            <div class="col">
              <h1 class="h1">Documentation Request Form</h1>
              <p class="subhead">Internal only. All fields are required unless otherwise noted.</p>

                  <div class="gradient-line"></div>
            </div>
          </div>
          <div class="row">
            <div class="col">


              <div class="form-group" id="doc_name_div">
                <label for="doc_name" id="doc_name_label">Name</label>
                <input type="text" name="Name" id="doc_name" maxlength="80" required="required" value="" placeholder="Enter your name" class="form-control" />
              </div>
              <div class="form-group" id="doc_pm_div">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Y" id="doc_is_pm" name="Request_Is_PM">
                <label class="form-check-label" for="doc_is_pm" id="doc_pm_label">
                <span></span> I'm a product manager
              </label>
              </div>
              </div>
              <div class="form-group">

                <label for="doc_email" id="doc_email_label">Email address</label>
                <div class="input-group">
                  <input type="email" class="form-control email-input" id="doc_email" maxlength="80" name="Email" placeholder="e.g. firstname.lastname@braze.com" required="required" value="" />
                  <i class="fa-solid fa-envelope email-icon"></i>
                  </div>
              </div>
              <div class="form-group" id="doc_request_div">
                <label for="doc_request" id="doc_request_label">Request summary</label>
                <div class="sublabel">This is the name for your ticket</div>
                <input type="text" name="Request_Subject" id="doc_request" maxlength="180" required="required" value="" placeholder="Enter your request" class="form-control" />
              </div>

              <div class="form-group" id="doc_urgent_div">
              <div class="form-check">
                <label class="form-check-label" for="doc_urgent" style="display: block;">
                Priority
                </label>
              <select id="doc_urgent" name="Request_Urgent" class="drop-down-sel">
              <option value="urgent">Urgent — There’s an urgent problem that is immediately blocking my work</option>
              <option value="major">Major — There’s a major issue and I can’t find a workaround</option>
              <option value="minor" selected="selected">Minor — There’s a minor issue but I have a workaround</option>
              <option value="trivial" selected="selected">Trivial — I have a question or suggestion</option>
              </select>

              </div>
              </div>



              <div class="form-group">

                <label for="doc_description" id="doc_description_label" style="margin-bottom:6px;line-height:1.2;">Description</label>
                <div class="sublabel">What needs to be done for you to consider this request complete? Include links to any resources such as drive folders of images, relevant Slack threads, Confluence articles, and any relevant links that might need to be included in the documentation.</div>
                <textarea name="Description" class="form-control" id="doc_description" data-toggle="popover" data-trigger="focus" data-placement="top" data-content=""
                  rows="7"></textarea>
              </div>

              <div class="form-group">

                <label for="doc_snippet" id="doc_snippet_label" style="margin-bottom:6px;line-height:1.2;">Code snippets (optional)</label>
                <div class="sublabel" style="margin-bottom:6px;">This is useful if you’re a developer. Include context and make sure it’s clear what code language is used.</div>
                <textarea name="Snippet" class="form-control" id="doc_snippet" data-toggle="popover" data-trigger="focus" data-placement="top" data-content=""
                  rows="7"></textarea>
              </div>

              <div class="request_info">Please wait up to ten seconds after submitting for your request to process.</div>

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
