/*
Ex034 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais o aumento é de 15%.

 */
package ex034;

import java.util.Scanner;


public class Ex034 {
    
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.print("Valor do salário: R$");
        float sal = t.nextFloat();
        if (sal < 1250){
            sal = sal + (sal * 15 / 100);
        }
        else
        {
            sal = sal + (sal * 10 / 100);
        }
        System.out.printf("O salário com o aumento fica em R$%.2f\n", sal);
    
    }
    
}
