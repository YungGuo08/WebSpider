function hash(_0x2d4d71) {
  var _0x4fa55c = 8;
  var _0x47edc1 = 0;

  function _0x2c9622(_0x29359d, _0x4ae66f) {
    var _0xb605c0 = (_0x29359d & 65535) + (_0x4ae66f & 65535);

    var _0x27744e = (_0x29359d >> 16) + (_0x4ae66f >> 16) + (_0xb605c0 >> 16);

    return _0x27744e << 16 | _0xb605c0 & 65535;
  }

  function _0x19c666(_0xf7e020, _0x235055) {
    return _0xf7e020 >>> _0x235055 | _0xf7e020 << 32 - _0x235055;
  }

  function _0x436381(_0xd2ec5, _0x5c392d) {
    return _0xd2ec5 >>> _0x5c392d;
  }

  function _0x3f7e6a(_0x3df6f9, _0xb07891, _0x43446d) {
    return _0x3df6f9 & _0xb07891 ^ ~_0x3df6f9 & _0x43446d;
  }

  function _0x20e775(_0x51df81, _0xeeb3b4, _0x2ebd5f) {
    return _0x51df81 & _0xeeb3b4 ^ _0x51df81 & _0x2ebd5f ^ _0xeeb3b4 & _0x2ebd5f;
  }

  function _0x5450df(_0x155ce6) {
    return _0x19c666(_0x155ce6, 2) ^ _0x19c666(_0x155ce6, 13) ^ _0x19c666(_0x155ce6, 22);
  }

  function _0x2d51c9(_0xc877f4) {
    return _0x19c666(_0xc877f4, 6) ^ _0x19c666(_0xc877f4, 11) ^ _0x19c666(_0xc877f4, 25);
  }

  function _0x515e90(_0x16cf8f) {
    return _0x19c666(_0x16cf8f, 7) ^ _0x19c666(_0x16cf8f, 18) ^ _0x436381(_0x16cf8f, 3);
  }

  function _0x57905d(_0x9b4d6e) {
    return _0x19c666(_0x9b4d6e, 17) ^ _0x19c666(_0x9b4d6e, 19) ^ _0x436381(_0x9b4d6e, 10);
  }

  function _0x7dfc8(_0x10a4b0, _0x43831c) {
    var _0x1d2989 = new Array(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298);

    var _0x5cb44b = new Array(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225);

    var _0x5a20f0 = new Array(64);

    var _0x218e05, _0xe3c1e2, _0x107c4d, _0xf15343, _0x4e8165, _0x3d523b, _0x5552b2, _0x55b2d5, _0x8b0131, _0x4adfc9;

    var _0x92e82e, _0x281f56;

    _0x10a4b0[_0x43831c >> 5] |= 128 << 24 - _0x43831c % 32;
    _0x10a4b0[(_0x43831c + 64 >> 9 << 4) + 15] = _0x43831c;

    for (var _0x8b0131 = 0; _0x8b0131 < _0x10a4b0["length"]; _0x8b0131 += 16) {
      _0x218e05 = _0x5cb44b[0];
      _0xe3c1e2 = _0x5cb44b[1];
      _0x107c4d = _0x5cb44b[2];
      _0xf15343 = _0x5cb44b[3];
      _0x4e8165 = _0x5cb44b[4];
      _0x3d523b = _0x5cb44b[5];
      _0x5552b2 = _0x5cb44b[6];
      _0x55b2d5 = _0x5cb44b[7];

      for (var _0x4adfc9 = 0; _0x4adfc9 < 64; _0x4adfc9++) {
        if (_0x4adfc9 < 16) {
          _0x5a20f0[_0x4adfc9] = _0x10a4b0[_0x4adfc9 + _0x8b0131];
        } else {
          _0x5a20f0[_0x4adfc9] = _0x2c9622(_0x2c9622(_0x2c9622(_0x57905d(_0x5a20f0[_0x4adfc9 - 2]), _0x5a20f0[_0x4adfc9 - 7]), _0x515e90(_0x5a20f0[_0x4adfc9 - 15])), _0x5a20f0[_0x4adfc9 - 16]);
        }

        _0x92e82e = _0x2c9622(_0x2c9622(_0x2c9622(_0x2c9622(_0x55b2d5, _0x2d51c9(_0x4e8165)), _0x3f7e6a(_0x4e8165, _0x3d523b, _0x5552b2)), _0x1d2989[_0x4adfc9]), _0x5a20f0[_0x4adfc9]);
        _0x281f56 = _0x2c9622(_0x5450df(_0x218e05), _0x20e775(_0x218e05, _0xe3c1e2, _0x107c4d));
        _0x55b2d5 = _0x5552b2;
        _0x5552b2 = _0x3d523b;
        _0x3d523b = _0x4e8165;
        _0x4e8165 = _0x2c9622(_0xf15343, _0x92e82e);
        _0xf15343 = _0x107c4d;
        _0x107c4d = _0xe3c1e2;
        _0xe3c1e2 = _0x218e05;
        _0x218e05 = _0x2c9622(_0x92e82e, _0x281f56);
      }

      _0x5cb44b[0] = _0x2c9622(_0x218e05, _0x5cb44b[0]);
      _0x5cb44b[1] = _0x2c9622(_0xe3c1e2, _0x5cb44b[1]);
      _0x5cb44b[2] = _0x2c9622(_0x107c4d, _0x5cb44b[2]);
      _0x5cb44b[3] = _0x2c9622(_0xf15343, _0x5cb44b[3]);
      _0x5cb44b[4] = _0x2c9622(_0x4e8165, _0x5cb44b[4]);
      _0x5cb44b[5] = _0x2c9622(_0x3d523b, _0x5cb44b[5]);
      _0x5cb44b[6] = _0x2c9622(_0x5552b2, _0x5cb44b[6]);
      _0x5cb44b[7] = _0x2c9622(_0x55b2d5, _0x5cb44b[7]);
    }

    return _0x5cb44b;
  }

  function _0x180a16(_0xf1fd6e) {
    var _0xb0db85 = Array();

    var _0x25f9c5 = 255;

    for (var _0x2f8e7d = 0; _0x2f8e7d < _0xf1fd6e["length"] * _0x4fa55c; _0x2f8e7d += _0x4fa55c) {
      _0xb0db85[_0x2f8e7d >> 5] |= (_0xf1fd6e["charCodeAt"](_0x2f8e7d / _0x4fa55c) & _0x25f9c5) << 24 - _0x2f8e7d % 32;
    }

    return _0xb0db85;
  }

  function _0x46ee98(_0x58c977) {
    var _0x85a9a = new RegExp("\n", "g");

    _0x58c977 = _0x58c977["replace"](_0x85a9a, "\n");
    var _0x4bca3a = "";

    for (var _0x1e7342 = 0; _0x1e7342 < _0x58c977["length"]; _0x1e7342++) {
      var _0x5c7a8b = _0x58c977["charCodeAt"](_0x1e7342);

      if (_0x5c7a8b < 128) {
        _0x4bca3a += String["fromCharCode"](_0x5c7a8b);
      } else {
        if (_0x5c7a8b > 127 && _0x5c7a8b < 2048) {
          _0x4bca3a += String["fromCharCode"](_0x5c7a8b >> 6 | 192);
          _0x4bca3a += String["fromCharCode"](_0x5c7a8b & 63 | 128);
        } else {
          _0x4bca3a += String["fromCharCode"](_0x5c7a8b >> 12 | 224);
          _0x4bca3a += String["fromCharCode"](_0x5c7a8b >> 6 & 63 | 128);
          _0x4bca3a += String["fromCharCode"](_0x5c7a8b & 63 | 128);
        }
      }
    }

    return _0x4bca3a;
  }

  function _0x5fb598(_0x580622) {
    var _0x11d2a4 = "0123456789abcdef";
    var _0x180550 = "";

    for (var _0x11bebf = 0; _0x11bebf < _0x580622["length"] * 4; _0x11bebf++) {
      _0x180550 += _0x11d2a4["charAt"](_0x580622[_0x11bebf >> 2] >> (3 - _0x11bebf % 4) * 8 + 4 & 15) + _0x11d2a4["charAt"](_0x580622[_0x11bebf >> 2] >> (3 - _0x11bebf % 4) * 8 & 15);
    }

    return _0x180550;
  }

  _0x2d4d71 = _0x46ee98(_0x2d4d71);
  return _0x5fb598(_0x7dfc8(_0x180a16(_0x2d4d71), _0x2d4d71["length"] * _0x4fa55c));
}

