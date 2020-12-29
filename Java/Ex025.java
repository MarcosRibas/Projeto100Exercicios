/*
Ex025 Crie um programa que leia o nome de uma pessoa e dia se ela tem ''SILVA'' 
no nome.
 */
package ex025;

import java.util.Scanner;


public class Ex025 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite seu nome: ");
        String nome = t.nextLine().toLowerCase();
        
        if(nome.indexOf("silva")==-1){
            System.out.println("O nome não contém a palvra 'silva'");
        }
        else
        {
            System.out.println("O nome contém a palavra 'silva'");
        }
        
    
    }
    
}
