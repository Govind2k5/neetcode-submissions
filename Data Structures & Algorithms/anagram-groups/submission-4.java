class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for (String s : strs){
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String sort = new String(arr);
            map.putIfAbsent(sort,new ArrayList<>());
            map.get(sort).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
