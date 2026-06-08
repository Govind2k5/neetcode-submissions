class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String,List<String>> map = new HashMap<>();
        for (String s : strs){
            char[] chararray = s.toCharArray();
            Arrays.sort(chararray);
            String sortS = new String(chararray);
            map.putIfAbsent(sortS,new ArrayList<>());
            map.get(sortS).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
