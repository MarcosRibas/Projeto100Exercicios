/*
Ex012 Faça um algoritmo que leia o preço de um produto e mostre o seu novo 
preço, com 5% de desconto.
 */
package ex012;

import java.util.Scanner;

public class Ex012 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.print("Qual o valor do produto? R$ ");
        float valor = t.nextFloat();
        float desc = valor - (valor * 5 / 100f);
        System.out.printf("Com o desconto, o valor fica em R$%.2f", desc);
    
    }
    
}
