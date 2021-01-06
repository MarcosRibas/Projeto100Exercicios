/*
Ex052 Faça um programa que leia um número inteiro e diga se ele é ou não um 
número primo.
 */
package ex052;

import java.util.Scanner;

public class Ex052 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite o número inteiro que você quer saber se é primo: ");
        int num = t.nextInt();
        int tot = 0;
        for (int c = 0; c <= num; c++){
            if (num % c == 0){
                tot = tot + 1;
            }
        }
        System.out.printf("O número %d foi divido %d vezes", num, tot); 
        if (tot == 2){
            System.out.println("E por isso ele é primo");
        }
        else{
            System.out.println("E por isso ele não é primo");
        }

    }
    
}
