/*
Ex013 Faça um algoritmo que leia o salário de um funcionário e mostre 
seu novo salário, com 15% de aumento.
 */
package ex013;

import java.util.Scanner;


public class Ex013 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual é o salario atual? R$");
        float sal = t.nextFloat();
        float aum = (float) sal + (sal * 15 / 100);
        System.out.printf("Com o aumento o salário fica em R$%.2f", aum);
    
    }
    
}
