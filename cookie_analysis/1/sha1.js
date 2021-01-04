function hash(_0x598fff) {
  var _0x49b45e = 8;
  var _0x24cbeb = 0;

  function _0x1e2c4a(_0x22d2f0, _0x279b20) {
    var _0x4cfd21 = (_0x22d2f0 & 65535) + (_0x279b20 & 65535);

    var _0x328847 = (_0x22d2f0 >> 16) + (_0x279b20 >> 16) + (_0x4cfd21 >> 16);

    return _0x328847 << 16 | _0x4cfd21 & 65535;
  }

  function _0x1e5263(_0x39c4e1, _0x4daf38) {
    return _0x39c4e1 >>> _0x4daf38 | _0x39c4e1 << 32 - _0x4daf38;
  }

  function _0x30cd19(_0x47776a, _0x5d77bc) {
    return _0x47776a >>> _0x5d77bc;
  }

  function _0x30c57c(_0x33afb8, _0x9b5e13, _0x250600) {
    return _0x33afb8 & _0x9b5e13 ^ ~_0x33afb8 & _0x250600;
  }

  function _0x52ab50(_0x44fb21, _0x5e23f1, _0x207702) {
    return _0x44fb21 & _0x5e23f1 ^ _0x44fb21 & _0x207702 ^ _0x5e23f1 & _0x207702;
  }

  function _0x168be7(_0x32dd62) {
    return _0x1e5263(_0x32dd62, 2) ^ _0x1e5263(_0x32dd62, 13) ^ _0x1e5263(_0x32dd62, 22);
  }

  function _0x1268dc(_0x35c727) {
    return _0x1e5263(_0x35c727, 6) ^ _0x1e5263(_0x35c727, 11) ^ _0x1e5263(_0x35c727, 25);
  }

  function _0x52baa8(_0x48259e) {
    return _0x1e5263(_0x48259e, 7) ^ _0x1e5263(_0x48259e, 18) ^ _0x30cd19(_0x48259e, 3);
  }

  function _0x3ff1a3(_0x12bd2d) {
    return _0x1e5263(_0x12bd2d, 17) ^ _0x1e5263(_0x12bd2d, 19) ^ _0x30cd19(_0x12bd2d, 10);
  }

  function _0x5c597b(_0x36294a, _0x1dd99a) {
    var _0x5a0c84 = new Array(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298);

    var _0x6c9bea = new Array(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225);

    var _0xc3c450 = new Array(64);

    var _0x373692, _0x3f68cd, _0x87a717, _0xb248f7, _0x3bf938, _0x20e59a, _0x4d419c, _0x2c7256, _0x40b379, _0x41163b;

    var _0x4fdc54, _0x4adea3;

    _0x36294a[_0x1dd99a >> 5] |= 128 << 24 - _0x1dd99a % 32;
    _0x36294a[(_0x1dd99a + 64 >> 9 << 4) + 15] = _0x1dd99a;

    for (var _0x40b379 = 0; _0x40b379 < _0x36294a["length"]; _0x40b379 += 16) {
      _0x373692 = _0x6c9bea[0];
      _0x3f68cd = _0x6c9bea[1];
      _0x87a717 = _0x6c9bea[2];
      _0xb248f7 = _0x6c9bea[3];
      _0x3bf938 = _0x6c9bea[4];
      _0x20e59a = _0x6c9bea[5];
      _0x4d419c = _0x6c9bea[6];
      _0x2c7256 = _0x6c9bea[7];

      for (var _0x41163b = 0; _0x41163b < 64; _0x41163b++) {
        if (_0x41163b < 16) {
          _0xc3c450[_0x41163b] = _0x36294a[_0x41163b + _0x40b379];
        } else {
          _0xc3c450[_0x41163b] = _0x1e2c4a(_0x1e2c4a(_0x1e2c4a(_0x3ff1a3(_0xc3c450[_0x41163b - 2]), _0xc3c450[_0x41163b - 7]), _0x52baa8(_0xc3c450[_0x41163b - 15])), _0xc3c450[_0x41163b - 16]);
        }

        _0x4fdc54 = _0x1e2c4a(_0x1e2c4a(_0x1e2c4a(_0x1e2c4a(_0x2c7256, _0x1268dc(_0x3bf938)), _0x30c57c(_0x3bf938, _0x20e59a, _0x4d419c)), _0x5a0c84[_0x41163b]), _0xc3c450[_0x41163b]);
        _0x4adea3 = _0x1e2c4a(_0x168be7(_0x373692), _0x52ab50(_0x373692, _0x3f68cd, _0x87a717));
        _0x2c7256 = _0x4d419c;
        _0x4d419c = _0x20e59a;
        _0x20e59a = _0x3bf938;
        _0x3bf938 = _0x1e2c4a(_0xb248f7, _0x4fdc54);
        _0xb248f7 = _0x87a717;
        _0x87a717 = _0x3f68cd;
        _0x3f68cd = _0x373692;
        _0x373692 = _0x1e2c4a(_0x4fdc54, _0x4adea3);
      }

      _0x6c9bea[0] = _0x1e2c4a(_0x373692, _0x6c9bea[0]);
      _0x6c9bea[1] = _0x1e2c4a(_0x3f68cd, _0x6c9bea[1]);
      _0x6c9bea[2] = _0x1e2c4a(_0x87a717, _0x6c9bea[2]);
      _0x6c9bea[3] = _0x1e2c4a(_0xb248f7, _0x6c9bea[3]);
      _0x6c9bea[4] = _0x1e2c4a(_0x3bf938, _0x6c9bea[4]);
      _0x6c9bea[5] = _0x1e2c4a(_0x20e59a, _0x6c9bea[5]);
      _0x6c9bea[6] = _0x1e2c4a(_0x4d419c, _0x6c9bea[6]);
      _0x6c9bea[7] = _0x1e2c4a(_0x2c7256, _0x6c9bea[7]);
    }

    return _0x6c9bea;
  }

  function _0x233cde(_0xa4db63) {
    var _0x150ea6 = Array();

    var _0x4a31ad = 255;

    for (var _0x381bf0 = 0; _0x381bf0 < _0xa4db63["length"] * _0x49b45e; _0x381bf0 += _0x49b45e) {
      _0x150ea6[_0x381bf0 >> 5] |= (_0xa4db63["charCodeAt"](_0x381bf0 / _0x49b45e) & _0x4a31ad) << 24 - _0x381bf0 % 32;
    }

    return _0x150ea6;
  }

  function _0x53d701(_0x334568) {
    var _0x5aaafa = new RegExp("\n", "g");

    _0x334568 = _0x334568["replace"](_0x5aaafa, "\n");
    var _0xfe4485 = "";

    for (var _0x2d348e = 0; _0x2d348e < _0x334568["length"]; _0x2d348e++) {
      var _0x28ae49 = _0x334568["charCodeAt"](_0x2d348e);

      if (_0x28ae49 < 128) {
        _0xfe4485 += String["fromCharCode"](_0x28ae49);
      } else {
        if (_0x28ae49 > 127 && _0x28ae49 < 2048) {
          _0xfe4485 += String["fromCharCode"](_0x28ae49 >> 6 | 192);
          _0xfe4485 += String["fromCharCode"](_0x28ae49 & 63 | 128);
        } else {
          _0xfe4485 += String["fromCharCode"](_0x28ae49 >> 12 | 224);
          _0xfe4485 += String["fromCharCode"](_0x28ae49 >> 6 & 63 | 128);
          _0xfe4485 += String["fromCharCode"](_0x28ae49 & 63 | 128);
        }
      }
    }

    return _0xfe4485;
  }

  function _0x46713f(_0x4f4b2f) {
    var _0x586e90 = "0123456789abcdef";
    var _0xfa0926 = "";

    for (var _0x3fc4b8 = 0; _0x3fc4b8 < _0x4f4b2f["length"] * 4; _0x3fc4b8++) {
      _0xfa0926 += _0x586e90["charAt"](_0x4f4b2f[_0x3fc4b8 >> 2] >> (3 - _0x3fc4b8 % 4) * 8 + 4 & 15) + _0x586e90["charAt"](_0x4f4b2f[_0x3fc4b8 >> 2] >> (3 - _0x3fc4b8 % 4) * 8 & 15);
    }

    return _0xfa0926;
  }

  _0x598fff = _0x53d701(_0x598fff);
  return _0x46713f(_0x5c597b(_0x233cde(_0x598fff), _0x598fff["length"] * _0x49b45e));
}

function go(data) {
    var chars = data["chars"]["length"];
    for (var i = 0; i < chars; i++) {
      for (var j = 0; j < chars; j++) {
        var cookie = data["bts"][0] + data["chars"]["substr"](i, 1) + data["chars"]["substr"](j, 1) + data["bts"][1];
        if (hash(cookie) == data["ct"]) {
          return cookie;
        }
      }
    }
}


