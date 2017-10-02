var mime_samples = [
  { 'mime': 'application/javascript', 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/cookie.js', 'dir': '_m0/0', 'linked': 2, 'len': 3423 },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/deep-diff.js', 'dir': '_m0/1', 'linked': 2, 'len': 4966 },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/pixi.js', 'dir': '_m0/2', 'linked': 2, 'len': 303981 },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprintf.js', 'dir': '_m0/3', 'linked': 2, 'len': 3142 },
    { 'url': 'http://shell2017.picoctf.com:16929/server/init.js', 'dir': '_m0/4', 'linked': 1, 'len': 431 },
    { 'url': 'http://shell2017.picoctf.com:16929/server/serv.js', 'dir': '_m0/5', 'linked': 1, 'len': 897 },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/', 'dir': '_m0/6', 'linked': 2, 'len': 40 },
    { 'url': 'http://shell2017.picoctf.com:16929/package.json', 'dir': '_m0/7', 'linked': 1, 'len': 610 } ]
  },
  { 'mime': 'application/xhtml+xml', 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/A', 'dir': '_m1/0', 'linked': 1, 'len': 151 } ]
  },
  { 'mime': 'text/html', 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/', 'dir': '_m2/0', 'linked': 2, 'len': 4818 } ]
  },
  { 'mime': 'text/plain', 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/css/style.css', 'dir': '_m3/0', 'linked': 2, 'len': 6045 },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/jquery.js', 'dir': '_m3/1', 'linked': 5, 'len': 85588 },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/socket.io.js', 'dir': '_m3/2', 'linked': 2, 'len': 72202 } ]
  }
];

