/*
Ex027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
Último nome separadamente.
Exemplo: Ana Maria de Souza
Primeiro = Ana
Último = Souza

 */
package ex027;

import java.util.Scanner;

public class Ex027 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Digite seu nome completo: ");
        String nome = t.nextLine().strip();
        String []x = nome.split(" ");     
        System.out.println("Seu primeiro nome: " + x[0]);
        System.out.println("Seu ultimo nome: "+ x[x.length-1]);
        
       
        
    
    }
    
}
