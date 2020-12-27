/*
Ex016 Crie um programa que leia um número Real qualquer pelo teclado e mostre 
na tela a sua porção inteira.

 */
package ex016;

import java.util.Scanner;

public class Ex016 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um número real: ");
        float a = t.nextFloat();
        int b = (int)a;
       
        System.out.println("a porção inteira do valor digitado é " + b);
    
    }
    
}
