/*
Ex022 Crie um programa que leia o nome completo de uma pessoa, e mostre:
O nome com todas as letras maiúsculas:
O nome com todas as letras minúsculas:
Quantas letras ao todo sem considerar espaço:
Quantas letras tem o primeiro nome:

 */
package ex022;

import java.util.Scanner;

public class Ex022 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite seu nome completo: ");
        String nome = t.nextLine().strip();        
        System.out.println("Seu nome com todas as letras em maiúsculo fica: \n"+ nome.toUpperCase());
        System.out.println("Seu nome com todas as letras minúsculas fica: \n" + nome.toLowerCase());
        String []x = nome.split(" ");  
        int tot = x.length-1;
        System.out.println("Quantidade de letras em seu nome completo: "+(nome.length() - tot));
        System.out.println("Quantidade de letras em seu primeiro nome: "+x[0].length());
        
        
    
    }
    
}
