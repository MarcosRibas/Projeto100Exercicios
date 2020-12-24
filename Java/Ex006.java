/*
Ex006 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
 */
package ex006;

import java.util.Scanner;

public class Ex006 {
   

    public static void main(String[] args) {
    
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um número: ");
        float num = t.nextFloat();
        float dobro = num * 2;
        float triplo = num * 3;
        float raiz = (float) Math.sqrt(num);
        System.out.printf("Você digitou o número: %.0f %n", num);
        System.out.printf("Que quando dobrado fica no valor de: %.0f %n", dobro);
        System.out.printf("E quando triplicado tem o valor de: %.0f %n", triplo);
        System.out.printf("Tendo sua raiz quadrada em %.1f", raiz);
        
    
    }
    
}
