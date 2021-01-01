/*
Ex036 Escreva um programa para aprovar o empréstimo bancário para a compra de 
uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.
 */
package ex036;

import java.util.Scanner;


public class Ex036 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual o valor da casa? R$");
        float val = t.nextFloat();
        System.out.println("Qual o valor do salário? R$");
        float sal = t.nextFloat();
        System.out.println("Em quantos anos pretende pagar?");
        int anos = t.nextInt();
        float mes = (val / anos) / 12;
        if (mes <= sal * 30 / 100){
            System.out.printf("Empréstimo aprovado! As parcelas serão de R$%.2f", mes);
        }
        else
        {
            System.out.println("Empréstimo negado! As parcelas excedem 30% de seu salário.Tente novamente com um prazo maior");
        }
    
    }
    
}
