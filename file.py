int numero;
def int fatorial (int fat):
if fat > 1:
print fat;
return fat * fatorial(fat - 1);
} else:
return 1;
}
}
def void resultado (int valor):
print "Resultado: ", valor;
}
main():
 print "Fatorial de N. Digite o número?";
 numero = input();
 resultado (fatorial (numero));

}