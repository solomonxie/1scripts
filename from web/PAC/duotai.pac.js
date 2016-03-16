function Custom(o, e) {}
var direct = "DIRECT;",
proxy = "PROXY hyatt.krv3-h.xduotai.com:11536;",
exits = [direct, proxy, "PROXY hyatt.g.xduotai.com:11536;"],
Domains = function() {
	var o = {};
	return function(e, c) {
		var m;
		do {
			if (o.hasOwnProperty(c)) return exits[o[c]];
			m = c.indexOf(".") + 1, c = c.slice(m)
		} while ( m >= 1 )
	}
} (),
routes = [];
routes.push(Domains);
function FindProxyForURL(r, t) {
	for (var e = 0; e < routes.length; ++e) if (route = routes[e](r, t), route) return route;
	return direct
}