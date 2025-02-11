
var validurls = (typeof validurls === "undefined")  ? {} : validurls;

(function(){


  var urlpath = removeleadingslash(window.location.pathname);

  //lower case name => path name
  function removeleadingslash(str){
    var rstr = str;
    if (rstr.slice(-1) === "/") {
      rstr = rstr.slice(0, -1);
    }
    return rstr;
  }
  function redirecturl(ky,uh,redirect) {
    var val_urls = validurls[ky];
    var hashes = val_urls.split('#');
    var returl = hashes[0] + redirect;
    if (hashes[1]) {
      returl += '#' + hashes[1];
    }
    else if (uh ) {
      returl += '#' + uh;
    }
    return returl;
  }
  var urlhash = window.location.hash;
  var urlsearch = window.location.search;
  var queryparams = getQueryParams();
  var redirected_count = parseInt(query_params.get('redirected'),10) || 0;
  if (!redirected_count) {
    if (urlhash) {
      redirected_count++;
      urlhash = urlhash.replace('#','')
      query_params.set('redirected',redirected_count );
      var redirected  = ((urlsearch.indexOf('?') > -1 ) ? '?' : '&') + query_params.toString();
      if (validurls[urlhash] ) {
        window.location  =  redirecturl(urlhash,urlhash,redirected);
      }
      else {

      }
    }
  }
}  )();
