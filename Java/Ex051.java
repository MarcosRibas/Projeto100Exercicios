/*
Ex051 Desenvolva um programa que leia o primeiro termo e a razão de uma 
Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.
 */
package ex051;

import java.util.Scanner;

public class Ex051 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("---PROGRESSÃO ARITMÉTICA---");
        System.out.println("Primeiro termo: ");
        int termo = t.nextInt();
        System.out.println("Razão: ");
        int razao = t.nextInt();
        for (int c = termo; c <=10; c+=razao)            
            System.out.println(c);
            
        

    }
    
}
