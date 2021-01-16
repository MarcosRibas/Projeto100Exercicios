/*
Ex030 Crie um programa que leia um número inteiro e mostre se ele é PAR ou IMPAR.

 */
package ex030;

import java.util.Scanner;

public class Ex030 {


    public static void main(String[] args) {
    Scanner t = new Scanner(System.in);
        System.out.println("Digite um número inteiro: ");
        int n = t.nextInt();
        int x = n % 2;
        if (x==0){
            System.out.println("O número é par");
        }
        else
        {
            System.out.println("O número é impar");
        }
    }
    
}
