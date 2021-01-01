/*
Ex039 Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar. 
- Se é a hora de se alistar
- Se já passou do tempo de alistamento.
Seu programa deverá mostrar também quanto tempo falta ou que já passou do prazo.
*/
package ex039;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Ex039 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        Date data = new Date();
        SimpleDateFormat x = new SimpleDateFormat("y");
        String y = x.format(data);
        int ano = Integer.parseInt(y);
        System.out.println("Em que ano você nasceu? ");
        int nasc = t.nextInt();
        int idade = ano - nasc;
        int faltam = 18 - idade;
        int passou = idade - 18;
        if (idade == 18){
            System.out.printf("Em %d você completa 18 anos. Precisa se alistar imediatamente\n",ano);
        }
        else if (idade <= 17){
            System.out.printf("Em %d você completa %d anos. Então, ainda faltam %d ano(s) para você se alistar\n", ano, idade, faltam);
        }
        else
        {
            System.out.printf("Em %d você completa %d anos. Deveria ter se alistado a %d ano(s)\n", ano, idade, passou);
        }
        
        

    }
    
}
