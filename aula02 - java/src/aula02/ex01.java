package aula02;

public class ex01 {
	public static void main(String[] args) {
		int intarray[] = {2,5,46,12,34};
		
		for(int x=0; x<intarray.length; x++) {
			System.out.print(intarray[x]+" ");
		}
		
		System.out.println(" ");
		
		for(int x=4; x >= 0; x--) {
			System.out.print(intarray[x]+" ");
		}
	}
}
