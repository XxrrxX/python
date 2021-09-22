print ("Escoje una opcion para calcular: ");
print("[a] Calcular con minado por dia:");
print("[b] Caular con minado por hora:");
res = str(input("Elije una opcion: "));
while res != "a" and  res != "b":
 print("Opcion: "+res+" no disponible");
 res =  str(input("Elije una opcion valida: "));
if res == "a":
 xd = int(input("Minado por dia: ")); 
 inp = xd;
if res == "b":
 xh = int(input("Minado por hora: "));
 inp = xh;
 xd = xh * 24;
if len(str(inp)) < 9:
 ldinp = 8 - len(str(inp));
 res = "0" * ldinp;
 
print("0."+str(res)+str(inp));

xs = xd * 7;
print("Minado por semana: ");

if len(str(inp)) < 9:
 ldinp = 8 - len(str(xs));
 res = "0" * ldinp;
 print("0."+str(res)+str(xs));

xm = xs * 4;
print("Minado por mes: ");

if len(str(inp)) < 9:
 ldinp = 8 - len(str(xm));
 res = "0" * ldinp;
 print("0."+str(res)+str(xm));

xa = xm * 12;
print("Minado por ano: ");

if len(str(xa)) < 9:
 ldinp = 8 - len(str(xa));
 res = "0" * ldinp;
 print("0."+str(res)+str(xa));


