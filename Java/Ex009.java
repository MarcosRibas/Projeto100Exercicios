/*
Ex009 Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
 */
package ex009;

import java.util.Scanner;


public class Ex009 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite o número que gostaria de saber a taboada: ");
        int num = t.nextInt();
        int c = 1;
        
        while (c <= 10){
            int r = c * num;
            System.out.println(num + "X" + c + "=" + r);
            c = c + 1;
            
        }
    }
    
}
