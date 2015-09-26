function headTags() {
 tag1=document.createElement('meta');
 tag1.id="viewport";
 tag1.name = "viewport";
 tag1.content = "width=device-width; initial-scale=1.0; user-scalable=true;";
 document.getElementsByTagName('head')[0].appendChild(tag1); 
 tag2=document.createElement('meta');
 tag2.id="HandheldFriendly";
 tag2.name = "HandheldFriendly";
 tag2.content = "true";
 document.getElementsByTagName('head')[0].appendChild(tag2);
}
headTags();

// flash interaction
function getLocation() {
	return window.location.toString();
}

// localization
DecSep = (1.5).toLocaleString().charAt(1);
ThouSep = String.fromCharCode(90 - DecSep.charCodeAt(0));
if (DecSep==",") { DecType = "c"; } else { DecType = ""; }
function decfmt() {
	if (DecSep==",") {
		// 0,00=>0#00 then 0.0=>0,0, then 0#0=>0.0  
		document.body.innerHTML=document.body.innerHTML.replace(/(\d),(\d\d)/g,'$1#$2').replace(/(\d)\.(\d)/g,'$1,$2').replace(/(\d)#(\d)/g,'$1.$2');
		// images replace "." with "c."
		var imgs = document.body.getElementsByTagName("img"); 
		for (var i = 0; i < imgs.length; i++) { 
			if (imgs[i].getAttribute("hasdec")!=null && imgs[i].getAttribute("hasdec")!="") {
				imgs[i].src=imgs[i].src.replace(/\.(gif|jpg|png)/g,"c.$1");
			}
		}
	}
}
function doSpell() {
	var userLang = (navigator.language) ? navigator.language : navigator.userLanguage;
	switch (userLang.toLowerCase()) {
		case "en-us":
			break;
		case "en-au":
		case "en-ca":
		case "en-gb":
		case "en-ie":
		case "en-nz":
		case "en-za":
			var s = document.body.innerHTML;
			for (var i=0; i<reSpell.length; i++) {
				var s0 = reSpell[i][0];
				var s1 = reSpell[i][1];
				s = s.replace(new RegExp('\\b' + s0 + '\\b' , 'g'), s1).replace(new RegExp('\\b' + proper(s0) + '\\b' , 'g'), proper(s1));
			}
			document.body.innerHTML = s;
			break;
		default:
	}
}

function doLocal() { decfmt(); doSpell(); }
if (typeof(hasdec)=='undefined' && typeof(reSpell)=='undefined') {
} else {
	window.onload = doLocal;
}

function proper(s) { return s.charAt(0).toUpperCase() + s.substring(1,s.length).toLowerCase(); }
function tellAFriend() {
	var msg = "\nI found '" + document.title + "' here: " + location.href + "\n";
	window.location = "mailto:?subject="+encodeURIComponent(document.title)+"&body="+encodeURIComponent(msg);
}
function addFavorites() {
	if (window.sidebar) { // Mozilla Firefox Bookmark
		window.sidebar.addPanel( document.title, location.href, "");
	} else if( window.external ) { // IE Favorite
		window.external.AddFavorite( location.href, document.title ); 
	}
}
function openEnglish() {
	if (typeof tranfrom == 'undefined') tranfrom='index.htm';
	var path = tranfrom;  // only relative path to avoid spoofing
	var url = "http://www.mathsisfun.com/" + path;
	window.location = url;
}
function linkToUs() {
	var path = location.pathname + location.search;  // only relative path to avoid spoofing         
	var title = document.title;
	postWith("http://" + document.domain + "/link-to-us.php",{path:path,title:title});
}
function Citation() {
	var months=new Array('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	var path = location.pathname + location.search;  // only relative path to avoid spoofing
	var atitle = document.title;
	var md = new Date(document.lastModified)
	mDate = md.getDate() + " " + months[md.getMonth()] + " " + md.getFullYear();
	if (typeof Author == 'undefined') Author='Pierce, Rod';
	postWith("http://" + document.domain + "/citation.php",{path:path,title:atitle,moddate:mDate,author:Author});
}
function Contribute() {
	var path = location.pathname + location.search;  // only relative path to avoid spoofing
	var atitle = document.title;
	postWith("http://" + document.domain + "/contribute.php",{path:path,title:atitle});
}
function postWith (to,p) {
// from http://mentaljetsam.wordpress.com
	var myForm = document.createElement("form");
	myForm.method="post" ;
	myForm.action = to ;
	for (var k in p) {
		var myInput = document.createElement("input") ;
		myInput.setAttribute("name", k) ;
		myInput.setAttribute("value", p[k]);
		myForm.appendChild(myInput) ;
	}
	document.body.appendChild(myForm) ;
	myForm.submit() ;
	document.body.removeChild(myForm) ;
}

function URLEncode(text) {
	// The Javascript escape and unescape functions do not correspond with what browsers actually do...
	var SAFECHARS = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "-_.!~*'()"; // numeric,alpha, and RFC2396 Mark characters
	var HEX = "0123456789ABCDEF";

	var s = "";
	for (var i=0; i<text.length; i++ ) {
		var ch = text.charAt(i);
	  if (ch == " ") {
		  s += "+";	// x-www-urlencoded, rather than %20
		} else if (SAFECHARS.indexOf(ch) != -1) {
		  s += ch;
		} else {
		  var charCode = ch.charCodeAt(0);
			if (charCode > 255) {  // Unicode cannot be encoded using standard URL encoding
        s += "+";
      } else {
        s += "%";
        s += HEX.charAt((charCode >> 4) & 0xF);
        s += HEX.charAt(charCode & 0xF);
      }
    }
  } 

	return s;
}

function CopyToClipboard(txtArea) {
   txtArea.focus();
   txtArea.select();
   CopiedTxt = document.selection.createRange();
   CopiedTxt.execCommand("Copy");
}

/* Flash */
function getFlash6HTML(w, h, fn, querystring, clr) {
	// w=width, h=height, fn=filename(minus '.swf'), querystring=..., clr=bg color
	if (!querystring) {querystring = "";} else {querystring = "?" +querystring;}
	// default background color
	if (!clr) {clr="#d6d9e6";}

	// append .swf if absent 
	if (fn.substring(fn.lastIndexOf('.swf')) != '.swf') fn = fn + '.swf';

	var s = '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http:\/\/download.macromedia.com\/pub\/shockwave\/cabs\/flash\/swflash.cab#version=6,0,79,0"/n width="' + w + '" height="' + h + '" id="' + fn + '">\n';
 	s += '<param name="movie" value="' + fn + querystring + '"\/> ';
	s += '<param name="quality" value="high"\/> ';
	s += '<param name="bgcolor" value="' + clr + '"\/> ';
	s += '<param name="menu" value="false"\/> ';
	s += '<param name="allowScriptAccess" value="sameDomain"\/> ';
	s += '<param name="allowFullScreen" value="true"\/> ';
	s += '<embed src="' + fn + querystring + '" quality="high" bgcolor="' + clr + '" ';
	s += 'menu="false" width="' + w + '" height="' + h + '" type="application\/x-shockwave-flash" ';
	s += 'pluginspage="http:\/\/www.macromedia.com\/go\/getflashplayer" ';
	s += 'swLiveConnect="true" allowscriptaccess="samedomain" allowFullScreen="true" id="' + fn + '" name="' + fn + '"><noembed><\/noembed><\/embed>\n';
  s += '</object>\n';
	
	return(s);
}
function putFlash6(w, h, fn, querystring, clr, noflash) {
	if (hasFlash()) {
		document.write(getFlash6HTML(w, h, fn, querystring, clr));
 	} else {
		if (noflash) {
			s = noflash;
		} else {
			s = '<a href="/flash-player.html"><img src="/images/style/no-flash.jpg" alt="Needs Flash Player"></a>';
		}
		document.write( s );
	}
}
function hasFlash() {
	try {
		var fo = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
		if(fo) return true;
	} catch(e) {
		if (navigator.mimeTypes && 
			navigator.mimeTypes["application/x-shockwave-flash"] &&
			navigator.mimeTypes["application/x-shockwave-flash"].enabledPlugin)	return true;
	}
	return false;
}
function FlashPHP(w, h, pathtoswf, clr) {
	var path = location.pathname;  
	path = URLEncode(path.substring(0,path.lastIndexOf('/')));
	var atitle = URLEncode(document.title);
	var url = "http://" + document.domain + "/flash.php?path=" + path + "/" + pathtoswf + "&w=" + w + "&h=" + h + "&col=" + URLEncode(clr) + "&title=" + atitle ;
 	window.location = url;
}

/* ads */
var adIDs = Array(Array('topads',1,0), Array('hideads1',1,0), Array('showads1',0,1) );
function sethideadscookie(val) {
  var date = new Date();
  if (val == 1)
		date.setTime(date.getTime()+(1*25*60*60*1000));  // 25 hrs
	else
		date.setTime(date.getTime()-(30*24*60*60*1000));
    document.cookie = "math_hideads="+val+"; expires="+date.toGMTString()+"; path=/";
}

function setAds(stateNo) {
	var styles = Array('none', 'inline');
	for (var i = 0; i < adIDs.length; i++) {
		var e = document.getElementById(adIDs[i][0]);
		if (e) {
			var styleNo = adIDs[i][stateNo];
			if (navigator.userAgent.indexOf('MSIE') > 0) {
				//e.style.setAttribute('csstext', style, 0);
				e.style.display = styles[styleNo];
			} else {
				var style = "display: " + styles[styleNo] + ";";
				e.setAttribute('style', style); 
			}
		}
	}
}

function hideads() {
	sethideadscookie(1);
	setAds(2);
}

function showads() {
	sethideadscookie(0);
	setAds(1);
}

var ca = document.cookie.split(';');

for(var i=0; i<ca.length; i++) {
  var c = ca[i];
  var pair = c.split('=');
  var key = pair[0];
  var value = pair[1];
  key=key.replace(/ /, '');
  if (key == 'math_hideads') {
		if (value == '1') {
			document.write('<style type="text/css" media="screen">#topads { display: none; }\n #hideads1 { display: none; }\n #showads1 { display: inline; }</style>');
		}
  }
}
function printImg(s) {
  pwin = window.open(s,"_blank");
  setTimeout("pwin.print()",2000);
}

/* Question Database */
function doQ(id,qs) {
	var fromPath = location.pathname + location.search;  // only relative path to avoid spoofing
	var url = "http://www.mathopolis.com/questions/q.php?id=" + parseInt(id) + "&site=1" + "&ref=" + fromPath;
	if(typeof qs == 'undefined') {
		url += "&qs=0";
	} else {
		url += "&qs=" + qs;
	}
	window.open(url, "mathopolis");
}
function getQ() {
	var qs = "";
	for( var i = 0; i < arguments.length; i++ ) {
		if (i>0) qs += "_";
		qs += arguments[i];
	}
	var s = "";    
	for( var i = 0; i < arguments.length; i++ ) {
		s += '<a href="javascript:doQ(' + arguments[i] + ",'" + qs + "'" + ')">Question&nbsp;' + (i+1) + '</a> ';
	}
	document.write(s);
}


function getAdRight() {
  var s = "";   
	s += '<div style="margin-left: -425px; width:300px;">'; 
	s += getLinks(true);
  s += '</div>';
  document.write(s);
}
function getAdRight2() {
  var s = getLinks(false);  
  document.write(s);
}
function getLinks(oldQ) {
  //var ffq = false;
	//if (navigator.userAgent.indexOf("Firefox")!=-1) ffq = true;
	//var url    = encodeURIComponent(location.href);
	var url = location.href;   //  safe?
	var title  = encodeURIComponent(document.title);
	var linkstt = '<a target="_blank" href="';
	
  var s = "";    
  s += linkstt + 'http://twitter.com/home?status=' + title + ': ' + url + '" id="linktw">Twitter</a> ';
  s += linkstt + "http://www.stumbleupon.com/submit?url=" + url + "&title=" + title.replace(/%20/g,'+') + '" id="linksu">StumbleUpon</a> ';
	s += linkstt + "http://www.facebook.com/sharer.php?u=" + url + "&t=" + title + '" id="linkfb">Facebook</a> ';
  s += '<a href="javascript:linkToUs()" id="linkus">Link To Us</a>';
  if (oldQ) {
	s += '<div class="g-plusone" data-size="standard" data-href="' + url + '"></div>';
	s += gPlusOneCall();
	} else {
	s += '<div class="g-plusone" data-size="standard" data-href="' + url + '"></div>';   
	}
  return s;
}
function getBodyEnd() {
// delay scripts till end to speed page load (only on templates post June 2011)
  var ffq = false;
	if (navigator.userAgent.indexOf("Firefox")!=-1) ffq = true;

  var s = "";    
		//s += '<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script>';
		s += gPlusOneCall();
		s += gAnalyticsCall();
	if (ffq) {
	} else {
		//s += '<script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script>';    
  }

  document.write(s);
}
function gPlusOneCall() {
// http://www.google.com/webmasters/+1/button/#utm_source=wm&utm_medium=blog&utm_campaign=schema
var s = "";
s += '<script type="text/javascript">';
s += '(function() {';
s += "var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;";
s += "po.src = 'https://apis.google.com/js/plusone.js';";
s += "var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);";
s += '})();';
s += '</script>';
return s;
}
function gAnalyticsCall() {
var s = "";
s += '<script type="text/javascript">';
s += 'var _gaq = _gaq || [];';
s += "_gaq.push(['_setAccount', 'UA-29771508-1']);";
s += "_gaq.push(['_trackPageview']);";
s += '(function() {';
s += "var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;";
s += "ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';";
s += "var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);";
s += '})();';
s += '</script>';
return s;
}