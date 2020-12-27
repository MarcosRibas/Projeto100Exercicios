/*
Ex020 O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que leia o nome 
dos quatro alunos e mostre a ordem sorteada.
 */
package ex020;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Ex020 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Primeiro nome: ");
        String n1 = t.nextLine();
        System.out.println("Segundo nome: ");
        String n2 = t.nextLine();
        System.out.println("Terceiro nome: ");
        String n3 = t.nextLine();
        System.out.println("Quarto nome: ");
        String n4 = t.nextLine();        
        List<String> lista = Arrays.asList(n1, n2, n3, n4);

        Collections.shuffle(lista); 
        System.out.println("Ordem de apresentação: " + lista);
       



        
        
    
    }
    
}
