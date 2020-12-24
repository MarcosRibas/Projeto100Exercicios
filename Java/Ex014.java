/*
Ex014 Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
 */
package ex014;

import java.util.Scanner;

public class Ex014 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual a temperatura atual?(°C)");
        float c = t.nextFloat();
        float f = (float) (c * 9/5) + 32;
        System.out.printf("%.0f°C convertidos ficam em %.1f°F %n",c , f);
        
        

    }
    
}
