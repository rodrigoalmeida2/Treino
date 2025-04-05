
package LeetCode;
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        
        String pref = strs[0];
        int prefLen = pref.length();

        for (int i = 1; i < strs.length; i++) {
            String s = strs[i];
            while (prefLen > s.length() || !pref.equals(s.substring(0, prefLen))) {
                prefLen--;
                if (prefLen == 0) {
                    return "";
                }
                pref = pref.substring(0, prefLen);
            }
        }

        return pref;        
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Teste 1: Caso comum
        String[] test1 = {"flower", "flow", "flight"};
        System.out.println("Teste 1: " + solution.longestCommonPrefix(test1)); // Deve imprimir "fl"
        
        // Teste 2: Sem prefixo comum
        String[] test2 = {"dog", "racecar", "car"};
        System.out.println("Teste 2: " + solution.longestCommonPrefix(test2)); // Deve imprimir ""
        
        // Teste 3: Lista vazia
        String[] test3 = {"dog","dog","dog"};
        System.out.println("Teste 3: " + solution.longestCommonPrefix(test3)); // Deve imprimir ""
        
        // Teste 4: Strings iguais
        String[] test4 = {"apple", "apple", "apple"};
        System.out.println("Teste 4: " + solution.longestCommonPrefix(test4)); // Deve imprimir "apple"
        
        // Teste 5: Um elemento apenas
        String[] test5 = {"single"};
        System.out.println("Teste 5: " + solution.longestCommonPrefix(test5)); // Deve imprimir "single"
    }
}
