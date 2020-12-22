/*
Ex002 Faça um programa que leia o nome de uma pessoa e 
mostre uma mensagem de boas-vindas.
 */
package ex002;

import java.util.Scanner;

public class Ex002 {


    public static void main(String[] args) {
       Scanner tec = new Scanner(System.in);
        System.out.println("Qual é o seu nome? ");
        String nome = tec.nextLine();
        
        System.out.println("Olá, " + nome + ". Seja bem vindo!");

    }
    
}
