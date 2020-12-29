/*
Ex024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou 
não com o nome ''SANTO".
 */
package ex024;

import java.util.Scanner;

public class Ex024 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite o nome da cidade: ");
        String nome = t.nextLine();
        String pnome = nome.toLowerCase();        
        String []x = pnome.split(" ");
        System.out.println(x[0]);

        if("santo".equals(x[0])){
            System.out.println("O nome da cidade começa com a palavra 'santo'");
        }
        else
        {
            System.out.println("O nome da cidade não começa com a palavra 'santo'");
        }
        
    
    }
    
}
