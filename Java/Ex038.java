/*
Ex038 Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais. 
*/
package ex038;

import java.util.Scanner;

public class Ex038 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um valor inteiro: ");
        int n1 = t.nextInt();
        System.out.println("Digite outro valor: ");
        int n2 = t.nextInt();
        if (n1 > n2){
            System.out.printf("%d é maior do que %d\n", n1, n2);
        } else if (n2 > n1){
            System.out.printf("%d é maior do que %d\n", n2, n1);
        }
        else
        {
            System.out.println("Os dois valores são iguais");
        }
        
        

    }
    
}
