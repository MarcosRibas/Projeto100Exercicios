/*
Ex033 Faça um programa que leia três números e mostre qual é o maior e 
qual é o menor.
 */
package ex033;

import java.util.Scanner;

public class Ex033 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um número: ");
        int n1 = t.nextInt();
        System.out.println("Digite outro número: ");
        int n2 = t.nextInt();
        System.out.println("Digite o ultimo núemro: ");
        int n3 =  t.nextInt();
        int menor = n1;
        int maior = n1;
        if ((n2<n1) && (n2<n3)){
            menor = n2;        
    }
        if ((n3<n1) && (n3<n2)){
            menor = n3;
        }
        if ((n2>n1) && (n2>n3)){
            maior = n2;
        }
        if ((n3>n1) && (n3>n2))
            maior = n3;
        System.out.println("O menor número citado é: "+ menor);
        System.out.println("E o maior número citado é: " + maior);
        
    
    }
    
    
}
