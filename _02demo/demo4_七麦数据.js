function o(t) {
    var e, r = +new Date() - (1697 || H) - 1661224081041, a = [];
    var d = 'xyz517cda96abcd'
    a = (0,
        v)(a),
        a = (a += v + t[Jt][T](t[Mt], _)) + (v + r) + (v + 3),
        e = (0,
            v)((0,
            h)(a, d))
    return e
}

function v(t) {
    t = encodeURIComponent().replace(/%([0-9A-F]{2})/g, function (n, t) {
        return o(Y1 + t)
    });
    try {
        return btoa(t)
    } catch (n) {
        return z[W1][K1](t)[U1](Z1)
    }
}

function h(n, t) {
    t = t || u();
    for (var e = (n = n[$1](_))[R], r = t[R], a = q1, i = H; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n[I1](_)
}

t = '/rank/indexPlus/brand_id/1'
console.log(o(t))
