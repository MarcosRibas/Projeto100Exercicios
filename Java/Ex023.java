/*
Ex023 Faça um programa que leia um número de 1 a 9999 e mostre na tela cada um dos dígitos separados.
exemplo: digite um número: 1843
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

 */
package ex023;

import java.util.Scanner;

public class Ex023 {

    
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um número de 1 a 9999: ");
        int n = t.nextInt();
        int u = n / 1 % 10;
        int d = n / 10 % 10;
        int c = n / 100 % 10;
        int m = n / 1000 % 10;
        System.out.println("Unidade: "+u);
        System.out.println("Dezena: "+d);
        System.out.println("Centena: "+c);
        System.out.println("Milhar: "+m);
    }
    
}
