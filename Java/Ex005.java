/*
Ex005 Faça um programa que leia um número inteiro e mostre na tela 
o seu sucessor e seu antecessor.
 */
package ex005;

import java.util.Scanner;


public class Ex005 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um número inteiro: ");
        int num = t.nextInt();
        int a = num - 1;
        int s = num + 1;
        System.out.println("O antecessor de " + num + " é: " + a +". E o seu sucessor é: "+s);
    
    }
    
}
