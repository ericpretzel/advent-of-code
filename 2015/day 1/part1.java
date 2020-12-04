import java.util.*;
import java.io.*;

public class part1 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));
		String line = in.readLine();

		int floor = 0;
		for (int i = 0; i < line.length(); i++) {
			floor += line.charAt(i) == '(' ? 1 : -1;
		}
		System.out.println(floor);

	}
}