var issue_samples = [
  { 'severity': 3, 'type': 40401, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/jquery.js', 'extra': 'Delimited database dump', 'sid': '0', 'dir': '_i0/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/socket.io.js', 'extra': 'Delimited database dump', 'sid': '0', 'dir': '_i0/1' } ]
  },
  { 'severity': 2, 'type': 30701, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/css/style.css', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/1' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/html/', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/2' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/html/index.html', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/3' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/cookie.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/4' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/deep-diff.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/5' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/jquery.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/6' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/pixi.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/7' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprintf.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/8' },
    { 'url': 'http://shell2017.picoctf.com:16929/server/init.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/9' },
    { 'url': 'http://shell2017.picoctf.com:16929/server/serv.js', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/10' },
    { 'url': 'http://shell2017.picoctf.com:16929/package.json', 'extra': 'conflicting \x27Cache-Control\x27 data', 'sid': '0', 'dir': '_i1/11' } ]
  },
  { 'severity': 1, 'type': 20301, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/core', 'extra': '', 'sid': '0', 'dir': '_i2/0' } ]
  },
  { 'severity': 1, 'type': 20101, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/1' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/blur/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/2' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/css/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/3' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/css/style.css/9%201%20-', 'extra': 'SQL injection', 'sid': '0', 'dir': '_i3/4' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/display/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/5' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/filters/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/6' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/html/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/7' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/js/', 'extra': 'inject behavior', 'sid': '0', 'dir': '_i3/8' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/js/animations.js', 'extra': 'during initial resource fetch', 'sid': '0', 'dir': '_i3/9' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/10' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/ascii/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/11' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/bloom/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/12' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/blur/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/13' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/color/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/14' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/convolution/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/15' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/crosshatch/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/16' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/displacement/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/17' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/display/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/18' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/dot/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/19' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/dropshadow/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/20' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/filters/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/21' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/graphics/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/22' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/graphics/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/23' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/gray/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/24' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/gulp/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/25' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/gulp/util/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/26' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/invert/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/27' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/managers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/28' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/middlewares/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/29' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/middlewares/caching/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/30' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/middlewares/parsing/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/31' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/particles/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/32' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/pixelate/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/33' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/34' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/canvas/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/35' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/canvas/utils/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/36' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/37' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/webgl/filters/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/38' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/webgl/managers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/39' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/renderers/webgl/utils/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/40' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/rgb/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/41' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sepia/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/42' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/shapes/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/43' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/shockwave/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/44' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprites/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/45' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprites/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/46' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/src/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/47' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/textures/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/48' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/tiltshift/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/49' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/50' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/cookie.js/`sleep%24{IFS}5`', 'extra': 'Shell injection (spec)', 'sid': '0', 'dir': '_i3/51' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/deep-diff.js/8-7', 'extra': 'SQL injection', 'sid': '0', 'dir': '_i3/52' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprintf.js/\x22`uname`\x22', 'extra': 'Shell injection (diff)', 'sid': '0', 'dir': '_i3/53' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/u.y?width.assign;y=u.width%20u.x;x=u.height%20u.y;p=p', 'extra': 'during parameter brute-force tests', 'sid': '0', 'dir': '_i3/54' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/u.y?s:u.y;y=u.width%20u.x;x=u.height%20u.y;p=`sleep%24{IFS}4`', 'extra': 'Shell injection (spec)', 'sid': '0', 'dir': '_i3/55' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/56' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/canvas/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/57' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/canvas/utils/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/58' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/59' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/webgl/managers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/60' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/renderers/webgl/utils/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/61' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/shaders/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/62' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/textures/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/63' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/core/renderers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/64' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/core/renderers/canvas/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/65' },
    { 'url': 'http://shell2017.picoctf.com:16929/renderers/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/66' },
    { 'url': 'http://shell2017.picoctf.com:16929/renderers/webgl/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/67' },
    { 'url': 'http://shell2017.picoctf.com:16929/renderers/webgl/shaders/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/68' },
    { 'url': 'http://shell2017.picoctf.com:16929/server/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/69' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/FOO-sfi9876', 'extra': 'PUT upload', 'sid': '0', 'dir': '_i3/70' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/socket.io.js/9%201%20-', 'extra': 'SQL injection', 'sid': '0', 'dir': '_i3/71' } ]
  },
  { 'severity': 0, 'type': 10803, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/cookie.js', 'extra': '', 'sid': '0', 'dir': '_i4/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/deep-diff.js', 'extra': '', 'sid': '0', 'dir': '_i4/1' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/jquery.js', 'extra': '', 'sid': '0', 'dir': '_i4/2' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/pixi.js', 'extra': '', 'sid': '0', 'dir': '_i4/3' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/sprintf.js', 'extra': '', 'sid': '0', 'dir': '_i4/4' },
    { 'url': 'http://shell2017.picoctf.com:16929/server/init.js', 'extra': '', 'sid': '0', 'dir': '_i4/5' },
    { 'url': 'http://shell2017.picoctf.com:16929/server/serv.js', 'extra': '', 'sid': '0', 'dir': '_i4/6' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/', 'extra': '', 'sid': '0', 'dir': '_i4/7' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/socket.io.js', 'extra': '', 'sid': '0', 'dir': '_i4/8' },
    { 'url': 'http://shell2017.picoctf.com:16929/package.json', 'extra': '', 'sid': '0', 'dir': '_i4/9' } ]
  },
  { 'severity': 0, 'type': 10601, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/public/lib/jquery.js', 'extra': '', 'sid': '0', 'dir': '_i5/0' } ]
  },
  { 'severity': 0, 'type': 10401, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/', 'extra': '', 'sid': '0', 'dir': '_i6/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/html/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i7/1' } ]
  },
  { 'severity': 0, 'type': 10204, 'samples': [
    { 'url': 'http://shell2017.picoctf.com:16929/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i8/0' },
    { 'url': 'http://shell2017.picoctf.com:16929/public/html/', 'extra': 'X-Content-Type-Options', 'sid': '0', 'dir': '_i8/1' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/', 'extra': 'X-Powered-By', 'sid': '0', 'dir': '_i8/2' },
    { 'url': 'http://shell2017.picoctf.com:16929/socket.io/socket.io.js', 'extra': 'X-SourceMap', 'sid': '0', 'dir': '_i8/3' } ]
  }
];

