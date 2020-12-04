import java.util.*;
import java.io.*;

public class part2 {

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

		StringBuilder passport = new StringBuilder();
		List<String> passports = new ArrayList<>();

		while ((line = in.readLine()) != null) {
			if (line.equals("") || line.equals("\n")) {
				passports.add(passport.toString());
				passport = new StringBuilder();
			}
			else
				passport.append(" ").append(line).append(" ");
		}
		passports.add(passport.toString());

		for (String pass : passports) {
			boolean valid = true;
			for (String s : keys)
				if (!pass.contains(s + ":")) {
					valid = false;
					break;
				}

			Scanner sc = new Scanner(pass);



			while (valid && sc.hasNext()) {
				String input = sc.next();
				System.out.println(input);

				if (!handleInput(input.substring(0,3), input.substring(4))) {
					valid = false;
					break;
				}
			}
			passes += valid ? 1 : 0;
		}


		System.out.println(passes);

	}


	static boolean handleInput(String key, String content) {
		try {
			switch (key) {
				case "byr":
					int byr = Integer.parseInt(content);
					if (byr < 1920 || byr > 2002) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
				case "iyr":
					int iyr = Integer.parseInt(content);
					if (iyr < 2010 || iyr > 2020) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
				case "eyr":
					int eyr = Integer.parseInt(content);
					if (eyr < 2020 || eyr > 2030) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
				case "hgt":
					String hgt = content.substring(content.length() - 2);
					int h = Integer.parseInt(content.substring(0, content.length() - 2));
					if (hgt.equals("in")) {
						if (h < 59 || h > 76) {
							System.out.println(key + ":" + content);
							return false;
						}
					} else if (hgt.equals("cm")) {
						if (h < 150 || h > 193) {
							System.out.println(key + ":" + content);
							return false;
						}
					}
					break;
				case "hcl":
					if (!content.matches("#(\\d|[a-f]){6}")) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
				case "ecl":
					if (!content.matches("((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))")) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
				case "pid":
					if (!content.matches("\\d{9}")) {
						System.out.println(key + ":" + content);
						return false;
					}
					break;
			}
		
		} catch (Exception e) {
			System.out.println("except: " + key + ":" + content);
			return false;
		}
		return true;
	}
}