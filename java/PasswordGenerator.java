import java.security.SecureRandom;
import java.util.Scanner;

public class PasswordGenerator {
    private static final String UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
    private static final String DIGITS = "0123456789";
    private static final String SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:,.<>?/";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o comprimento da senha: ");
        int length = scanner.nextInt();

        System.out.print("Incluir letras maiúsculas? (true/false): ");
        boolean useUpper = scanner.nextBoolean();

        System.out.print("Incluir letras minúsculas? (true/false): ");
        boolean useLower = scanner.nextBoolean();

        System.out.print("Incluir números? (true/false): ");
        boolean useDigits = scanner.nextBoolean();

        System.out.print("Incluir caracteres especiais? (true/false): ");
        boolean useSpecial = scanner.nextBoolean();

        scanner.close();

        String password = generatePassword(length, useUpper, useLower, useDigits, useSpecial);
        System.out.println("Senha gerada: " + password);
    }

    public static String generatePassword(int length, boolean useUpper, boolean useLower, boolean useDigits, boolean useSpecial) {
        if (length <= 0 || !(useUpper || useLower || useDigits || useSpecial)) {
            throw new IllegalArgumentException("Parâmetros inválidos para geração da senha.");
        }

        StringBuilder charPool = new StringBuilder();
        if (useUpper) charPool.append(UPPERCASE);
        if (useLower) charPool.append(LOWERCASE);
        if (useDigits) charPool.append(DIGITS);
        if (useSpecial) charPool.append(SPECIAL_CHARACTERS);

        SecureRandom random = new SecureRandom();
        StringBuilder password = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(charPool.length());
            password.append(charPool.charAt(index));
        }

        return password.toString();
    }
}
