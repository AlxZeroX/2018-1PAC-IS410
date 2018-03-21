public class Test {
	public static void main(String[] args) {
		Pato pato1 = new Pato();
		Pato pato2 = new PatoFalso();

		probar(pato1);
		probar(pato2);
	}

	public static void probar(Pato p) {
		p.graznar();
	}
}