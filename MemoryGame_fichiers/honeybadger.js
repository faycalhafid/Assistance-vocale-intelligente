!function(e,t){"use strict";var n={};!function(){var e=document.getElementsByTagName("script"),t=e[e.length-1];if(t)for(var r,o=t.attributes,i=0,a=o.length;i<a;i++)/data-(\w+)$/.test(o[i].nodeName)&&(r=o[i].nodeValue,"false"===r&&(r=!1),n[RegExp.$1]=r)}();var r=function(){var e=t(),r=e(n);return r.factory=e,r};"function"==typeof define&&define.amd?define([],r):"object"==typeof module&&module.exports?module.exports=r():e.Honeybadger=r()}(this,function(){function e(e,t){var n={};for(k in e)n[k]=e[k];for(k in t)n[k]=t[k];return n}function t(e){return!!u&&(u.name===e.name&&(u.message===e.message&&u.stack===e.stack))}function n(e,t){var n=e.message;for(p in t)if(n.match(t[p]))return!0;return!1}function r(){var e={};return e.HTTP_USER_AGENT=navigator.userAgent,document.referrer.match(/\S/)&&(e.HTTP_REFERER=document.referrer),e}function o(e){if("object"==typeof e){var t=[];for(k in e)t.push(k+"="+e[k]);return t.join(";")}}function i(e){return e.stacktrace||e.stack||void 0}function a(e){var t;if(e&&(t=i(e)))return{stack:t,generator:void 0};try{throw new Error("")}catch(e){if(t=i(e))return{stack:t,generator:"throw"}}t=["<call-stack>"];for(var n=arguments.callee;n&&t.length<10;){/function(?:\s+([\w$]+))+\s*\(/.test(n.toString())?t.push(RegExp.$1||"<anonymous>"):t.push("<anonymous>");try{n=n.caller}catch(e){break}}return{stack:t.join("\n"),generator:"walk"}}function c(e,t){var n,r;for(n=0,r=e.length;n<r;n++)if(!1===(0,e[n])(t))return!0;return!1}var u,s,f={name:"honeybadger.js",url:"https://github.com/honeybadger-io/honeybadger-js",version:"0.4.8",language:"javascript"},l=!1,d=!1;return function(p){function g(e){y("debug")&&this.console&&console.log(e)}function y(e,t){var n=H[e];return void 0===n&&(n=H[e.toLowerCase()]),"false"===n&&(n=!1),void 0!==n?n:t}function h(){return"http"+(y("ssl",!0)&&"s"||"")+"://"+y("host","api.honeybadger.io")}function v(e){return!/function|symbol/.test(typeof e)&&("object"!=typeof e||void 0!==e.hasOwnProperty)}function m(e,t,n){var r,o,i,a;if(i=[],n||(n=0),n>=y("max_depth",8))return encodeURIComponent(t)+"=[MAX DEPTH REACHED]";for(r in e)a=e[r],e.hasOwnProperty(r)&&null!=r&&null!=a&&(v(a)||(a=Object.prototype.toString.call(a)),o=t?t+"["+r+"]":r,i.push("object"==typeof a?m(a,o,n+1):encodeURIComponent(o)+"="+encodeURIComponent(a)));return i.join("&")}function b(e){try{return x=new(this.XMLHttpRequest||ActiveXObject)("MSXML2.XMLHTTP.3.0"),x.open("GET",e,y("async",!0)),void x.send()}catch(e){g("Error encountered during XHR request (will retry): "+e)}img=new Image,img.src=e}function w(e){u=s=null;var t=y("apiKey",y("api_key"));return t?(b(h()+"/v1/notices/js.gif?"+m({notice:e})+"&api_key="+t+"&t="+(new Date).getTime()),!0):(g("Unable to send error report: no API key has been configured."),!1)}function E(a,p){if(y("disabled",!1))return!1;if("object"!=typeof a)return!1;if("[object Error]"===Object.prototype.toString.call(a)){var d=a;a=e(a,{name:d.name,message:d.message,stack:i(d)})}if(t(a))return!1;if(s&&l&&w(s),0===function(){var e,t;t=[];for(e in a)({}).hasOwnProperty.call(a,e)&&t.push(e);return t}().length)return!1;if(p&&(a=e(a,p)),n(a,y("ignorePatterns")))return!1;if(c(H.beforeNotifyHandlers,a))return!1;var h=r();"string"==typeof a.cookies?h.HTTP_COOKIE=a.cookies:"object"==typeof a.cookies&&(h.HTTP_COOKIE=o(a.cookies));var v={notifier:f,error:{class:a.name||"Error",message:a.message,backtrace:a.stack,generator:a.generator,fingerprint:a.fingerprint},request:{url:a.url||document.URL,component:a.component||y("component"),action:a.action||y("action"),context:e(H.context,a.context),cgi_data:h,params:a.params},server:{project_root:a.projectRoot||a.project_root||y("projectRoot",y("project_root",window.location.protocol+"//"+window.location.host)),environment_name:a.environment||y("environment")}};return s=v,u=a,l?(g("Deferring notice.",a,v),window.setTimeout(function(){t(a)&&w(v)})):(g("Queuing notice.",a,v),O.push(v)),a}function j(e){return"function"!=typeof Object.isExtensible||Object.isExtensible(e)}function T(e,t){try{return"function"!=typeof e?e:j(e)?(e.___hb||(e.___hb=function(){var n=y("onerror",!0);if(!(L&&(n||t)||t&&!n))return e.apply(this,arguments);try{return e.apply(this,arguments)}catch(e){throw E(e),e}}),e.___hb):e}catch(t){return e}}function _(e,t,n){if(!d&&e&&t&&n){var r=e[t];e[t]=n(r)}}var R=[],O=[],H={context:{},beforeNotifyHandlers:[]};if("object"==typeof p)for(k in p)H[k]=p[k];var L=!0;if(window.atob||(L=!1),window.ErrorEvent)try{0===new window.ErrorEvent("").colno&&(L=!1)}catch(e){}H.notify=function(t,n,r){if(t||(t={}),"[object Error]"===Object.prototype.toString.call(t)){var o=t;t=e(t,{name:o.name,message:o.message,stack:i(o)})}if("object"!=typeof t){t={message:String(t)}}if(n&&"object"!=typeof n){n={name:String(n)}}return n&&(t=e(t,n)),"object"==typeof r&&(t=e(t,r)),E(t,a(t))},H.wrap=function(e){return T(e,!0)},H.setContext=function(t){return"object"==typeof t&&(H.context=e(H.context,t)),H},H.resetContext=function(t){return H.context="object"==typeof t?e({},t):{},H},H.configure=function(e){for(k in e)H[k]=e[k];return H},H.beforeNotify=function(e){return H.beforeNotifyHandlers.push(e),H};var S=[].indexOf||function(e){for(var t=0,n=this.length;t<n;t++)if(t in this&&this[t]===e)return t;return-1};H.reset=function(){H.context={},H.beforeNotifyHandlers=[];for(k in H)-1==S.call(R,k)&&(H[k]=void 0);return H},H.getVersion=function(){return"0.4.8"};var C=function(e){return function(t,n){if("function"==typeof t){var r=Array.prototype.slice.call(arguments,2);return t=T(t),e(function(){t.apply(null,r)},n)}return e(t,n)}};_(window,"setTimeout",C),_(window,"setInterval",C),"EventTarget Window Node ApplicationCache AudioTrackList ChannelMergerNode CryptoOperation EventSource FileReader HTMLUnknownElement IDBDatabase IDBRequest IDBTransaction KeyOperation MediaController MessagePort ModalWindow Notification SVGElementInstance Screen TextTrack TextTrackCue TextTrackList WebSocket WebSocketWorker Worker XMLHttpRequest XMLHttpRequestEventTarget XMLHttpRequestUpload".replace(/\w+/g,function(e){var t=window[e]&&window[e].prototype;t&&t.hasOwnProperty&&t.hasOwnProperty("addEventListener")&&(_(t,"addEventListener",function(e){return function(t,n,r,o){try{n&&null!=n.handleEvent&&(n.handleEvent=T(n.handleEvent))}catch(e){g(e)}return e.call(this,t,T(n),r,o)}}),_(t,"removeEventListener",function(e){return function(t,n,r,o){return e.call(this,t,n,r,o),e.call(this,t,T(n),r,o)}}))}),_(window,"onerror",function(e){function t(e,t,n,r,o){if(!u&&y("onerror",!0)){if(0===n&&/Script error\.?/.test(e))return void g("Ignoring cross-domain script error. Use CORS to enable tracking of these types of errors.");if(g("Error caught by window.onerror"),o)return void E(o);stack=[e,"\n    at ? (",t||"unknown",":",n||0,":",r||0,")"].join(""),E({name:"window.onerror",message:e,stack:stack})}}return function(n,r,o,i,a){return t(n,r,o,i,a),"function"==typeof e&&e.apply(this,arguments)}}),d=!0;for(k in H)R.push(k);if(g("Initializing honeybadger.js 0.4.8"),/complete|interactive|loaded/.test(document.readyState))l=!0,g("honeybadger.js 0.4.8 ready");else{g("Installing ready handler");var I=function(){for(l=!0,g("honeybadger.js 0.4.8 ready");notice=O.pop();)w(notice)};document.addEventListener?document.addEventListener("DOMContentLoaded",I,!0):window.attachEvent("onload",I)}return H}});
//# sourceMappingURL=//js.honeybadger.io/v0.4/honeybadger.min.js.map