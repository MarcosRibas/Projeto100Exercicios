/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ex042;

import java.util.Scanner;

/**
Ex042 Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
 */
public class Ex042 {

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
            System.out.print("Os segmentos acima formam um triângulo ");
            if (s1 == s2 && s2== s3){
                System.out.println("EQUILÁTERO");
            }
            else if (s1 != s2 && s2 != s3 && s3 != s1){
                System.out.println("ESCALENO");
            }
            else
            {
                System.out.println("ISÓCELES");
            }
        }
        else
        {
            System.out.println("Os segmentos acima não formam um triângulo");
        }
    }
    
}
