/*
Ex011 Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo 
que cada litro de tinta pinta a área de 2m².
 */
package ex011;

import java.util.Scanner;


public class Ex011 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual a largura de sua parede?");
        float l = (float)t.nextFloat();
        System.out.println("Qual a altura de sua parede?");
        float a = (float) t.nextFloat();
        float q = l * a;
        float litros = q / 2;
        System.out.printf("Sua parede tem %.2f m². Então você vai precisar de %.1f litros para pinta-la", q, litros);
        
    
    }
    
}
