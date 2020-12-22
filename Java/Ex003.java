/*
Ex003 Crie um programa que leia dois números e mostre a soma entre eles.
*/
package ex003;

import java.util.Scanner;

public class Ex003 {

    public static void main(String[] args) {
    
    Scanner t = new Scanner(System.in);
        System.out.println("Digite um número: ");
        int n1 = t.nextInt();
        System.out.println("Agora digite outro número: ");
        int n2 = t.nextInt();
        int s = n1 + n2;
        
        System.out.println("A soma entre " + n1 + " e " + n2 + " é " + s);
        
    }
    
}
