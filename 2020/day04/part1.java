import java.util.*;
import java.io.*;

public class part1 {

	static String[] keys = new String[] {
		"byr",
		"iyr",
		"eyr",
		"hgt",
		"hcl",
		"ecl",
		"pid"
	};

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));

		String line;
		long passes = 0;

		String passport = "";
		List<String> passports = new ArrayList<>();

		while ((line = in.readLine()) != null) {
			if (line.equals("") || line.equals("\n")) {
				System.out.println(passport);
				passports.add(passport);
				passport = "";
			}
			else
				passport += line + " ";
		}
		passports.add(passport);

		for (String pass : passports) {
			boolean b = true;
			for (String s : keys) 
				if (!pass.contains(s + ":"))
					b = false;

			if (b) {
				passes++;
			}
		}


		System.out.println(passes);

	}
}