/*
Ex035 Desenvolva um programa que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triangulo.
 */
package ex035;

import java.util.Scanner;


public class Ex035 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Analizando triângulos");
        System.out.println("Primeiro segmento: ");
        int s1 = t.nextInt();
        System.out.println("Segundo segmento: ");
        int s2 = t.nextInt();
        System.out.println("Terceiro segmento: ");
        int s3 = t.nextInt();
        if (s1 < s2 + s3 && s2 < s1 + s3 && s3 < s1 + s2){
            System.out.println("Os segmentos acima formam um triângulo");
        }
        else
        {
            System.out.println("Os segmentos acima não formam um triângulo");
        }
    
    }
    
}
