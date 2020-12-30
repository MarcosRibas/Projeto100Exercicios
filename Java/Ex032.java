/*
Ex032 Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
 */
package ex032;

import java.util.Scanner;


public class Ex032 {


    public static void main(String[] args) {
        
        Scanner t = new Scanner(System.in);
        System.out.println("Que ano você quer saber se é bissexto?");
        int ano = t.nextInt();
        if (ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0){
            System.out.printf("O ano %d é bissexto\n",ano);
        }
        else
        {
            System.out.printf("O ano %d não é bissexto\n", ano);
        }        
    
    }
    
}
