/*
Ex019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do 
escolhido.
 */
package ex019;


import java.util.Scanner;

public class Ex019 {

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
        int s = (int)(Math.random()*3+1);
        switch (s){
            case 1:
                System.out.println("O escolhido foi: " + n1);
                break;
            case 2:
                System.out.println("O escolhido foi: " + n2);
                break;
            case 3:
                System.out.println("O escolhido foi: " + n3);
                break;
            case 4:
                System.out.println("O escolhido foi: " + n4);
            
        }
         

       
        
        
        
        
        
    }
    
}
