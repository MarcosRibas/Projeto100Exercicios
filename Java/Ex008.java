/*
Ex008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 
 */
package ex008;

import java.util.Scanner;

public class Ex008 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite um valor em metros: ");
        int m = t.nextInt();
        int cm = m * 100;
        int mm = m * 1000;
        System.out.println(m + "m convertidos para centimetros fica: " + cm +"cm");
        System.out.println("E convertido para milimitros fica: " + mm + "mm");
    
    }
    
}
