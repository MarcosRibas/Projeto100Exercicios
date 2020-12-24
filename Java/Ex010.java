/*
Ex010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
e mostre quantos Dólares ela pode comprar. Considere o dólar atual
 */
package ex010;

import java.util.Scanner;

public class Ex010 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Quanto de dinheiro você tem em reais? R$");
        float real = t.nextFloat();
        float dolar = real / 5.22f;
        System.out.printf("R$%.2f convertido em dólares fica U$%.2f", real, dolar );
        
        
    
    }
    
}
