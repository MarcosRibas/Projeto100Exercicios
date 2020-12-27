/*
Ex017 Crie um programa que leia o comprimento do cateto oposto e do cateto 
adjacente de um triângulo retângulo, calcule e mostre o comprimento da 
hipotenusa.
 */
package ex017;


import java.util.Scanner;

public class Ex017 {

    public static void main(String[] args) {
        
        Scanner t = new Scanner(System.in);
        System.out.println("Comprimento do cateto oposto: ");
        float co = t.nextFloat();
        System.out.println("Comprimento do cateto adjacente: ");
        float ca = t.nextFloat();
        float num = (co * co) + (ca * ca);
        float hi = (float) Math.sqrt(num);
        System.out.printf("A hipotenusa é %.1f \n", hi);
    
    
    }
    
}