function go(_0x50e72d) {
  
  var _0x30800c = new Date();

  function _0x4d3c6a(_0x51f750, _0x2cc5b7) {
    var _0x5f4776 = _0x50e72d["chars"]["length"];

    for (var _0x2066c1 = 0; _0x2066c1 < _0x5f4776; _0x2066c1++) {
      for (var _0x1fda25 = 0; _0x1fda25 < _0x5f4776; _0x1fda25++) {
        var _0x446909 = _0x2cc5b7[0] + _0x50e72d["chars"]["substr"](_0x2066c1, 1) + _0x50e72d["chars"]["substr"](_0x1fda25, 1) + _0x2cc5b7[1];

        if (hash(_0x446909) == _0x51f750) {
          return [_0x446909, new Date() - _0x30800c];
        }
      }
    }
  }

  var _0xfe7727 = _0x4d3c6a(_0x50e72d["ct"], _0x50e72d["bts"]);

  if (_0xfe7727) {
    var _0x6eaa1f;

    if (_0x50e72d["wt"]) {
      _0x6eaa1f = parseInt(_0x50e72d["wt"]) > _0xfe7727[1] ? parseInt(_0x50e72d["wt"]) - _0xfe7727[1] : 500;
    } else {
      _0x6eaa1f = 1500;
    }

    
    return _0x50e72d["tn"] + "=" + _0xfe7727[0] + ";Max-age=" + _0x50e72d["vt"] + "; path = /";
    
  }
}
