var a = 21;
console.log(a);
console.dir(a);

let n = {
  firstname: "wewe",
  f: "wewe",
};

let g = function (i) {
  console.log(this.a, this.f, this.firstname, i);
};

let n1 = {
  firstname: "weddddwe",
  f: "wwopop",
};

g(432)
g.call(n, 2332);
g.call(n1);
