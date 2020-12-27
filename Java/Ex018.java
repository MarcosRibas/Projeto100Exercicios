/*
Ex018 Faça um programa que leia um ângulo qualquer e mostre na tela o 
valor do seno, cosseno e tangente desse ângulo.
 */
package ex018;

import java.util.Scanner;

public class Ex018 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um ângulo: ");
        double num = t.nextDouble();
        double a = Math.toRadians(num);

        double se = Math.sin(a);
        double co = Math.cos(a);
        double ta = Math.tan(a);
        float b = (float)se;
        float c = (float)co;
        float d = (float)ta;
        System.out.printf("SENO: %.2f \n", b);
        System.out.printf("COSSENO: %.2f \n", c);
        System.out.printf("TANGENTE: %.2f \n", ta);
    
    }
    
}
