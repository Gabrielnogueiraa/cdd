package aula02;
import java.util.Scanner;

public class desafio01 {
	//lembrar de terminar toda o exercicio 1 dps

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		//aqui começa criando uma varíavel para saer o array
		int[] lista;
		//depois atribui a ele o tamanho que ele vai ter, com o new int
		lista = new int[10];
		//cria um for para ir pedindo imput para o usuário ir digitando os números que ele quer que encha esse array de tamanho 10
		for(int x=0; x <= lista.length -1;x++) {
			System.out.printf("digite o %d numero da lista: ", x + 1);
			lista[x] = scanner.nextInt();
		}
		//e aqui esse for ele só printa o array final
		for(int i=0; i <= lista.length -1; i++) {
			System.out.print(lista[i] + " ");
		}
	}
}