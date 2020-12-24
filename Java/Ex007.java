/*
Ex007 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
 */
package ex007;

import java.util.Scanner;


public class Ex007 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual a dua primeira nota?");
        float n1 = t.nextFloat();
        System.out.println("Qual a sua segunta nota?: ");
        float n2 = t.nextFloat();
        float media = (n1 + n2) / 2;
        System.out.printf("Sua média ficou em: %.1f %n", media);
    
    }
    
}
