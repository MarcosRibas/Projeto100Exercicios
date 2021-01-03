/*
Ex041 A Confederação Nacional de Natação precisa de um programa que leia o ano 
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: Master
.
 */
package ex041;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;


public class Ex041 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        Date data = new Date();
        SimpleDateFormat x = new SimpleDateFormat("y");
        String y = x.format(data);
        int ano = Integer.parseInt(y);
        System.out.println("Em que ano o atleta nasceu? ");
        int nasc = t.nextInt();
        int idade = ano - nasc; 
        System.out.printf("Em %d o atleta completa %d anos\n", ano, idade);
        if (idade < 9){
            System.out.println("Categoria: MIRIM");
        }
        else if(idade >= 9 && idade < 14){
            System.out.println("Categoria: INFANTIL");
        }
        else if (idade >= 14 && idade < 19){
            System.out.println("Categoria: JUNIOR");
        }
        else if (idade == 19 || idade == 20){
            System.out.println("Categoria: SENIOR");
        }
        else
        {
            System.out.println("Categoria: MASTER");
        }

    }
    
}
