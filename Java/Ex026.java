/*
Ex026 Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece pela última vez

 */
package ex026;

import java.util.Scanner;

public class Ex026 {


    public static void main(String[] args) {
    Scanner t = new Scanner(System.in);
        System.out.println("Digite uma frase: ");
        String frase = t.nextLine().strip().toLowerCase();
        String [] x = frase.split("a");
        int n_a = x.length-1;
        System.out.println("Sua frase tem " + n_a + " vez(es) a letra A");
        System.out.println("A letra A aparece em sua frase pela vez na " + ((frase.indexOf("a")+1)) +"° posição.");
        System.out.println("A letra A aparece em sua frase pela ultima vez na " + (frase.lastIndexOf("a")-1) + "° posição");
        
    }
    
}
